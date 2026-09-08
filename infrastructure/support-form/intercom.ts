// Copyright 2016-2026, Pulumi Corporation.  All rights reserved.

// Intercom API client for filing support conversations from accepted
// submissions. Split out from handler.ts so the network-calling code stays
// separate from request/response plumbing; createSupportConversation is the
// only export handler.ts needs.

import type { SupportRequest } from "./validation";

const INTERCOM_API_BASE = "https://api.intercom.io";
const INTERCOM_VERSION = "2.13";

// Per-call ceiling. Up to four sequential calls run inside the Lambda's own
// timeout (find-or-create contact, create the conversation, then set its
// custom attributes -- custom_attributes isn't accepted on creation, only via
// a follow-up PUT), and a bare fetch has none of its own: if Intercom stops
// responding, the function is killed by the runtime instead of returning.
// That matters because the kill happens outside the handler's try/catch, so
// the caller gets the runtime's 502 rather than the documented
// {ok:false,error:"conversation_creation_failed",id} envelope, and
// support_request_conversation_failed is never logged -- a contact can be
// created with no conversation and no trace of it. Bounding each call keeps
// the failure inside the handler, where it is shaped and recorded. 4 * 2000ms
// leaves 2s of the Lambda's 10s timeout for everything else in the handler.
const INTERCOM_TIMEOUT_MS = 2000;

function intercomFetch(url: string, body: object, method: "POST" | "PUT" = "POST"): Promise<Response> {
    return fetch(url, {
        method,
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

// Conversations don't take structured attributes at creation -- only a
// contact ("from") and a message body -- so subject and description (the two
// fields with nowhere else to go) are folded into the body text.
async function createConversation(contactId: string, request: SupportRequest): Promise<string> {
    const res = await intercomFetch(`${INTERCOM_API_BASE}/conversations`, {
        from: { type: "user", id: contactId },
        body: `${request.subject}\n\n${request.description}`,
    });
    if (!res.ok) {
        throw new Error(`Intercom conversation create failed: ${res.status} ${await res.text()}`);
    }
    // The response is the created message, not the conversation itself --
    // the conversation's own id is nested in conversation_id.
    const message = (await res.json()) as { conversation_id: string };
    return message.conversation_id;
}

// custom_attributes is rejected on POST /conversations; it only takes effect
// through a follow-up PUT against the conversation it just created.
async function setConversationAttributes(conversationId: string, request: SupportRequest): Promise<void> {
    const res = await intercomFetch(
        `${INTERCOM_API_BASE}/conversations/${conversationId}`,
        {
            custom_attributes: {
                "pulumi-org": request.organization,
                priority: request.priority,
            },
        },
        "PUT",
    );
    if (!res.ok) {
        throw new Error(`Intercom conversation attributes update failed: ${res.status} ${await res.text()}`);
    }
}

// createSupportConversation finds or creates the submitter's Intercom
// contact, then files a conversation against it. Throws on any Intercom API
// failure; the caller (handler.ts) is responsible for turning that into a
// response.
export async function createSupportConversation(request: SupportRequest): Promise<string> {
    let contactId = await findContactByEmail(request.email);
    if (!contactId) {
        contactId = await createContact(request.email, request.name);
    }
    const conversationId = await createConversation(contactId, request);
    await setConversationAttributes(conversationId, request);
    return conversationId;
}
