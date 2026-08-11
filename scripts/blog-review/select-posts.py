#!/usr/bin/env python3
"""Select existing blog posts for the daily known-issues review.

Deterministic pre-step for the blog-review-index workflow
(`.github/workflows/blog-review-index.yml`): given the S3-fetched traffic
snapshot, the optional reader-signals (Search Console) snapshot, and the
per-post review ledger, emit the day's review queue as JSON. The model never
chooses what to review — this script does, so the selection is auditable and
reproducible from its inputs.

This is the blog sibling of `scripts/content-review/select-articles.py`, and
it keeps that script's proven mechanics (single-pass git history read,
median-imputed log-normalized traffic, boost-only GSC multiplier,
path-ascending tie-break). The differences are deliberate:

  * The corpus is `content/blog/*/index.md` only (one bundle per post).
  * No strategic tiers (blogs aren't tiered) and no feedback-widget term
    (the widget is docs-only).
  * Posts published fewer than MIN_AGE_DAYS ago are excluded — fresh posts
    just went through the PR-time docs review; content rot needs time.
  * The never-reviewed staleness fallback is the post's frontmatter `date`
    (its publish date), not the git creation date: with no traffic snapshot
    the selection degrades to an oldest-unreviewed-first sweep.
  * No open-PR dedup and no MAX_OPEN_PRS halt: the review is flag-only
    (findings land in the S3 index; no PRs are opened), so there is nothing
    to guard. The `halted` output key is kept for shape parity with the docs
    queue, but is always null.

Selection algorithm (weighted fair queuing by staleness):

    score      = importance * staleness
    importance = (0.5 + 0.5 * traffic_n) * gsc_m     with a traffic snapshot
               = gsc_m                                without one
    traffic_n  = log1p(visits) / log1p(max_visits); posts missing from the
                 snapshot impute the median
    gsc_m      = 1 + 0.25 * impressions_n * ctr_gap, in [1.0, 1.25]: the
                 Search Console "opportunity" boost — only posts searchers
                 see a lot (high impressions) but rarely click (CTR below
                 the corpus median) boost. Boost-only with a floor of
                 exactly 1.0: a post absent from the export scores exactly
                 what it would have scored before the term existed.
    staleness  = (today - effective_last_review).days, floored at 0
    effective_last_review = max(completed bot review, newest non-bot commit)
                 where an `incomplete` review never advances the clock.
                 Never-reviewed posts fall back to their publish date.

    Ties break on path ascending, so runs are reproducible.

Hard filters: `draft: true`; posts younger than MIN_AGE_DAYS; posts whose
`incomplete` review already burned ATTEMPT_CAP retries (they back off and
are surfaced for a human instead of looping forever).

Usage:
    select-posts.py --count 5 --out .blog-review-queue.json
        [--traffic-file .blog-traffic-snapshot]
        [--signals-file .blog-reader-signals.json]
        [--ledger-dir .ledger-cache]
        [--paths content/blog/a/index.md,content/blog/b/index.md]
        [--today YYYY-MM-DD] [--dry-run]
    select-posts.py --stats   # ledger outcome report
    select-posts.py --prune   # GC ledger entries whose posts are gone

`--paths` bypasses scoring entirely (workflow_dispatch testing). `--today`
exists for tests. When `$GITHUB_OUTPUT` is set, the script appends
`has_posts=`, `halted=`, and `count=` for workflow gating.
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
DEFAULT_LEDGER_DIR = REPO_ROOT / "scripts/blog-review/ledger"
CONTENT_DIR = "content/blog"

# An `incomplete` review (worker exited before recording valid findings)
# never advances the staleness clock, so the post stays due and is retried
# next sweep. This caps the retries: once a post has burned ATTEMPT_CAP
# incomplete runs it backs off (is excluded and surfaced) instead of looping
# forever on whatever keeps breaking it.
ATTEMPT_CAP = 3

# Posts younger than this never enter the queue: they were just reviewed at
# PR time by the pre-merge docs review, and the rot this process hunts for
# (dead links, deprecated products, stale facts) needs time to accumulate.
MIN_AGE_DAYS = 90

# Search Console boost tuning — same shape and rationale as the docs
# selector: the multiplier floors at exactly 1.0 (absent posts score exactly
# as if the export never existed) and caps well under the traffic spread, so
# it reorders comparably stale peers without overriding staleness.
GSC_MIN_IMPRESSIONS = 200  # below this, CTR is noise -> neutral
GSC_BOOST_MAX = 0.25  # gsc multiplier in [1.0, 1.25]

# Statuses a ledger entry can carry (set by record-findings.py). Any status
# other than "incomplete" is a completed review whose date advances the clock.
INCOMPLETE_STATUS = "incomplete"

# "Pulumi Bot" (display name) is how the SDK-regen tooling authors its
# commits; "pulumi-bot" is how the review workflows configure git. Both are
# the same bot and neither resets a post's staleness clock, and neither does
# "workprentice[bot]", the docs automation app.
BOT_AUTHORS = {
    "pulumi-bot", "Pulumi Bot", "workprentice[bot]",
    "dependabot[bot]", "github-actions[bot]",
}

FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)


# ---- Path helpers -----------------------------------------------------------


def slugify(content_path: str) -> str:
    """content/blog/my-post/index.md -> my-post"""
    p = content_path
    if p.startswith(f"{CONTENT_DIR}/"):
        p = p[len(f"{CONTENT_DIR}/") :]
    if p.endswith("/index.md"):
        p = p[: -len("/index.md")]
    return p.replace("/", "-")


def url_for(content_path: str) -> str:
    """content/blog/my-post/index.md -> /blog/my-post/"""
    p = content_path
    if p.startswith("content/"):
        p = p[len("content/") :]
    if p.endswith("/index.md"):
        p = p[: -len("/index.md")]
    return f"/{p}/"


def content_path_for_url(url_path: str, known_paths: set[str]) -> str | None:
    """Map a live /blog/... URL path back to its content bundle, if it exists."""
    p = url_path.split("#", 1)[0].split("?", 1)[0].strip()
    if p.startswith("https://"):
        p = re.sub(r"^https://[^/]+", "", p)
    p = "/" + p.strip("/")
    candidate = f"content{p}/index.md"
    if candidate in known_paths:
        return candidate
    return None


# ---- Input loading ----------------------------------------------------------


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
            # A URL and its aliases may both appear; credit the same post once
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


def load_reader_signals(
    signals_file: Path | None, known_paths: set[str]
) -> tuple[dict[str, dict], dict]:
    """Parse the reader-signals snapshot into a per-post GSC map.

    Same contract as the docs selector's export (independently optional
    sections under `signals`), but blogs consume only the `gsc` section —
    there is no feedback widget on blog pages.

    Returns (gsc, meta). A missing/unreadable/malformed file degrades the
    signal to unavailable: selection then scores exactly as if the export
    never existed.
    """
    meta = {
        "gsc": {"available": False, "source": None, "period": None,
                "pages_matched": 0, "median_ctr": None, "max_impressions": None},
    }
    gsc: dict[str, dict] = {}
    if signals_file is None or not signals_file.is_file():
        return gsc, meta
    try:
        data = json.loads(signals_file.read_text(errors="replace"))
    except (OSError, json.JSONDecodeError):
        return gsc, meta
    if not isinstance(data, dict):
        return gsc, meta
    sections = data.get("signals")
    if not isinstance(sections, dict):
        return gsc, meta

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
            # A URL and its aliases may both appear; keep the row with the
            # larger figure rather than double-counting.
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

    return gsc, meta


def load_ledger(ledger_dir: Path) -> dict[str, dict]:
    """Return {content_path: ledger entry} from one-file-per-post JSON."""
    entries: dict[str, dict] = {}
    if not ledger_dir.is_dir():
        # Not fatal — the workflow only passes --ledger-dir when the S3 sync
        # produced one — but never silent: with no ledger every post scores as
        # never-reviewed, which is a very different queue. DEFAULT_LEDGER_DIR is
        # the in-repo path this script has never actually had, so a run that
        # falls back to it is one that meant to read the S3 cache and didn't.
        print(
            f"select-posts: no ledger directory at {ledger_dir}; scoring every "
            "post as never-reviewed",
            file=sys.stderr,
        )
        return entries
    for f in sorted(ledger_dir.glob("*.json")):
        try:
            entry = json.loads(f.read_text())
        except (OSError, json.JSONDecodeError):
            print(f"select-posts: unreadable ledger file {f}", file=sys.stderr)
            continue
        path = entry.get("path")
        if path:
            entry["_file"] = str(f)
            entries[path] = entry
    return entries


# ---- Frontmatter ------------------------------------------------------------


def read_frontmatter(file_path: Path) -> dict:
    try:
        head = file_path.read_text(errors="replace")[:8192]
    except OSError:
        return {}
    m = FRONTMATTER_RE.match(head)
    if not m:
        return {}
    try:
        fm = yaml.safe_load(m.group(1))
    except yaml.YAMLError:
        return {}
    return fm if isinstance(fm, dict) else {}


def is_draft(fm: dict) -> bool:
    return bool(fm.get("draft"))


def publish_date(fm: dict) -> date | None:
    d = fm.get("date")
    if isinstance(d, datetime):
        return d.date()
    if isinstance(d, date):
        return d
    return parse_day(str(d)) if d else None


# ---- Git signals (single-pass, no per-file subprocess fan-out) ---------------


def git_history_signals(repo: Path) -> tuple[dict[str, int], dict[str, int]]:
    """Per-path git timestamps for content/blog, from one history pass.

    Walks history newest-first and returns two maps of unix commit times:

      newest_non_bot : the most recent commit by a *non-bot* author that
                       touched the path (a human edit — resets the staleness
                       clock). Absent for posts only ever touched by bots.
      created        : the oldest commit that touched the path, the fallback
                       clock when a post's frontmatter carries no usable date.
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
    published: date | None,
    created: dict[str, int],
) -> date | None:
    """The date the staleness clock is measured from.

    max(completed bot review, newest human edit); an `incomplete` review does
    not count, so the post stays due. Never-reviewed posts fall back to their
    publish date (frontmatter `date`), then to the git creation date. None
    only when the post has no usable date at all.
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
    return published or _ts_to_day(created.get(path))


def gsc_multiplier(
    entry: dict | None, max_impressions: int | None, median_ctr: float | None
) -> tuple[float, float]:
    """(multiplier in [1, 1+GSC_BOOST_MAX], opportunity in [0, 1]).

    Opportunity is impressions_n * ctr_gap: only the high-impressions AND
    below-median-CTR quadrant boosts. Posts absent from the export or under
    GSC_MIN_IMPRESSIONS are neutral.
    """
    if (
        not entry
        or entry["impressions"] < GSC_MIN_IMPRESSIONS
        or not max_impressions
        or not median_ctr
    ):
        return 1.0, 0.0
    impressions_n = math.log1p(entry["impressions"]) / math.log1p(max_impressions)
    ctr_gap = min(max(median_ctr - entry["ctr"], 0.0) / median_ctr, 1.0)
    opportunity = min(impressions_n * ctr_gap, 1.0)
    return 1.0 + GSC_BOOST_MAX * opportunity, round(opportunity, 4)


def importance(
    visits: int | None,
    max_visits: int,
    median_visits: int,
    have_traffic: bool,
    gsc_m: float = 1.0,
) -> float:
    """Traffic weight when a snapshot is available; neutral 1.0 otherwise."""
    if have_traffic and max_visits > 0:
        v = visits if visits is not None else median_visits
        traffic_n = math.log1p(v) / math.log1p(max_visits)
        return (0.5 + 0.5 * traffic_n) * gsc_m
    return gsc_m


def score_post(
    visits: int | None,
    max_visits: int,
    median_visits: int,
    last_review: date | None,
    today: date,
    have_traffic: bool,
    gsc_m: float = 1.0,
) -> float:
    staleness = max((today - last_review).days, 0) if last_review else 0
    return round(
        importance(visits, max_visits, median_visits, have_traffic, gsc_m) * staleness,
        4,
    )


# ---- Subcommands ---------------------------------------------------------------


def cmd_stats(ledger_dir: Path) -> int:
    entries = load_ledger(ledger_dir)
    counts = {"reviewed": 0, "clean": 0, "skipped": 0,
              "incomplete": 0, "capped": 0, "other": 0}
    with_issues = 0
    for path, entry in sorted(entries.items()):
        status = entry.get("status")
        if status == INCOMPLETE_STATUS:
            counts["incomplete"] += 1
            if int(entry.get("attempts", 0)) >= ATTEMPT_CAP:
                counts["capped"] += 1
            continue
        if status in counts:
            counts[status] += 1
        else:
            counts["other"] += 1
        if int(entry.get("issues", 0)) > 0:
            with_issues += 1
    print(json.dumps({"entries": len(entries), "outcomes": counts,
                      "posts_with_issues": with_issues}, indent=2))
    return 0


def cmd_prune(ledger_dir: Path, repo: Path, dry_run: bool) -> int:
    pruned = []
    for path, entry in load_ledger(ledger_dir).items():
        if not (repo / path).is_file():
            pruned.append(entry["_file"])
            if not dry_run:
                Path(entry["_file"]).unlink()
    verb = "would prune" if dry_run else "pruned"
    print(f"select-posts: {verb} {len(pruned)} orphaned ledger file(s)")
    for f in pruned:
        print(f"  {f}")
    return 0


# ---- Main ----------------------------------------------------------------------


def write_github_output(queue: dict) -> None:
    gh_out = os.environ.get("GITHUB_OUTPUT")
    if not gh_out:
        return
    with open(gh_out, "a") as fh:
        fh.write(f"has_posts={'true' if queue['posts'] else 'false'}\n")
        fh.write(f"halted={queue.get('halted') or ''}\n")
        fh.write(f"count={len(queue['posts'])}\n")


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--count", type=int, default=5)
    p.add_argument("--out", help="Queue JSON output path")
    p.add_argument("--traffic-file", help="S3-fetched traffic snapshot (CSV or JSON)")
    p.add_argument("--signals-file", help="S3-fetched reader-signals snapshot (JSON)")
    p.add_argument("--ledger-dir", default=str(DEFAULT_LEDGER_DIR))
    p.add_argument("--repo-root", default=str(REPO_ROOT), help=argparse.SUPPRESS)
    p.add_argument("--paths", help="Comma-separated content paths; bypasses scoring (testing)")
    p.add_argument("--lane", help="Override lane for --paths entries (default manual)")
    p.add_argument("--today", help="Override today's date YYYY-MM-DD (testing)")
    p.add_argument("--dry-run", action="store_true", help="Print queue, write nothing")
    p.add_argument("--stats", action="store_true", help="Report ledger outcomes and exit")
    p.add_argument("--prune", action="store_true", help="GC ledger entries for deleted posts")
    args = p.parse_args()

    repo = Path(args.repo_root)
    ledger_dir = Path(args.ledger_dir)

    if args.stats:
        return cmd_stats(ledger_dir)
    if args.prune:
        return cmd_prune(ledger_dir, repo, args.dry_run)
    if not args.out and not args.dry_run:
        p.error("--out is required (or use --dry-run/--stats/--prune)")

    today = parse_day(args.today) or datetime.now(timezone.utc).date()
    ledger = load_ledger(ledger_dir)

    all_paths = sorted(
        str(f.relative_to(repo)) for f in (repo / CONTENT_DIR).glob("*/index.md")
    )
    known = set(all_paths)
    frontmatter = {path: read_frontmatter(repo / path) for path in all_paths}

    traffic, traffic_meta = load_traffic(
        Path(args.traffic_file) if args.traffic_file else None, known
    )
    have_traffic = bool(traffic)
    visits_known = sorted(traffic.values())
    max_visits = visits_known[-1] if visits_known else 0
    median_visits = visits_known[len(visits_known) // 2] if visits_known else 0

    gsc, signals_meta = load_reader_signals(
        Path(args.signals_file) if args.signals_file else None, known
    )
    signals_available = signals_meta["gsc"]["available"]

    queue: dict = {
        "generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "count": 0,
        "halted": None,
        "traffic": {**traffic_meta, "available": have_traffic},
        "reader_signals": {"available": signals_available, **signals_meta},
        "posts": [],
    }

    def signal_terms(path: str) -> tuple[float, dict | None]:
        """(gsc_m, per-post signals block) — one source for both scoring and
        the queue entry, so they can't diverge."""
        if not signals_available:
            return 1.0, None
        gsc_entry = gsc.get(path)
        gsc_m, opportunity = gsc_multiplier(
            gsc_entry, signals_meta["gsc"]["max_impressions"], signals_meta["gsc"]["median_ctr"]
        )
        return gsc_m, {
            "gsc": {
                "impressions": gsc_entry["impressions"],
                "ctr": gsc_entry["ctr"],
                "opportunity": opportunity,
                "multiplier": round(gsc_m, 4),
            } if gsc_entry else None,
        }

    def post(path: str, lane: str, score: float | None) -> dict:
        entry = ledger.get(path, {})
        pub = publish_date(frontmatter.get(path, {}))
        return {
            "path": path,
            "url": url_for(path),
            "slug": slugify(path),
            "lane": lane,
            "post_date": pub.isoformat() if pub else None,
            "monthly_visits": traffic.get(path),
            "signals": signal_terms(path)[1],
            "last_reviewed": entry.get("reviewed_at"),
            "attempts": int(entry.get("attempts", 0)),
            "score": score,
        }

    # --paths: explicit override, no scoring, no filters (testing path).
    if args.paths:
        lane = args.lane or "manual"
        for raw in args.paths.split(","):
            path = raw.strip()
            if not path:
                continue
            if path not in known:
                print(f"select-posts: --paths entry not found: {path}", file=sys.stderr)
                return 1
            queue["posts"].append(post(path, lane, None))
        return finish(queue, args)

    newest_non_bot, created = git_history_signals(repo)

    candidates: list[str] = []
    capped: list[str] = []
    for path in all_paths:
        fm = frontmatter.get(path, {})
        if is_draft(fm):
            continue
        pub = publish_date(fm)
        if pub and (today - pub).days < MIN_AGE_DAYS:
            continue
        entry = ledger.get(path)
        if entry and entry.get("status") == INCOMPLETE_STATUS \
                and int(entry.get("attempts", 0)) >= ATTEMPT_CAP:
            capped.append(path)
            continue
        candidates.append(path)

    if capped:
        print(
            f"select-posts: {len(capped)} post(s) backed off at the "
            f"{ATTEMPT_CAP}-attempt cap (need a human): " + ", ".join(sorted(capped)[:10])
            + (" ..." if len(capped) > 10 else ""),
            file=sys.stderr,
        )

    def scored_entry(path: str) -> tuple[float, str]:
        gsc_m, _ = signal_terms(path)
        return (
            score_post(
                traffic.get(path),
                max_visits,
                median_visits,
                effective_last_review(
                    path, ledger.get(path), newest_non_bot,
                    publish_date(frontmatter.get(path, {})), created,
                ),
                today,
                have_traffic,
                gsc_m=gsc_m,
            ),
            path,
        )

    scored = sorted(
        (scored_entry(path) for path in candidates),
        key=lambda t: (-t[0], t[1]),
    )

    for score, path in scored[: max(args.count, 0)]:
        queue["posts"].append(post(path, "priority", score))

    return finish(queue, args)


def finish(queue: dict, args) -> int:
    queue["count"] = len(queue["posts"])
    body = json.dumps(queue, indent=2)
    if args.dry_run or not args.out:
        print(body)
    else:
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(body + "\n")
        print(
            f"select-posts: {queue['count']} post(s)"
            + (f" (halted: {queue['halted']})" if queue["halted"] else "")
            + f" → {out}",
            file=sys.stderr,
        )
    write_github_output(queue)
    return 0


if __name__ == "__main__":
    sys.exit(main())
