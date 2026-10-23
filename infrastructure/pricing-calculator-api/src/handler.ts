// Copyright 2016-2026, Pulumi Corporation.  All rights reserved.

// Lambda handler for the pricing estimate endpoint. Accepts the usage either as
// query parameters on a GET or as a JSON body on a POST, with the same field
// names in both:
//
//     GET /?edition=essentials&iac_resources=1000
//     POST / {"edition": "pro", "unit": "hour", "iac_resources": 1460000}
//
// Fields: edition (essentials | pro | enterprise, or whatever editions the
// deployed rates list; required), unit (month |
// hour, default month), iac_resources, esc_secrets, workflow_minutes,
// neo_million_tokens, insights_resources (non-negative numbers, default 0).
//
// It's pure computation with no secrets or side effects, so unlike
// support-form/handler.ts there's no origin check.

import { DEFAULT_RATES, estimate, PricingRates, RateUnit, Usage } from "./pricing";

export interface FunctionUrlEvent {
    body?: string;
    isBase64Encoded?: boolean;
    headers?: Record<string, string | undefined>;
    queryStringParameters?: Record<string, string | undefined>;
    requestContext?: {
        http?: {
            method?: string;
        };
    };
}

export interface FunctionUrlResult {
    statusCode: number;
    headers: Record<string, string>;
    body: string;
}

export const MAX_BODY_BYTES = 4096;

const QUANTITY_FIELDS = {
    iac_resources: "iacResources",
    esc_secrets: "escSecrets",
    workflow_minutes: "workflowMinutes",
    neo_million_tokens: "neoMillionTokens",
    insights_resources: "insightsResources",
} as const;

// A plain array, not a Set: the handler is shipped through Pulumi's closure
// serialization (aws.lambda.CallbackFunction), which doesn't preserve Set
// instances. handler.test.ts runs the serialized handler to catch this.
const KNOWN_KEYS = ["edition", "unit", ...Object.keys(QUANTITY_FIELDS)];

type Parsed = { ok: true; usage: Usage } | { ok: false; fields: Record<string, string> };

// The deploy passes the rates it chose (live or built-in; see index.ts) as
// JSON. Read on every call rather than at module load, since the closure is
// serialized at deploy time.
export function ratesFromEnv(env: Record<string, string | undefined> = process.env): PricingRates {
    const raw = env.PRICING_RATES;
    if (!raw) {
        return DEFAULT_RATES;
    }
    try {
        return JSON.parse(raw) as PricingRates;
    } catch (err) {
        console.error(JSON.stringify({ type: "pricing_rates_invalid", error: String(err) }));
        return DEFAULT_RATES;
    }
}

export function parseUsage(input: Record<string, unknown>, rates: PricingRates = DEFAULT_RATES): Parsed {
    const fields: Record<string, string> = {};

    for (const key of Object.keys(input)) {
        if (!KNOWN_KEYS.includes(key)) {
            fields[key] = "unknown field";
        }
    }

    const edition = input.edition;
    if (typeof edition !== "string" || !Object.prototype.hasOwnProperty.call(rates.editions, edition)) {
        fields.edition = `must be one of ${Object.keys(rates.editions).join(", ")}`;
    }

    const unit = input.unit === undefined ? "month" : input.unit;
    if (unit !== "month" && unit !== "hour") {
        fields.unit = "must be month or hour";
    }

    const quantities: Record<string, number> = {};
    for (const [key, prop] of Object.entries(QUANTITY_FIELDS)) {
        const raw = input[key];
        if (raw === undefined || raw === "") {
            quantities[prop] = 0;
            continue;
        }
        const n = typeof raw === "string" ? Number(raw) : raw;
        if (typeof n !== "number" || !Number.isFinite(n) || n < 0) {
            fields[key] = "must be a non-negative number";
            continue;
        }
        quantities[prop] = n;
    }

    if (Object.keys(fields).length > 0) {
        return { ok: false, fields };
    }
    return {
        ok: true,
        usage: {
            edition: edition as string,
            unit: unit as RateUnit,
            iacResources: quantities.iacResources,
            escSecrets: quantities.escSecrets,
            workflowMinutes: quantities.workflowMinutes,
            neoMillionTokens: quantities.neoMillionTokens,
            insightsResources: quantities.insightsResources,
        },
    };
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

export async function pricingHandler(event: FunctionUrlEvent): Promise<FunctionUrlResult> {
    const method = (event.requestContext?.http?.method || "").toUpperCase();

    let input: unknown;
    if (method === "GET") {
        input = { ...(event.queryStringParameters || {}) };
    } else if (method === "POST") {
        const contentType = (event.headers?.["content-type"] || "").toLowerCase().split(";")[0].trim();
        if (contentType !== "application/json") {
            return jsonResponse(400, { ok: false, error: "unsupported_content_type" });
        }
        if (!event.body) {
            return jsonResponse(400, { ok: false, error: "empty_body" });
        }
        const rawBody = event.isBase64Encoded ? Buffer.from(event.body, "base64").toString("utf8") : event.body;
        if (Buffer.byteLength(rawBody, "utf8") > MAX_BODY_BYTES) {
            return jsonResponse(413, { ok: false, error: "payload_too_large" });
        }
        try {
            input = JSON.parse(rawBody);
        } catch (err) {
            return jsonResponse(400, { ok: false, error: "invalid_json" });
        }
    } else {
        return jsonResponse(405, { ok: false, error: "method_not_allowed" }, { allow: "GET, POST" });
    }

    if (typeof input !== "object" || input === null || Array.isArray(input)) {
        return jsonResponse(400, { ok: false, error: "invalid_body" });
    }

    const rates = ratesFromEnv();
    const parsed = parseUsage(input as Record<string, unknown>, rates);
    if (!parsed.ok) {
        return jsonResponse(400, { ok: false, error: "validation_failed", fields: parsed.fields });
    }
    return jsonResponse(200, { ok: true, estimate: estimate(parsed.usage, rates) });
}
