// Copyright 2016-2026, Pulumi Corporation.  All rights reserved.

// Run from this directory with `yarn test`. testdata/pricing.md is a snapshot
// of https://www.pulumi.com/pricing.md; refresh it when the page's format
// changes.

import * as assert from "assert";
import * as fs from "fs";
import { test } from "node:test";
import * as path from "path";

import { comparePricing, parseLivePricing, toRates } from "./livePricing";
import { DEFAULT_RATES, estimate } from "./pricing";

const snapshot = fs.readFileSync(path.join(__dirname, "../../pricing-api/testdata/pricing.md"), "utf8");

test("parses every rate from the pricing page", () => {
    const live = parseLivePricing(snapshot);
    assert.deepStrictEqual(live.editions.essentials, {
        base_usd: 40,
        included_credits: 40,
        included_resources: 500,
        iac_resource_month: 0.1825,
        iac_resource_hour: 0.00025,
        esc_secret_month: 0.5,
        esc_secret_hour: 0.000685,
        insights_resource_month: 0.0185,
        insights_resource_hour: 0.000025,
        workflow_minute: 0.01,
        neo_tokens_per_million: 3,
    });
    assert.strictEqual(live.editions.enterprise.base_usd, 2000);
    assert.strictEqual(live.editions.pro.iac_resource_hour, 0.0005);
    assert.strictEqual(live.contactSalesResources, 4750);
});

test("the snapshot matches pricing-api/pricing.ts", () => {
    assert.deepStrictEqual(comparePricing(parseLivePricing(snapshot)), []);
});

test("reports a changed rate", () => {
    const changed = snapshot.replace("| IaC resource, per month | $0.1825 |", "| IaC resource, per month | $0.2 |");
    assert.deepStrictEqual(comparePricing(parseLivePricing(changed)), [
        "essentials.iac_resource_month: pricing-api/pricing.ts has 0.1825, the pricing page has 0.2",
    ]);
});

test("reports a changed hourly rate", () => {
    const changed = snapshot.replace("$0.000685/hour", "$0.0007/hour");
    assert.deepStrictEqual(comparePricing(parseLivePricing(changed)), [
        "essentials.esc_secret_hour: pricing-api/pricing.ts has 0.000685, the pricing page has 0.0007",
    ]);
});

test("reports a changed base price", () => {
    const changed = snapshot.replace("**Pro** — $400/month base", "**Pro** — $450/month base");
    assert.deepStrictEqual(comparePricing(parseLivePricing(changed)), [
        "pro.base_usd: pricing-api/pricing.ts has 400, the pricing page has 450",
    ]);
});

test("reports a new edition", () => {
    const added = snapshot.replace(
        "**Pro** —",
        "**Team** — $100/month base, which includes 100 credits and covers up to 1,000 IaC resources.\n\n**Pro** —",
    );
    assert.deepStrictEqual(comparePricing(parseLivePricing(added)), [
        "team: edition is on the pricing page but not in pricing-api/pricing.ts",
    ]);
});

test("fails rather than passing when the page format changes", () => {
    const problems = comparePricing(parseLivePricing("# Pricing\n\nSomething else entirely.\n"));
    assert.ok(problems.length > 0);
    assert.ok(problems.every(p => p.includes("not found on the pricing page")));
});

test("rates built from the snapshot equal the built-in rates", () => {
    const result = toRates(parseLivePricing(snapshot));
    assert.ok(result.ok);
    if (result.ok) {
        assert.deepStrictEqual(result.rates, DEFAULT_RATES);
    }
});

test("rates built from a changed page use the page's values", () => {
    const changed = snapshot.replace("| IaC resource, per month | $0.1825 |", "| IaC resource, per month | $0.2 |");
    const result = toRates(parseLivePricing(changed));
    assert.ok(result.ok);
    if (result.ok) {
        assert.strictEqual(result.rates.editions.essentials.iac_resource_month, 0.2);
        const usage = {
            edition: "essentials",
            iacResources: 1000,
            iacResourceHours: 0,
            escSecrets: 0,
            escSecretHours: 0,
            workflowMinutes: 0,
            neoMillionTokens: 0,
            insightsResources: 0,
            insightsResourceHours: 0,
        };
        assert.strictEqual(estimate(usage, result.rates).totalUsd, 140);
    }
});

test("won't build rates from a page with a missing value", () => {
    const missing = snapshot.replace("| ESC secret, per month | $0.75 |\n", "");
    const result = toRates(parseLivePricing(missing));
    assert.ok(!result.ok);
    if (!result.ok) {
        assert.deepStrictEqual(result.problems, ["pro: not found on the pricing page: esc_secret_month"]);
    }
});

test("won't build rates when a shared meter differs between editions", () => {
    const changed = snapshot.replace("| 1M Neo tokens | $3.00 |", "| 1M Neo tokens | $4.00 |");
    const result = toRates(parseLivePricing(changed));
    assert.ok(!result.ok);
    if (!result.ok) {
        assert.ok(result.problems[0].startsWith("neo_tokens_per_million: expected one value across editions"));
    }
});

test("won't build rates from an unrecognizable page", () => {
    assert.ok(!toRates(parseLivePricing("# Pricing\n")).ok);
});
