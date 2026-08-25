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

// Longest value accepted from x-viewer-ip. An IPv6 address with a zone index
// fits comfortably; anything longer is not an address we stamped.
const MAX_IP_LENGTH = 64;

// The submitter's IP address, for the abuse trail in the logs below.
//
// requestContext.http.sourceIp is NOT it: CloudFront invokes the Function URL,
// so that field is always the edge node's address (a 3.x CLOUDFRONT_ORIGIN_FACING
// IP), identical in shape for every submission and useless for tracing anyone.
//
// X-Forwarded-For is not the answer either, and this is the trap worth naming.
// CloudFront *appends* the viewer to whatever X-Forwarded-For the viewer already
// sent, so the header is partly attacker-authored by the time it leaves the
// edge; and Lambda Function URLs are documented to truncate it to the leftmost
// value, which is precisely the part the attacker controls. Reading it would log
// a forged address that looks authentic — worse than logging the edge.
//
// So the address is stamped at the edge instead: a CloudFront Function writes
// event.viewer.ip (CloudFront's own view of the TCP peer, unforgeable, and
// overwriting anything the client sent) into x-viewer-ip. See
// getViewerIpFunctionAssociation in ../cloudfrontFunctions.ts.
//
// Trusting that header is only sound because the caller already proved it came
// through our distribution: supportFormHandler rejects anything without the
// x-origin-verify shared secret before this is ever called. On a direct Function
// URL invocation there is no valid secret, so we never reach here — and the
// requestContext fallback below is the honest AWS-supplied peer anyway.
export function clientIp(event: FunctionUrlEvent): string | undefined {
    const stamped = event.headers?.["x-viewer-ip"];
    if (typeof stamped === "string") {
        const value = stamped.trim();
        if (value.length > 0 && value.length <= MAX_IP_LENGTH) {
            return value;
        }
    }
    return event.requestContext?.http?.sourceIp;
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
                sourceIp: clientIp(event),
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
                sourceIp: clientIp(event),
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
            sourceIp: clientIp(event),
            request: result.value,
        }),
    );

    return jsonResponse(200, { ok: true, id, ticketId });
}
