#!/usr/bin/env node
// Fetches the policies in each pre-built policy pack from the Pulumi Cloud REST
// API and writes them to data/policy_pack_policies/<pack>.json, the source of
// truth for the auto-generated reference pages under
// content/docs/reference/pre-built-policy-packs/.
//
// Which packs are fetched is controlled by the allowlist in data/policy_packs.yaml.
//
// These endpoints require authentication, so this script is NOT part of the
// normal `make ensure` build (which must work without a token). It is run by the
// .github/workflows/update-policy-packs.yml GitHub Action, which supplies a token
// and opens a PR when the committed data changes. Run it locally only for
// testing, with PULUMI_ACCESS_TOKEN set.

const fs = require("fs");
const path = require("path");
const yaml = require("js-yaml");

const API = process.env.PULUMI_API || "https://api.pulumi.com";
const TOKEN = process.env.PULUMI_ACCESS_TOKEN;
const ROOT = path.join(__dirname, "..");
const ALLOWLIST = path.join(ROOT, "data", "policy_packs.yaml");
// Kept separate from data/policy_packs.yaml: Hugo derives the site.Data key from
// the basename, so a data/policy_packs/ directory would collide with it.
const OUTPUT_DIR = path.join(ROOT, "data", "policy_pack_policies");
// Honest "content last changed" ledger, read by content/docs/reference/pre-built-policy-packs/
// _content.gotmpl to set each generated page's sitemap <lastmod>. A pack's date only
// moves forward here when its JSON content actually changes (see the diff check below) —
// never on every run, and never to "today" just because the script ran.
const LASTMOD_FILE = path.join(ROOT, "data", "policy_pack_lastmod.json");

// Guarded so the pure helpers below can be required by scripts/fetch-policy-packs.test.js
// without a token; the fetching path still refuses to run without one.
if (!TOKEN && require.main === module) {
    console.error("error: PULUMI_ACCESS_TOKEN is not set. This script calls authenticated");
    console.error("       Pulumi Cloud policy pack endpoints and cannot run without a token.");
    process.exit(1);
}

// Fetch JSON from the API, retrying transient failures.
async function fetchJSON(urlPath) {
    let lastErr;
    for (let attempt = 1; attempt <= 3; attempt++) {
        try {
            const res = await fetch(`${API}${urlPath}`, {
                headers: { Authorization: `token ${TOKEN}` },
                signal: AbortSignal.timeout(60000),
            });
            if (!res.ok) {
                // 4xx is a real error (bad pack name, no access) — do not retry.
                if (res.status >= 400 && res.status < 500) {
                    throw new Error(`GET ${urlPath} -> HTTP ${res.status}: ${(await res.text()).slice(0, 200)}`);
                }
                throw new Error(`GET ${urlPath} -> HTTP ${res.status}`);
            }
            return await res.json();
        } catch (err) {
            lastErr = err;
            if (/HTTP 4\d\d/.test(err.message)) throw err;
            if (attempt < 3) await new Promise((r) => setTimeout(r, 1000 * attempt));
        }
    }
    throw lastErr;
}

// The latest published version of a pack. `versions` (ints) and `versionTags`
// (semver) are parallel arrays, so index the tag by the highest version number
// rather than trusting array order.
function latestVersionTag(entry) {
    const { versions = [], versionTags = [] } = entry;
    if (!versions.length) return null;
    let best = 0;
    for (let i = 1; i < versions.length; i++) {
        if (versions[i] > versions[best]) best = i;
    }
    return versionTags[best] || null;
}

// Policies whose remediationSteps contain a code fence that is never closed.
//
// remediationSteps is Markdown, and an unclosed fence swallows every heading that
// follows it, silently dropping policies from the rendered page. This is an upstream
// authoring bug (a "```," typo), so warn rather than fail: the docs should still
// build, and layouts/partials/policy-packs/remediation.html repairs the common case.
function unclosedFences(policies) {
    return policies
        .filter((p) => {
            let open = false;
            for (const line of (p.remediationSteps || "").split("\n")) {
                const s = line.trim();
                if (!s.startsWith("```")) continue;
                // An opening fence may carry an info string ("```typescript");
                // a closing fence may not.
                if (!open) open = true;
                else if (s.slice(3).trim() === "") open = false;
            }
            return open;
        })
        .map((p) => p.name);
}

// Recursively sort object keys so the committed JSON diffs cleanly.
function sortKeys(value) {
    if (Array.isArray(value)) return value.map(sortKeys);
    if (value && typeof value === "object") {
        return Object.fromEntries(
            Object.keys(value)
                .sort()
                .map((k) => [k, sortKeys(value[k])]),
        );
    }
    return value;
}

function todayUTC() {
    return new Date().toISOString().slice(0, 10);
}

function loadLastmodLedger() {
    if (!fs.existsSync(LASTMOD_FILE)) {
        return {
            _meta: {
                purpose:
                    "Sitemap <lastmod> and JSON-LD dateModified source for content/docs/reference/pre-built-policy-packs/ pages.",
                generator: "scripts/fetch-policy-packs.js (self-stamping diff on each nightly run)",
                methodology:
                    "A pack's lastmod is the date its data/policy_pack_policies/<pack>.json last actually changed content (canonicalized diff), not merely the date the file was last committed for an unrelated reason.",
            },
            packs: {},
        };
    }
    return JSON.parse(fs.readFileSync(LASTMOD_FILE, "utf8"));
}

// The `pulumi` org holds two different things under one name: the packs we ship as
// products, and packs published to the org privately (internal use, experiments,
// customer one-offs). `/api/orgs/{org}/policypacks` returns both with nothing to tell
// them apart, which is how the private hitrust-awsnative pack ended up with a public
// reference page (pulumi/docs#21055).
//
// The registry listing does carry the distinction, in `source`. Verified against the
// live listing for the `pulumi` org on 2026-08-25 (36 packs: 23 `pulumi`, 13 `private`):
//
//     { "source": "private", "publisher": "pulumi",
//       "name": "approved-component-versions-bad", "version": "1.0.4", ... }
//     { "source": "pulumi",  "publisher": "pulumi",
//       "name": "aws-organizations-tag-policies",  "version": "1.0.0", ... }
//
// Note `publisher` is "pulumi" for everything in our org, so it is NOT the discriminator
// -- do not "improve" this by filtering on it. `source` is, and it is set by an admin
// command rather than by whoever publishes the pack, so an engineer testing something
// cannot set it by accident.
//
// The response is `ListPolicyPacksResponse` in the published Pulumi Cloud OpenAPI spec:
// a required `policyPacks` array plus an optional `continuationToken` for paging.
//
// This fails closed. If the listing cannot be read, looks different from the above, or
// is only partly readable, the job stops rather than falling back to publishing
// unverified pages: a broken check should cost us a nightly sync, not put a private pack
// on the website.
async function fetchRegistryProducts(org) {
    const body = await fetchJSON(`/api/registry/policypacks?orgLogin=${encodeURIComponent(org)}`);
    return parseRegistryListing(body, org);
}

// The pure half of the above, split out so the shape handling is testable without a token.
function parseRegistryListing(body, org) {
    const rows = body?.policyPacks;
    if (!Array.isArray(rows)) {
        throw new Error(
            `could not read the registry policy pack listing for the "${org}" org: expected a\n` +
                `       "policyPacks" array. The API shape may have changed -- see the comment above\n` +
                `       fetchRegistryProducts in this file.`,
        );
    }
    // The response pages, and no documented query parameter asks for page two. A partial
    // read is worse than no read: it fails documented packs that are fine, and it hides
    // products nobody documented from the check below, which is the one thing that check
    // exists to catch. Stop rather than trust an incomplete list.
    if (body.continuationToken) {
        throw new Error(
            `the registry policy pack listing for the "${org}" org is paginated\n` +
                `       (continuationToken present) and this script only reads the first page. Teach it\n` +
                `       to follow the token before trusting the result.`,
        );
    }
    const products = new Set();
    const nonProducts = new Map();
    for (const row of rows) {
        if (!row?.name) continue;
        // Distinguish "present but carries no source" from "absent from the listing"; the
        // caller reports the latter, and conflating them sends whoever reads the error
        // looking for a deleted pack that is right there.
        if (row.source === "pulumi") products.add(row.name);
        else nonProducts.set(row.name, row.source ?? "(no source field)");
    }
    // A listing with rows but no products is a shape problem, never an allowlist problem.
    // `source` going missing for this org's records would otherwise surface as the
    // allowlist error below naming every documented pack as privately published, which is
    // the most alarming possible misreading of an upstream schema change.
    if (rows.length && !products.size) {
        throw new Error(
            `the registry listing for the "${org}" org returned ${rows.length} record(s) but not\n` +
                `       one with source: "pulumi". That is far more likely a change to the API's\n` +
                `       "source" field than every pack being unpublished at once -- see the comment\n` +
                `       above fetchRegistryProducts.`,
        );
    }
    return { products, nonProducts };
}

// Both directions of the gate, pure so it can be exercised without the network.
// Forward: nothing documented may be a non-product. Reverse: no product may go
// undocumented without a recorded reason.
function auditAllowlist({ org, packs, allowlistUndocumented, products, nonProducts, warn = console.warn }) {
    // Gate the allowlist on what the registry says we actually publish as products.
    const notProducts = packs.filter((p) => !products.has(p));
    if (notProducts.length) {
        const detail = notProducts
            .map((p) => `${p} (source: ${nonProducts.get(p) ?? "absent from the listing"})`)
            .join(", ");
        throw new Error(
            `these entries in data/policy_packs.yaml are not published Pulumi products: ${detail}\n` +
                `       Only packs the registry returns with source: "pulumi" may be documented. A pack\n` +
                `       can be built in policy-packs-internal and resolvable through\n` +
                `       /api/orgs/${org}/policypacks while still being private to the org.\n` +
                `       Remove the entry, or publish the pack as a product before documenting it.`,
        );
    }

    // ...and the other way round: a pack we publish as a product but do not document is
    // the same failure this PR was opened to fix, just pointing the other way. Anything
    // the registry calls a product needs either an entry above or a line in
    // `undocumented:` saying why not.
    // The exemption list is the one input here with nothing behind it, so validate it or
    // the reason it exists to record isn't actually required: `- pack: foo` with no `why:`
    // would silence the check exactly as well as a real exemption, and it is the shortest
    // path for whoever is unblocking a red nightly at 08:00. The bare-string form
    // (`- foo`) is worse still -- `e.pack` is undefined, so the pack stays unaccounted for
    // and the check fires naming a pack the author believes they just listed.
    const undocumented = allowlistUndocumented || [];
    const unexplained = undocumented.filter((e) => !e?.pack || !String(e?.why || "").trim());
    if (unexplained.length) {
        throw new Error(
            `every entry under "undocumented:" in data/policy_packs.yaml needs both a "pack:" and\n` +
                `       a "why:": ${JSON.stringify(unexplained)}\n` +
                `       The list records why a product stays unlisted; it is not a way to silence the\n` +
                `       check below.`,
        );
    }
    const alsoDocumented = undocumented.map((e) => e.pack).filter((p) => packs.includes(p));
    if (alsoDocumented.length) {
        throw new Error(
            `these packs are listed under "undocumented:" in data/policy_packs.yaml but also have\n` +
                `       a page above: ${alsoDocumented.join(", ")}. Remove the "undocumented:" entry.`,
        );
    }
    // A pack that loses product status leaves a permanent, invisible exemption behind --
    // which is how hitrust-awsnative survived as long as it did. Harmless but stale, so
    // this says something rather than throwing.
    const staleExemptions = undocumented.map((e) => e.pack).filter((p) => !products.has(p));
    if (staleExemptions.length) {
        warn(
            `warning: these "undocumented:" entries in data/policy_packs.yaml are no longer\n` +
                `         published products: ${staleExemptions.join(", ")}. Drop them once confirmed.`,
        );
    }

    const accountedFor = new Set([...packs, ...undocumented.map((e) => e.pack)]);
    const undocumentedProducts = [...products].filter((p) => !accountedFor.has(p));
    if (undocumentedProducts.length) {
        throw new Error(
            `these packs are published as Pulumi products but have no reference page:\n` +
                `       ${undocumentedProducts.join(", ")}\n` +
                `       Add an entry to data/policy_packs.yaml, or list the pack under\n` +
                `       "undocumented:" there with the reason it stays unlisted.`,
        );
    }

}

async function main() {
    const allowlist = yaml.load(fs.readFileSync(ALLOWLIST, "utf8"));
    const org = allowlist.org;
    const entries = allowlist.sections.flatMap((s) => s.packs);

    // Only packs built from pulumi/policy-packs-internal may be documented. The `pulumi`
    // org is also where we publish policy packs for our own internal use (plus
    // experiments and customer one-offs), and those are not products. Requiring every
    // entry to name the repo directory that builds it means an internal-use pack cannot
    // be added without someone first having to invent a `source:` path for it.
    const undeclared = entries.filter((e) => !e.source || !String(e.source).startsWith("packs/"));
    if (undeclared.length) {
        throw new Error(
            `these entries in data/policy_packs.yaml have no valid "source:" (a packs/... directory in\n` +
                `       pulumi/policy-packs-internal): ${undeclared.map((e) => e.pack).join(", ")}\n` +
                `       Only packs built from that repo may be documented — see the comment at the top of the file.`,
        );
    }

    const packs = entries.map((e) => e.pack);

    const { products, nonProducts } = await fetchRegistryProducts(org);
    auditAllowlist({ org, packs, allowlistUndocumented: allowlist.undocumented, products, nonProducts });

    console.log(`Fetching ${packs.length} policy packs from ${API} (org: ${org})...`);

    const list = await fetchJSON(`/api/orgs/${org}/policypacks`);
    const published = new Map((list.policyPacks || []).map((p) => [p.name, p]));

    fs.mkdirSync(OUTPUT_DIR, { recursive: true });
    const warnings = [];
    const lastmodLedger = loadLastmodLedger();

    for (const name of packs) {
        const entry = published.get(name);
        if (!entry) {
            throw new Error(
                `pack "${name}" is in data/policy_packs.yaml but is not published to the "${org}" org`,
            );
        }
        const tag = latestVersionTag(entry);
        if (!tag) {
            throw new Error(`pack "${name}" has no published versions`);
        }

        // NB: the {version} path segment is the semver tag ("1.0.2"), NOT the
        // numeric version ("3"), despite what the OpenAPI spec's description says.
        const pack = await fetchJSON(
            `/api/orgs/${org}/policypacks/${encodeURIComponent(name)}/versions/${encodeURIComponent(tag)}`,
        );

        if (!Array.isArray(pack.policies) || pack.policies.length === 0) {
            throw new Error(`pack "${name}@${tag}" came back with no policies`);
        }
        if (!pack.versionTag) {
            throw new Error(`pack "${name}@${tag}" came back with no versionTag`);
        }

        // Sort policies by name so a republish that only reorders them is a no-op diff.
        pack.policies.sort((a, b) => a.name.localeCompare(b.name));

        const broken = unclosedFences(pack.policies);
        if (broken.length) {
            warnings.push(`${name}@${pack.versionTag}: ${broken.join(", ")}`);
        }

        console.log(`  ${name}@${pack.versionTag} (${pack.policies.length} policies)`);
        const outPath = path.join(OUTPUT_DIR, `${name}.json`);
        const newContent = JSON.stringify(sortKeys(pack), null, 2) + "\n";
        const oldContent = fs.existsSync(outPath) ? fs.readFileSync(outPath, "utf8") : null;
        if (newContent !== oldContent) {
            lastmodLedger.packs[name] = todayUTC();
        }
        fs.writeFileSync(outPath, newContent);
    }

    // Drop data for packs that are no longer in the allowlist.
    const expected = new Set(packs.map((p) => `${p}.json`));
    for (const file of fs.readdirSync(OUTPUT_DIR)) {
        if (file.endsWith(".json") && !expected.has(file)) {
            console.log(`  removing stale ${file}`);
            fs.unlinkSync(path.join(OUTPUT_DIR, file));
        }
    }
    for (const pack of Object.keys(lastmodLedger.packs)) {
        if (!packs.includes(pack)) delete lastmodLedger.packs[pack];
    }
    lastmodLedger.packs = Object.fromEntries(
        Object.keys(lastmodLedger.packs)
            .sort()
            .map((k) => [k, lastmodLedger.packs[k]]),
    );
    fs.writeFileSync(LASTMOD_FILE, JSON.stringify(lastmodLedger, null, 2) + "\n");

    console.log(`Wrote policy pack data to data/policy_pack_policies/`);

    if (warnings.length) {
        console.warn(
            "\nwarning: unclosed Markdown code fence in remediationSteps (an upstream\n" +
                "         authoring bug in pulumi/policy-packs-internal — the page still renders,\n" +
                "         but the policy source should be fixed):",
        );
        for (const w of warnings) console.warn(`  ${w}`);
    }
}

if (require.main === module) {
    main().catch((err) => {
        console.error(`error: ${err.message}`);
        process.exit(1);
    });
}

module.exports = { parseRegistryListing, auditAllowlist, latestVersionTag, unclosedFences };
