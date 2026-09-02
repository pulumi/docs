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

Plus one SOFT check, a `::warning::` rather than a violation: added lines
carrying superlative or ranking language ("fastest", "the recommended",
"where to start", "the only", …) that no `verified` verdict in this run's
`.verified-claims.json` sits under. PR #21291 (2026-09-01) shipped
"`pulumi convert` is the fastest path for most configurations, and it's where
to start" with no artifact behind it; the words are the extractor's own
`POSITIONING_RES` (imported, not copied) plus the bare forms the glow-up
actually wrote. The model is told to acknowledge each warning in the PR body
— cite the supporting verdict or remove the language — and the reviewer sees
the same list in the report's `superlatives`.

Exit codes mirror verify-fix-scope: 0 = pass, 2 = violation (report written
either way), 1 = operational error.

Usage:
    verify-glowup-scope.py --diff-file .review-changes.u0.diff \
        --article <path> --article-blob .review-snapshot/article-base.txt \
        [--verified-claims .verified-claims.json] \
        [--max-changed-lines N] [--out .glowup-scope-report.json]

Self-contained smoke checks: `python3 verify-glowup-scope.py --self-test`.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path, PurePosixPath

import yaml

SCHEMA_VERSION = 1
MAX_CHANGED_LINES = 400
PROTECTED_KEYS = ("title", "aliases", "redirect_to")

HERE = Path(__file__).resolve().parent
_EXTRACT_CLAIMS = (HERE.parent.parent / ".claude" / "commands" / "docs-review"
                   / "scripts" / "extract-claims.py")
# The bare forms PR #21291 wrote; the extractor's list needs "the " before
# recommended/primary and never matches "where to start". "best practice(s)"
# is the one idiom a docs page says all day without ranking anything.
SUPERLATIVE_SUPPLEMENT_RES = [
    re.compile(r"\bwhere to start\b", re.I),
    re.compile(r"\b(?:recommended|primary)\b", re.I),
    re.compile(r"\bbest\b(?!\s+practices?\b)", re.I),
]
SUPPORT_VERDICTS = {"verified", "matches"}
SUPPORT_TOLERANCE = 2  # lines, mirrors verify-fix-scope's TOL_DEFAULT


def superlative_patterns() -> list[re.Pattern]:
    """The extractor's `POSITIONING_RES` plus the supplement. Imported by path
    so the two vocabularies cannot drift; a missing extractor degrades to the
    supplement with a warning rather than silencing the check."""
    pats: list[re.Pattern] = []
    try:
        spec = importlib.util.spec_from_file_location("extract_claims", _EXTRACT_CLAIMS)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        pats.extend(mod.POSITIONING_RES)
    except Exception as e:  # noqa: BLE001
        warn(f"extract-claims.py unavailable ({e}); superlative check uses the supplement only")
    pats.extend(SUPERLATIVE_SUPPLEMENT_RES)
    return pats

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
                "new_start": int(m.group(3)),
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


def _verdict_spans(verified) -> list[tuple[int, int]]:
    spans = []
    for v in ((verified or {}).get("verdicts") or []) if isinstance(verified, dict) else []:
        if (v.get("verdict") or "").lower() not in SUPPORT_VERDICTS:
            continue
        for a, b in re.findall(r"L?(\d+)(?:-L?(\d+))?", str(v.get("line_range") or "")):
            lo = int(a)
            hi = int(b) if b else lo
            spans.append((min(lo, hi), max(lo, hi)))
    return spans


def superlatives(hunks: list[dict], verified, patterns: list[re.Pattern] | None = None) -> list[dict]:
    """Added lines carrying superlative/ranking language, each marked with
    whether a `verified`/`matches` verdict sits on the OLD lines the hunk
    replaces (±SUPPORT_TOLERANCE). The verdicts are pre-model and numbered
    against the base file, so the old side of the hunk is the only honest
    place to look; a pure insertion anchors on the line it follows."""
    patterns = superlative_patterns() if patterns is None else patterns
    spans = _verdict_spans(verified)
    out: list[dict] = []
    for h in hunks:
        old_lo = h["old_start"] - SUPPORT_TOLERANCE
        old_hi = h["old_start"] + max(h["old_count"], 1) - 1 + SUPPORT_TOLERANCE
        supported = any(a <= old_hi and b >= old_lo for a, b in spans)
        in_fence = False
        for i, text in enumerate(h["added"]):
            if text.lstrip().startswith(("```", "~~~")):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            hit = next((m.group(0) for rx in patterns for m in [rx.search(text)] if m), None)
            if not hit:
                continue
            out.append({
                "line": h.get("new_start", h["old_start"]) + i,
                "old_lines": f"L{h['old_start']}" + (f"-{h['old_start'] + h['old_count'] - 1}" if h["old_count"] > 1 else ""),
                "match": hit.strip(),
                "text": text.strip()[:200],
                "supported": supported,
            })
    return out


def evaluate(diff_text: str, article: str, base_blob: str,
             max_changed_lines: int, verified=None,
             patterns: list[re.Pattern] | None = None) -> dict:
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

    flagged = superlatives(art["hunks"], verified, patterns) if art and not art["deleted"] else []
    warnings = [
        f"superlative or ranking language added at L{f['line']} with no verified "
        f"verdict on {f['old_lines']}: \"{f['match']}\" in \"{f['text'][:120]}\" — "
        "cite the artifact verdict that supports it in the PR body, or remove it"
        for f in flagged if not f["supported"]
    ]

    return {
        "schema_version": SCHEMA_VERSION,
        "result": "pass" if not violations else "violation",
        "article": article,
        "changed_paths": sorted(files),
        "churn": churn,
        "violations": violations,
        "superlatives": flagged,
        "warnings": warnings,
    }


def run(args) -> int:
    try:
        diff_text = Path(args.diff_file).read_text()
        base_blob = Path(args.article_blob).read_text()
    except OSError as e:
        error(f"required input unreadable ({e})")
        return 1
    verified = None
    if args.verified_claims:
        try:
            verified = json.loads(Path(args.verified_claims).read_text())
        except (OSError, json.JSONDecodeError) as e:
            warn(f"{args.verified_claims} unreadable ({e}); every superlative counts as unsupported")
    report = evaluate(diff_text, args.article, base_blob, args.max_changed_lines, verified)
    Path(args.out).write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({k: report[k] for k in ("result", "churn", "changed_paths")}))
    for w in report["warnings"]:
        warn(w)
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

    # Superlatives: a soft check. PR #21291's sentence, verbatim.
    pats = superlative_patterns()
    fastest = diff_for(art, "@@ -7,1 +7,1 @@\n-Body line.\n+`pulumi convert` is the fastest path "
                       "for most configurations, and it's where to start.\n")
    r = evaluate(fastest, art, base, 400, None, pats)
    check("superlative on an added line is reported, not a violation",
          r["result"] == "pass" and len(r["superlatives"]) == 1
          and r["superlatives"][0]["supported"] is False and len(r["warnings"]) == 1)
    check("the report names the line, the match and the old range",
          r["superlatives"][0]["line"] == 7 and r["superlatives"][0]["match"] == "fastest"
          and r["superlatives"][0]["old_lines"] == "L7")
    backed = {"verdicts": [{"claim_id": "c1", "line_range": "L8", "verdict": "verified"}]}
    r2 = evaluate(fastest, art, base, 400, backed, pats)
    check("a verified verdict within tolerance of the replaced lines counts as support",
          r2["superlatives"][0]["supported"] is True and not r2["warnings"])
    far = {"verdicts": [{"claim_id": "c1", "line_range": "L40", "verdict": "verified"}]}
    check("a verified verdict elsewhere on the page does not",
          evaluate(fastest, art, base, 400, far, pats)["superlatives"][0]["supported"] is False)
    contra = {"verdicts": [{"claim_id": "c1", "line_range": "L7", "verdict": "contradicted"}]}
    check("only verified/matches verdicts support a superlative",
          evaluate(fastest, art, base, 400, contra, pats)["superlatives"][0]["supported"] is False)
    bare = diff_for(art, "@@ -7,1 +7,2 @@\n-Body line.\n+This is the recommended approach.\n"
                    "+Follow the best practices below.\n")
    r3 = evaluate(bare, art, base, 400, None, pats)
    check("bare 'recommended' is flagged, 'best practices' is not",
          [f["match"].lower() for f in r3["superlatives"]] == ["the recommended"])
    fenced = diff_for(art, "@@ -7,1 +7,3 @@\n-Body line.\n+```bash\n+echo fastest\n+```\n")
    check("code inside an added fence is skipped",
          not evaluate(fenced, art, base, 400, None, pats)["superlatives"])
    plain = diff_for(art, "@@ -7,1 +7,1 @@\n-Body line.\n+A plain sentence about stacks.\n")
    check("no superlative, no warning", not evaluate(plain, art, base, 400, None, pats)["warnings"])

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
    p.add_argument("--verified-claims", default="",
                   help="this run's .verified-claims.json; a verified verdict on the "
                        "replaced lines is what makes added superlative language 'supported'")
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
