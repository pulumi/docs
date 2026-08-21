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


def _load_selector():
    """select-articles.py imported by path — hyphenated filename, and its
    main() is guarded so importing has no side effects (the same pattern
    record-review.py and check-retire-veto.py use). Most of this suite shells
    out to the CLI; the tier-policy checks below are pure functions, where
    calling them directly says more than parsing a queue would.
    """
    import importlib.util

    spec = importlib.util.spec_from_file_location("select_articles", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


selector = _load_selector()


def load_repo_tiers():
    """The shipped strategic-tiers.yaml as rules, or None if it won't parse."""
    if not REPO_TIERS.is_file():
        return None
    try:
        return selector.load_tiers(REPO_TIERS)
    except Exception:  # noqa: BLE001 - the caller reports it as a failed check
        return None


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
STUB = "---\nredirect_to: /docs/misc/one/\n---\n"

TIERS = """\
tiers:
  - prefix: content/docs/generated/
    tier: 0
  - prefix: content/docs/clidocs/
    tier: 3
    editable: false
    reviewable: true
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
    "content/docs/generated/cli.md",     # tier 0 (excluded from both lanes)
    "content/docs/clidocs/pulumi_up.md",    # generated but reviewable (report lane)
    "content/docs/clidocs/pulumi_down.md",  # generated but reviewable (report lane)
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
    (repo / "content/docs/misc/stub.md").write_text(STUB)
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
        check("content/docs/misc/stub.md" not in [a["path"] for a in
              run_select(repo, tiers, empty, "--count", "20")["articles"]],
              "redirect_to stub excluded")
        check(all(a["lane"] == "priority" for a in q["articles"]), "all picks priority lane")
        check(paths[0] == C, f"most-stale tier-1 tops the queue (got {paths[0]})")
        check(paths[1] == OVERVIEW, f"stale tier-2 outranks stale tier-3 (got {paths[1]})")
        check(STACKS not in paths, "freshly human-edited tier-1 is NOT in the top picks")
        q2 = run_select(repo, tiers, empty, "--count", "3")
        check([a["path"] for a in q2["articles"]] == paths, "selection is deterministic")

        print("report mode: the other half of the corpus, and only that half")
        # #20996: `editable: false, reviewable: true` pages are invisible to the
        # fix lane and are the ONLY pages the report lane sees. Neither lane
        # touches a tier-0 tree.
        fix_all = [a["path"] for a in
                   run_select(repo, tiers, empty, "--count", "50")["articles"]]
        rq = run_select(repo, tiers, empty, "--mode", "report", "--count", "50")
        rep_all = [a["path"] for a in rq["articles"]]
        check(sorted(rep_all) == ["content/docs/clidocs/pulumi_down.md",
                                  "content/docs/clidocs/pulumi_up.md"],
              f"report lane sees exactly the reviewable generated pages (got {rep_all})")
        check(not set(rep_all) & set(fix_all), "the two lanes never overlap")
        check(not any(p.startswith("content/docs/clidocs/") for p in fix_all),
              "fix lane never sees a non-editable page")
        check("content/docs/generated/cli.md" not in rep_all,
              "tier 0 stays out of the report lane too")
        check(rq.get("mode") == "report"
              and all(a["mode"] == "report" for a in rq["articles"]),
              "the queue and every entry carry the mode the worker runs in")
        check(all(a["editable"] is False for a in rq["articles"]),
              "report entries carry editable: false for the downstream gates")
        check(all(a["no_retire"] is True for a in rq["articles"]),
              "a page no PR may edit is stamped no_retire, matching check-retire-veto")
        check(all(a["editable"] is True for a in
                  run_select(repo, tiers, empty, "--count", "3")["articles"]),
              "fix entries carry editable: true")
        check(run_select(repo, tiers, empty, "--count", "3")["mode"] == "fix",
              "fix is the default mode")

        print("report mode: staleness laps the tree (a recorded page steps aside)")
        recorded = tmp / "ledger-reported"
        write_ledger(recorded, "content/docs/clidocs/pulumi_down.md", "2026-06-11",
                     status="reported")
        rq2 = run_select(repo, tiers, recorded, "--mode", "report", "--count", "1")
        check([a["path"] for a in rq2["articles"]] == ["content/docs/clidocs/pulumi_up.md"],
              "the just-reported page yields to its unreported sibling")

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

        print("reader signals: bare GSC export (no envelope) parses identically")
        bare = tmp / "signals-gsc-bare.json"
        bare.write_text(json.dumps({
            "source": "fct_google_search_console_metrics",
            "period": {"start": "2026-03-14", "end": "2026-06-11"},
            "generated": "2026-06-11T00:00:00Z",
            "pages": {
                "/docs/misc/one/": {"impressions": 50000, "clicks": 250},
                "/docs/misc/two/": {"impressions": 50000, "clicks": 5000},
                "/docs/misc/protected/keep/": {"impressions": 100, "clicks": 1},
            }}))
        qbare = run_select(repo, tiers, empty, "--count", "20", "--signals-file", str(bare))
        check(scores(qbare) == sg, "bare GSC export scores identically to the enveloped one")
        check(qbare["reader_signals"]["gsc"]["available"] is True,
              "bare GSC export marked available")
        check(qbare["reader_signals"]["feedback"]["available"] is False,
              "bare GSC export leaves feedback unavailable")

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
        check(qcap.get("capped") == [TWO], "capped pages surfaced on the queue")
        check(full.get("capped") == [], "no capped pages -> empty list, not a missing key")

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

        print("repo strategic-tiers.yaml routes each generated tree to its lane")
        # Both trees are generated, so NEITHER is editable. They differ on
        # whether the pipeline may read them (#20996): the CLI reference is
        # hand-written prose a generator assembles (report-only lane), the SDK
        # API reference is rendered from the machine-readable API definition
        # that IS the source of truth (excluded outright).
        rules = load_repo_tiers()
        if rules is None:
            check(False, "real tiers file parses")
        else:
            cli = selector.policy_for("content/docs/iac/cli/commands/pulumi.md", rules)
            check(not cli.editable, "real tiers file marks CLI commands non-editable")
            check(cli.reviewable, "real tiers file marks CLI commands reviewable")
            check(selector.eligible(cli, "report") and not selector.eligible(cli, "fix"),
                  "CLI commands are a report-lane candidate and never a fix-lane one")

            pkg = selector.policy_for(
                "content/docs/reference/pkg/python/pulumi/_index.md", rules)
            check(pkg.tier == 0 and not pkg.editable and not pkg.reviewable,
                  "real tiers file keeps the SDK API reference out of both lanes")
            check(not selector.eligible(pkg, "report")
                  and not selector.eligible(pkg, "fix"),
                  "SDK API reference is a candidate for neither lane")

    # --- stale-claim markers ride the queue, and escalation stops the boost ---
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        repo = make_repo(tmp)
        tiers = tmp / "tiers.yaml"
        tiers.write_text(REPO_TIERS.read_text() if REPO_TIERS.is_file() else "rules: []\n")

        marker = {"entity_key": "version/pulumi-package", "verdict": "contradicted",
                  "evidence": "CHANGELOG says 3.163.0", "source": "gh release view",
                  # Before TODAY's review: the review saw this marker and left it
                  # unresolved, so it is real drift and must keep boosting. (A
                  # marker dated AFTER the last completed review is the #20970
                  # echo instead — see boost_suppressed_by_recent_fix.)
                  "checked_at": "2026-06-10"}

        led = tmp / "ledger-markers"
        # STACKS is freshly reviewed, so absent a marker it never reaches the queue.
        write_ledger(led, STACKS, TODAY, stale_claims=[marker])
        q = run_select(repo, tiers, led)
        entry = next((a for a in q["articles"] if a["path"] == STACKS), None)
        check(entry is not None, "marked page is boosted into the queue")
        if entry:
            check(entry["stale_claims"] == 1, "count field preserved")
            check([m["entity_key"] for m in entry.get("stale_claim_markers") or []]
                  == ["version/pulumi-package"], "queue item carries the marker itself")
            check((entry["stale_claim_markers"][0].get("evidence") or "")
                  == "CHANGELOG says 3.163.0", "marker evidence reaches the worker")

        # An escalated marker must still ride in the queue item and still be
        # counted: record-review.py rebuilds the ledger entry from the queue,
        # so a marker withheld here is a marker deleted from the ledger the
        # next time this page is reviewed for any reason.
        led_mixed = tmp / "ledger-mixed"
        write_ledger(led_mixed, STACKS, TODAY, stale_claims=[
            marker,
            {**marker, "entity_key": "version/old-miss",
             "unresolved_reviews": 2, "escalated": True},
        ])
        q_mixed = run_select(repo, tiers, led_mixed)
        mixed = next((a for a in q_mixed["articles"] if a["path"] == STACKS), None)
        check(mixed is not None, "page with one active marker is still boosted")
        if mixed:
            keys = [m["entity_key"] for m in mixed.get("stale_claim_markers") or []]
            check("version/old-miss" in keys,
                  "escalated marker still travels in the queue item (survives the round-trip)")
            check(mixed["stale_claims"] == len(mixed["stale_claim_markers"]),
                  "stale_claims count matches the marker list it describes")

        led_esc = tmp / "ledger-escalated"
        write_ledger(led_esc, STACKS, TODAY,
                     stale_claims=[{**marker, "unresolved_reviews": 2, "escalated": True}])
        q_esc = run_select(repo, tiers, led_esc)
        esc = next((a for a in q_esc["articles"] if a["path"] == STACKS), None)
        check(esc is None, "an escalated marker alone no longer boosts the page")

        # ...and when such a page is reviewed anyway (staleness, --paths), the
        # escalated marker must reach record-review.py rather than evaporating.
        q_paths = run_select(repo, tiers, led_esc, "--paths", STACKS)
        forced = q_paths["articles"][0]
        check([m["entity_key"] for m in forced.get("stale_claim_markers") or []]
              == ["version/pulumi-package"],
              "escalated marker reaches a --paths review instead of being dropped")

        print("stale-claim boost cooldown (#20970's missing half)")
        import importlib.util
        from datetime import date as _date
        _spec = importlib.util.spec_from_file_location("select_articles", SCRIPT)
        sa = importlib.util.module_from_spec(_spec)
        _spec.loader.exec_module(sa)
        _t = _date(2026, 8, 19)
        def _e(reviewed, checked, status="reviewed"):
            e = {"status": status, "reviewed_at": reviewed}
            if checked is not None:
                e["stale_claims"] = [{"entity_key": "version/x", "checked_at": checked}]
            return e
        check(sa.boost_suppressed_by_recent_fix(_e("2026-08-18", "2026-08-19"), _t) is True,
              "marker written AFTER a just-completed review is an echo: suppressed")
        check(sa.boost_suppressed_by_recent_fix(_e("2026-08-18", "2026-08-17"), _t) is False,
              "marker the review SAW and left unresolved is real drift: still boosts")
        check(sa.boost_suppressed_by_recent_fix(_e("2026-08-01", "2026-08-02"), _t) is False,
              "past the cooldown, an echo has had time to be real: still boosts")
        check(sa.boost_suppressed_by_recent_fix(
                  _e("2026-08-18", "2026-08-19", status="incomplete"), _t) is False,
              "an incomplete review fixed nothing, so it never suppresses")
        check(sa.boost_suppressed_by_recent_fix(_e("2026-08-18", None), _t) is False,
              "no markers, nothing to suppress")
        check(sa.boost_suppressed_by_recent_fix(_e("2026-08-18", "garbage"), _t) is False,
              "an undated marker is not provably an echo, so it keeps its boost")
        check(sa.boost_suppressed_by_recent_fix(_e("garbage", "2026-08-19"), _t) is False,
              "an unparseable review date fails open (boosts), never suppresses silently")
        _edge = str(_date.fromordinal(_t.toordinal() - sa.STALE_BOOST_COOLDOWN_DAYS))
        check(sa.boost_suppressed_by_recent_fix(_e(_edge, "2026-08-19"), _t) is False,
              "exactly COOLDOWN days old is outside the window")
        check(sa.boost_suppressed_by_recent_fix(
                  {"status": "reviewed", "reviewed_at": "2026-08-18",
                   "stale_claims": [{"entity_key": "a", "checked_at": "2026-08-19"},
                                    {"entity_key": "b", "checked_at": "2026-08-17"}]}, _t) is False,
              "one pre-review marker is enough to keep the boost")

    print(f"\n{_passes} passed, {len(_failures)} failed")
    return 1 if _failures else 0


if __name__ == "__main__":
    sys.exit(main())
