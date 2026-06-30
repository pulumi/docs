#!/usr/bin/env python3
"""per-tool-spend.py — parse a Claude Code execution log and emit per-tool counts + approximate $.

Closes the cost-variance observability gap: the workflow log carries
total_cost_usd / num_turns / duration_ms, but no per-tool attribution. This
parser reads the stream-JSON the action saves to
/home/runner/work/_temp/claude-execution-output.json and emits a JSON summary
operators can use to answer "where did the $X go?" — WebFetch retries vs Agent
dispatches vs gh calls vs Read/Grep.

Output is operator-side only, never a public PR comment. The pinned-comment
audience is the PR author / maintainer; cost data is operator-internal.

Operator workflow:
  1. The Claude Code Review workflow uploads the action's stream-JSON
     execution log as a private artifact named `claude-execution-pr<N>-run<R>`.
  2. Download via:
       gh run download <run-id> --repo <owner>/<repo> --name claude-execution-pr<N>-run<R>
  3. Run this parser against the downloaded JSON:
       per-tool-spend.py --execution-log claude-execution-output.json --format markdown

Why operator-side rather than inline in the workflow: the runner checks out the
PR head, which for fixture branches and most synchronize events doesn't carry
this script's path. Keeping the parser as an ad-hoc operator tool avoids the
working-tree dependency. Operators run the latest parser version against any
historical artifact.

Usage:
  per-tool-spend.py --execution-log <path> [--output <path>] [--format json|markdown]

Stream-JSON shape (from anthropic-ai/claude-agent-sdk) — accepted either as
ndjson (one JSON object per line) OR as a single pretty-printed JSON array of
those objects (`[ {...},\n  {...} ]`); newer action versions emit the array
form. Message objects look like:
  {"type": "assistant", "message": {"content": [{"type": "tool_use", "name": "...", "input": {...}}]}}
  {"type": "user", "message": {"content": [{"type": "tool_result", ...}]}}
  {"type": "result", "total_cost_usd": ..., "num_turns": ..., "duration_ms": ...}

Rate card (approximate; calibrated for relative-cost picture, not precise reconciliation):
  Agent dispatch        $0.05 / call (avg across Sonnet 5 + Haiku 4.5 mix)
  WebFetch              $0.02 / call
  WebSearch             $0.01 / call
  Bash (gh)             $0.002 / call
  Bash (other)          $0.002 / call
  Read/Grep/Glob        $0.005 / call (combined)
  Edit/Write            $0.005 / call (combined; render side)

Total estimated $ will not match the workflow's total_cost_usd exactly — the
rate card averages across PR shapes. The relative breakdown across categories
is what's load-bearing for cost-variance analysis.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

RATE_CARD = {
    "Agent": 0.05,
    "WebFetch": 0.02,
    "WebSearch": 0.01,
    "Bash:gh": 0.002,
    "Bash:other": 0.002,
    "Bash:validator-fix": 0.015,  # one Haiku 4.5 dispatch per call (avg, capped at 5/body)
    "Read/Grep/Glob": 0.005,
    "Edit/Write": 0.005,
}

# Categorize Bash commands by their leading token.
# - `gh` calls are GitHub CLI.
# - `validator-fix.py` invocations dispatch Haiku 4.5 via the claude CLI as a
#   subprocess. We can't see the underlying token spend from this layer, so
#   the rate card carries a synthetic per-call cost reflecting the typical
#   Haiku-with-medium-prompt size.
# - Everything else (curl, awk, sed, pinned-comment.sh, validate-pinned.py
#   itself) is "other".
_BASH_GH_RE = re.compile(r"^\s*(?:gh|sudo\s+gh)\b")
_BASH_VALIDATOR_FIX_RE = re.compile(r"validator-fix\.py\b")


def categorize_bash(input_obj: dict) -> str:
    cmd = input_obj.get("command", "") or ""
    if _BASH_GH_RE.match(cmd):
        return "Bash:gh"
    if _BASH_VALIDATOR_FIX_RE.search(cmd):
        return "Bash:validator-fix"
    return "Bash:other"


def _iter_messages(path: Path):
    """Yield message dicts from an execution log that's either a single JSON
    array (`[ {...}, {...} ]`, possibly pretty-printed) or ndjson (one JSON
    object per line). Tries the whole-file parse first; falls back to
    line-by-line on a JSONDecodeError. Non-dict entries are skipped."""
    raw = path.read_text(encoding="utf-8").strip()
    if not raw:
        return
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        data = None
    if data is not None:
        seq = data if isinstance(data, list) else [data]
        for msg in seq:
            if isinstance(msg, dict):
                yield msg
        return
    # ndjson fallback — tolerate trailing commas / bare brackets from a
    # truncated array dump too.
    for line in raw.splitlines():
        line = line.strip().rstrip(",")
        if not line or line in ("[", "]"):
            continue
        try:
            msg = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(msg, dict):
            yield msg


def parse_stream_json(path: Path) -> dict:
    """Parse a stream-JSON execution log and return tool counts + costs.

    Counts every tool_use occurrence in assistant messages. Subagent dispatches
    appear as `Agent` tool calls; the subagent's own tool calls are nested
    inside the dispatch and are NOT counted separately at this layer (the
    action's stream-JSON aggregates subagent work under the parent dispatch).
    If a future action version flattens subagent calls into the parent stream,
    this counter will overcount Agents — adjust here if that drift surfaces.

    Accepts the log as a JSON array or as ndjson (see `_iter_messages`).
    """
    counts: Counter[str] = Counter()
    retries: Counter[str] = Counter()  # tool name -> count of error/retry results
    seen_tool_use_ids: set[str] = set()
    last_tool_per_id: dict[str, str] = {}

    result_meta: dict = {}

    for msg in _iter_messages(path):
        mtype = msg.get("type")

        if mtype == "result":
            # Final result line carries authoritative cost + turn metadata.
            # Keep the LAST occurrence — the action emits one at the end.
            result_meta = {
                "total_cost_usd": msg.get("total_cost_usd"),
                "num_turns": msg.get("num_turns"),
                "duration_ms": msg.get("duration_ms"),
                "is_error": msg.get("is_error", False),
            }

        elif mtype == "assistant":
            content = msg.get("message", {}).get("content", []) or []
            if isinstance(content, str):
                continue
            for item in content:
                if not isinstance(item, dict):
                    continue
                if item.get("type") != "tool_use":
                    continue
                name = item.get("name") or "?"
                tool_id = item.get("id") or ""
                if tool_id and tool_id in seen_tool_use_ids:
                    continue
                if tool_id:
                    seen_tool_use_ids.add(tool_id)

                if name == "Bash":
                    category = categorize_bash(item.get("input", {}) or {})
                elif name in ("Read", "Grep", "Glob"):
                    category = "Read/Grep/Glob"
                elif name in ("Edit", "Write"):
                    category = "Edit/Write"
                else:
                    category = name

                counts[category] += 1
                if tool_id:
                    last_tool_per_id[tool_id] = category

        elif mtype == "user":
            # tool_result with is_error=true counts as a retry indicator
            # (the model presumably re-tried after the error). Track per
            # category for the WebFetch retry signal in particular.
            content = msg.get("message", {}).get("content", []) or []
            if isinstance(content, str):
                continue
            for item in content:
                if not isinstance(item, dict):
                    continue
                if item.get("type") != "tool_result":
                    continue
                if not item.get("is_error"):
                    continue
                tid = item.get("tool_use_id") or ""
                cat = last_tool_per_id.get(tid)
                if cat:
                    retries[cat] += 1

    # Compute approximate $ per category from the rate card.
    costs = {cat: round(counts[cat] * RATE_CARD.get(cat, 0.0), 4)
             for cat in counts}
    estimated_total = round(sum(costs.values()), 4)

    return {
        "result_meta": result_meta,
        "counts": dict(counts),
        "retries": dict(retries),
        "estimated_costs_usd": costs,
        "estimated_total_usd": estimated_total,
        "rate_card": RATE_CARD,
    }


def render_markdown(summary: dict) -> str:
    rm = summary.get("result_meta", {}) or {}
    counts = summary.get("counts", {}) or {}
    retries = summary.get("retries", {}) or {}
    costs = summary.get("estimated_costs_usd", {}) or {}
    total_actual = rm.get("total_cost_usd")
    total_est = summary.get("estimated_total_usd", 0.0)

    parts: list[str] = ["# Per-tool spend", ""]
    if total_actual is not None:
        parts.append(f"- **Workflow total (actual):** ${total_actual:.4f}")
    parts.append(f"- **Estimated total (rate card):** ${total_est:.4f}")
    if rm.get("num_turns") is not None:
        parts.append(f"- **Turns:** {rm['num_turns']}")
    if rm.get("duration_ms") is not None:
        parts.append(f"- **Duration:** {rm['duration_ms'] / 1000:.1f} s")
    parts.append("")
    parts.append("| Tool | Calls | Retries | Est. $ |")
    parts.append("|---|---:|---:|---:|")

    # Sort by est-$ descending so the biggest spenders surface first.
    rows = [(cat, counts[cat], retries.get(cat, 0), costs.get(cat, 0.0))
            for cat in counts]
    rows.sort(key=lambda r: r[3], reverse=True)
    for cat, n, r, c in rows:
        retry_cell = str(r) if r else ""
        parts.append(f"| {cat} | {n} | {retry_cell} | ${c:.4f} |")
    parts.append("")
    return "\n".join(parts)


def emit_threshold_warnings(summary: dict) -> None:
    """Emit GitHub Actions ::warning:: annotations to stderr when inline-lane
    drift indicators exceed thresholds.

    Targets the inline-rabbit-hole pattern (70+ turns, 30+ inline `gh` calls,
    zero Pass 1 / zero Pass 3 — pure inline drift). The thresholds are advisory
    observability, not a hard block: the model already has a per-claim cap in
    `fact-check.md` §Inline lane, this surfaces violations operators can audit.

    Run in any context (CI, local). When run inside a GitHub Actions workflow,
    the `::warning::` lines are picked up as job annotations; outside CI they
    are inert stderr text.
    """
    counts = summary.get("counts", {}) or {}
    rm = summary.get("result_meta", {}) or {}
    gh_calls = counts.get("Bash:gh", 0)
    turns = rm.get("num_turns") or 0

    if gh_calls > 25:
        print(
            f"::warning title=Inline-lane drift::Bash:gh calls = {gh_calls} "
            f"(threshold 25). Suspected inline rabbit hole — audit per-claim "
            f"cap compliance in fact-check.md §Inline lane.",
            file=sys.stderr,
        )
    if gh_calls > 50:
        print(
            f"::error title=Inline-lane over-spend::Bash:gh calls = {gh_calls} "
            f"(threshold 50). Past the PR-level 40-call cap in fact-check.md "
            f"§Inline lane — the model should have summarized unresolved claims "
            f"and dispatched a final Pass 1 batch instead of iterating further.",
            file=sys.stderr,
        )
    if turns > 80:
        print(
            f"::warning title=Inline-lane drift::num_turns = {turns} "
            f"(threshold 80). Suspected runaway — audit stream-JSON for "
            f"unbounded inline iteration.",
            file=sys.stderr,
        )


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--execution-log", required=True,
                   help="Path to claude-execution-output.json")
    p.add_argument("--output",
                   help="Output path (default: stdout). Format inferred from extension or --format.")
    p.add_argument("--format", choices=("json", "markdown"),
                   help="Output format. Default: inferred from --output extension; falls back to json.")
    args = p.parse_args()

    log_path = Path(args.execution_log)
    if not log_path.exists():
        print(f"per-tool-spend: execution-log not found: {log_path}", file=sys.stderr)
        return 2

    summary = parse_stream_json(log_path)
    emit_threshold_warnings(summary)

    fmt = args.format
    if fmt is None and args.output:
        ext = Path(args.output).suffix.lower()
        fmt = "markdown" if ext in (".md", ".markdown") else "json"
    if fmt is None:
        fmt = "json"

    if fmt == "markdown":
        out = render_markdown(summary)
    else:
        out = json.dumps(summary, indent=2)

    if args.output:
        Path(args.output).write_text(out)
    else:
        print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
