// Copyright 2016-2026, Pulumi Corporation.  All rights reserved.

// Validation for support-request submissions POSTed to /api/support.
//
// This module is deliberately pure and dependency-free (types only) so it can
// be unit-tested with the Node test runner without standing up any AWS
// machinery, and so the Lambda closure it ships in stays small. The rules here
// are the single source of truth for the payload contract; the client-side
// validation in theme/src/ts/support-form.ts mirrors them for UX, but only
// this module is authoritative.

// Category ids for the "I need help with:" select. The display labels live in
// the form's front matter (content/support/new/_index.md); ids and labels must
// stay in sync with it.
export const CATEGORIES = ["account-sales", "program", "cloud", "docs"] as const;
export type Category = (typeof CATEGORIES)[number];

// Maximum accepted request body, enforced before JSON.parse. The field limits
// below keep legitimate payloads far under this.
export const MAX_BODY_BYTES = 256 * 1024;

export const LIMITS = {
    email: 254,
    name: 200,
    company: 200,
    organization: 40,
    subject: 200,
    descriptionMin: 10,
    description: 20000,
    pulumiAbout: 20000,
    attachmentsMax: 5,
    attachmentFilename: 255,
    attachmentSizeBytes: 20 * 1024 * 1024,
    attachmentContentType: 100,
};

// Pragmatic email shape check: something@something.tld. Full RFC 5322
// validation rejects real addresses and accepts junk; the confirmation email
// is the real verifier.
const EMAIL_PATTERN = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

// Pulumi organization names: alphanumeric start, then alphanumeric, hyphen, or
// underscore, 40 chars max (matches the Pulumi Cloud org-name rules).
const ORGANIZATION_PATTERN = /^[a-zA-Z0-9][a-zA-Z0-9-_]{0,39}$/;

export interface AttachmentMetadata {
    filename: string;
    sizeBytes: number;
    contentType: string;
}

export interface SupportRequest {
    email: string;
    name: string;
    company?: string;
    organization: string;
    category: Category;
    subject: string;
    description: string;
    pulumiAbout?: string;
    // Metadata only: attachment bytes are not uploaded until the Intercom
    // integration defines where they go.
    attachments?: AttachmentMetadata[];
}

export type ValidationResult =
    | { ok: true; value: SupportRequest }
    | { ok: false; fields: Record<string, string> };

// Keys accepted at the top level of the JSON payload. "website" is the
// honeypot field: the handler checks it before validation runs, but it is
// tolerated here so a spam submission that slips through still validates
// rather than erroring on an unknown key.
const KNOWN_KEYS = new Set([
    "email",
    "name",
    "company",
    "organization",
    "category",
    "subject",
    "description",
    "pulumiAbout",
    "attachments",
    "website",
]);

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

function validateAttachments(input: unknown, fields: Record<string, string>): AttachmentMetadata[] | undefined {
    if (input === undefined || input === null) {
        return undefined;
    }
    if (!Array.isArray(input)) {
        fields.attachments = "Expected a list of attachment metadata.";
        return undefined;
    }
    if (input.length === 0) {
        return undefined;
    }
    if (input.length > LIMITS.attachmentsMax) {
        fields.attachments = `Attach up to ${LIMITS.attachmentsMax} files.`;
        return undefined;
    }
    const result: AttachmentMetadata[] = [];
    for (const item of input) {
        if (!isRecord(item)) {
            fields.attachments = "Expected a list of attachment metadata.";
            return undefined;
        }
        const { filename, sizeBytes, contentType } = item;
        if (
            typeof filename !== "string" ||
            filename.trim().length === 0 ||
            filename.length > LIMITS.attachmentFilename
        ) {
            fields.attachments = "Each attachment needs a filename of at most 255 characters.";
            return undefined;
        }
        if (
            typeof sizeBytes !== "number" ||
            !Number.isFinite(sizeBytes) ||
            sizeBytes < 0 ||
            sizeBytes > LIMITS.attachmentSizeBytes
        ) {
            fields.attachments = "Each attachment must be 20 MB or smaller.";
            return undefined;
        }
        if (typeof contentType !== "string" || contentType.length > LIMITS.attachmentContentType) {
            fields.attachments = "Each attachment needs a content type.";
            return undefined;
        }
        result.push({ filename: filename.trim(), sizeBytes, contentType });
    }
    return result;
}

export function validateSubmission(input: unknown): ValidationResult {
    const fields: Record<string, string> = {};

    if (!isRecord(input)) {
        return { ok: false, fields: { _form: "Expected a JSON object." } };
    }

    for (const key of Object.keys(input)) {
        if (!KNOWN_KEYS.has(key)) {
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
            fields.name = `Keep your name under ${LIMITS.name} characters.`;
        }
    }

    const company = stringField(input, "company", fields);
    if (fields.company === undefined && company && company.length > LIMITS.company) {
        fields.company = `Keep your company name under ${LIMITS.company} characters.`;
    }

    const organizationRaw = stringField(input, "organization", fields);
    let organization: string | undefined;
    if (fields.organization === undefined) {
        organization = organizationRaw ? normalizeOrganization(organizationRaw) : undefined;
        if (!organization) {
            fields.organization = "Enter your Pulumi organization name.";
        } else if (!ORGANIZATION_PATTERN.test(organization)) {
            fields.organization =
                "Enter just the organization name from https://app.pulumi.com/PULUMI_ORG_NAME " +
                "(letters, numbers, hyphens, and underscores).";
        }
    }

    const category = stringField(input, "category", fields);
    if (fields.category === undefined) {
        if (!category) {
            fields.category = "Choose the area you need help with.";
        } else if ((CATEGORIES as readonly string[]).indexOf(category) === -1) {
            fields.category = "Choose one of the listed areas.";
        }
    }

    const subject = stringField(input, "subject", fields);
    if (fields.subject === undefined) {
        if (!subject) {
            fields.subject = "Enter a subject.";
        } else if (subject.length > LIMITS.subject) {
            fields.subject = `Keep the subject under ${LIMITS.subject} characters.`;
        }
    }

    const description = stringField(input, "description", fields);
    if (fields.description === undefined) {
        if (!description || description.length < LIMITS.descriptionMin) {
            fields.description = "Describe the issue in at least a few words.";
        } else if (description.length > LIMITS.description) {
            fields.description = `Keep the description under ${LIMITS.description} characters.`;
        }
    }

    const pulumiAbout = stringField(input, "pulumiAbout", fields);
    if (fields.pulumiAbout === undefined && pulumiAbout && pulumiAbout.length > LIMITS.pulumiAbout) {
        fields.pulumiAbout = `Keep the output under ${LIMITS.pulumiAbout} characters.`;
    }

    const attachments = validateAttachments(input.attachments, fields);

    if (Object.keys(fields).length > 0) {
        return { ok: false, fields };
    }

    const value: SupportRequest = {
        email: email as string,
        name: name as string,
        organization: organization as string,
        category: category as Category,
        subject: subject as string,
        description: description as string,
    };
    if (company) {
        value.company = company;
    }
    if (pulumiAbout) {
        value.pulumiAbout = pulumiAbout;
    }
    if (attachments && attachments.length > 0) {
        value.attachments = attachments;
    }
    return { ok: true, value };
}
