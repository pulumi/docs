// Copyright 2016-2026, Pulumi Corporation.  All rights reserved.

// Lambda handler for POST /api/support — the support-request form endpoint.
//
// The function sits behind a Lambda Function URL that is only reachable (in
// practice) through the www.pulumi.com CloudFront distribution, which injects
// a shared-secret x-origin-verify header at the origin (see supportForm.ts).
// Requests without the secret are rejected, so the public Function URL can't
// be used to bypass the CDN's WAF and rate limiting.
//
// The Intercom integration is stubbed: accepted submissions are written to
// CloudWatch Logs as single-line JSON documents (type
// "support_request_accepted") where they can be observed and, later, replayed
// against the real ticket API.

import * as crypto from "crypto";
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
                sourceIp: event.requestContext?.http?.sourceIp,
            }),
        );
        return jsonResponse(200, { ok: true, id: crypto.randomUUID() });
    }

    const result = validateSubmission(parsed);
    if (!result.ok) {
        return jsonResponse(422, { ok: false, error: "validation_failed", fields: result.fields });
    }

    const id = crypto.randomUUID();

    // Observability stub: one JSON document per accepted submission, queryable
    // in CloudWatch Logs Insights via { $.type = "support_request_accepted" }.
    console.log(
        JSON.stringify({
            type: "support_request_accepted",
            id,
            receivedAt: new Date().toISOString(),
            sourceIp: event.requestContext?.http?.sourceIp,
            request: result.value,
        }),
    );

    // TODO(intercom): replace the log line above with a ticket-create call to
    // the Intercom API once its spec is available. The API key arrives as a
    // stack secret surfaced through another environment variable — never in
    // this repo or the frontend.

    return jsonResponse(200, { ok: true, id });
}
