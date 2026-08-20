#!/usr/bin/env python3
"""Select one page for the daily automated glow-up (whole-page rehab).

Deterministic pre-step for the glow-up lane of the review-existing-content
dispatcher. Where `select-articles.py` picks pages whose FACTS are most likely
stale, this selector picks the page with the largest ACCUMULATED backlog of
judgment-level findings the fix lane has banked and deferred — the
"Findings not applied" sections, readthrough reconceptions (`clarity_flag`),
and the flag-only Search-opportunity signal. The glow-up worker executes that
backlog under human review (glow-up PRs never arm auto-merge; the PR-review
sweep routes them to Cam/Josh).

Scoring (over ledger entries only — a never-reviewed page has no banked
backlog to execute):

    score = skipped_findings * tier_w * (0.25 + 0.75*traffic_n)
            + CLARITY_BOOST   (ledger clarity_flag — a flagged reconception
                               is the strongest single glow-up signal)
            + LOW_CTR_BOOST   (the queue-recorded low_ctr_flag rode into the
                               ledger's signals block: searchers see the page
                               and don't click)

Exclusions: tier-0 paths, drafts, `redirect_to:` stubs, pages with any open
`content-review/*` PR (fix, retirement, or glow-up), pages with no banked
signal at all, and pages whose ledger records a `glowup` outcome within
GLOWUP_COOLDOWN_DAYS. (A later fix-lane review overwrites the ledger entry
and with it the glowup status — the cooldown can under-count after that.
Acceptable: the fix review also rewrote skipped_findings, so the score
re-derives from the fresh backlog.)

Backlog cap: when >= GLOWUP_MAX_OPEN_PRS open `content-review/glowup-*`
branches exist, emit an empty queue with `"halted": "max_open_glowup_prs"` —
the day's glow-up slot is skipped, not queued.

Usage:
    select-glowup.py --count 1 --out .glowup-queue.json
        [--traffic-file .traffic-snapshot] [--tiers <yaml>]
        [--ledger-dir .ledger-cache] [--no-gh] [--today YYYY-MM-DD]
        [--open-branches b1,b2] [--dry-run]

`--open-branches` injects the open-branch set for tests (implies no gh call).
When `$GITHUB_OUTPUT` is set, appends `has_articles=` / `halted=` like the
fix-lane selector.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _selector_common import (  # noqa: E402  (needs the sys.path insert above)
    Lane,
    finish,
    load_ledger,
    load_traffic,
    parse_day,
)

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[1]

# The fix-lane selector owns the shared path/tier/exclusion helpers — import
# it by path (hyphenated filename; main() is guarded), the record-review.py
# pattern, so the two selectors can never drift on slugging or stub rules.
_spec = importlib.util.spec_from_file_location("select_articles", HERE / "select-articles.py")
_select = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_select)

BRANCH_PREFIX = _select.BRANCH_PREFIX  # "content-review/"
GLOWUP_BRANCH_PREFIX = BRANCH_PREFIX + "glowup-"
TIER_WEIGHTS = _select.TIER_WEIGHTS

LANE = Lane(
    prog="select-glowup",
    items_key="articles",
    corpus_noun="page",
    item_noun="article",
    has_output="has_articles",
)

# Backlog cap (Cam): at this many open glow-up PRs the day's slots are skipped
# until reviews drain the queue. Raised 5 -> 10 alongside GLOWUP_COUNT 1 -> 2
# (2026-08-19): the cap is review-latency backpressure, so it has to clear at
# least count x expected-review-days or the lane spends most of its time
# halted and the nominal rate is fiction.
GLOWUP_MAX_OPEN_PRS = 10
# A page glow-upped this recently is not re-selected: the point of the lane
# is executing an accumulated backlog, and one just was.
GLOWUP_COOLDOWN_DAYS = 90
# ...but a page whose backlog recovery keeps failing must not re-qualify
# forever. A degraded glow-up executes nothing, re-sets `glowup_degraded`, and
# would re-qualify on the very next run — an unbounded loop that burns a slot a
# day and eventually halts the whole lane on GLOWUP_MAX_OPEN_PRS, which is
# backpressure aimed at the wrong thing. `attempts` cannot guard it: the glowup
# status path resets it to 0. After this many consecutive degraded runs the
# page serves the normal cooldown, by which time either a fix-lane review has
# banked something recoverable or the page genuinely has nothing to recover.
GLOWUP_DEGRADED_ATTEMPT_CAP = 2
# Additive signal boosts, in units of weighted findings (the base term is
# skipped_findings, typically 1-6, times a tier weight <= 1).
CLARITY_BOOST = 5.0
LOW_CTR_BOOST = 3.0


def low_ctr_flagged(entry: dict) -> bool:
    signals = entry.get("signals") or {}
    gsc = signals.get("gsc") or {}
    return bool(gsc.get("low_ctr_flag"))


def glowup_cooldown_active(entry: dict, today) -> bool:
    if entry.get("status") != "glowup":
        return False
    # A glow-up whose backlog never reached it executed nothing and declined
    # nothing, so the page is still owed its rehab and must stay selectable.
    # record-review.py sets this flag precisely because the counters alone
    # cannot say it: a degraded run CARRIES the prior banked count forward, so
    # `skipped_findings: 17` reads identically to a run that declined 17. #20984.
    # Bounded, though: past the cap the page serves the normal cooldown rather
    # than looping on a recovery that keeps failing for the same reason.
    if (entry.get("glowup_degraded")
            and int(entry.get("glowup_degraded_runs") or 0)
            < GLOWUP_DEGRADED_ATTEMPT_CAP):
        return False
    reviewed = parse_day(entry.get("reviewed_at"))
    return bool(reviewed and (today - reviewed).days < GLOWUP_COOLDOWN_DAYS)


def findings_for(findings_dir: Path | None, slug: str) -> dict | None:
    """This page's structured findings record, or None. Never raises: a
    missing or malformed record just means the worker falls back to the
    PR-body scrape, which is what it did before the record existed."""
    if findings_dir is None or not slug:
        return None
    f = findings_dir / f"{slug}.json"
    if not f.is_file():
        return None
    try:
        rec = json.loads(f.read_text())
    except (OSError, json.JSONDecodeError):
        return None
    return rec if isinstance(rec, dict) else None


def score_entry(entry: dict, tier: int, visits: int | None, max_visits: int,
                median_visits: int, have_traffic: bool) -> float:
    tier_w = TIER_WEIGHTS.get(tier, TIER_WEIGHTS[3])
    banked = max(int(entry.get("skipped_findings") or 0), 0)
    base = banked * tier_w * _traffic_term(visits, max_visits, median_visits, have_traffic)
    boost = 0.0
    if entry.get("clarity_flag"):
        boost += CLARITY_BOOST
    if low_ctr_flagged(entry):
        boost += LOW_CTR_BOOST
    return round(base + boost, 4)


def _traffic_term(visits: int | None, max_visits: int, median_visits: int,
                  have_traffic: bool) -> float:
    import math
    if not have_traffic or max_visits <= 0:
        return 1.0
    v = visits if visits is not None else median_visits
    traffic_n = math.log1p(v) / math.log1p(max_visits)
    return 0.25 + 0.75 * traffic_n


def open_branches(args) -> set[str] | None:
    if args.open_branches is not None:
        return {b.strip() for b in args.open_branches.split(",") if b.strip()}
    return _select.open_review_branches(use_gh=not args.no_gh)


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--count", type=int, default=1)
    p.add_argument("--findings-dir", default="",
                   help="synced findings/ prefix; each selected article carries "
                        "its record into the unprivileged worker")
    p.add_argument("--out", help="Queue JSON output path")
    p.add_argument("--traffic-file", help="S3-fetched traffic snapshot (CSV or JSON)")
    p.add_argument("--tiers", default=str(_select.DEFAULT_TIERS))
    p.add_argument("--ledger-dir", default=str(_select.DEFAULT_LEDGER_DIR))
    p.add_argument("--repo-root", default=str(REPO_ROOT), help=argparse.SUPPRESS)
    p.add_argument("--no-gh", action="store_true", help="Skip gh API calls (testing)")
    p.add_argument("--today", help="Override today's date YYYY-MM-DD (testing)")
    p.add_argument("--open-branches",
                   help="Comma-separated open content-review branch names (testing)")
    p.add_argument("--dry-run", action="store_true", help="Print queue, write nothing")
    args = p.parse_args()

    if not args.out and not args.dry_run:
        p.error("--out is required (or use --dry-run)")

    repo = Path(args.repo_root)
    today = parse_day(args.today) or datetime.now(timezone.utc).date()
    tier_rules = _select.load_tiers(Path(args.tiers))
    findings_dir = Path(args.findings_dir) if args.findings_dir else None
    ledger = load_ledger(Path(args.ledger_dir), LANE)

    all_paths = sorted(
        str(f.relative_to(repo)) for f in (repo / _select.CONTENT_DIR).rglob("*.md")
    )
    known = set(all_paths)
    traffic, traffic_meta = load_traffic(
        Path(args.traffic_file) if args.traffic_file else None, known,
        _select.content_path_for_url,
    )
    have_traffic = bool(traffic)
    visits_known = sorted(traffic.values())
    max_visits = visits_known[-1] if visits_known else 0
    median_visits = visits_known[len(visits_known) // 2] if visits_known else 0

    queue: dict = {
        "generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "count": 0,
        "halted": None,
        "traffic": {**traffic_meta, "available": have_traffic},
        "articles": [],
    }

    branches = open_branches(args)
    if branches is None:
        queue["halted"] = "gh_unavailable"
        return finish(queue, args, LANE)
    n_glowup_open = sum(1 for b in branches if b.startswith(GLOWUP_BRANCH_PREFIX))
    if n_glowup_open >= GLOWUP_MAX_OPEN_PRS:
        queue["halted"] = "max_open_glowup_prs"
        return finish(queue, args, LANE)
    open_slugs = {
        b[len(BRANCH_PREFIX):].removeprefix("retire-").removeprefix("glowup-")
        for b in branches
    }

    scored: list[tuple[float, str, dict]] = []
    for path, entry in ledger.items():
        if path not in known:
            continue
        policy = _select.policy_for(path, tier_rules)
        tier, no_retire = policy.tier, policy.no_retire
        # A glow-up rewrites the page, so this lane asks the editable question,
        # not the tier one: a generated tree the report lane fact-checks is
        # still one no PR here may rehab (pulumi/docs#20996).
        if not policy.editable:
            continue
        if _select.slugify(path) in open_slugs:
            continue
        if _select.is_draft(repo / path):
            continue
        if _select.is_redirect_stub(repo / path):
            continue
        banked = int(entry.get("skipped_findings") or 0)
        if banked <= 0 and not entry.get("clarity_flag"):
            continue  # nothing banked to execute
        if glowup_cooldown_active(entry, today):
            continue
        score = score_entry(entry, tier, traffic.get(path), max_visits,
                            median_visits, have_traffic)
        scored.append((score, path, entry))

    scored.sort(key=lambda t: (-t[0], t[1]))
    for score, path, entry in scored[: max(args.count, 0)]:
        tier, no_retire = _select.tier_for(path, tier_rules)
        queue["articles"].append({
            "path": path,
            "url": _select.url_for(path),
            "slug": _select.slugify(path),
            "lane": "glowup",
            "mode": "glowup",
            "tier": tier,
            "no_retire": no_retire,
            "monthly_visits": traffic.get(path),
            "signals": entry.get("signals"),
            "last_reviewed": entry.get("reviewed_at"),
            "skipped_findings": int(entry.get("skipped_findings") or 0),
            "clarity_flag": bool(entry.get("clarity_flag")),
            # Stale-claim markers ride EVERY queue that can reach record-review:
            # it rebuilds the ledger entry from the queue article, so a glow-up
            # run on a marked page would otherwise silently drop the markers —
            # the exact carry-forward bug #20968 fixed for --paths reviews.
            "stale_claims": len(_select.all_markers(entry)),
            "stale_claim_markers": _select.all_markers(entry),
            # The banked-findings source: the ledger entry's latest review PR.
            # Carried on the queue because the worker has no ledger cache —
            # build-glowup-backlog.py reads it from here.
            # `pr_number` is only set when the LATEST review opened a PR, and a
            # review that banks findings without applying any opens none — so
            # falling back to the durable pointer is the whole point of it
            # existing. Without this the worker is handed None for exactly the
            # pages with the largest backlogs. #20984.
            "source_pr_number": int(entry.get("pr_number")
                                    or entry.get("last_pr_number") or 0) or None,
            # The structured findings record rides the queue for the same
            # reason the markers above do: build-glowup-backlog.py runs in the
            # UNPRIVILEGED review job, which has no AWS credentials and so
            # cannot read the findings/ prefix itself. The dispatcher can, so
            # it hands the record over rather than leaving the worker to scrape
            # the PR body (see record-page-findings.py).
            "findings_record": findings_for(findings_dir, _select.slugify(path)),
            "score": score,
        })

    return finish(queue, args, LANE)


if __name__ == "__main__":
    sys.exit(main())
