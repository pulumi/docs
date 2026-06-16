#!/usr/bin/env python3
"""Summarize permission-denied tool calls from a Claude Code execution log.

TEMPORARY DIAGNOSTIC. The content-review worker runs the review model under a
tight `--allowed-tools` allowlist, and runs show a high `permission_denials_count`
(12-21 per run) with no record of *which* commands were rejected — the GitHub log
streams only the init and result events. This reads the action's `execution_file`
(the full stream-json transcript, which only exists on the runner) and prints the
denied command strings so the allowlist can be sized from real data.

Safe for a public repo: it emits only the model's own *attempted* (and therefore
un-executed) command strings — never tool results, which can carry command output
or secrets. It cross-checks its tally against the result event's
`permission_denials_count` and notes any mismatch so the parse can be trusted.

Usage: python3 summarize-denials.py <execution_file>
"""

from __future__ import annotations

import argparse
import collections
import json
import os
import sys

# Substrings that mark a tool-permission rejection in a tool_result. Kept broad
# (matching is anchored on an `is_error` result) so a wording change upstream
# doesn't silently drop denials.
DENIAL_MARKERS = (
    "haven't granted",
    "hasn't been granted",
    "requested permissions",
    "permission to use",
    "not allowed to use",
    "permission denied",
    "permission to run",
)


def load_events(path: str) -> list[dict]:
    """Return the transcript events, tolerating a JSON array or JSONL."""
    text = open(path, encoding="utf-8").read()
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return [json.loads(line) for line in text.splitlines() if line.strip()]
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        return data.get("messages", [data])
    return []


def content_blocks(event: dict) -> list:
    """The content blocks of an event, whether nested under `message` or not."""
    msg = event.get("message", event)
    blocks = msg.get("content")
    return blocks if isinstance(blocks, list) else []


def block_text(content) -> str:
    """Flatten a tool_result `content` (string or list of text blocks)."""
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return " ".join(
            b.get("text", "") for b in content if isinstance(b, dict)
        )
    return ""


def describe(tool_use: dict) -> str:
    """A short label for a tool_use: the Bash command, else the tool name."""
    name = tool_use.get("name", "?")
    inp = tool_use.get("input") or {}
    detail = inp.get("command") or inp.get("file_path") or inp.get("path")
    return f"{name}: {detail}" if detail else name


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("logfile")
    args = ap.parse_args()

    if not os.path.isfile(args.logfile):
        print(f"summarize-denials: no execution log at {args.logfile}")
        return 0
    try:
        events = load_events(args.logfile)
    except (OSError, json.JSONDecodeError) as e:
        print(f"summarize-denials: could not parse execution log ({e})")
        return 0

    # Map each tool_use id to its label, then attribute denial results back to it.
    labels: dict[str, str] = {}
    reported_count = None
    for ev in events:
        for b in content_blocks(ev):
            if b.get("type") == "tool_use":
                labels[b.get("id")] = describe(b)
        if ev.get("type") == "result":
            reported_count = ev.get("permission_denials_count", reported_count)

    denied: collections.Counter[str] = collections.Counter()
    for ev in events:
        for b in content_blocks(ev):
            if b.get("type") != "tool_result" or not b.get("is_error"):
                continue
            text = block_text(b.get("content")).lower()
            if any(m in text for m in DENIAL_MARKERS):
                denied[labels.get(b.get("tool_use_id"), "<unknown tool>")] += 1

    total = sum(denied.values())
    lines = [f"## Tool permission denials ({total} matched)", ""]
    if denied:
        for label, n in denied.most_common():
            lines.append(f"- ({n}×) `{label}`")
    else:
        lines.append("_No denial markers found in the transcript._")
    if reported_count is not None and reported_count != total:
        lines += [
            "",
            f"> Note: result reports {reported_count} denials but {total} were "
            "matched here — the denial wording may have changed; widen "
            "`DENIAL_MARKERS`.",
        ]
    report = "\n".join(lines)
    print(report)

    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as f:
            f.write(report + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
