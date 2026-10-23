// Copyright 2016-2026, Pulumi Corporation.  All rights reserved.

// Run from this directory with `yarn test`.

import * as assert from "assert";
import { test } from "node:test";

import * as pulumi from "@pulumi/pulumi";

import { FunctionUrlEvent, MAX_BODY_BYTES, pricingHandler, ratesFromEnv } from "./handler";
import { DEFAULT_RATES } from "./pricing";

function get(query: Record<string, string>): FunctionUrlEvent {
    return { queryStringParameters: query, requestContext: { http: { method: "GET" } } };
}

function post(body: string, contentType = "application/json"): FunctionUrlEvent {
    return { body, headers: { "content-type": contentType }, requestContext: { http: { method: "POST" } } };
}

test("estimates from GET query parameters", async () => {
    const res = await pricingHandler(get({ edition: "essentials", iac_resources: "1000" }));
    assert.strictEqual(res.statusCode, 200);
    assert.strictEqual(JSON.parse(res.body).estimate.totalUsd, 131.25);
});

test("estimates from a POST JSON body", async () => {
    const body = { edition: "essentials", unit: "hour", iac_resources: 730000 };
    const res = await pricingHandler(post(JSON.stringify(body)));
    assert.strictEqual(res.statusCode, 200);
    assert.strictEqual(JSON.parse(res.body).estimate.totalUsd, 131.25);
});

test("reports every invalid field", async () => {
    const res = await pricingHandler(get({ edition: "free", unit: "day", iac_resources: "-1", esc_secrets: "lots", typo: "1" }));
    assert.strictEqual(res.statusCode, 400);
    const { fields } = JSON.parse(res.body);
    for (const key of ["edition", "unit", "iac_resources", "esc_secrets", "typo"]) {
        assert.ok(fields[key], `expected an error for ${key}`);
    }
});

test("requires an edition", async () => {
    const res = await pricingHandler(get({ iac_resources: "10" }));
    assert.strictEqual(res.statusCode, 400);
    assert.ok(JSON.parse(res.body).fields.edition);
});

test("doesn't accept inherited property names as an edition", async () => {
    const res = await pricingHandler(get({ edition: "constructor" }));
    assert.strictEqual(res.statusCode, 400);
});

test("rejects malformed POSTs", async () => {
    assert.strictEqual((await pricingHandler(post("{", "application/json"))).statusCode, 400);
    assert.strictEqual((await pricingHandler(post("[]"))).statusCode, 400);
    assert.strictEqual((await pricingHandler(post("{}", "text/plain"))).statusCode, 400);
    assert.strictEqual((await pricingHandler(post(""))).statusCode, 400);
    assert.strictEqual((await pricingHandler(post("x".repeat(MAX_BODY_BYTES + 1)))).statusCode, 413);
});

test("rejects other methods", async () => {
    const res = await pricingHandler({ requestContext: { http: { method: "DELETE" } } });
    assert.strictEqual(res.statusCode, 405);
});

test("uses the rates the deploy passes in PRICING_RATES", async () => {
    const rates = {
        ...DEFAULT_RATES,
        editions: { ...DEFAULT_RATES.editions, team: { ...DEFAULT_RATES.editions.essentials, base_usd: 100 } },
    };
    process.env.PRICING_RATES = JSON.stringify(rates);
    try {
        const res = await pricingHandler(get({ edition: "team" }));
        assert.strictEqual(res.statusCode, 200);
        assert.strictEqual(JSON.parse(res.body).estimate.totalUsd, 100);
    } finally {
        delete process.env.PRICING_RATES;
    }
});

test("falls back to the built-in rates when PRICING_RATES is unset or invalid", () => {
    assert.strictEqual(ratesFromEnv({}), DEFAULT_RATES);
    assert.strictEqual(ratesFromEnv({ PRICING_RATES: "{" }), DEFAULT_RATES);
});

// The deployed handler isn't this module: aws.lambda.CallbackFunction ships it
// through Pulumi's closure serialization, which can change captured values (it
// turns a Set into a plain object, for one). Run the serialized copy too.
test("works after Pulumi's closure serialization", async () => {
    const serialized = await pulumi.runtime.serializeFunction(pricingHandler);
    const mod: { exports: Record<string, typeof pricingHandler> } = { exports: {} };
    new Function("module", "exports", "require", serialized.text)(mod, mod.exports, require);
    const res = await mod.exports[serialized.exportName](get({ edition: "essentials", iac_resources: "1000" }));
    assert.strictEqual(res.statusCode, 200, res.body);
    assert.strictEqual(JSON.parse(res.body).estimate.totalUsd, 131.25);
});
