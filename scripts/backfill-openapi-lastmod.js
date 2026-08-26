#!/usr/bin/env node
// ONE-TIME historical backfill for data/openapi_lastmod.json. Not run by any
// workflow -- run by hand, once, then leave in the repo as a documented,
// reproducible record of how the backfilled dates were derived.
//
// The nightly scripts/update-openapi-lastmod.js only ever compares "now" to
// the last recorded hash, so every tag/schema was seeded dateless on
// 2026-08-15 and only accumulates real dates going forward. This script adds
// *historical* evidence: three archived captures of the OpenAPI spec on the
// Wayback Machine (2026-03-04, 2026-05-13, 2026-08-02), plus the 2026-08-15
// seed ledger itself (recovered from git history) as a fourth, all-dateless
// observation. Walking those observations oldest -> newest lets us date any
// key whose hash changed, or that first appeared, somewhere in that window --
// using the exact same canonicalize/sha256 logic the nightly job uses, so a
// backfilled date and a nightly-observed date mean the same thing.
//
// It NEVER overwrites an existing lastmod: the 16 dates already recorded by
// the live nightly job (2026-08-19 onward) are later and more precise than
// anything this script could derive, and leaving them untouched keeps this
// script safely re-runnable (a second run is a no-op).
//
// Usage:
//   node scripts/backfill-openapi-lastmod.js [--dry-run] [--cache-dir DIR] [--seed-ledger FILE]
//
// --dry-run       Print the summary but do not write data/openapi_lastmod.json.
// --cache-dir     Where archived spec snapshots are cached as
//                 <wayback-timestamp>.json (default: .openapi-wayback-cache/,
//                 not committed). A cached file is trusted as-is and not
//                 re-verified against the CDX API; only a freshly-fetched
//                 snapshot's digest is checked.
// --seed-ledger   Path to a JSON file shaped like data/openapi_lastmod.json to
//                 use as the 2026-08-15 seed observation, instead of reading
//                 it out of git history (see SEED_COMMIT below).

const fs = require("fs");
const path = require("path");
const { execSync } = require("child_process");
const lib = require("./update-openapi-lastmod.js");

const ROOT = path.join(__dirname, "..");
const LEDGER_FILE = path.join(ROOT, "data", "openapi_lastmod.json");
const SPEC_HOST_PATH = "api.pulumi.com/api/openapi/pulumi-spec.json";

// The ledger was seeded dateless from a live fetch on 2026-08-15; that seed,
// recovered from its own commit, is itself a fourth (all-dateless) observation.
const SEED_COMMIT = "34820a4bcc";
const SEED_DATE = "2026-08-15";

// The three archived captures identified via the CDX API on 2026-08-25, and
// the digest the CDX API reported for each at that time. If the archive ever
// reports a different digest for one of these exact timestamps, that is a
// sign of corruption or tampering upstream -- fail loudly rather than trust
// unverified content silently.
const OBSERVATIONS = [
    { date: "2026-03-04", timestamp: "20260304000737", digest: "BJN2UP25U2Q3UJWXJOSZKYGEP2M5OJF4" },
    { date: "2026-05-13", timestamp: "20260513062732", digest: "A6OSK3ELSZ7JXWYIVJHWN2ZICB4KZVT6" },
    { date: "2026-08-02", timestamp: "20260802095519", digest: "RUFKQ5FS5JGBSCHWPU3OK4AXPSDRZ2JB" },
];

const USER_AGENT =
    "pulumi-docs-openapi-lastmod-backfill/1.0 (+https://github.com/pulumi/docs; one-time historical backfill script; polite, low-volume, cached)";
const TIME_BUDGET_MS = 10 * 60 * 1000;
const startedAt = Date.now();

function timeLeftMs() {
    return TIME_BUDGET_MS - (Date.now() - startedAt);
}

function sleep(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms));
}

async function fetchWithBackoff(url, { maxAttempts = 6 } = {}) {
    let attempt = 0;
    let lastErr;
    while (attempt < maxAttempts) {
        if (timeLeftMs() <= 0) {
            throw new Error(`time budget (${TIME_BUDGET_MS}ms) exhausted fetching ${url}`);
        }
        try {
            const res = await fetch(url, {
                headers: { "User-Agent": USER_AGENT },
                signal: AbortSignal.timeout(Math.min(60000, Math.max(5000, timeLeftMs()))),
            });
            if (res.status === 429 || res.status >= 500) {
                throw new Error(`HTTP ${res.status}`);
            }
            if (!res.ok) {
                throw new Error(`HTTP ${res.status}`);
            }
            return res;
        } catch (err) {
            lastErr = err;
            attempt++;
            if (attempt >= maxAttempts) break;
            const backoff = Math.min(60000, 1000 * 2 ** attempt) + Math.floor(Math.random() * 1000);
            const wait = Math.max(0, Math.min(backoff, timeLeftMs()));
            console.error(`  fetch attempt ${attempt}/${maxAttempts} failed (${err.message}); retrying in ${Math.round(wait / 1000)}s`);
            await sleep(wait);
        }
    }
    throw new Error(`giving up on ${url} after ${maxAttempts} attempts: ${lastErr && lastErr.message}`);
}

async function queryCdxDigest(timestamp) {
    const cdxUrl =
        `https://web.archive.org/cdx/search/cdx?url=${encodeURIComponent(SPEC_HOST_PATH)}` +
        `&output=json&fl=timestamp,original,statuscode,digest,length&from=${timestamp}&to=${timestamp}`;
    const res = await fetchWithBackoff(cdxUrl);
    const rows = await res.json();
    const match = rows.slice(1).find((r) => r[0] === timestamp);
    if (!match) throw new Error(`CDX API returned no row for timestamp ${timestamp}`);
    return match[3]; // digest column, per fl= above
}

async function fetchSnapshot(obs, cacheDir) {
    const cachePath = path.join(cacheDir, `${obs.timestamp}.json`);
    if (fs.existsSync(cachePath)) {
        console.log(`  ${obs.date} (${obs.timestamp}): using cached snapshot at ${cachePath}`);
        return JSON.parse(fs.readFileSync(cachePath, "utf8"));
    }
    console.log(`  ${obs.date} (${obs.timestamp}): querying CDX API for digest...`);
    const liveDigest = await queryCdxDigest(obs.timestamp);
    if (liveDigest !== obs.digest) {
        throw new Error(
            `CDX digest mismatch for ${obs.timestamp}: expected ${obs.digest}, archive reports ${liveDigest}. ` +
                "Refusing to trust unverified snapshot content -- investigate before updating OBSERVATIONS.",
        );
    }
    console.log(`  ${obs.date} (${obs.timestamp}): CDX metadata verified, fetching content...`);
    const contentUrl = `https://web.archive.org/web/${obs.timestamp}id_/https://${SPEC_HOST_PATH}`;
    // Note on what is and isn't verified here: the CDX digest checked above
    // is the base32 SHA-1 of the *raw captured bytes* as transmitted over the
    // wire (confirmed by comparing a fetched snapshot's decoded length against
    // the CDX API's own `length` column, which is smaller -- the archive
    // stores the original gzip-compressed response). `fetch()` transparently
    // decompresses, so the JSON text below cannot be rehashed against that
    // digest; what's verified is that the archive's own metadata for this
    // exact timestamp still matches what was recorded on 2026-08-25, not the
    // bytes of this particular fetch. That is an acceptable bar for a
    // one-time, human-reviewed script whose only output is a committed diff.
    const res = await fetchWithBackoff(contentUrl);
    const text = await res.text();
    const spec = JSON.parse(text);
    fs.mkdirSync(cacheDir, { recursive: true });
    fs.writeFileSync(cachePath, text);
    return spec;
}

// Mirror scripts/update-openapi-lastmod.js's own hashing exactly (imported,
// not reimplemented) so a backfilled date and a nightly-observed date are
// produced by the same rule.
function hashesFor(spec) {
    const tagOps = lib.deriveTagOperations(spec);
    const tags = {};
    for (const [tag, ops] of tagOps.entries()) {
        const sorted = ops.slice().sort((a, b) => (a[0] + a[1]).localeCompare(b[0] + b[1]));
        tags[tag] = lib.sha256(sorted);
    }
    const schemas = {};
    for (const [name, value] of Object.entries((spec.components && spec.components.schemas) || {})) {
        schemas[name] = lib.sha256(value);
    }
    return { tags, schemas };
}

function loadSeedObservation(seedLedgerPath) {
    const raw = seedLedgerPath
        ? fs.readFileSync(seedLedgerPath, "utf8")
        : execSync(`git show ${SEED_COMMIT}:data/openapi_lastmod.json`, {
              cwd: ROOT,
              encoding: "utf8",
              maxBuffer: 1024 * 1024 * 32,
          });
    const seed = JSON.parse(raw);
    for (const section of ["tags", "schemas"]) {
        for (const [key, entry] of Object.entries(seed[section] || {})) {
            if (entry.lastmod) {
                throw new Error(
                    `seed ledger entry ${section}.${key} unexpectedly already has a lastmod -- ` +
                        "the seed is supposed to be entirely dateless; refusing to treat it as a clean observation",
                );
            }
        }
    }
    return {
        tags: Object.fromEntries(Object.entries(seed.tags || {}).map(([k, v]) => [k, v.hash])),
        schemas: Object.fromEntries(Object.entries(seed.schemas || {}).map(([k, v]) => [k, v.hash])),
    };
}

// The dating rule. observations: [[date, {key: hash}], ...] oldest -> newest.
// existingSection: current ledger section ({key: {hash[, lastmod]}}).
function backfillSection(existingSection, observations) {
    const updated = {};
    const stats = {
        byDate: {},
        byClass: { appeared: 0, changed: 0 },
        newlyDated: 0,
        alreadyDated: 0,
        stillDateless: 0,
    };
    for (const [key, entry] of Object.entries(existingSection)) {
        if (entry.lastmod) {
            updated[key] = entry; // never overwrite an existing date
            stats.alreadyDated++;
            continue;
        }
        let prevHash;
        let prevSeen = false;
        let lastChangeDate = null;
        let lastChangeClass = null;
        for (let i = 0; i < observations.length; i++) {
            const [date, hashes] = observations[i];
            const hash = hashes[key];
            const present = hash !== undefined;
            if (present && !prevSeen && i > 0) {
                lastChangeDate = date;
                lastChangeClass = "appeared";
            } else if (present && prevSeen && hash !== prevHash) {
                lastChangeDate = date;
                lastChangeClass = "changed";
            }
            if (present) {
                prevHash = hash;
                prevSeen = true;
            }
        }
        if (lastChangeDate) {
            updated[key] = { hash: entry.hash, lastmod: lastChangeDate };
            stats.byDate[lastChangeDate] = (stats.byDate[lastChangeDate] || 0) + 1;
            stats.byClass[lastChangeClass]++;
            stats.newlyDated++;
        } else {
            updated[key] = entry;
            stats.stillDateless++;
        }
    }
    return { updated, stats };
}

function updateMeta(meta, { totalNewlyDated, totalDateless }) {
    const next = { ...meta };
    const methodologyAddition =
        " A one-time historical backfill (see _meta.backfill) extended this ledger using archived " +
        "captures of the spec itself as direct evidence of when tracked content changed.";
    if (next.methodology && !next.methodology.includes("one-time historical backfill")) {
        next.methodology = next.methodology + methodologyAddition;
    }
    const seedNoteAddition =
        " Update (2026-08-25): retried, and the Wayback CDX API returned HTTP 200 with no rate-limiting " +
        "this time. The three snapshots below were fetched and used for the one-time backfill recorded in _meta.backfill.";
    if (next.seed_note && !next.seed_note.includes("2026-08-25")) {
        next.seed_note = next.seed_note + seedNoteAddition;
    }
    if (!next.backfill) {
        next.backfill = {
            performed_at: "2026-08-25",
            script: "scripts/backfill-openapi-lastmod.js",
            source: "Wayback Machine (web.archive.org) archived captures of https://api.pulumi.com/api/openapi/pulumi-spec.json",
            observations: [
                ...OBSERVATIONS.map((o) => ({ date: o.date, wayback_timestamp: o.timestamp, cdx_digest: o.digest })),
                {
                    date: SEED_DATE,
                    source: `git commit ${SEED_COMMIT} (this ledger's own dateless seed -- a direct observation of the spec at seed time)`,
                },
            ],
            method:
                "Walk observations oldest to newest. Record a change event when, relative to the immediately " +
                "preceding observation in which the key was seen, the key's hash differs (content changed) or the " +
                "key was absent in the preceding observation and present now (content created in that window). Set " +
                "lastmod to the date of the latest such event. Keys present in the oldest observation with no later " +
                "event, or absent from every observation, stay dateless.",
            precision:
                "A stamped date is the date on which the changed content was directly observed, not necessarily " +
                "the date the change was made. The true change falls somewhere in the interval after the preceding " +
                "observation up to and including the stamped date (up to 70 days before 2026-05-13, up to 81 days " +
                "before 2026-08-02, up to 13 days before 2026-08-15). The later, more recent bound of each interval " +
                "is what gets stamped, so no page ever claims to be fresher than a date on which its current content " +
                "was actually observed.",
            coverage: `${totalNewlyDated} of ${totalDateless} previously dateless keys recovered a lastmod; the remainder had not changed since the oldest available observation (2026-03-04) and legitimately stay dateless.`,
            not_overwritten:
                "No pre-existing lastmod value (all set by the live nightly job since 2026-08-19) was read, compared, or modified by this backfill.",
        };
    }
    return next;
}

function requireValue(argv, i, flag) {
    const v = argv[i + 1];
    if (v === undefined || v.startsWith("--")) {
        throw new Error(`${flag} requires a value`);
    }
    return v;
}

function parseArgs(argv) {
    const args = { cacheDir: path.join(ROOT, ".openapi-wayback-cache"), dryRun: false, seedLedger: null };
    for (let i = 0; i < argv.length; i++) {
        const a = argv[i];
        if (a === "--dry-run") args.dryRun = true;
        else if (a === "--cache-dir") args.cacheDir = requireValue(argv, i++, "--cache-dir");
        else if (a === "--seed-ledger") args.seedLedger = requireValue(argv, i++, "--seed-ledger");
        else throw new Error(`unknown argument: ${a}`);
    }
    return args;
}

async function main() {
    const args = parseArgs(process.argv.slice(2));
    console.log(`cache dir: ${args.cacheDir}`);
    console.log(args.dryRun ? "mode: dry-run (no files will be written)" : "mode: live");

    console.log("fetching/verifying archived spec snapshots...");
    const snapshotObs = [];
    for (const obs of OBSERVATIONS) {
        const spec = await fetchSnapshot(obs, args.cacheDir);
        snapshotObs.push([obs.date, hashesFor(spec)]);
    }

    const seedSource = args.seedLedger || `git show ${SEED_COMMIT}:data/openapi_lastmod.json`;
    console.log(`loading seed observation (${SEED_DATE}) from ${seedSource}...`);
    const seedHashes = loadSeedObservation(args.seedLedger);

    const allObservations = [...snapshotObs, [SEED_DATE, seedHashes]].sort((a, b) => a[0].localeCompare(b[0]));

    const ledger = JSON.parse(fs.readFileSync(LEDGER_FILE, "utf8"));
    const totalDatelessBefore =
        Object.values(ledger.tags || {}).filter((v) => !v.lastmod).length +
        Object.values(ledger.schemas || {}).filter((v) => !v.lastmod).length;

    const tagResult = backfillSection(
        ledger.tags || {},
        allObservations.map(([d, h]) => [d, h.tags]),
    );
    const schemaResult = backfillSection(
        ledger.schemas || {},
        allObservations.map(([d, h]) => [d, h.schemas]),
    );

    for (const [label, result] of [
        ["tags", tagResult],
        ["schemas", schemaResult],
    ]) {
        console.log(
            `\n${label}: ${result.stats.newlyDated} newly dated ` +
                `(${result.stats.byClass.appeared} appeared, ${result.stats.byClass.changed} changed), ` +
                `${result.stats.stillDateless} still dateless, ${result.stats.alreadyDated} already dated (untouched)`,
        );
        for (const date of Object.keys(result.stats.byDate).sort()) {
            console.log(`  ${date}: ${result.stats.byDate[date]}`);
        }
    }
    const totalNewlyDated = tagResult.stats.newlyDated + schemaResult.stats.newlyDated;
    console.log(`\ntotal newly dated: ${totalNewlyDated} of ${totalDatelessBefore} previously dateless keys`);

    if (args.dryRun) {
        console.log("\ndry-run: not writing ledger file.");
        return;
    }

    ledger.tags = tagResult.updated;
    ledger.schemas = schemaResult.updated;
    ledger._meta = updateMeta(ledger._meta || {}, { totalNewlyDated, totalDateless: totalDatelessBefore });

    fs.writeFileSync(LEDGER_FILE, JSON.stringify(ledger, null, 2) + "\n");
    console.log(`\nwrote ${LEDGER_FILE}`);
}

main().catch((err) => {
    console.error(`error: ${err.message}`);
    process.exit(1);
});
