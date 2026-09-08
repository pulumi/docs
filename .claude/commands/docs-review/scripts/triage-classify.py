#!/usr/bin/env python3
"""Deterministic PR triage classification.

Reads the PR JSON (from `gh pr view --json title,body,author,files,labels,additions,deletions,commits,isDraft`)
on argv[1] and the unified diff (from `gh pr diff`) on stdin. Emits a single
JSON object on stdout with the classification fields the workflow consumes.

This script does not call any APIs and has no side effects. The model is only
invoked downstream when `prose_check_needed` is true (trivial or
frontmatter-only PRs); everything else is path matching and grep-on-diff.

Importable by path (`importlib.util.spec_from_file_location`, same pattern
`review-worklist.py` uses for `validate-pinned.py`): every top-level
statement is a def/class/constant, and `main()` is guarded by
`if __name__ == "__main__":`, so importing this module runs no I/O and has
no side effects. `classify_path`, `classify_file`, `classify_pr`, and (v3)
`classify_mechanical` are the stable functions other scripts should import
rather than re-implement.
"""

from __future__ import annotations

import importlib.util
import json
import re
import subprocess
import sys
from collections.abc import Iterable
from pathlib import Path

HERE = Path(__file__).resolve().parent

# ---- Path-precedence domain classification --------------------------------

WEBPACK_RE = re.compile(r"^webpack\.[^/]+\.js$")

# Applied at the PR level when no file matched a domain rule, so that every
# triaged PR carries exactly one domain signal and "no domain label" always
# means "triage didn't run" rather than "triage ran and had nothing to say".
# Deliberately NOT domain:mixed: mixed is derived from len(domains) > 1 and
# asserts "touches more than one domain, each file reviewed under its own" —
# the opposite of what's true here — and overloading it would destroy its
# filter value for the multi-domain PRs it exists to mark. domain:other is
# an honest "no specific domain"; those files review under shared-criteria
# only, per docs-review:references:domain-routing rule 6.
FALLBACK_DOMAIN = "domain:other"

# Above this many changed lines (additions + deletions), the PR is `oversized`:
# too big for the review pipeline to finish inside its time budget, and at this
# scale the bulk is invariably generated output that an LLM line-review adds no
# value to (PR #20274: ~100K generated lines; the main review step was killed
# at the then-25-minute job timeout on every attempt). Triage labels it
# `review:oversized` and the review workflow skips it with an advisory comment
# instead of error-cycling. Hand-written PRs run one to two orders of
# magnitude smaller.
OVERSIZED_TOTAL_LINES = 15_000

# File count is an independent budget axis: a PR can sit well under the line
# threshold and still not be reviewable, because per-file work (claim
# extraction, sibling reads, per-page verdicts) scales with pages touched,
# not lines. PR #20560 (155 files, ~3.5K changed lines) timed out the Opus
# step on every attempt and error-cycled exactly the way the line threshold
# exists to prevent. Either axis over budget classifies the PR oversized.
OVERSIZED_TOTAL_FILES = 150


def classify_path(path: str) -> str | None:
    # Programs first — both static/programs/** AND scripts/programs/** are
    # programs territory (the latter would otherwise fall to infra).
    if path.startswith("static/programs/") or path.startswith("scripts/programs/"):
        return "domain:programs"
    if path.startswith("content/blog/") or path.startswith("content/case-studies/"):
        return "domain:blog"
    for prefix in ("content/docs/", "content/what-is/"):
        if path.startswith(prefix):
            return "domain:docs"
    if path.startswith(".github/workflows/"):
        return "domain:infra"
    if path.startswith("scripts/") or path.startswith("infrastructure/"):
        return "domain:infra"
    if path in ("Makefile", "package.json", "webpack.config.js"):
        return "domain:infra"
    if WEBPACK_RE.match(path):
        return "domain:infra"
    # Hugo templates + asset-pipeline source + static-served files — build-time
    # infrastructure that affects how content renders. static/programs/ is
    # already routed at the top of this function (programs check returns
    # first); the explicit exclusion below documents intent for readers.
    # theme/ is the same kind of thing one level down: the SCSS and TypeScript
    # sources compiled into the site's CSS/JS bundles. Its omission is why
    # PR #21164 (a consent-manager change under theme/src/ts/) carried no
    # domain label and was reviewed under shared-criteria only.
    if (path.startswith("layouts/")
            or path.startswith("assets/")
            or path.startswith("theme/")):
        return "domain:infra"
    if path.startswith("static/") and not path.startswith("static/programs/"):
        return "domain:infra"
    # Marketing / landing pages under content/ that aren't blog or docs
    # (about/, pricing/, vs/, why-pulumi/, legal/, careers/, etc.). These
    # carry pricing, legal, and competitive claims with real consequences
    # if wrong, so they need their own domain rather than the bare
    # shared-criteria fallback.
    if path.startswith("content/") and path.endswith(".md"):
        return "domain:website"
    return None


# ---- Per-file diff inspection ---------------------------------------------

HUNK_HEADER_RE = re.compile(r"^@@ -(\d+)(?:,\d+)? \+(\d+)(?:,\d+)? @@")
LINK_RE = re.compile(r"\[[^\]]*\]\([^)]+\)")
# A top-level (unindented) YAML `key:` line inside a frontmatter block. Used
# to attribute a frontmatter change to the key it belongs to (v3 mechanical
# bar §6) — an indented continuation/list-item line under that key doesn't
# match, so `current_key` (tracked below) stays whatever the last top-level
# key line said.
FRONTMATTER_KEY_RE = re.compile(r"^([a-zA-Z_][a-zA-Z0-9_-]*):")


def split_files(diff_text: str) -> list[tuple[str, str]]:
    """Split the unified diff into [(path, file_diff_text), ...]."""
    if not diff_text.strip():
        return []
    chunks = re.split(r"^diff --git ", diff_text, flags=re.MULTILINE)
    out: list[tuple[str, str]] = []
    for chunk in chunks[1:]:  # chunks[0] is empty preamble
        first_line, _, _ = chunk.partition("\n")
        m = re.match(r"a/(\S+) b/(\S+)", first_line)
        if not m:
            continue
        path = m.group(2)  # 'b' path is the new path (handles renames)
        out.append((path, "diff --git " + chunk))
    return out


# Lines a compiler would recognise: statement/block terminators, declaration
# keywords, comment openers, operators that don't occur in prose. Kept
# deliberately narrow — a prose line ending in `)` or containing `=` is not
# code; `{`, `;`, `=>`, `:=` and leading keywords are. The heuristic only ever
# ADDS "this is code" signal, and a wrong call there costs one review run;
# the wrong call in the other direction skipped the review entirely.
_CODE_LINE_RE = re.compile(
    r"^\s*(?:import |package |func |const |var |let |def |class |public |private |protected "
    r"|return\b|export |from \S+ import |using |namespace |@\w+|#include|\}|\)|//|/\*|\*/)"
    r"|[{};]\s*$|:=|=>|\(\)|\bnew \w+\("
)


def _looks_like_code(text: str) -> bool:
    return bool(_CODE_LINE_RE.search(text))


def _hunk_looks_like_code(body_lines: list[str], min_lines: int = 3, ratio: float = 0.6) -> bool:
    """True when most of a hunk's non-blank lines (context + changes) read as
    code — the shape of a hunk that starts inside a fenced block."""
    texts = [ln[1:] for ln in body_lines if ln and ln[1:].strip()]
    if len(texts) < min_lines:
        return False
    return sum(1 for t in texts if _looks_like_code(t)) / len(texts) >= ratio


def iter_hunks(file_diff: str) -> Iterable[tuple[str, list[str]]]:
    """Yield (header_line, body_lines) per hunk."""
    header: str | None = None
    body: list[str] = []
    in_hunk = False
    for line in file_diff.split("\n"):
        if line.startswith("@@"):
            if header is not None:
                yield header, body
            header = line
            body = []
            in_hunk = True
        elif in_hunk:
            body.append(line)
    if header is not None:
        yield header, body


def detect_starting_state(body_lines: list[str], old_start: int) -> str:
    """For an .md file hunk, decide whether the hunk starts in frontmatter
    or body. Uses `---` context lines as ground truth when present;
    falls back to content-shape heuristics."""
    dashdash_positions = [
        i for i, line in enumerate(body_lines)
        if line.startswith(" ") and line[1:].strip() == "---"
    ]
    # Two or more `---` context lines: hunk started before the opening
    # delimiter (only happens when old_start == 1).
    if len(dashdash_positions) >= 2:
        return "pre-frontmatter"
    # Single `---` context line: opening if old_start == 1, otherwise
    # closing (the more common case for aliases / meta_desc edits).
    if len(dashdash_positions) == 1:
        return "pre-frontmatter" if old_start == 1 else "frontmatter"
    # No `---` context. Hugo content frontmatter sits in the first ~30
    # lines of every file; a hunk past that is body, full stop. The
    # YAML-key heuristic below is unreliable past frontmatter because
    # markdown YAML code blocks (e.g., `description: A minimal program.`
    # inside a Pulumi.yaml example) match the same shape and cause body
    # changes to be misclassified as frontmatter changes.
    if old_start > 30:
        return "body"
    # No `---` context. Look at the surrounding content to guess.
    for line in body_lines:
        if not line:
            continue
        if line[0] not in " +-":
            continue
        stripped = line[1:].strip()
        if not stripped:
            continue
        # Markdown-shaped content → body.
        if stripped.startswith(("#", "```", "{{<", "{{%")):
            return "body"
        # YAML-shaped content (key:value at root, no leading whitespace) →
        # frontmatter.
        if re.match(r"^[a-z_][a-zA-Z0-9_-]*:", stripped):
            return "frontmatter"
        # Long prose-looking line → body.
        if len(stripped) > 60 and " " in stripped:
            return "body"
    # Fall back: small line numbers default to frontmatter.
    return "frontmatter" if old_start <= 30 else "body"


def _fence_parity_from_file(repo_root, path: str, header: str, body_lines: list[str]):
    """Is this hunk's first line inside a fenced code block? Counted from the
    checked-out file (fence markers above the hunk start), not from the hunk:
    a hunk whose leading context is the CLOSING fence of a block that opened
    above it reads as "opener" to any diff-only tracker, and that mis-tagged
    two prose-only PRs as code changes in the 2026-09-01 replay (#21220,
    #21089). Tries the new-side start (head checkout) then the old-side start
    (base checkout), accepting whichever position's lines match the file.
    None when the file is missing or neither side lines up — callers fall
    back to the diff-only tracker.

    Pinned by test_triage_classify_mechanical.py::test_fence_parity_seeded_from_file,
    which reproduces the #21220/#21089 shape (a hunk whose leading context
    line is the CLOSING fence of a block opened above it) and asserts the
    diff-only tracker calls it code while the file-seeded pass does not.
    """
    if repo_root is None:
        return None
    m = HUNK_HEADER_RE.match(header)
    if not m:
        return None
    try:
        lines = (Path(repo_root) / path).read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return None
    old_start, new_start = int(m.group(1)), int(m.group(2))
    for start, side in ((new_start, "+"), (old_start, "-")):
        i, ok, checked = start - 1, True, 0
        for ln in body_lines:
            if not ln or ln[0] not in " +-":
                continue
            if ln[0] == " " or ln[0] == side:
                if i >= len(lines) or lines[i] != ln[1:]:
                    ok = False
                    break
                i += 1
                checked += 1
        if ok and checked:
            n = sum(1 for l in lines[: start - 1] if l.lstrip().startswith(("```", "~~~")))
            return n % 2 == 1
    return None


def classify_file(path: str, file_diff: str, repo_root=None) -> dict:
    """Walk a single file's diff and return its classification flags.

    `repo_root` (a checkout of the PR's base or head) lets the fence tracker
    seed each hunk's inside-a-code-block state from the file; without it the
    tracker starts every hunk outside a fence and leans on the code-shaped
    hunk heuristic."""
    head300 = file_diff[:300]
    is_rename = "rename from" in head300 or "rename to" in head300
    is_delete = "+++ /dev/null" in head300
    is_new = "--- /dev/null" in head300
    is_binary = "GIT binary patch" in file_diff or "\nBinary files " in file_diff
    is_md = path.endswith(".md")

    flags = {
        "path": path,
        "is_md": is_md,
        "is_rename": is_rename,
        "is_delete": is_delete,
        "is_new": is_new,
        "is_binary": is_binary,
        "has_frontmatter_change": False,
        "has_body_change": False,
        "has_code_block_change": False,
        "has_shortcode_change": False,
        "has_link_change": False,
        # v3 additions (unused by classify_pr / the CLI output — consumed
        # only by classify_mechanical). Kept on the same flags dict rather
        # than a second per-file structure so there's exactly one place a
        # caller looks for "what did this file's diff do".
        "frontmatter_keys_changed": set(),
    }

    # Per-file link-set comparison: detect link change by comparing the
    # union of (text, url) tuples on `+` lines vs `-` lines. A typo fix in
    # a paragraph that contains unchanged links produces matching sets =>
    # no link change.
    plus_links: set[tuple[str, str]] = set()
    minus_links: set[tuple[str, str]] = set()

    for header, body_lines in iter_hunks(file_diff):
        m = HUNK_HEADER_RE.match(header)
        if not m:
            continue
        old_start = int(m.group(1))

        if is_md:
            state = detect_starting_state(body_lines, old_start)
        else:
            state = "body"

        # Code-inside-fences detection. `has_code_block_change` used to fire
        # only when a changed line WAS a fence marker, so a PR rewriting the
        # Java/Go/TypeScript inside existing fences classified as trivial
        # (+10 lines of snippet fixes → `review:trivial` → review skipped).
        # Two signals, both of which fail toward "code": (1) fence state
        # tracked across the hunk's context lines; (2) a hunk with no marker
        # in view whose lines mostly look like code (the hunk started
        # mid-fence). Mis-calling prose "code" only costs a review run.
        in_fence = False
        if is_md and _hunk_looks_like_code(body_lines):
            flags["has_code_block_change"] = True

        # Which top-level frontmatter key the current line belongs to. Reset
        # per hunk (like `state`): a hunk that starts mid-block without its
        # key line in context can't recover the key from the diff alone —
        # `frontmatter_keys_changed` gets the `<unresolved>` sentinel in that
        # case (see below), which classify_mechanical treats as a disallowed
        # key (fail closed rather than silently accept an unattributable
        # change).
        current_key: str | None = None

        # Code-inside-fences detection. `has_code_block_change` used to fire
        # only when a changed line WAS a fence marker, so a PR rewriting the
        # Java/Go/TypeScript inside existing fences classified as trivial /
        # mechanical (fork PR 242, 2026-09-01: +10 lines of snippet fixes →
        # review skipped). Two signals, both fail toward "code": (1) fence
        # state tracked across the hunk's context lines; (2) a hunk with no
        # marker in view whose lines mostly look like code (the hunk started
        # mid-fence). Mis-calling prose "code" only costs a review run.
        seeded = _fence_parity_from_file(repo_root, path, header, body_lines) if is_md else None
        in_fence = bool(seeded)
        if is_md and seeded is None and _hunk_looks_like_code(body_lines):
            flags["has_code_block_change"] = True

        for line in body_lines:
            if not line:
                continue
            marker = line[0]
            content = line[1:]
            stripped = content.strip()

            if is_md and stripped.startswith(("```", "~~~")) and marker in " +-":
                if marker == " ":
                    in_fence = not in_fence
                    continue
                # a changed fence marker is itself a code-block change (below)
                in_fence = not in_fence

            # Frontmatter boundary toggling — both context and changed
            # lines can be `---`. If a `---` line is added or removed,
            # that's itself a frontmatter change.
            if is_md and stripped == "---" and marker in " +-":
                if state == "pre-frontmatter":
                    state = "frontmatter"
                elif state == "frontmatter":
                    state = "body"
                if marker in "+-":
                    flags["has_frontmatter_change"] = True
                continue

            # Track which top-level key the line belongs to *before* the
            # context-line gate below — a context line (unchanged) still
            # tells us which key's block we're in, the same way it would if
            # a human were reading the diff. Only an unindented `key:` line
            # starts a new key; an indented continuation/list item leaves
            # `current_key` as whatever the last top-level line said.
            if is_md and state == "frontmatter" and content and not content[0].isspace():
                km = FRONTMATTER_KEY_RE.match(content.strip())
                if km:
                    current_key = km.group(1)

            if marker == " ":
                continue  # plain context line, no signal

            if marker not in "+-":
                continue

            if is_md and state in ("pre-frontmatter", "frontmatter"):
                flags["has_frontmatter_change"] = True
                flags["frontmatter_keys_changed"].add(current_key or "<unresolved>")
                continue

            # Body-side change
            flags["has_body_change"] = True
            if stripped.startswith(("```", "~~~")) or in_fence:
                flags["has_code_block_change"] = True
            if "{{<" in stripped or "{{%" in stripped:
                flags["has_shortcode_change"] = True
            line_links = set(re.findall(r"\[([^\]]*)\]\(([^)]+)\)", stripped))
            if marker == "+":
                plus_links |= line_links
            else:
                minus_links |= line_links

    flags["has_link_change"] = plus_links != minus_links
    # v3: net-new and net-removed link pairs, for classify_mechanical's link
    # check. A (text, url) pair present on both sides is unchanged (dropped
    # by the set difference); one that moved from minus to plus with a
    # different text or url shows up in both sets below — the mechanical bar
    # treats that as "removed" (old pair gone) same as an outright deletion.
    flags["link_added_pairs"] = plus_links - minus_links
    flags["link_removed_pairs"] = minus_links - plus_links
    return flags


# ---- v3 mechanical bar ------------------------------------------------------
#
# classify_mechanical() is the tightened "safe to skip the model entirely"
# bar for the v3 review workflow (see scripts/review-v3/README.md). It is
# deliberately NOT wired into classify_pr() or main(): the CLI's `trivial` /
# `frontmatter_only` fields keep today's looser thresholds until the
# workflow itself cuts over, per the v3 rollout plan. This is new, parallel
# logic that reuses classify_path and classify_file's per-file flags rather
# than duplicating them.

# Additions/files unchanged from the v2 trivial bar; deletions is new — v2
# left deletions uncapped, which let a PR that mostly *removes* content
# (e.g. stripping a stale paragraph) through as "trivial" with no line cap
# at all. 30 is generous enough for e.g. deleting a few paragraphs while
# still bounding the blast radius a human isn't reading closely.
MECHANICAL_MAX_ADDITIONS = 10
MECHANICAL_MAX_FILES = 2
MECHANICAL_MAX_DELETIONS = 30

# Frontmatter keys the mechanical bar allows changing unsupervised. Anything
# else (title, meta_desc, aliases, redirect_to, social, category, series,
# ...) can change reader-facing behavior, SEO, or routing, so it always
# needs a read.
FRONTMATTER_MECHANICAL_ALLOWED_KEYS = {"updated", "tags"}

# The two added-line shapes condition 6 already governs, exempt from the
# condition-7 claims signal: an `updated:`/`tags:` key line, and a tags list
# item (lowercase hyphen-delimited single token, per the blog tag rules). A
# single-token body list line matching the latter is conceivable but is still
# bounded by every other mechanical condition.
MECHANICAL_CLAIMS_EXEMPT_LINE_RE = re.compile(r"^(?:(?:updated|tags):(?:\s|$)|- [a-z0-9][a-z0-9-]*$)")

# Files whose content is a live pricing/edition claim. A change here is
# never mechanical regardless of size — see AGENTS.md "Pulumi Cloud
# availability markers" / "Pricing data".
PRICING_SENSITIVE_EXACT = {"data/pulumi_pricing.yaml"}
PRICING_SENSITIVE_PREFIXES = ("content/pricing/",)


def _is_pricing_sensitive(path: str) -> bool:
    return path in PRICING_SENSITIVE_EXACT or any(
        path.startswith(p) for p in PRICING_SENSITIVE_PREFIXES
    )


def _is_internal_absolute_link(url: str) -> bool:
    """True for a `/docs/...`-style absolute internal path.

    The mechanical bar only trusts links shaped like an absolute in-repo
    path — no scheme, no `//` (protocol-relative), no relative `../`. Any
    other shape (external URL, relative link, mailto:, anchor-only `#foo`)
    is treated as "not mechanically verifiable" and fails the link check.
    """
    if not url or not url.startswith("/") or url.startswith("//"):
        return False
    if url.startswith(("http://", "https://", "mailto:")):
        return False
    return True


def _resolve_content_target(url: str, repo_root: Path, added_paths: set[str]) -> bool:
    """Does this internal link's target exist under repo_root's content tree?

    Mirrors validate-pinned.py's `check_internal_link_existence` resolution
    (candidate .md / _index.md / index.md paths under content/, then an
    alias-list grep fallback) rather than importing it: that function reads
    off a `Context` dataclass built from a whole pinned-review body/diff
    (placeholder-token skipping, "target already in this PR's diff" short
    circuit, etc.), which doesn't fit resolving one already-extracted URL
    against a repo checkout. This replicates just the resolution core —
    same two techniques, same order — and nothing else from that function.
    """
    path = url.split("#", 1)[0].split("?", 1)[0].rstrip("/")
    if not path:
        return False
    rel = "content" + path
    candidates_rel = [f"{rel}.md", f"{rel}/_index.md", f"{rel}/index.md"]
    if any((repo_root / c).exists() for c in candidates_rel):
        return True
    # The mechanical bar never allows new files (rule 2), so added_paths is
    # normally empty; kept for parity with the validate-pinned.py logic this
    # mirrors and in case a future caller relaxes that rule.
    if any(c in added_paths for c in candidates_rel):
        return True
    try:
        result = subprocess.run(
            ["git", "grep", "-l", "-e", f"- {path}", "--", "content/"],
            cwd=repo_root, capture_output=True, text=True, timeout=10,
        )
        if result.returncode == 0 and result.stdout.strip():
            return True
    except (subprocess.SubprocessError, OSError):
        pass
    return False


_extract_claims_mod = None


def _extract_claims_from_patch(diff_text: str):
    """Lazy import-by-path of extract-claims.py's Layer-A regex matcher.

    Same import-by-path pattern review-worklist.py uses for
    validate-pinned.py (hyphenated filename, __main__-guarded, no import
    side effects). Reusing `extract_claims_from_patch` — rather than
    re-deriving a claims signal — keeps exactly one copy of the claim
    regexes in the repo; a PR that trips Layer A's claim extraction fails
    the mechanical bar regardless of *what kind* of claim it is.
    """
    global _extract_claims_mod
    if _extract_claims_mod is None:
        spec = importlib.util.spec_from_file_location(
            "triage_classify_extract_claims", HERE / "extract-claims.py")
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        _extract_claims_mod = mod
    return _extract_claims_mod.extract_claims_from_patch(diff_text)


def classify_mechanical(
    pr_data: dict,
    file_flags: list[dict],
    diff_text: str,
    repo_root: Path,
) -> tuple[bool, list[str]]:
    """The v3 tightened mechanical bar: ALL conditions must hold.

    Returns (is_mechanical, reasons) — reasons is empty iff is_mechanical is
    True. Every failing condition appends exactly one human-readable reason
    (these surface verbatim in Sentinel/triage explanations), even when
    several files trip the same condition, so the list stays short and
    scannable rather than exploding per-file.

    `pr_data` is the same `gh pr view --json ...` shape classify_pr() takes;
    `file_flags` is `[classify_file(path, diff) for path, diff in
    split_files(diff_text)]` — the same list main() already builds.
    `diff_text` is the full unified diff (needed whole, not per-file, for
    the claim-extraction pass). `repo_root` resolves internal link targets
    against a real checkout.
    """
    reasons: list[str] = []
    files = pr_data.get("files") or []
    additions = int(pr_data.get("additions") or 0)
    deletions = int(pr_data.get("deletions") or 0)
    file_count = len(files)

    if file_count == 0:
        return False, ["no files changed"]

    # 1. Every file is domain:docs or domain:blog.
    off_domain = sorted(
        f.get("path", "") for f in files
        if classify_path(f.get("path", "")) not in ("domain:docs", "domain:blog")
    )
    if off_domain:
        reasons.append(
            "file(s) outside domain:docs/domain:blog: " + ", ".join(off_domain[:5])
            + (f" (+{len(off_domain) - 5} more)" if len(off_domain) > 5 else "")
        )

    # 2. No new, renamed, deleted, or binary files.
    structural = sorted({
        f["path"] for f in file_flags
        if f["is_new"] or f["is_rename"] or f["is_delete"] or f["is_binary"]
    })
    if structural:
        reasons.append("new/renamed/deleted/binary file(s): " + ", ".join(structural[:5]))

    # 3. Size caps — additions, files, deletions (deletions is new in v3).
    if additions > MECHANICAL_MAX_ADDITIONS:
        reasons.append(f"additions ({additions}) exceed the mechanical cap of {MECHANICAL_MAX_ADDITIONS}")
    if file_count > MECHANICAL_MAX_FILES:
        reasons.append(f"file count ({file_count}) exceeds the mechanical cap of {MECHANICAL_MAX_FILES}")
    if deletions > MECHANICAL_MAX_DELETIONS:
        reasons.append(f"deletions ({deletions}) exceed the mechanical cap of {MECHANICAL_MAX_DELETIONS}")

    # 4. No code fence or shortcode changes.
    code_or_shortcode = sorted({
        f["path"] for f in file_flags
        if f["has_code_block_change"] or f["has_shortcode_change"]
    })
    if code_or_shortcode:
        reasons.append("code fence or shortcode change in: " + ", ".join(code_or_shortcode[:5]))

    # 5. Links: additions only, and every added link is internal + resolves.
    added_paths = {f["path"] for f in file_flags if f["is_new"]}
    link_removed_files: set[str] = set()
    bad_links: list[str] = []
    for f in file_flags:
        if f.get("link_removed_pairs"):
            link_removed_files.add(f["path"])
        for _text, url in sorted(f.get("link_added_pairs") or ()):
            if not _is_internal_absolute_link(url):
                bad_links.append(f"{f['path']}: external/non-internal link added ({url})")
                continue
            if not _resolve_content_target(url, repo_root, added_paths):
                bad_links.append(f"{f['path']}: added link does not resolve ({url})")
    if link_removed_files:
        reasons.append("modified or removed link in: " + ", ".join(sorted(link_removed_files)[:5]))
    if bad_links:
        reasons.append("; ".join(bad_links[:5]) + (f" (+{len(bad_links) - 5} more)" if len(bad_links) > 5 else ""))

    # 6. Frontmatter: changed keys must be a subset of {updated, tags}.
    bad_key_files: list[str] = []
    for f in file_flags:
        bad_keys = (f.get("frontmatter_keys_changed") or set()) - FRONTMATTER_MECHANICAL_ALLOWED_KEYS
        if bad_keys:
            bad_key_files.append(f"{f['path']} ({', '.join(sorted(bad_keys))})")
    if bad_key_files:
        reasons.append("frontmatter key(s) outside {updated, tags} changed: " + ", ".join(bad_key_files[:5]))

    # 7. Claims signal — see claims_signal_reasons().
    reasons.extend(claims_signal_reasons(files, diff_text))

    return (len(reasons) == 0, reasons)


def claims_signal_reasons(files: list[dict], diff_text: str) -> list[str]:
    """Condition 7 of the mechanical bar, callable on its own.

    The routing step also needs this signal in isolation: a claims hit
    stacks the marketing lane onto a PR's required approvers regardless of
    every other mechanical condition, so route-pr.py must be able to ask
    "claims?" without asking "mechanical?".

    Pricing-sensitive paths, or Layer-A claim extraction hitting an added
    line anywhere in the diff. Layer A is reused verbatim, but its net is
    deliberately wider than this condition's purpose (it feeds a downstream
    verifier, so it catches every markdown link and reads
    `updated: YYYY-MM-DD` as a numeric range). Unfiltered, it would shadow
    the two carve-outs that make the mechanical lane exist at all — link
    fixes (condition 5 already forces added links to be internal AND
    resolve) and updated/tags frontmatter bumps (condition 6 already
    forbids every other key). So url-type claims and claims whose source
    line is one of the two allowed frontmatter shapes are exempt here; a
    prose claim (a price, an edition name, a version assertion in body
    text) still disqualifies.
    """
    reasons: list[str] = []
    pricing_hits = sorted({f.get("path", "") for f in files if _is_pricing_sensitive(f.get("path", ""))})
    if pricing_hits:
        reasons.append("pricing-sensitive file(s) changed: " + ", ".join(pricing_hits))
    if diff_text.strip():
        claims, _stats = _extract_claims_from_patch(diff_text)
        claims = [
            c for c in claims
            if c["type"] != "url"
            and not MECHANICAL_CLAIMS_EXEMPT_LINE_RE.match(c["text"])
        ]
        if claims:
            c0 = claims[0]
            reasons.append(
                f"claim-extraction signal on an added line (e.g. {c0['file']} {c0['line_range']}, "
                f"type={c0['type']}; {len(claims)} total)"
            )
    return reasons


# ---- PR-level aggregation --------------------------------------------------


def classify_pr(pr_data: dict, file_flags: list[dict]) -> dict:
    additions = int(pr_data.get("additions") or 0)
    deletions = int(pr_data.get("deletions") or 0)
    files = pr_data.get("files") or []
    file_count = len(files)
    total_lines = additions + deletions

    domains: set[str] = set()
    for f in files:
        d = classify_path(f.get("path", ""))
        if d:
            domains.add(d)
    # Fallback fires only for a PR where NOTHING classified — never
    # alongside a real domain. A PR touching content/docs/ plus data/ is
    # domain:docs, not docs+other+mixed: the unmatched file adds no review
    # lane, so surfacing it as a second domain would flip `mixed` on
    # PRs that aren't. Placed before the mixed computation for that reason.
    if not domains and files:
        domains.add(FALLBACK_DOMAIN)

    has_any_frontmatter = any(f["has_frontmatter_change"] for f in file_flags)
    has_any_body = any(f["has_body_change"] for f in file_flags)
    has_any_link = any(f["has_link_change"] for f in file_flags)
    has_any_code = any(f["has_code_block_change"] or f["has_shortcode_change"] for f in file_flags)
    has_any_rename_or_delete = any(f["is_rename"] or f["is_delete"] for f in file_flags)
    has_any_new_file = any(f["is_new"] for f in file_flags)
    has_any_binary = any(f["is_binary"] for f in file_flags)

    # Trivial and frontmatter-only short-circuits only apply to docs and blog
    # content. Marketing/legal pages (domain:website) need fact-check rigor
    # on every change regardless of size; programs, scripts, and layouts get
    # full domain reviews. The maintainer-glance assumption only holds for
    # docs/blog prose.
    all_files_docs_or_blog = file_count > 0 and all(
        classify_path(f.get("path", "")) in ("domain:docs", "domain:blog")
        for f in files
    )

    trivial = (
        additions <= 10
        and file_count <= 2
        and all_files_docs_or_blog
        and not has_any_frontmatter
        and not has_any_link
        and not has_any_code
        and not has_any_rename_or_delete
        and not has_any_new_file
        and not has_any_binary
    )

    # Frontmatter-only: any number of docs/blog files, but every file's
    # changes are entirely within the frontmatter block. Mutually exclusive
    # with trivial.
    frontmatter_only = (
        not trivial
        and all_files_docs_or_blog
        and has_any_frontmatter
        and not has_any_body
        and not has_any_rename_or_delete
        and not has_any_new_file
        and not has_any_binary
    )

    return {
        "target_domains": sorted(domains),
        "mixed": len(domains) > 1,
        "trivial": trivial,
        "frontmatter_only": frontmatter_only,
        "oversized": total_lines > OVERSIZED_TOTAL_LINES or file_count > OVERSIZED_TOTAL_FILES,
        "prose_check_needed": trivial or frontmatter_only,
        "summary": {
            "lines": total_lines,
            "files": file_count,
            "frontmatter_changed": has_any_frontmatter,
            "body_changed": has_any_body,
            "rename_or_delete": has_any_rename_or_delete,
        },
    }


# ---- Entry point -----------------------------------------------------------


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: triage-classify.py <pr-data.json>  (diff on stdin)", file=sys.stderr)
        return 2
    with open(sys.argv[1], encoding="utf-8") as fh:
        pr_data = json.load(fh)
    diff_text = sys.stdin.read()
    files = split_files(diff_text)
    file_flags = [classify_file(p, d, repo_root=Path.cwd()) for p, d in files]
    result = classify_pr(pr_data, file_flags)
    json.dump(result, sys.stdout, separators=(",", ":"))
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
