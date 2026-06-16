#!/usr/bin/env python3
"""Tests for select-articles.py.

Self-contained — run with `python3 test_select_articles.py` (no pytest dep).
Builds a throwaway git repo with a miniature content/docs tree, fixture
tiers/ledger/traffic files, and shells out to the script with `--no-gh`
(no GitHub API) and `--today` (frozen clock), asserting on the queue JSON.
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

FILES = [
    "content/docs/concepts/_index.md",
    "content/docs/concepts/stacks.md",
    "content/docs/esc/overview.md",
    "content/docs/misc/one.md",
    "content/docs/misc/two.md",
    "content/docs/misc/protected/keep.md",
    "content/docs/generated/cli.md",
]


def make_repo(tmp: Path) -> Path:
    repo = tmp / "repo"
    for rel in FILES:
        f = repo / rel
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(PAGE)
    (repo / "content/docs/misc/draft.md").write_text(DRAFT)
    env = {**os.environ, "GIT_AUTHOR_DATE": "2026-01-01T00:00:00Z",
           "GIT_COMMITTER_DATE": "2026-01-01T00:00:00Z"}
    for cmd in (
        ["git", "init", "-q"],
        ["git", "config", "user.email", "t@example.com"],
        ["git", "config", "user.name", "Human Author"],
        ["git", "config", "commit.gpgsign", "false"],
        ["git", "add", "."],
        ["git", "commit", "-q", "-m", "seed"],
    ):
        subprocess.run(cmd, cwd=repo, check=True, env=env)
    return repo


def run_select(repo: Path, tiers: Path, ledger: Path, *extra: str) -> dict:
    out = repo / ".queue.json"
    env = {k: v for k, v in os.environ.items() if k != "GITHUB_OUTPUT"}
    proc = subprocess.run(
        [sys.executable, str(SCRIPT), "--no-gh", "--today", "2026-06-12",
         "--repo-root", str(repo), "--tiers", str(tiers),
         "--ledger-dir", str(ledger), "--out", str(out), *extra],
        capture_output=True, text=True, env=env,
    )
    check(proc.returncode == 0, f"exit 0 (stderr: {proc.stderr.strip()[:200]})")
    return json.loads(out.read_text()) if out.is_file() else {}


def write_ledger(ledger: Path, path: str, reviewed_at: str, **kw) -> None:
    ledger.mkdir(parents=True, exist_ok=True)
    slug = path.removeprefix("content/").removesuffix("/_index.md").removesuffix(".md").replace("/", "-")
    entry = {"path": path, "reviewed_at": reviewed_at, "pr": "", "lane": "priority",
             "clean": False, "fixes": 0, "skipped_findings": 0, **kw}
    (ledger / f"{slug}.json").write_text(json.dumps(entry, indent=2) + "\n")


def main() -> int:
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        repo = make_repo(tmp)
        tiers = tmp / "tiers.yaml"
        tiers.write_text(TIERS)
        ledger = tmp / "ledger"
        traffic = tmp / "traffic.json"

        print("tier-0, drafts excluded; deterministic ordering")
        q = run_select(repo, tiers, ledger)
        paths = [a["path"] for a in q["articles"]]
        check(len(paths) == 3, f"3 picks (got {paths})")
        check("content/docs/generated/cli.md" not in paths, "tier-0 excluded")
        check("content/docs/misc/draft.md" not in paths, "draft excluded")
        check(q["articles"][-1]["lane"] == "stale", "last slot is the stale lane")
        check(all(a["lane"] == "priority" for a in q["articles"][:-1]), "other slots priority")
        q2 = run_select(repo, tiers, ledger)
        check([a["path"] for a in q2["articles"]] == paths, "selection is deterministic")

        print("no traffic file: tier dominates (renormalized weights)")
        # All never-reviewed (age_n=1.0). The stale lane claims the path-first
        # never-reviewed page (concepts/_index.md); the priority slots should
        # then rank tier 1 > 2 > 3.
        check(q["articles"][-1]["path"] == "content/docs/concepts/_index.md", "stale slot takes path-first never-reviewed")
        check(paths[0] == "content/docs/concepts/stacks.md", f"tier-1 tops priority lane (got {paths[0]})")
        check(paths[1] == "content/docs/esc/overview.md", "tier-2 second in priority lane")

        print("traffic ranking: high-traffic tier-3 outranks low-traffic tier-2")
        traffic.write_text(json.dumps({
            "period": "2026-05", "source": "test",
            "pages": {"/docs/misc/one/": 50000, "/docs/esc/overview/": 3},
        }))
        q = run_select(repo, tiers, ledger, "--traffic-file", str(traffic))
        prio = [a["path"] for a in q["articles"] if a["lane"] == "priority"]
        check(prio.index("content/docs/misc/one.md") < prio.index("content/docs/esc/overview.md")
              if "content/docs/esc/overview.md" in prio
              else "content/docs/misc/one.md" in prio,
              "traffic term lifts the busy tier-3 page")
        one = next(a for a in q["articles"] if a["path"] == "content/docs/misc/one.md")
        check(one["monthly_visits"] == 50000, "visits recorded on the queue entry")
        check(q["traffic"]["available"] is True, "traffic marked available")
        check(q["traffic"]["pages_matched"] == 2, "URL→path normalization matched both")

        print("median imputation: missing pages don't zero out")
        two = next((a for a in q["articles"] if a["path"] == "content/docs/misc/two.md"), None)
        if two is not None and two["lane"] == "priority":
            check(two["score"] > 0, "imputed page scores nonzero")

        print("CSV traffic parses")
        csvf = tmp / "traffic.csv"
        csvf.write_text("path,views\n/docs/misc/one/,1234\n")
        q = run_select(repo, tiers, ledger, "--traffic-file", str(csvf))
        check(q["traffic"]["pages_matched"] == 1, "CSV snapshot parsed")

        print("cooldown: recently reviewed pages are skipped")
        write_ledger(ledger, "content/docs/concepts/_index.md", "2026-05-01")
        q = run_select(repo, tiers, ledger)
        paths = [a["path"] for a in q["articles"]]
        check("content/docs/concepts/_index.md" not in paths, "365d cooldown respected")

        print("cooldown expiry: old review re-enters the pool")
        write_ledger(ledger, "content/docs/concepts/_index.md", "2024-01-01")
        q = run_select(repo, tiers, ledger)
        paths = [a["path"] for a in q["articles"]]
        check("content/docs/concepts/_index.md" in paths, "page back after cooldown")

        print("stale lane prefers never-reviewed over oldest-reviewed")
        stale = next(a for a in q["articles"] if a["lane"] == "stale")
        check(stale["last_reviewed"] is None, "stale pick is never-reviewed")

        print("--paths override bypasses scoring")
        q = run_select(repo, tiers, ledger, "--paths", "content/docs/misc/two.md")
        check([a["path"] for a in q["articles"]] == ["content/docs/misc/two.md"], "explicit path honored")
        check(q["articles"][0]["lane"] == "manual", "manual lane tagged")

        print("--lane overrides the lane for --paths entries")
        q = run_select(repo, tiers, ledger, "--paths", "content/docs/misc/two.md", "--lane", "stale")
        check([a["path"] for a in q["articles"]] == ["content/docs/misc/two.md"], "single explicit path")
        check(q["articles"][0]["lane"] == "stale", "lane override honored")

        print("count=1 yields just the stale pick")
        q = run_select(repo, tiers, ledger, "--count", "1")
        check(len(q["articles"]) == 1 and q["articles"][0]["lane"] == "stale",
              "reserved stale slot survives count=1")

        print("no_retire flags propagate")
        q = run_select(repo, tiers, ledger, "--paths",
                       "content/docs/misc/protected/keep.md,content/docs/concepts/stacks.md")
        flags = {a["path"]: a["no_retire"] for a in q["articles"]}
        check(flags["content/docs/misc/protected/keep.md"] is True, "explicit no_retire")
        check(flags["content/docs/concepts/stacks.md"] is True, "tier 1 implies no_retire")

        print("repo strategic-tiers.yaml parses and excludes generated trees")
        proc = subprocess.run(
            [sys.executable, str(SCRIPT), "--no-gh", "--today", "2026-06-12",
             "--tiers", str(REPO_TIERS), "--ledger-dir", str(tmp / "empty"),
             "--paths", "content/docs/iac/cli/commands/pulumi.md", "--dry-run"],
            capture_output=True, text=True,
        )
        if proc.returncode == 0:
            entry = json.loads(proc.stdout)["articles"][0]
            check(entry["tier"] == 0, "real tiers file marks CLI commands tier 0")
        else:
            # Page may not exist in a sparse checkout; the parse still ran.
            check("tiers" not in proc.stderr.lower(), "real tiers file parses")

    print(f"\n{_passes} passed, {len(_failures)} failed")
    return 1 if _failures else 0


if __name__ == "__main__":
    sys.exit(main())
