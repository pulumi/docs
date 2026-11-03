// Copyright 2016-2026, Pulumi Corporation.  All rights reserved.

// Unit tests for the OneTrust consent bridge. From the theme directory:
//
//     yarn test-ts
//
// These drive the pure engine and mapping helpers directly — no DOM required —
// which is where the behavior that matters lives: which Segment destination
// maps to which category, that unknown destinations fail closed, and that the
// callback queue runs each integration exactly once and only after its category
// is granted.

import * as assert from "assert";
import { test } from "node:test";

import { ConsentEngine, STRICTLY_NECESSARY, SEGMENT_DESTINATION_CATEGORIES, categoryForDestination, parseActiveGroups, destinationPreferencesFromGroups, hasRevokedGroup } from "./onetrust";

test("parseActiveGroups handles OneTrust's comma-wrapped string", () => {
    const groups = parseActiveGroups(",C0001,C0003,");
    assert.ok(groups.has("C0001"));
    assert.ok(groups.has("C0003"));
    assert.ok(!groups.has("C0002"));
});

test("parseActiveGroups tolerates empty / non-string input", () => {
    assert.strictEqual(parseActiveGroups("").size, 0);
    assert.strictEqual(parseActiveGroups(undefined).size, 0);
    assert.strictEqual(parseActiveGroups(null).size, 0);
});

test("every Segment destination maps to its documented category", () => {
    const expected: Record<string, string> = {
        "AWS S3": "C0002",
        "Google Analytics 4": "C0002",
        "Google Analytics 4 Web": "C0002",
        "Intercom": "C0003",
        "Intercom Web Actions": "C0003",
        "HubSpot": "C0004",
        "Google Ads": "C0004",
        "LinkedIn Insight Tag": "C0004",
    };
    for (const name of Object.keys(expected)) {
        assert.strictEqual(categoryForDestination(name), expected[name], `${name} should map to ${expected[name]}`);
        assert.strictEqual(SEGMENT_DESTINATION_CATEGORIES[name], expected[name]);
    }
});

test("an unmapped Segment destination has no category", () => {
    assert.strictEqual(categoryForDestination("Some New Vendor"), null);
});

test("destinationPreferencesFromGroups defaults unknown destinations to disabled", () => {
    const destinations = [
        { id: "s3", name: "AWS S3" },
        { id: "hs", name: "HubSpot" },
        { id: "mystery", name: "Some New Vendor" },
    ];
    const active = new Set(["C0001", "C0002"]);
    const prefs = destinationPreferencesFromGroups(destinations, active);
    assert.strictEqual(prefs["s3"], true); // C0002 active
    assert.strictEqual(prefs["hs"], false); // C0004 not active
    assert.strictEqual(prefs["mystery"], false); // unmapped -> disabled
});

test("C0001 Strictly Necessary is always active, even before OneTrust resolves", () => {
    const engine = new ConsentEngine();
    assert.strictEqual(engine.isActive(STRICTLY_NECESSARY), true);

    let ran = false;
    engine.run(STRICTLY_NECESSARY, () => {
        ran = true;
    });
    assert.strictEqual(ran, true);
});

test("optional categories default to disabled until consent resolves", () => {
    const engine = new ConsentEngine();
    assert.strictEqual(engine.isActive("C0002"), false);
    assert.strictEqual(engine.isActive("C0004"), false);
});

test("a callback waits while consent is unresolved, then runs once granted", () => {
    const engine = new ConsentEngine();
    let count = 0;
    const loader = () => {
        count += 1;
    };

    engine.run("C0004", loader);
    assert.strictEqual(count, 0, "must not run before consent");

    engine.setGroups(new Set(["C0001"]), true);
    assert.strictEqual(count, 0, "must not run when its category is absent");

    engine.setGroups(new Set(["C0001", "C0004"]), true);
    assert.strictEqual(count, 1, "runs once its category is granted");
});

test("repeated OneTrust events do not load an integration twice", () => {
    const engine = new ConsentEngine();
    let count = 0;
    engine.run("C0002", () => {
        count += 1;
    });

    engine.setGroups(new Set(["C0002"]), true);
    engine.setGroups(new Set(["C0002"]), true);
    engine.setGroups(new Set(["C0002", "C0004"]), true);

    assert.strictEqual(count, 1);
});

test("a callback registered after consent is already granted runs immediately", () => {
    const engine = new ConsentEngine();
    engine.setGroups(new Set(["C0001", "C0003"]), true);

    let ran = false;
    engine.run("C0003", () => {
        ran = true;
    });
    assert.strictEqual(ran, true);
});

test("fails closed: optional callbacks never run when OneTrust is unavailable", () => {
    const engine = new ConsentEngine();
    let ran = false;
    engine.run("C0004", () => {
        ran = true;
    });

    // Resolved, but OneTrust reported unavailable (available=false).
    engine.setGroups(new Set(), false);
    assert.strictEqual(ran, false);
});

test("a throwing loader does not block other queued integrations", () => {
    const engine = new ConsentEngine();
    let second = false;
    engine.run("C0002", () => {
        throw new Error("vendor blew up");
    });
    engine.run("C0002", () => {
        second = true;
    });
    engine.setGroups(new Set(["C0002"]), true);
    assert.strictEqual(second, true);
});

test("hasRevokedGroup only reports withdrawn categories, so grants and repeat events don't reload", () => {
    const before = parseActiveGroups(",C0001,C0002,");
    // Same decision re-announced (OneTrust fires on page load too).
    assert.strictEqual(hasRevokedGroup(before, parseActiveGroups(",C0001,C0002,")), false);
    // A grant.
    assert.strictEqual(hasRevokedGroup(before, parseActiveGroups(",C0001,C0002,C0004,")), false);
    // First resolution from the unresolved (empty) state.
    assert.strictEqual(hasRevokedGroup(new Set(), before), false);
    // A withdrawal.
    assert.strictEqual(hasRevokedGroup(before, parseActiveGroups(",C0001,")), true);
});
