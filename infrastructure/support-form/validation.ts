// Copyright 2016-2026, Pulumi Corporation.  All rights reserved.

// Validation for support-request submissions POSTed to /api/support.
//
// This module is deliberately pure and dependency-free (types only) so it can
// be unit-tested with the Node test runner without standing up any AWS
// machinery, and so the Lambda closure it ships in stays small. The rules here
// are the single source of truth for the payload contract; the client-side
// validation in theme/src/ts/support-form.ts mirrors them for UX, but only
// this module is authoritative.

// Priority ids for the "Priority" select. The display labels live in the
// form's front matter (content/support/new/_index.md); ids and labels must
// stay in sync with it.
export const PRIORITIES = ["normal", "urgent"] as const;
export type Priority = (typeof PRIORITIES)[number];

// Maximum accepted request body, enforced before JSON.parse. The field limits
// below keep legitimate payloads far under this.
export const MAX_BODY_BYTES = 256 * 1024;

export const LIMITS = {
    email: 254,
    name: 200,
    organization: 40,
    subject: 200,
    descriptionMin: 10,
    description: 20000,
};

// Pragmatic email shape check: something@something.tld. Full RFC 5322
// validation rejects real addresses and accepts junk; the confirmation email
// is the real verifier.
const EMAIL_PATTERN = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

// Pulumi organization names: alphanumeric start, then alphanumeric, hyphen, or
// underscore (matches the Pulumi Cloud org-name rules). The length bound is
// LIMITS.organization rather than a repeat count here, so the two rules have
// one source of truth apiece — and an over-long name gets told it's too long
// instead of being blamed on its characters.
const ORGANIZATION_PATTERN = /^[a-zA-Z0-9][a-zA-Z0-9-_]*$/;

export interface SupportRequest {
    email: string;
    name: string;
    organization: string;
    priority: Priority;
    subject: string;
    description: string;
}

export type ValidationResult =
    | { ok: true; value: SupportRequest }
    | { ok: false; fields: Record<string, string> };

// Keys accepted at the top level of the JSON payload. "website" is the
// honeypot field: the handler checks it before validation runs, but it is
// tolerated here so a spam submission that slips through still validates
// rather than erroring on an unknown key.
const KNOWN_KEYS = [
    "email",
    "name",
    "organization",
    "priority",
    "subject",
    "description",
    "website",
];

// Strips a pasted console URL ("https://app.pulumi.com/my-org/...") or
// stray slashes down to the bare organization name.
export function normalizeOrganization(raw: string): string {
    let value = raw.trim();
    value = value.replace(/^https?:\/\/(www\.)?app\.pulumi\.com\//i, "");
    value = value.replace(/^app\.pulumi\.com\//i, "");
    value = value.replace(/^\/+/, "");
    const slash = value.indexOf("/");
    if (slash !== -1) {
        value = value.slice(0, slash);
    }
    return value.trim();
}

function isRecord(input: unknown): input is Record<string, unknown> {
    return typeof input === "object" && input !== null && !Array.isArray(input);
}

// Returns the trimmed string value of a field, or undefined (recording an
// error) when the value is present but not a string.
function stringField(
    record: Record<string, unknown>,
    key: string,
    fields: Record<string, string>,
): string | undefined {
    const value = record[key];
    if (value === undefined || value === null) {
        return undefined;
    }
    if (typeof value !== "string") {
        fields[key] = "Expected a string.";
        return undefined;
    }
    return value.trim();
}

export function validateSubmission(input: unknown): ValidationResult {
    const fields: Record<string, string> = {};

    if (!isRecord(input)) {
        return { ok: false, fields: { _form: "Expected a JSON object." } };
    }

    for (const key of Object.keys(input)) {
        if (!KNOWN_KEYS.includes(key)) {
            return { ok: false, fields: { _form: `Unexpected field "${key}".` } };
        }
    }

    const email = stringField(input, "email", fields);
    if (fields.email === undefined) {
        if (!email) {
            fields.email = "Enter your email address.";
        } else if (email.length > LIMITS.email || !EMAIL_PATTERN.test(email)) {
            fields.email = "Enter a valid email address.";
        }
    }

    const name = stringField(input, "name", fields);
    if (fields.name === undefined) {
        if (!name) {
            fields.name = "Enter your full name.";
        } else if (name.length > LIMITS.name) {
            fields.name = `Keep your name to ${LIMITS.name} characters or fewer.`;
        }
    }

    const organizationRaw = stringField(input, "organization", fields);
    let organization: string | undefined;
    if (fields.organization === undefined) {
        organization = organizationRaw ? normalizeOrganization(organizationRaw) : undefined;
        if (!organization) {
            fields.organization = "Enter your Pulumi organization name.";
        } else if (organization.length > LIMITS.organization) {
            fields.organization = `Keep the organization name to ${LIMITS.organization} characters or fewer.`;
        } else if (!ORGANIZATION_PATTERN.test(organization)) {
            fields.organization =
                "Enter just the organization name from https://app.pulumi.com/PULUMI_ORG_NAME " +
                "(letters, numbers, hyphens, and underscores).";
        }
    }

    const priority = stringField(input, "priority", fields);
    if (fields.priority === undefined) {
        if (!priority) {
            fields.priority = "Choose a priority.";
        } else if ((PRIORITIES as readonly string[]).indexOf(priority) === -1) {
            fields.priority = "Choose one of the listed priorities.";
        }
    }

    const subject = stringField(input, "subject", fields);
    if (fields.subject === undefined) {
        if (!subject) {
            fields.subject = "Enter a subject.";
        } else if (subject.length > LIMITS.subject) {
            fields.subject = `Keep the subject to ${LIMITS.subject} characters or fewer.`;
        }
    }

    const description = stringField(input, "description", fields);
    if (fields.description === undefined) {
        if (!description || description.length < LIMITS.descriptionMin) {
            fields.description = "Describe the issue in at least a few words.";
        } else if (description.length > LIMITS.description) {
            fields.description = `Keep the description to ${LIMITS.description} characters or fewer.`;
        }
    }

    if (Object.keys(fields).length > 0) {
        return { ok: false, fields };
    }

    const value: SupportRequest = {
        email: email as string,
        name: name as string,
        organization: organization as string,
        priority: priority as Priority,
        subject: subject as string,
        description: description as string,
    };
    return { ok: true, value };
}
