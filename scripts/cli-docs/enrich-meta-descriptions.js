#!/usr/bin/env node
// Replaces the generic "Learn about the pulumi X command." meta_desc emitted by
// `pulumi gen-markdown` with a description derived from each page's own summary line.
// Idempotent: only touches meta_desc values that match the generator's boilerplate, so
// hand-written descriptions from upstream are left alone.
//
// Usage: node scripts/cli-docs/enrich-meta-descriptions.js [commandsDir]

const fs = require("fs");
const path = require("path");

const dir = process.argv[2] || path.join(__dirname, "..", "..", "content", "docs", "iac", "cli", "commands");
const BOILERPLATE = /^meta_desc: "Learn about the (pulumi[^"]*) command\."$/m;
const MAX = 160;

function clean(s) {
    return s
        .replace(/^\[(EXPERIMENTAL|BETA)\]\s*/i, "")
        .replace(/`/g, "")
        .replace(/\[([^\]]+)\]\([^)]*\)/g, "$1")
        .replace(/[*_]{1,2}([^*_]+)[*_]{1,2}/g, "$1")
        .replace(/\s+/g, " ")
        .trim()
        .replace(/[.:;,]+$/, "");
}

function lowerFirst(s) {
    // Keep acronyms and proper nouns (second char uppercase, or all caps first word) intact.
    if (/^[A-Z]{2,}/.test(s)) return s;
    return s.charAt(0).toLowerCase() + s.slice(1);
}

function describe(cmd, body) {
    const lines = body.split("\n").map(l => l.trim());
    const summary = lines.find(l => l && !l.startsWith("#") && !l.startsWith("<") && !l.startsWith("{{"));
    if (!summary) return null;
    const head = `Reference for the ${cmd} command: `;
    const tail = " Usage, flags, and examples for the Pulumi CLI.";
    let sum = lowerFirst(clean(summary));
    if (!sum) return null;
    sum += ".";
    let out = head + sum + tail;
    if (out.length > MAX) {
        out = head + sum;
    }
    if (out.length > MAX) {
        const room = MAX - head.length - 1;
        let cut = sum.slice(0, room);
        cut = cut.slice(0, cut.lastIndexOf(" ")).replace(/[.:;,]+$/, "");
        out = head + cut + ".";
    }
    return out;
}

let changed = 0;
for (const name of fs.readdirSync(dir)) {
    if (!name.endsWith(".md") || name === "_index.md") continue;
    const file = path.join(dir, name);
    const text = fs.readFileSync(file, "utf8");
    const m = text.match(BOILERPLATE);
    if (!m) continue;
    const fmEnd = text.indexOf("\n---", 4);
    if (fmEnd < 0) continue;
    const desc = describe(m[1], text.slice(fmEnd + 4));
    if (!desc) continue;
    const escaped = desc.replace(/\\/g, "\\\\").replace(/"/g, '\\"');
    fs.writeFileSync(file, text.replace(BOILERPLATE, `meta_desc: "${escaped}"`));
    changed++;
}
console.log(`Updated meta_desc in ${changed} CLI command pages`);
