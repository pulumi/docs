#!/usr/bin/env python3
"""Deterministic scope gate for glow-up (whole-page rehab) reviews.

The fix lane's `verify-fix-scope.py` requires every hunk to sit inside a
recorded finding's line range — exactly wrong for a glow-up, whose whole job
is page-wide restructuring. This gate bounds a glow-up differently, judged
from the zero-context diff and the PRE-model article snapshot:

1. Paths: only the queued article itself, plus non-markdown files in its own
   directory (page-bundle assets). Never sibling articles, never shared
   render sources — a glow-up is one page's rehab.
2. Size: total added+deleted lines <= MAX_CHANGED_LINES. A rehab bigger than
   that is a rewrite the human should be doing interactively.
3. The article must not be deleted (a glow-up is never a retirement).
4. Protected frontmatter: `title`, `aliases`, and `redirect_to` must be
   byte-identical before and after. Retitling and URL surgery change the
   page's identity and SEO surface — out of scope for this lane.

Exit codes mirror verify-fix-scope: 0 = pass, 2 = violation (report written
either way), 1 = operational error.

Usage:
    verify-glowup-scope.py --diff-file .review-changes.u0.diff \
        --article <path> --article-blob .review-snapshot/article-base.txt \
        [--max-changed-lines N] [--out .glowup-scope-report.json]

Self-contained smoke checks: `python3 verify-glowup-scope.py --self-test`.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path, PurePosixPath

import yaml

SCHEMA_VERSION = 1
MAX_CHANGED_LINES = 400
PROTECTED_KEYS = ("title", "aliases", "redirect_to")

FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
HUNK_RE = re.compile(r"^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@")


def warn(msg: str) -> None:
    print(f"::warning::verify-glowup-scope: {msg}", file=sys.stderr)


def error(msg: str) -> None:
    print(f"::error::verify-glowup-scope: {msg}", file=sys.stderr)


def parse_diff(diff_text: str) -> tuple[dict[str, dict], int]:
    """Per-path {deleted: bool, hunks: [...]}, plus total changed-line count.

    Hunks are collected for the article's frontmatter re-application; each is
    (old_start, old_count, [added lines]).
    """
    files: dict[str, dict] = {}
    churn = 0
    current: dict | None = None
    old_path = None
    for line in diff_text.splitlines():
        if line.startswith("diff --git "):
            current = None
            old_path = None
            continue
        if line.startswith("--- "):
            old_path = None if line.endswith("/dev/null") else line[4:].removeprefix("a/")
            continue
        if line.startswith("+++ "):
            new_path = None if line.endswith("/dev/null") else line[4:].removeprefix("b/")
            path = new_path or old_path
            if path:
                current = files.setdefault(path, {"deleted": new_path is None, "hunks": []})
                current["deleted"] = new_path is None
            continue
        m = HUNK_RE.match(line)
        if m and current is not None:
            current["hunks"].append({
                "old_start": int(m.group(1)),
                "old_count": int(m.group(2) or "1"),
                "added": [],
            })
            continue
        if current is not None and current["hunks"] and line.startswith("+"):
            current["hunks"][-1]["added"].append(line[1:])
            churn += 1
        elif current is not None and current["hunks"] and line.startswith("-"):
            churn += 1
    return files, churn


def apply_hunks(base: str, hunks: list[dict]) -> str:
    """Re-apply zero-context hunks to the base text (old-side line numbers)."""
    base_lines = base.splitlines()
    out: list[str] = []
    cursor = 0  # 0-based index into base_lines
    for h in sorted(hunks, key=lambda h: h["old_start"]):
        # In unified diffs an old_count of 0 (pure insertion) anchors AFTER
        # the old_start line; a non-zero count starts AT old_start.
        start = h["old_start"] if h["old_count"] == 0 else h["old_start"] - 1
        out.extend(base_lines[cursor:start])
        out.extend(h["added"])
        cursor = start + h["old_count"]
    out.extend(base_lines[cursor:])
    return "\n".join(out) + ("\n" if base.endswith("\n") or out else "")


def frontmatter(text: str) -> dict:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    try:
        fm = yaml.safe_load(m.group(1))
    except yaml.YAMLError:
        return {}
    return fm if isinstance(fm, dict) else {}


def evaluate(diff_text: str, article: str, base_blob: str,
             max_changed_lines: int) -> dict:
    files, churn = parse_diff(diff_text)
    violations: list[str] = []

    art_dir = str(PurePosixPath(article).parent)
    for path, info in files.items():
        if path == article:
            if info["deleted"]:
                violations.append(f"article {article!r} is deleted — a glow-up is never a retirement")
            continue
        in_bundle = str(PurePosixPath(path).parent) == art_dir
        if in_bundle and not path.endswith(".md"):
            continue  # a page-bundle asset (image, include) — allowed
        violations.append(f"changed path {path!r} is outside the glow-up scope "
                          f"(the article and its bundle's non-markdown assets)")

    if churn > max_changed_lines:
        violations.append(f"diff churn {churn} exceeds the glow-up ceiling "
                          f"({max_changed_lines} changed lines)")

    art = files.get(article)
    if art and not art["deleted"]:
        new_blob = apply_hunks(base_blob, art["hunks"])
        before, after = frontmatter(base_blob), frontmatter(new_blob)
        for key in PROTECTED_KEYS:
            if before.get(key) != after.get(key):
                violations.append(
                    f"protected frontmatter key {key!r} changed "
                    f"({before.get(key)!r} -> {after.get(key)!r})")

    return {
        "schema_version": SCHEMA_VERSION,
        "result": "pass" if not violations else "violation",
        "article": article,
        "changed_paths": sorted(files),
        "churn": churn,
        "violations": violations,
    }


def run(args) -> int:
    try:
        diff_text = Path(args.diff_file).read_text()
        base_blob = Path(args.article_blob).read_text()
    except OSError as e:
        error(f"required input unreadable ({e})")
        return 1
    report = evaluate(diff_text, args.article, base_blob, args.max_changed_lines)
    Path(args.out).write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({k: report[k] for k in ("result", "churn", "changed_paths")}))
    if report["violations"]:
        for v in report["violations"]:
            error(v)
        return 2
    return 0


def self_test() -> int:
    failures = []

    def check(name, cond):
        if not cond:
            failures.append(name)
            print(f"FAIL: {name}", file=sys.stderr)
        else:
            print(f"ok: {name}")

    art = "content/docs/x/guide.md"
    base = "---\ntitle: Guide\naliases:\n- /docs/old/\n---\n\nIntro.\nBody line.\nOutro.\n"

    def diff_for(path, hunks_text, deleted=False):
        new = "/dev/null" if deleted else f"b/{path}"
        return (f"diff --git a/{path} b/{path}\n--- a/{path}\n+++ {new}\n" + hunks_text)

    # Prose rewrite inside the page: pass, frontmatter intact.
    d = diff_for(art, "@@ -7,1 +7,2 @@\n-Body line.\n+Better body.\n+Extra detail.\n")
    r = evaluate(d, art, base, 400)
    check("in-page rewrite passes", r["result"] == "pass" and r["churn"] == 3)

    # A bundle asset alongside: allowed. A sibling article: not.
    d2 = d + diff_for("content/docs/x/diagram.png", "@@ -1,1 +1,1 @@\n-x\n+y\n")
    check("bundle asset allowed", evaluate(d2, art, base, 400)["result"] == "pass")
    d3 = d + diff_for("content/docs/x/other.md", "@@ -1,1 +1,1 @@\n-x\n+y\n")
    r3 = evaluate(d3, art, base, 400)
    check("sibling article rejected", r3["result"] == "violation"
          and any("outside the glow-up scope" in v for v in r3["violations"]))

    # Churn ceiling.
    big = diff_for(art, "@@ -7,1 +7,401 @@\n-Body line.\n" + "+l\n" * 401)
    check("churn over ceiling rejected",
          any("ceiling" in v for v in evaluate(big, art, base, 400)["violations"]))

    # Deletion.
    gone = diff_for(art, "@@ -1,8 +0,0 @@\n" + "".join(f"-{l}\n" for l in base.splitlines()),
                    deleted=True)
    check("article deletion rejected",
          any("never a retirement" in v for v in evaluate(gone, art, base, 400)["violations"]))

    # Protected frontmatter: retitle rejected; body edit that leaves it alone passes.
    retitle = diff_for(art, "@@ -2,1 +2,1 @@\n-title: Guide\n+title: The Best Guide\n")
    rt = evaluate(retitle, art, base, 400)
    check("retitle rejected", any("'title' changed" in v for v in rt["violations"]))
    dealias = diff_for(art, "@@ -3,2 +3,0 @@\n-aliases:\n-- /docs/old/\n")
    check("alias removal rejected",
          any("'aliases' changed" in v for v in evaluate(dealias, art, base, 400)["violations"]))

    # Pure insertion hunk (old_count 0) applies correctly.
    ins = diff_for(art, "@@ -6,0 +7,1 @@\n+A new paragraph.\n")
    check("pure insertion passes with frontmatter intact",
          evaluate(ins, art, base, 400)["result"] == "pass")

    if failures:
        print(f"\n{len(failures)} failure(s)", file=sys.stderr)
        return 1
    print("\nall verify-glowup-scope self-tests passed")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--diff-file", help="zero-context diff of the staged changes")
    p.add_argument("--article", help="the queued article path")
    p.add_argument("--article-blob", help="pre-model article content (snapshot)")
    p.add_argument("--max-changed-lines", type=int, default=MAX_CHANGED_LINES)
    p.add_argument("--out", default=".glowup-scope-report.json")
    p.add_argument("--self-test", action="store_true", help="run built-in smoke checks")
    args = p.parse_args()
    if args.self_test:
        return self_test()
    missing = [f for f in ("diff_file", "article", "article_blob") if not getattr(args, f)]
    if missing:
        p.error("missing required argument(s): " + ", ".join(missing))
    return run(args)


if __name__ == "__main__":
    sys.exit(main())
