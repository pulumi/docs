#!/usr/bin/env python3
"""Tests for extract.py.

Self-contained — run with `python3 test_extract.py` (no pytest dep).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from extract import extract_blocks, normalize_lang

_failures: list[str] = []
_passes = 0


def check(cond: bool, msg: str) -> None:
    global _passes
    if cond:
        _passes += 1
    else:
        _failures.append(msg)
        print(f"  FAIL: {msg}", file=sys.stderr)


def blocks_of(text: str):
    return extract_blocks(text, "test.md")


print("== language normalization")
check(normalize_lang("typescript {hl_lines=[3]}") == "typescript",
      "info-string attributes stripped")
check(normalize_lang("ts") == "typescript", "ts alias")
check(normalize_lang("py") == "python", "py alias")
check(normalize_lang("yml") == "yaml", "yml alias")
check(normalize_lang("Golang") == "go", "case-insensitive alias")
check(normalize_lang("") == "", "no info string -> empty lang")

print("== plain fences")
bs = blocks_of("a\n\n```python\nx = 1\n```\n\nb\n")
check(len(bs) == 1, "one block")
check(bs[0]["lang"] == "python", "lang parsed")
check(bs[0]["start_line"] == 4 and bs[0]["end_line"] == 4, "line numbers")
check(bs[0]["content"] == "x = 1", "content")
check(bs[0]["block_index"] == 0, "index")

print("== tilde fences")
bs = blocks_of("~~~go\nfmt.Println()\n~~~\n")
check(len(bs) == 1 and bs[0]["lang"] == "go", "tilde fence extracted")

print("== nested fences (CommonMark length rule)")
bs = blocks_of("````\n```typescript\ninner\n```\n````\n")
check(len(bs) == 1, "outer four-backtick block is one block")
check("```typescript" in bs[0]["content"], "inner fence is literal content")
check(bs[0]["lang"] == "", "outer block has no lang")

print("== longer closing fence closes")
bs = blocks_of("```python\nx = 1\n`````\nprose\n")
check(len(bs) == 1 and bs[0]["content"] == "x = 1", "close on longer fence")

print("== mismatched fence char does not close")
bs = blocks_of("```python\nx = 1\n~~~\ny = 2\n```\n")
check(len(bs) == 1 and "~~~" in bs[0]["content"], "tildes inside backtick block")

print("== unclosed fence runs to EOF")
bs = blocks_of("```python\nx = 1\ny = 2\n")
check(len(bs) == 1 and bs[0]["content"] == "x = 1\ny = 2", "unclosed at EOF")

print("== backtick info string with backtick is not a fence")
bs = blocks_of("``` `not a fence`\ntext\n")
check(len(bs) == 0, "inline-code lookalike skipped")

print("== indentation")
bs = blocks_of("   ```python\nx = 1\n   ```\n")
check(len(bs) == 1, "three-space indented fence opens")
bs = blocks_of("    ```python\nnot a fence\n    ```\n")
check(len(bs) == 0, "four-space indent is an indented code block, not a fence")

print("== frontmatter skipped")
md = "---\ntitle: T\ndraft: false\n---\n\n```yaml\na: 1\n```\n"
bs = blocks_of(md)
check(len(bs) == 1, "frontmatter --- lines don't confuse the extractor")
check(bs[0]["start_line"] == 7, "line numbers account for frontmatter")

print("== choosable-wrapped blocks")
md = (
    "---\ntitle: T\n---\n\n"
    '{{< chooser language "typescript,python" >}}\n'
    "{{% choosable language typescript %}}\n\n"
    "```typescript\nconst a = 1;\n```\n\n"
    "{{% /choosable %}}\n"
    "{{% choosable language python %}}\n\n"
    "```python\na = 1\n```\n\n"
    "{{% /choosable %}}\n"
    "{{< /chooser >}}\n"
)
bs = blocks_of(md)
check(len(bs) == 2, "both choosable blocks extracted")
check([b["lang"] for b in bs] == ["typescript", "python"], "langs in order")
check([b["block_index"] for b in bs] == [0, 1], "indices sequential")

if _failures:
    print(f"\n{len(_failures)} failure(s), {_passes} passed", file=sys.stderr)
    sys.exit(1)
print(f"\nall {_passes} checks passed")
