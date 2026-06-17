#!/usr/bin/env python3
"""Select existing content pages for automated review.

Deterministic pre-step for the review-existing-content workflow
(`.github/workflows/review-existing-content.yml`): given the strategic tier
map, the S3-fetched traffic snapshot, and the per-page review ledger, emit
the day's review queue as JSON. The model never chooses what to review —
this script does, so the selection is auditable and reproducible from its
inputs.

Selection algorithm (weighted fair queuing by staleness):

1. Enumerate `content/docs/**/*.md`; drop tier-0 (generated/synced) paths
   and `draft: true` pages.
2. Hard filters: pages with an open `content-review/<slug>` bot PR; pages
   whose `incomplete` review has already burned ATTEMPT_CAP retries (they
   back off and are surfaced for a human instead of looping forever).
3. Runaway guardrail: if >= MAX_OPEN_PRS open `content-review/*` PRs exist,
   emit an empty queue with `"halted": "max_open_prs"` so the workflow
   warns instead of piling on.
4. Score every remaining page and take the top `count`. No threshold, no
   reserved lane — staleness self-corrects starvation (the longer a page
   goes unreviewed the higher it climbs, so the whole corpus is swept):

       score = importance * staleness

   importance = tier_w * (0.5 + 0.5*traffic_n)   with a traffic snapshot
              = tier_w                            tier-only when absent
   tier_w     = {1: 1.0, 2: 0.6, 3: 0.3}
   traffic_n  = log1p(visits) / log1p(max_visits); pages missing from the
                report impute the median
   staleness  = (today - effective_last_review).days, floored at 0
   effective_last_review = max(bot_reviewed_at, last_non-bot_commit_date)
                where bot_reviewed_at counts only for a *completed* review
                (an `incomplete` outcome never advances the clock, so the
                page stays due). Never-bot-reviewed pages fall back to their
                git creation date: a brand-new page sorts to the back, an
                ancient never-reviewed page to the front. A human (non-bot)
                edit fully resets the clock.

   Ties break on path ascending, so runs are reproducible.

Usage:
    select-articles.py --count 3 --out .content-review-queue.json
        [--traffic-file .traffic-snapshot] [--tiers <yaml>]
        [--ledger-dir scripts/content-review/ledger]
        [--paths content/docs/a.md,content/docs/b/_index.md]
        [--no-gh] [--today YYYY-MM-DD] [--dry-run]
    select-articles.py --stats   # ledger outcome report (merged/closed/open)
    select-articles.py --prune   # GC ledger entries whose pages are gone

`--paths` bypasses scoring entirely (workflow_dispatch testing). `--no-gh`
and `--today` exist for tests. When `$GITHUB_OUTPUT` is set, the script
appends `has_articles=`, `halted=`, and `count=` for workflow gating.
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import math
import os
import re
import subprocess
import sys
from datetime import date, datetime, timezone
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_TIERS = (
    REPO_ROOT
    / ".claude/commands/review-existing-content/references/strategic-tiers.yaml"
)
DEFAULT_LEDGER_DIR = REPO_ROOT / "scripts/content-review/ledger"
CONTENT_DIR = "content/docs"

BRANCH_PREFIX = "content-review/"
MAX_OPEN_PRS = 9
# An `incomplete` review (worker exited before recording a verdict, or claimed
# a fix with no PR) never advances the staleness clock, so the page stays due
# and is retried next sweep. This caps the retries: once a page has burned
# ATTEMPT_CAP incomplete runs it backs off (is excluded and surfaced) instead
# of looping forever on whatever keeps breaking it.
ATTEMPT_CAP = 3

TIER_WEIGHTS = {1: 1.0, 2: 0.6, 3: 0.3}

# Statuses a ledger entry can carry (set by record-review.py). Any status other
# than "incomplete" is a completed review whose date advances the clock; legacy
# entries predating the field have no `status` and are treated as completed.
INCOMPLETE_STATUS = "incomplete"

BOT_AUTHORS = {"pulumi-bot", "dependabot[bot]", "github-actions[bot]"}

FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)


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
    p = url_path.split("#", 1)[0].split("?", 1)[0].strip()
    if p.startswith("https://"):
        p = re.sub(r"^https://[^/]+", "", p)
    p = "/" + p.strip("/")
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


def tier_for(path: str, rules: list[dict]) -> tuple[int, bool]:
    """Longest-prefix match wins. Returns (tier, no_retire)."""
    for rule in rules:
        if path.startswith(rule.get("prefix", "")):
            tier = int(rule.get("tier", 3))
            no_retire = bool(rule.get("no_retire", False)) or tier == 1
            return tier, no_retire
    return 3, False


def load_traffic(traffic_file: Path | None, known_paths: set[str]) -> tuple[dict[str, int], dict]:
    """Parse the S3 traffic snapshot (JSON or CSV) into {content_path: visits}.

    Returns ({}, meta) when the file is missing/unreadable — selection then
    drops the traffic term entirely (graceful degradation).
    """
    meta = {"source": None, "period": None, "pages_matched": 0}
    if traffic_file is None or not traffic_file.is_file():
        return {}, meta
    raw = traffic_file.read_text(errors="replace").strip()
    if not raw:
        return {}, meta

    pages: dict[str, int] = {}

    def record(url_path: str, views) -> None:
        try:
            views = int(float(views))
        except (TypeError, ValueError):
            return
        cp = content_path_for_url(str(url_path), known_paths)
        if cp:
            # A URL and its aliases may both appear; credit the same file once
            # with the larger figure rather than double-counting.
            pages[cp] = max(pages.get(cp, 0), views)

    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        data = None

    if isinstance(data, dict):
        meta["source"] = data.get("source")
        meta["period"] = data.get("period") or data.get("generated")
        body = data.get("pages", data)
        if isinstance(body, dict):
            for url_path, views in body.items():
                record(url_path, views)
    elif data is None:
        # CSV: `path,views` with an optional header row.
        reader = csv.reader(io.StringIO(raw))
        for row in reader:
            if len(row) < 2:
                continue
            record(row[0], row[1])

    meta["pages_matched"] = len(pages)
    return pages, meta


def load_ledger(ledger_dir: Path) -> dict[str, dict]:
    """Return {content_path: ledger entry} from one-file-per-page JSON."""
    entries: dict[str, dict] = {}
    if not ledger_dir.is_dir():
        return entries
    for f in sorted(ledger_dir.glob("*.json")):
        try:
            entry = json.loads(f.read_text())
        except (OSError, json.JSONDecodeError):
            print(f"select-articles: unreadable ledger file {f}", file=sys.stderr)
            continue
        path = entry.get("path")
        if path:
            entry["_file"] = str(f)
            entries[path] = entry
    return entries


# ---- Git signals (single-pass, no per-file subprocess fan-out) ---------------


def git_history_signals(repo: Path) -> tuple[dict[str, int], dict[str, int]]:
    """Per-path git timestamps for content/docs, from one history pass.

    Walks history newest-first and returns two maps of unix commit times:

      newest_non_bot : the most recent commit by a *non-bot* author that
                       touched the path (a human edit — resets the staleness
                       clock). Absent for pages only ever touched by bots.
      created        : the oldest commit that touched the path (its creation),
                       the fallback clock for never-bot-reviewed pages.
    """
    out = run_git(repo, ["log", "--name-only", "--format=%x01%ct%x01%an", "--", CONTENT_DIR])
    newest_non_bot: dict[str, int] = {}
    created: dict[str, int] = {}
    current_ct = 0
    author_is_bot = True
    for line in out.splitlines():
        if line.startswith("\x01"):
            # Header line is "\x01<commit-time>\x01<author-name>".
            parts = line.split("\x01")
            ct = parts[1] if len(parts) > 1 else ""
            an = parts[2] if len(parts) > 2 else ""
            try:
                current_ct = int(ct.strip())
            except ValueError:
                current_ct = 0
            author_is_bot = an.strip() in BOT_AUTHORS
        elif line.strip():
            path = line.strip()
            created[path] = current_ct  # last write wins -> oldest commit
            if not author_is_bot and path not in newest_non_bot:
                newest_non_bot[path] = current_ct
    return newest_non_bot, created


def run_git(repo: Path, args: list[str]) -> str:
    proc = subprocess.run(
        ["git", "-C", str(repo), *args], capture_output=True, text=True, check=False
    )
    return proc.stdout


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


def parse_day(s: str | None) -> date | None:
    if not s:
        return None
    try:
        return datetime.fromisoformat(str(s).replace("Z", "+00:00")).date()
    except ValueError:
        try:
            return datetime.strptime(str(s), "%Y-%m-%d").date()
        except ValueError:
            return None


def _ts_to_day(ts: int | None) -> date | None:
    if not ts:
        return None
    return datetime.fromtimestamp(ts, tz=timezone.utc).date()


def effective_last_review(
    path: str,
    entry: dict | None,
    newest_non_bot: dict[str, int],
    created: dict[str, int],
) -> date | None:
    """The date the staleness clock is measured from.

    max(completed bot review, newest human edit); an `incomplete` review does
    not count, so the page stays due. Never-bot-reviewed pages fall back to the
    git creation date. None only when the page has no git history at all.
    """
    cands: list[date] = []
    if entry:
        reviewed = parse_day(entry.get("reviewed_at"))
        if reviewed and entry.get("status") != INCOMPLETE_STATUS:
            cands.append(reviewed)
    human = _ts_to_day(newest_non_bot.get(path))
    if human:
        cands.append(human)
    if cands:
        return max(cands)
    return _ts_to_day(created.get(path))


def importance(
    tier: int,
    visits: int | None,
    max_visits: int,
    median_visits: int,
    have_traffic: bool,
) -> float:
    """Strategic weight, modulated by traffic when a snapshot is available."""
    tier_w = TIER_WEIGHTS.get(tier, TIER_WEIGHTS[3])
    if have_traffic and max_visits > 0:
        v = visits if visits is not None else median_visits
        traffic_n = math.log1p(v) / math.log1p(max_visits)
        return tier_w * (0.5 + 0.5 * traffic_n)
    return tier_w


def score_page(
    tier: int,
    visits: int | None,
    max_visits: int,
    median_visits: int,
    last_review: date | None,
    today: date,
    have_traffic: bool,
) -> float:
    staleness = max((today - last_review).days, 0) if last_review else 0
    return round(importance(tier, visits, max_visits, median_visits, have_traffic) * staleness, 4)


# ---- Subcommands ---------------------------------------------------------------


def cmd_stats(ledger_dir: Path, use_gh: bool) -> int:
    entries = load_ledger(ledger_dir)
    counts = {"merged": 0, "closed": 0, "open": 0, "clean": 0,
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


def cmd_prune(ledger_dir: Path, repo: Path, dry_run: bool) -> int:
    pruned = []
    for path, entry in load_ledger(ledger_dir).items():
        if not (repo / path).is_file():
            pruned.append(entry["_file"])
            if not dry_run:
                Path(entry["_file"]).unlink()
    verb = "would prune" if dry_run else "pruned"
    print(f"select-articles: {verb} {len(pruned)} orphaned ledger file(s)")
    for f in pruned:
        print(f"  {f}")
    return 0


# ---- Main ----------------------------------------------------------------------


def write_github_output(queue: dict) -> None:
    gh_out = os.environ.get("GITHUB_OUTPUT")
    if not gh_out:
        return
    with open(gh_out, "a") as fh:
        fh.write(f"has_articles={'true' if queue['articles'] else 'false'}\n")
        fh.write(f"halted={queue.get('halted') or ''}\n")
        fh.write(f"count={len(queue['articles'])}\n")


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--count", type=int, default=3)
    p.add_argument("--out", help="Queue JSON output path")
    p.add_argument("--traffic-file", help="S3-fetched traffic snapshot (CSV or JSON)")
    p.add_argument("--tiers", default=str(DEFAULT_TIERS))
    p.add_argument("--ledger-dir", default=str(DEFAULT_LEDGER_DIR))
    p.add_argument("--repo-root", default=str(REPO_ROOT), help=argparse.SUPPRESS)
    p.add_argument("--paths", help="Comma-separated content paths; bypasses scoring (testing)")
    p.add_argument("--lane", help="Override lane for --paths entries (default manual)")
    p.add_argument("--no-gh", action="store_true", help="Skip gh API calls (testing)")
    p.add_argument("--today", help="Override today's date YYYY-MM-DD (testing)")
    p.add_argument("--dry-run", action="store_true", help="Print queue, write nothing")
    p.add_argument("--stats", action="store_true", help="Report ledger outcomes and exit")
    p.add_argument("--prune", action="store_true", help="GC ledger entries for deleted pages")
    args = p.parse_args()

    repo = Path(args.repo_root)
    ledger_dir = Path(args.ledger_dir)
    use_gh = not args.no_gh

    if args.stats:
        return cmd_stats(ledger_dir, use_gh)
    if args.prune:
        return cmd_prune(ledger_dir, repo, args.dry_run)
    if not args.out and not args.dry_run:
        p.error("--out is required (or use --dry-run/--stats/--prune)")

    today = parse_day(args.today) or datetime.now(timezone.utc).date()
    tier_rules = load_tiers(Path(args.tiers))
    ledger = load_ledger(ledger_dir)

    all_paths = sorted(
        str(f.relative_to(repo)) for f in (repo / CONTENT_DIR).rglob("*.md")
    )
    known = set(all_paths)
    traffic, traffic_meta = load_traffic(
        Path(args.traffic_file) if args.traffic_file else None, known
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

    def article(path: str, lane: str, score: float | None) -> dict:
        tier, no_retire = tier_for(path, tier_rules)
        entry = ledger.get(path, {})
        return {
            "path": path,
            "url": url_for(path),
            "slug": slugify(path),
            "lane": lane,
            "tier": tier,
            "no_retire": no_retire,
            "monthly_visits": traffic.get(path),
            "last_reviewed": entry.get("reviewed_at"),
            "attempts": int(entry.get("attempts", 0)),
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
        return finish(queue, args)

    open_branches = open_review_branches(use_gh)
    if open_branches is None:
        # Can't dedup against open PRs -> opening more is unsafe. Halt loudly.
        queue["halted"] = "gh_unavailable"
        return finish(queue, args)
    if len(open_branches) >= MAX_OPEN_PRS:
        queue["halted"] = "max_open_prs"
        return finish(queue, args)
    open_slugs = {b[len(BRANCH_PREFIX):].removeprefix("retire-") for b in open_branches}

    newest_non_bot, created = git_history_signals(repo)

    candidates: list[str] = []
    capped: list[str] = []
    for path in all_paths:
        tier, _ = tier_for(path, tier_rules)
        if tier == 0:
            continue
        if slugify(path) in open_slugs:
            continue
        if is_draft(repo / path):
            continue
        entry = ledger.get(path)
        if entry and entry.get("status") == INCOMPLETE_STATUS \
                and int(entry.get("attempts", 0)) >= ATTEMPT_CAP:
            capped.append(path)
            continue
        candidates.append(path)

    if capped:
        print(
            f"select-articles: {len(capped)} page(s) backed off at the "
            f"{ATTEMPT_CAP}-attempt cap (need a human): " + ", ".join(sorted(capped)[:10])
            + (" ..." if len(capped) > 10 else ""),
            file=sys.stderr,
        )

    scored = sorted(
        (
            (
                score_page(
                    tier_for(path, tier_rules)[0],
                    traffic.get(path),
                    max_visits,
                    median_visits,
                    effective_last_review(path, ledger.get(path), newest_non_bot, created),
                    today,
                    have_traffic,
                ),
                path,
            )
            for path in candidates
        ),
        key=lambda t: (-t[0], t[1]),
    )

    for score, path in scored[: max(args.count, 0)]:
        queue["articles"].append(article(path, "priority", score))

    return finish(queue, args)


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


def finish(queue: dict, args) -> int:
    queue["count"] = len(queue["articles"])
    body = json.dumps(queue, indent=2)
    if args.dry_run or not args.out:
        print(body)
    else:
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(body + "\n")
        print(
            f"select-articles: {queue['count']} article(s)"
            + (f" (halted: {queue['halted']})" if queue["halted"] else "")
            + f" → {out}",
            file=sys.stderr,
        )
    write_github_output(queue)
    return 0


if __name__ == "__main__":
    sys.exit(main())
