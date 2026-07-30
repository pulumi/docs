#!/usr/bin/env python3
"""Record one content-review article's verified claims to the S3 claims index.

The per-article worker (`.github/workflows/content-review-article.yml`) already
runs the docs-review claim pipeline over a synthetic whole-file diff and then
throws `.verified-claims.json` away. This script persists it instead: one JSON
object per page at `<CONTENT_REVIEW_CLAIMS_URI>/<slug>.json` (the same bucket
as the review ledger, under a `claims/` prefix), keyed by the entity keying
`merge-claims.py` stamps via `entity_key.py`.

The index is the foundation for event-driven freshness (pulumi/docs#20078
§4.1): the nightly `reverify-claims.py` job re-checks volatile entities
(versions, prices, limits) straight from the index — no re-extraction — and
release-triggered / contradiction-detection consumers join pages on
`entity_key`.

Writer discipline: ONLY this per-article worker writes the claims index. Its
runs are whole-page snapshots, so overwriting `<slug>.json` is always correct;
the pre-merge PR review sees partial-page diffs and must never write here (a
partial snapshot would silently shrink a page's claim set).

Snapshot rules:
  * Kept verdicts: verified | matches | contradicted | mismatch — the claims
    that say something about the page. `not-a-claim` and `unverifiable` are
    noise for index consumers and are dropped.
  * A verified artifact that is absent, unparseable, or degraded (zero
    verdicts WITH pipeline errors — e.g. the verifier never started) skips the
    upload entirely, preserving the page's previous snapshot. Zero verdicts
    with no errors is a genuinely claim-free page and uploads an empty
    snapshot.
  * Claims without an `entity_key` are persisted too — they're invisible to
    entity-keyed consumers but keep the snapshot a faithful record of the page.

Degrades gracefully like `record-review.py`: no CONTENT_REVIEW_CLAIMS_URI →
local artifact only; a failed upload warns and never fails the run.

Self-contained — run the smoke checks with `python3 record-claims.py --self-test`.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent

# Reuse slugify from select-articles.py (single source of truth), same
# import-by-path pattern as record-review.py.
_spec = importlib.util.spec_from_file_location(
    "select_articles", HERE / "select-articles.py"
)
_select = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_select)
slugify = _select.slugify

SCHEMA_VERSION = 1
# `framing-drift` persists: it's a decided source-vs-claim outcome (value
# accurate, published meaning drifted) the reverify lane should track, unlike
# `unverifiable`/`not-a-claim` which carry no decided state.
KEPT_VERDICTS = {"verified", "matches", "contradicted", "mismatch", "framing-drift"}

# Verdict fields carried into the snapshot, in output order.
CLAIM_FIELDS = [
    "claim_id", "entity_key", "volatile", "type", "text", "line_range",
    "verdict", "confidence", "evidence", "source",
]


def log(msg: str) -> None:
    print(f"record-claims: {msg}", file=sys.stderr)


def warn(msg: str) -> None:
    print(f"::warning::record-claims: {msg}", file=sys.stderr)


# ---- inputs -----------------------------------------------------------------


def load_queue_article(queue_path: Path) -> dict:
    data = json.loads(queue_path.read_text())
    articles = data.get("articles") or []
    if not articles:
        raise SystemExit(f"record-claims: no articles in {queue_path}")
    a = articles[0]
    path = a["path"]
    return {"path": path, "slug": a.get("slug") or slugify(path)}


def load_verified(verified_path: Path) -> dict | None:
    """The `.verified-claims.json` artifact, or None when absent/unparseable."""
    if not verified_path.is_file():
        return None
    try:
        doc = json.loads(verified_path.read_text())
    except (OSError, json.JSONDecodeError) as e:
        warn(f"verified-claims artifact unreadable ({e})")
        return None
    return doc if isinstance(doc, dict) else None


def head_commit(commit: str | None) -> str:
    """The snapshot's provenance commit; `--commit` injects it for tests."""
    if commit:
        return commit
    try:
        out = subprocess.run(
            ["git", "rev-parse", "HEAD"], capture_output=True, text=True, check=False,
        )
    except FileNotFoundError:
        return ""
    return out.stdout.strip() if out.returncode == 0 else ""


# ---- snapshot ----------------------------------------------------------------


def build_snapshot(article: dict, verified: dict, commit: str) -> dict:
    """The canonical claims-index object for one page."""
    kept = []
    verdicts = [v for v in (verified.get("verdicts") or []) if isinstance(v, dict)]
    for v in verdicts:
        if v.get("verdict") not in KEPT_VERDICTS:
            continue
        entry = {k: v.get(k) for k in CLAIM_FIELDS if k in v}
        entry.setdefault("entity_key", None)
        entry.setdefault("volatile", False)
        kept.append(entry)
    return {
        "schema_version": SCHEMA_VERSION,
        "path": article["path"],
        "slug": article["slug"],
        "commit": commit,
        "reviewed_at": datetime.now(timezone.utc).date().isoformat(),
        "model": verified.get("model"),
        "claims": kept,
        "meta": {
            "n_verdicts": len(verdicts),
            "n_kept": len(kept),
            "n_keyed": sum(1 for c in kept if c.get("entity_key")),
            "n_volatile": sum(1 for c in kept if c.get("volatile")),
        },
    }


def degraded(verified: dict | None) -> str | None:
    """Why this artifact must not overwrite the page's previous snapshot, or
    None when it's trustworthy. Zero verdicts + pipeline errors = the verifier
    never really ran (missing API key, uncaught exception); an upload would
    clobber a good snapshot with an empty one."""
    if verified is None:
        return "verified-claims artifact absent or unreadable"
    if not (verified.get("verdicts") or []) and (verified.get("errors") or []):
        return f"zero verdicts with pipeline errors: {'; '.join(str(e) for e in verified['errors'][:3])}"
    return None


# ---- outputs ----------------------------------------------------------------


def upload(snapshot: dict, slug: str, uri: str) -> None:
    key = f"{uri.rstrip('/')}/{slug}.json"
    try:
        subprocess.run(
            ["aws", "s3", "cp", "-", key],
            input=json.dumps(snapshot, indent=2) + "\n",
            text=True, check=True,
        )
        log(f"uploaded claims snapshot to {key}")
    except FileNotFoundError:
        warn("aws CLI not available; claims snapshot not uploaded")
    except subprocess.CalledProcessError as e:
        warn(f"claims snapshot upload failed for {slug} ({e})")


# ---- main -------------------------------------------------------------------


def run(args) -> int:
    article = load_queue_article(Path(args.queue))
    verified = load_verified(Path(args.verified))

    skip_reason = degraded(verified)
    if skip_reason:
        warn(f"{skip_reason}; keeping the page's previous snapshot (no upload)")
        return 0

    snapshot = build_snapshot(article, verified, head_commit(args.commit))
    out_path = Path(args.out)
    out_path.write_text(json.dumps(snapshot, indent=2) + "\n")
    m = snapshot["meta"]
    log(f"slug={article['slug']} kept={m['n_kept']}/{m['n_verdicts']} "
        f"keyed={m['n_keyed']} volatile={m['n_volatile']} -> {out_path}")

    uri = os.environ.get("CONTENT_REVIEW_CLAIMS_URI", "").strip()
    if uri:
        upload(snapshot, article["slug"], uri)
    else:
        warn("CONTENT_REVIEW_CLAIMS_URI unset; claims snapshot written locally only")
    return 0


def self_test() -> int:
    import tempfile

    failures = []

    def check(name, cond):
        if not cond:
            failures.append(name)
            print(f"FAIL: {name}", file=sys.stderr)
        else:
            print(f"ok: {name}")

    article = {"path": "content/docs/iac/concepts/stacks.md",
               "slug": "docs-iac-concepts-stacks"}
    verified = {
        "schema_version": 1,
        "model": "claude-sonnet-5",
        "verdicts": [
            {"claim_id": "c1", "type": "version", "text": "pulumi-gcp v8.2.0",
             "line_range": "L10", "entity_key": "version/pulumi-gcp",
             "volatile": True, "verdict": "verified", "confidence": "high",
             "evidence": "release notes", "source": "gh release view",
             "route": "pass1", "model_usage": {"turns": 2}},
            {"claim_id": "c2", "type": "behavior", "text": "pulumi up deploys",
             "line_range": "L20", "verdict": "verified", "confidence": "high",
             "evidence": "docs", "source": "repo:content/docs/cli.md"},
            {"claim_id": "c3", "type": "numerical", "text": ":latest tag",
             "line_range": "L30", "verdict": "not-a-claim", "confidence": "high",
             "evidence": "docker tag", "source": "pass0"},
            {"claim_id": "c4", "type": "numerical", "text": "price is $75",
             "line_range": "L40", "entity_key": "numerical/price",
             "volatile": True, "verdict": "contradicted", "confidence": "high",
             "evidence": "now $99", "source": "vendor page"},
            {"claim_id": "c5", "type": "feature", "text": "supports X",
             "line_range": "L50", "verdict": "unverifiable", "confidence": "low",
             "evidence": "paywalled", "source": "n/a"},
        ],
        "errors": [],
    }

    snap = build_snapshot(article, verified, "abc1234")
    check("keeps verified/contradicted, drops not-a-claim/unverifiable",
          [c["claim_id"] for c in snap["claims"]] == ["c1", "c2", "c4"])
    check("route/model_usage stripped from entries",
          all("route" not in c and "model_usage" not in c for c in snap["claims"]))
    check("unkeyed claim persists with null key",
          snap["claims"][1]["entity_key"] is None and snap["claims"][1]["volatile"] is False)
    check("meta counts", snap["meta"] == {"n_verdicts": 5, "n_kept": 3,
                                          "n_keyed": 2, "n_volatile": 2})
    check("provenance carried", snap["commit"] == "abc1234"
          and snap["path"] == article["path"] and snap["slug"] == article["slug"]
          and snap["model"] == "claude-sonnet-5" and bool(snap["reviewed_at"]))

    # Degradation rules.
    check("absent artifact -> skip", degraded(None) is not None)
    check("zero verdicts + errors -> skip (degraded run)",
          degraded({"verdicts": [], "errors": ["ANTHROPIC_API_KEY not set"]}) is not None)
    check("zero verdicts, no errors -> genuine empty snapshot uploads",
          degraded({"verdicts": [], "errors": []}) is None)
    check("normal artifact -> no skip", degraded(verified) is None)

    empty = build_snapshot(article, {"verdicts": [], "errors": []}, "")
    check("claim-free page yields empty claims list", empty["claims"] == []
          and empty["meta"]["n_kept"] == 0)

    with tempfile.TemporaryDirectory() as d:
        q = Path(d) / "queue.json"
        q.write_text(json.dumps({"articles": [{"path": "content/docs/iac/concepts/stacks/_index.md"}]}))
        a = load_queue_article(q)
        check("queue slug falls back to slugify", a["slug"] == "docs-iac-concepts-stacks")

    if failures:
        print(f"\n{len(failures)} failure(s)", file=sys.stderr)
        return 1
    print("\nall record-claims self-tests passed")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description="Record a page's verified claims to the S3 claims index.")
    p.add_argument("--queue", help="single-article queue JSON (.content-review-queue.json)")
    p.add_argument("--verified", default=".verified-claims.json",
                   help="verified-claims artifact from the pre-compute step")
    p.add_argument("--commit", help="inject the provenance commit (tests); default: git rev-parse HEAD")
    p.add_argument("--out", default=".content-review-claims.json",
                   help="local snapshot artifact path")
    p.add_argument("--self-test", action="store_true", help="run built-in smoke checks")
    args = p.parse_args()

    if args.self_test:
        return self_test()
    if not args.queue:
        p.error("--queue is required")
    return run(args)


if __name__ == "__main__":
    sys.exit(main())
