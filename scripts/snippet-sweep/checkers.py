#!/usr/bin/env python3
"""Per-language parse checkers for the snippet sweep.

Design contract (precision over recall — "zero-slop"): a checker returns

    None                          — block parses cleanly
    SKIP                          — block cannot be checked with near-
                                    certainty; counted, never flagged
    {"message": str,
     "line_offset": int}          — parse error; line_offset is 0-based
                                    within the block content, so the
                                    reported source line is
                                    block["start_line"] + line_offset

Only languages in CHECKERS are checked at all; everything else (bash
transcripts, HCL, C#/Java until v2, untagged blocks) is out of scope by
construction, not skipped-and-counted.

The TypeScript/JavaScript checker shells out once per corpus to
`check-ts.mjs` (see `check_ts_batch`), not per block. Go shells out to
`gofmt -e` per candidate with a scaffold ladder. Python/YAML/JSON are
stdlib/PyYAML in-process.
"""

from __future__ import annotations

import ast
import json
import re
import subprocess
import textwrap
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
CHECK_TS = HERE / "check-ts.mjs"

SKIP = "skip"

# A line of nothing but dots (`...`, `....`) is a documentation elision,
# not code. Replaced with a per-language comment (indent preserved) before
# parsing.
ELLIPSIS_LINE_RE = re.compile(r"^(\s*)(\.{2,}|…)\s*$")

# Inline elision used as an expression placeholder — `prop: ...`, `f(...)`,
# `[...]` at end of list. The lookbehind spares Go variadics (`args...`)
# and TS spreads (`...args` has an identifier after, so the lookahead
# already excludes it). re.M so `$` means end-of-line (`const x = ...`).
INLINE_ELISION_RE = re.compile(
    r"(?<![\w\])])(\.\.\.|…)(?=\s*[,)\]};]|\s*$)", re.M
)

# Python fragments that open mid-construct can never parse standalone.
PY_CONTINUATION_RE = re.compile(
    r"^\s*(else\b|elif\b|except\b|finally\b|case\b)"
)

# Blocks composed by Hugo at render time ({{< example-program-snippet >}}
# inside a fence), containing hyphenated angle placeholders
# (`<backend-url>`, `<your-org>` — hyphens keep this away from real
# generics, since identifiers can't contain `-`), or containing
# elision-bracketed prose (`... a cluster's output property ...`) are
# pseudo-code by design — uncheckable.
_UNCHECKABLE_RES = (
    re.compile(r"\{\{[<%]"),
    re.compile(r"<[a-z0-9]+(?:-[a-z0-9]+)+>"),
    re.compile(r"\.\.\. [A-Za-z][^.\n]* \.\.\."),
)


def pre_skip(content: str) -> bool:
    """True when a block is uncheckable regardless of language."""
    return any(r.search(content) for r in _UNCHECKABLE_RES)


def _replace_elision_lines(content: str, comment: str) -> str:
    return "\n".join(
        ELLIPSIS_LINE_RE.sub(rf"\g<1>{comment}", line)
        for line in content.split("\n")
    )


def _strip_elisions(content: str, comment: str, placeholder: str) -> str:
    """Neutralize doc elisions: dot-only lines become a comment, inline
    `...` placeholders become a parseable expression."""
    return INLINE_ELISION_RE.sub(
        placeholder, _replace_elision_lines(content, comment)
    )


# ---- Python -----------------------------------------------------------------


def check_python(content: str):
    stripped = content.strip()
    if not stripped:
        return SKIP
    first = stripped.split("\n", 1)[0]
    # Interactive-session transcripts (>>> prompts) aren't parseable modules.
    if first.lstrip().startswith(">>>"):
        return SKIP
    if PY_CONTINUATION_RE.match(first):
        return SKIP
    src = textwrap.dedent(content)
    # `...` is a legal expression, but dot-lines like `....` aren't, and a
    # trailing `, ...` elision after a keyword argument parses as a
    # positional-after-keyword error — drop it.
    src = _replace_elision_lines(src, "...")
    src = re.sub(r",[ \t]*(\.\.\.|…)(?=\s*\))", "", src)
    # Scaffold ladder, mirroring the Go checker. Doc fragments routinely
    # (2) elide a def/class body with only a comment, (3) elide trailing
    # keyword arguments with a `...` line inside a call, or (4) show a bare
    # signature with no body. Flag only if every form fails; report the
    # as-is error.
    scaffolds = [
        src,
        re.sub(r"^(\s*)#.*$", r"\g<1>...", src, flags=re.M),
        "\n".join(
            line for line in src.split("\n")
            if not re.match(r"^\s*(\.\.\.|…)\s*$", line)
        ),
        src.rstrip() + (" ..." if src.rstrip().endswith(":") else ": ..."),
    ]
    first_error = None
    for candidate in scaffolds:
        try:
            ast.parse(candidate)
            return None
        except SyntaxError as e:
            if first_error is None:
                first_error = {
                    "message": f"python: {e.msg}",
                    "line_offset": max((e.lineno or 1) - 1, 0),
                }
    return first_error


# ---- YAML -------------------------------------------------------------------


class _PermissiveLoader(yaml.SafeLoader):
    """SafeLoader that accepts unknown tags (!Ref, !!custom, ...).

    Docs YAML routinely carries CloudFormation and other domain tags; the
    sweep checks well-formedness, not schema, so every tag constructs to
    None instead of erroring.
    """


_PermissiveLoader.add_multi_constructor("", lambda loader, suffix, node: None)


def check_yaml(content: str):
    if not content.strip():
        return SKIP
    # Hugo/Helm templating renders before the YAML is ever parsed for real;
    # the raw text is not valid YAML by design.
    if "{{" in content:
        return SKIP
    try:
        list(yaml.load_all(_replace_elision_lines(content, "# ..."),
                           Loader=_PermissiveLoader))
    except yaml.YAMLError as e:
        line = getattr(getattr(e, "problem_mark", None), "line", 0)
        msg = getattr(e, "problem", None) or str(e).split("\n")[0]
        return {"message": f"yaml: {msg}", "line_offset": line}
    return None


# ---- JSON -------------------------------------------------------------------


def check_json(content: str):
    if not content.strip():
        return SKIP
    # Commented or elided JSON is legal *as documentation*; only clean-looking
    # blocks are held to strict JSON. `\s//` catches both full-line and
    # trailing annotations (`"value": 21600 // seconds`) without skipping
    # every block that merely contains a URL ("https://...").
    if "..." in content or "…" in content:
        return SKIP
    if re.search(r"(?:^|\s)//|/\*", content, re.M):
        return SKIP
    try:
        json.loads(content)
    except json.JSONDecodeError as e:
        # Keyed fragments of a larger object (`"key": {...}`) are common in
        # schema docs; retry wrapped in braces and flag only if both fail.
        try:
            json.loads("{%s}" % content)
        except json.JSONDecodeError:
            return {"message": f"json: {e.msg}", "line_offset": e.lineno - 1}
    return None


# ---- Go ---------------------------------------------------------------------


def _gofmt(src: str):
    """Run `gofmt -e` on src; return None if clean, else (message, line)."""
    proc = subprocess.run(
        ["gofmt", "-e"],
        input=src,
        capture_output=True,
        text=True,
    )
    if proc.returncode == 0:
        return None
    first = (proc.stderr.strip() or "syntax error").split("\n")[0]
    # gofmt errors look like `<standard input>:3:5: message`.
    m = re.match(r"^<standard input>:(\d+):(?:\d+:)?\s*(.*)$", first)
    if m:
        return m.group(2), int(m.group(1)) - 1
    return first, 0


GO_IMPORT_RE = re.compile(
    r"\A((?:\s*(?://.*)?\n)*(?:import\s+(?:\([^)]*\)|\"[^\"]*\"|\w+\s+\"[^\"]*\")\s*\n)+)",
)


def check_go(content: str):
    if not content.strip():
        return SKIP
    # go.mod files are conventionally fenced as ```go but aren't Go source.
    first = next(
        (l for l in content.split("\n") if l.strip() and not l.strip().startswith("//")),
        "",
    )
    if first.startswith("module "):
        return SKIP
    src = _strip_elisions(content, "// ...", "nil")
    # Scaffold ladder: a snippet may be a full file, a file body missing its
    # package clause, a bare statement fragment, a pedagogical mix of an
    # import block followed by statement code (imports hoisted, rest
    # wrapped), or a func-literal/value fragment lifted from a larger
    # expression (`var _ =`, trailing comma stripped). Flag only if *every*
    # form fails; report the as-is error (closest to what the reader sees).
    scaffolds = [
        (src, 0),
        (f"package main\n{src}", 1),
        ("package main\nfunc _() {\n" + src + "\n}", 2),
        ("package main\nvar _ = " + src.rstrip().rstrip(","), 1),
    ]
    m = GO_IMPORT_RE.match(src)
    if m:
        imports, rest = m.group(1), src[m.end():]
        scaffolds.append(
            (f"package main\n{imports}func _() {{\n{rest}\n}}", None)
        )
    first_error = None
    for candidate, prefix_lines in scaffolds:
        result = _gofmt(candidate)
        if result is None:
            return None
        if first_error is None:
            msg, line = result
            first_error = {
                "message": f"go: {msg}",
                "line_offset": max(line - prefix_lines, 0),
            }
    return first_error


# ---- TypeScript / JavaScript (batch) -----------------------------------------


# A full-line comment naming a config file marks a multi-file teaching
# block (`// package.json` followed by JSON, then application code) —
# not a single parseable unit.
TS_FILENAME_COMMENT_RE = re.compile(
    r"^\s*//\s*[\w@./-]*\.(json|jsonc|yaml|yml|toml|txt)\s*$", re.M
)


def check_ts_batch(blocks: list[dict]) -> dict[int, dict | str | None]:
    """Check all TS/JS blocks in one Node process.

    `blocks` items need `lang` and `content`; the return maps each input
    index to None (clean), SKIP (uncheckable), or an error dict. Elision
    handling and the scaffold ladder live in check-ts.mjs.

    Raises RuntimeError if the Node helper itself fails (infra error, not
    a finding).
    """
    if not blocks:
        return {}
    results: dict[int, dict | str | None] = {}
    payload = []
    for i, b in enumerate(blocks):
        if TS_FILENAME_COMMENT_RE.search(b["content"]):
            results[i] = SKIP
            continue
        results[i] = None
        payload.append({"id": i, "lang": b["lang"], "content": b["content"]})
    if not payload:
        return results
    proc = subprocess.run(
        ["node", str(CHECK_TS)],
        input=json.dumps(payload),
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(
            f"check-ts.mjs failed (exit {proc.returncode}): {proc.stderr.strip()}"
        )
    for item in json.loads(proc.stdout):
        results[item["id"]] = {
            "message": f"{blocks[item['id']]['lang']}: {item['message']}",
            "line_offset": item["line_offset"],
        }
    return results


# Languages checked in-process, one block at a time. TS/JS run through
# check_ts_batch instead (see sweep.py).
CHECKERS = {
    "python": check_python,
    "yaml": check_yaml,
    "json": check_json,
    "go": check_go,
}

TS_LANGS = {"typescript", "javascript"}
