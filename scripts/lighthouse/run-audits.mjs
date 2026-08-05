#!/usr/bin/env node

// Runs the Lighthouse performance audits behind the per-PR performance report.
//
// Usage: node scripts/lighthouse/run-audits.mjs <base-url> <output-dir>
//
// Every page in pages.json is audited on both mobile and desktop, and each result
// is written to <output-dir>/<page-key>-<device>.json for scripts/run-lighthouse-pr.sh
// to render. Two things make this meaningfully faster than shelling out to the
// Lighthouse CLI once per audit:
//
//   1. All audits share a single Chrome process instead of paying a cold boot each
//      time. (Lighthouse still resets storage and uses a fresh tab per run, so the
//      audits stay independent.)
//   2. The screenshot audits are skipped. They're the most expensive part of a
//      performance run and the report only reads the score plus the five metrics
//      below, so the screenshots were captured, encoded, and thrown away.

import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

import * as chromeLauncher from "chrome-launcher";
import lighthouse from "lighthouse";
import desktopConfig from "lighthouse/core/config/desktop-config.js";

const scriptDir = path.dirname(fileURLToPath(import.meta.url));

const [baseUrl, outputDir] = process.argv.slice(2);

if (!baseUrl || !outputDir) {
    console.error("Usage: run-audits.mjs <base-url> <output-dir>");
    process.exit(1);
}

const pages = JSON.parse(fs.readFileSync(path.join(scriptDir, "pages.json"), "utf8"));

const settings = {
    onlyCategories: ["performance"],
    skipAudits: ["screenshot-thumbnails", "final-screenshot", "full-page-screenshot"],
};

const configs = {
    mobile: {
        extends: "lighthouse:default",
        settings,
    },
    desktop: {
        ...desktopConfig,
        settings: { ...desktopConfig.settings, ...settings },
    },
};

const chrome = await chromeLauncher.launch({
    chromeFlags: ["--headless", "--no-sandbox"],
});

let failures = 0;

try {
    for (const page of pages) {
        for (const device of Object.keys(configs)) {
            const url = `${baseUrl.replace(/\/$/, "")}${page.path}`;
            console.log(`Auditing ${page.name} (${device}): ${url}`);

            try {
                const result = await lighthouse(
                    url,
                    { port: chrome.port, output: "json", logLevel: "error" },
                    configs[device],
                );
                fs.writeFileSync(path.join(outputDir, `${page.key}-${device}.json`), result.report);
            } catch (err) {
                failures++;
                console.error(`Lighthouse failed for ${page.name} (${device}), continuing: ${err.message}`);
            }
        }
    }
} finally {
    await chrome.kill();
}

// Individual failures are tolerated — the report renders an "Error" row for any
// audit whose JSON is missing. Only bail if nothing at all succeeded.
if (failures === pages.length * Object.keys(configs).length) {
    console.error("All Lighthouse audits failed.");
    process.exit(1);
}
