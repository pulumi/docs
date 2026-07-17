#!/usr/bin/env python3
"""Extract fenced code blocks from Hugo markdown content.

Pure, importable module: no I/O beyond reading the file handed to it, no
side effects. The sweep orchestrator (`sweep.py`) feeds each block to the
per-language checkers in `checkers.py`.

Fence handling follows CommonMark:

- An opening fence is 3+ backticks or tildes, indented at most 3 spaces,
  optionally followed by an info string (no backticks allowed in a
  backtick fence's info string).
- The block closes only on a fence of the *same character* with *at least
  the opening length* and nothing but whitespace after it. This makes
  nested fences safe (a four-backtick block quoting a three-backtick
  example stays one block).
- An unclosed fence runs to end of file.

The leading `---` frontmatter block is skipped. Hugo shortcode wrapper
lines outside fences ({{% choosable %}}, {{< chooser >}}) are ordinary
non-fence text and need no special handling; shortcode text *inside* a
fence is literal block content and is left to the checkers' skip rules.

Each block is reported as a dict:

    {"path": str, "block_index": int, "lang": str,
     "start_line": int, "end_line": int, "content": str}

`start_line` is the 1-based line number of the first *content* line (the
line after the opening fence); `end_line` is the last content line.
`block_index` is the 0-based index among all fenced blocks in the file.
`lang` is the first info-string token, lowercased, with common aliases
normalized (`ts` -> `typescript`, `py` -> `python`, ...). Blocks with no
info string get `lang == ""`.
"""

from __future__ import annotations

import re

FENCE_OPEN_RE = re.compile(r"^ {0,3}(`{3,}|~{3,})[ \t]*(.*)$")

LANG_ALIASES = {
    "ts": "typescript",
    "js": "javascript",
    "py": "python",
    "yml": "yaml",
    "golang": "go",
    "sh": "bash",
    "shell": "bash",
    "cs": "csharp",
}


def normalize_lang(info: str) -> str:
    """First info-string token, lowercased, aliases resolved.

    Hugo allows attribute blocks in the info string (```typescript
    {hl_lines=[3]}); the token ends at whitespace or `{`.
    """
    token = re.split(r"[\s{]", info.strip(), maxsplit=1)[0].lower()
    return LANG_ALIASES.get(token, token)


def extract_blocks(text: str, path: str) -> list[dict]:
    """Return all fenced code blocks in `text` (see module docstring)."""
    lines = text.split("\n")
    # A file ending in a newline yields a phantom empty final element; drop
    # it so an unclosed fence at EOF doesn't grow a trailing blank line.
    if lines and lines[-1] == "":
        lines.pop()
    blocks: list[dict] = []
    i = 0
    n = len(lines)

    # Skip frontmatter line-wise so downstream line numbers stay correct.
    if lines and lines[0].strip() == "---":
        j = 1
        while j < n and lines[j].strip() != "---":
            j += 1
        if j < n:
            i = j + 1

    block_index = 0
    while i < n:
        m = FENCE_OPEN_RE.match(lines[i])
        if not m:
            i += 1
            continue
        fence = m.group(1)
        fence_char, fence_len = fence[0], len(fence)
        info = m.group(2)
        # CommonMark: a backtick fence's info string cannot contain backticks
        # (that's inline code, not a fence).
        if fence_char == "`" and "`" in info:
            i += 1
            continue
        close_re = re.compile(
            r"^ {0,3}%s{%d,}[ \t]*$" % (re.escape(fence_char), fence_len)
        )
        start = i + 1
        j = start
        while j < n and not close_re.match(lines[j]):
            j += 1
        content_lines = lines[start:j]
        blocks.append(
            {
                "path": path,
                "block_index": block_index,
                "lang": normalize_lang(info),
                "start_line": start + 1,  # 1-based; == fence line + 1
                "end_line": j,  # 1-based last content line
                "content": "\n".join(content_lines),
            }
        )
        block_index += 1
        i = j + 1

    return blocks
