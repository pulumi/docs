#!/usr/bin/env python3
"""Tests for select-posts.py.

Self-contained — run with `python3 test_select_posts.py` (no pytest dep). The
cases are named `_case_*` rather than `test_*` on purpose: pytest still collects
this file by name, and a `test_*(tmp: Path)` signature makes it error out
looking for a `tmp` fixture that doesn't exist. Keep new cases `_case_*` and
call them from main().

Builds a throwaway git repo with a miniature content/blog tree committed at
controlled dates by human and bot authors, plus fixture ledger/traffic/signals
files, and shells out to the script with `--today` (frozen clock), asserting
on the queue JSON.

The selector scores every post by `importance * staleness` and takes the top
N. `staleness` is measured from `effective_last_review = max(completed bot
review, newest non-bot commit)`, falling back to the post's frontmatter
publish date — so with no traffic snapshot the queue is an
oldest-unreviewed-first sweep. Fixture posts are dated deliberately:

  published 2019-01-01  -> ~7.4 years stale at the 2026-06-12 clock
  published 2022-01-01  -> ~4.4 years stale
  published 2024-01-01  -> ~2.4 years stale
  published 2026-05-01  -> 42 days old: excluded by the 90-day minimum age
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPT = HERE / "select-posts.py"

TODAY = "2026-06-12"

_failures: list[str] = []
_passes = 0


def check(cond: bool, msg: str) -> None:
    global _passes
    if cond:
        _passes += 1
    else:
        _failures.append(msg)
        print(f"  FAIL: {msg}", file=sys.stderr)


def post_body(date: str, draft: bool = False) -> str:
    fm = f"---\ntitle: T\ndate: {date}\n"
    if draft:
        fm += "draft: true\n"
    fm += "---\n\nBody.\n"
    return fm


# slug -> publish date. All committed in one initial commit, so git history
# is identical across them and ordering is driven by the frontmatter dates.
BASE_POSTS = {
    "ancient-post": "2019-01-01",
    "old-post": "2022-01-01",
    "middling-post": "2024-01-01",
    "recent-post": "2026-05-01",  # < 90 days old at TODAY -> excluded
}


def git(repo: Path, *args: str, date: str | None = None,
        name: str = "Human Author", email: str = "human@example.com") -> None:
    env = {**os.environ, "GIT_AUTHOR_NAME": name, "GIT_AUTHOR_EMAIL": email,
           "GIT_COMMITTER_NAME": name, "GIT_COMMITTER_EMAIL": email}
    if date:
        env["GIT_AUTHOR_DATE"] = date
        env["GIT_COMMITTER_DATE"] = date
    subprocess.run(["git", "-C", str(repo), *args], check=True, env=env,
                   capture_output=True)


def make_repo(tmp: Path) -> Path:
    repo = tmp / "repo"
    repo.mkdir(parents=True)
    git(repo, "init", "-q")
    git(repo, "config", "commit.gpgsign", "false")

    for slug, date in BASE_POSTS.items():
        f = repo / "content/blog" / slug / "index.md"
        f.parent.mkdir(parents=True)
        f.write_text(post_body(date))
    # A draft post — never selectable.
    d = repo / "content/blog/draft-post/index.md"
    d.parent.mkdir(parents=True)
    d.write_text(post_body("2020-01-01", draft=True))
    # Seed commit is bot-authored so no post starts with a human edit: the
    # staleness clock falls back to each post's frontmatter publish date,
    # which is exactly the degraded age-based mode under test.
    git(repo, "add", "-A", date="2026-01-01T00:00:00Z")
    git(repo, "commit", "-q", "-m", "seed", date="2026-01-01T00:00:00Z",
        name="pulumi-bot", email="bot@pulumi.com")

    # A human edit to middling-post two days before TODAY: resets its clock,
    # so its staleness drops from ~2.4 years to ~2 days.
    f = repo / "content/blog/middling-post/index.md"
    f.write_text(post_body("2024-01-01") + "\nHuman touch.\n")
    git(repo, "add", "-A", date="2026-06-10T00:00:00Z")
    git(repo, "commit", "-q", "-m", "human edit", date="2026-06-10T00:00:00Z")

    # A bot edit to old-post at the same time: does NOT reset the clock.
    f = repo / "content/blog/old-post/index.md"
    f.write_text(post_body("2022-01-01") + "\nBot touch.\n")
    git(repo, "add", "-A", date="2026-06-10T00:00:00Z")
    git(repo, "commit", "-q", "-m", "bot edit", date="2026-06-10T00:00:00Z",
        name="pulumi-bot", email="bot@pulumi.com")

    return repo


def run_select(repo: Path, *extra: str, ledger: Path | None = None,
               gh_output: Path | None = None) -> dict:
    out = repo / ".queue.json"
    args = [sys.executable, str(SCRIPT), "--repo-root", str(repo),
            "--today", TODAY, "--out", str(out)]
    if ledger:
        args += ["--ledger-dir", str(ledger)]
    args += list(extra)
    env = dict(os.environ)
    env.pop("GITHUB_OUTPUT", None)
    if gh_output:
        env["GITHUB_OUTPUT"] = str(gh_output)
    proc = subprocess.run(args, capture_output=True, text=True, env=env)
    if proc.returncode != 0:
        raise AssertionError(f"select-posts failed:\n{proc.stderr}")
    return json.loads(out.read_text())


def paths(queue: dict) -> list[str]:
    return [p["path"] for p in queue["posts"]]


def write_ledger(tmp: Path, entries: list[dict]) -> Path:
    d = tmp / "ledger"
    d.mkdir(parents=True, exist_ok=True)
    for e in entries:
        (d / f"{e['slug']}.json").write_text(json.dumps(e))
    return d


def _case_age_based_sweep(tmp: Path) -> None:
    print("test: degraded (no traffic) selection is an oldest-first sweep")
    repo = make_repo(tmp / "t1")
    q = run_select(repo, "--count", "10")
    got = paths(q)
    check(got[0] == "content/blog/ancient-post/index.md",
          f"oldest post first, got {got}")
    check(got[1] == "content/blog/old-post/index.md",
          "bot edit does not reset the staleness clock")
    check("content/blog/recent-post/index.md" not in got,
          "posts younger than 90 days are excluded")
    check("content/blog/draft-post/index.md" not in got,
          "draft posts are excluded")
    check(got[-1] == "content/blog/middling-post/index.md",
          "a human edit resets the clock (sorts to the back)")
    check(q["halted"] is None, "halted is null")
    check(q["traffic"]["available"] is False, "traffic marked unavailable")
    check(all(p["score"] is not None for p in q["posts"]), "scored entries carry scores")
    check(q["posts"][0]["post_date"] == "2019-01-01", "post_date carried on the entry")


def _case_ledger_clock(tmp: Path) -> None:
    print("test: ledger review advances the clock; incomplete does not; cap excludes")
    repo = make_repo(tmp / "t2")
    ledger = write_ledger(tmp / "t2", [
        # Completed review of ancient-post yesterday -> drops to the back.
        {"slug": "ancient-post", "path": "content/blog/ancient-post/index.md",
         "status": "reviewed", "reviewed_at": "2026-06-11", "attempts": 0},
        # Incomplete review of old-post -> clock NOT advanced, stays in front.
        {"slug": "old-post", "path": "content/blog/old-post/index.md",
         "status": "incomplete", "reviewed_at": "2026-06-11", "attempts": 1},
    ])
    q = run_select(repo, "--count", "10", ledger=ledger)
    got = paths(q)
    check(got[0] == "content/blog/old-post/index.md",
          f"incomplete review leaves the post due, got {got}")
    check(got[-1] == "content/blog/ancient-post/index.md",
          "completed review resets the clock")
    check(q["posts"][0]["attempts"] == 1, "attempts carried onto the queue entry")

    ledger = write_ledger(tmp / "t2b", [
        {"slug": "old-post", "path": "content/blog/old-post/index.md",
         "status": "incomplete", "reviewed_at": "2026-06-11", "attempts": 3},
    ])
    q = run_select(repo, "--count", "10", ledger=ledger)
    check("content/blog/old-post/index.md" not in paths(q),
          "attempt-capped post is excluded")


def _case_traffic_and_gsc(tmp: Path) -> None:
    print("test: traffic weights equally stale posts; GSC boost is boost-only")
    repo = make_repo(tmp / "t3")
    # Give every post the same publish date so staleness ties and importance
    # decides. Rewrite dates, amend history in one commit.
    for slug in BASE_POSTS:
        (repo / "content/blog" / slug / "index.md").write_text(post_body("2020-01-01"))
    git(repo, "add", "-A", date="2026-01-02T00:00:00Z")
    git(repo, "commit", "-q", "-m", "level dates", date="2026-01-02T00:00:00Z",
        name="pulumi-bot", email="bot@pulumi.com")

    traffic = repo / ".traffic.json"
    traffic.write_text(json.dumps({"pages": {
        "/blog/old-post/": 50000,
        "/blog/middling-post/": 500,
        "/blog/recent-post/": 40,
        # ancient-post absent -> imputes the median (500), never zero
    }}))
    q = run_select(repo, "--count", "10", "--traffic-file", str(traffic))
    got = paths(q)
    check(q["traffic"]["available"] is True, "traffic marked available")
    check(got[0] == "content/blog/old-post/index.md",
          f"high-traffic post ranks first among equally stale posts, got {got}")
    entry = {p["slug"]: p for p in q["posts"]}
    check(entry["old-post"]["monthly_visits"] == 50000, "visits carried on the entry")
    check(entry["ancient-post"]["monthly_visits"] is None,
          "absent post carries null visits (median imputed in scoring only)")
    check(entry["ancient-post"]["score"] > entry["recent-post"]["score"],
          "median imputation outranks a known-tiny-traffic equally stale post")

    signals = repo / ".signals.json"
    signals.write_text(json.dumps({"version": 1, "signals": {"gsc": {"pages": {
        # High impressions, terrible CTR -> boosted.
        "/blog/middling-post/": {"impressions": 30000, "clicks": 30},
        # High impressions, great CTR -> neutral (never suppressed).
        "/blog/old-post/": {"impressions": 30000, "clicks": 6000},
        # Below the noise floor -> neutral.
        "/blog/ancient-post/": {"impressions": 50, "clicks": 0},
    }}}}))
    q2 = run_select(repo, "--count", "10", "--traffic-file", str(traffic),
                    "--signals-file", str(signals))
    e2 = {p["slug"]: p for p in q2["posts"]}
    check(q2["reader_signals"]["available"] is True, "signals marked available")
    check(e2["middling-post"]["signals"]["gsc"]["multiplier"] > 1.0,
          "high-impressions low-CTR post gets a boost")
    check(e2["middling-post"]["score"] > entry["middling-post"]["score"],
          "the boost raises the score vs the signal-blind run")
    check(e2["old-post"]["score"] == entry["old-post"]["score"],
          "good CTR is neutral, never a suppression")
    check(e2["ancient-post"]["score"] == entry["ancient-post"]["score"],
          "sub-noise-floor impressions are neutral")


def _case_paths_override_and_output(tmp: Path) -> None:
    print("test: --paths bypasses scoring/filters; GITHUB_OUTPUT contract")
    repo = make_repo(tmp / "t4")
    gh_out = tmp / "t4" / "gh_output"
    q = run_select(repo, "--paths", "content/blog/recent-post/index.md",
                   gh_output=gh_out)
    check(paths(q) == ["content/blog/recent-post/index.md"],
          "--paths selects the named post even under the age filter")
    check(q["posts"][0]["lane"] == "manual", "--paths entries default to manual lane")
    check(q["posts"][0]["score"] is None, "--paths entries carry no score")
    check(q["posts"][0]["slug"] == "recent-post", "slug is the bundle dir name")
    check(q["posts"][0]["url"] == "/blog/recent-post/", "url derived from the bundle")
    out = gh_out.read_text()
    check("has_posts=true" in out and "count=1" in out and "halted=\n" in out,
          f"GITHUB_OUTPUT contract, got: {out!r}")

    proc = subprocess.run(
        [sys.executable, str(SCRIPT), "--repo-root", str(repo), "--today", TODAY,
         "--out", str(repo / ".q.json"), "--paths", "content/blog/nope/index.md"],
        capture_output=True, text=True)
    check(proc.returncode == 1, "unknown --paths entry fails loudly")


def _case_determinism(tmp: Path) -> None:
    print("test: repeated runs produce identical ordering")
    repo = make_repo(tmp / "t5")
    a = paths(run_select(repo, "--count", "10"))
    b = paths(run_select(repo, "--count", "10"))
    check(a == b, "two identical runs, identical queues")
    q = run_select(repo, "--count", "2")
    check(len(q["posts"]) == 2 and q["count"] == 2, "--count truncates the queue")


def main() -> int:
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        _case_age_based_sweep(tmp)
        _case_ledger_clock(tmp)
        _case_traffic_and_gsc(tmp)
        _case_paths_override_and_output(tmp)
        _case_determinism(tmp)

    if _failures:
        print(f"\n{len(_failures)} failure(s), {_passes} passed", file=sys.stderr)
        return 1
    print(f"\nall select-posts tests passed ({_passes} checks)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
