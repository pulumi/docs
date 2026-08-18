#!/usr/bin/env node
// Keeps data/openapi_lastmod.json honest: an sha256 hash of each OpenAPI tag's
// and schema's content, plus the date that hash last changed. Read by
// content/docs/reference/cloud-rest-api/_content.gotmpl and
// content/docs/reference/cloud-rest-api/schema/_content.gotmpl to set each
// generated page's sitemap <lastmod> — those pages have no other honest
// per-page date, since they come from a gitignored, build-time-fetched spec
// with no date fields of its own.
//
// A key's lastmod only moves to today when its hash actually differs from
// the previously recorded hash (a real content change) or the key is new.
// Unchanged keys keep their existing date (or stay dateless if none has ever
// been recorded). Never stamp "today" across the board — an inaccurate,
// wholesale lastmod bump is exactly the anti-pattern that gets Google Search
// Console to distrust lastmod site-wide, and it would erase every future
// signal this ledger is meant to produce.
//
// Run by .github/workflows/update-openapi-lastmod.yml nightly. No auth
// needed — this hits the same public spec endpoint scripts/fetch-openapi-spec.sh
// downloads for the build itself.

const fs = require("fs");
const path = require("path");
const crypto = require("crypto");

const SPEC_URL = process.env.OPENAPI_SPEC_URL || "https://api.pulumi.com/api/openapi/pulumi-spec.json";
const ROOT = path.join(__dirname, "..");
const LEDGER_FILE = path.join(ROOT, "data", "openapi_lastmod.json");

const HTTP_METHODS = new Set(["get", "post", "put", "patch", "delete", "head", "options"]);

function todayUTC() {
    return new Date().toISOString().slice(0, 10);
}

// Canonical JSON: sorted keys, no whitespace, so semantically identical
// objects always hash the same regardless of upstream key ordering.
function canonicalize(value) {
    if (Array.isArray(value)) return value.map(canonicalize);
    if (value && typeof value === "object") {
        return Object.fromEntries(
            Object.keys(value)
                .sort()
                .map((k) => [k, canonicalize(value[k])]),
        );
    }
    return value;
}

function sha256(value) {
    return crypto.createHash("sha256").update(JSON.stringify(canonicalize(value))).digest("hex");
}

// Mirror content/docs/reference/cloud-rest-api/_content.gotmpl's tag derivation
// exactly: only the LAST tag on each operation counts, and a "Foo: Bar" tag
// collapses to "Foo". Keep this in sync if the adapter's logic ever changes.
function deriveTagOperations(spec) {
    const byTag = new Map();
    for (const [urlPath, methods] of Object.entries(spec.paths || {})) {
        if (!methods || typeof methods !== "object") continue;
        for (const [method, details] of Object.entries(methods)) {
            if (!HTTP_METHODS.has(method)) continue;
            const tags = details && details.tags;
            if (!tags || !tags.length) continue;
            let top = tags[tags.length - 1];
            if (top.includes(":")) {
                top = top.split(":")[0].replace(/\s+$/, "");
            }
            if (!byTag.has(top)) byTag.set(top, []);
            byTag.get(top).push([urlPath, method, details]);
        }
    }
    return byTag;
}

function loadLedger() {
    if (!fs.existsSync(LEDGER_FILE)) {
        throw new Error(
            `${LEDGER_FILE} is missing. This script only updates an existing ledger; ` +
                "seed it once (see the PR that introduced this file) before running the nightly job.",
        );
    }
    return JSON.parse(fs.readFileSync(LEDGER_FILE, "utf8"));
}

async function fetchSpec() {
    const res = await fetch(SPEC_URL, { signal: AbortSignal.timeout(60000) });
    if (!res.ok) {
        throw new Error(`GET ${SPEC_URL} -> HTTP ${res.status}`);
    }
    return res.json();
}

function updateSection(existingSection, currentHashes, today) {
    const updated = {};
    let changed = 0;
    let added = 0;
    let removed = 0;
    for (const key of Object.keys(currentHashes).sort()) {
        const hash = currentHashes[key];
        const prior = existingSection[key];
        if (!prior) {
            updated[key] = { hash };
            added++;
        } else if (prior.hash !== hash) {
            updated[key] = { hash, lastmod: today };
            changed++;
        } else {
            updated[key] = prior;
        }
    }
    for (const key of Object.keys(existingSection)) {
        if (!(key in currentHashes)) removed++;
    }
    return { updated, changed, added, removed };
}

async function main() {
    const ledger = loadLedger();
    const spec = await fetchSpec();
    const today = todayUTC();

    const tagOps = deriveTagOperations(spec);
    const tagHashes = {};
    for (const [tag, ops] of tagOps.entries()) {
        const sorted = ops.slice().sort((a, b) => (a[0] + a[1]).localeCompare(b[0] + b[1]));
        tagHashes[tag] = sha256(sorted);
    }

    const schemas = (spec.components && spec.components.schemas) || {};
    const schemaHashes = {};
    for (const [name, value] of Object.entries(schemas)) {
        schemaHashes[name] = sha256(value);
    }

    const tagResult = updateSection(ledger.tags || {}, tagHashes, today);
    const schemaResult = updateSection(ledger.schemas || {}, schemaHashes, today);

    ledger.tags = tagResult.updated;
    ledger.schemas = schemaResult.updated;

    // Deliberately do NOT stamp a "last_checked" (or any other) timestamp into
    // _meta on every run. This script runs nightly whether or not anything
    // changed, and _meta is part of the committed file: touching it
    // unconditionally would make every run's diff non-empty, so the calling
    // workflow's `git diff --cached --quiet` gate would never see "nothing to
    // commit" and would open (and auto-merge) a no-op PR every single night.
    // _meta is only ever edited by hand.

    const totalChanged =
        tagResult.changed + tagResult.added + tagResult.removed + schemaResult.changed + schemaResult.added + schemaResult.removed;

    fs.writeFileSync(LEDGER_FILE, JSON.stringify(ledger, null, 2) + "\n");

    console.log(
        `tags: ${tagResult.changed} changed, ${tagResult.added} added, ${tagResult.removed} removed ` +
            `(${Object.keys(tagHashes).length} total)`,
    );
    console.log(
        `schemas: ${schemaResult.changed} changed, ${schemaResult.added} added, ${schemaResult.removed} removed ` +
            `(${Object.keys(schemaHashes).length} total)`,
    );
    if (totalChanged === 0) {
        console.log("no changes observed \u2014 ledger file is byte-identical to its prior committed state");
    }
}

main().catch((err) => {
    console.error(`error: ${err.message}`);
    process.exit(1);
});
