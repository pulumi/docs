#!/usr/bin/env python3
"""extract-claims.py — Layer A of the claim-extraction pre-step.

A deterministic regex/heuristic floor for "what claims does this PR introduce?".
Walks the PR diff hunks and, for every *added/modified* line, always emits a
candidate-claim record whenever the line matches one of a fixed set of
patterns (numbers + units, version pins, temporal/recency words, source
attributions, URLs/internal links, named-entity/spec claims, capability/
positioning/comparison trigger words).

This is the *guarantee* layer: a regex has no judgment to vary run-to-run, so
the concrete claims (a price, a version pin, a model-size row, an attribution)
can never be silently dropped. Layer B (`extract-claims-llm.py`) adds the
softer, judgment-y pulls; `merge-claims.py` unions all three into
`.candidate-claims.json`. The main review then MUST verify every entry and MAY
add more.

False positives are expected and fine — the reviewer's contract is to triage
each artifact entry (see `references/pre-computation.md` §"False-positive
triage is a contractual responsibility"). Code-fence URLs, snake_case
identifiers in code blocks, etc. will surface; the reviewer demotes them.

Usage:
    extract-claims.py --pr <PR_NUMBER> --out <out.json>
    extract-claims.py --patch-file <file> --out <out.json>   # for testing

Scope:
    - Walks the FULL diff (all changed files, including static/programs/
      go.mod / Pulumi.yaml — that's where `pulumi-gcp v8.2.0`-style pins
      live), not just content/.
    - For non-markdown files (and inside fenced code blocks in markdown),
      emits only `version`, `url`, and `numerical` claims — prose patterns
      (capability words, attributions) don't make sense there.

Output schema:
    {
      "schema_version": 1,
      "claims": [
        {"file": "content/blog/foo.md",
         "line_range": "L42",
         "text": "<the added line, stripped + capped>",
         "type": "numerical" | "version" | "temporal" | "attribution"
                 | "url" | "entity-spec" | "capability" | "positioning"
                 | "comparison",
         "source_hint": "https://...",   # optional — URL / named source
         "confidence": "high"},          # regex hits are high-confidence-this-is-a-claim
        ...
      ],
      "errors": [],
      "stats": {"claims_count": N, "files_scanned": M, "by_type": {...}}
    }

The script calls no APIs except `gh pr diff`. `safe_main()` guarantees a
structured JSON artifact even on an uncaught exception, so the workflow's
`||` fallback is reserved for "can't even start" (ImportError, etc.).
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import traceback
from pathlib import Path

SCHEMA_VERSION = 1
TEXT_CAP = 300  # characters retained per claim's `text`

# ---- Diff parsing ----------------------------------------------------------

DIFF_FILE_RE = re.compile(r"^\+\+\+ b/(.+)$")
HUNK_RE = re.compile(r"^@@ -\d+(?:,\d+)? \+(\d+)(?:,(\d+))? @@")
FENCE_RE = re.compile(r"^\s*(```|~~~)")  # opens/closes a fenced code block
DIFF_GIT_RE = re.compile(r"^diff --git a/(.+?) b/(.+)$")
SIMILARITY_RE = re.compile(r"^similarity index (\d+)%$")
RENAME_FROM_RE = re.compile(r"^rename from (.+)$")
RENAME_TO_RE = re.compile(r"^rename to (.+)$")


def fetch_pr_patch(pr: str) -> str:
    proc = subprocess.run(
        ["gh", "pr", "diff", pr, "--patch"],
        check=True, capture_output=True, text=True,
    )
    return proc.stdout


def parse_renames(patch: str) -> list[dict]:
    """Return `[{from, to, similarity}]` for every `rename` block in the diff.

    Observability hint for `extract-claims-llm.py` (which skips the unchanged
    body of a high-similarity rename) and for whoever is reading the artifact.
    """
    out: list[dict] = []
    cur_sim: int | None = None
    cur_from: str | None = None
    for raw in patch.splitlines():
        if DIFF_GIT_RE.match(raw):
            cur_sim = None
            cur_from = None
            continue
        sm = SIMILARITY_RE.match(raw)
        if sm:
            cur_sim = int(sm.group(1))
            continue
        fm = RENAME_FROM_RE.match(raw)
        if fm:
            cur_from = fm.group(1)
            continue
        tm = RENAME_TO_RE.match(raw)
        if tm and cur_from is not None:
            out.append({"from": cur_from, "to": tm.group(1), "similarity": cur_sim})
            cur_from = None
            continue
    return out


def iter_added_lines(patch: str):
    """Yield (file_path, new_line_number, line_text, in_code_context) for every
    added line in the diff.

    `in_code_context` is True for non-markdown files and for lines inside a
    fenced code block in a markdown file. Fence state is tracked from context
    (` `) and added (`+`) lines only — removed lines describe the old file.
    A hunk that starts mid-fence can't be detected from the diff alone
    (the opener is above the hunk); that edge case is accepted (FP-tolerant).
    """
    current_file: str | None = None
    is_markdown = False
    new_lineno = 0
    in_fence = False
    for raw in patch.splitlines():
        m = DIFF_FILE_RE.match(raw)
        if m:
            current_file = m.group(1)
            is_markdown = current_file.endswith(".md")
            in_fence = False
            continue
        if current_file is None:
            continue
        if raw.startswith("--- "):
            continue
        hm = HUNK_RE.match(raw)
        if hm:
            new_lineno = int(hm.group(1))
            # A new hunk doesn't reset fence state reliably; assume not-in-fence
            # at hunk boundaries (best effort).
            in_fence = False
            continue
        if not raw:
            # Bare empty line in the patch body — treat as a context blank line.
            new_lineno += 1
            continue
        tag, body = raw[0], raw[1:]
        if tag == "-":
            # Removed line: doesn't exist in the new file; don't advance lineno
            # and don't toggle fence (that's old-file state).
            continue
        if tag not in ("+", " "):
            # "\ No newline at end of file" and other meta lines.
            continue
        # Context (" ") or added ("+") line — it's part of the new file.
        # Toggle fence on a ``` / ~~~ delimiter (markdown only).
        if is_markdown and FENCE_RE.match(body):
            in_fence = not in_fence
            new_lineno += 1
            continue
        if tag == "+":
            yield current_file, new_lineno, body, (not is_markdown) or in_fence
        new_lineno += 1


# ---- Claim matchers --------------------------------------------------------
#
# Each matcher is (compiled_regex, claim_type, prose_only). `prose_only`
# matchers are skipped in code context (non-markdown files, fenced blocks).
# A line can match several matchers → several claim records (deduped later
# by merge-claims.py).

_MONTHS = (
    r"January|February|March|April|May|June|July|August|September|October|"
    r"November|December|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec"
)

NUMERICAL_RES = [
    # Money, optionally with a rate suffix: $98.32/hr, $1,000 per engineer, $2.40/M
    re.compile(r"\$\s?\d[\d,]*(?:\.\d+)?\s?(?:[KMB]\b|/\s?\w+|per\s+\w+)?"),
    # Number + unit: 200 MB, 90%, 41x, 32k lines, 93.2 ms, 17.8 GB/s, 2 minor versions
    re.compile(
        r"\b~?\d[\d,]*(?:\.\d+)?\s?"
        r"(?:[KMGT]i?B(?:/s)?|ms|µs|ns|seconds?|minutes?|hours?|days?|weeks?|months?|years?"
        r"|%|×|x\b|fps|qps|rps|requests?/\w+|PRs?/\w+|tokens?/\w+|ops?/\w+"
        r"|lines?\b|files?\b|users?\b|customers?\b|companies\b|countries\b|engineers?\b"
        r"|(?:minor|major|patch)\s+versions?|releases?\b|nodes?\b|replicas?\b|cores?\b|vCPUs?\b)"
    ),
    # Numeric ranges: 200–400 MB, 200 to 300 MB, 9–12 minutes
    re.compile(r"\b\d[\d,]*(?:\.\d+)?\s?(?:-|–|—|to)\s?\d[\d,]*(?:\.\d+)?\s?\w+"),
    # Bare "Nk" magnitudes near a noun: 32k lines, 1k PRs
    re.compile(r"\b\d+k\b"),
    # Multipliers: 2x, 10×, up to 40x
    re.compile(r"\b(?:up to\s+)?\d+(?:\.\d+)?\s?(?:x|×)\b", re.IGNORECASE),
]

VERSION_RES = [
    # pulumi-gcp v8.2.0, pulumi/pulumi v3.236.0, terraform 1.7.x
    re.compile(r"\b[\w.-]*pulumi[\w.-]*\s+v?\d+\.\d+(?:\.\d+)?(?:\.x)?\b", re.IGNORECASE),
    # Docker-image-style tags: pulumi/pulumi-base:3.236.0
    re.compile(r"\b[\w./-]+:\d+\.\d+(?:\.\d+)?\b"),
    # "version 8.2.0", "v8.2.0", "8.2.0" near a version word
    re.compile(r"\b(?:version|release|tag)\s+v?\d+\.\d+(?:\.\d+)?\b", re.IGNORECASE),
    re.compile(r"\bv\d+\.\d+(?:\.\d+)?\b"),
    # Runtime/language version statements: Node.js 18+, Go 1.21, .NET 8, Python 3.12
    re.compile(
        r"\b(?:Node(?:\.js)?|Go|Golang|Python|Java|JDK|\.NET|dotnet|TypeScript|Deno|Bun|Ruby|PHP)"
        r"\s+(?:LTS|v?\d+(?:\.\d+)?\+?)\b",
        re.IGNORECASE,
    ),
    # "requires Foo 18 or higher", "available in v3.230+", "since v3.0"
    re.compile(r"\b(?:available in|requires|supported (?:in|since)|since|added in)\s+v?\d+(?:\.\d+)?\+?\b", re.IGNORECASE),
]

TEMPORAL_RES = [
    re.compile(r"\b(?:recently|newly|now supports?|just (?:launched|released|shipped|added)|latest|brand[- ]new)\b", re.IGNORECASE),
    re.compile(r"\bnew(?:ly)?\b", re.IGNORECASE),
    re.compile(r"\b(?:introduced|launched|released|shipped|deprecated|retiring|retired|sunset(?:ting)?|end[- ]of[- ]life|EOL)\b", re.IGNORECASE),
    re.compile(rf"\bas of\s+(?:{_MONTHS})?\.?\s*\d{{4}}", re.IGNORECASE),
    re.compile(rf"\b(?:in|by|until|through|since)\s+(?:{_MONTHS})\.?\s+\d{{4}}", re.IGNORECASE),
]

ATTRIBUTION_RES = [
    # "X reported", "X said", "X writes" — capitalized subject + reporting verb (most specific; try first)
    re.compile(r"\b[A-Z][\w'’.-]+(?:\s+[A-Z][\w'’.-]+)?\s+(?:reported(?:ly)?|said|states?|stated|wrote|writes?|notes?|noted|argues?|argued|claims?|claimed|found|estimates?|estimated|projects?|projected|quotes?|quoted|describes?|described|announced|confirmed)\b"),
    # possessive source: "Willison's piece", "BCG's report", "StrongDM's pattern", "Pulumi's docs"
    re.compile(r"\b[A-Z][\w'’.-]+(?:’s|'s)\s+(?:piece|post|article|report|blog|README|docs?|documentation|announcement|study|survey|paper|analysis|manifesto|essay|writeup|guide|benchmark|pattern|approach|method|methodology|process|workflow|pipeline|implementation|setup|design|playbook|recipe|technique|framework)\b"),
    # "according to X"
    re.compile(r"\baccording to\b", re.IGNORECASE),
    # "per the README", "per Willison's piece" — require "the <noun>" or a capitalized name (avoid "per day")
    re.compile(r"\bper\s+(?:the\s+[A-Za-z][\w-]+|[A-Z][\w'’.-]+)", ),
    # "the README says", "the docs state", "the changelog notes"
    re.compile(r"\bthe\s+(?:README|docs?|documentation|changelog|release notes?|blog post|announcement|spec(?:ification)?|RFC|paper)\b", re.IGNORECASE),
    # bare reporting adverbs that imply an external subject
    re.compile(r"\b(?:reportedly|allegedly|supposedly)\b", re.IGNORECASE),
]

# Markdown link to ANY target (internal or external) + bare URLs + bare
# internal paths.
URL_RES = [
    re.compile(r"\[[^\]]*\]\((https?://[^)\s]+|/[^)\s]+)\)"),
    re.compile(r"https?://[\w\-._~:/?#\[\]@!$&'*+,;=%()]+"),
    re.compile(r"(?<![\w/])/(?:docs|blog|tutorials|registry|product|learn|what-is)/[\w\-./#?=&%]+"),
]

ENTITY_SPEC_RES = [
    # LLM name + parameter size: "Llama 3.3 32B", "DeepSeek-R1 32B distill", "Mistral 7B"
    re.compile(
        r"\b(?:Llama|Mistral|Mixtral|Qwen|DeepSeek|GPT-?\d?|Claude|Gemini|Gemma|Phi|Falcon|Yi|Command[- ]?R|Grok|Nemotron|StarCoder|CodeLlama)"
        r"[\s.-]*[\d.]*[\s.-]*\d+\s?[Bb]\b",
        re.IGNORECASE,
    ),
    # Bare parameter-size token near a model context: "32B model", "70B variant"
    re.compile(r"\b\d+\s?B\b(?=\s+(?:model|variant|parameter|distill|version|checkpoint))"),
    # snake_case identifier in backticks (resource property / permission scope)
    re.compile(r"`[a-z][a-z0-9]*(?:_[a-z0-9]+)+`"),
    # scoped permission/identifier: auth_policies:update, billing:read
    re.compile(r"\b[a-z][a-z0-9_]*:[a-z][a-z0-9_]+\b"),
    # Cloud region codes: us-west-2, eu-central-1, ap-southeast-2
    re.compile(r"\b(?:us|eu|ap|sa|ca|me|af|cn)-(?:east|west|north|south|central|northeast|northwest|southeast|southwest)-?\d?\b"),
    # "hosted in", "runs in", "deployed in" + something
    re.compile(r"\b(?:hosted|runs?|running|deployed|located|provisioned)\s+in\b", re.IGNORECASE),
]

CAPABILITY_RES = [
    re.compile(r"\b(?:not\s+(?:implemented|supported|available|yet supported)|no longer\s+(?:supported|maintained|available)|unsupported|deprecated)\b", re.IGNORECASE),
    re.compile(r"\b(?:actively maintained|production[- ]ready|generally available|in (?:general availability|public preview|private preview|beta)|GA\b)\b", re.IGNORECASE),
    re.compile(r"\bsufficient on its own\b", re.IGNORECASE),
    re.compile(r"\bkitchen[- ]sink\b", re.IGNORECASE),
]

POSITIONING_RES = [
    re.compile(r"\bthe\s+(?:only|first|canonical|primary|recommended|default|standard|de[- ]facto|leading|preferred)\b", re.IGNORECASE),
    re.compile(r"\b(?:industry[- ]standard|best[- ]in[- ]class|widely adopted|the go[- ]to|the gold standard|battle[- ]tested|enterprise[- ]grade|world[- ]class|cutting[- ]edge|next[- ]generation|state[- ]of[- ]the[- ]art|revolutionary|seamlessly integrates?|blazing[- ]fast)\b", re.IGNORECASE),
    re.compile(r"\b(?:fastest|slowest|cheapest|easiest|simplest|most popular|most widely used|largest|smallest)\b", re.IGNORECASE),
]

COMPARISON_RES = [
    re.compile(r"\bunlike\s+[A-Z][\w.-]+", ),
    re.compile(r"\b(?:faster|slower|cheaper|simpler|easier|better|worse|more (?:performant|reliable|scalable)|less (?:performant|reliable))\s+than\b", re.IGNORECASE),
    re.compile(r"\b(?:outperforms?|beats?|surpasses?|compared (?:to|with))\b", re.IGNORECASE),
    re.compile(r"\bup to\s+\d+(?:\.\d+)?\s?(?:x|×|times|%)\b", re.IGNORECASE),
]

# (regexes, claim_type, prose_only)
MATCHERS: list[tuple[list[re.Pattern], str, bool]] = [
    (NUMERICAL_RES, "numerical", False),
    (VERSION_RES, "version", False),
    (URL_RES, "url", False),
    (TEMPORAL_RES, "temporal", True),
    (ATTRIBUTION_RES, "attribution", True),
    (ENTITY_SPEC_RES, "entity-spec", True),
    (CAPABILITY_RES, "capability", True),
    (POSITIONING_RES, "positioning", True),
    (COMPARISON_RES, "comparison", True),
]

# Lines that are pure diff/markdown structure, never claims on their own.
SKIP_LINE_RE = re.compile(
    r"^\s*$"                       # blank
    r"|^\s*[-=*_]{3,}\s*$"         # hr / setext underline
    r"|^\s*\|[\s:|-]+\|\s*$"       # markdown table separator row
    r"|^\s*---\s*$"                # frontmatter delimiter
    r"|^\s*```|^\s*~~~"            # fence delimiter (also handled in iter)
)


def _source_hint(claim_type: str, match_text: str) -> str | None:
    if claim_type == "url":
        # Pull the URL out of a markdown link if that's what matched.
        m = re.search(r"\((https?://[^)\s]+|/[^)\s]+)\)", match_text)
        if m:
            return m.group(1)
        m = re.search(r"https?://[^\s)]+", match_text)
        if m:
            return m.group(0).rstrip(".,;)")
        m = re.search(r"/[\w\-./#?=&%]+", match_text)
        return m.group(0) if m else None
    if claim_type == "attribution":
        # Best-effort: the capitalized run preceding the reporting verb, or the
        # token after "per"/"according to".
        m = re.search(r"((?:[A-Z][\w'’.-]+\s?){1,3})(?:’s|'s|\s+(?:reported|said|states?|wrote|writes?|notes?|argues?|claims?|found|quotes?))", match_text)
        if m:
            return m.group(1).strip()
        m = re.search(r"\b(?:per|according to)\s+(?:the\s+)?([\w'’.-]+(?:\s+[\w'’.-]+){0,2})", match_text, re.IGNORECASE)
        return m.group(1).strip() if m else None
    return None


def extract_claims_from_patch(patch: str) -> tuple[list[dict], dict]:
    claims: list[dict] = []
    seen: set[tuple] = set()  # (file, lineno, type, matched-token) — intra-file de-dup
    files_scanned: set[str] = set()
    for file_path, lineno, body, in_code in iter_added_lines(patch):
        files_scanned.add(file_path)
        if SKIP_LINE_RE.match(body):
            continue
        text = body.strip()[:TEXT_CAP]
        if not text:
            continue
        for regexes, claim_type, prose_only in MATCHERS:
            if prose_only and in_code:
                continue
            matched_token = None
            for rx in regexes:
                m = rx.search(body)
                if m:
                    matched_token = m.group(0).strip()
                    break
            if matched_token is None:
                continue
            key = (file_path, lineno, claim_type, matched_token.lower())
            if key in seen:
                continue
            seen.add(key)
            record = {
                "file": file_path,
                "line_range": f"L{lineno}",
                "text": text,
                "type": claim_type,
                "confidence": "high",
            }
            hint = _source_hint(claim_type, matched_token)
            if hint:
                record["source_hint"] = hint
            claims.append(record)
    by_type: dict[str, int] = {}
    for c in claims:
        by_type[c["type"]] = by_type.get(c["type"], 0) + 1
    stats = {
        "claims_count": len(claims),
        "files_scanned": len(files_scanned),
        "by_type": by_type,
    }
    return claims, stats


# ---- Driver ----------------------------------------------------------------


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--pr", help="PR number (for `gh pr diff`)")
    p.add_argument("--patch-file", help="Read the unified diff from a file instead of `gh` (testing)")
    p.add_argument("--out", required=True, help="Output JSON path")
    args = p.parse_args()

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    if args.patch_file:
        patch = Path(args.patch_file).read_text(errors="replace")
    elif args.pr:
        try:
            patch = fetch_pr_patch(args.pr)
        except subprocess.SubprocessError as e:
            payload = {
                "schema_version": SCHEMA_VERSION,
                "claims": [],
                "errors": [f"extract-claims: gh pr diff failed: {e}"],
                "stats": {"claims_count": 0, "files_scanned": 0, "by_type": {}},
            }
            out_path.write_text(json.dumps(payload, indent=2) + "\n")
            print(f"extract-claims: gh pr diff failed: {e}", file=sys.stderr)
            return 0
    else:
        p.error("one of --pr or --patch-file is required")
        return 2  # unreachable

    claims, stats = extract_claims_from_patch(patch)
    renames = parse_renames(patch)
    payload = {
        "schema_version": SCHEMA_VERSION,
        "claims": claims,
        "renames": renames,
        "errors": [],
        "stats": stats,
    }
    out_path.write_text(json.dumps(payload, indent=2) + "\n")
    print(
        f"extract-claims: {stats['claims_count']} candidate claim(s) "
        f"across {stats['files_scanned']} file(s); {len(renames)} rename(s) → {out_path}",
        file=sys.stderr,
    )
    return 0


def safe_main() -> int:
    """Never crash. Always emit a structured JSON artifact, even on an
    unexpected exception — the workflow's `||` fallback is reserved for
    can't-even-start failures (ImportError, missing python3)."""
    try:
        return main()
    except SystemExit:
        raise
    except BaseException as e:  # noqa: BLE001 — deliberately broad
        out_path = None
        argv = sys.argv
        for i, a in enumerate(argv):
            if a == "--out" and i + 1 < len(argv):
                out_path = Path(argv[i + 1])
                break
            if a.startswith("--out="):
                out_path = Path(a.split("=", 1)[1])
                break
        if out_path is not None:
            payload = {
                "schema_version": SCHEMA_VERSION,
                "claims": [],
                "renames": [],
                "errors": [f"extract-claims uncaught exception: {type(e).__name__}: {e}"],
                "stats": {"claims_count": 0, "files_scanned": 0, "by_type": {}},
            }
            try:
                out_path.parent.mkdir(parents=True, exist_ok=True)
                out_path.write_text(json.dumps(payload, indent=2) + "\n")
            except OSError:
                pass
        traceback.print_exc(file=sys.stderr)
        return 0


if __name__ == "__main__":
    sys.exit(safe_main())
