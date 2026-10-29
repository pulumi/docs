// Copyright 2016-2026, Pulumi Corporation.  All rights reserved.

// Run from this directory with `yarn test`.

import * as assert from "assert";
import { test } from "node:test";

import { estimate, Usage } from "./pricing";

function usage(overrides: Partial<Usage>): Usage {
    return {
        edition: "essentials",
        iacResources: 0,
        iacResourceHours: 0,
        escSecrets: 0,
        escSecretHours: 0,
        workflowMinutes: 0,
        neoMillionTokens: 0,
        insightsResources: 0,
        insightsResourceHours: 0,
        ...overrides,
    };
}

test("the base price covers the included resources", () => {
    assert.strictEqual(estimate(usage({ iacResources: 0 })).totalUsd, 40);
    assert.strictEqual(estimate(usage({ iacResources: 500 })).totalUsd, 40);
    assert.strictEqual(estimate(usage({ edition: "pro", iacResources: 2000 })).totalUsd, 400);
    assert.strictEqual(estimate(usage({ edition: "enterprise", iacResources: 4750 })).totalUsd, 2000);
});

test("resources beyond the included tranche are charged the list rate", () => {
    const e = estimate(usage({ iacResources: 1000 }));
    assert.strictEqual(e.totalUsd, 131.25);
    assert.strictEqual(e.overageUsd, 91.25);
    assert.strictEqual(e.creditsUsed, 131.25);
});

// Only IaC: the published hourly ESC and Insights rates are rounded, so their
// full-month figures drift slightly from the monthly rates (Insights on
// Essentials is $0.000025 x 730 = $0.01825, against $0.0185/mo).
test("a full month of IaC resource-hours costs the same as the resources", () => {
    for (const [edition, count] of [["essentials", 1000], ["pro", 3000], ["enterprise", 6000]] as const) {
        const monthly = estimate(usage({ edition, iacResources: count }));
        const hourly = estimate(usage({ edition, iacResourceHours: count * 730 }));
        assert.strictEqual(hourly.totalUsd, monthly.totalUsd, edition);
    }
});

test("resources and resource-hours share the included tranche", () => {
    // 400 resources + 100 resources' worth of hours exactly fills Essentials' 500.
    assert.strictEqual(estimate(usage({ iacResources: 400, iacResourceHours: 73000 })).totalUsd, 40);
    // 600 resources' worth: 73,000 hours past the tranche at $0.00025.
    const mixed = estimate(usage({ iacResources: 400, iacResourceHours: 146000 }));
    assert.strictEqual(mixed.totalUsd, 58.25);
    assert.strictEqual(mixed.totalUsd, estimate(usage({ iacResources: 600 })).totalUsd);
});

test("secret and discovered-resource hours are priced at the hourly rates", () => {
    const e = estimate(usage({ iacResources: 1000, escSecretHours: 730, insightsResourceHours: 1000 }));
    assert.strictEqual(e.creditsUsed, 131.25 + 0.50005 + 0.025);
});

test("other meters draw from the same credit pool", () => {
    const e = estimate(usage({ iacResources: 1000, escSecrets: 20, workflowMinutes: 100, neoMillionTokens: 2 }));
    assert.strictEqual(e.totalUsd, 131.25 + 10 + 1 + 6);
});

test("flags volume pricing above the contact-sales threshold", () => {
    assert.strictEqual(estimate(usage({ iacResources: 4750 })).volumePricingLikely, false);
    assert.strictEqual(estimate(usage({ iacResources: 4751 })).volumePricingLikely, true);
    assert.strictEqual(estimate(usage({ iacResourceHours: 4751 * 730 })).volumePricingLikely, true);
    assert.strictEqual(estimate(usage({ iacResources: 4000, iacResourceHours: 751 * 730 })).volumePricingLikely, true);
});

test("rejects an unknown edition", () => {
    assert.throws(() => estimate(usage({ edition: "free" })));
});
