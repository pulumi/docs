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
    "external-claim-pass2-outcome",
    "bucket-bullet-line-range-prefix",
    "mandatory-h3-order",
}

HAIKU_MODEL = "claude-haiku-4-5-20251001"
HAIKU_TIMEOUT_S = 60
MAX_DISPATCHES_PER_CALL = 5  # cost ceiling — refuse to fix more than this many


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
    elif rule_id == "bucket-bullet-line-range-prefix":
        # Validator hint cites the prefix and which bullet.
        instr = (
            f"VIOLATION (`bucket-bullet-line-range-prefix`): A bullet in "
            f"the 🚨 Outstanding, ⚠️ Low-confidence, or 💡 Pre-existing "
            f"section is missing its `**[L<a>-<b>]**` line-range prefix.\n\n"
            f"Expected: {expected}\nActual: {actual}\nValidator hint: {hint}\n\n"
            f"Find the bullet referenced by the validator hint and prepend "
            f"the `**[L<a>-<b>]**` prefix as instructed. Do not edit any "
            f"other bullets."
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
    # No --bare: --bare requires ANTHROPIC_API_KEY explicitly. CI has the
    # var set via the action; local dev uses OAuth. Either path works
    # without --bare and the startup cost (~1s) is fine for fix dispatches.
    cmd = [
        "claude",
        "-p", prompt,
        "--model", HAIKU_MODEL,
        "--append-system-prompt", SYSTEM_PROMPT,
        "--allowedTools", "",
    ]
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
