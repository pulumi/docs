// Copyright 2016-2026, Pulumi Corporation.  All rights reserved.

// Run from the infrastructure directory with `yarn test-pricing-api`.

import * as assert from "assert";
import { test } from "node:test";

import * as pulumi from "@pulumi/pulumi";

import { DISCLAIMER, FunctionUrlEvent, MAX_BODY_BYTES, originSecretOk, pricingHandler } from "./handler";

// What CloudFront stamps on every origin request (see pricingApi.ts).
const SECRET = "test-origin-secret";
process.env.PRICING_API_ORIGIN_SECRET = SECRET;

function get(query: Record<string, string>, headers: Record<string, string> = { "x-origin-verify": SECRET }) {
    const event: FunctionUrlEvent = {
        queryStringParameters: query,
        headers,
        requestContext: { http: { method: "GET" } },
    };
    return event;
}

function post(body: string, contentType = "application/json"): FunctionUrlEvent {
    const headers = { "content-type": contentType, "x-origin-verify": SECRET };
    return { body, headers, requestContext: { http: { method: "POST" } } };
}

test("rejects requests that didn't come through CloudFront", async () => {
    const attempts: Record<string, string>[] = [{}, { "x-origin-verify": "wrong" }, { "x-origin-verify": "" }];
    for (const headers of attempts) {
        const res = await pricingHandler(get({ edition: "essentials" }, headers));
        assert.strictEqual(res.statusCode, 403, JSON.stringify(headers));
    }
});

test("checks the origin secret against a rotation list, and fails closed without one", () => {
    assert.strictEqual(originSecretOk("new", "old, new"), true);
    assert.strictEqual(originSecretOk("old", "old, new"), true);
    assert.strictEqual(originSecretOk("other", "old, new"), false);
    assert.strictEqual(originSecretOk("anything", undefined), false);
    assert.strictEqual(originSecretOk("anything", ""), false);
    assert.strictEqual(originSecretOk(undefined, "old"), false);
});

test("includes the disclaimer and the rates' source", async () => {
    const body = JSON.parse((await pricingHandler(get({ edition: "pro" }))).body);
    assert.strictEqual(body.disclaimer, DISCLAIMER);
    // No PRICING_URL in the test environment, so the refresh is off.
    assert.deepStrictEqual(body.rates, { source: "built-in" });
});

test("estimates from GET query parameters", async () => {
    const res = await pricingHandler(get({ edition: "essentials", iac_resources: "1000" }));
    assert.strictEqual(res.statusCode, 200);
    assert.strictEqual(JSON.parse(res.body).estimate.totalUsd, 131.25);
});

test("estimates from a POST JSON body", async () => {
    const body = { edition: "essentials", iac_resource_hours: 730000 };
    const res = await pricingHandler(post(JSON.stringify(body)));
    assert.strictEqual(res.statusCode, 200);
    assert.strictEqual(JSON.parse(res.body).estimate.totalUsd, 131.25);
});

test("combines resources and resource-hours", async () => {
    const query = { edition: "essentials", iac_resources: "400", iac_resource_hours: "146000" };
    const res = await pricingHandler(get(query));
    assert.strictEqual(res.statusCode, 200);
    assert.strictEqual(JSON.parse(res.body).estimate.totalUsd, 58.25);
});

test("explains that unit was replaced by the _hours fields", async () => {
    const res = await pricingHandler(get({ edition: "essentials", unit: "hour", iac_resources: "730000" }));
    assert.strictEqual(res.statusCode, 400);
    assert.match(JSON.parse(res.body).fields.unit, /iac_resource_hours/);
});

test("reports every invalid field", async () => {
    const query = { edition: "free", iac_resource_hours: "-1", esc_secrets: "lots", typo: "1" };
    const res = await pricingHandler(get(query));
    assert.strictEqual(res.statusCode, 400);
    const { fields } = JSON.parse(res.body);
    for (const key of ["edition", "iac_resource_hours", "esc_secrets", "typo"]) {
        assert.ok(fields[key], `expected an error for ${key}`);
    }
});

test("accepts an edition in any case, with whitespace or quotes", async () => {
    for (const edition of ["Pro", "PRO", " pro ", "\"pro\"", "'Pro'"]) {
        const res = await pricingHandler(get({ edition, iac_resources: "2000" }));
        assert.strictEqual(res.statusCode, 200, `${JSON.stringify(edition)}: ${res.body}`);
        assert.strictEqual(JSON.parse(res.body).estimate.edition, "pro");
        assert.strictEqual(JSON.parse(res.body).estimate.totalUsd, 400);
    }
});

test("echoes an unrecognized edition in the error", async () => {
    const res = await pricingHandler(get({ edition: "{{edition}}" }));
    assert.strictEqual(res.statusCode, 400);
    assert.match(JSON.parse(res.body).fields.edition, /received "\{\{edition\}\}"/);
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
    const res = await pricingHandler({ headers: { "x-origin-verify": SECRET }, requestContext: { http: { method: "DELETE" } } });
    assert.strictEqual(res.statusCode, 405);
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
