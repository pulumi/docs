#!/usr/bin/env python3
"""Site-wide scan for shortcodes that leak into the rendered markdown output.

Docs pages cascade `outputs: [HTML, markdown]`, rendering each shortcode through
its `layouts/shortcodes/<name>.markdown.md` template. A shortcode missing that
template can leave raw Hugo delimiters (`{{<`, `>}}`, `{{%`, `%}}`) in the
built `.md` output. Whether a shortcode renders cleanly is a property of the
SHORTCODE, not the page — so this is one pass over the whole built corpus
(`public/**/*.md`), run once or in CI, instead of a per-page check re-paid on
every content review (which the content-review worker therefore no longer does).

Legitimate shortcode-syntax *examples* (docs that teach Hugo) live in fenced
code blocks or inline code spans; those are stripped before scanning so the
signal stays clean. A delimiter outside code formatting is a real leak.

Scope note — this catches DELIMITER leaks only. It does NOT catch content
*mangling*, where a shortcode's markdown template silently drops or rewrites
content (e.g. stripped `<artifactId>` tags in Java blocks, or `[ -f` collapsing
to `[-f` in Bash blocks). Those are rendering-pipeline bugs for the templating
owner — tracked separately, not rediscoverable by a delimiter grep.

Usage:
    check-rendered-markdown.py [--public public] [--strict]
    check-rendered-markdown.py --self-test

`--strict` exits non-zero when any leak is found (for gating CI); the default is
advisory (report and exit 0). Requires a built site (`make build`) for a real
run; `--self-test` exercises the scan logic offline.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# An opening (`{{<`, `{{%`) or closing (`>}}`, `%}}`) Hugo shortcode delimiter.
DELIM_RE = re.compile(r"\{\{[<%]|[>%]\}\}")
# A markdown fenced-code-block marker (``` or ~~~), optionally indented / with a
# language tag. Toggles in/out of a code block.
FENCE_RE = re.compile(r"^\s*(?:```|~~~)")
# An inline code span: `…`. Stripped so documented syntax doesn't false-positive.
INLINE_CODE_RE = re.compile(r"`[^`]*`")


def scan_text(text: str) -> list[tuple[int, str]]:
    """Return (line_number, line) for every leaked delimiter outside code."""
    hits: list[tuple[int, str]] = []
    in_fence = False
    for i, line in enumerate(text.splitlines(), 1):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if DELIM_RE.search(INLINE_CODE_RE.sub("", line)):
            hits.append((i, line.strip()))
    return hits


def scan_tree(public: Path) -> dict[str, list[tuple[int, str]]]:
    """Scan every `*.md` under `public`, returning {relpath: hits} for leaks."""
    found: dict[str, list[tuple[int, str]]] = {}
    for md in sorted(public.rglob("*.md")):
        try:
            hits = scan_text(md.read_text(errors="replace"))
        except OSError:
            continue
        if hits:
            found[str(md.relative_to(public))] = hits
    return found


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--public", default="public", help="built-site root (default: public)")
    ap.add_argument("--strict", action="store_true", help="exit non-zero if any leak is found")
    ap.add_argument("--self-test", action="store_true", help="run offline scan-logic checks")
    args = ap.parse_args()

    if args.self_test:
        return self_test()

    root = Path(args.public)
    if not root.is_dir():
        print(f"check-rendered-markdown: no build found at {root}/ — run `make build` first",
              file=sys.stderr)
        return 2

    found = scan_tree(root)
    total = sum(len(h) for h in found.values())
    if not found:
        print(f"check-rendered-markdown: scanned {root}/ — no leaked shortcode delimiters")
        return 0

    for rel, hits in found.items():
        for line_no, line in hits:
            print(f"{rel}:{line_no}: {line}")
    print(f"\ncheck-rendered-markdown: {total} leak(s) across {len(found)} page(s)",
          file=sys.stderr)
    return 1 if args.strict else 0


def self_test() -> int:
    failures = []

    def check(name, cond):
        print(("ok: " if cond else "FAIL: ") + name,
              file=sys.stdout if cond else sys.stderr)
        if not cond:
            failures.append(name)

    leak = scan_text("Intro prose.\n\nThis page uses {{< notes >}} without a template.\n")
    check("leaked delimiter in prose is flagged", len(leak) == 1 and leak[0][0] == 3)

    closing = scan_text("Some text >}} dangling.\n")
    check("closing delimiter is flagged", len(closing) == 1)

    pct = scan_text("A {{% choosable %}} fragment leaked.\n")
    check("percent-delimiter is flagged", len(pct) == 1)

    fenced = scan_text("Example:\n\n```go\n{{< chooser >}}\ncode\n{{< /chooser >}}\n```\n\nDone.\n")
    check("delimiters inside a fenced block are ignored", fenced == [])

    inline = scan_text("Use the `{{< notes >}}` shortcode to add a callout.\n")
    check("delimiters inside inline code are ignored", inline == [])

    clean = scan_text("# Title\n\nPlain prose, a `code` span, and a list.\n\n- one\n- two\n")
    check("clean rendered markdown yields no hits", clean == [])

    mixed = scan_text("```\n{{< safe >}}\n```\n\nBut {{< leaked >}} here.\n")
    check("fence then a real leak: only the leak counts",
          len(mixed) == 1 and mixed[0][0] == 5)

    if failures:
        print(f"\n{len(failures)} failure(s)", file=sys.stderr)
        return 1
    print("\nall check-rendered-markdown self-tests passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
