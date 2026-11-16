#!/usr/bin/env python3
"""The stale-PR sweep — close any open PR that hasn't moved in
`stale_prs.close_days` days, with a heads-up comment first.

One clock, every open PR (drafts, bot PRs, and PRs the review never ran on
included), policy from the `stale_prs:` block of `.github/review-routing.yml`:

  idle >= close_days - notice_days    post a heads-up comment (once per window)
  idle >= close_days, heads-up at     close the PR, with a comment saying how
  least notice_days old               to reopen it and buy more time

A PR wearing `stale_prs.extended_label` gets `extended_close_days` instead.
The label is a bigger grace period, never an exemption: nothing here leaves
a PR open forever.

## What counts as movement

Read from the PR's issue timeline, latest of:

  - the PR being opened (the baseline, whoever opened it);
  - a commit landing (`committed`, committer date) or a force-push
    (`head_ref_force_pushed`), whoever pushed: any push is somebody working
    on it, and no automation here pushes to PRs nobody asked it to;
  - a comment, review, review-thread comment, reopen, ready-for-review,
    convert-to-draft, or retitle by a HUMAN.

Bots never move the clock: an actor in the routing config's `bots:` list,
any `type: Bot` account, any `[bot]` login. That covers the review pipeline,
the label reconciler, the SLA sweep, and this sweep's own comments. Labels
and review requests don't count either (adding the extended label buys a
longer window; it doesn't also restart it).

## State

None of its own. The heads-up comment carries a marker,
`<!-- STALE_PR_SWEEP:warn close_days=N -->`, and the timeline already
returns comment bodies, so "has this PR been warned since it last moved, for
the window it's in now" is answered from the PR itself. A heads-up only
counts when a bot posted it, after the last movement, for the same window
(adding or removing the label after a heads-up re-arms one for the new
window). No S3, no ledger: re-running the sweep is always safe.

## Safety

`--dry-run` comments and closes nothing; it prints the same run record, so
its output is the preview. `--max-closes` caps closes per run (warns are
uncapped: they're the harmless half, and a close needs one a week old
anyway). Any PR whose timeline can't be read or parsed is skipped, never
guessed at.

Self-contained: run the checks with `stale-pr-sweep.py --self-test`
(delegates to test_stale_pr_sweep.py, same convention as sla-sweep.py).
"""

from __future__ import annotations

import argparse
import json
import math
import os
import re
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
import routing  # noqa: E402

MARKER_RE = re.compile(r"<!-- STALE_PR_SWEEP:(warn|close) close_days=(\d+) -->")
DEFAULT_MAX_CLOSES = 25

# A heads-up posted by one scheduled run must be "old enough" at the same
# scheduled run a week later, even when that run starts a few minutes earlier
# in its slot than the first did. Without slack, cron jitter alone can push a
# close back a whole day.
NOTICE_SLACK = timedelta(hours=2)

# Human-actor timeline events that count as movement. Anything not listed
# (labeled, review_requested, mentioned, subscribed, referenced, ...) doesn't:
# `mentioned`/`subscribed` in particular name the person a BOT comment pinged
# as their actor, so counting them would let an escalation comment reset the
# clock for whoever it mentioned.
HUMAN_EVENTS = frozenset({
    "commented", "reopened", "ready_for_review", "convert_to_draft", "renamed",
})


def log(msg: str) -> None:
    print(f"stale-pr-sweep: {msg}", file=sys.stderr)


def warn(msg: str) -> None:
    print(f"::warning::stale-pr-sweep: {msg}", file=sys.stderr)


# ---- GitHub I/O ----------------------------------------------------------


class Gh:
    """Thin `gh` wrapper; every method is stubbed in tests."""

    def __init__(self, repo: str):
        self.repo = repo

    def _run(self, args: list[str]) -> str:
        result = subprocess.run(["gh", *args], text=True, capture_output=True, check=True)
        return result.stdout

    def list_open_prs(self) -> list[dict]:
        out = self._run([
            "pr", "list", "--repo", self.repo, "--state", "open", "--limit", "1000",
            "--json", "number,title,author,isDraft,createdAt,url,labels",
        ])
        return json.loads(out)

    def get_timeline(self, pr: int) -> list[dict]:
        out = self._run(["api", "--paginate", f"repos/{self.repo}/issues/{pr}/timeline"])
        return json.loads(out)

    def create_issue_comment(self, pr: int, body: str) -> None:
        self._run(["api", "--method", "POST", f"repos/{self.repo}/issues/{pr}/comments",
                   "-f", f"body={body}"])

    def close_pr(self, pr: int, body: str) -> None:
        self._run(["pr", "close", str(pr), "--repo", self.repo, "--comment", body])


# ---- policy ---------------------------------------------------------------


def policy(config: routing.Config) -> dict:
    stale = config.stale_prs
    if not stale:
        raise SystemExit("stale-pr-sweep: .github/review-routing.yml has no stale_prs: block")
    return stale


def window_for(labels: set[str], stale: dict) -> tuple[int, bool]:
    """(close_days, extended?) for a PR wearing `labels`."""
    if stale["extended_label"] in labels:
        return stale["extended_close_days"], True
    return stale["close_days"], False


# ---- timeline reads ---------------------------------------------------------


def _parse_ts(value: str | None) -> datetime:
    """Raises ValueError on anything unparsable; the caller skips the PR."""
    if not value:
        raise ValueError("empty timestamp")
    dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt


def is_bot(user: dict | None, bots: set[str]) -> bool:
    """Bot by config list, by account type, or by `[bot]` login. A missing
    user (deleted account, "ghost") counts as a bot: it can't be a person
    still working on the PR."""
    if not user:
        return True
    login = user.get("login") or ""
    return not login or login in bots or login.endswith("[bot]") or user.get("type") == "Bot"


def last_movement(timeline: list[dict], pr_created_at: str, bots: set[str]) -> tuple[datetime, str]:
    """(when, what) of the latest movement, per the module docstring."""
    best = (_parse_ts(pr_created_at), "opened")

    def consider(ts: str | None, what: str) -> None:
        nonlocal best
        if not ts:
            return
        dt = _parse_ts(ts)
        if dt > best[0]:
            best = (dt, what)

    for e in timeline:
        event = e.get("event")
        if event == "committed":
            consider((e.get("committer") or {}).get("date") or (e.get("author") or {}).get("date"),
                     "commit")
        elif event == "head_ref_force_pushed":
            consider(e.get("created_at"), "force-push")
        elif event == "reviewed":
            if not is_bot(e.get("user"), bots):
                consider(e.get("submitted_at"), f"review by {e['user'].get('login')}")
        elif event == "line-commented":
            for c in e.get("comments") or []:
                if not is_bot(c.get("user"), bots):
                    consider(c.get("created_at"), f"review comment by {c['user'].get('login')}")
        elif event in HUMAN_EVENTS:
            actor = e.get("actor") or e.get("user")
            if not is_bot(actor, bots):
                consider(e.get("created_at"), f"{event} by {actor.get('login')}")
    return best


def heads_ups(timeline: list[dict], bots: set[str]) -> list[tuple[datetime, int]]:
    """Every bot-posted heads-up on the timeline: (posted_at, close_days)."""
    found = []
    for e in timeline:
        if e.get("event") != "commented":
            continue
        if not is_bot(e.get("actor") or e.get("user"), bots):
            continue
        m = MARKER_RE.search(e.get("body") or "")
        if m and m.group(1) == "warn" and e.get("created_at"):
            found.append((_parse_ts(e["created_at"]), int(m.group(2))))
    return found


# ---- comment copy -------------------------------------------------------
#
# These bodies are posted with a token whose comments DO trigger workflows, so
# they must never contain a review command (`/update-review`, `/new-review`,
# `/social-review`) or `@claude`: the comment-triggered workflows match on a
# bare substring. test_comment_bodies_trigger_nothing pins that.


def _activity_line() -> str:
    return ("Activity means a commit, or a comment, review, or reopen from a person. "
            "Bot comments, including this one, don't count.")


def warn_body(close_days: int, extended: bool, idle_days: int, closes_in: int,
              stale: dict) -> str:
    label = stale["extended_label"]
    marker = f"<!-- STALE_PR_SWEEP:warn close_days={close_days} -->"
    days = "day" if closes_in == 1 else "days"
    if extended:
        lead = (f"Heads up: this PR hasn't moved in {idle_days} days. PRs labeled `{label}` close "
                f"automatically after {close_days} days without activity, so this one closes in "
                f"about {closes_in} {days}.")
        keep = "To keep it open, push a commit or leave a comment."
    else:
        lead = (f"Heads up: this PR hasn't moved in {idle_days} days. Open PRs close automatically "
                f"after {close_days} days without activity, so this one closes in about "
                f"{closes_in} {days}.")
        keep = (f"To keep it open, push a commit or leave a comment. If it's meant to sit for a "
                f"while, add the `{label}` label, which stretches the window to "
                f"{stale['extended_close_days']} days.")
    return f"{marker}\n{lead}\n\n{keep} {_activity_line()}"


def close_body(close_days: int, extended: bool, idle_days: int, stale: dict) -> str:
    label = stale["extended_label"]
    marker = f"<!-- STALE_PR_SWEEP:close close_days={close_days} -->"
    if extended:
        lead = (f"Closing this PR: no activity in {idle_days} days, past the {close_days}-day "
                f"limit for `{label}` PRs. Nothing is lost, and the branch stays put.")
        rest = "Reopen it whenever you're ready to pick it back up."
    else:
        lead = (f"Closing this PR: no activity in {idle_days} days. Nothing is lost, and the "
                f"branch stays put.")
        rest = (f"If you meant to leave it open, reopen it and add the `{label}` label, which "
                f"gives it {stale['extended_close_days']} days between updates instead of "
                f"{close_days}.")
    return (f"{marker}\n{lead}\n\n{rest} If you can't reopen or label it yourself, ask a "
            f"maintainer to.")


# ---- per-PR evaluation ----------------------------------------------------


def evaluate(pr: dict, timeline: list[dict], stale: dict, bots: set[str],
             now: datetime) -> dict:
    """Pure: what the sweep would do to this PR. Never mutates anything."""
    labels = {lbl.get("name") for lbl in pr.get("labels") or []}
    close_days, extended = window_for(labels, stale)
    notice_days = stale["notice_days"]
    moved_at, moved_by = last_movement(timeline, pr.get("createdAt") or "", bots)
    idle = (now - moved_at).total_seconds() / 86400.0

    # Only a heads-up for THIS window, posted after the last movement, counts.
    live = [at for at, days in heads_ups(timeline, bots) if days == close_days and at > moved_at]
    warned_at = max(live) if live else None

    base = {
        "pr": pr["number"], "title": pr.get("title") or "", "url": pr.get("url") or "",
        "draft": bool(pr.get("isDraft")), "extended": extended, "close_days": close_days,
        "idle_days": round(idle, 2), "last_movement": moved_at.isoformat(),
        "last_movement_was": moved_by,
    }

    if idle < close_days - notice_days:
        return {**base, "type": "none", "closes_in_days": math.ceil(close_days - idle)}

    if warned_at is None:
        # The close can't come sooner than notice_days after this heads-up,
        # however long the PR has already sat (first run, label removed, ...).
        closes_in = max(notice_days, math.ceil(close_days - idle))
        return {**base, "type": "warn", "closes_in_days": closes_in}

    warn_age = now - warned_at
    if idle >= close_days and warn_age + NOTICE_SLACK >= timedelta(days=notice_days):
        return {**base, "type": "close", "warned_at": warned_at.isoformat()}

    notice_left = notice_days - warn_age.total_seconds() / 86400.0
    return {**base, "type": "none", "warned_at": warned_at.isoformat(),
            "closes_in_days": max(0, math.ceil(max(close_days - idle, notice_left)))}


# ---- sweep ------------------------------------------------------------------


def sweep(gh: Gh, config: routing.Config, *, now: datetime, dry_run: bool,
          max_closes: int = DEFAULT_MAX_CLOSES) -> dict:
    stale = policy(config)
    bots = set(config.bots)
    results: list[dict] = []
    closes = 0

    for pr in gh.list_open_prs():
        number = pr["number"]
        try:
            timeline = gh.get_timeline(number)
            if not isinstance(timeline, list):
                raise ValueError("timeline response is not a list")
            verdict = evaluate(pr, timeline, stale, bots, now)
        except Exception as exc:  # noqa: BLE001 — one unreadable PR never stops the sweep
            log(f"PR #{number}: unreadable timeline ({exc}); skipping")
            results.append({"pr": number, "type": "skipped", "error": str(exc)[:300]})
            continue

        kind = verdict["type"]
        idle_whole = math.floor(verdict["idle_days"])
        try:
            if kind == "warn":
                body = warn_body(verdict["close_days"], verdict["extended"], idle_whole,
                                 verdict["closes_in_days"], stale)
                if not dry_run:
                    gh.create_issue_comment(number, body)
            elif kind == "close":
                if closes >= max_closes:
                    log(f"PR #{number}: due to close, but this run already closed {closes} "
                        f"(--max-closes); next run picks it up")
                    verdict = {**verdict, "type": "deferred"}
                else:
                    body = close_body(verdict["close_days"], verdict["extended"], idle_whole, stale)
                    if not dry_run:
                        gh.close_pr(number, body)
                    closes += 1
        except Exception as exc:  # noqa: BLE001
            log(f"PR #{number}: {kind} failed ({exc})")
            verdict = {**verdict, "error": str(exc)[:300]}

        log(f"PR #{number}: {verdict['type']} (idle {verdict.get('idle_days')}d of "
            f"{verdict.get('close_days')}, last: {verdict.get('last_movement_was')})")
        results.append(verdict)

    counts: dict[str, int] = {}
    for r in results:
        counts[r["type"]] = counts.get(r["type"], 0) + 1
    return {"schema": 1, "run_at": now.isoformat(), "dry_run": dry_run,
            "policy": dict(stale), "counts": counts, "prs": results}


# ---- reporting --------------------------------------------------------------


def step_summary(record: dict) -> str:
    """Markdown for $GITHUB_STEP_SUMMARY: what happened (or would have)."""
    p = record["policy"]
    verb = "Would" if record["dry_run"] else "Did"
    lines = [
        f"## Stale PR sweep{' (dry run)' if record['dry_run'] else ''}",
        "",
        f"Policy: close after {p['close_days']} days without movement "
        f"({p['extended_close_days']} with `{p['extended_label']}`), heads-up "
        f"{p['notice_days']} days before.",
        "",
    ]
    acted = [r for r in record["prs"] if r["type"] in ("warn", "close", "deferred", "skipped")]
    if not acted:
        lines.append("Nothing to do.")
    else:
        lines += ["| PR | Action | Idle (days) | Window | Last movement |", "|---|---|---|---|---|"]
        label = {"warn": f"{verb} warn", "close": f"{verb} close", "deferred": "Deferred (cap)",
                 "skipped": "Skipped (unreadable)"}
        for r in sorted(acted, key=lambda r: (r["type"], r["pr"])):
            title = (r.get("title") or "").replace("|", "\\|")[:60]
            lines.append(
                f"| [#{r['pr']}]({r.get('url', '')}) {title} | {label[r['type']]} | "
                f"{r.get('idle_days', '')} | {r.get('close_days', '')} | "
                f"{r.get('last_movement_was', r.get('error', ''))} |"
            )
    upcoming = sorted((r for r in record["prs"] if r["type"] == "none"),
                      key=lambda r: r.get("closes_in_days", 0))[:10]
    if upcoming:
        lines += ["", "Next up:", ""]
        lines += [f"- #{r['pr']} closes in ~{r['closes_in_days']}d" for r in upcoming]
    return "\n".join(lines) + "\n"


# ---- CLI ----------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--repo")
    parser.add_argument("--config", default=str(REPO_ROOT / ".github" / "review-routing.yml"))
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--max-closes", type=int, default=DEFAULT_MAX_CLOSES,
                        help=f"close at most this many PRs per run (default {DEFAULT_MAX_CLOSES})")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        import test_stale_pr_sweep  # noqa: PLC0415 — the pytest file doubles as the harness

        return test_stale_pr_sweep.run_standalone()

    if not args.repo:
        parser.error("--repo is required")

    try:
        config = routing.load_config(args.config)
    except routing.RoutingConfigError as exc:
        for msg in exc.errors:
            log(f"routing config error: {msg}")
        return 1

    record = sweep(Gh(args.repo), config, now=datetime.now(timezone.utc),
                   dry_run=args.dry_run, max_closes=args.max_closes)
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as fh:
            fh.write(step_summary(record))
    print(json.dumps(record, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
