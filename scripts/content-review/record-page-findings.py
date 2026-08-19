#!/usr/bin/env python3
"""Persist one page's review findings as structured data.

Until this existed, a review's findings survived in exactly two forms:

  * the ledger's `skipped_findings` — an integer, with no record of WHAT
  * the PR body — prose, written for a human

and `build-glowup-backlog.py` recovered them months later by downloading the
PR body and parsing the markdown back into data. That round trip is the
problem this closes:

  * the PR body became load-bearing data, so anyone tidying a table silently
    changed what the glow-up lane would act on;
  * heading-based extraction fails silently — rename a section and the backlog
    just comes back empty;
  * only the LATEST PR is recoverable (branches are reused, so older reviews
    cannot be found), which quietly discarded every earlier review's findings;
  * GitHub became a hard dependency for reading our own bookkeeping.

Nothing new is asked of the model. The findings themselves already exist as
JSON — they are the deterministic pre-step artifacts that `compose-pr-body.py`
stubs the PR body FROM, and this script reuses that module's `collect()` so the
two can never drift on what counts as a finding. The only model-supplied part
is the DISPOSITION, and that is already structured too: the verdict's
`applied[]` array records what was fixed. Everything found and not applied is
the difference between the two.

What is deliberately NOT captured is the model's one-line reason for deferring,
which exists only as PR-body prose. `build-glowup-backlog.py` still reads the
PR body for that, and merges it onto this spine — so this file is strictly more
than the backlog had, never less, and the prose stays enrichment rather than
the system of record.

Output (uploaded to the ledger bucket's `findings/` prefix, beside `ledger/`
and `claims/`):

    {"schema_version": 1, "slug": ..., "path": ..., "reviewed_at": ...,
     "commit": ..., "verdict": "fixed|clean|skipped",
     "counts": {"total": N, "applied": N, "deferred": N},
     "findings": [{"id": "f3", "label": ..., "source": ..., "detail": ...,
                   "fix_candidate": bool, "applied": bool}, ...]}

Whole-page snapshot semantics, same as `record-claims.py`: a review sees the
entire page, so overwriting `<slug>.json` is always correct.

Usage:
    record-page-findings.py --queue .content-review-queue.json \
        --verdict .content-review-verdict.json --out .page-findings.json \
        [--verified-claims .verified-claims.json] [--vale-findings ...] \
        [--readthrough ...] [--frontmatter ...] [--uri s3://.../findings/]
    record-page-findings.py --self-test
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCHEMA_VERSION = 1


def log(msg: str) -> None:
    print(f"record-page-findings: {msg}", file=sys.stderr)


def warn(msg: str) -> None:
    print(f"::warning::record-page-findings: {msg}", file=sys.stderr)


def _compose():
    """compose-pr-body.py by path — its collect() is the single definition of
    'what counts as a finding', and duplicating it here would guarantee drift
    between the PR body and this record."""
    spec = importlib.util.spec_from_file_location(
        "compose_pr_body", HERE / "compose-pr-body.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def read_json(path: Path | None):
    if path is None or not path.is_file():
        return None
    try:
        return json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as e:
        warn(f"{path} unreadable ({e})")
        return None


def applied_sources(verdict: dict | None) -> list[str]:
    """The `source` pointer of every applied fix, lowercased for matching."""
    out: list[str] = []
    for a in ((verdict or {}).get("applied") or []):
        if isinstance(a, dict) and a.get("source"):
            out.append(str(a["source"]).strip().lower())
    return out


def mark_applied(findings: list[dict], sources: list[str]) -> list[dict]:
    """Flag each finding the verdict claims to have fixed.

    Matching is substring-either-way on the finding's `source` and `label`,
    because `applied[].source` is a human-written pointer ("Claim (c28)",
    "vale L48") rather than a key. That is loose, and deliberately so: a false
    POSITIVE drops one item from a glow-up backlog, while a false negative
    leaves an already-fixed finding in it forever, re-proposing work that is
    done. Neither is good, but a backlog that cannot be drained is the one
    that erodes trust in the lane.
    """
    out = []
    for i, f in enumerate(findings):
        hay = f"{f.get('source', '')} {f.get('label', '')}".strip().lower()
        hit = any(s and (s in hay or hay[:80] in s) for s in sources)
        out.append({
            "id": f"f{i + 1}",
            "label": f.get("label", ""),
            "source": f.get("source", ""),
            "detail": f.get("detail", ""),
            "fix_candidate": bool(f.get("fix")),
            "applied": hit,
        })
    return out


def head_commit(repo_root: Path) -> str:
    try:
        r = subprocess.run(["git", "-C", str(repo_root), "rev-parse", "HEAD"],
                           capture_output=True, text=True, check=False)
        return r.stdout.strip() if r.returncode == 0 else ""
    except OSError:
        return ""


def build(queue: dict, verdict: dict | None, artifacts: dict,
          repo_root: Path) -> dict | None:
    articles = queue.get("articles") or []
    if not articles:
        warn("queue has no article; nothing to record")
        return None
    art = articles[0]
    cpb = _compose()
    findings, _errors = cpb.collect(
        artifacts.get("verified"), artifacts.get("vale"),
        artifacts.get("readthrough"), artifacts.get("frontmatter"))
    marked = mark_applied(findings, applied_sources(verdict))
    n_applied = sum(1 for f in marked if f["applied"])
    return {
        "schema_version": SCHEMA_VERSION,
        "slug": art.get("slug", ""),
        "path": art.get("path", ""),
        "reviewed_at": datetime.now(timezone.utc).date().isoformat(),
        "commit": head_commit(repo_root),
        "verdict": (verdict or {}).get("verdict"),
        "counts": {"total": len(marked), "applied": n_applied,
                   "deferred": len(marked) - n_applied},
        "findings": marked,
    }


def upload(record: dict, uri: str) -> None:
    key = f"{uri.rstrip('/')}/{record['slug']}.json"
    body = json.dumps(record, indent=2) + "\n"
    proc = subprocess.run(["aws", "s3", "cp", "-", key, "--quiet"],
                          input=body, text=True, capture_output=True)
    if proc.returncode != 0:
        warn(f"upload to {key} failed: {proc.stderr.strip()[:200]}")
    else:
        log(f"uploaded findings record to {key}")


def self_test() -> int:
    passes, failures = 0, []

    def check(label, ok):
        nonlocal passes
        if ok:
            passes += 1
            print(f"  ok: {label}")
        else:
            failures.append(label)
            print(f"  FAIL: {label}")

    check("applied_sources reads the verdict array",
          applied_sources({"applied": [{"source": "Claim (c28)"}, {"source": "vale L48"}]})
          == ["claim (c28)", "vale l48"])
    check("a verdict with no applied[] yields nothing", applied_sources({}) == [])
    check("a None verdict is not fatal", applied_sources(None) == [])

    findings = [
        {"label": "Claim (c28, L89): version is 3.157.0", "source": "gh release view", "fix": True},
        {"label": "Vale filler (L48): Don't start with 'There are'.", "source": "vale", "fix": False},
        {"label": "Readthrough missing-step (L636)", "source": "readthrough pass", "fix": True},
    ]
    marked = mark_applied(findings, ["claim (c28, l89): version is 3.157.0"])
    check("the applied finding is flagged", marked[0]["applied"] is True)
    check("the others are not", [f["applied"] for f in marked[1:]] == [False, False])
    check("ids are stable and 1-based", [f["id"] for f in marked] == ["f1", "f2", "f3"])
    check("fix_candidate survives from collect()",
          [f["fix_candidate"] for f in marked] == [True, False, True])
    check("nothing applied -> everything deferred",
          all(not f["applied"] for f in mark_applied(findings, [])))

    # A deferred finding is the whole point of the record: it must survive
    # even when the verdict fixed nothing at all.
    empty = mark_applied(findings, [])
    check("deferred findings are recorded, not dropped", len(empty) == 3)

    print(f"\n{passes} passed, {len(failures)} failed")
    return 1 if failures else 0


def main() -> int:
    p = argparse.ArgumentParser(description="Persist a page's review findings as JSON.")
    p.add_argument("--queue", default=".content-review-queue.json")
    p.add_argument("--verdict", default=".content-review-verdict.json")
    p.add_argument("--verified-claims", default=".verified-claims.json")
    p.add_argument("--vale-findings", default=".vale-findings.json")
    p.add_argument("--readthrough", default=".readthrough-findings.json")
    p.add_argument("--frontmatter", default=".frontmatter-validation.json")
    p.add_argument("--repo-root", default=".")
    p.add_argument("--out", default=".page-findings.json")
    p.add_argument("--uri", default="", help="s3://bucket/findings/ (skipped when empty)")
    p.add_argument("--self-test", action="store_true")
    args = p.parse_args()
    if args.self_test:
        return self_test()

    queue = read_json(Path(args.queue))
    if not isinstance(queue, dict):
        warn(f"{args.queue} missing or unreadable; nothing recorded")
        return 0
    record = build(
        queue, read_json(Path(args.verdict)),
        {"verified": read_json(Path(args.verified_claims)),
         "vale": read_json(Path(args.vale_findings)),
         "readthrough": read_json(Path(args.readthrough)),
         "frontmatter": read_json(Path(args.frontmatter))},
        Path(args.repo_root))
    if record is None:
        return 0
    Path(args.out).write_text(json.dumps(record, indent=2) + "\n")
    c = record["counts"]
    log(f"slug={record['slug']} findings={c['total']} "
        f"applied={c['applied']} deferred={c['deferred']} -> {args.out}")
    if args.uri:
        upload(record, args.uri)
    return 0


if __name__ == "__main__":
    sys.exit(main())
