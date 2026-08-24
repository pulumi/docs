// Copyright 2016-2026, Pulumi Corporation.  All rights reserved.

// Intercom API client for filing support tickets from accepted submissions.
// Split out from handler.ts so the network-calling code stays separate from
// request/response plumbing; createSupportTicket is the only export handler.ts
// needs.

import type { SupportRequest } from "./validation";

const INTERCOM_API_BASE = "https://api.intercom.io";
const INTERCOM_VERSION = "2.11";

function intercomHeaders(): Record<string, string> {
    return {
        Authorization: `Bearer ${process.env.INTERCOM_API_KEY}`,
        "Content-Type": "application/json",
        "Intercom-Version": INTERCOM_VERSION,
    };
}

async function findContactByEmail(email: string): Promise<string | undefined> {
    const res = await fetch(`${INTERCOM_API_BASE}/contacts/search`, {
        method: "POST",
        headers: intercomHeaders(),
        body: JSON.stringify({
            query: { field: "email", operator: "=", value: email },
        }),
    });
    if (!res.ok) {
        throw new Error(`Intercom contact search failed: ${res.status} ${await res.text()}`);
    }
    const data = (await res.json()) as { data: Array<{ id: string }> };
    return data.data[0]?.id;
}

async function createContact(email: string, name: string): Promise<string> {
    const res = await fetch(`${INTERCOM_API_BASE}/contacts`, {
        method: "POST",
        headers: intercomHeaders(),
        body: JSON.stringify({ role: "lead", email, name }),
    });
    if (!res.ok) {
        throw new Error(`Intercom contact create failed: ${res.status} ${await res.text()}`);
    }
    const contact = (await res.json()) as { id: string };
    return contact.id;
}

async function createTicket(contactId: string, request: SupportRequest): Promise<string> {
    const res = await fetch(`${INTERCOM_API_BASE}/tickets`, {
        method: "POST",
        headers: intercomHeaders(),
        body: JSON.stringify({
            ticket_type_id: process.env.INTERCOM_TICKET_TYPE_ID,
            contacts: [{ id: contactId }],
            ticket_attributes: {
                _default_title_: request.subject,
                _default_description_: request.description,
                "pulumi-org": request.organization,
                priority: request.priority,
            },
        }),
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
