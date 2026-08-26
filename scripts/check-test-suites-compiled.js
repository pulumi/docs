// Copyright 2016-2026, Pulumi Corporation.  All rights reserved.

// Guards a compile-then-run test script against silently running nothing.
//
// Three ways that happens, all of which otherwise report success:
//
//   1. `node --test <glob>` exits 0 when the glob matches no files. Rename or
//      move a suite and CI goes green having run zero tests.
//   2. Both tsconfigs here use an explicit `files` array, so a new *.test.ts
//      that nobody added to it is never compiled. `tsc` exits 0 and emits
//      nothing, even if the file has type errors, and the glob then can't see
//      it.
//   3. The glob is not recursive, so a suite one directory down
//      (support-form/sub/foo.test.ts) is never run even when it compiles.
//
// Any of these recreates the exact gap support-form-tests.yml exists to close --
// an unrun suite is indistinguishable from a passing one. So: every .test.ts on
// disk, at any depth, must have a compiled .test.js counterpart that the runner
// will actually pick up, and there must be at least one.
//
// This checks that the suites will RUN. It cannot check that they contain
// assertions; the workflow asserts a non-zero test count from the runner itself
// for that half.
//
// Both halves of the support form need this, and they are separate packages
// with separate toolchains, so it takes its directories as arguments and lives
// at the repo root rather than inside either one:
//
//   node ../scripts/check-test-suites-compiled.js <srcDir> <outDir> <tsconfig>
//
// Paths are relative to the calling package. <tsconfig> is named only so the
// failure message can tell you which `files` array to edit.
//
// Plain JS on purpose. It has to run before the test runner and outside the
// TypeScript build it is checking.

const fs = require("fs");
const path = require("path");

const [srcArg, outArg, tsconfigArg] = process.argv.slice(2);

if (!srcArg || !outArg || !tsconfigArg) {
    console.error("usage: check-test-suites-compiled.js <srcDir> <outDir> <tsconfigPath>");
    process.exit(2);
}

const srcDir = path.resolve(srcArg);
const outDir = path.resolve(outArg);

if (!fs.existsSync(srcDir)) {
    console.error(`check-test-suites-compiled: source directory ${srcArg} does not exist.`);
    process.exit(1);
}

// Relative paths of every *.test.ts under srcDir, at any depth.
function findSuites(dir, prefix) {
    const found = [];
    for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
        const rel = prefix ? path.join(prefix, entry.name) : entry.name;
        if (entry.isDirectory()) {
            found.push(...findSuites(path.join(dir, entry.name), rel));
        } else if (entry.name.endsWith(".test.ts")) {
            found.push(rel);
        }
    }
    return found;
}

const suites = findSuites(srcDir, "");

if (suites.length === 0) {
    console.error(`check-test-suites-compiled: no *.test.ts found under ${srcArg} — the suite has vanished.`);
    process.exit(1);
}

const problems = [];

for (const rel of suites) {
    const compiled = rel.replace(/\.ts$/, ".js");
    if (!fs.existsSync(path.join(outDir, compiled))) {
        problems.push(`  - ${srcArg}/${rel} was not compiled — add it to "files" in ${tsconfigArg}`);
        continue;
    }
    // The runners use a single-level glob, so a compiled suite in a
    // subdirectory exists but never runs.
    if (rel.includes(path.sep)) {
        problems.push(`  - ${srcArg}/${rel} is in a subdirectory, which the test glob does not reach`);
    }
}

if (problems.length > 0) {
    console.error("check-test-suites-compiled: these suites would not run:\n" + problems.join("\n"));
    process.exit(1);
}

console.log(`check-test-suites-compiled: ${suites.length} suite(s) under ${srcArg} compiled and reachable.`);
