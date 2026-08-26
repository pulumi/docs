// Copyright 2016-2026, Pulumi Corporation.  All rights reserved.

// Intercom API client for filing support tickets from accepted submissions.
// Split out from handler.ts so the network-calling code stays separate from
// request/response plumbing; createSupportTicket is the only export handler.ts
// needs.

import type { SupportRequest } from "./validation";

const INTERCOM_API_BASE = "https://api.intercom.io";
const INTERCOM_VERSION = "2.11";

// Per-call ceiling. Three sequential calls run inside the Lambda's own timeout,
// and a bare fetch has none of its own: if Intercom stops responding, the
// function is killed by the runtime instead of returning. That matters because
// the kill happens outside the handler's try/catch, so the caller gets the
// runtime's 502 rather than the documented {ok:false,error:"ticket_creation_failed",id}
// envelope, and support_request_ticket_failed is never logged -- a contact can
// be created with no ticket and no trace of it. Bounding each call keeps the
// failure inside the handler, where it is shaped and recorded.
const INTERCOM_TIMEOUT_MS = 2500;

function intercomFetch(url: string, body: object): Promise<Response> {
    return fetch(url, {
        method: "POST",
        headers: intercomHeaders(),
        body: JSON.stringify(body),
        signal: AbortSignal.timeout(INTERCOM_TIMEOUT_MS),
    });
}

function intercomHeaders(): Record<string, string> {
    return {
        Authorization: `Bearer ${process.env.INTERCOM_API_KEY}`,
        "Content-Type": "application/json",
        "Intercom-Version": INTERCOM_VERSION,
    };
}

async function findContactByEmail(email: string): Promise<string | undefined> {
    const res = await intercomFetch(`${INTERCOM_API_BASE}/contacts/search`, {
        query: { field: "email", operator: "=", value: email },
    });
    if (!res.ok) {
        throw new Error(`Intercom contact search failed: ${res.status} ${await res.text()}`);
    }
    const data = (await res.json()) as { data: Array<{ id: string }> };
    return data.data[0]?.id;
}

async function createContact(email: string, name: string): Promise<string> {
    const res = await intercomFetch(`${INTERCOM_API_BASE}/contacts`, { role: "lead", email, name });
    if (!res.ok) {
        throw new Error(`Intercom contact create failed: ${res.status} ${await res.text()}`);
    }
    const contact = (await res.json()) as { id: string };
    return contact.id;
}

async function createTicket(contactId: string, request: SupportRequest): Promise<string> {
    const res = await intercomFetch(`${INTERCOM_API_BASE}/tickets`, {
        ticket_type_id: process.env.INTERCOM_TICKET_TYPE_ID,
        contacts: [{ id: contactId }],
        ticket_attributes: {
            _default_title_: request.subject,
            _default_description_: request.description,
            "pulumi-org": request.organization,
            priority: request.priority,
        },
    });
    if (!res.ok) {
        throw new Error(`Intercom ticket create failed: ${res.status} ${await res.text()}`);
    }
    const ticket = (await res.json()) as { id: string };
    return ticket.id;
}

// createSupportTicket finds or creates the submitter's Intercom contact, then
// files a ticket against it. Throws on any Intercom API failure; the caller
// (handler.ts) is responsible for turning that into a response.
export async function createSupportTicket(request: SupportRequest): Promise<string> {
    let contactId = await findContactByEmail(request.email);
    if (!contactId) {
        contactId = await createContact(request.email, request.name);
    }
    return createTicket(contactId, request);
}
