#!/usr/bin/env python3
"""Deterministic fix-scope gate for publishing content-review fixes.

The worker's "high-confidence fixes only" restriction (SKILL.md step 3: five
enumerated categories, everything else flag-only) was honored purely by the
review model until this gate existed — the only hard check on the model's
edits was `make lint`, which validates well-formedness, not restraint (issue
#20078 §3.1). This script is the code-enforced backstop: every hunk in the
review's exported patch must fall within the line range of a finding
recorded by the deterministic pre-steps. An out-of-range edit means the
model strayed beyond the recorded findings; the publish job then fails
before anything is pushed, and the ledger records the page incomplete for a
human to look at.

The comparison is anchored on **pre-fix (old-side) line numbers**: the
pre-steps ran on a synthetic `/dev/null → <article>` diff of the master
checkout, so every artifact line reference indexes the file as it exists at
the base SHA — exactly the old side of the patch, which the workflow hands
in as a zero-context (`--unified=0`) diff so context lines never widen a
hunk's range. Matching old-side ranges needs no drift adjustment as earlier
hunks add or remove lines. Artifacts are read from the `review-snapshot`
run artifact — uploaded before the model step and immutable from then on —
so the model cannot widen its own allowance by editing the workspace.

Allowed ranges per category (the SKILL's five, same order):

  * claim        — `.verified-claims.json` verdicts `contradicted`/`mismatch`,
                   `line_range` ("L42" / "L42-58") ± 2 lines.
  * link         — dead internal links have no pre-step artifact; ranges come
                   from the verdict sentinel's `applied` entries (category
                   "link"), each validated against the pre-fix blob: every
                   declared line must contain a link construct, and the range
                   is capped at 3 lines.
  * frontmatter  — the frontmatter block (line 1 to its closing `---`), and
                   only when `.frontmatter-validation.json` actually reports a
                   violation (a missing menu parent or an alias collision).
  * vale         — `.vale-findings.json` entries with `deterministic_fix:
                   true`, `line` ± 2.
  * readthrough  — `.readthrough-findings.json` findings with `fix_class`
                   "local_repair", `line_range` ± 5, plus a move heuristic:
                   a pure insertion whose text mostly (≥80%) re-uses lines
                   deleted by an in-range hunk is a reorder, not new prose.

An artifact whose snapshot carries a non-empty `errors` list (the workflow's
`|| stub` fallback) contributes no ranges — fixes in that category then read
as out-of-range and the PR stays draft for a human (fail closed; nothing is
lost, a human can still promote).

The sentinel's `applied` array is the audit trail, not the authority: each
entry is cross-checked against the snapshot artifacts and invalid entries are
reported (`invalid_applied`) and ignored for coverage. Only the `link`
category, having no artifact, draws its allowance from `applied` — which is
why its entries get the extra plausibility validation above.

Skip rules (result "skipped", exit 0): an empty diff, or — when a `--branch`
with the `retire-` prefix is passed — a retirement branch (its diff
legitimately deletes the page and touches siblings' aliases/menus/links; the
retire veto in check-retire-veto.py is the guardrail for that shape). The
workflow routes retirement verdicts to the veto instead of this gate, so it
does not pass `--branch`; a retirement-shaped patch smuggled under a
non-retirement verdict therefore hits this gate and fails wholesale.

Usage:
    # Workflow invocation (patch handed over from the review job):
    verify-fix-scope.py --diff-file .review-changes.u0.diff --base-sha <sha> \
        --article content/docs/... --verdict .content-review-verdict.json \
        --artifacts-dir .review-snapshot [--out .fix-scope-report.json]
    # Branch mode (no --diff-file): derives the diff itself; --branch required.
    verify-fix-scope.py --branch content-review/<slug> --base-sha <sha> ...
    verify-fix-scope.py --self-test

Writes a report JSON: {result, reason, checked_hunks, uncovered_hunks,
invalid_applied, allowed_ranges}. Exit 0 = pass/skipped, 2 = fail,
1 = usage/input error.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

TOL_DEFAULT = 2
TOL_READTHROUGH = 5
LINK_RANGE_CAP = 3
MOVE_OVERLAP = 0.8

CATEGORIES = {"claim", "link", "frontmatter", "vale", "readthrough"}

LINE_RANGE_RE = re.compile(r"^L(\d+)(?:-L?(\d+))?$")
HUNK_RE = re.compile(r"^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@")
DIFF_FILE_RE = re.compile(r"^\+\+\+ (?:b/)?(.+)$")
# A line that plausibly carries the link being fixed: markdown link target,
# HTML href, or a Hugo ref/relref shortcode.
LINK_LINE_RE = re.compile(r"\]\(|href=|\{\{<\s*(?:rel)?ref\b")


def parse_line_range(s: str) -> tuple[int, int] | None:
    """'L42' -> (42, 42); 'L42-58' -> (42, 58); junk -> None."""
    m = LINE_RANGE_RE.match((s or "").strip())
    if not m:
        return None
    start = int(m.group(1))
    end = int(m.group(2)) if m.group(2) else start
    return (min(start, end), max(start, end))


def parse_hunks(diff_text: str) -> list[dict]:
    """Parse a --unified=0 diff into per-hunk records with old-side ranges.

    Old-side semantics: `@@ -a,b` with b>0 covers old lines [a, a+b-1]; a pure
    insertion (b==0) inserts AFTER old line a and is recorded as the point a
    with old_count 0.
    """
    hunks: list[dict] = []
    current_file = None
    hunk = None
    for line in diff_text.splitlines():
        if line.startswith("+++ "):
            m = DIFF_FILE_RE.match(line)
            current_file = None if m.group(1) == "/dev/null" else m.group(1)
            continue
        m = HUNK_RE.match(line)
        if m:
            old_start = int(m.group(1))
            old_count = int(m.group(2)) if m.group(2) is not None else 1
            hunk = {
                "file": current_file,
                "old_start": old_start,
                "old_count": old_count,
                "removed": [],
                "added": [],
            }
            hunks.append(hunk)
            continue
        if hunk is not None and line.startswith("-") and not line.startswith("---"):
            hunk["removed"].append(line[1:])
        elif hunk is not None and line.startswith("+") and not line.startswith("+++"):
            hunk["added"].append(line[1:])
    return hunks


def _loadable(artifacts_dir: Path, name: str):
    """Load one snapshot artifact; a stub with a non-empty `errors` list, a
    missing file, or unparseable JSON all yield None (fail closed)."""
    p = artifacts_dir / name
    if not p.is_file():
        return None
    try:
        data = json.loads(p.read_text())
    except (OSError, json.JSONDecodeError):
        return None
    if isinstance(data, dict) and data.get("errors"):
        return None
    return data


def frontmatter_end(blob_text: str) -> int | None:
    """1-based line number of the closing `---` of the frontmatter block."""
    lines = blob_text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    for i, line in enumerate(lines[1:], start=2):
        if line.strip() == "---":
            return i
    return None


def build_allowed_ranges(article: str, artifacts_dir: Path, blob_text: str,
                         applied: list[dict]) -> tuple[list[dict], list[dict]]:
    """(allowed ranges, invalid applied entries) for the article.

    Each range is {"start", "end", "category", "source"} in pre-fix line
    numbers. Artifact-backed categories draw ranges from the snapshot;
    `applied` entries are cross-checked against them and contribute coverage
    only for the artifact-less `link` category.
    """
    ranges: list[dict] = []
    invalid: list[dict] = []

    claims = _loadable(artifacts_dir, ".verified-claims.json")
    for v in (claims or {}).get("verdicts", []):
        if v.get("file") != article or v.get("verdict") not in ("contradicted", "mismatch"):
            continue
        r = parse_line_range(v.get("line_range", ""))
        if r:
            ranges.append({"start": max(1, r[0] - TOL_DEFAULT), "end": r[1] + TOL_DEFAULT,
                           "category": "claim",
                           "source": f"verified-claims:{v.get('claim_id', '?')}"})

    vale = _loadable(artifacts_dir, ".vale-findings.json")
    for f in vale if isinstance(vale, list) else []:
        if f.get("file") != article or not f.get("deterministic_fix"):
            continue
        line = f.get("line")
        if isinstance(line, int):
            ranges.append({"start": max(1, line - TOL_DEFAULT), "end": line + TOL_DEFAULT,
                           "category": "vale",
                           "source": f"vale:{f.get('rule', '?')}@L{line}"})

    rt = _loadable(artifacts_dir, ".readthrough-findings.json")
    for f in (rt or {}).get("findings", []):
        if f.get("file") != article or f.get("fix_class") != "local_repair":
            continue
        r = parse_line_range(f.get("line_range", ""))
        if r:
            ranges.append({"start": max(1, r[0] - TOL_READTHROUGH),
                           "end": r[1] + TOL_READTHROUGH,
                           "category": "readthrough",
                           "source": f"readthrough:{f.get('line_range')}"})

    fm = _loadable(artifacts_dir, ".frontmatter-validation.json")
    fm_violation = False
    for f in (fm or {}).get("files", []):
        if f.get("file") != article:
            continue
        if any(not p.get("parent_exists_in_menu", True) for p in f.get("menu_parents", [])):
            fm_violation = True
        if f.get("alias_collisions"):
            fm_violation = True
    if fm_violation:
        fm_end = frontmatter_end(blob_text)
        if fm_end:
            ranges.append({"start": 1, "end": fm_end, "category": "frontmatter",
                           "source": "frontmatter-validation"})

    blob_lines = blob_text.splitlines()
    for entry in applied:
        cat = entry.get("category")
        lines = entry.get("lines")
        ok_shape = (cat in CATEGORIES and isinstance(lines, list) and len(lines) == 2
                    and all(isinstance(n, int) and n > 0 for n in lines)
                    and entry.get("file") == article)
        if not ok_shape:
            invalid.append({**entry, "why": "malformed entry (category/file/lines)"})
            continue
        start, end = min(lines), max(lines)
        if cat == "link":
            if end - start + 1 > LINK_RANGE_CAP:
                invalid.append({**entry, "why": f"link range wider than {LINK_RANGE_CAP} lines"})
                continue
            declared = blob_lines[start - 1:end]
            if len(declared) < end - start + 1 or not all(LINK_LINE_RE.search(l) for l in declared):
                invalid.append({**entry, "why": "declared lines carry no link construct in the pre-fix file"})
                continue
            ranges.append({"start": max(1, start - TOL_DEFAULT), "end": end + TOL_DEFAULT,
                           "category": "link",
                           "source": entry.get("source") or f"applied:link@L{start}"})
        else:
            # Artifact-backed category: the entry must sit inside a range the
            # artifact already granted; it adds no coverage of its own.
            if not any(r["category"] == cat and r["start"] <= start and end <= r["end"]
                       for r in ranges):
                invalid.append({**entry, "why": "no matching finding in the snapshot artifacts"})

    return ranges, invalid


def hunk_covered(hunk: dict, ranges: list[dict]) -> bool:
    """True when EVERY old-side line of the hunk lies in an allowed range.

    Full coverage, not intersection: one oversized hunk (a whole-page rewrite
    or deletion) that merely overlaps a single finding must not ride that
    finding's allowance — each changed line has to be individually granted.
    """
    if hunk["old_count"] > 0:
        lo, hi = hunk["old_start"], hunk["old_start"] + hunk["old_count"] - 1
        return all(
            any(r["start"] <= n <= r["end"] for r in ranges)
            for n in range(lo, hi + 1)
        )
    # Pure insertion after old line N: covered when a range touches either
    # side of the insertion point.
    n = hunk["old_start"]
    return any(r["start"] <= n <= r["end"] or r["start"] <= n + 1 <= r["end"]
               for r in ranges)


def is_moved_text(hunk: dict, covered_hunks: list[dict]) -> bool:
    """Move heuristic: a pure insertion is a reorder (not new prose) when its
    stripped lines are mostly (≥ MOVE_OVERLAP) drawn from lines deleted by
    already-covered hunks in the same file."""
    if hunk["old_count"] != 0 or not hunk["added"]:
        return False
    deleted: dict[str, int] = {}
    for c in covered_hunks:
        if c["file"] != hunk["file"]:
            continue
        for l in c["removed"]:
            key = l.strip()
            if key:
                deleted[key] = deleted.get(key, 0) + 1
    inserted = [l.strip() for l in hunk["added"] if l.strip()]
    if not inserted:
        return False
    matched = 0
    for l in inserted:
        if deleted.get(l, 0) > 0:
            deleted[l] -= 1
            matched += 1
    return matched / len(inserted) >= MOVE_OVERLAP


def evaluate(diff_text: str, blob_text: str, verdict: dict | None,
             artifacts_dir: Path, article: str, branch: str) -> dict:
    """Pure gate evaluation; main() handles the git/file IO around it."""
    if branch.startswith("content-review/retire-"):
        return {"result": "skipped",
                "reason": "retirement branch — scope gate does not apply "
                          "(the retire veto is the guardrail for this shape)",
                "checked_hunks": 0, "uncovered_hunks": [], "invalid_applied": [],
                "allowed_ranges": []}

    hunks = parse_hunks(diff_text)
    if not hunks:
        return {"result": "skipped", "reason": "empty diff — nothing to check",
                "checked_hunks": 0, "uncovered_hunks": [], "invalid_applied": [],
                "allowed_ranges": []}

    applied = (verdict or {}).get("applied") or []
    applied = [e for e in applied if isinstance(e, dict)]
    ranges, invalid = build_allowed_ranges(article, artifacts_dir, blob_text, applied)

    covered, uncovered = [], []
    for h in hunks:
        if h["file"] != article:
            uncovered.append({**h, "why": "edit outside the reviewed article"})
        elif hunk_covered(h, ranges):
            covered.append(h)
        else:
            uncovered.append({**h, "why": "no recorded finding covers these lines"})

    # Second pass: pure insertions that are really moves of covered deletions.
    still_uncovered = []
    for h in uncovered:
        if h["file"] == article and is_moved_text(h, covered):
            covered.append(h)
        else:
            still_uncovered.append(h)

    def render(h):
        old_end = h["old_start"] + max(h["old_count"] - 1, 0)
        excerpt = (h["removed"] or h["added"] or [""])[0][:120]
        return {"file": h["file"], "old_start": h["old_start"], "old_end": old_end,
                "insertion": h["old_count"] == 0, "why": h["why"], "excerpt": excerpt}

    result = "fail" if still_uncovered else "pass"
    reason = ("" if result == "pass"
              else f"{len(still_uncovered)} hunk(s) fall outside every recorded finding")
    return {
        "result": result,
        "reason": reason,
        "checked_hunks": len(hunks),
        "uncovered_hunks": [render(h) for h in still_uncovered],
        "invalid_applied": invalid,
        "allowed_ranges": ranges,
    }


def _git(args: list[str]) -> str:
    out = subprocess.run(["git", *args], capture_output=True, text=True, check=True)
    return out.stdout


def run(args) -> int:
    if args.diff_file:
        diff_text = Path(args.diff_file).read_text()
    else:
        diff_text = _git(["diff", "--unified=0", args.base_sha, f"origin/{args.branch}"])
    branch = args.branch or ""
    if args.article_blob:
        blob_text = Path(args.article_blob).read_text()
    else:
        try:
            blob_text = _git(["show", f"{args.base_sha}:{args.article}"])
        except subprocess.CalledProcessError:
            blob_text = ""  # article absent at base (shouldn't happen for a fix PR)

    verdict = None
    vp = Path(args.verdict) if args.verdict else None
    if vp and vp.is_file():
        try:
            verdict = json.loads(vp.read_text())
        except (OSError, json.JSONDecodeError):
            verdict = None  # applied[] just stays empty; artifacts still gate

    report = evaluate(diff_text, blob_text, verdict,
                      Path(args.artifacts_dir), args.article, branch)
    Path(args.out).write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({k: report[k] for k in ("result", "reason", "checked_hunks")}))
    if report["invalid_applied"]:
        print(f"::warning::verify-fix-scope: {len(report['invalid_applied'])} "
              "applied[] entr(ies) did not match any recorded finding", file=sys.stderr)
    if report["result"] == "fail":
        for h in report["uncovered_hunks"]:
            print(f"::error::verify-fix-scope: uncovered hunk {h['file']}:"
                  f"L{h['old_start']}-L{h['old_end']} ({h['why']})", file=sys.stderr)
        return 2
    return 0


# ---- self-test ---------------------------------------------------------------


ARTICLE = "content/docs/example/page.md"


def _blob() -> str:
    """Fixture article, spaced so category tolerances don't overlap:
    frontmatter L1-6, claim L10, link L20, vale L30, readthrough L40,
    never-flagged prose L50."""
    lines = ["---", "title: Example", "menu:", "  iac:",
             "    parent: nowhere", "---", "", "# Example", ""]
    lines.append("Pulumi supports version 3.100 of the CLI.")            # L10
    lines += [f"Filler line {i}." for i in range(11, 20)]
    lines.append("See [the stacks doc](/docs/iac/stacks/) for more.")    # L20
    lines += [f"Filler line {i}." for i in range(21, 30)]
    lines.append("Click the Deployments tab in the console.")            # L30
    lines += [f"Filler line {i}." for i in range(31, 40)]
    lines.append("Step two comes before step one in this section.")      # L40
    lines += [f"Filler line {i}." for i in range(41, 50)]
    lines.append("A paragraph that is perfectly fine and was never flagged.")  # L50
    return "\n".join(lines) + "\n"


BLOB = _blob()

def _diff(hunks: list[str]) -> str:
    return (f"diff --git a/{ARTICLE} b/{ARTICLE}\n--- a/{ARTICLE}\n+++ b/{ARTICLE}\n"
            + "\n".join(hunks) + "\n")


def self_test() -> int:
    import tempfile

    failures = []

    def check(name, cond):
        print(("ok: " if cond else "FAIL: ") + name,
              file=sys.stdout if cond else sys.stderr)
        if not cond:
            failures.append(name)

    with tempfile.TemporaryDirectory() as d:
        snap = Path(d)
        (snap / ".verified-claims.json").write_text(json.dumps({
            "schema_version": 1, "verdicts": [
                {"claim_id": "c1", "file": ARTICLE, "line_range": "L10",
                 "verdict": "contradicted"},
                {"claim_id": "c2", "file": ARTICLE, "line_range": "L50",
                 "verdict": "verified"},
            ], "errors": []}))
        (snap / ".vale-findings.json").write_text(json.dumps([
            {"file": ARTICLE, "line": 30, "rule": "Pulumi.Substitutions",
             "deterministic_fix": True},
            {"file": ARTICLE, "line": 31, "rule": "Pulumi.Style",
             "deterministic_fix": False},
        ]))
        (snap / ".readthrough-findings.json").write_text(json.dumps({
            "schema_version": 1, "ran": True, "findings": [
                {"file": ARTICLE, "line_range": "L40", "fix_class": "local_repair",
                 "proposed_fix": "swap the steps"},
            ], "errors": []}))
        (snap / ".frontmatter-validation.json").write_text(json.dumps({
            "files": [{"file": ARTICLE, "menu_parents": [
                {"menu_name": "iac", "parent_identifier": "nowhere",
                 "parent_exists_in_menu": False}], "alias_collisions": []}]}))

        ev = lambda diff, verdict=None, branch="content-review/x": evaluate(
            diff, BLOB, verdict, snap, ARTICLE, branch)

        r = ev(_diff(["@@ -10,1 +10,1 @@",
                      "-Pulumi supports version 3.100 of the CLI.",
                      "+Pulumi supports version 3.147 of the CLI."]))
        check("in-range claim fix passes", r["result"] == "pass")

        r = ev(_diff(["@@ -50,1 +50,1 @@",
                      "-A paragraph that is perfectly fine and was never flagged.",
                      "+A paragraph rewritten on a whim."]))
        check("out-of-range prose edit fails", r["result"] == "fail")
        check("verified (non-contradicted) claim grants no range",
              all(x["category"] != "claim" or x["source"] != "verified-claims:c2"
                  for x in r["allowed_ranges"]))
        check("uncovered hunk is reported with its lines",
              r["uncovered_hunks"][0]["old_start"] == 50)

        r = ev(_diff(["@@ -8,7 +8,2 @@"]
                     + [f"-line {i}" for i in range(8, 15)]
                     + ["+# Example", "+Pulumi supports version 3.147 of the CLI."]))
        check("oversized hunk overlapping a finding still fails (full coverage)",
              r["result"] == "fail")

        r = ev(_diff(["@@ -11,0 +12,1 @@",
                      "+Adjacent clarification within the claim's tolerance."]))
        check("insertion adjacent to a finding passes", r["result"] == "pass")

        r = ev(_diff(["@@ -49,0 +50,1 @@", "+Entirely new paragraph far away."]))
        check("distant insertion fails", r["result"] == "fail")

        r = ev(_diff(["@@ -5,1 +5,1 @@", "-    parent: nowhere", "+    parent: iac-home"]))
        check("frontmatter hunk passes with reported violation", r["result"] == "pass")

        (snap / ".frontmatter-validation.json").write_text(json.dumps({
            "files": [{"file": ARTICLE, "menu_parents": [
                {"menu_name": "iac", "parent_identifier": "nowhere",
                 "parent_exists_in_menu": True}], "alias_collisions": []}]}))
        r = ev(_diff(["@@ -2,1 +2,1 @@", "-title: Example", "+title: Renamed"]))
        check("frontmatter hunk fails without a violation", r["result"] == "fail")

        link_verdict = {"verdict": "fixed", "applied": [
            {"category": "link", "file": ARTICLE, "lines": [20, 20],
             "source": "dead link /docs/iac/stacks/"}]}
        r = ev(_diff(["@@ -20,1 +20,1 @@",
                      "-See [the stacks doc](/docs/iac/stacks/) for more.",
                      "+See [the stacks doc](/docs/iac/concepts/stacks/) for more."]),
               verdict=link_verdict)
        check("declared link fix on a link-bearing line passes", r["result"] == "pass")

        bad_link = {"verdict": "fixed", "applied": [
            {"category": "link", "file": ARTICLE, "lines": [50, 50],
             "source": "dead link"}]}
        r = ev(_diff(["@@ -50,1 +50,1 @@",
                      "-A paragraph that is perfectly fine and was never flagged.",
                      "+A paragraph laundered through a fake link entry."]),
               verdict=bad_link)
        check("link entry on a non-link line is rejected and fails",
              r["result"] == "fail" and r["invalid_applied"])

        fake_claim = {"verdict": "fixed", "applied": [
            {"category": "claim", "file": ARTICLE, "lines": [50, 50],
             "source": "made-up finding"}]}
        r = ev(_diff(["@@ -50,1 +50,1 @@",
                      "-A paragraph that is perfectly fine and was never flagged.",
                      "+Rewritten."]), verdict=fake_claim)
        check("applied claim entry with no artifact finding is invalid + fails",
              r["result"] == "fail" and r["invalid_applied"][0]["why"]
              == "no matching finding in the snapshot artifacts")

        r = ev(_diff(["@@ -10,1 +10,1 @@", "-x", "+y",
                      "diff --git a/content/docs/other.md b/content/docs/other.md",
                      "--- a/content/docs/other.md", "+++ b/content/docs/other.md",
                      "@@ -1,1 +1,1 @@", "-a", "+b"]))
        check("hunk in a second file fails",
              r["result"] == "fail"
              and r["uncovered_hunks"][0]["why"] == "edit outside the reviewed article")

        # Reorder: the readthrough local_repair at L40 covers deleting the
        # out-of-order step; re-inserting the same text elsewhere is a move.
        r = ev(_diff(["@@ -40,1 +40,0 @@",
                      "-Step two comes before step one in this section.",
                      "@@ -25,0 +25,1 @@",
                      "+Step two comes before step one in this section."]))
        check("move heuristic accepts a readthrough reorder", r["result"] == "pass")

        r = ev("", branch="content-review/x")
        check("empty diff skips", r["result"] == "skipped")

        r = ev(_diff(["@@ -1,50 +0,0 @@"] + [f"-{l}" for l in BLOB.splitlines()]),
               branch="content-review/retire-x")
        check("retire branch skips", r["result"] == "skipped")

        # Workflow mode: no branch is passed (retirement routes to the veto
        # instead), so a retirement-shaped patch under a non-retirement
        # verdict must FAIL here, not skip.
        r = ev(_diff(["@@ -1,50 +0,0 @@"] + [f"-{l}" for l in BLOB.splitlines()]),
               branch="")
        check("branch-less retirement-shaped patch fails (no skip)",
              r["result"] == "fail")
        r = ev(_diff(["@@ -10,1 +10,1 @@",
                      "-Pulumi supports version 3.100 of the CLI.",
                      "+Pulumi supports version 3.147 of the CLI."]), branch="")
        check("branch-less in-range fix still passes", r["result"] == "pass")

        (snap / ".verified-claims.json").write_text(json.dumps({
            "schema_version": 1, "verdicts": [],
            "errors": ["verify-claims.py failed to start"]}))
        r = ev(_diff(["@@ -10,1 +10,1 @@",
                      "-Pulumi supports version 3.100 of the CLI.",
                      "+Pulumi supports version 3.147 of the CLI."]))
        check("stubbed claims artifact blocks claim fixes (fail closed)",
              r["result"] == "fail")

    if failures:
        print(f"\n{len(failures)} failure(s)", file=sys.stderr)
        return 1
    print("\nall verify-fix-scope self-tests passed")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(
        description="Code-enforced fix-scope gate for content-review promotion.")
    p.add_argument("--branch", default="",
                   help="review branch (content-review/<slug>); required only "
                        "without --diff-file (branch mode derives the diff from "
                        "origin/<branch>), and enables the retire-branch skip")
    p.add_argument("--base-sha", help="master SHA the pre-steps ran on")
    p.add_argument("--article", help="article repo path (content/docs/...)")
    p.add_argument("--verdict", help="model verdict sentinel (.content-review-verdict.json)")
    p.add_argument("--artifacts-dir",
                   help="pre-model snapshot dir holding the pre-step artifact JSONs")
    p.add_argument("--out", default=".fix-scope-report.json",
                   help="machine-readable report path")
    p.add_argument("--diff-file", help="inject the branch diff (tests); skips git")
    p.add_argument("--article-blob", help="inject the pre-fix article content (tests)")
    p.add_argument("--self-test", action="store_true", help="run built-in checks")
    args = p.parse_args()

    if args.self_test:
        return self_test()
    missing = [f for f in ("article", "artifacts_dir") if not getattr(args, f)]
    if not args.diff_file and not args.branch:
        missing.append("branch (or --diff-file)")
    if not args.base_sha and not (args.diff_file and args.article_blob):
        missing.append("base_sha")
    if missing:
        p.error("required: --" + ", --".join(m.replace("_", "-") for m in missing))
    return run(args)


if __name__ == "__main__":
    sys.exit(main())
