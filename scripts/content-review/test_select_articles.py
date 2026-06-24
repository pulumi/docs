#!/usr/bin/env python3
"""Tests for select-articles.py.

Self-contained — run with `python3 test_select_articles.py` (no pytest dep).
Builds a throwaway git repo with a miniature content/docs tree committed at
controlled dates by human and bot authors, plus fixture tiers/ledger/traffic
files, and shells out to the script with `--no-gh` (no GitHub API) and
`--today` (frozen clock), asserting on the queue JSON.

The selector scores every page by `importance * staleness` and takes the top N.
`staleness` is measured from `effective_last_review = max(completed bot review,
newest non-bot commit)`, falling back to the git creation date — so the fixture
commits are dated deliberately:

  created 2024-01-01 (human)  -> ~893 days stale at the 2026-06-12 clock
  edited  2026-06-10 (human)  -> ~2 days stale  (a human edit resets the clock)
  edited  2026-06-10 (bot)    -> still ~893     (a bot edit does NOT reset)
  created 2026-06-01 (human)  -> ~11 days stale (a brand-new page sorts to back)
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPT = HERE / "select-articles.py"
REPO_TIERS = (
    HERE.parents[1]
    / ".claude/commands/review-existing-content/references/strategic-tiers.yaml"
)

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


PAGE = "---\ntitle: T\n---\n\nBody.\n"
DRAFT = "---\ntitle: T\ndraft: true\n---\n\nBody.\n"

TIERS = """\
tiers:
  - prefix: content/docs/generated/
    tier: 0
  - prefix: content/docs/concepts/
    tier: 1
  - prefix: content/docs/esc/
    tier: 2
  - prefix: content/docs/misc/protected/
    tier: 3
    no_retire: true
"""

# Created long ago (2024-01-01) by a human, so all share the same high staleness
# and ordering among them is driven purely by tier (and traffic, when present).
BASE_FILES = [
    "content/docs/concepts/_index.md",   # tier 1
    "content/docs/concepts/stacks.md",   # tier 1 — later human-edited (reset)
    "content/docs/esc/overview.md",      # tier 2
    "content/docs/misc/one.md",          # tier 3 — later bot-edited (no reset)
    "content/docs/misc/two.md",          # tier 3
    "content/docs/misc/protected/keep.md",  # tier 3, no_retire
    "content/docs/generated/cli.md",     # tier 0 (excluded)
]


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
    repo.mkdir()
    git(repo, "init", "-q")
    git(repo, "config", "commit.gpgsign", "false")

    # C1 — the base corpus, created long ago by a human.
    for rel in BASE_FILES:
        f = repo / rel
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(PAGE)
    (repo / "content/docs/misc/draft.md").write_text(DRAFT)
    git(repo, "add", ".")
    git(repo, "commit", "-q", "-m", "seed", date="2024-01-01T00:00:00Z")

    # C2 — a brand-new page, recently created by a human.
    (repo / "content/docs/misc/newpage.md").write_text(PAGE)
    git(repo, "add", ".")
    git(repo, "commit", "-q", "-m", "new page", date="2026-06-01T00:00:00Z")

    # C3 — a human edit to concepts/stacks: resets its staleness clock.
    (repo / "content/docs/concepts/stacks.md").write_text(PAGE + "\nEdited.\n")
    git(repo, "add", ".")
    git(repo, "commit", "-q", "-m", "human edit", date="2026-06-10T00:00:00Z")

    # C4 — a bot edit to misc/one: must NOT reset its clock.
    (repo / "content/docs/misc/one.md").write_text(PAGE + "\nBot touch.\n")
    git(repo, "add", ".")
    git(repo, "commit", "-q", "-m", "bot edit", date="2026-06-10T00:00:00Z",
        name="pulumi-bot", email="bot@pulumi.com")
    return repo


def run_select(repo: Path, tiers: Path, ledger: Path, *extra: str) -> dict:
    out = repo / ".queue.json"
    env = {k: v for k, v in os.environ.items() if k != "GITHUB_OUTPUT"}
    proc = subprocess.run(
        [sys.executable, str(SCRIPT), "--no-gh", "--today", TODAY,
         "--repo-root", str(repo), "--tiers", str(tiers),
         "--ledger-dir", str(ledger), "--out", str(out), *extra],
        capture_output=True, text=True, env=env,
    )
    check(proc.returncode == 0, f"exit 0 (stderr: {proc.stderr.strip()[:200]})")
    return json.loads(out.read_text()) if out.is_file() else {}


def scores(q: dict) -> dict[str, float]:
    return {a["path"]: a["score"] for a in q["articles"]}


def write_ledger(ledger: Path, path: str, reviewed_at: str, **kw) -> None:
    ledger.mkdir(parents=True, exist_ok=True)
    slug = path.removeprefix("content/").removesuffix("/_index.md").removesuffix(".md").replace("/", "-")
    entry = {"path": path, "reviewed_at": reviewed_at, "pr": "", "lane": "priority",
             "status": "reviewed", "fixes": 0, "skipped_findings": 0, "attempts": 0, **kw}
    (ledger / f"{slug}.json").write_text(json.dumps(entry, indent=2) + "\n")


C = "content/docs/concepts/_index.md"
STACKS = "content/docs/concepts/stacks.md"
OVERVIEW = "content/docs/esc/overview.md"
ONE = "content/docs/misc/one.md"
TWO = "content/docs/misc/two.md"
KEEP = "content/docs/misc/protected/keep.md"
NEWPAGE = "content/docs/misc/newpage.md"


def main() -> int:
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        repo = make_repo(tmp)
        tiers = tmp / "tiers.yaml"
        tiers.write_text(TIERS)
        empty = tmp / "ledger-empty"
        traffic = tmp / "traffic.json"

        print("exclusions, lanes, and staleness ordering (no traffic, no ledger)")
        q = run_select(repo, tiers, empty, "--count", "3")
        paths = [a["path"] for a in q["articles"]]
        check(len(paths) == 3, f"3 picks (got {paths})")
        check("content/docs/generated/cli.md" not in paths, "tier-0 excluded")
        check("content/docs/misc/draft.md" not in paths, "draft excluded")
        check(all(a["lane"] == "priority" for a in q["articles"]), "all picks priority lane")
        check(paths[0] == C, f"most-stale tier-1 tops the queue (got {paths[0]})")
        check(paths[1] == OVERVIEW, f"stale tier-2 outranks stale tier-3 (got {paths[1]})")
        check(STACKS not in paths, "freshly human-edited tier-1 is NOT in the top picks")
        q2 = run_select(repo, tiers, empty, "--count", "3")
        check([a["path"] for a in q2["articles"]] == paths, "selection is deterministic")

        print("human edit resets the clock; a bot edit does not")
        full = run_select(repo, tiers, empty, "--count", "20")
        s = scores(full)
        check(s[STACKS] < s[C], "human-edited tier-1 scores far below the never-edited tier-1")
        check(s[STACKS] < s[KEEP], "freshly human-edited page falls below stale tier-3 pages")
        check(s[ONE] == s[TWO], "bot-edited page scores identically to its never-edited tier-3 sibling")
        check(s[ONE] > s[STACKS], "bot edit left the page stale (unlike the human-edited one)")

        print("multiplicative score: stale tier-2 beats a fresh tier-1")
        check(s[OVERVIEW] > s[STACKS], "importance*staleness lets a very stale tier-2 outrank a fresh tier-1")

        print("creation-date fallback: a brand-new page sorts behind an ancient one")
        check(s[TWO] > s[NEWPAGE], "older-created tier-3 outranks the just-created tier-3")
        check(s[NEWPAGE] > 0, "brand-new page still scores nonzero")

        print("traffic ranking: within a tier, the busier page outranks the quieter")
        traffic.write_text(json.dumps({
            "period": "2026-05", "source": "test",
            "pages": {"/docs/misc/one/": 50000, "/docs/misc/two/": 5},
        }))
        qt = run_select(repo, tiers, empty, "--count", "20", "--traffic-file", str(traffic))
        st = scores(qt)
        check(st[ONE] > st[TWO], "traffic lifts the busy tier-3 page above the quiet one")
        check(qt["traffic"]["available"] is True, "traffic marked available")
        check(qt["traffic"]["pages_matched"] == 2, "URL→path normalization matched both")
        one_art = next(a for a in qt["articles"] if a["path"] == ONE)
        check(one_art["monthly_visits"] == 50000, "visits recorded on the queue entry")

        print("CSV traffic parses")
        csvf = tmp / "traffic.csv"
        csvf.write_text("path,views\n/docs/misc/one/,1234\n")
        qc = run_select(repo, tiers, empty, "--count", "20", "--traffic-file", str(csvf))
        check(qc["traffic"]["pages_matched"] == 1, "CSV snapshot parsed")

        print("incomplete review keeps a page due (its reviewed_at is ignored)")
        led_inc = tmp / "ledger-incomplete"
        write_ledger(led_inc, OVERVIEW, "2026-06-11", status="incomplete", attempts=1)
        qi = run_select(repo, tiers, led_inc, "--count", "20")
        si = scores(qi)
        check(OVERVIEW in si, "incomplete page stays in the queue despite a fresh reviewed_at")
        check(si[OVERVIEW] == s[OVERVIEW], "incomplete reviewed_at does not advance the staleness clock")

        print("attempt cap backs a perpetually-failing page off")
        led_cap = tmp / "ledger-capped"
        write_ledger(led_cap, TWO, "2026-06-11", status="incomplete", attempts=3)
        qcap = run_select(repo, tiers, led_cap, "--count", "20")
        check(TWO not in scores(qcap), "page at the attempt cap is excluded entirely")
        check(ONE in scores(qcap), "non-capped pages still selected")

        print("completed review advances the clock (page is deprioritized)")
        led_done = tmp / "ledger-done"
        write_ledger(led_done, C, "2026-06-05", status="reviewed")
        qd = run_select(repo, tiers, led_done, "--count", "3")
        dpaths = [a["path"] for a in qd["articles"]]
        check(dpaths[0] == OVERVIEW, "after a fresh completed review the tier-1 page drops below the stale tier-2")
        check(C not in dpaths, "just-reviewed tier-1 leaves the top picks")

        print("--paths override bypasses scoring")
        q = run_select(repo, tiers, empty, "--paths", TWO)
        check([a["path"] for a in q["articles"]] == [TWO], "explicit path honored")
        check(q["articles"][0]["lane"] == "manual", "manual lane tagged")

        print("--lane overrides the lane for --paths entries")
        q = run_select(repo, tiers, empty, "--paths", TWO, "--lane", "stale")
        check(q["articles"][0]["lane"] == "stale", "lane override honored")

        print("no_retire flags propagate")
        q = run_select(repo, tiers, empty, "--paths", f"{KEEP},{STACKS}")
        flags = {a["path"]: a["no_retire"] for a in q["articles"]}
        check(flags[KEEP] is True, "explicit no_retire")
        check(flags[STACKS] is True, "tier 1 implies no_retire")

        print("attempts surfaced on queue entries")
        check(all("attempts" in a for a in full["articles"]), "every queue entry carries attempts")

        print("repo strategic-tiers.yaml parses and excludes generated trees")
        proc = subprocess.run(
            [sys.executable, str(SCRIPT), "--no-gh", "--today", TODAY,
             "--tiers", str(REPO_TIERS), "--ledger-dir", str(tmp / "empty"),
             "--paths", "content/docs/iac/cli/commands/pulumi.md", "--dry-run"],
            capture_output=True, text=True,
        )
        if proc.returncode == 0:
            entry = json.loads(proc.stdout)["articles"][0]
            check(entry["tier"] == 0, "real tiers file marks CLI commands tier 0")
        else:
            check("tiers" not in proc.stderr.lower(), "real tiers file parses")

    print(f"\n{_passes} passed, {len(_failures)} failed")
    return 1 if _failures else 0


if __name__ == "__main__":
    sys.exit(main())
