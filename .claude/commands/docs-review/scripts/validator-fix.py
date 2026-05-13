#!/usr/bin/env python3
"""validator-fix.py — deterministic surgical-fix for validator violations.

Reads the fix-me JSON from validate-pinned.py and dispatches Haiku 4.5 via
the Anthropic Messages API to make targeted edits for surgical-fixable rule
classes. Surgical violations are applied even when non-surgical violations
are present (the caller restarts the model retry on the residual fix-me).

Usage:
    validator-fix.py --body-file <path> --fix-me-json <path>

Exit codes:
    0  all surgical violations applied; no non-surgical residual
    1  Haiku API error (auth, transient network, malformed response)
    2  surgical fixes applied OR none to apply, but non-surgical residual
       remains for the model to handle

Design notes:
    Each violation runs as a single Haiku call with a class-specific prompt
    template. The body is passed verbatim in the user message; Haiku echoes
    back the full edited body. We use the Messages API directly (urllib +
    `x-api-key`) — the same path verify-claims.py uses — rather than the
    `claude` CLI subprocess, because (a) the API is the proven auth path in
    CI, (b) errors surface as readable strings instead of being truncated
    inside a 50KB CalledProcessError repr, and (c) it removes the dependency
    on the `claude` CLI being installed at a compatible version.

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
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

# Rule classes this script can splice mechanically. Non-surgical violations
# are noted but don't gate the surgical pass (see main()).
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
    "verified-claims-trail-faithful",
}

# Sonnet 4.6 for the splice model. Pre-v16 used Haiku 4.5 per call, which
# handled single-violation splices fine but lacked the reasoning headroom
# for batched multi-fix prompts — Haiku tracking 30+ independent edit
# targets in one rewrite started dropping fixes. Sonnet costs ~4× per token
# but the per-rule batching (see build_batched_prompt) collapses N sequential
# calls into 1 call per rule_id, so the review-level cost lands ~$0.40 — a
# 6.5× drop vs Haiku-sequential's ~$2.64, with lower fumble risk.
SPLICE_MODEL = "claude-sonnet-4-6"
ANTHROPIC_URL = "https://api.anthropic.com/v1/messages"
ANTHROPIC_VERSION = "2023-06-01"
# 180s per call — Sonnet processes large prompts faster than Haiku but the
# response (full body) is still ~12K output tokens; 180s gives a buffer
# for the larger model + network jitter.
SPLICE_TIMEOUT_S = 180
MAX_RETRIES = 3  # API-level retries on 429 / 5xx / transient network
# Maximum response tokens from Haiku. The whole body is echoed back verbatim;
# 16K covers a 60K-char review body with room for any minor expansion. Goes
# in the messages.create `max_tokens` field.
MAX_OUTPUT_TOKENS = 16000
# Maximum number of surgical violations to fold into a single batched Haiku
# call. Pre-v16 was N sequential calls (each one rewrites the whole ~50KB
# body — ~12K output tokens × ~250 tok/s = ~50s/call); a hot review with 30
# violations cost ~5-10 min wall-clock per upsert-validated retry and tripped
# Opus's 2-min Bash timeout, leaving the model to defer to soft-floor without
# the splices applying. v16 batches all surgical fixes into ONE Haiku call:
# the body is sent + received once, the per-violation instructions stack
# above it. 50 fix instructions add ~25KB to the prompt vs the 50KB body —
# easily within Haiku's 200K context, and Anthropic charges the same tokens
# regardless of whether they were "input prompt" or "input body".
MAX_VIOLATIONS_PER_BATCH = 50


SYSTEM_PROMPT = (
    "You edit a single PR-review body to apply ALL the surgical fixes the "
    "user lists. Output ONLY the full edited body — no explanation, no "
    "preamble, no code fence, no fix summary. Apply every fix in the list; "
    "make the smallest change per fix; do not rewrite or restructure "
    "anything that isn't explicitly targeted by one of the fixes."
)


def build_instruction(rule_id: str, violation: dict) -> str:
    """Return the class-specific instruction block for ONE violation (no body).

    Factored out of the older single-violation `build_prompt` so the same
    per-rule instruction can be reused inside a batched prompt that appends
    the body once at the end.
    """
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
    elif rule_id == "verified-claims-trail-faithful":
        # Schema v15. Restore the trail line's verdict word + emoji to what the
        # `.verified-claims.json` artifact records. The violation strings carry
        # everything we need: `actual` ≈ "trail says `<wrong>`; artifact says
        # `<right>` — evidence: ..." and `hint` ≈ "...Render the trail line
        # for <L-anchor> as `<emoji> <right>` with the artifact's..."
        line_ref = violation.get("line_ref", "")
        wrong_m = re.search(r"trail says `([^`]+)`", actual)
        right_m = re.search(r"artifact says `([^`]+)`", actual)
        emoji_m = None
        if right_m:
            # Parse the right emoji out of the hint's "Render the trail line
            # for <ref> as `<emoji> <right>`" template; the emoji comes
            # immediately before the right word inside the backtick pair.
            emoji_m = re.search(
                r"Render the trail line[^`]*`(\S+)\s+" + re.escape(right_m.group(1)) + r"`",
                hint,
            )
        wrong = wrong_m.group(1) if wrong_m else "<unknown>"
        right = right_m.group(1) if right_m else "<unknown>"
        emoji = emoji_m.group(1) if emoji_m else "?"
        instr = (
            f"VIOLATION (`verified-claims-trail-faithful`): A trail line under "
            f"### 🔍 Verification trail records a verdict word that contradicts "
            f"the verdict recorded in `.verified-claims.json`. The artifact is "
            f"the source of truth for verdicts; the trail can't silently "
            f"overwrite it.\n\n"
            f"Trail line anchor: `{line_ref}`\n"
            f"Currently in the trail: `{wrong}` (wrong)\n"
            f"Recorded in the artifact: `{right}` (right)\n"
            f"Right per-verdict emoji: `{emoji}`\n\n"
            f"Find the trail line under ### 🔍 Verification trail whose L-token "
            f"matches `{line_ref}` (look for `- L<n> ` or `- L<n> in \\`...\\` `). "
            f"After its `→`, replace the two tokens — the per-verdict glyph "
            f"AND the verdict word — with `{emoji} {right}`. Preserve the "
            f"claim text, evidence pointer, and any `(also L<n>, …)` cross-"
            f"reference verbatim. Do not modify any other trail line, any "
            f"bucket bullet, or surrounding sections."
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

    return instr


def build_batched_prompt(violations: list[dict], body: str) -> str:
    """Stack N per-violation instructions above the body, append the body once.

    Used for per-rule batched calls — every violation in the list shares the
    same `rule_id` semantics (hugogeneous fix shape), so the splice model
    just sees a list of independent targeted edits to apply in one rewrite.
    """
    if len(violations) == 1:
        # Special-case to avoid awkward "FIX 1 of 1" framing on tiny batches;
        # the body suffix is the same.
        instr = build_instruction(violations[0]["rule_id"], violations[0])
        return (
            f"{instr}\n\n"
            f"FULL BODY (edit and return verbatim with the fix applied):\n\n"
            f"{body}"
        )
    rule_id = violations[0]["rule_id"]  # all violations share this in per-rule mode
    fix_blocks = []
    for i, v in enumerate(violations, 1):
        block = build_instruction(v["rule_id"], v)
        fix_blocks.append(f"FIX {i} of {len(violations)}:\n{block}")
    header = (
        f"You will apply {len(violations)} independent surgical fixes for the "
        f"`{rule_id}` rule to a single PR-review body. Each FIX block below "
        f"targets a different anchor (different L-token, claim, file, or "
        f"section). Apply EVERY fix; the targets do not overlap. After all "
        f"fixes are applied, output the FULL edited body verbatim — no "
        f"explanation, no fix summary, no code fence.\n\n"
    )
    return (
        header +
        "\n\n".join(fix_blocks) +
        f"\n\nFULL BODY (edit and return verbatim with all {len(violations)} fixes applied):\n\n" +
        body
    )


def dispatch_splice(prompt: str, api_key: str) -> str | None:
    """Run one splice call (Sonnet 4.6) via the Anthropic Messages API.
    Returns the edited body or None on error.

    Pre-v16 used the `claude` CLI as a subprocess, which silently failed in
    CI because Opus's Bash tool truncates output at ~2KB — the actual
    `returned non-zero exit status N` error tail got pushed out by the
    huge CalledProcessError repr (which includes the full `-p <prompt>`
    argument). Direct API calls surface errors as plain readable strings
    and use the same auth path verify-claims.py uses (proven to work in CI).

    Splice model: Sonnet 4.6 (see SPLICE_MODEL note). Haiku 4.5 worked
    fine on single-violation prompts but lost fixes when ~30 independent
    edits were batched into one call; Sonnet's reasoning headroom is
    worth the ~4× per-token cost when per-rule batching collapses the
    call count anyway.
    """
    body = {
        "model": SPLICE_MODEL,
        "max_tokens": MAX_OUTPUT_TOKENS,
        "system": SYSTEM_PROMPT,
        "messages": [{"role": "user", "content": prompt}],
    }
    req = urllib.request.Request(
        ANTHROPIC_URL,
        data=json.dumps(body).encode("utf-8"),
        headers={
            "x-api-key": api_key,
            "anthropic-version": ANTHROPIC_VERSION,
            "content-type": "application/json",
        },
        method="POST",
    )
    last_err: Exception | None = None
    for attempt in range(MAX_RETRIES):
        try:
            with urllib.request.urlopen(req, timeout=SPLICE_TIMEOUT_S) as resp:
                payload = json.loads(resp.read().decode("utf-8"))
                break
        except urllib.error.HTTPError as e:
            detail = ""
            try:
                detail = e.read().decode("utf-8", errors="replace")[:300]
            except Exception:  # noqa: BLE001
                pass
            if e.code in (429, 500, 502, 503, 529) and attempt < MAX_RETRIES - 1:
                last_err = RuntimeError(f"HTTP {e.code}: {detail}")
                time.sleep(2 ** attempt + 0.5)
                continue
            print(
                f"validator-fix.py: splice API error: HTTP {e.code}: {detail}",
                file=sys.stderr,
            )
            return None
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            if attempt < MAX_RETRIES - 1:
                last_err = e
                time.sleep(2 ** attempt + 0.5)
                continue
            print(f"validator-fix.py: splice API error: {type(e).__name__}: {e}",
                  file=sys.stderr)
            return None
    else:
        print(f"validator-fix.py: splice API gave up after {MAX_RETRIES} retries: {last_err}",
              file=sys.stderr)
        return None

    # Successful 2xx → extract the assistant text content. The response shape:
    #   {"content": [{"type":"text","text":"<edited body>"}, ...], ...}
    content = payload.get("content") or []
    text_parts = [c.get("text", "") for c in content if isinstance(c, dict) and c.get("type") == "text"]
    output = "".join(text_parts).strip()
    if not output:
        print(
            f"validator-fix.py: splice model returned empty content "
            f"(stop_reason={payload.get('stop_reason')!r})",
            file=sys.stderr,
        )
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

    api_key = os.environ.get("ANTHROPIC_API_KEY", "").strip()
    if not api_key:
        print(
            "validator-fix.py: ANTHROPIC_API_KEY is unset; cannot dispatch "
            "Haiku — deferring to soft-floor",
            file=sys.stderr,
        )
        return 2

    fix_data = json.loads(fix_path.read_text())
    violations = fix_data.get("violations", [])
    if not violations:
        return 0  # nothing to fix

    # Partition: surgical fixes apply here, non-surgical are noted and left
    # for the model's retry. Pre-v15 this was an all-or-nothing gate (any
    # non-surgical → defer everything), which meant a single mandatory-h3
    # or trail-faithful violation blocked every other surgical fix on the
    # body. The new behaviour preserves the all-or-nothing exit signal
    # (2 = caller should re-render) but applies the surgical class anyway,
    # so a hot review with mixed violations still gets ~80% of its
    # validator load shed before the model's retry kicks in.
    surgical = [v for v in violations if v["rule_id"] in SURGICAL_CLASSES]
    non_surgical = [v["rule_id"] for v in violations
                    if v["rule_id"] not in SURGICAL_CLASSES]
    if non_surgical:
        print(
            f"validator-fix.py: {len(non_surgical)} non-surgical violation(s) "
            f"({', '.join(sorted(set(non_surgical)))}) will need a model retry; "
            f"applying {len(surgical)} surgical fix(es) first",
            file=sys.stderr,
        )
    if not surgical:
        return 2  # all violations are non-surgical → caller re-renders
    violations = surgical

    if len(violations) > MAX_VIOLATIONS_PER_BATCH:
        print(
            f"validator-fix.py: {len(violations)} surgical violations exceeds "
            f"cap of {MAX_VIOLATIONS_PER_BATCH}; deferring to soft-floor",
            file=sys.stderr,
        )
        return 2

    # Group surgical violations by rule_id and run one batched splice per
    # rule. Schema v16: each rule_id's violations are homogeneous edits
    # (same shape; different anchors), so one Sonnet call per rule handles
    # them all in a single body rewrite. Wall-clock: ~30-60s × number-of-
    # distinct-rule-ids per review, vs the pre-v16 N sequential calls.
    by_rule: dict[str, list[dict]] = {}
    for v in violations:
        by_rule.setdefault(v["rule_id"], []).append(v)
    rule_order = sorted(by_rule.keys())  # deterministic order

    body = body_path.read_text()
    for rule_id in rule_order:
        rule_violations = by_rule[rule_id]
        prompt = build_batched_prompt(rule_violations, body)
        edited = dispatch_splice(prompt, api_key)
        if edited is None:
            print(
                f"validator-fix.py: splice dispatch failed for rule "
                f"`{rule_id}` ({len(rule_violations)} violation(s))",
                file=sys.stderr,
            )
            return 1
        body = edited
        print(
            f"validator-fix.py: spliced {len(rule_violations)} `{rule_id}` "
            f"violation(s) in one batched call",
            file=sys.stderr,
        )

    body_path.write_text(body)
    summary = (
        f"applied {len(violations)} surgical fix(es) across "
        f"{len(rule_order)} batched call(s)"
    )
    if non_surgical:
        print(
            f"validator-fix.py: {summary}; {len(non_surgical)} non-surgical "
            f"violation(s) remain — caller should re-render",
            file=sys.stderr,
        )
        return 2  # partial fix; caller should re-validate + model retry
    print(f"validator-fix.py: {summary}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
