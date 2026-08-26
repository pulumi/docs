// Copyright 2016-2026, Pulumi Corporation.  All rights reserved.

// Unit tests for the Intercom ticket-filing client. The Intercom API is
// replaced with an in-process fake bound to globalThis.fetch: intercom.ts calls
// the global directly, so the module needs no injection seam and nothing about
// what handler.ts serializes into the Lambda changes. Run from the
// infrastructure directory with:
//
//     yarn test-support-form

import * as assert from "assert";
import { test } from "node:test";

import { createSupportTicket } from "./intercom";
import { SupportRequest } from "./validation";

process.env.INTERCOM_API_KEY = "test-key";
process.env.INTERCOM_TICKET_TYPE_ID = "ticket-type-1";

interface IntercomCall {
    url: string;
    method: string;
    headers: Record<string, string>;
    body: any;
}

const request: SupportRequest = {
    email: "jane@example.com",
    name: "Jane Doe",
    organization: "example-corp",
    priority: "normal",
    subject: "Stack update stuck in progress",
    description: "Running `pulumi up` hangs after the preview completes.",
};

// Installs a fake Intercom API and returns both the calls it received and a
// restore function, so one test's fake can't leak into the next. failingPath
// makes one leg reject, which is how the throw-on-error paths are exercised.
function fakeIntercom(options: { existingContactId?: string; failingPath?: string } = {}) {
    const calls: IntercomCall[] = [];
    const realFetch = globalThis.fetch;

    globalThis.fetch = async (input, init) => {
        const url = String(input);
        calls.push({
            url,
            method: (init && init.method) || "GET",
            headers: ((init && init.headers) || {}) as Record<string, string>,
            body: init && init.body ? JSON.parse(init.body as string) : undefined,
        });

        if (options.failingPath && url.endsWith(options.failingPath)) {
            return new Response("bad request", { status: 400 });
        }
        if (url.endsWith("/contacts/search")) {
            return new Response(
                JSON.stringify({ data: options.existingContactId ? [{ id: options.existingContactId }] : [] }),
                { status: 200 },
            );
        }
        if (url.endsWith("/contacts")) {
            return new Response(JSON.stringify({ id: "contact-created" }), { status: 200 });
        }
        if (url.endsWith("/tickets")) {
            return new Response(JSON.stringify({ id: "ticket-42" }), { status: 200 });
        }
        throw new Error(`unexpected request to ${url}`);
    };

    return {
        calls,
        restore: () => {
            globalThis.fetch = realFetch;
        },
    };
}

test("files a ticket against an existing contact", async t => {
    const fake = fakeIntercom({ existingContactId: "contact-1" });
    t.after(fake.restore);

    assert.strictEqual(await createSupportTicket(request), "ticket-42");
    assert.deepStrictEqual(
        fake.calls.map(c => c.url),
        ["https://api.intercom.io/contacts/search", "https://api.intercom.io/tickets"],
    );
    assert.deepStrictEqual(fake.calls[0].body.query, { field: "email", operator: "=", value: request.email });
    assert.deepStrictEqual(fake.calls[1].body.contacts, [{ id: "contact-1" }]);
});

test("creates a contact when the submitter is unknown to Intercom", async t => {
    const fake = fakeIntercom();
    t.after(fake.restore);

    await createSupportTicket(request);

    assert.deepStrictEqual(
        fake.calls.map(c => c.url),
        [
            "https://api.intercom.io/contacts/search",
            "https://api.intercom.io/contacts",
            "https://api.intercom.io/tickets",
        ],
    );
    assert.deepStrictEqual(fake.calls[1].body, { role: "lead", email: request.email, name: request.name });
    assert.deepStrictEqual(fake.calls[2].body.contacts, [{ id: "contact-created" }]);
});

test("sends the validated submission as ticket attributes", async t => {
    const fake = fakeIntercom({ existingContactId: "contact-1" });
    t.after(fake.restore);

    await createSupportTicket(request);

    const ticket = fake.calls[fake.calls.length - 1];
    assert.strictEqual(ticket.method, "POST");
    assert.strictEqual(ticket.headers.Authorization, "Bearer test-key");
    assert.strictEqual(ticket.headers["Intercom-Version"], "2.11");
    assert.strictEqual(ticket.body.ticket_type_id, "ticket-type-1");
    assert.deepStrictEqual(ticket.body.ticket_attributes, {
        _default_title_: request.subject,
        _default_description_: request.description,
        "pulumi-org": request.organization,
        priority: request.priority,
    });
});

// handler.ts turns any throw from here into a 502, so each leg has to throw
// rather than resolve with a partial result. "/contacts/search" does not end
// with "/contacts", so the middle case really does exercise the create leg.
for (const failingPath of ["/contacts/search", "/contacts", "/tickets"]) {
    test(`throws when Intercom rejects ${failingPath}`, async t => {
        const fake = fakeIntercom({ failingPath });
        t.after(fake.restore);
        await assert.rejects(createSupportTicket(request), /Intercom/);
    });
}
