// Copyright 2016-2026, Pulumi Corporation.  All rights reserved.

// Unit tests for the support-form payload validation and Lambda handler.
// Pure Node — no AWS machinery. Run from the infrastructure directory with:
//
//     yarn test-support-form
//
// (which compiles this directory with tsc and runs the output under the
// built-in Node test runner).

import * as assert from "assert";
import { test } from "node:test";

import { FunctionUrlEvent, supportFormHandler } from "./handler";
import { normalizeOrganization, validateSubmission } from "./validation";

function validPayload(): Record<string, unknown> {
    return {
        email: "jane@example.com",
        name: "Jane Doe",
        organization: "example-corp",
        priority: "normal",
        subject: "Stack update stuck in progress",
        description: "Running `pulumi up` hangs after the preview completes. Expected the update to apply.",
    };
}

test("accepts a fully valid payload", () => {
    const result = validateSubmission(validPayload());
    assert.ok(result.ok);
    if (result.ok) {
        assert.strictEqual(result.value.email, "jane@example.com");
        assert.strictEqual(result.value.priority, "normal");
    }
});

test("flags every missing required field", () => {
    const result = validateSubmission({});
    assert.ok(!result.ok);
    if (!result.ok) {
        for (const key of ["email", "name", "organization", "priority", "subject", "description"]) {
            assert.ok(result.fields[key], `expected an error for ${key}`);
        }
    }
});

test("rejects malformed email addresses", () => {
    for (const email of ["not-an-email", "a@b", "a b@example.com", ""]) {
        const result = validateSubmission({ ...validPayload(), email });
        assert.ok(!result.ok, `expected ${JSON.stringify(email)} to be rejected`);
        if (!result.ok) {
            assert.ok(result.fields.email);
        }
    }
});

test("normalizes a pasted console URL to the organization name", () => {
    assert.strictEqual(normalizeOrganization("https://app.pulumi.com/example-corp"), "example-corp");
    assert.strictEqual(normalizeOrganization("https://app.pulumi.com/example-corp/stacks/dev"), "example-corp");
    assert.strictEqual(normalizeOrganization("app.pulumi.com/example-corp"), "example-corp");
    assert.strictEqual(normalizeOrganization("  example-corp  "), "example-corp");
    assert.strictEqual(normalizeOrganization("example-corp/"), "example-corp");
});

test("applies normalization before validating the organization", () => {
    const result = validateSubmission({
        ...validPayload(),
        organization: "https://app.pulumi.com/example-corp",
    });
    assert.ok(result.ok);
    if (result.ok) {
        assert.strictEqual(result.value.organization, "example-corp");
    }
});

test("rejects organization names that fail the naming rules", () => {
    for (const organization of ["-leading-hyphen", "has spaces", "a".repeat(41)]) {
        const result = validateSubmission({ ...validPayload(), organization });
        assert.ok(!result.ok, `expected ${JSON.stringify(organization)} to be rejected`);
    }
});

test("rejects priorities outside the closed set", () => {
    const result = validateSubmission({ ...validPayload(), priority: "everything" });
    assert.ok(!result.ok);
    if (!result.ok) {
        assert.ok(result.fields.priority);
    }
});

test("rejects unknown top-level keys", () => {
    const result = validateSubmission({ ...validPayload(), admin: true });
    assert.ok(!result.ok);
    if (!result.ok) {
        assert.ok(result.fields._form);
    }
});

test("rejects non-string values for string fields", () => {
    const result = validateSubmission({ ...validPayload(), subject: 42 });
    assert.ok(!result.ok);
    if (!result.ok) {
        assert.ok(result.fields.subject);
    }
});

test("rejects too-short descriptions", () => {
    const result = validateSubmission({ ...validPayload(), description: "help" });
    assert.ok(!result.ok);
    if (!result.ok) {
        assert.ok(result.fields.description);
    }
});

// --- Handler-level tests ---

const SECRET = "test-secret";

function postEvent(body: unknown, overrides: Partial<FunctionUrlEvent> = {}): FunctionUrlEvent {
    return {
        body: typeof body === "string" ? body : JSON.stringify(body),
        isBase64Encoded: false,
        headers: {
            "content-type": "application/json",
            "x-origin-verify": SECRET,
        },
        requestContext: { http: { method: "POST", path: "/api/support", sourceIp: "192.0.2.1" } },
        ...overrides,
    };
}

test("handler accepts a valid submission", async () => {
    process.env.SUPPORT_FORM_ORIGIN_SECRET = SECRET;
    const response = await supportFormHandler(postEvent(validPayload()));
    assert.strictEqual(response.statusCode, 200);
    const parsed = JSON.parse(response.body);
    assert.strictEqual(parsed.ok, true);
    assert.ok(parsed.id);
    assert.strictEqual(response.headers["cache-control"], "no-store");
});

test("handler rejects a missing or wrong origin secret", async () => {
    process.env.SUPPORT_FORM_ORIGIN_SECRET = SECRET;
    const noHeader = postEvent(validPayload());
    delete (noHeader.headers as Record<string, string | undefined>)["x-origin-verify"];
    assert.strictEqual((await supportFormHandler(noHeader)).statusCode, 403);

    const wrongHeader = postEvent(validPayload());
    (wrongHeader.headers as Record<string, string | undefined>)["x-origin-verify"] = "nope";
    assert.strictEqual((await supportFormHandler(wrongHeader)).statusCode, 403);
});

test("handler accepts any secret in a comma-separated rotation list", async () => {
    process.env.SUPPORT_FORM_ORIGIN_SECRET = `old-secret, ${SECRET}`;
    const response = await supportFormHandler(postEvent(validPayload()));
    assert.strictEqual(response.statusCode, 200);
    process.env.SUPPORT_FORM_ORIGIN_SECRET = SECRET;
});

test("handler fails closed when no secret is configured", async () => {
    delete process.env.SUPPORT_FORM_ORIGIN_SECRET;
    const response = await supportFormHandler(postEvent(validPayload()));
    assert.strictEqual(response.statusCode, 403);
    process.env.SUPPORT_FORM_ORIGIN_SECRET = SECRET;
});

test("handler rejects non-POST methods with Allow", async () => {
    process.env.SUPPORT_FORM_ORIGIN_SECRET = SECRET;
    const event = postEvent(validPayload());
    event.requestContext = { http: { method: "GET", path: "/api/support" } };
    const response = await supportFormHandler(event);
    assert.strictEqual(response.statusCode, 405);
    assert.strictEqual(response.headers.allow, "POST");
});

test("handler rejects non-JSON content types", async () => {
    process.env.SUPPORT_FORM_ORIGIN_SECRET = SECRET;
    const event = postEvent(validPayload());
    (event.headers as Record<string, string | undefined>)["content-type"] = "text/plain";
    assert.strictEqual((await supportFormHandler(event)).statusCode, 400);
});

test("handler rejects malformed JSON", async () => {
    process.env.SUPPORT_FORM_ORIGIN_SECRET = SECRET;
    const response = await supportFormHandler(postEvent("{not json"));
    assert.strictEqual(response.statusCode, 400);
    assert.strictEqual(JSON.parse(response.body).error, "invalid_json");
});

test("handler rejects oversized bodies", async () => {
    process.env.SUPPORT_FORM_ORIGIN_SECRET = SECRET;
    const response = await supportFormHandler(postEvent("x".repeat(256 * 1024 + 1)));
    assert.strictEqual(response.statusCode, 413);
});

test("handler decodes base64-encoded bodies", async () => {
    process.env.SUPPORT_FORM_ORIGIN_SECRET = SECRET;
    const event = postEvent(validPayload());
    event.body = Buffer.from(event.body as string, "utf8").toString("base64");
    event.isBase64Encoded = true;
    assert.strictEqual((await supportFormHandler(event)).statusCode, 200);
});

test("handler returns field errors as a 422", async () => {
    process.env.SUPPORT_FORM_ORIGIN_SECRET = SECRET;
    const response = await supportFormHandler(postEvent({ ...validPayload(), email: "nope" }));
    assert.strictEqual(response.statusCode, 422);
    const parsed = JSON.parse(response.body);
    assert.strictEqual(parsed.error, "validation_failed");
    assert.ok(parsed.fields.email);
});

test("handler swallows honeypot submissions with a fake success", async () => {
    process.env.SUPPORT_FORM_ORIGIN_SECRET = SECRET;
    const response = await supportFormHandler(postEvent({ ...validPayload(), website: "https://spam.example" }));
    assert.strictEqual(response.statusCode, 200);
    assert.strictEqual(JSON.parse(response.body).ok, true);
});
