// Copyright 2016-2026, Pulumi Corporation.  All rights reserved.

// Guards the support-form test script against silently running nothing.
//
// Two ways that happens, both of which report success:
//
//   1. `node --test <glob>` exits 0 when the glob matches no files. Rename or
//      move a suite and CI goes green having run zero tests.
//   2. tsconfig.json uses an explicit `files` array, so a new *.test.ts that
//      nobody added to it is never compiled. `tsc` exits 0 and emits nothing,
//      even if the file has type errors, and the glob then can't see it.
//
// Either one recreates the exact gap support-form-tests.yml exists to close --
// an unrun suite is indistinguishable from a passing one. So: every .test.ts on
// disk must have a compiled .test.js counterpart, and there must be at least one.
//
// Plain JS on purpose. It has to run before the test runner and outside the
// TypeScript build it is checking.

const fs = require("fs");
const path = require("path");

const srcDir = __dirname;
const outDir = path.join(__dirname, "..", "bin", "support-form");

const suites = fs
    .readdirSync(srcDir)
    .filter(f => f.endsWith(".test.ts"))
    .map(f => f.replace(/\.ts$/, ".js"));

if (suites.length === 0) {
    console.error("check-suites-compiled: no *.test.ts found in support-form/ — the suite has vanished.");
    process.exit(1);
}

const missing = suites.filter(f => !fs.existsSync(path.join(outDir, f)));

if (missing.length > 0) {
    console.error(
        "check-suites-compiled: these suites were not compiled, so they would not run:\n" +
            missing.map(f => `  - support-form/${f.replace(/\.js$/, ".ts")}`).join("\n") +
            '\n\nAdd each one to the "files" array in infrastructure/tsconfig.json.',
    );
    process.exit(1);
}

console.log(`check-suites-compiled: ${suites.length} suite(s) compiled and ready.`);
