#!/usr/bin/env python3
"""Select existing content pages for automated review.

Deterministic pre-step for the review-existing-content workflow
(`.github/workflows/review-existing-content.yml`): given the strategic tier
map, the S3-fetched traffic snapshot, and the per-page review ledger, emit
the day's review queue as JSON. The model never chooses what to review —
this script does, so the selection is auditable and reproducible from its
inputs.

Selection algorithm (weighted fair queuing by staleness):

1. Enumerate `content/docs/**/*.md`; keep the paths this mode is allowed to
   touch (`--mode fix`: editable pages; `--mode report`: reviewable pages a
   generator owns — see MODES below), then drop `draft: true` pages and
   `redirect_to:` stubs (tombstones, not content).
2. Hard filters: pages with an open `content-review/<slug>` bot PR; pages
   whose `incomplete` review has already burned ATTEMPT_CAP retries (they
   back off and are surfaced for a human instead of looping forever).
3. Runaway guardrail: if >= MAX_OPEN_PRS open `content-review/*` PRs exist,
   emit an empty queue with `"halted": "max_open_prs"` so the workflow
   warns instead of piling on.
4. Score every remaining page and take the top `count`. No threshold, no
   reserved lane — staleness self-corrects starvation (the longer a page
   goes unreviewed the higher it climbs, so the whole corpus is swept):

       score = importance * staleness + stale_claim_boost

   importance = tier_w * (0.25 + 0.75*traffic_n) * gsc_m * feedback_m
              = tier_w * gsc_m * feedback_m     tier-only when no traffic
   tier_w     = {1: 1.0, 2: 0.6, 3: 0.3}
   traffic_n  = log1p(visits) / log1p(max_visits); pages missing from the
                report impute the median
   gsc_m      = 1 + 0.25 * impressions_n * ctr_gap, in [1.0, 1.25]: the
                Search Console "opportunity" boost — only pages searchers
                see a lot (high impressions) but rarely click (CTR below
                the corpus median) boost
   feedback_m = 1 + 0.30 * neg_rate * min(1, votes/10), in [1.0, 1.30]:
                the feedback-widget boost — "No, this page didn't help"
                votes raise priority, damped below 10 total votes so a
                couple of noisy votes can't max it out

   The two reader-signal terms come from the optional reader-signals
   export (--signals-file) and are boost-only with a floor of exactly
   1.0: a page missing from the export (or under the noise thresholds,
   or the export not existing at all) scores precisely what it would
   have scored before these terms existed, and no page ever ranks lower
   because of them. High CTR / positive feedback never suppress — a
   well-titled page can still be factually stale, and that page is
   exactly what the review is for. Unlike the traffic term (an always-on
   scaler where absent pages impute the median so they aren't punished),
   these are pure boosts, so neutral 1.0 — not the median — is the
   no-penalty imputation.
   staleness  = (today - effective_last_review).days, floored at 0
   effective_last_review = max(bot_reviewed_at, last_non-bot_commit_date)
                where bot_reviewed_at counts only for a *completed* review
                (an `incomplete` outcome never advances the clock, so the
                page stays due). Never-bot-reviewed pages fall back to their
                git creation date: a brand-new page sorts to the back, an
                ancient never-reviewed page to the front. A human (non-bot)
                edit fully resets the clock.

   stale_claim_boost = STALE_CLAIM_BOOST when the page's ledger entry carries
                a non-escalated stale-claim marker (written by the nightly
                reverify-claims.py when a volatile claim the page asserts
                re-verified contradicted; see active_markers); 0 otherwise.
                Marked pages jump the queue; a marker retires when a review
                resolves it (record-review.py `resolved_claims`), and one
                unresolved through MARKER_ESCALATION_CAP reviews stops
                boosting (escalated — a human's turn), so the boost is
                bounded either way.

   Ties break on path ascending, so runs are reproducible.

Two modes, over disjoint halves of the corpus (see `eligible`):

* `--mode fix` (default) — pages a PR may edit. Unchanged: score, queue,
  dispatch a worker that reviews the page and opens a PR for what it fixed.
* `--mode report` — pages a PR may NOT edit but whose prose is still ours to
  check: generated trees, chiefly the 248-page CLI command reference. Same
  scoring, but the worker records the page's claim list and changes nothing.
  This exists because "a generator owns this file" and "don't look at this
  file" were the same flag (tier 0) until pulumi/docs#20996, and selection is
  the only thing that ever writes a page's claim list — so 30% of
  `content/docs/` had never been fact-checked once. Contradictions found on
  these pages route upstream (reverify-claims.py's `fix_route`), never to a
  marker no PR here could ever retire.

Usage:
    select-articles.py --count 3 --out .content-review-queue.json
        [--mode fix|report]
        [--traffic-file .traffic-snapshot] [--signals-file .reader-signals.json]
        [--tiers <yaml>] [--ledger-dir scripts/content-review/ledger]
        [--paths content/docs/a.md,content/docs/b/_index.md]
        [--no-gh] [--today YYYY-MM-DD] [--dry-run]
    select-articles.py --stats   # ledger outcome report (merged/closed/open)
    select-articles.py --prune   # GC ledger entries whose pages are gone

`--paths` bypasses scoring entirely (workflow_dispatch testing). `--no-gh`
and `--today` exist for tests. When `$GITHUB_OUTPUT` is set, the script
appends `has_articles=` and `halted=` for workflow gating (the queue count is
read from the queue JSON, which every consumer already has).
"""

from __future__ import annotations

import argparse
import json
import math
import subprocess
import sys
from datetime import date, datetime, timezone
from pathlib import Path
from typing import NamedTuple

import yaml

# Infrastructure this selector shares with scripts/blog-review/select-posts.py —
# see _selector_common.py's docstring for why it is shared rather than copied.
# The sys.path insert is anchored on this file's own location because the
# selector is not always run with its directory on the path: scripts/snippet-
# sweep/sweep.py loads it by path from a different directory.
sys.path.insert(0, str(Path(__file__).resolve().parent))

from _selector_common import (  # noqa: E402  (needs the sys.path insert above)
    FRONTMATTER_RE,
    INCOMPLETE_STATUS,
    Lane,
    cmd_prune,
    effective_last_review,
    finish,
    git_history_signals,
    load_ledger,
    load_traffic,
    normalize_url_path,
    parse_day,
)

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_TIERS = (
    REPO_ROOT
    / ".claude/commands/review-existing-content/references/strategic-tiers.yaml"
)
DEFAULT_LEDGER_DIR = REPO_ROOT / "scripts/content-review/ledger"
CONTENT_DIR = "content/docs"

# How the shared helpers in _selector_common.py address this lane.
LANE = Lane(
    prog="select-articles",
    items_key="articles",
    corpus_noun="page",
    item_noun="article",
    has_output="has_articles",
    # No `count=`: every consumer of this lane's gate already reads the queue
    # JSON, which carries the count.
)

BRANCH_PREFIX = "content-review/"

# Worker modes this selector can queue for. `fix` is the original lane: pages a
# PR may edit. `report` is the fact-check-only lane (pulumi/docs#20996) over the
# pages a PR may NOT edit — generated trees whose prose is still ours to check.
FIX_MODE = "fix"
REPORT_MODE = "report"
MODES = {FIX_MODE, REPORT_MODE}
MAX_OPEN_PRS = 9
# An `incomplete` review (worker exited before recording a verdict, or claimed
# a fix with no PR) never advances the staleness clock, so the page stays due
# and is retried next sweep. This caps the retries: once a page has burned
# ATTEMPT_CAP incomplete runs it backs off (is excluded and surfaced) instead
# of looping forever on whatever keeps breaking it.
ATTEMPT_CAP = 3

TIER_WEIGHTS = {1: 1.0, 2: 0.6, 3: 0.3}

# Additive boost for a page whose ledger entry carries a non-empty
# `stale_claims` marker (a volatile claim it asserts re-verified contradicted
# — see reverify-claims.py). Sized to outrank a top-importance page that has
# gone unreviewed for a year (1.0 * 365), so a known-stale fact beats any
# ordinary staleness — while an ancient never-reviewed page can still win, so
# the sweep is never fully starved. A marker retires when the page's next
# review resolves it (record-review.py), so the boost self-clears.
STALE_CLAIM_BOOST = 400.0

# A marker the last MARKER_ESCALATION_CAP reviews each saw and left unresolved
# stops boosting. Carrying an unresolved marker forward is what keeps a missed
# finding from evaporating (record-review.py), but an unboundedly boosted page
# would be re-picked every sweep and starve the rest of the queue, which is the
# same failure the marker was meant to cure. Past the cap the marker stays on
# the ledger entry — visible, still reported, still blocking re-verification
# churn — but it stops jumping the page to the front. That is the signal a
# human needs to look at it.
MARKER_ESCALATION_CAP = 2

# A stale-claim marker does not boost while the page's last COMPLETED review is
# newer than this. The claims index snapshots the PRE-fix page on purpose (the
# model must not launder its own edits into the index), so the night after a
# fix merges the marker is still there describing a value the merged PR already
# corrected — and a +400 boost would drag the just-fixed page straight back to
# the front of the queue. That echo bought one redundant full review per fix,
# observed twice in the 2026-08-18 queue alone.
#
# reverify-claims.superseded_by_review() is the primary guard and stops the
# re-check upstream of the marker; this is the second, independent one, on the
# consumer side, for a marker that is already on the entry when a fix lands.
# Both were specified in #20970; only the reverify half shipped.
#
# An INCOMPLETE review never suppresses — it did not fix anything, so the
# marker is still live. A marker surviving past the cooldown is real drift and
# boosts exactly as before.
STALE_BOOST_COOLDOWN_DAYS = 5


def all_markers(entry: dict | None) -> list[dict]:
    """Every stale-claim marker on this ledger entry, escalated or not.

    This is what rides in the queue item, and it is deliberately unfiltered.
    record-review.py rebuilds the ledger entry from the queue and writes back
    whatever markers survive the review, so a marker withheld here would be
    dropped from the ledger the next time the page is reviewed for any reason
    — and `already_marked()` in reverify-claims.py would then let the entity
    back into the nightly pool, restarting the detect/boost/miss/clear cycle
    this whole mechanism exists to break.
    """
    return [m for m in (entry or {}).get("stale_claims") or [] if isinstance(m, dict)]


def _day(value) -> date | None:
    try:
        return datetime.strptime(str(value), "%Y-%m-%d").date()
    except (TypeError, ValueError):
        return None


def boost_suppressed_by_recent_fix(entry: dict | None, today: date) -> bool:
    """True when this page's markers are an ECHO of a fix that already landed.

    See STALE_BOOST_COOLDOWN_DAYS. Three conditions, all required:

    1. The last review COMPLETED (record-review.py's vocabulary: any status
       but "incomplete"). An incomplete review fixed nothing.
    2. It is inside the cooldown window.
    3. EVERY marker on the entry was checked AFTER that review.

    (3) is the one that makes this precise rather than a blunt mute. A marker
    written after a completed review is the echo #20970 describes: the claims
    index still holds the PRE-fix snapshot, so that night's re-check re-flags
    a value the merged PR already corrected. A marker written BEFORE the
    review is the opposite situation — the review saw it and left it — and
    that is real, unresolved drift which must keep boosting (and escalates on
    its own via MARKER_ESCALATION_CAP). Suppressing those would mute the
    finding the whole mechanism exists to carry.
    """
    entry = entry or {}
    if entry.get("status") == "incomplete":
        return False
    reviewed = _day(entry.get("reviewed_at"))
    if reviewed is None or not (0 <= (today - reviewed).days < STALE_BOOST_COOLDOWN_DAYS):
        return False
    markers = all_markers(entry)
    if not markers:
        return False
    # An undated marker is not provably an echo, so it keeps its boost.
    checked = [_day(m.get("checked_at")) for m in markers]
    return all(c is not None and c > reviewed for c in checked)


def active_markers(entry: dict | None) -> list[dict]:
    """The subset of markers that still earn the page a priority boost.

    Escalated markers (see MARKER_ESCALATION_CAP) are excluded *from the
    boost only*: repeated reviews have already failed to act on them, so
    another jump to the front of the queue is not the remedy. They still
    travel in the queue item and still persist on the ledger — see
    all_markers().
    """
    return [m for m in all_markers(entry) if not m.get("escalated")]

# Reader-signal boost tuning. Both multipliers floor at exactly 1.0 (see the
# module docstring); the caps keep the maximum combined boost (~1.63x) well
# under the tier spread (3.3x), so signals reorder comparably stale same-tier
# peers without overriding tiering or staleness.
GSC_MIN_IMPRESSIONS = 200  # below this, CTR is noise -> neutral
GSC_BOOST_MAX = 0.25  # gsc multiplier in [1.0, 1.25]
FEEDBACK_MIN_TOTAL = 3  # fewer votes than this -> neutral
FEEDBACK_SATURATION = 10  # votes at which neg_rate gets full weight
FEEDBACK_BOOST_MAX = 0.30  # feedback multiplier in [1.0, 1.30]
# The flag-only "title/meta_desc may under-sell this page in search" signal.
# Deliberately stricter than the boost thresholds: the flag surfaces in the
# review PR for a human, so it fires only on unambiguous cases.
LOW_CTR_FLAG_MIN_IMPRESSIONS = 1000
LOW_CTR_FLAG_RATIO = 0.5  # flag when ctr <= 0.5 * corpus median CTR


# ---- Path helpers -----------------------------------------------------------


def slugify(content_path: str) -> str:
    """content/docs/iac/concepts/stacks/_index.md -> docs-iac-concepts-stacks"""
    p = content_path
    if p.startswith("content/"):
        p = p[len("content/") :]
    if p.endswith("/_index.md"):
        p = p[: -len("/_index.md")]
    elif p.endswith(".md"):
        p = p[: -len(".md")]
    return p.replace("/", "-")


def url_for(content_path: str) -> str:
    """content/docs/iac/concepts/stacks.md -> /docs/iac/concepts/stacks/"""
    p = content_path
    if p.startswith("content/"):
        p = p[len("content/") :]
    if p.endswith("/_index.md"):
        p = p[: -len("/_index.md")]
    elif p.endswith(".md"):
        p = p[: -len(".md")]
    return f"/{p}/"


def content_path_for_url(url_path: str, known_paths: set[str]) -> str | None:
    """Map a live /docs/... URL path back to its content file, if it exists."""
    p = normalize_url_path(url_path)
    candidate_leaf = f"content{p}.md"
    candidate_index = f"content{p}/_index.md"
    if candidate_leaf in known_paths:
        return candidate_leaf
    if candidate_index in known_paths:
        return candidate_index
    return None


# ---- Input loading ----------------------------------------------------------


def load_tiers(tiers_file: Path) -> list[dict]:
    """Return tier rules sorted longest-prefix-first for first-match lookup."""
    data = yaml.safe_load(tiers_file.read_text())
    rules = data.get("tiers", []) if isinstance(data, dict) else []
    return sorted(rules, key=lambda r: len(r.get("prefix", "")), reverse=True)


class PagePolicy(NamedTuple):
    """What the review pipeline may do with one page.

    `tier`/`no_retire` are the scoring and retirement inputs they always were.
    The two booleans are the split of what tier 0 used to conflate:

      editable   — may a PR change this file? False for a tree a generator
                   owns: the generator overwrites any edit, so a fix, a
                   glow-up, or a snippet sweep there is spend thrown away.
      reviewable — may the pipeline read this page and record what it claims?
                   Independent of the above: "a generator owns this file" says
                   nothing about whether its prose is true.

    Conflating them meant tier 0 read as "never select", and selection is the
    only thing that ever writes a page's claim list — so 254 pages (30% of
    content/docs, 248 of them the CLI command reference) had never been
    fact-checked once. See pulumi/docs#20996.
    """

    tier: int
    no_retire: bool
    editable: bool
    reviewable: bool


def policy_for(path: str, rules: list[dict]) -> PagePolicy:
    """Longest-prefix match wins; unmatched paths are ordinary tier-3 content.

    `tier: 0` stays valid as shorthand for "neither editable nor reviewable"
    (the trees we genuinely never want to look at), and explicit `editable:` /
    `reviewable:` keys override it in either direction.
    """
    for rule in rules:
        if path.startswith(rule.get("prefix", "")):
            tier = int(rule.get("tier", 3))
            editable = bool(rule.get("editable", tier != 0))
            # A page no PR may edit is a page no PR may retire, so the queue
            # field agrees with check-retire-veto.py rather than reading
            # `no_retire: false` on a page nothing could retire anyway.
            no_retire = bool(rule.get("no_retire", False)) or tier == 1 or not editable
            return PagePolicy(
                tier,
                no_retire,
                editable,
                bool(rule.get("reviewable", tier != 0)),
            )
    return PagePolicy(3, False, True, True)


def tier_for(path: str, rules: list[dict]) -> tuple[int, bool]:
    """(tier, no_retire) — the pre-#20996 shape, for callers that want only
    the scoring facts. `policy_for` is the full answer."""
    policy = policy_for(path, rules)
    return policy.tier, policy.no_retire


def eligible(policy: PagePolicy, mode: str) -> bool:
    """Is this page a candidate for `mode`?

    The two lanes partition the corpus rather than overlapping: a page the fix
    lane can edit is never queued for report-only (the fix lane already records
    its claims as a side effect of reviewing it), and a page it cannot edit is
    never queued for a fix it could not keep. Pages that are neither editable
    nor reviewable are out of both.
    """
    if mode == REPORT_MODE:
        return policy.reviewable and not policy.editable
    return policy.editable


def load_reader_signals(
    signals_file: Path | None, known_paths: set[str]
) -> tuple[dict[str, dict], dict[str, dict], dict]:
    """Parse the S3 reader-signals snapshot into per-content-path signal maps.

    The snapshot is a single JSON object with independently optional sections
    (see the data-export contract in the review-existing-content skill docs):

        {"version": 1, "generated": ..., "signals": {
            "gsc":      {"source", "period", "pages": {url: {impressions, clicks, position}}},
            "feedback": {"source", "period", "pages": {url: {yes, no}}}}}

    A bare GSC section with no {"signals": ...} envelope is also accepted —
    that is the shape of the export the data team ships today
    (pulumi/data#865 phase 2, the Airflow stack's docsTrafficGscLatestS3Uri):

        {"source", "period", "generated", "pages": {url: {clicks, impressions, position}}}

    Returns (gsc, feedback, meta). A missing/unreadable/malformed file — or a
    missing section — degrades that signal to unavailable, mirroring
    load_traffic: selection then scores exactly as if the signal never existed.
    """
    meta = {
        "gsc": {"available": False, "source": None, "period": None,
                "pages_matched": 0, "median_ctr": None, "max_impressions": None},
        "feedback": {"available": False, "source": None, "period": None,
                     "pages_matched": 0},
    }
    gsc: dict[str, dict] = {}
    feedback: dict[str, dict] = {}
    if signals_file is None or not signals_file.is_file():
        return gsc, feedback, meta
    try:
        data = json.loads(signals_file.read_text(errors="replace"))
    except (OSError, json.JSONDecodeError):
        return gsc, feedback, meta
    if not isinstance(data, dict):
        return gsc, feedback, meta
    sections = data.get("signals")
    if not isinstance(sections, dict):
        # No envelope: accept the bare GSC-only export (pulumi/data#865
        # phase 2) so the signal activates on what ships today. The full
        # envelope (adding feedback) supersedes it whenever it lands.
        if isinstance(data.get("pages"), dict):
            sections = {"gsc": data}
        else:
            return gsc, feedback, meta

    def _int(v) -> int:
        try:
            return max(int(float(v)), 0)
        except (TypeError, ValueError):
            return 0

    gsc_section = sections.get("gsc")
    if isinstance(gsc_section, dict) and isinstance(gsc_section.get("pages"), dict):
        for url_path, row in gsc_section["pages"].items():
            if not isinstance(row, dict):
                continue
            cp = content_path_for_url(str(url_path), known_paths)
            if not cp:
                continue
            impressions = _int(row.get("impressions"))
            clicks = _int(row.get("clicks"))
            entry = {
                "impressions": impressions,
                "clicks": clicks,
                "ctr": round(clicks / impressions, 6) if impressions else 0.0,
                "position": row.get("position"),
            }
            # A URL and its aliases may both appear; like the traffic snapshot,
            # keep the row with the larger figure rather than double-counting.
            prev = gsc.get(cp)
            if prev is None or entry["impressions"] > prev["impressions"]:
                gsc[cp] = entry
        if gsc:
            # Corpus stats over pages with meaningful volume only, so the
            # long tail of near-zero-impression rows can't drag the median.
            eligible = [e for e in gsc.values() if e["impressions"] >= GSC_MIN_IMPRESSIONS]
            ctrs = sorted(e["ctr"] for e in eligible)
            meta["gsc"] = {
                "available": True,
                "source": gsc_section.get("source"),
                "period": gsc_section.get("period"),
                "pages_matched": len(gsc),
                "median_ctr": ctrs[len(ctrs) // 2] if ctrs else None,
                "max_impressions": max((e["impressions"] for e in eligible), default=None),
            }

    fb_section = sections.get("feedback")
    if isinstance(fb_section, dict) and isinstance(fb_section.get("pages"), dict):
        for url_path, row in fb_section["pages"].items():
            if not isinstance(row, dict):
                continue
            cp = content_path_for_url(str(url_path), known_paths)
            if not cp:
                continue
            # Unlike pageviews, alias rows here are distinct vote events, not
            # the same measurement counted twice — so aliases sum.
            entry = feedback.setdefault(cp, {"yes": 0, "no": 0})
            entry["yes"] += _int(row.get("yes"))
            entry["no"] += _int(row.get("no"))
        if feedback:
            meta["feedback"] = {
                "available": True,
                "source": fb_section.get("source"),
                "period": fb_section.get("period"),
                "pages_matched": len(feedback),
            }

    return gsc, feedback, meta


# ---- GitHub signals ----------------------------------------------------------


def gh_json(args: list[str]):
    proc = subprocess.run(["gh", *args], capture_output=True, text=True, check=False)
    if proc.returncode != 0:
        print(f"select-articles: gh {' '.join(args[:3])}... failed: {proc.stderr.strip()}", file=sys.stderr)
        return None
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError:
        return None


def open_review_branches(use_gh: bool) -> set[str] | None:
    """Branch names of open pulumi-bot content-review PRs; None on gh failure."""
    if not use_gh:
        return set()
    prs = gh_json(
        ["pr", "list", "--author", "pulumi-bot", "--state", "open",
         "--json", "headRefName", "--limit", "100"]
    )
    if prs is None:
        return None
    return {p["headRefName"] for p in prs if p.get("headRefName", "").startswith(BRANCH_PREFIX)}


def pr_state(pr_url: str, use_gh: bool) -> dict | None:
    if not use_gh or not pr_url:
        return None
    return gh_json(["pr", "view", pr_url, "--json", "state,mergedAt"])


# ---- Scoring -----------------------------------------------------------------


def gsc_multiplier(
    entry: dict | None, max_impressions: int | None, median_ctr: float | None
) -> tuple[float, float, bool]:
    """(multiplier in [1, 1+GSC_BOOST_MAX], opportunity in [0, 1], low_ctr_flag).

    Opportunity is impressions_n * ctr_gap: only the high-impressions AND
    below-median-CTR quadrant boosts. Pages absent from the export or under
    GSC_MIN_IMPRESSIONS are neutral (see the module docstring on imputation).
    """
    if (
        not entry
        or entry["impressions"] < GSC_MIN_IMPRESSIONS
        or not max_impressions
        or not median_ctr
    ):
        return 1.0, 0.0, False
    impressions_n = math.log1p(entry["impressions"]) / math.log1p(max_impressions)
    ctr_gap = min(max(median_ctr - entry["ctr"], 0.0) / median_ctr, 1.0)
    opportunity = min(impressions_n * ctr_gap, 1.0)
    flag = (
        entry["impressions"] >= LOW_CTR_FLAG_MIN_IMPRESSIONS
        and entry["ctr"] <= LOW_CTR_FLAG_RATIO * median_ctr
    )
    return 1.0 + GSC_BOOST_MAX * opportunity, round(opportunity, 4), flag


def feedback_multiplier(entry: dict | None) -> tuple[float, float | None]:
    """(multiplier in [1, 1+FEEDBACK_BOOST_MAX], neg_rate or None when too few votes)."""
    if not entry:
        return 1.0, None
    total = entry["yes"] + entry["no"]
    if total < FEEDBACK_MIN_TOTAL:
        return 1.0, None
    neg_rate = entry["no"] / total
    weight = min(1.0, total / FEEDBACK_SATURATION)
    return 1.0 + FEEDBACK_BOOST_MAX * neg_rate * weight, round(neg_rate, 4)


def importance(
    tier: int,
    visits: int | None,
    max_visits: int,
    median_visits: int,
    have_traffic: bool,
    gsc_m: float = 1.0,
    feedback_m: float = 1.0,
) -> float:
    """Strategic weight, modulated by traffic when a snapshot is available."""
    tier_w = TIER_WEIGHTS.get(tier, TIER_WEIGHTS[3])
    if have_traffic and max_visits > 0:
        v = visits if visits is not None else median_visits
        traffic_n = math.log1p(v) / math.log1p(max_visits)
        # Floor 0.25, not 0.5: with the old floor the log-normalized term
        # compressed a 7,600x traffic gap into a <1% score difference, so
        # staleness alone decided the queue across wildly different reader
        # impact. The floor still guarantees a zero-traffic page a quarter of
        # full weight (staleness must be able to win eventually), but traffic
        # now separates same-tier peers by up to 4x instead of 2x.
        return tier_w * (0.25 + 0.75 * traffic_n) * gsc_m * feedback_m
    return tier_w * gsc_m * feedback_m


def score_page(
    tier: int,
    visits: int | None,
    max_visits: int,
    median_visits: int,
    last_review: date | None,
    today: date,
    have_traffic: bool,
    stale_claims: bool = False,
    gsc_m: float = 1.0,
    feedback_m: float = 1.0,
) -> float:
    staleness = max((today - last_review).days, 0) if last_review else 0
    boost = STALE_CLAIM_BOOST if stale_claims else 0.0
    return round(
        importance(tier, visits, max_visits, median_visits, have_traffic, gsc_m, feedback_m)
        * staleness
        + boost,
        4,
    )


# ---- Subcommands ---------------------------------------------------------------


def cmd_stats(ledger_dir: Path, use_gh: bool) -> int:
    entries = load_ledger(ledger_dir, LANE)
    counts = {"merged": 0, "closed": 0, "open": 0, "clean": 0, "reported": 0,
              "incomplete": 0, "capped": 0, "unknown": 0}
    by_lane: dict[str, int] = {}
    for path, entry in sorted(entries.items()):
        by_lane[entry.get("lane", "priority")] = by_lane.get(entry.get("lane", "priority"), 0) + 1
        status = entry.get("status")
        if status == INCOMPLETE_STATUS:
            counts["incomplete"] += 1
            if int(entry.get("attempts", 0)) >= ATTEMPT_CAP:
                counts["capped"] += 1
            continue
        # `status == "clean"` is the canonical form; `clean: true` is the legacy
        # pre-standardization field still present on older ledger objects.
        if status == "clean" or entry.get("clean"):
            counts["clean"] += 1
            continue
        # The report-only lane never opens a PR, so a `pr_state` lookup on it
        # would book every one of these as "unknown" — and there are 248 pages
        # in that lane.
        if status == "reported":
            counts["reported"] += 1
            continue
        state = pr_state(entry.get("pr", ""), use_gh)
        if state is None:
            counts["unknown"] += 1
        elif state.get("mergedAt"):
            counts["merged"] += 1
        elif state.get("state") == "CLOSED":
            counts["closed"] += 1
        else:
            counts["open"] += 1
    print(json.dumps({"entries": len(entries), "outcomes": counts, "by_lane": by_lane}, indent=2))
    return 0


# ---- Main ----------------------------------------------------------------------


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--count", type=int, default=3)
    p.add_argument("--out", help="Queue JSON output path")
    p.add_argument("--traffic-file", help="S3-fetched traffic snapshot (CSV or JSON)")
    p.add_argument("--signals-file", help="S3-fetched reader-signals snapshot (JSON)")
    p.add_argument("--tiers", default=str(DEFAULT_TIERS))
    p.add_argument("--ledger-dir", default=str(DEFAULT_LEDGER_DIR))
    p.add_argument("--repo-root", default=str(REPO_ROOT), help=argparse.SUPPRESS)
    p.add_argument("--paths", help="Comma-separated content paths; bypasses scoring (testing)")
    p.add_argument("--lane", help="Override lane for --paths entries (default manual)")
    p.add_argument("--mode", choices=sorted(MODES), default="fix",
                   help="fix (default): editable pages, the lane that opens PRs. "
                        "report: reviewable-but-not-editable pages (generated "
                        "trees) — record the claim list, change nothing.")
    p.add_argument("--no-gh", action="store_true", help="Skip gh API calls (testing)")
    p.add_argument("--today", help="Override today's date YYYY-MM-DD (testing)")
    p.add_argument("--dry-run", action="store_true", help="Print queue, write nothing")
    p.add_argument("--stats", action="store_true", help="Report ledger outcomes and exit")
    p.add_argument("--prune", action="store_true", help="GC ledger entries for deleted pages")
    args = p.parse_args()

    repo = Path(args.repo_root)
    ledger_dir = Path(args.ledger_dir)
    mode = args.mode
    # The report lane opens no branch and no PR, so every gh call the fix lane
    # makes to dedup against its own open PRs is both pointless and a way for a
    # gh outage to halt a lane that cannot collide with anything.
    use_gh = not args.no_gh and mode != REPORT_MODE

    if args.stats:
        return cmd_stats(ledger_dir, use_gh)
    if args.prune:
        return cmd_prune(ledger_dir, repo, args.dry_run, LANE)
    if not args.out and not args.dry_run:
        p.error("--out is required (or use --dry-run/--stats/--prune)")

    today = parse_day(args.today) or datetime.now(timezone.utc).date()
    tier_rules = load_tiers(Path(args.tiers))
    ledger = load_ledger(ledger_dir, LANE)

    all_paths = sorted(
        str(f.relative_to(repo)) for f in (repo / CONTENT_DIR).rglob("*.md")
    )
    known = set(all_paths)
    traffic, traffic_meta = load_traffic(
        Path(args.traffic_file) if args.traffic_file else None, known, content_path_for_url
    )
    have_traffic = bool(traffic)
    visits_known = sorted(traffic.values())
    max_visits = visits_known[-1] if visits_known else 0
    median_visits = visits_known[len(visits_known) // 2] if visits_known else 0

    gsc, feedback, signals_meta = load_reader_signals(
        Path(args.signals_file) if args.signals_file else None, known
    )
    signals_available = signals_meta["gsc"]["available"] or signals_meta["feedback"]["available"]

    queue: dict = {
        "generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "count": 0,
        "mode": mode,
        "halted": None,
        "traffic": {**traffic_meta, "available": have_traffic},
        "reader_signals": {"available": signals_available, **signals_meta},
        # Pages backed off at the attempt cap (needing a human). Filled by the
        # scored path below; signal-health.py's capped-pages signal reads it.
        "capped": [],
        "articles": [],
    }

    def signal_terms(path: str) -> tuple[float, float, dict | None]:
        """(gsc_m, feedback_m, per-article signals block) — one source for
        both scoring and the queue entry, so they can't diverge."""
        if not signals_available:
            return 1.0, 1.0, None
        gsc_entry = gsc.get(path)
        fb_entry = feedback.get(path)
        gsc_m, opportunity, low_ctr_flag = gsc_multiplier(
            gsc_entry, signals_meta["gsc"]["max_impressions"], signals_meta["gsc"]["median_ctr"]
        )
        fb_m, neg_rate = feedback_multiplier(fb_entry)
        return gsc_m, fb_m, {
            "gsc": {
                "impressions": gsc_entry["impressions"],
                "ctr": gsc_entry["ctr"],
                "opportunity": opportunity,
                "multiplier": round(gsc_m, 4),
                "low_ctr_flag": low_ctr_flag,
            } if gsc_entry else None,
            "feedback": {
                "yes": fb_entry["yes"],
                "no": fb_entry["no"],
                "neg_rate": neg_rate,
                "multiplier": round(fb_m, 4),
            } if fb_entry else None,
        }

    def article(path: str, lane: str, score: float | None) -> dict:
        policy = policy_for(path, tier_rules)
        entry = ledger.get(path, {})
        return {
            "path": path,
            "url": url_for(path),
            "slug": slugify(path),
            "lane": lane,
            "mode": mode,
            "tier": policy.tier,
            "no_retire": policy.no_retire,
            # Ride the queue so every downstream consumer reads the same
            # answer this selection was made on, rather than re-deriving it
            # from a tiers file it may not have (the worker's publish job
            # reads the queue; only the retire veto re-reads the YAML).
            "editable": policy.editable,
            "monthly_visits": traffic.get(path),
            "signals": signal_terms(path)[2],
            "last_reviewed": entry.get("reviewed_at"),
            "attempts": int(entry.get("attempts", 0)),
            "stale_claims": len(all_markers(entry)),
            # The markers themselves, not just how many there are. The nightly
            # re-verification already did the expensive work — it identified the
            # entity, reached an authoritative source, and wrote down the
            # evidence — and the review skill is told to treat those as priority
            # findings. Passing only the count meant the worker had to re-derive
            # the finding from scratch and could silently miss it (pulumi/docs
            # #20927: a page boosted for a contradicted version pin was reviewed,
            # reported "0 contradicted" across 74 re-extracted claims, and merged
            # a one-line unrelated repair while the flagged bug stayed on master).
            "stale_claim_markers": all_markers(entry),
            "score": score,
        }

    # --paths: explicit override, no scoring, no guardrails (testing path).
    # The per-article worker passes --lane to carry the dispatcher's lane
    # through; without it entries are manual.
    if args.paths:
        lane = args.lane or "manual"
        for raw in args.paths.split(","):
            path = raw.strip()
            if not path:
                continue
            if path not in known:
                print(f"select-articles: --paths entry not found: {path}", file=sys.stderr)
                return 1
            queue["articles"].append(article(path, lane, None))
        return finish(queue, args, LANE)

    open_branches = open_review_branches(use_gh)
    if open_branches is None:
        # Can't dedup against open PRs -> opening more is unsafe. Halt loudly.
        queue["halted"] = "gh_unavailable"
        return finish(queue, args, LANE)
    if len(open_branches) >= MAX_OPEN_PRS:
        queue["halted"] = "max_open_prs"
        return finish(queue, args, LANE)
    open_slugs = {
        b[len(BRANCH_PREFIX):].removeprefix("retire-").removeprefix("glowup-")
        for b in open_branches
    }

    newest_non_bot, created = git_history_signals(repo, CONTENT_DIR)

    candidates: list[str] = []
    capped: list[str] = []
    for path in all_paths:
        policy = policy_for(path, tier_rules)
        if not eligible(policy, mode):
            continue
        if slugify(path) in open_slugs:
            continue
        if is_draft(repo / path):
            continue
        if is_redirect_stub(repo / path):
            continue
        entry = ledger.get(path)
        if entry and entry.get("status") == INCOMPLETE_STATUS \
                and int(entry.get("attempts", 0)) >= ATTEMPT_CAP:
            capped.append(path)
            continue
        candidates.append(path)

    queue["capped"] = sorted(capped)
    if capped:
        print(
            f"select-articles: {len(capped)} page(s) backed off at the "
            f"{ATTEMPT_CAP}-attempt cap (need a human): " + ", ".join(sorted(capped)[:10])
            + (" ..." if len(capped) > 10 else ""),
            file=sys.stderr,
        )

    def scored_entry(path: str) -> tuple[float, str]:
        gsc_m, fb_m, _ = signal_terms(path)
        return (
            score_page(
                tier_for(path, tier_rules)[0],
                traffic.get(path),
                max_visits,
                median_visits,
                effective_last_review(path, ledger.get(path), newest_non_bot, created),
                today,
                have_traffic,
                stale_claims=(bool(active_markers(ledger.get(path)))
                              and not boost_suppressed_by_recent_fix(
                                  ledger.get(path), today)),
                gsc_m=gsc_m,
                feedback_m=fb_m,
            ),
            path,
        )

    scored = sorted(
        (scored_entry(path) for path in candidates),
        key=lambda t: (-t[0], t[1]),
    )

    for score, path in scored[: max(args.count, 0)]:
        queue["articles"].append(article(path, "priority", score))

    return finish(queue, args, LANE)


def is_draft(file_path: Path) -> bool:
    try:
        head = file_path.read_text(errors="replace")[:4096]
    except OSError:
        return True
    m = FRONTMATTER_RE.match(head)
    if not m:
        return False
    try:
        fm = yaml.safe_load(m.group(1))
    except yaml.YAMLError:
        return False
    return bool(isinstance(fm, dict) and fm.get("draft"))


def is_redirect_stub(file_path: Path) -> bool:
    """A page whose frontmatter is a `redirect_to:` — a tombstone, not content.

    There is nothing on such a page to review, but with the traffic term
    floored these stubs scored like real pages and burned queue slots
    (organizing-stacks-projects.md: 1 visit/month, reviewed twice). The test
    is the `redirect_to` key specifically — NOT "small file with aliases",
    which misfires on legitimately tiny pages like reference/glossary.md.
    """
    try:
        head = file_path.read_text(errors="replace")[:4096]
    except OSError:
        return False
    m = FRONTMATTER_RE.match(head)
    if not m:
        return False
    try:
        fm = yaml.safe_load(m.group(1))
    except yaml.YAMLError:
        return False
    return bool(isinstance(fm, dict) and fm.get("redirect_to"))


if __name__ == "__main__":
    sys.exit(main())
