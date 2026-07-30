#!/usr/bin/env python3
"""Nightly re-verification of volatile claims from the S3 claims index.

Consumes the per-page claims snapshots `record-claims.py` persists (one JSON
object per page under the ledger bucket's `claims/` prefix) and re-checks the
*volatile* entities — version pins, prices, limits — straight from the index:
no page diff, no re-extraction, one verifier call per entity. This is the
event-driven-freshness consumer from pulumi/docs#20078 §4.1: a claim that
drifted (the provider released v9, the price changed) is caught within a
night instead of waiting for the page's next staleness-driven sweep.

How a stale finding flows (no new human burden, no prose generation):
  1. An entity re-verifies `contradicted`/`mismatch`.
  2. Every page asserting that entity gets a `stale_claims` marker written
     into its LEDGER object (`ledger/<slug>.json`) — evidence attached.
  3. `select-articles.py` adds a large additive boost for marked pages, so
     the next daily content-review sweep picks them up; the normal worker
     re-reviews the page, fixes it through the existing PR machinery, and
     its ledger/claims rewrites clear the marker automatically.

Selection (deterministic, stateless): volatile keyed entities are deduped
across pages (one verification per entity per night, fanned back out to all
pages asserting it), entities already marked stale are skipped (they're
waiting on a review, not on another check), the rest are sorted by entity
key and swept in day-rotated chunks of `--count` — days-since-epoch modulo
the chunk count picks tonight's chunk, so the whole volatile set is covered
every ceil(N/count) nights with no persisted cursor.

Verification reuses `verify-claims.py`'s per-claim machinery (routing +
agent-loop verifier) by module import; each entity's freshest claim record is
the input. `contradicted`/`mismatch` → stale; `verified`/`matches` → fresh;
anything else (`unverifiable`, errors) → inconclusive, reported but never
marked — a flaky check must not burn review-queue slots.

Writes `.claims-reverify-report.json` (plus `n_checked`/`n_stale`/`has_stale`
to $GITHUB_OUTPUT) and, when CONTENT_REVIEW_LEDGER_URI is set, uploads each
marked ledger object. Degrades gracefully: no API key, no claims dir, or no
volatile entities → empty report, exit 0.

Usage:
    reverify-claims.py --claims-dir .claims-cache --ledger-dir .ledger-cache \
        --count 25 [--today YYYY-MM-DD] [--repo-root .] [--model <m>]
        [--out .claims-reverify-report.json] [--dry-run]

Self-contained smoke checks: `python3 reverify-claims.py --self-test`.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parents[2]
VERIFY_CLAIMS = HERE / ".claude/commands/docs-review/scripts/verify-claims.py"

SCHEMA_VERSION = 1
DEFAULT_COUNT = 25
MAX_CONCURRENCY = 8
STALE_VERDICTS = {"contradicted", "mismatch", "framing-drift"}
FRESH_VERDICTS = {"verified", "matches"}


def log(msg: str) -> None:
    print(f"reverify-claims: {msg}", file=sys.stderr)


def warn(msg: str) -> None:
    print(f"::warning::reverify-claims: {msg}", file=sys.stderr)


def _load_verify_claims():
    """Import verify-claims.py by path (hyphenated filename; main() is guarded,
    so importing has no side effects). Same pattern record-review.py uses for
    select-articles.py."""
    spec = importlib.util.spec_from_file_location("verify_claims", VERIFY_CLAIMS)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ---- index loading -----------------------------------------------------------


def load_snapshots(claims_dir: Path) -> list[dict]:
    """All parseable per-page claims snapshots under the synced claims/ prefix."""
    out: list[dict] = []
    if not claims_dir.is_dir():
        return out
    for f in sorted(claims_dir.glob("*.json")):
        try:
            snap = json.loads(f.read_text())
        except (OSError, json.JSONDecodeError):
            warn(f"unreadable claims snapshot {f}")
            continue
        if isinstance(snap, dict) and snap.get("path") and snap.get("slug"):
            out.append(snap)
    return out


def volatile_entities(snapshots: list[dict]) -> dict[str, list[dict]]:
    """{entity_key: [assertion, ...]} over every volatile keyed claim.

    Each assertion carries the claim record plus its page provenance
    (path/slug/reviewed_at), so a stale verdict can fan back out to every
    page asserting the entity."""
    entities: dict[str, list[dict]] = {}
    for snap in snapshots:
        for c in snap.get("claims") or []:
            if not isinstance(c, dict) or not c.get("entity_key") or not c.get("volatile"):
                continue
            entities.setdefault(c["entity_key"], []).append({
                "claim": c,
                "path": snap["path"],
                "slug": snap["slug"],
                "reviewed_at": snap.get("reviewed_at") or "",
            })
    return entities


def already_marked(key: str, assertions: list[dict], ledger: dict[str, dict]) -> bool:
    """True when some page asserting this entity already carries its stale
    marker — the entity is waiting on a review, not on another check."""
    for a in assertions:
        entry = ledger.get(a["path"]) or {}
        for m in entry.get("stale_claims") or []:
            if isinstance(m, dict) and m.get("entity_key") == key:
                return True
    return False


def tonight_chunk(keys: list[str], count: int, today: date) -> list[str]:
    """Day-rotated chunk of the sorted entity keys: full coverage every
    ceil(N/count) nights, deterministic from the date alone."""
    if not keys or count <= 0:
        return []
    n_chunks = -(-len(keys) // count)  # ceil
    idx = today.toordinal() % n_chunks
    return keys[idx * count:(idx + 1) * count]


def representative(assertions: list[dict]) -> dict:
    """The freshest assertion's claim record — the input to the verifier."""
    return max(assertions, key=lambda a: a["reviewed_at"])["claim"]


# ---- ledger markers ----------------------------------------------------------


def load_ledger(ledger_dir: Path) -> dict[str, dict]:
    entries: dict[str, dict] = {}
    if not ledger_dir.is_dir():
        return entries
    for f in sorted(ledger_dir.glob("*.json")):
        try:
            entry = json.loads(f.read_text())
        except (OSError, json.JSONDecodeError):
            continue
        if isinstance(entry, dict) and entry.get("path"):
            entry["_file"] = str(f)
            entries[entry["path"]] = entry
    return entries


def apply_markers(ledger: dict[str, dict], stale: list[dict], today: date) -> dict[str, dict]:
    """Fold stale entity verdicts into the affected pages' ledger entries.

    Returns {slug: updated entry (without bookkeeping keys)} for every entry
    that changed. Idempotent: a marker for an already-marked entity_key is
    replaced, not duplicated. A page missing from the ledger (shouldn't
    happen — the same worker run writes both objects) gets a minimal entry so
    the selector can still see the marker."""
    changed: dict[str, dict] = {}
    for s in stale:
        marker = {
            "entity_key": s["entity_key"],
            "verdict": s["verdict"],
            "evidence": s.get("evidence") or "",
            "source": s.get("source") or "",
            "checked_at": today.isoformat(),
        }
        for page in s["pages"]:
            entry = ledger.get(page["path"])
            if entry is None:
                warn(f"no ledger entry for {page['path']}; creating a minimal one")
                entry = {"path": page["path"], "slug": page["slug"]}
                ledger[page["path"]] = entry
            markers = [m for m in (entry.get("stale_claims") or [])
                       if isinstance(m, dict) and m.get("entity_key") != s["entity_key"]]
            markers.append(marker)
            entry["stale_claims"] = markers
            slug = entry.get("slug") or page["slug"]
            changed[slug] = {k: v for k, v in entry.items() if k != "_file"}
    return changed


def upload_entry(entry: dict, slug: str, uri: str) -> None:
    import subprocess
    key = f"{uri.rstrip('/')}/{slug}.json"
    try:
        subprocess.run(
            ["aws", "s3", "cp", "-", key],
            input=json.dumps(entry, indent=2) + "\n",
            text=True, check=True,
        )
        log(f"uploaded stale-claims marker to {key}")
    except FileNotFoundError:
        warn("aws CLI not available; ledger markers not uploaded")
    except subprocess.CalledProcessError as e:
        warn(f"marker upload failed for {slug} ({e})")


# ---- outputs -----------------------------------------------------------------


def write_outputs(report: dict) -> None:
    gh_out = os.environ.get("GITHUB_OUTPUT")
    if not gh_out:
        return
    with open(gh_out, "a") as fh:
        fh.write(f"n_checked={report['meta']['n_checked']}\n")
        fh.write(f"n_stale={report['meta']['n_stale']}\n")
        fh.write(f"has_stale={'true' if report['meta']['n_stale'] else 'false'}\n")


def finish(report: dict, out_path: Path) -> int:
    out_path.write_text(json.dumps(report, indent=2) + "\n")
    m = report["meta"]
    log(f"checked={m['n_checked']} stale={m['n_stale']} fresh={m['n_fresh']} "
        f"inconclusive={m['n_inconclusive']} (volatile entities={m['n_entities']}) -> {out_path}")
    write_outputs(report)
    return 0


# ---- main --------------------------------------------------------------------


def run(args) -> int:
    today = None
    if args.today:
        today = datetime.strptime(args.today, "%Y-%m-%d").date()
    today = today or datetime.now(timezone.utc).date()

    report = {
        "schema_version": SCHEMA_VERSION,
        "checked_at": today.isoformat(),
        "entities": [],
        "meta": {"n_snapshots": 0, "n_entities": 0, "n_due": 0, "n_checked": 0,
                 "n_stale": 0, "n_fresh": 0, "n_inconclusive": 0},
    }
    out_path = Path(args.out)

    # The meta block doubles as the health observation consumed by
    # signal-health.py's reverify signal: `skipped` distinguishes "couldn't
    # run" (degraded) from the quiet-night n_due=0 (healthy), and an
    # all-inconclusive n_checked is the broken-verifier tell. Keep those
    # semantics intact when touching the early-exit paths below.
    snapshots = load_snapshots(Path(args.claims_dir))
    report["meta"]["n_snapshots"] = len(snapshots)
    if not snapshots:
        log("no claims snapshots; nothing to re-verify")
        report["meta"]["skipped"] = "no_snapshots"
        return finish(report, out_path)

    ledger = load_ledger(Path(args.ledger_dir))
    entities = volatile_entities(snapshots)
    report["meta"]["n_entities"] = len(entities)

    unmarked = sorted(k for k, v in entities.items() if not already_marked(k, v, ledger))
    keys = tonight_chunk(unmarked, args.count, today)
    report["meta"]["n_due"] = len(keys)
    if not keys:
        log("no volatile entities due tonight")
        return finish(report, out_path)

    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key and not args.dry_run:
        warn("ANTHROPIC_API_KEY not set; re-verification skipped")
        report["meta"]["skipped"] = "no_api_key"
        return finish(report, out_path)

    vc = _load_verify_claims()
    repo_root = Path(args.repo_root).resolve()

    def check_entity(key: str) -> dict:
        claim = dict(representative(entities[key]))
        claim["__id"] = key
        claim["__route"] = vc.route_claim(claim, {})
        rec, err = vc.process_claim(api_key, claim, {}, args.model, repo_root, args.dry_run)
        return {
            "entity_key": key,
            "verdict": rec.get("verdict"),
            "confidence": rec.get("confidence"),
            "evidence": rec.get("evidence"),
            "source": rec.get("source"),
            "route": rec.get("route"),
            "error": err,
            "pages": [{"path": a["path"], "slug": a["slug"]} for a in entities[key]],
        }

    with ThreadPoolExecutor(max_workers=min(MAX_CONCURRENCY, len(keys))) as pool:
        results = list(pool.map(check_entity, keys))

    stale = [r for r in results if r["verdict"] in STALE_VERDICTS]
    fresh = [r for r in results if r["verdict"] in FRESH_VERDICTS]
    report["entities"] = results
    report["meta"]["n_checked"] = len(results)
    report["meta"]["n_stale"] = len(stale)
    report["meta"]["n_fresh"] = len(fresh)
    report["meta"]["n_inconclusive"] = len(results) - len(stale) - len(fresh)

    if stale:
        changed = apply_markers(ledger, stale, today)
        uri = os.environ.get("CONTENT_REVIEW_LEDGER_URI", "").strip()
        for slug, entry in sorted(changed.items()):
            local = Path(args.ledger_dir) / f"{slug}.json"
            local.parent.mkdir(parents=True, exist_ok=True)
            local.write_text(json.dumps(entry, indent=2) + "\n")
            if uri and not args.dry_run:
                upload_entry(entry, slug, uri)
        if not uri:
            warn("CONTENT_REVIEW_LEDGER_URI unset; markers written locally only")

    return finish(report, out_path)


# ---- self-test ---------------------------------------------------------------


def self_test() -> int:
    failures = []

    def check(name, cond):
        if not cond:
            failures.append(name)
            print(f"FAIL: {name}", file=sys.stderr)
        else:
            print(f"ok: {name}")

    def snap(slug, reviewed_at, *claims):
        return {"schema_version": 1, "path": f"content/docs/{slug}.md",
                "slug": f"docs-{slug}", "reviewed_at": reviewed_at,
                "claims": list(claims)}

    ver = {"entity_key": "version/pulumi-gcp", "volatile": True, "type": "version",
           "text": "pulumi-gcp v8.2.0", "line_range": "L10", "verdict": "verified"}
    price = {"entity_key": "numerical/team-plan-price", "volatile": True,
             "type": "numerical", "text": "the Team plan costs $75", "line_range": "L5",
             "verdict": "verified"}
    stable = {"entity_key": "api-surface/versioning", "volatile": False,
              "type": "api-surface", "text": "`versioning` argument", "line_range": "L7",
              "verdict": "verified"}
    unkeyed = {"entity_key": None, "volatile": True, "type": "numerical",
               "text": "40x", "line_range": "L9", "verdict": "verified"}

    snaps = [snap("a", "2026-07-01", ver, stable),
             snap("b", "2026-07-05", dict(ver, text="pulumi-gcp v8.3.0"), price, unkeyed)]

    ents = volatile_entities(snaps)
    check("volatile keyed entities only",
          set(ents) == {"version/pulumi-gcp", "numerical/team-plan-price"})
    check("entity fans out across pages", len(ents["version/pulumi-gcp"]) == 2)
    check("representative is the freshest assertion",
          representative(ents["version/pulumi-gcp"])["text"] == "pulumi-gcp v8.3.0")

    # Chunk rotation: deterministic, complete coverage across consecutive days.
    keys = [f"k{i}" for i in range(5)]
    d0 = date(2026, 7, 6)
    chunks = [tonight_chunk(keys, 2, date.fromordinal(d0.toordinal() + i)) for i in range(3)]
    check("chunks cover all keys over the rotation",
          sorted(k for ch in chunks for k in ch) == sorted(keys))
    check("same day -> same chunk", tonight_chunk(keys, 2, d0) == chunks[0])
    check("count of zero -> empty chunk", tonight_chunk(keys, 0, d0) == [])
    check("empty keys -> empty chunk", tonight_chunk([], 3, d0) == [])

    # Markers: fan-out, idempotence, minimal entry for a ledger gap.
    ledger = {"content/docs/a.md": {"path": "content/docs/a.md", "slug": "docs-a",
                                    "status": "clean", "_file": "x"}}
    stale = [{"entity_key": "version/pulumi-gcp", "verdict": "contradicted",
              "evidence": "v9.0 released", "source": "gh release view",
              "pages": [{"path": "content/docs/a.md", "slug": "docs-a"},
                        {"path": "content/docs/b.md", "slug": "docs-b"}]}]
    today = date(2026, 7, 9)
    changed = apply_markers(ledger, stale, today)
    check("marker fans out to both pages", set(changed) == {"docs-a", "docs-b"})
    check("existing entry keeps its fields",
          changed["docs-a"]["status"] == "clean" and "_file" not in changed["docs-a"])
    check("marker shape", changed["docs-a"]["stale_claims"][0] == {
        "entity_key": "version/pulumi-gcp", "verdict": "contradicted",
        "evidence": "v9.0 released", "source": "gh release view",
        "checked_at": "2026-07-09"})
    check("minimal entry created for ledger gap",
          changed["docs-b"]["path"] == "content/docs/b.md")

    changed2 = apply_markers(ledger, stale, today)
    check("re-marking is idempotent",
          len(changed2["docs-a"]["stale_claims"]) == 1)

    check("already_marked sees the marker",
          already_marked("version/pulumi-gcp", ents["version/pulumi-gcp"], ledger))
    check("already_marked ignores other entities",
          not already_marked("numerical/team-plan-price",
                             ents["numerical/team-plan-price"], ledger))

    # Health-observation meta: the early-exit paths must say why they stopped
    # (signal-health.py's reverify signal reads these fields).
    import tempfile

    def run_report(d: Path, extra_env_unset: list[str]) -> dict:
        saved = {k: os.environ.pop(k) for k in extra_env_unset if k in os.environ}
        try:
            argv = ["--claims-dir", str(d / "claims"), "--ledger-dir", str(d / "ledger"),
                    "--out", str(d / "report.json"), "--today", "2026-07-06"]
            args = build_parser().parse_args(argv)
            run(args)
            return json.loads((d / "report.json").read_text())
        finally:
            os.environ.update(saved)

    with tempfile.TemporaryDirectory() as tmp:
        d = Path(tmp)
        (d / "claims").mkdir()
        (d / "ledger").mkdir()
        rep = run_report(d, [])
        check("empty claims dir -> skipped=no_snapshots",
              rep["meta"]["skipped"] == "no_snapshots" and rep["meta"]["n_due"] == 0)

        (d / "claims" / "docs-a.json").write_text(json.dumps(snap("a", "2026-07-01", ver)))
        rep = run_report(d, ["ANTHROPIC_API_KEY"])
        check("due entities without API key -> skipped=no_api_key",
              rep["meta"]["skipped"] == "no_api_key" and rep["meta"]["n_due"] == 1)

    if failures:
        print(f"\n{len(failures)} failure(s)", file=sys.stderr)
        return 1
    print("\nall reverify-claims self-tests passed")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--claims-dir", default=".claims-cache",
                   help="local sync of the claims/ prefix")
    p.add_argument("--ledger-dir", default=".ledger-cache",
                   help="local sync of the ledger/ prefix (markers are written here)")
    p.add_argument("--count", type=int, default=DEFAULT_COUNT,
                   help="entities to re-verify tonight (chunk size of the rotation)")
    p.add_argument("--today", help="override today's date YYYY-MM-DD (testing)")
    p.add_argument("--repo-root", default=str(HERE), help="repo root for the verifier's read_file")
    p.add_argument("--model", default=None, help="verifier model (default: verify-claims.py's)")
    p.add_argument("--out", default=".claims-reverify-report.json")
    p.add_argument("--dry-run", action="store_true",
                   help="no API calls, no uploads; placeholder verdicts (testing)")
    p.add_argument("--self-test", action="store_true", help="run built-in smoke checks")
    return p


def main() -> int:
    args = build_parser().parse_args()

    if args.self_test:
        return self_test()
    if args.model is None:
        args.model = _load_verify_claims().DEFAULT_MODEL
    return run(args)


if __name__ == "__main__":
    sys.exit(main())
