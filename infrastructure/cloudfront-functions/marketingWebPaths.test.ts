// Copyright 2016-2026, Pulumi Corporation.  All rights reserved.

import * as assert from "assert";
import * as fs from "fs";
import { test } from "node:test";
import * as path from "path";

import { marketingWebAssetPaths, marketingWebPagePaths } from "../marketingWebPaths";

const workflow = fs.readFileSync(
    path.resolve(__dirname, "../../../.github/workflows/invalidate-dev-cache.yml"),
    "utf8",
);

function invalidationDefaults(): string[][] {
    const inputDefault = workflow.match(/^\s+paths:\n(?:\s+#.*\n|\s+description:.*\n)*\s+default: "([^"]+)"$/m);
    const pathsFallback = workflow.match(/^\s*PATHS: .*\|\| '([^']+)' \}\}$/m);
    assert.ok(inputDefault && pathsFallback, "couldn't find the default paths in invalidate-dev-cache.yml");
    return [inputDefault[1].split(" "), pathsFallback[1].split(" ")];
}

function covers(invalidationPath: string, pathPattern: string): boolean {
    const base = pathPattern.replace(/\*$/, "");
    if (!invalidationPath.endsWith("*")) {
        return !pathPattern.endsWith("*") && invalidationPath === base;
    }
    const prefix = invalidationPath.slice(0, -1);
    return pathPattern.endsWith("*") ? prefix.startsWith(base) || base.startsWith(prefix) : base.startsWith(prefix);
}

test("invalidate-dev-cache.yml flushes every marketing-web path by default", () => {
    for (const defaults of invalidationDefaults()) {
        for (const pathPattern of [...marketingWebPagePaths, ...marketingWebAssetPaths]) {
            assert.ok(defaults.some((p) => covers(p, pathPattern)), `${pathPattern} isn't invalidated`);
        }
    }
});
