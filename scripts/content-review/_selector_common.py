"""Infrastructure shared by the two review-queue selectors.

`scripts/content-review/select-articles.py` (docs pages) and
`scripts/blog-review/select-posts.py` (blog posts) are deliberately separate
selectors — they score different corpora against different signals — but they
sit on the same plumbing: the same bot-author list, the same single-pass git
history read, the same ledger loader, the same date parsing, the same
`$GITHUB_OUTPUT` and queue-writing tail. This module is that plumbing, held in
exactly one place.

Why it exists, so nobody re-inlines it later
--------------------------------------------
BOT_AUTHORS was copied rather than shared, and the copies drifted. "Pulumi Bot"
and "workprentice[bot]" were added to one selector's set after a bot touch was
found resetting the staleness clock on ~65% of `content/docs` pages — and the
fix was never back-ported, so on the other lane bot commits went on looking
like human edits. That is the whole argument for this file: a duplicated
constant does not stay in sync, and nothing in either script made the drift
visible.

So: anything genuinely common lives here and only here. "Keeping the selector
self-contained" is precisely what caused the bug.

What deliberately stays duplicated
----------------------------------
The *scoring* does not belong here — tier weights, the GSC/feedback tuning
constants, the multipliers, each lane's URL-to-path mapping, and each lane's
retry cap. Those legitimately differ per corpus, and a shared knob that
silently retuned the other lane would be this bug wearing a different hat.
Where a helper differs only in wording or in one value, the difference is
passed in explicitly (see `Lane`) rather than smoothed over — a caller that has
to name its own noun cannot accidentally inherit the other lane's behavior.

Import path
-----------
`select-posts.py` lives in a sibling directory, so both scripts bootstrap onto
this module with an explicit `sys.path` insert anchored on `__file__` (see the
import block in each). That works for every way they are invoked: as
`python3 scripts/<dir>/<name>.py` from the repo root (how the workflows run
them), directly, and loaded by path via `importlib` from elsewhere in the tree
(`record-review.py`, `check-retire-veto.py`, `record-claims.py`,
`snippet-sweep/sweep.py` all do this).

Standard library only — no third-party imports, so neither lane grows a
dependency by reaching for a helper.
"""

from __future__ import annotations

import csv
import io
import json
import os
import re
import subprocess
import sys
from collections.abc import Callable
from dataclasses import dataclass
from datetime import date, datetime, timezone
from pathlib import Path

# "Pulumi Bot" (display name) is how the SDK-regen tooling authors its commits
# and "pulumi-bot" is how the review workflows configure git — the same bot
# either way; "workprentice[bot]" is the docs automation app. None of them is a
# human edit, so none resets a page's staleness clock. Missing names here are
# expensive: a single bot touch would otherwise look like a fresh human edit and
# park the page at the back of the queue.
BOT_AUTHORS = {
    "pulumi-bot", "Pulumi Bot", "workprentice[bot]",
    "dependabot[bot]", "github-actions[bot]",
}

# Statuses a ledger entry can carry (set by record-review.py / record-findings.py).
# Any status other than "incomplete" is a completed review whose date advances
# the clock; legacy entries predating the field have no `status` and are treated
# as completed.
INCOMPLETE_STATUS = "incomplete"

FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)


@dataclass(frozen=True)
class Lane:
    """Every per-lane string and flag a shared helper needs, in one object.

    The helpers below are identical across the two selectors *except* for how
    they address the reader: which prefix they log under, which key holds the
    queue's items, what a corpus entry is called. Collecting those here keeps
    the differences visible and reviewable in one place instead of scattered
    through five keyword arguments — and makes each per-lane asymmetry hard
    to acquire by accident.
    """

    prog: str  # log prefix: "select-articles" / "select-posts"
    items_key: str  # queue key holding the selected items: "articles" / "posts"
    corpus_noun: str  # what the corpus is made of: "page" / "post"
    item_noun: str  # what a queue entry is: "article" / "post"
    has_output: str  # $GITHUB_OUTPUT boolean key: "has_articles" / "has_posts"


# ---- Git signals (single-pass, no per-file subprocess fan-out) ---------------


def run_git(repo: Path, args: list[str]) -> str:
    proc = subprocess.run(
        ["git", "-C", str(repo), *args], capture_output=True, text=True, check=False
    )
    return proc.stdout


def git_history_signals(repo: Path, content_dir: str) -> tuple[dict[str, int], dict[str, int]]:
    """Per-path git timestamps for `content_dir`, from one history pass.

    Walks history newest-first and returns two maps of unix commit times:

      newest_non_bot : the most recent commit by a *non-bot* author that
                       touched the path (a human edit — resets the staleness
                       clock). Absent for entries only ever touched by bots.
      created        : the oldest commit that touched the path (its creation),
                       the fallback clock when nothing else dates the entry.
    """
    out = run_git(repo, ["log", "--name-only", "--format=%x01%ct%x01%an", "--", content_dir])
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


# ---- Dates -------------------------------------------------------------------


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


def ts_to_day(ts: int | None) -> date | None:
    if not ts:
        return None
    return datetime.fromtimestamp(ts, tz=timezone.utc).date()


def effective_last_review(
    path: str,
    entry: dict | None,
    newest_non_bot: dict[str, int],
    created: dict[str, int],
    fallback: date | None = None,
) -> date | None:
    """The date the staleness clock is measured from.

    max(completed bot review, newest human edit); an `incomplete` review does
    not count, so the entry stays due. Never-reviewed entries fall back to
    `fallback` when the lane has a better date than git (the blog lane passes
    the post's frontmatter publish date; the docs lane has no such field and
    passes nothing), then to the git creation date. None only when the entry
    has no usable date at all.
    """
    cands: list[date] = []
    if entry:
        reviewed = parse_day(entry.get("reviewed_at"))
        if reviewed and entry.get("status") != INCOMPLETE_STATUS:
            cands.append(reviewed)
    human = ts_to_day(newest_non_bot.get(path))
    if human:
        cands.append(human)
    if cands:
        return max(cands)
    return fallback or ts_to_day(created.get(path))


# ---- Input loading ----------------------------------------------------------


def normalize_url_path(url_path: str) -> str:
    """Strip fragment, query, and origin from a reported URL; return "/a/b".

    The half of URL-to-content-path resolution the two lanes share. Which
    filenames a normalized path maps onto is lane-specific (docs tries both a
    leaf `.md` and an `_index.md`; blogs are always bundles), so each selector
    keeps its own `content_path_for_url` on top of this.
    """
    p = url_path.split("#", 1)[0].split("?", 1)[0].strip()
    if p.startswith("https://"):
        p = re.sub(r"^https://[^/]+", "", p)
    return "/" + p.strip("/")


def load_traffic(
    traffic_file: Path | None,
    known_paths: set[str],
    resolve: Callable[[str, set[str]], str | None],
) -> tuple[dict[str, int], dict]:
    """Parse the S3 traffic snapshot (JSON or CSV) into {content_path: visits}.

    `resolve` is the lane's URL-to-content-path mapper, which is the only part
    of this that differs between corpora.

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
        cp = resolve(str(url_path), known_paths)
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


def load_ledger(ledger_dir: Path, lane: Lane) -> dict[str, dict]:
    """Return {content_path: ledger entry} from one-file-per-entry JSON."""
    entries: dict[str, dict] = {}
    if not ledger_dir.is_dir():
        # Not fatal — the workflow only passes --ledger-dir when the S3 sync
        # produced one — but never silent: with no ledger every entry scores as
        # never-reviewed, which is a very different queue. DEFAULT_LEDGER_DIR is
        # the in-repo path these scripts have never actually had, so a run that
        # falls back to it is one that meant to read the S3 cache and didn't.
        print(
            f"{lane.prog}: no ledger directory at {ledger_dir}; scoring every "
            f"{lane.corpus_noun} as never-reviewed",
            file=sys.stderr,
        )
        return entries
    for f in sorted(ledger_dir.glob("*.json")):
        try:
            entry = json.loads(f.read_text())
        except (OSError, json.JSONDecodeError):
            print(f"{lane.prog}: unreadable ledger file {f}", file=sys.stderr)
            continue
        path = entry.get("path")
        if path:
            entry["_file"] = str(f)
            entries[path] = entry
    return entries


# ---- Subcommands -------------------------------------------------------------


def cmd_prune(ledger_dir: Path, repo: Path, dry_run: bool, lane: Lane) -> int:
    """GC ledger entries whose content file no longer exists."""
    pruned = []
    for path, entry in load_ledger(ledger_dir, lane).items():
        if not (repo / path).is_file():
            pruned.append(entry["_file"])
            if not dry_run:
                Path(entry["_file"]).unlink()
    verb = "would prune" if dry_run else "pruned"
    print(f"{lane.prog}: {verb} {len(pruned)} orphaned ledger file(s)")
    for f in pruned:
        print(f"  {f}")
    return 0


# ---- Output ------------------------------------------------------------------


def write_github_output(queue: dict, lane: Lane) -> None:
    gh_out = os.environ.get("GITHUB_OUTPUT")
    if not gh_out:
        return
    items = queue[lane.items_key]
    with open(gh_out, "a") as fh:
        fh.write(f"{lane.has_output}={'true' if items else 'false'}\n")
        fh.write(f"halted={queue.get('halted') or ''}\n")


def finish(queue: dict, args, lane: Lane) -> int:
    """Stamp the count, emit the queue (stdout or --out), and set job outputs."""
    queue["count"] = len(queue[lane.items_key])
    body = json.dumps(queue, indent=2)
    if args.dry_run or not args.out:
        print(body)
    else:
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(body + "\n")
        print(
            f"{lane.prog}: {queue['count']} {lane.item_noun}(s)"
            + (f" (halted: {queue['halted']})" if queue["halted"] else "")
            + f" → {out}",
            file=sys.stderr,
        )
    write_github_output(queue, lane)
    return 0
