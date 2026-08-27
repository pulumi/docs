#!/usr/bin/env python3
"""Tests for select-glowup.py (glow-up lane selection).

Same standalone harness style as test_select_articles.py: run the script as a
subprocess against a throwaway corpus + ledger fixtures with --no-gh/--today,
parse the queue, assert. No git history needed — glow-up selection reads only
the ledger and the working tree.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPT = HERE / "select-glowup.py"


def glowup_cap() -> int:
    """GLOWUP_MAX_OPEN_PRS read from the script under test, so the boundary
    cases below follow the knob instead of pinning a stale literal."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("select_glowup", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return int(mod.GLOWUP_MAX_OPEN_PRS)
TODAY = "2026-08-18"

_failures: list[str] = []
_passes = 0


def check(cond: bool, msg: str) -> None:
    global _passes
    if cond:
        _passes += 1
    else:
        _failures.append(msg)
        print(f"  FAIL: {msg}", file=sys.stderr)


PAGE = "---\ntitle: T\n---\n\nBody.\n"
TIERS = """\
tiers:
  - prefix: content/docs/generated/
    tier: 0
  - prefix: content/docs/concepts/
    tier: 1
  - prefix: content/docs/esc/
    tier: 2
"""

A = "content/docs/concepts/alpha.md"
B = "content/docs/concepts/beta.md"
C = "content/docs/esc/gamma.md"
GEN = "content/docs/generated/cli.md"
STUB = "content/docs/misc/stub.md"


def make_repo(tmp: Path) -> Path:
    repo = tmp / "repo"
    for rel in (A, B, C, GEN):
        f = repo / rel
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(PAGE)
    (repo / STUB).parent.mkdir(parents=True, exist_ok=True)
    (repo / STUB).write_text("---\nredirect_to: /docs/concepts/alpha/\n---\n")
    return repo


def write_ledger(ledger: Path, path: str, **kw) -> None:
    ledger.mkdir(parents=True, exist_ok=True)
    slug = path.removeprefix("content/").removesuffix(".md").replace("/", "-")
    entry = {"path": path, "slug": slug, "reviewed_at": "2026-08-01",
             "status": "reviewed", "lane": "priority", "pr_number": 100,
             "fixes": 1, "skipped_findings": 0, "attempts": 0, **kw}
    (ledger / f"{slug}.json").write_text(json.dumps(entry, indent=2) + "\n")


def run_select(repo: Path, tiers: Path, ledger: Path, *extra: str) -> dict:
    out = repo / ".glowup-queue.json"
    env = {k: v for k, v in os.environ.items() if k != "GITHUB_OUTPUT"}
    proc = subprocess.run(
        [sys.executable, str(SCRIPT), "--no-gh", "--today", TODAY,
         "--repo-root", str(repo), "--tiers", str(tiers),
         "--ledger-dir", str(ledger), "--out", str(out), *extra],
        capture_output=True, text=True, env=env,
    )
    check(proc.returncode == 0, f"exit 0 (stderr: {proc.stderr.strip()[:200]})")
    return json.loads(out.read_text()) if out.is_file() else {}


def main() -> int:
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        repo = make_repo(tmp)
        tiers = tmp / "tiers.yaml"
        tiers.write_text(TIERS)

        print("ranking: more banked findings wins; queue carries the glow-up fields")
        led = tmp / "ledger-rank"
        write_ledger(led, A, skipped_findings=5, pr_number=111)
        write_ledger(led, B, skipped_findings=2)
        q = run_select(repo, tiers, led, "--count", "1")
        check(q["count"] == 1, f"one pick (got {q['count']})")
        art = q["articles"][0]
        check(art["path"] == A, f"most-banked page wins (got {art['path']})")
        check(art["mode"] == "glowup" and art["lane"] == "glowup", "mode/lane stamped")
        check(art["slug"] == "docs-concepts-alpha", f"slug derived (got {art['slug']})")
        check(art["source_pr_number"] == 111, "prior PR pointer carried for the backlog")
        check(art["skipped_findings"] == 5, "banked count carried")
        check(art["stale_claim_markers"] == [] and art["stale_claims"] == 0,
              "marker fields present (empty) so record-review's rebuild can't drop them")

        print("stale-claim markers ride the glow-up queue (carry-forward safety)")
        led_m = tmp / "ledger-markers"
        marker = {"entity_key": "version/x", "verdict": "contradicted",
                  "unresolved_reviews": 1}
        write_ledger(led_m, A, skipped_findings=3, stale_claims=[marker])
        qm = run_select(repo, tiers, led_m, "--count", "1")
        check(qm["articles"][0]["stale_claim_markers"] == [marker]
              and qm["articles"][0]["stale_claims"] == 1,
              "ledger markers carried in full on the glow-up article")
        q2 = run_select(repo, tiers, led, "--count", "1")
        check(q2["articles"][0]["path"] == A, "selection is deterministic")

        print("clarity_flag boost outranks a slightly larger plain backlog")
        led2 = tmp / "ledger-clarity"
        write_ledger(led2, A, skipped_findings=3)
        write_ledger(led2, B, skipped_findings=2, clarity_flag=True)
        q = run_select(repo, tiers, led2, "--count", "2")
        check(q["articles"][0]["path"] == B,
              f"clarity-flagged page tops the queue (got {q['articles'][0]['path']})")
        check(q["articles"][0]["clarity_flag"] is True, "clarity_flag carried")

        print("exclusions: no banked signal, tier-0, stubs, cooldown")
        led3 = tmp / "ledger-excl"
        write_ledger(led3, A, skipped_findings=0)                    # nothing banked
        write_ledger(led3, GEN, skipped_findings=9)                  # tier-0
        write_ledger(led3, STUB, skipped_findings=9)                 # redirect stub
        write_ledger(led3, B, skipped_findings=4, status="glowup",
                     reviewed_at="2026-08-10")                       # cooldown (8 days)
        write_ledger(led3, C, skipped_findings=1)
        q = run_select(repo, tiers, led3, "--count", "10")
        paths = [a["path"] for a in q["articles"]]
        check(paths == [C], f"only the eligible page selected (got {paths})")

        print("a degraded glow-up does not start the cooldown (#20984)")
        # The backlog never reached the model, so nothing was executed and
        # nothing declined; record-review carried the banked count forward and
        # flagged it. The page is still owed its rehab.
        led_deg = tmp / "ledger-glowup-degraded"
        write_ledger(led_deg, B, skipped_findings=17, clarity_flag=True,
                     status="glowup", reviewed_at="2026-08-10",
                     fixes=0, glowup_degraded=True)
        q = run_select(repo, tiers, led_deg, "--count", "10")
        check([a["path"] for a in q["articles"]] == [B],
              "degraded glow-up stays selectable inside the cooldown window")

        print("the degraded exemption is bounded, not an unbounded re-select loop")
        led_cap = tmp / "ledger-glowup-degraded-capped"
        write_ledger(led_cap, B, skipped_findings=17, clarity_flag=True,
                     status="glowup", reviewed_at="2026-08-10",
                     fixes=0, glowup_degraded=True, glowup_degraded_runs=2)
        check(run_select(repo, tiers, led_cap, "--count", "10")["articles"] == [],
              "past the cap a degraded page serves the normal cooldown")
        led_under = tmp / "ledger-glowup-degraded-under-cap"
        write_ledger(led_under, B, skipped_findings=17, clarity_flag=True,
                     status="glowup", reviewed_at="2026-08-10",
                     fixes=0, glowup_degraded=True, glowup_degraded_runs=1)
        check([a["path"] for a in
               run_select(repo, tiers, led_under, "--count", "10")["articles"]] == [B],
              "under the cap it is still exempt")

        print("the durable PR pointer reaches the worker when pr_number is 0")
        led_ptr = tmp / "ledger-last-pr"
        write_ledger(led_ptr, A, skipped_findings=4, pr_number=0, last_pr_number=19885)
        q = run_select(repo, tiers, led_ptr, "--count", "10")
        check(q["articles"][0]["source_pr_number"] == 19885,
              "source_pr_number falls back to last_pr_number")
        led_both = tmp / "ledger-both-prs"
        write_ledger(led_both, A, skipped_findings=4, pr_number=222, last_pr_number=111)
        check(run_select(repo, tiers, led_both, "--count", "10")
              ["articles"][0]["source_pr_number"] == 222,
              "this review's own PR still wins when it opened one")

        print("a glow-up that did work still starts the cooldown")
        led_did = tmp / "ledger-glowup-executed"
        write_ledger(led_did, B, skipped_findings=1, status="glowup",
                     reviewed_at="2026-08-10", fixes=4, glowup_degraded=False)
        check(run_select(repo, tiers, led_did, "--count", "10")["articles"] == [],
              "executed glow-up excluded by the cooldown")
        led_dec = tmp / "ledger-glowup-declined"
        write_ledger(led_dec, B, skipped_findings=3, status="glowup",
                     reviewed_at="2026-08-10", fixes=0, glowup_degraded=False)
        check(run_select(repo, tiers, led_dec, "--count", "10")["articles"] == [],
              "glow-up that declined everything is real work, still cooled down")

        print("cooldown expires: an old glowup outcome is selectable again")
        led4 = tmp / "ledger-cooldown-old"
        write_ledger(led4, B, skipped_findings=4, status="glowup",
                     reviewed_at="2026-04-01")                       # 139 days ago
        q = run_select(repo, tiers, led4, "--count", "10")
        check([a["path"] for a in q["articles"]] == [B],
              "page past the 90-day cooldown re-selectable")

        print("zero banked but clarity_flag alone still qualifies")
        led5 = tmp / "ledger-clarity-only"
        write_ledger(led5, A, skipped_findings=0, clarity_flag=True)
        q = run_select(repo, tiers, led5, "--count", "10")
        check([a["path"] for a in q["articles"]] == [A],
              "clarity-only page selected (taxonomy-run candidate)")

        print("open-PR dedupe: any content-review branch on the page excludes it")
        led6 = tmp / "ledger-open"
        write_ledger(led6, A, skipped_findings=5)
        write_ledger(led6, C, skipped_findings=1)
        for branch in ("content-review/docs-concepts-alpha",
                       "content-review/retire-docs-concepts-alpha",
                       "content-review/glowup-docs-concepts-alpha"):
            q = run_select(repo, tiers, led6, "--count", "10",
                           "--open-branches", branch)
            check([a["path"] for a in q["articles"]] == [C],
                  f"page with open {branch} excluded")

        # Driven off the constant, not a literal: the cap is a tuning knob
        # (5 -> 10 on 2026-08-19) and a hard-coded 5 here silently stops
        # testing the boundary the moment someone moves it.
        cap = glowup_cap()
        print(f"backlog cap: {cap} open glow-up PRs halt the lane")
        at_cap = ",".join(f"content-review/glowup-docs-x{i}" for i in range(cap))
        q = run_select(repo, tiers, led6, "--count", "10", "--open-branches", at_cap)
        check(q["halted"] == "max_open_glowup_prs", f"halted (got {q['halted']})")
        check(q["articles"] == [], "halted queue is empty")
        under = ",".join(f"content-review/glowup-docs-x{i}" for i in range(cap - 1))
        q = run_select(repo, tiers, led6, "--count", "10", "--open-branches", under)
        check(q["halted"] is None and len(q["articles"]) == 2,
              "one under the cap the lane runs")

    print(f"\n{_passes} passed, {len(_failures)} failed")
    return 1 if _failures else 0


if __name__ == "__main__":
    sys.exit(main())
