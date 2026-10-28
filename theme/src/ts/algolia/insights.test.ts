// Copyright 2016-2026, Pulumi Corporation.  All rights reserved.

// Unit tests for the consent-gated Algolia insights client. From the theme
// directory:
//
//     yarn test-ts

import * as assert from "assert";
import { test } from "node:test";

import { createConsentGatedInsightsClient } from "./insights";

// A stand-in for runWithPulumiConsent: grant() runs the queued C0002 callbacks.
function setup() {
    const pending: Array<() => void> = [];
    (globalThis as any).window = {
        runWithPulumiConsent: (category: string, cb: () => void) => {
            assert.strictEqual(category, "C0002");
            pending.push(cb);
        },
    };
    const calls: unknown[][] = [];
    const client = Object.assign((...args: unknown[]) => calls.push(args), { version: "2.17.3" });
    const gated = createConsentGatedInsightsClient(client);
    return { gated, calls, grant: () => pending.splice(0).forEach(cb => cb()) };
}

test("keeps the real client's version so Autocomplete sends credentials as headers", () => {
    assert.strictEqual(setup().gated.version, "2.17.3");
});

test("sends nothing to Algolia before C0002, and drops events made then", () => {
    const { gated, calls, grant } = setup();
    gated("addAlgoliaAgent", "insights-plugin");
    gated("viewedObjectIDs", { objectIDs: ["a"] });
    gated("clickedObjectIDsAfterSearch", { objectIDs: ["a"], queryID: "q" });
    assert.deepStrictEqual(calls, []);

    grant();
    assert.deepStrictEqual(calls, [["addAlgoliaAgent", "insights-plugin"]]);
});

test("forwards every call once C0002 is granted", () => {
    const { gated, calls, grant } = setup();
    grant();
    gated("viewedObjectIDs", { objectIDs: ["b"] });
    assert.deepStrictEqual(calls, [["viewedObjectIDs", { objectIDs: ["b"] }]]);
});
