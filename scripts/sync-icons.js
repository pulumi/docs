#!/usr/bin/env node
/**
 * sync-icons.js
 *
 * Populates assets/icons/ from:
 *   - @phosphor-icons/core  → assets/icons/phosphor/{regular,bold,duotone}/
 *   - simple-icons          → assets/icons/brand/
 *   - svglogos.dev (CDN)    → assets/icons/brand/  (fallback for missing simple-icons entries)
 *
 * Run automatically by `make ensure` after yarn install.
 */

'use strict';

const fs = require('fs');
const path = require('path');
const https = require('https');

const ROOT = path.resolve(__dirname, '..');
const PHOSPHOR_SRC = path.join(ROOT, 'node_modules/@phosphor-icons/core/assets');
const ICONS_DEST = path.join(ROOT, 'assets/icons');

const PHOSPHOR_WEIGHTS = ['regular', 'bold', 'fill', 'duotone'];

/**
 * Brand icon allowlist.
 *
 * name            — output filename under assets/icons/brand/ (no .svg)
 * simpleIconsSlug — slug to look up in simple-icons (icon.slug); null = not available
 * svglogosUrl     — svglogos.dev URL used when simpleIconsSlug is null or not found
 */
const BRAND_ICONS = [
    { name: 'github',   simpleIconsSlug: 'github',   svglogosUrl: null },
    { name: 'youtube',  simpleIconsSlug: 'youtube',  svglogosUrl: null },
    { name: 'x',        simpleIconsSlug: 'x',        svglogosUrl: null },
    { name: 'readme',   simpleIconsSlug: 'readme',   svglogosUrl: null },
    { name: 'slack',    simpleIconsSlug: null,        svglogosUrl: 'https://cdn.svglogos.dev/logos/slack-icon.svg' },
    { name: 'linkedin', simpleIconsSlug: null,        svglogosUrl: 'https://cdn.svglogos.dev/logos/linkedin-icon.svg' },
    { name: 'bluesky',  simpleIconsSlug: 'bluesky',  svglogosUrl: null },
];

// ─── Utilities ───────────────────────────────────────────────────────────────

function ensureDir(dir) {
    fs.mkdirSync(dir, { recursive: true });
}

function rmDir(dir) {
    if (fs.existsSync(dir)) {
        fs.rmSync(dir, { recursive: true, force: true });
    }
}

/**
 * Strip weight suffix from a phosphor filename.
 * 'cloud-bold.svg'    (weight=bold)    → 'cloud.svg'
 * 'cloud-duotone.svg' (weight=duotone) → 'cloud.svg'
 * 'cloud.svg'         (weight=regular) → 'cloud.svg'
 */
function stripWeightSuffix(filename, weight) {
    if (weight === 'regular') return filename;
    const suffix = `-${weight}.svg`;
    if (filename.endsWith(suffix)) {
        return filename.slice(0, -suffix.length) + '.svg';
    }
    return filename;
}

/**
 * Inject CSS classes into a duotone SVG's paths.
 *   opacity="0.2" path → class="duotone-secondary"
 *   primary path       → class="duotone-primary"
 *
 * Phosphor duotone SVGs have exactly 2 self-closing <path .../> elements.
 */
function tagDuotonePaths(svg) {
    // Secondary path: has opacity="0.2" attribute
    svg = svg.replace(
        /(<path)([^>]*?) opacity="0\.2"([^>]*?)(\/?>)/g,
        '$1$2 opacity="0.2"$3 class="duotone-secondary"$4',
    );
    // Primary path: no class attribute yet
    svg = svg.replace(
        /(<path)(?![^>]*class=)([^>]*?)(\/?>)/g,
        '$1$2 class="duotone-primary"$3',
    );
    return svg;
}

/**
 * Normalise a brand SVG fetched from simple-icons.
 * - Remove the embedded <title> element (we handle a11y in the partial).
 * - simple-icons paths have no explicit fill; the SVG root already lacks fill
 *   so the partial's <svg> replacement will add fill="currentColor".
 */
function normaliseSimpleIconsSvg(svg) {
    return svg.replace(/<title>[^<]*<\/title>/g, '');
}

/**
 * Normalise a brand SVG fetched from svglogos.dev.
 * - Strip the XML declaration.
 * - Strip hard-coded fill="#..." attributes from all elements so they
 *   inherit currentColor from the injected <svg> wrapper.
 * - Remove width/height attributes from <svg> (keep viewBox).
 */
function normalisesvglogosSvg(svg) {
    // Strip XML declaration
    svg = svg.replace(/<\?xml[^?]*\?>\s*/g, '');
    // Strip hard-coded fill attributes on any element
    svg = svg.replace(/ fill="#[0-9a-fA-F]+"(?=[^>]*>)/g, '');
    // Strip width/height from the root <svg> element (they come before viewBox usually)
    svg = svg.replace(/(<svg[^>]*?) width="[^"]*"/g, '$1');
    svg = svg.replace(/(<svg[^>]*?) height="[^"]*"/g, '$1');
    return svg.trim();
}

/**
 * Fetch a URL and resolve with the response body as a string.
 * Follows HTTP 3xx redirects (up to 5 hops).
 */
function fetchUrl(url, redirectsLeft = 5) {
    return new Promise((resolve, reject) => {
        if (redirectsLeft === 0) {
            reject(new Error(`Too many redirects for ${url}`));
            return;
        }
        https.get(url, { timeout: 15000 }, (res) => {
            if (res.statusCode >= 300 && res.statusCode < 400 && res.headers.location) {
                res.resume();
                resolve(fetchUrl(res.headers.location, redirectsLeft - 1));
                return;
            }
            if (res.statusCode !== 200) {
                res.resume();
                reject(new Error(`HTTP ${res.statusCode} for ${url}`));
                return;
            }
            const chunks = [];
            res.on('data', (chunk) => chunks.push(chunk));
            res.on('end', () => resolve(Buffer.concat(chunks).toString('utf8')));
            res.on('error', reject);
        }).on('error', reject).on('timeout', function () {
            this.destroy(new Error(`Request timed out: ${url}`));
        });
    });
}

// ─── Phosphor sync ───────────────────────────────────────────────────────────

function syncPhosphorWeight(weight) {
    const srcDir = path.join(PHOSPHOR_SRC, weight);
    const destDir = path.join(ICONS_DEST, 'phosphor', weight);

    if (!fs.existsSync(srcDir)) {
        console.error(`  [phosphor] Source dir not found: ${srcDir}`);
        process.exit(1);
    }

    ensureDir(destDir);
    const files = fs.readdirSync(srcDir).filter(f => f.endsWith('.svg'));

    let count = 0;
    for (const file of files) {
        const outName = stripWeightSuffix(file, weight);
        let svg = fs.readFileSync(path.join(srcDir, file), 'utf8');

        if (weight === 'duotone') {
            svg = tagDuotonePaths(svg);
        }

        fs.writeFileSync(path.join(destDir, outName), svg);
        count++;
    }

    console.log(`  [phosphor/${weight}] ${count} icons`);
}

function syncPhosphor() {
    console.log('Syncing Phosphor icons…');
    rmDir(path.join(ICONS_DEST, 'phosphor'));

    for (const weight of PHOSPHOR_WEIGHTS) {
        syncPhosphorWeight(weight);
    }
}

// ─── Brand sync ──────────────────────────────────────────────────────────────

function loadSimpleIcons() {
    try {
        return require('simple-icons');
    } catch (e) {
        console.error('  [brand] Could not load simple-icons:', e.message);
        process.exit(1);
    }
}

async function syncBrand() {
    console.log('Syncing brand icons…');
    const brandDir = path.join(ICONS_DEST, 'brand');
    rmDir(brandDir);
    ensureDir(brandDir);

    const allSimpleIcons = Object.values(loadSimpleIcons());

    for (const entry of BRAND_ICONS) {
        const destFile = path.join(brandDir, `${entry.name}.svg`);
        let svg = null;

        // Try simple-icons first
        if (entry.simpleIconsSlug) {
            const icon = allSimpleIcons.find(i => i.slug === entry.simpleIconsSlug);
            if (icon) {
                svg = normaliseSimpleIconsSvg(icon.svg);
                console.log(`  [brand] ${entry.name} ← simple-icons`);
            } else {
                console.warn(`  [brand] WARN: simple-icons slug "${entry.simpleIconsSlug}" not found`);
            }
        }

        // Fall back to svglogos.dev
        if (!svg) {
            if (!entry.svglogosUrl) {
                console.error(`  [brand] ERROR: "${entry.name}" not found in simple-icons and no svglogosUrl configured`);
                process.exit(1);
            }
            try {
                const raw = await fetchUrl(entry.svglogosUrl);
                svg = normalisesvglogosSvg(raw);
                console.log(`  [brand] ${entry.name} ← svglogos.dev`);
            } catch (e) {
                console.error(`  [brand] ERROR: Failed to fetch ${entry.svglogosUrl}: ${e.message}`);
                console.error('  Network is required for brand icons not in simple-icons (slack, linkedin).');
                console.error('  Run `make ensure` with internet access, or pre-commit the fallback SVGs.');
                process.exit(1);
            }
        }

        fs.writeFileSync(destFile, svg);
    }

    console.log(`  [brand] ${BRAND_ICONS.length} icons`);
}

// ─── Main ─────────────────────────────────────────────────────────────────────

async function main() {
    console.log('=== sync-icons ===');
    ensureDir(ICONS_DEST);

    syncPhosphor();
    await syncBrand();

    console.log('=== done ===');
}

main().catch((e) => {
    console.error('sync-icons failed:', e);
    process.exit(1);
});
