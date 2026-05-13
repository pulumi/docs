#!/usr/bin/env python3
"""validator-fix.py — deterministic surgical-fix for validator violations.

Reads the fix-me JSON from validate-pinned.py and dispatches Haiku 4.5 via
the claude CLI to make targeted edits for surgical-fixable rule classes.
On any non-surgical violation, exits 2 (caller falls through to soft-floor
without invoking Haiku, since the violation needs a re-render decision).

Usage:
    validator-fix.py --body-file <path> --fix-me-json <path>

Exit codes:
    0  all violations attempted; body file rewritten in place
    1  Haiku dispatch error (e.g., claude CLI unavailable, edit produced no output)
    2  one or more violations fall outside the surgical-fixable set

Design notes:
    Each violation runs as a single Haiku call with a class-specific prompt
    template. Tool use is disabled — we want a pure text edit, not an agent
    that might wander off and run shell or read files. The body is passed
    verbatim in the prompt; Haiku echoes back the full edited body.

    The caller (pinned-comment.sh cmd_upsert_validated) is expected to:
    1. snapshot the pre-fix body to a .pre-haiku.bak file
    2. invoke this script
    3. re-validate after success
    4. on persistent failure, restore from backup and fall through to
       soft-floor — the soft-floor publishes the original body, not a
       Haiku-degraded one
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

# Rule classes this script handles. Anything else → exit 2.
SURGICAL_CLASSES: set[str] = {
    "internal-link-existence",
    "shortcode-existence",
    "external-claim-state-format",
    "external-claim-dispatch-metadata",
    "external-claim-routed-metadata",
    "external-claim-pass2-outcome",
    "bucket-bullet-line-range-prefix",
    "mandatory-h3-order",
    "trail-per-verdict-emoji",
    "trail-canonical-verdict-word",
    "pass-3-unverifiable-evidence",
}

HAIKU_MODEL = "claude-haiku-4-5-20251001"
# 60s is plenty for --bare mode (~2-3s CLI startup, sub-10s Haiku call). OAuth
# mode adds ~30s of CLI startup so 60s leaves Haiku very little headroom; bump
# to 120s when ANTHROPIC_API_KEY is unset (local-test path) to avoid spurious
# timeouts during corpus runs.
HAIKU_TIMEOUT_S = 60 if os.environ.get("ANTHROPIC_API_KEY") else 120
# Sequential dispatches; each rewrites the whole body. Cap accounts for the
# pass-3 surgical-per-line emission landed in schema v13 (one violation per
# Pass 3 unverifiable verdict missing its pointer; a hot review can run 5-8).
MAX_DISPATCHES_PER_CALL = 10  # cost / wall-clock ceiling


SYSTEM_PROMPT = (
    "You edit a single PR-review body to fix one specific validator "
    "violation. Output ONLY the full edited body — no explanation, no "
    "preamble, no code fence. Make the smallest change that resolves "
    "the violation; do not rewrite or restructure anything else."
)


def build_prompt(rule_id: str, violation: dict, body: str) -> str:
    """Return a class-specific user prompt for one violation."""
    expected = violation.get("expected", "")
    actual = violation.get("actual", "")
    hint = violation.get("hint", "")

    if rule_id == "internal-link-existence":
        # `expected` is "link <href> resolves to a file or alias under content/".
        m = re.search(r"link (\S+) resolves", expected)
        broken = m.group(1) if m else "(unknown)"
        instr = (
            f"VIOLATION (`internal-link-existence`): The body contains a "
            f"markdown link whose target path does not resolve.\n\n"
            f"Broken target path: `{broken}`\n\n"
            f"Find the markdown link `[some text]({broken})` (or with "
            f"trailing slash variants) in the body. Remove the link "
            f"markdown wrapper, leaving the link text bare. If the same "
            f"path appears as a code-formatted reference inside narrative "
            f"prose, leave it alone — only edit the markdown-link form. "
            f"If you cannot find an actual `[...](...)` link with this "
            f"target, output the body unchanged."
        )
    elif rule_id == "shortcode-existence":
        # Hint typically names the shortcode.
        instr = (
            f"VIOLATION (`shortcode-existence`): The body uses a Hugo "
            f"shortcode that has no corresponding layout file.\n\n"
            f"{actual}\n\nValidator hint: {hint}\n\n"
            f"Find the offending `{{{{< NAME >}}}}` shortcode usage in the "
            f"body and remove the entire line that contains it. Do not "
            f"edit any other shortcodes."
        )
    elif rule_id == "trail-per-verdict-emoji":
        # `expected` ≈ "trail line for L<n> renders `<want>` for verdict `<word>`";
        # `actual` ≈ "renders `<legacy emoji>` (legacy bucket emoji)".
        instr = (
            f"VIOLATION (`trail-per-verdict-emoji`): A line in the 🔍 Verification "
            f"trail renders a legacy bucket emoji instead of the per-verdict glyph.\n\n"
            f"Expected: {expected}\n"
            f"Actual: {actual}\n"
            f"Validator hint: {hint}\n\n"
            f"In the 🔍 Verification trail, find the bullet for the cited line "
            f"reference whose verdict word matches the one named in `Expected` above. "
            f"Replace ONLY its emoji (the glyph immediately after the `→`) with the "
            f"glyph named in `Expected`. The per-verdict map is: ✅ `verified`, "
            f"🤝 `matches`, ➖ `not-a-claim`, 🤷 `unverifiable`, ❌ `contradicted`, "
            f"⚔️ `mismatch`. Do not change the verdict word, the line text, the "
            f"evidence pointer, or any other line."
        )
    elif rule_id == "trail-canonical-verdict-word":
        # `line_ref` is the trail line's L<n> anchor; `actual` names the bad
        # token + the rendered emoji; `hint` names the canonical word to use
        # (when the emoji maps to one of the six).
        line_ref = violation.get("line_ref", "")
        instr = (
            f"VIOLATION (`trail-canonical-verdict-word`): A line in the 🔍 Verification "
            f"trail uses a freelanced verdict token instead of one of the six canonical "
            f"verdict words.\n\n"
            f"Trail line anchor: `{line_ref}`\n"
            f"Actual: {actual}\n"
            f"Validator hint: {hint}\n\n"
            f"In the `### 🔍 Verification trail` section, find the bullet whose line "
            f"reference is `{line_ref}`. It reads like `- {line_ref} \"...\" → <emoji> "
            f"<bad-token> (...)`. Replace ONLY the `<bad-token>` (the word(s) "
            f"immediately after the `→ <emoji>`, before any parenthetical) with the "
            f"canonical verdict word the validator hint names. If the hint does not name "
            f"a specific word, pick the one of `verified` / `matches` / `not-a-claim` / "
            f"`unverifiable` / `contradicted` / `mismatch` that best matches the line's "
            f"evidence text, and set the emoji to its glyph (✅ `verified`, 🤝 `matches`, "
            f"➖ `not-a-claim`, 🤷 `unverifiable`, ❌ `contradicted`, ⚔️ `mismatch`). Keep "
            f"the claim quote, the parenthetical evidence pointer, and every other line "
            f"unchanged."
        )
    elif rule_id == "bucket-bullet-line-range-prefix":
        # Validator hint cites the prefix and which bullet.
        instr = (
            f"VIOLATION (`bucket-bullet-line-range-prefix`): A bullet in "
            f"the 🚨 Outstanding, ⚠️ Low-confidence, or 💡 Pre-existing "
            f"section is missing its bracketed line-range prefix.\n\n"
            f"Expected: bullet starts with `- **[L<start>-<end>]**` (or "
            f"`- **[L<line>]**` for a single line)\n"
            f"Actual: {actual}\n"
            f"Validator hint: {hint}\n\n"
            f"Find the bullet whose actual content matches the snippet "
            f"shown in `Actual` above. Look up the corresponding record "
            f"in `### 🔍 Verification trail` -- the trail record's anchor "
            f"is the EXACT prefix to use (e.g., trail says `L40` → use "
            f"`**[L40]**`; trail says `L83-87` → use `**[L83-87]**`). The "
            f"bracket-then-bold shape is mandatory; do NOT invent a "
            f"single-line range like `[L40-40]`. If the trail anchor is "
            f"`L40`, the bullet prefix is `**[L40]**`, not `**[L40-40]**`.\n\n"
            f"Prepend the prefix to the offending bullet. If the bullet "
            f"already has a non-bracketed bold prefix like `**L40**` or "
            f"`**Outstanding**`, replace just that with the bracketed "
            f"trail anchor; preserve the rest of the bullet text. Do not "
            f"edit any other bullets."
        )
    elif rule_id == "external-claim-state-format":
        # The leading `X of Y claims verified (...)` state form drifted.
        instr = (
            f"VIOLATION (`external-claim-state-format`): The External "
            f"claim verification investigation-log bullet's leading state "
            f"form is non-canonical.\n\n"
            f"Expected: {expected}\nActual: {actual}\nValidator hint: {hint}\n\n"
            f"Find the bullet starting with `- **External claim verification**` "
            f"in the Investigation log <details> block. Rewrite ONLY the "
            f"state portion (the text immediately after the bold label) so "
            f"it begins with `X of Y claims verified (N unverifiable, M "
            f"contradicted)` -- substitute integers based on the verdicts "
            f"in the `### 🔍 Verification trail` section: Y = total claim "
            f"count, X = number of ✅ verified, N = number of ⚠️ unverifiable, "
            f"M = number of 🚨 contradicted. Preserve the rest of the bullet "
            f"(the `· N specialists (...)` and `· routed: ...` segments) "
            f"verbatim. If the bullet currently says `not run (...)`, leave "
            f"it alone.\n\n"
            f"Do not edit anything else."
        )
    elif rule_id == "external-claim-dispatch-metadata":
        # Append `· N specialists (...); K cross-specialist corroborations`.
        instr = (
            f"VIOLATION (`external-claim-dispatch-metadata`): The External "
            f"claim verification investigation-log line is missing the "
            f"extraction-specialists segment.\n\n"
            f"Expected: {expected}\nActual: {actual}\nValidator hint: {hint}\n\n"
            f"Append `· 4 specialists (numerical, cross-reference, "
            f"capability, framing); K cross-specialist corroborations` to "
            f"the bullet, where K = the number of trail records whose "
            f"`found_by` field lists more than one specialist (cross-"
            f"specialist corroboration). If the trail does not record "
            f"`found_by`, default K to 0.\n\n"
            f"Insert the segment after the leading `X of Y claims verified "
            f"(N unverifiable, M contradicted)` state form, separated by ` · `. "
            f"Preserve the `routed: ...` segment that follows verbatim.\n\n"
            f"Do not edit anything else."
        )
    elif rule_id == "external-claim-routed-metadata":
        # Append `· routed: I inline, P Pass 1, F Pass 2[, S Pass 3]` plus
        # any required V/C/U attribution for non-zero external lanes.
        instr = (
            f"VIOLATION (`external-claim-routed-metadata`): The External "
            f"claim verification investigation-log line is missing the "
            f"routed-verification segment.\n\n"
            f"Expected: {expected}\nActual: {actual}\nValidator hint: {hint}\n\n"
            f"The bullet currently ends after the dispatch-metadata "
            f"segment (the part reading `...K cross-specialist "
            f"corroborations`). Your job is to APPEND a new segment to "
            f"the END of that line. Do NOT replace any existing text. "
            f"Specifically:\n\n"
            f"  1. Locate the bullet starting with `- **External claim "
            f"     verification`.\n"
            f"  2. Find the dispatch-metadata segment ending in "
            f"     `cross-specialist corroborations`. Preserve it verbatim.\n"
            f"  3. Append ` · routed: I inline, P Pass 1, F Pass 2, "
            f"     S Pass 3` AFTER that segment, before any final period.\n\n"
            f"Integer values for the routing counts:\n"
            f"  I = inline (`pulumi-internal` source class; resolved "
            f"      during combine step via gh / Read / Grep)\n"
            f"  P = Pass 1 (`ambiguous`; cheap-source subagent fan-out)\n"
            f"  F = Pass 2 (URL fetch from `.fetched-urls.json`)\n"
            f"  S = Pass 3 (search-then-fetch via WebSearch + WebFetch)\n\n"
            f"I + P + F + S must equal Y (the claim count from the leading "
            f"state form).\n\n"
            f"**Important:** if F > 0, immediately append "
            f"`(verified V, contradicted C, unverifiable U)` after "
            f"`F Pass 2` where V + C + U = F. Same for S Pass 3 -- if "
            f"S > 0, append the same outcome parenthetical. Compute V/C/U "
            f"for each external lane by counting trail entries that close "
            f"as ✅ (verified), 🚨 (contradicted), or ⚠️ (unverifiable). If "
            f"the trail does not record per-claim routing, default to "
            f"placing all external claims in Pass 2 (F = number of "
            f"external claims; S = 0; the S Pass 3 segment then has no "
            f"V/C/U parenthetical).\n\n"
            f"Do not edit anything else, especially the dispatch-metadata "
            f"segment containing `K cross-specialist corroborations`."
        )
    elif rule_id == "external-claim-pass2-outcome":
        # The Pass 2 segment of the External claim verification log line
        # needs `(verified V, contradicted C, unverifiable U)` appended.
        instr = (
            f"VIOLATION (`external-claim-pass2-outcome`): The External "
            f"claim verification investigation-log line is missing the "
            f"Pass 2 outcome parenthetical.\n\n"
            f"Expected: {expected}\nActual: {actual}\nValidator hint: {hint}\n\n"
            f"Look at the `### 🔍 Verification trail` section. For each "
            f"claim that was routed to Pass 2 (typically `external-public` "
            f"sources, web-verified), count outcomes: V = number of ✅ "
            f"verified, C = number of 🚨 contradicted, U = number of ⚠️ "
            f"unverifiable. V + C + U must equal F (the Pass 2 count "
            f"already shown on the line as `<F> Pass 2`).\n\n"
            f"Append `(verified V, contradicted C, unverifiable U)` to "
            f"the Pass 2 segment of the External claim verification "
            f"investigation-log line, substituting the integers you "
            f"counted. The line should read like:\n\n"
            f"  routed: I inline, P Pass 1, F Pass 2 (verified V, "
            f"contradicted C, unverifiable U).\n\n"
            f"Do not edit anything else."
        )
    elif rule_id == "pass-3-unverifiable-evidence":
        # Schema v13. The validator's per-line emission carries an L-token
        # anchor, a claim-text snippet, and the exact pointer phrase to splice
        # in (all in `hint`). Haiku just executes the splice.
        line_ref = violation.get("line_ref", "")
        instr = (
            f"VIOLATION (`pass-3-unverifiable-evidence`): A trail line under "
            f"### 🔍 Verification trail is for a Pass 3 ⚠️/🤷 unverifiable "
            f"verdict but is missing the search-was-run negative-evidence "
            f"pointer the composer rendered from `.verified-claims.json`.\n\n"
            f"Trail line anchor: `{line_ref}`\n"
            f"Actual (the offending line): {actual}\n"
            f"Validator hint: {hint}\n\n"
            f"Follow the hint exactly: locate the single trail line it "
            f"identifies (by L-token + claim-text prefix), insert the "
            f"specified `; <pointer phrase>` immediately before the closing "
            f"`)` of the line's parenthetical, and preserve the rest of the "
            f"parenthetical verbatim. Do not modify any other trail line, "
            f"the verdict word, the emoji, the count table, or surrounding "
            f"sections."
        )
    elif rule_id == "mandatory-h3-order":
        # Re-order H3s OR insert missing _explicit empty form_ block.
        instr = (
            f"VIOLATION (`mandatory-h3-order`): The mandatory H3 sections "
            f"are out of order or one is missing.\n\n"
            f"Expected: {expected}\nActual: {actual}\nValidator hint: {hint}\n\n"
            f"Required H3 order: `### 🔍 Verification trail` → "
            f"`### 🚨 Outstanding` → `### ⚠️ Low-confidence` → "
            f"`### 📜 Review history`. (The conditional sections "
            f"`### 📊 Editorial balance` and `### 💡 Pre-existing issues "
            f"in touched files (optional)` may also appear at their "
            f"documented positions.)\n\n"
            f"Either reorder existing H3 sections to match, or insert a "
            f"missing one in its `_explicit empty form_` (an italicized "
            f"one-liner like `_No findings._`). Preserve all other content "
            f"and ordering."
        )
    else:
        # Defensive — caller already filtered by SURGICAL_CLASSES.
        instr = f"Unrecognized surgical rule: {rule_id}"

    return f"{instr}\n\nFULL BODY (edit and return verbatim with the fix applied):\n\n{body}"


def dispatch_haiku(prompt: str) -> str | None:
    """Run one Haiku call via the claude CLI. Returns the edited body or None on error."""
    # --bare skips hooks, LSP, plugin sync, CLAUDE.md auto-discovery, and
    # keychain reads — drops startup from ~30s to ~2-3s per dispatch. It
    # requires ANTHROPIC_API_KEY explicitly. CI has it via the action env;
    # local testing without the API key falls through to OAuth (~30s per
    # dispatch). The implicit fallback keeps the script runnable in both
    # environments without any operator config.
    cmd = [
        "claude",
        "-p", prompt,
        "--model", HAIKU_MODEL,
        "--append-system-prompt", SYSTEM_PROMPT,
        "--allowedTools", "",
    ]
    if os.environ.get("ANTHROPIC_API_KEY"):
        cmd.append("--bare")
    try:
        result = subprocess.run(
            cmd,
            capture_output=True, text=True,
            timeout=HAIKU_TIMEOUT_S,
            check=True,
        )
    except (subprocess.SubprocessError, OSError) as e:
        print(f"validator-fix.py: claude CLI error: {e}", file=sys.stderr)
        return None
    output = result.stdout.strip()
    if not output:
        print("validator-fix.py: claude CLI returned empty output", file=sys.stderr)
        return None
    # Defensive: strip code fences if Haiku wrapped the output despite
    # the system prompt's instruction.
    if output.startswith("```"):
        lines = output.splitlines()
        if lines[0].startswith("```") and lines[-1].startswith("```"):
            output = "\n".join(lines[1:-1])
    return output


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--body-file", required=True)
    parser.add_argument("--fix-me-json", required=True)
    args = parser.parse_args()

    body_path = Path(args.body_file)
    if not body_path.is_file():
        print(f"validator-fix.py: body file not found: {body_path}", file=sys.stderr)
        return 1

    fix_path = Path(args.fix_me_json)
    if not fix_path.is_file():
        print(f"validator-fix.py: fix-me JSON not found: {fix_path}", file=sys.stderr)
        return 1

    fix_data = json.loads(fix_path.read_text())
    violations = fix_data.get("violations", [])
    if not violations:
        return 0  # nothing to fix

    # Gate on surgical-class membership BEFORE dispatching anything. If even
    # one violation isn't in our set, the body needs a model re-render
    # decision the caller's soft-floor path handles.
    non_surgical = [v["rule_id"] for v in violations
                    if v["rule_id"] not in SURGICAL_CLASSES]
    if non_surgical:
        print(
            f"validator-fix.py: {len(non_surgical)} non-surgical violation(s) "
            f"present ({', '.join(sorted(set(non_surgical)))}); deferring to "
            f"soft-floor",
            file=sys.stderr,
        )
        return 2

    if len(violations) > MAX_DISPATCHES_PER_CALL:
        print(
            f"validator-fix.py: {len(violations)} violations exceeds cap "
            f"of {MAX_DISPATCHES_PER_CALL}; deferring to soft-floor",
            file=sys.stderr,
        )
        return 2

    body = body_path.read_text()
    for v in violations:
        rule_id = v["rule_id"]
        prompt = build_prompt(rule_id, v, body)
        edited = dispatch_haiku(prompt)
        if edited is None:
            print(f"validator-fix.py: dispatch failed for `{rule_id}`",
                  file=sys.stderr)
            return 1
        body = edited

    body_path.write_text(body)
    print(
        f"validator-fix.py: applied {len(violations)} surgical fix(es)",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
