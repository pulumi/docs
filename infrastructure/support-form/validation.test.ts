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

import { clientAddress, FunctionUrlEvent, supportFormHandler } from "./handler";
import { KNOWN_KEYS, LIMITS, normalizeOrganization, validateSubmission } from "./validation";

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

test("blames an over-long organization on its length, not its characters", () => {
    const result = validateSubmission({ ...validPayload(), organization: "a".repeat(LIMITS.organization + 1) });
    assert.ok(!result.ok);
    if (!result.ok) {
        assert.match(result.fields.organization || "", /characters/);
        assert.doesNotMatch(result.fields.organization || "", /hyphens/);
    }
    // The bound itself is LIMITS.organization, so a name exactly at it passes.
    assert.ok(validateSubmission({ ...validPayload(), organization: "a".repeat(LIMITS.organization) }).ok);
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
const TICKET_ID = "ticket-42";

// handler.ts files an Intercom ticket on the accept path, so every test below
// that expects a 200 would otherwise reach api.intercom.io with no credentials
// — hanging or 401-ing depending on the network. Replacing the global fetch for
// the whole file (node --test gives each test file its own process, and runs
// tests non-concurrently) makes that impossible by construction rather than
// test by test. intercomCalls records the traffic so the paths that must *not*
// file a ticket can assert on it. The request shape itself is covered in
// intercom.test.ts.
const intercomCalls: string[] = [];
const intercomRequests: Array<{ url: string; body: any }> = [];
let intercomUp = true;

globalThis.fetch = async (input, init) => {
    const url = String(input);
    intercomCalls.push(url);
    let sent: any;
    try {
        sent = init && typeof init.body === "string" ? JSON.parse(init.body) : undefined;
    } catch (e) {
        sent = undefined;
    }
    intercomRequests.push({ url, body: sent });
    if (!intercomUp) {
        return new Response("service unavailable", { status: 503 });
    }
    const body = url.endsWith("/contacts/search") ? { data: [{ id: "contact-1" }] } : { id: TICKET_ID };
    return new Response(JSON.stringify(body), { status: 200 });
};

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
    // id is minted locally; ticketId has to come back from Intercom, so
    // asserting it is what catches the result being dropped on the floor.
    assert.strictEqual(parsed.ticketId, TICKET_ID);
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

// --- Client-IP attribution ---
//
// requestContext.http.sourceIp is CloudFront's edge node, never the submitter.
// The real address arrives as the CloudFront-managed CloudFront-Viewer-Address
// header; these pin that it is preferred, that nothing a caller can author gets
// logged in its place, and that a fallback is labelled as one.

const EDGE_IP = "3.172.120.71";
const VIEWER_IP = "198.51.100.9";
const VIEWER_HEADER = "cloudfront-viewer-address";

function ipEvent(headers: Record<string, any> = {}): FunctionUrlEvent {
    return {
        headers,
        requestContext: { http: { method: "POST", path: "/api/support", sourceIp: EDGE_IP } },
    };
}

test("reads the viewer address CloudFront forwarded, stripping the port", () => {
    assert.deepStrictEqual(clientAddress(ipEvent({ [VIEWER_HEADER]: `${VIEWER_IP}:52001` })), {
        ip: VIEWER_IP,
        source: "viewer",
    });
    assert.deepStrictEqual(clientAddress(ipEvent({ [VIEWER_HEADER]: `  ${VIEWER_IP}:443  ` })), {
        ip: VIEWER_IP,
        source: "viewer",
    });
});

test("keeps an IPv6 viewer address intact by splitting on the last colon", () => {
    assert.deepStrictEqual(clientAddress(ipEvent({ [VIEWER_HEADER]: "2001:db8::1:443" })), {
        ip: "2001:db8::1",
        source: "viewer",
    });
});

test("never reads X-Forwarded-For, which is partly caller-authored", () => {
    // CloudFront appends the viewer to whatever the caller already sent, so the
    // header is half attacker-authored. If this ever starts returning 1.2.3.4,
    // the abuse trail has been poisoned.
    const result = clientAddress(ipEvent({ "x-forwarded-for": "1.2.3.4, 198.51.100.9" }));
    assert.deepStrictEqual(result, { ip: EDGE_IP, source: "edge" });
});

test("marks a fallback as edge, so it can't be mistaken for the submitter", () => {
    // The whole point of ipSource: a record that fell back must never read as an
    // attributed one. Malformed values fall back rather than being trusted.
    for (const value of ["", "   ", "A".repeat(65), ["1.2.3.4"], 5, null, {}]) {
        assert.deepStrictEqual(clientAddress(ipEvent({ [VIEWER_HEADER]: value } as any)), {
            ip: EDGE_IP,
            source: "edge",
        });
    }
    assert.deepStrictEqual(clientAddress({}), { ip: undefined, source: "unknown" });
});

test("never throws, whatever the headers hold", () => {
    // This feeds the success-path log, which runs after the Intercom ticket
    // already exists. A throw there would 502 a request that had filed, and the
    // user would resubmit into a duplicate.
    for (const headers of [{}, { [VIEWER_HEADER]: null }, { [VIEWER_HEADER]: {} }]) {
        assert.doesNotThrow(() => clientAddress(ipEvent(headers as any)));
    }
});

test("logs the viewer address and its provenance on an accepted submission", async () => {
    process.env.SUPPORT_FORM_ORIGIN_SECRET = SECRET;
    const logged: string[] = [];
    const realLog = console.log;
    console.log = (msg?: any) => {
        logged.push(String(msg));
    };
    try {
        const event = postEvent(validPayload());
        (event.headers as Record<string, string>)[VIEWER_HEADER] = `${VIEWER_IP}:52001`;
        (event.headers as Record<string, string>)["x-forwarded-for"] = "1.2.3.4";
        await supportFormHandler(event);
    } finally {
        console.log = realLog;
    }
    const accepted = logged.map(l => JSON.parse(l)).find(l => l.type === "support_request_accepted");
    assert.ok(accepted, "expected a support_request_accepted record");
    assert.strictEqual(accepted.sourceIp, VIEWER_IP);
    assert.strictEqual(accepted.ipSource, "viewer");
});

test("handler rejects an empty body", async () => {
    process.env.SUPPORT_FORM_ORIGIN_SECRET = SECRET;
    const event = postEvent(validPayload());
    event.body = "";
    const response = await supportFormHandler(event);
    assert.strictEqual(response.statusCode, 400);
    assert.strictEqual(JSON.parse(response.body).error, "empty_body");
});

test("handler returns field errors as a 422", async () => {
    process.env.SUPPORT_FORM_ORIGIN_SECRET = SECRET;
    const before = intercomCalls.length;
    const response = await supportFormHandler(postEvent({ ...validPayload(), email: "nope" }));
    assert.strictEqual(response.statusCode, 422);
    const parsed = JSON.parse(response.body);
    assert.strictEqual(parsed.error, "validation_failed");
    assert.ok(parsed.fields.email);
    // A submission that failed validation must never reach Intercom.
    assert.strictEqual(intercomCalls.length, before);
});

test("handler reports a ticket-creation failure as a 502", async () => {
    process.env.SUPPORT_FORM_ORIGIN_SECRET = SECRET;
    intercomUp = false;
    try {
        const response = await supportFormHandler(postEvent(validPayload()));
        assert.strictEqual(response.statusCode, 502);
        const parsed = JSON.parse(response.body);
        assert.strictEqual(parsed.ok, false);
        assert.strictEqual(parsed.error, "ticket_creation_failed");
        // The id still comes back so a failed submission can be traced to its
        // support_request_ticket_failed log entry.
        assert.ok(parsed.id);
    } finally {
        intercomUp = true;
    }
});

test("handler swallows honeypot submissions with a fake success", async () => {
    process.env.SUPPORT_FORM_ORIGIN_SECRET = SECRET;
    const before = intercomCalls.length;
    const response = await supportFormHandler(postEvent({ ...validPayload(), website: "https://spam.example" }));
    assert.strictEqual(response.statusCode, 200);
    const parsed = JSON.parse(response.body);
    assert.strictEqual(parsed.ok, true);
    // The whole point of the honeypot: it looks like success to the bot but
    // files nothing. The absent ticketId is what distinguishes it from a real
    // acceptance.
    assert.strictEqual(intercomCalls.length, before);
    assert.strictEqual(parsed.ticketId, undefined);
});

// --- The validation -> side-effect boundary -------------------------------
//
// Every other handler test posts an already-normalized validPayload(), so the
// normalization is a no-op in them and nothing notices which object crosses
// into the Intercom client. Posting a value that normalization actually
// changes is what makes the difference observable.

test("handler files the validated value, not the caller's raw payload", async () => {
    process.env.SUPPORT_FORM_ORIGIN_SECRET = SECRET;
    const before = intercomRequests.length;

    const response = await supportFormHandler(postEvent({
        ...validPayload(),
        organization: "https://app.pulumi.com/example-corp/stacks/dev",
    }));
    assert.strictEqual(response.statusCode, 200);

    const ticket = intercomRequests.slice(before).find(r => r.url.endsWith("/tickets"));
    assert.ok(ticket, "expected a ticket to be filed");
    assert.strictEqual(ticket!.body.ticket_attributes["pulumi-org"], "example-corp");
});

test("handler does not forward the honeypot key to Intercom", async () => {
    process.env.SUPPORT_FORM_ORIGIN_SECRET = SECRET;
    const before = intercomRequests.length;

    // An empty honeypot is not spam, so this is accepted and filed -- but the
    // key is not part of the ticket.
    const response = await supportFormHandler(postEvent({ ...validPayload(), website: "" }));
    assert.strictEqual(response.statusCode, 200);

    const ticket = intercomRequests.slice(before).find(r => r.url.endsWith("/tickets"));
    assert.ok(ticket, "expected a ticket to be filed");
    assert.ok(!JSON.stringify(ticket!.body).includes("website"));
});

// --- The 403 gate --------------------------------------------------------

test("the origin-secret gate cannot be swayed by anything in the body", async () => {
    process.env.SUPPORT_FORM_ORIGIN_SECRET = SECRET;

    // The realistic regression here is not "the check was deleted" -- that is
    // already covered -- but "someone added an escape hatch for an internal
    // caller". Any such hatch is derived from the payload, so the gate has to
    // be proven independent of it rather than tested at one body shape.
    const bodies: unknown[] = [
        validPayload(),
        { ...validPayload(), website: "spam" },
        { website: "x" },
        {},
        [],
        "",
        "{not json",
        "x".repeat(256 * 1024 + 1),
    ];

    for (const body of bodies) {
        const event = postEvent(body);
        delete event.headers!["x-origin-verify"];
        const response = await supportFormHandler(event);
        assert.strictEqual(
            response.statusCode, 403,
            `a request without the origin secret must be refused whatever the body holds (${JSON.stringify(body).slice(0, 40)})`);
    }
});

// --- Length caps ---------------------------------------------------------

test("enforces every length cap at its exact documented boundary", () => {
    // Literal boundaries on purpose. Writing these as LIMITS.foo + 1 pins the
    // shape of the rule but not its value, so the cap could be raised to
    // anything and the test would follow it up.
    const domain = "@example.com";
    const atLimit: Record<string, string> = {
        email: "a".repeat(254 - domain.length) + domain,
        name: "a".repeat(200),
        organization: "a".repeat(40),
        subject: "a".repeat(200),
        description: "a".repeat(20000),
    };
    const overLimit: Record<string, string> = {
        email: "a".repeat(255 - domain.length) + domain,
        name: "a".repeat(201),
        organization: "a".repeat(41),
        subject: "a".repeat(201),
        description: "a".repeat(20001),
    };

    for (const field of Object.keys(atLimit)) {
        const ok = validateSubmission({ ...validPayload(), [field]: atLimit[field] });
        assert.ok(ok.ok, `${field} at its limit must be accepted`);

        const tooLong = validateSubmission({ ...validPayload(), [field]: overLimit[field] });
        assert.ok(!tooLong.ok, `${field} one character over its limit must be rejected`);
        if (!tooLong.ok) {
            assert.ok(tooLong.fields[field], `expected the error to be reported against ${field}`);
        }
    }
});

test("pins the published limits, which /llms.txt documents to agents", () => {
    assert.deepStrictEqual(LIMITS, {
        email: 254,
        name: 200,
        organization: 40,
        subject: 200,
        descriptionMin: 10,
        description: 20000,
    });
});

// --- The accepted-key set ------------------------------------------------

test("pins the accepted top-level keys", () => {
    // A "rejects an unknown key" test cannot see the way this actually erodes,
    // which is a key being added to the allowlist.
    assert.deepStrictEqual(KNOWN_KEYS, [
        "email",
        "name",
        "organization",
        "priority",
        "subject",
        "description",
        "website",
    ]);
});

test("rejects payloads that are not JSON objects", () => {
    for (const input of [[], [validPayload()], null, "a string", 42, true]) {
        const result = validateSubmission(input);
        assert.ok(!result.ok, `expected ${JSON.stringify(input)} to be rejected`);
        if (!result.ok) {
            assert.ok(result.fields._form, "a payload-level problem is reported against _form");
        }
    }
});

// --- Header normalization ------------------------------------------------

test("matches the method and content type case-insensitively", async () => {
    process.env.SUPPORT_FORM_ORIGIN_SECRET = SECRET;

    const lowercaseMethod = postEvent(validPayload());
    lowercaseMethod.requestContext!.http!.method = "post";
    assert.strictEqual((await supportFormHandler(lowercaseMethod)).statusCode, 200);

    const mixedContentType = postEvent(validPayload());
    mixedContentType.headers!["content-type"] = "Application/JSON; charset=utf-8";
    assert.strictEqual((await supportFormHandler(mixedContentType)).statusCode, 200);
});

// --- Normalization details -----------------------------------------------

test("normalizes the remaining console-URL shapes", () => {
    assert.strictEqual(normalizeOrganization("/example-corp"), "example-corp");
    assert.strictEqual(normalizeOrganization("https://www.app.pulumi.com/example-corp"), "example-corp");
    assert.strictEqual(normalizeOrganization("www.app.pulumi.com/example-corp"), "example-corp");
});

test("trims surrounding whitespace on every string field", () => {
    const result = validateSubmission({
        ...validPayload(),
        email: "  jane@example.com  ",
        subject: "  Stack update stuck in progress  ",
    });
    assert.ok(result.ok);
    if (result.ok) {
        assert.strictEqual(result.value.email, "jane@example.com");
        assert.strictEqual(result.value.subject, "Stack update stuck in progress");
    }
});

// --- Viewer-address shapes -----------------------------------------------

test("reads bracketed and portless viewer addresses", () => {
    // RFC 3986 bracketing, so an address is logged in one queryable form.
    assert.deepStrictEqual(
        clientAddress(ipEvent({ [VIEWER_HEADER]: "[2001:db8::1]:443" })),
        { ip: "2001:db8::1", source: "viewer" });

    // No port: the trailing group is not numeric, so it must not be mistaken
    // for one and trimmed away.
    assert.deepStrictEqual(
        clientAddress(ipEvent({ [VIEWER_HEADER]: "2001:db8::abc" })),
        { ip: "2001:db8::abc", source: "viewer" });

    assert.deepStrictEqual(
        clientAddress(ipEvent({ [VIEWER_HEADER]: "198.51.100.9" })),
        { ip: "198.51.100.9", source: "viewer" });
});
