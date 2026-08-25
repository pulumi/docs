// Copyright 2016-2026, Pulumi Corporation.  All rights reserved.

// Lambda handler for POST /api/support — the support-request form endpoint.
//
// The function sits behind a Lambda Function URL that is only reachable (in
// practice) through the www.pulumi.com CloudFront distribution, which injects
// a shared-secret x-origin-verify header at the origin (see supportForm.ts).
// Requests without the secret are rejected, so the public Function URL can't
// be used to bypass the CDN's WAF and rate limiting.
//
// Accepted submissions are filed as Intercom tickets (see ./intercom.ts) and,
// either way, written to CloudWatch Logs as single-line JSON documents (type
// "support_request_accepted" or "support_request_ticket_failed") for
// observability.

import * as crypto from "crypto";
import { createSupportTicket } from "./intercom";
import { MAX_BODY_BYTES, validateSubmission } from "./validation";

// Function URLs invoke with the API Gateway v2 payload shape. Only the pieces
// used here are typed, so the closure doesn't drag in @types/aws-lambda at
// runtime.
export interface FunctionUrlEvent {
    body?: string;
    isBase64Encoded?: boolean;
    headers?: Record<string, string | undefined>;
    requestContext?: {
        http?: {
            method?: string;
            path?: string;
            sourceIp?: string;
        };
    };
}

export interface FunctionUrlResult {
    statusCode: number;
    headers: Record<string, string>;
    body: string;
}

// Longest value accepted from CloudFront-Viewer-Address. An IPv6 address plus a
// port fits comfortably; anything longer is not an address CloudFront set.
const MAX_ADDRESS_LENGTH = 64;

// Where a logged address came from. Recorded alongside the address itself
// because the two sources mean very different things, and a record that
// silently mixed them would be worse than no record: "edge" is not the
// submitter, and must never be read as though it were.
export type IpSource = "viewer" | "edge" | "unknown";

export interface ClientAddress {
    ip: string | undefined;
    source: IpSource;
}

// The submitter's IP address, for the abuse trail in the logs below.
//
// requestContext.http.sourceIp is NOT it: CloudFront invokes the Function URL,
// so that field is the edge node's address (a 3.x CLOUDFRONT_ORIGIN_FACING IP),
// identical in shape for every submission and useless for tracing anyone.
//
// X-Forwarded-For is not the answer either. CloudFront appends the viewer to
// whatever X-Forwarded-For the caller already sent, so the header is partly
// caller-authored by the time it leaves the edge, and reading the wrong end of
// it logs a forged address that looks authentic. (A Function URL may also
// collapse the chain before the handler sees it; we could not find that
// documented either way, which is reason enough not to depend on the shape.)
//
// CloudFront-Viewer-Address avoids all of it. CloudFront sets it from the TCP
// connection and overwrites anything the client sent, so it cannot be forged,
// and it is forwarded by the origin request policy rather than produced by edge
// code that could fail. Trusting it is sound because the caller already proved
// the request came through our distribution: supportFormHandler rejects anything
// without the x-origin-verify shared secret before this is ever called.
//
// The value is "<ip>:<port>" and is IPv6-capable ("2001:db8::1:443"), so the
// address is everything before the LAST colon.
export function clientAddress(event: FunctionUrlEvent): ClientAddress {
    const forwarded = event.headers?.["cloudfront-viewer-address"];
    if (typeof forwarded === "string") {
        const value = forwarded.trim();
        if (value.length > 0 && value.length <= MAX_ADDRESS_LENGTH) {
            const lastColon = value.lastIndexOf(":");
            const ip = lastColon === -1 ? value : value.slice(0, lastColon);
            if (ip.length > 0) {
                return { ip, source: "viewer" };
            }
        }
    }
    // No viewer address: either the origin request policy is not forwarding it
    // (a misconfiguration, or mid-deploy propagation) or this is a direct
    // Function URL invocation, where sourceIp really is the caller's own peer.
    const peer = event.requestContext?.http?.sourceIp;
    return { ip: peer, source: peer ? "edge" : "unknown" };
}

function jsonResponse(statusCode: number, body: object, extraHeaders: Record<string, string> = {}): FunctionUrlResult {
    return {
        statusCode,
        headers: {
            "content-type": "application/json",
            "cache-control": "no-store",
            ...extraHeaders,
        },
        body: JSON.stringify(body),
    };
}

// The env var holds a comma-separated list so a rotation can accept both the
// old and new secret while the CloudFront origin-header change propagates.
function originSecretOk(header: string | undefined): boolean {
    const configured = process.env.SUPPORT_FORM_ORIGIN_SECRET;
    if (!configured) {
        // Fail closed if the function is somehow deployed without its secret.
        return false;
    }
    if (!header) {
        return false;
    }
    return configured
        .split(",")
        .map(s => s.trim())
        .filter(s => s.length > 0)
        .some(secret => secret === header);
}

export async function supportFormHandler(event: FunctionUrlEvent): Promise<FunctionUrlResult> {
    const headers = event.headers || {};

    if (!originSecretOk(headers["x-origin-verify"])) {
        return jsonResponse(403, { ok: false, error: "forbidden" });
    }

    // Resolved once, and deliberately only after the secret check: the viewer
    // address is trustworthy precisely because CloudFront vouched for this
    // request. Computed here rather than at each log site so the success path,
    // which runs after the Intercom ticket already exists, cannot fail on it.
    const address = clientAddress(event);

    const method = (event.requestContext?.http?.method || "").toUpperCase();
    if (method !== "POST") {
        return jsonResponse(405, { ok: false, error: "method_not_allowed" }, { allow: "POST" });
    }

    const contentType = (headers["content-type"] || "").toLowerCase();
    if (!contentType.startsWith("application/json")) {
        return jsonResponse(400, { ok: false, error: "unsupported_content_type" });
    }

    if (!event.body) {
        return jsonResponse(400, { ok: false, error: "empty_body" });
    }
    const rawBody = event.isBase64Encoded ? Buffer.from(event.body, "base64").toString("utf8") : event.body;
    if (Buffer.byteLength(rawBody, "utf8") > MAX_BODY_BYTES) {
        return jsonResponse(413, { ok: false, error: "payload_too_large" });
    }

    let parsed: unknown;
    try {
        parsed = JSON.parse(rawBody);
    } catch (err) {
        return jsonResponse(400, { ok: false, error: "invalid_json" });
    }

    // Honeypot: the "website" field is visually hidden on the form, so any
    // value in it marks a bot. Pretend success so the bot moves on.
    if (typeof parsed === "object" && parsed !== null && (parsed as Record<string, unknown>).website) {
        console.log(
            JSON.stringify({
                type: "support_request_spam_dropped",
                receivedAt: new Date().toISOString(),
                sourceIp: address.ip,
                ipSource: address.source,
            }),
        );
        return jsonResponse(200, { ok: true, id: crypto.randomUUID() });
    }

    const result = validateSubmission(parsed);
    if (!result.ok) {
        return jsonResponse(422, { ok: false, error: "validation_failed", fields: result.fields });
    }

    const id = crypto.randomUUID();

    let ticketId: string;
    try {
        ticketId = await createSupportTicket(result.value);
    } catch (err) {
        console.error(
            JSON.stringify({
                type: "support_request_ticket_failed",
                id,
                error: err instanceof Error ? err.message : String(err),
                sourceIp: address.ip,
                ipSource: address.source,
                request: result.value,
            }),
        );
        return jsonResponse(502, { ok: false, error: "ticket_creation_failed", id });
    }

    // One JSON document per accepted submission, queryable in CloudWatch Logs
    // Insights via { $.type = "support_request_accepted" }.
    console.log(
        JSON.stringify({
            type: "support_request_accepted",
            id,
            ticketId,
            receivedAt: new Date().toISOString(),
            sourceIp: address.ip,
            ipSource: address.source,
            request: result.value,
        }),
    );

    return jsonResponse(200, { ok: true, id, ticketId });
}
