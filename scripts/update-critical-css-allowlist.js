// Proposes updates to the critical-CSS allowlist in inline-critical-css.js
// against real Search Console traffic, on a schedule, instead of leaving that
// list to informal human memory (pulumi/docs#21439 review discussion).
//
// Input: the same reader-signals/GSC snapshot the content-review pipeline
// already consumes (see scripts/content-review/select-articles.py's
// load_reader_signals docstring for the accepted shapes). Degrades to
// no-op, not a crash, when the export is missing or empty -- this script
// runs unattended and a missing input is not this script's failure to
// surface.
//
// Output: this script only rewrites the `pages` array in
// inline-critical-css.js when the ranked list has actually drifted; the
// calling workflow diffs the working tree and only commits when something
// changed. It never opens or merges a pull request itself -- that is the
// workflow's job, and the resulting PR is judgment-class (unarmed, human
// merge only), the same as this repo's other traffic-informed content
// decisions, because "which pages matter enough to pay build cost on" is
// exactly the kind of call this repo's own conventions reserve for a human.

const fs = require("fs");
const path = require("path");

const TARGET_FILE = path.join(__dirname, "inline-critical-css.js");
const MAX_LIST_LENGTH = 20; // headroom over today's 14; keeps build cost bounded (see the file's own comment)
const HOMEPAGE = "public/index.html";

// Only rank pages this repo's own build actually serves under a path
// beginning with one of these prefixes (or exactly "/"). Registry pages are
// a separate repo/build (see finding E in the 2026-09-07 SEO run) and are
// deliberately excluded even if the export contains them.
const ELIGIBLE_PREFIXES = ["/docs/", "/blog/", "/what-is/", "/product/", "/pricing/", "/careers/"];

function urlPathToBuiltFile(urlPath) {
    if (urlPath === "/") return HOMEPAGE;
    if (!ELIGIBLE_PREFIXES.some((p) => urlPath.startsWith(p))) return null;
    const trimmed = urlPath.replace(/^\/|\/$/g, "");
    return `public/${trimmed}/index.html`;
}

function loadGscPages(signalsFile) {
    if (!signalsFile || !fs.existsSync(signalsFile)) return {};
    let data;
    try {
        data = JSON.parse(fs.readFileSync(signalsFile, "utf-8"));
    } catch {
        return {};
    }
    if (!data || typeof data !== "object") return {};
    // Accept both the full {"signals": {"gsc": {...}}} envelope and the bare
    // {"pages": {...}} GSC-only export -- same tolerance as
    // select-articles.py's load_reader_signals.
    const gscSection = data.signals && typeof data.signals === "object" ? data.signals.gsc : data;
    if (!gscSection || typeof gscSection.pages !== "object") return {};
    return gscSection.pages;
}

function currentAllowlist(source) {
    const match = source.match(/const pages = \[([\s\S]*?)\];/);
    if (!match) throw new Error("Could not locate `const pages = [...]` in inline-critical-css.js");
    return [...match[1].matchAll(/"([^"]+)"/g)].map((m) => m[1]);
}

function proposeAllowlist(gscPages) {
    const ranked = Object.entries(gscPages)
        .map(([urlPath, row]) => ({
            file: urlPathToBuiltFile(urlPath),
            clicks: Number(row?.clicks) || 0,
            impressions: Number(row?.impressions) || 0,
        }))
        .filter((r) => r.file && r.file !== HOMEPAGE)
        .sort((a, b) => (b.clicks - a.clicks) || (b.impressions - a.impressions));

    const proposed = [HOMEPAGE];
    for (const r of ranked) {
        if (proposed.length >= MAX_LIST_LENGTH) break;
        if (!proposed.includes(r.file)) proposed.push(r.file);
    }
    return proposed;
}

function writeAllowlist(source, newPages) {
    const listBody = newPages.map((p) => `    "${p}",`).join("\n");
    return source.replace(/const pages = \[[\s\S]*?\];/, `const pages = [\n${listBody}\n];`);
}

function main() {
    const signalsFile = process.argv[2] || ".reader-signals.json";
    const gscPages = loadGscPages(signalsFile);
    if (Object.keys(gscPages).length === 0) {
        console.log("No reader-signals/GSC data available; leaving the allowlist untouched.");
        return;
    }

    const source = fs.readFileSync(TARGET_FILE, "utf-8");
    const before = currentAllowlist(source);
    const proposed = proposeAllowlist(gscPages);

    const beforeSet = new Set(before);
    const proposedSet = new Set(proposed);
    const added = proposed.filter((p) => !beforeSet.has(p));
    const removed = before.filter((p) => !proposedSet.has(p));

    if (added.length === 0 && removed.length === 0) {
        console.log("Allowlist already matches current top-traffic ranking; no changes.");
        return;
    }

    fs.writeFileSync(TARGET_FILE, writeAllowlist(source, proposed));
    console.log(`Proposed allowlist update: +${added.length} / -${removed.length}`);
    if (added.length) console.log(`  Adding:   ${added.join(", ")}`);
    if (removed.length) console.log(`  Removing: ${removed.join(", ")}`);
}

main();
