// Copyright 2016-2026, Pulumi Corporation.  All rights reserved.

// Run from this directory with `yarn test`.

import * as assert from "assert";
import * as fs from "fs";
import { test } from "node:test";
import * as path from "path";

import { LivePricing, parseLivePricing } from "./livePricing";
import { currentRates, RateCache, RefreshConfig, refreshConfigFromEnv } from "./liveRates";
import { DEFAULT_RATES } from "./pricing";

const snapshot = fs.readFileSync(path.join(__dirname, "../../pricing-api/testdata/pricing.md"), "utf8");
const changedPage = snapshot.replace("| IaC resource, per month | $0.1825 |", "| IaC resource, per month | $0.2 |");

const config: RefreshConfig = { url: "https://example.test/pricing.md", ttlMs: 60_000, fetchTimeoutMs: 1000 };

// A fake page fetch that counts its calls and serves whatever `page` holds.
function fakeFetch(page: { markdown?: string; error?: string }) {
    const calls: string[] = [];
    const fetchPricing = async (url: string): Promise<LivePricing> => {
        calls.push(url);
        if (page.error) {
            throw new Error(page.error);
        }
        return parseLivePricing(page.markdown || "");
    };
    return { calls, fetchPricing };
}

// The refresh logs on change and on failure; keep test output readable.
function quietly<T>(fn: () => Promise<T>): Promise<T> {
    const { log, error } = console;
    console.log = () => undefined;
    console.error = () => undefined;
    return fn().finally(() => {
        console.log = log;
        console.error = error;
    });
}

test("uses the built-in rates when refresh is disabled", async () => {
    const { calls, fetchPricing } = fakeFetch({ markdown: changedPage });
    const result = await currentRates({ source: "built-in" }, DEFAULT_RATES, { ...config, ttlMs: 0 }, 0, fetchPricing);
    assert.strictEqual(result.source, "built-in");
    assert.strictEqual(result.rates, DEFAULT_RATES);
    assert.strictEqual(calls.length, 0);
});

test("picks up a changed price from the page", async () => {
    const { fetchPricing } = fakeFetch({ markdown: changedPage });
    const result = await quietly(() => currentRates({ source: "built-in" }, DEFAULT_RATES, config, 0, fetchPricing));
    assert.strictEqual(result.source, "live");
    assert.strictEqual(result.rates.editions.essentials.iac_resource_month, 0.2);
    assert.strictEqual(result.refreshedAt, 0);
});

test("reads the page at most once per TTL", async () => {
    const cache: RateCache = { source: "built-in" };
    const { calls, fetchPricing } = fakeFetch({ markdown: snapshot });
    await currentRates(cache, DEFAULT_RATES, config, 0, fetchPricing);
    await currentRates(cache, DEFAULT_RATES, config, 59_999, fetchPricing);
    assert.strictEqual(calls.length, 1);
    await currentRates(cache, DEFAULT_RATES, config, 60_000, fetchPricing);
    assert.strictEqual(calls.length, 2);
});

test("keeps the built-in rates when the page can't be read", async () => {
    const cache: RateCache = { source: "built-in" };
    const { calls, fetchPricing } = fakeFetch({ error: "GET returned 503" });
    const result = await quietly(() => currentRates(cache, DEFAULT_RATES, config, 0, fetchPricing));
    assert.strictEqual(result.source, "built-in");
    assert.strictEqual(result.rates, DEFAULT_RATES);
    // A failing page isn't retried on every request.
    await quietly(() => currentRates(cache, DEFAULT_RATES, config, 1000, fetchPricing));
    assert.strictEqual(calls.length, 1);
});

test("keeps the last good rates when the page stops parsing", async () => {
    const cache: RateCache = { source: "built-in" };
    const page: { markdown?: string; error?: string } = { markdown: changedPage };
    const { fetchPricing } = fakeFetch(page);
    await quietly(() => currentRates(cache, DEFAULT_RATES, config, 0, fetchPricing));

    page.markdown = "# Pricing\n\nRedesigned.\n";
    const result = await quietly(() => currentRates(cache, DEFAULT_RATES, config, 60_000, fetchPricing));
    assert.strictEqual(result.source, "live");
    assert.strictEqual(result.rates.editions.essentials.iac_resource_month, 0.2);
    assert.strictEqual(result.refreshedAt, 0);
});

test("logs a failed refresh with the type the alarm matches", async () => {
    const { fetchPricing } = fakeFetch({ markdown: "# Pricing\n" });
    const lines: string[] = [];
    const { error } = console;
    console.error = (line: string) => lines.push(line);
    try {
        await currentRates({ source: "built-in" }, DEFAULT_RATES, config, 0, fetchPricing);
    } finally {
        console.error = error;
    }
    assert.strictEqual(lines.length, 1);
    assert.strictEqual(JSON.parse(lines[0]).type, "pricing_rates_refresh_failed");
});

test("reads its settings from the environment", () => {
    assert.deepStrictEqual(refreshConfigFromEnv({}), { url: undefined, ttlMs: 0, fetchTimeoutMs: 3000 });
    assert.deepStrictEqual(
        refreshConfigFromEnv({ PRICING_URL: "https://x.test/p.md", PRICING_REFRESH_SECONDS: "3600" }),
        { url: "https://x.test/p.md", ttlMs: 3_600_000, fetchTimeoutMs: 3000 },
    );
    assert.strictEqual(refreshConfigFromEnv({ PRICING_REFRESH_SECONDS: "nope" }).ttlMs, 0);
});
