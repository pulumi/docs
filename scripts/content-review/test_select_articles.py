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

import ast
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPT = HERE / "select-articles.py"
COMMON = HERE / "_selector_common.py"
BLOG_SCRIPT = HERE.parent / "blog-review" / "select-posts.py"
REPO_TIERS = (
    HERE.parents[1]
    / ".claude/commands/review-existing-content/references/strategic-tiers.yaml"
)

TODAY = "2026-06-12"

_failures: list[str] = []
_passes = 0


def _module_assign(path: Path, name: str):
    """Return a module-level literal assignment's value, or None if absent.

    Parsed from source rather than imported: these filenames are hyphenated
    (not importable) and run argparse at module scope. Reading the value rather
    than restating it is the point — the test then covers whatever the constant
    actually holds.
    """
    for node in ast.parse(path.read_text()).body:
        if isinstance(node, ast.Assign) and any(
            isinstance(t, ast.Name) and t.id == name for t in node.targets
        ):
            try:
                return ast.literal_eval(node.value)
            except ValueError:
                # A non-literal re-declaration (`BOT_AUTHORS = COMMON | {...}`)
                # is still a re-declaration. Report it as one rather than
                # letting literal_eval raise out of the test harness.
                return f"<non-literal assignment in {path.name}>"
    return None


def _bot_authors() -> set[str]:
    """Read BOT_AUTHORS out of the shared selector module.

    It lives in _selector_common.py, not in either selector, because the two
    copies drifted once and cost ~65% of content/docs their staleness clock.
    _check_bot_authors_single_definition below is the guard that keeps it there.
    """
    value = _module_assign(COMMON, "BOT_AUTHORS")
    if value is None:
        raise AssertionError(f"BOT_AUTHORS not found in {COMMON.name}")
    return set(value)


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

        # Every name in BOT_AUTHORS must suppress the staleness clock, not just
        # the one the fixture above happens to use. This is the regression guard
        # for the real defect: "Pulumi Bot" and "workprentice[bot]" were missing
        # from the set, so their commits looked like human edits and reset the
        # clock on ~65% of content/docs pages. Driving the assertion off the
        # constant means the next identity added to the set is covered the day
        # it lands, and one omitted from it fails here.
        print("every BOT_AUTHORS identity suppresses the staleness clock")
        # The set has exactly one home. It used to have two, and the second one
        # missed the fix — which is the whole reason _selector_common.py exists.
        # A selector that re-declares it locally shadows the shared set for its
        # own lane only, silently recreating the divergence.
        for script in (SCRIPT, BLOG_SCRIPT):
            check(_module_assign(script, "BOT_AUTHORS") is None,
                  f"{script.name} re-declares BOT_AUTHORS instead of importing it "
                  f"from _selector_common.py; the two copies will drift again")
        bot_names = sorted(_bot_authors())
        # Identities observed authoring commits in pulumi/docs. A name missing
        # here can't be caught by the loop below (the loop only iterates what is
        # already in the set), so the membership assertion is the actual guard —
        # "Pulumi Bot" and "workprentice[bot]" are precisely what was missing.
        # Add to this list whenever a new automation starts committing.
        for required in ("pulumi-bot", "Pulumi Bot", "workprentice[bot]",
                         "dependabot[bot]", "github-actions[bot]"):
            check(required in bot_names,
                  f"{required!r} is missing from BOT_AUTHORS, so its commits "
                  f"reset the staleness clock as if a human made them")
        for i, bot in enumerate(bot_names):
            botdir = tmp / f"botclock{i}"
            botdir.mkdir()
            botrepo = make_repo(botdir)
            (botrepo / "content/docs/misc/two.md").write_text(PAGE + f"\n{bot} touch.\n")
            git(botrepo, "add", ".")
            git(botrepo, "commit", "-q", "-m", f"{bot} edit", date="2026-06-11T00:00:00Z",
                name=bot, email="bot@example.com")
            sb = scores(run_select(botrepo, tiers, empty, "--count", "20"))
            check(sb[TWO] == s[TWO],
                  f"a commit authored by {bot!r} did not reset the clock on {TWO}")

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

        print("reader signals: exact degradation — no file, and all-neutral signals, score identically")
        check(full["reader_signals"]["available"] is False, "no signals file -> unavailable")
        check(all(a["signals"] is None for a in full["articles"]),
              "no signals file -> per-article signals null")
        neutral = tmp / "signals-neutral.json"
        # Identical CTRs (gap 0 vs the median) and all-positive votes: every
        # multiplier is exactly 1.0, so scores must equal the signal-blind run's.
        neutral.write_text(json.dumps({"version": 1, "signals": {
            "gsc": {"source": "gsc", "pages": {
                "/docs/misc/one/": {"impressions": 5000, "clicks": 500},
                "/docs/misc/two/": {"impressions": 5000, "clicks": 500}}},
            "feedback": {"source": "segment", "pages": {
                "/docs/misc/one/": {"yes": 10, "no": 0}}},
        }}))
        qn = run_select(repo, tiers, empty, "--count", "20", "--signals-file", str(neutral))
        check(qn["reader_signals"]["available"] is True, "neutral signals file still marked available")
        check(scores(qn) == s, "all-neutral signals -> scores byte-identical to the signal-blind run")

        print("reader signals: GSC opportunity boost (high impressions AND low CTR only)")
        gscf = tmp / "signals-gsc.json"
        gscf.write_text(json.dumps({"version": 1, "signals": {"gsc": {
            "source": "gsc", "period": {"start": "2026-03-14", "end": "2026-06-11"},
            "pages": {
                "/docs/misc/one/": {"impressions": 50000, "clicks": 250},
                "/docs/misc/two/": {"impressions": 50000, "clicks": 5000},
                "/docs/misc/protected/keep/": {"impressions": 100, "clicks": 1},
            }}}}))
        qg = run_select(repo, tiers, empty, "--count", "20", "--signals-file", str(gscf))
        sg = scores(qg)
        arts = {a["path"]: a for a in qg["articles"]}
        check(sg[ONE] > sg[TWO], "low-CTR page outranks its equally stale high-CTR sibling")
        one_gsc = arts[ONE]["signals"]["gsc"]
        check(1.0 < one_gsc["multiplier"] <= 1.25, f"gsc multiplier bounded (got {one_gsc['multiplier']})")
        check(one_gsc["low_ctr_flag"] is True, "low-CTR flag set on the flagged page")
        check(arts[TWO]["signals"]["gsc"]["multiplier"] == 1.0, "at/above-median CTR stays neutral")
        check(arts[TWO]["signals"]["gsc"]["low_ctr_flag"] is False, "healthy CTR not flagged")
        keep_gsc = arts[KEEP]["signals"]["gsc"]
        check(keep_gsc["multiplier"] == 1.0 and keep_gsc["low_ctr_flag"] is False,
              "under-threshold impressions stay neutral and unflagged")
        check(sg[TWO] == s[TWO], "boost-only: unboosted pages score exactly as before")
        check(qg["reader_signals"]["gsc"]["available"] is True, "gsc meta available")
        check(qg["reader_signals"]["feedback"]["available"] is False,
              "gsc-only file leaves feedback unavailable")
        check(qg["reader_signals"]["gsc"]["pages_matched"] == 3, "gsc pages matched")
        check(qg["reader_signals"]["gsc"]["median_ctr"] is not None, "corpus median recorded")

        print("reader signals: feedback boost (negative votes, damped below saturation)")
        fbf = tmp / "signals-fb.json"
        fbf.write_text(json.dumps({"version": 1, "signals": {"feedback": {
            "source": "segment", "pages": {
                "/docs/misc/one/": {"yes": 1, "no": 9},
                "/docs/misc/two/": {"yes": 9, "no": 1},
                "/docs/misc/protected/keep/": {"yes": 1, "no": 1},
            }}}}))
        qf = run_select(repo, tiers, empty, "--count", "20", "--signals-file", str(fbf))
        sf = scores(qf)
        artsf = {a["path"]: a for a in qf["articles"]}
        check(sf[ONE] > sf[TWO], "negatively-voted page outranks its positively-voted sibling")
        one_fb = artsf[ONE]["signals"]["feedback"]
        check(1.0 < one_fb["multiplier"] <= 1.30, f"feedback multiplier bounded (got {one_fb['multiplier']})")
        check(one_fb["neg_rate"] == 0.9, "neg_rate recorded")
        check(artsf[KEEP]["signals"]["feedback"]["multiplier"] == 1.0,
              "below-minimum vote count stays neutral")

        print("reader signals: malformed file degrades to exactly the signal-blind run")
        garbage = tmp / "signals-garbage.json"
        garbage.write_text("not json {{{")
        qb = run_select(repo, tiers, empty, "--count", "20", "--signals-file", str(garbage))
        check(qb["reader_signals"]["available"] is False, "garbage file -> unavailable")
        check(scores(qb) == s, "garbage file -> scores identical to no file")

        print("reader signals: determinism with signals present")
        qg2 = run_select(repo, tiers, empty, "--count", "20", "--signals-file", str(gscf))
        check(scores(qg2) == sg, "signal-boosted selection is deterministic")

        print("reader signals: --paths entries carry the signals block")
        qp = run_select(repo, tiers, empty, "--paths", ONE, "--signals-file", str(gscf))
        check(qp["articles"][0]["signals"]["gsc"]["low_ctr_flag"] is True,
              "manual dispatch still carries the flag")

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
        # CLI command reference and SDK API reference are both generated -> tier 0.
        for gen_path, label in [
            ("content/docs/iac/cli/commands/pulumi.md", "CLI commands"),
            ("content/docs/reference/pkg/python/pulumi/_index.md", "SDK API reference"),
        ]:
            proc = subprocess.run(
                [sys.executable, str(SCRIPT), "--no-gh", "--today", TODAY,
                 "--tiers", str(REPO_TIERS), "--ledger-dir", str(tmp / "empty"),
                 "--paths", gen_path, "--dry-run"],
                capture_output=True, text=True,
            )
            if proc.returncode == 0:
                entry = json.loads(proc.stdout)["articles"][0]
                check(entry["tier"] == 0, f"real tiers file marks {label} tier 0")
            else:
                check("tiers" not in proc.stderr.lower(), "real tiers file parses")

    print(f"\n{_passes} passed, {len(_failures)} failed")
    return 1 if _failures else 0


if __name__ == "__main__":
    sys.exit(main())
