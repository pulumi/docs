#!/usr/bin/env node
// Batch TypeScript/JavaScript syntax checker for the snippet sweep.
//
// stdin:  JSON array of {id: number, lang: "typescript"|"javascript",
//         content: string}
// stdout: JSON array of {id, message, line_offset} — one entry per block
//         that FAILS to parse; clean blocks are omitted.
//
// Syntax only: ts.transpileModule with reportDiagnostics surfaces parse
// errors without type checking or module resolution, so import-less
// fragments parse fine (top-level statements are legal in a module).
//
// Precision over recall, via a scaffold ladder mirroring the Go/Python
// checkers. Documentation elisions (`...` as a value placeholder, `{ ... }`
// object stubs, `/*...*/` as an expression) are neutralized first; then a
// block that fails plain parsing is retried across elision substitutions
// (`null` for statement positions, `...{}` spread for object/array/call
// positions) and forms (.tsx for JSX samples, expression wrap for bare
// object/config fragments, brace-balancing for pedagogically truncated
// classes). A block flags only if EVERY combination fails; the plain
// diagnostic is the one reported (closest to what the reader sees).

import ts from "typescript";
import { readFileSync } from "node:fs";

const ELISION_LINE = /^(\s*)(\.{2,}|…)\s*$/;
// `/*...*/` used as an expression placeholder normalizes to `...` so the
// substitution variants below treat both spellings the same.
const COMMENT_ELISION = /\/\*\s*\.{3}\s*\*\/(?=\s*[,)\]};]|\s*$)/gm;
const INLINE_ELISION = /(?<![\w\])])(\.\.\.|…)(?=\s*[,)\]};]|\s*$)/gm;
const OBJECT_STUB = /\{\s*(\.\.\.|…)\s*\}/g;

function preprocess(content) {
  return content
    .split("\n")
    .map((line) => line.replace(ELISION_LINE, "$1// ..."))
    .join("\n")
    .replace(OBJECT_STUB, "{}")
    .replace(COMMENT_ELISION, "...");
}

function braceDeficit(content) {
  let open = 0;
  for (const ch of content) {
    if (ch === "{") open += 1;
    else if (ch === "}") open -= 1;
  }
  return open;
}

function firstDiagnostic(content, fileName, jsx) {
  const compilerOptions = {
    target: ts.ScriptTarget.ESNext,
    module: ts.ModuleKind.ESNext,
  };
  if (jsx) compilerOptions.jsx = ts.JsxEmit.Preserve;
  const out = ts.transpileModule(content, {
    fileName,
    reportDiagnostics: true,
    compilerOptions,
  });
  // Only diagnostics anchored to the source file are parse errors; unanchored
  // ones are compiler-option noise and must not flag a snippet.
  const diags = (out.diagnostics || []).filter(
    (d) => d.category === ts.DiagnosticCategory.Error && d.file
  );
  if (diags.length === 0) return null;
  const d = diags[0];
  let line = 0;
  if (d.file && typeof d.start === "number") {
    line = d.file.getLineAndCharacterOfPosition(d.start).line;
  }
  const message = ts.flattenDiagnosticMessageText(d.messageText, " ");
  return { message: `TS${d.code}: ${message}`, line_offset: line };
}

function check(block) {
  const ext = block.lang === "typescript" ? "ts" : "js";
  const base = preprocess(block.content);
  const substitutions = [
    base.replace(INLINE_ELISION, "null"),
    base.replace(INLINE_ELISION, "...{}"),
  ];

  let plainError;
  for (const src of substitutions) {
    const forms = [
      { text: src, file: `snippet.${ext}`, jsx: false },
      { text: src, file: `snippet.${ext}x`, jsx: true },
      { text: `const __snippet = {\n${src}\n};`, file: `snippet.${ext}`, jsx: false },
      { text: `const __snippet = (\n${src}\n);`, file: `snippet.${ext}`, jsx: false },
    ];
    const deficit = braceDeficit(src);
    if (deficit > 0) {
      forms.push({
        text: src + "\n" + "}".repeat(deficit),
        file: `snippet.${ext}`,
        jsx: false,
      });
    }
    for (const form of forms) {
      const err = firstDiagnostic(form.text, form.file, form.jsx);
      if (err === null) return null;
      if (plainError === undefined) plainError = err;
    }
  }
  return plainError;
}

const blocks = JSON.parse(readFileSync(0, "utf8"));
const failures = [];
for (const block of blocks) {
  const err = check(block);
  if (err !== null) failures.push({ id: block.id, ...err });
}
process.stdout.write(JSON.stringify(failures));
