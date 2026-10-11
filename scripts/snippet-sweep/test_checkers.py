#!/usr/bin/env python3
"""Tests for checkers.py — golden both ways per language.

Seeded errors MUST flag; documentation fragments MUST NOT. Every "must
not flag" case here is a false-positive class found during the initial
full-corpus audit — keep them passing or the sweep starts producing slop.

Self-contained — run with `python3 test_checkers.py` (no pytest dep;
requires `node` and `gofmt` on PATH, same as the sweep itself).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from checkers import (
    SKIP,
    check_go,
    check_json,
    check_python,
    check_ts_batch,
    check_yaml,
    pre_skip,
)

_failures: list[str] = []
_passes = 0


def check(cond: bool, msg: str) -> None:
    global _passes
    if cond:
        _passes += 1
    else:
        _failures.append(msg)
        print(f"  FAIL: {msg}", file=sys.stderr)


def ts(content: str, lang: str = "typescript"):
    return check_ts_batch([{"lang": lang, "content": content}])[0]


print("== pre_skip (uncheckable regardless of language)")
check(pre_skip('{{< example-program-snippet path="x" >}}'), "hugo shortcode <")
check(pre_skip("{{% choosable %}}"), "hugo shortcode %")
check(pre_skip("url: <backend-url>"), "hyphenated placeholder")
check(pre_skip("export const k = ... a cluster's output property ...;"),
      "elision-bracketed prose")
check(not pre_skip("const x: Array<string> = [];"), "generics don't skip")
check(not pre_skip("f(args...)"), "variadic doesn't skip")

print("== python")
check(check_python("bucket = s3.Bucket('b')") is None, "clean fragment")
check(check_python("    return x") is None, "indented body dedents")
check(check_python("else:\n    pass") == SKIP, "continuation keyword skips")
check(check_python(">>> import pulumi") == SKIP, "REPL transcript skips")
check(check_python("f(x=1, ...)") is None, "trailing elision after kwarg")
check(check_python("f(\n    x=1,\n    ...\n)") is None,
      "elision line inside call")
check(check_python("def f(args):\n    # ...\n\ng(f)") is None,
      "comment-only def body")
check(check_python("class C(Base):\n    # TODO one\n    # TODO two") is None,
      "comment-only class body")
check(check_python("def f(self,\n      x: int = 1) -> str") is None,
      "signature-only fragment")
check(check_python("....\nx = 1") is None, "dot-elision line")
check(check_python("web = Webhook('x',\n    active: True,\n)") is not None,
      "colon-for-equals kwargs flags")
check(check_python("f(a=1\n  b=2)") is not None, "missing comma flags")
check(check_python("x = (1") is not None, "unclosed paren flags")

print("== yaml")
check(check_yaml("a: 1\nb:\n  - c\n---\nd: 2") is None, "multi-doc")
check(check_yaml("Value: !Ref Foo\nB: !!custom x") is None, "unknown tags")
check(check_yaml("a: {{ .Values.x }}") == SKIP, "templating skips")
check(check_yaml("....\nbackend:\n  url: https://x") is None,
      "dot-elision line")
check(check_yaml("key: [${interp.id}]") is not None,
      "unquoted interpolation in flow sequence flags")
check(check_yaml("a: b\n c: d") is not None, "bad indent flags")

print("== json")
check(check_json('{"a": [1, 2], "b": null}') is None, "clean object")
check(check_json('"key": {"a": 1}') is None, "keyed fragment wraps")
check(check_json('{\n  // comment\n  "a": 1\n}') == SKIP, "line comment skips")
check(check_json('{"v": 21600 // seconds\n}') == SKIP,
      "trailing comment skips")
check(check_json('{"a": "https://x//y"}') is None, "URL // does not skip")
check(check_json('{"a": 1,}') is not None, "trailing comma flags")
check(check_json('{"a" 1}') is not None, "missing colon flags")

print("== go")
check(check_go(
    "package main\nimport \"fmt\"\nfunc main() { fmt.Println(1) }"
) is None, "full program")
check(check_go("func f() int {\n\treturn 1\n}") is None, "package-less decl")
check(check_go('x := cfg.Require("k")\nfmt.Println(x)') is None,
      "statement fragment")
check(check_go(
    'import (\n    "fmt"\n)\n\nx := 1\nfmt.Println(x)'
) is None, "imports hoisted over statements")
check(check_go(
    "func(_ ctx.Context, a *T) *R {\n\treturn nil\n},"
) is None, "func-literal fragment with trailing comma")
check(check_go("module example.com/x\n\ngo 1.24") == SKIP, "go.mod skips")
check(check_go("f(a, b...)") is None, "variadic untouched")
check(check_go("x := f(\n\ta,\n)") is None, "trailing comma call")
check(check_go("m := Map{ /*...*/ }") is None, "comment elision in braces")
check(check_go(
    "func main() {\n\tRun(func() error {\n\t\treturn nil\n\t}\n}"
) is not None, "missing close paren flags")
check(check_go("const t = `abc\n") is not None,
      "unterminated raw string flags")

print("== typescript / javascript")
check(ts('import * as aws from "@pulumi/aws";\nconst b = new aws.s3.Bucket("b");') is None,
      "import fragment")
check(ts("prop: value,\nother: 3,") is None, "object-property fragment")
check(ts("const el = <div a={1}>hi</div>;") is None, "JSX retries as tsx")
check(ts("const secret = ...\nconst x = 1;") is None, "statement elision")
check(ts('new R("n", { ... }, { parent: this });') is None, "object stub")
check(ts("new C(this, 'c', {\n  ..., // trimmed\n  a: 1,\n});") is None,
      "object spread elision")
check(ts('const o = { a: /*...*/ };') is None, "comment elision value")
check(ts('{\n  "compilerOptions": {\n    // ...\n    "baseUrl": "."\n  }\n}') is None,
      "JSONC config wraps as expression")
check(ts("class C {\n  readonly x: Output<string>;") is None,
      "brace-deficit class fragment")
check(ts("// package.json\n{\n}\nimport x from 'y';") == SKIP,
      "multi-file teaching block skips")
check(ts('f("h", new CB("f", {\n  cb: () => {},\n});') is not None,
      "missing close paren flags")
check(ts("const o = { foo() {} bar() {} };") is not None,
      "missing comma between methods flags")
check(ts("export = async () => {\n}", lang="javascript") is not None,
      "TS-only syntax in javascript flags")
check(ts("export docsBucketName = x.name;") is not None,
      "export without declaration flags")

print("== batch mapping")
res = check_ts_batch([
    {"lang": "typescript", "content": "const a = 1;"},
    {"lang": "typescript", "content": "// tsconfig.json\n{}"},
    {"lang": "typescript", "content": "const b = ((;"},
])
check(res[0] is None and res[1] == SKIP and res[2] is not None,
      "indices survive skip interleaving")

if _failures:
    print(f"\n{len(_failures)} failure(s), {_passes} passed", file=sys.stderr)
    sys.exit(1)
print(f"\nall {_passes} checks passed")
