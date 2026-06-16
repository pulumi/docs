#!/usr/bin/env python3
"""Summarize permission-denied tool calls from a Claude Code execution log.

TEMPORARY DIAGNOSTIC. The content-review worker runs the review model under a
tight `--allowed-tools` allowlist, and runs show a high permission-denial count
(6-21 per run) with no record of *which* commands were rejected — the GitHub log
streams only the init and result events. This reads the action's `execution_file`
(the full message array, which only exists on the runner) and prints the denied
command strings so the allowlist can be sized from real data.

The authoritative source is the SDK result message's `permission_denials` array
(claude-code-action derives its `permission_denials_count` from exactly this:
`resultMsg.permission_denials?.length`). Each entry carries the denied call's
`tool_name` and `tool_input`, so we read it directly rather than scraping
tool_result text.

Safe for a public repo: it emits only the model's own *attempted* (and therefore
un-executed) command strings — never tool results, which can carry command output
or secrets.

Usage: python3 summarize-denials.py <execution_file>
"""

from __future__ import annotations

import argparse
import collections
import json
import os
import sys


def load_events(path: str) -> list:
    """Return the message array, tolerating a JSON array, JSONL, or wrapper."""
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


def find_denials(events: list) -> list:
    """The permission_denials array, from the result message or anywhere it sits.

    Primary: the `type == "result"` message's `permission_denials`. Fallback: a
    recursive search, so a wrapper/shape change still surfaces the data.
    """
    for ev in events:
        if isinstance(ev, dict) and ev.get("type") == "result":
            pd = ev.get("permission_denials")
            if isinstance(pd, list):
                return pd

    found: list = []

    def walk(node):
        if isinstance(node, dict):
            for k, v in node.items():
                if k == "permission_denials" and isinstance(v, list):
                    found.extend(v)
                else:
                    walk(v)
        elif isinstance(node, list):
            for item in node:
                walk(item)

    walk(events)
    return found


def describe(denial: dict) -> str:
    """A short label for a denied call: tool name + the Bash command if present."""
    name = denial.get("tool_name") or denial.get("name") or "?"
    inp = denial.get("tool_input") or denial.get("input") or {}
    if isinstance(inp, dict):
        detail = inp.get("command") or inp.get("file_path") or inp.get("path")
        if not detail and inp:
            detail = json.dumps(inp, sort_keys=True)[:200]
    else:
        detail = str(inp)[:200]
    return f"{name}: {detail}" if detail else name


def event_skeleton(events: list) -> str:
    """A values-free shape summary, to refine the parser if denials don't surface."""
    type_counts: collections.Counter[str] = collections.Counter()
    keys: set[str] = set()
    for ev in events:
        if isinstance(ev, dict):
            type_counts[str(ev.get("type", "<no type>"))] += 1
            keys.update(ev.keys())
    types = ", ".join(f"{t}×{n}" for t, n in type_counts.most_common())
    return f"{len(events)} messages; types: {types or 'none'}; top-level keys: {sorted(keys)}"


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

    denials = find_denials(events)
    tally: collections.Counter[str] = collections.Counter()
    for d in denials:
        tally[describe(d) if isinstance(d, dict) else str(d)[:200]] += 1

    lines = [f"## Tool permission denials ({len(denials)})", ""]
    if tally:
        for label, n in tally.most_common():
            lines.append(f"- ({n}×) `{label}`")
    else:
        # No denials surfaced — could be a genuinely clean run, or a shape change.
        # The skeleton (no values) lets us tell which without another blind guess.
        lines.append("_No permission_denials found._")
        lines += ["", f"<sub>shape: {event_skeleton(events)}</sub>"]
    report = "\n".join(lines)
    print(report)

    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as f:
            f.write(report + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
