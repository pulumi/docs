#!/usr/bin/env node
/**
 * build-icon-sprite.js
 *
 * Builds an SVG sprite (assets/icons/sprite.svg) plus a JSON manifest
 * (assets/icons/sprite-manifest.json) from the per-icon SVGs that
 * sync-icons.js writes to assets/icons/{phosphor,custom,brand}/.
 *
 * The set of icons included is determined by tokenising the source tree
 * (layouts, content, data, archetypes) and intersecting the resulting
 * tokens with the available icon basenames. We err on the side of
 * including too many icons rather than too few — false positives are
 * cheap (the sprite is a single fingerprinted asset) and a missing icon
 * breaks rendering.
 *
 * Symbol id scheme:
 *   p-{name}-{weight}  → phosphor (4 weights)
 *   c-{name}-{weight}  → custom   (4 weights; weights without a dedicated
 *                                  file fall back to the base SVG content)
 *   b-{name}           → brand    (single weight)
 *
 * Run automatically by `make ensure` after sync-icons.js.
 */

'use strict';

const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const ICONS_DIR = path.join(ROOT, 'assets/icons');
const PHOSPHOR_DIR = path.join(ICONS_DIR, 'phosphor');
const CUSTOM_DIR = path.join(ICONS_DIR, 'custom');
const BRAND_DIR = path.join(ICONS_DIR, 'brand');
const SPRITE_PATH = path.join(ICONS_DIR, 'sprite.svg');
const MANIFEST_PATH = path.join(ICONS_DIR, 'sprite-manifest.json');

const PHOSPHOR_WEIGHTS = ['regular', 'bold', 'fill', 'duotone'];
const CUSTOM_WEIGHTS = ['regular', 'bold', 'fill', 'duotone'];

// Directories whose contents define which icons are referenced.
const SCAN_DIRS = [
    path.join(ROOT, 'layouts'),
    path.join(ROOT, 'content'),
    path.join(ROOT, 'data'),
    path.join(ROOT, 'archetypes'),
];

const SCAN_EXTS = new Set(['.html', '.md', '.yml', '.yaml', '.toml', '.json']);

// Always-include list for icons referenced only via highly dynamic patterns
// (e.g. concatenated names, runtime data) that the tokeniser may miss.
// Add names here if a build error reports a missing icon symbol.
const FORCE_INCLUDE = new Set([
    // Defensive: every brand icon (cheap, ~7 entries).
    // (Brand names are short common words like "x" that the min-length
    // filter would otherwise drop.)
]);

// ─── Utilities ───────────────────────────────────────────────────────────────

function listSvgs(dir) {
    if (!fs.existsSync(dir)) return [];
    return fs.readdirSync(dir).filter(f => f.endsWith('.svg'));
}

function basenameNoExt(file) {
    return file.replace(/\.svg$/, '');
}

function stripWeightSuffix(name) {
    return name.replace(/-(bold|fill|duotone)$/, '');
}

/**
 * Walk a directory recursively, yielding files matching SCAN_EXTS.
 */
function* walk(dir) {
    if (!fs.existsSync(dir)) return;
    for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
        const full = path.join(dir, entry.name);
        if (entry.isDirectory()) {
            yield* walk(full);
        } else if (entry.isFile() && SCAN_EXTS.has(path.extname(entry.name))) {
            yield full;
        }
    }
}

/**
 * Tokenise text, yielding lowercase identifiers of length >= 2 that look
 * like icon names: [a-z][a-z0-9-]*.
 */
function tokenise(text) {
    const out = new Set();
    const re = /[a-z][a-z0-9]*(?:-[a-z0-9]+)*/g;
    const lower = text.toLowerCase();
    let m;
    while ((m = re.exec(lower)) !== null) {
        out.add(m[0]);
    }
    return out;
}

function buildTokenSet() {
    const tokens = new Set();
    for (const dir of SCAN_DIRS) {
        for (const file of walk(dir)) {
            const text = fs.readFileSync(file, 'utf8');
            for (const tok of tokenise(text)) {
                tokens.add(tok);
            }
        }
    }
    return tokens;
}

/**
 * Extract the inner content (children of <svg>) and the viewBox attribute
 * from a raw SVG string. Returns { inner, viewBox }.
 */
function extractSvg(svg) {
    const vbMatch = svg.match(/viewBox="([^"]+)"/);
    const viewBox = vbMatch ? vbMatch[1] : '0 0 256 256';

    // Strip the opening <svg ...> and closing </svg>.
    let inner = svg.replace(/^[\s\S]*?<svg\b[^>]*>/, '');
    inner = inner.replace(/<\/svg>\s*$/, '');
    return { inner: inner.trim(), viewBox };
}

function makeSymbol(id, viewBox, inner) {
    return `<symbol id="${id}" viewBox="${viewBox}">${inner}</symbol>`;
}

// ─── Build ───────────────────────────────────────────────────────────────────

function build() {
    console.log('=== build-icon-sprite ===');

    const tokens = buildTokenSet();
    console.log(`  scanned tokens: ${tokens.size}`);

    // Discover available icon basenames per family.
    const phosphorAvailable = new Set(
        listSvgs(path.join(PHOSPHOR_DIR, 'regular')).map(basenameNoExt),
    );
    const customAvailable = new Set(
        listSvgs(CUSTOM_DIR).map(basenameNoExt).map(stripWeightSuffix),
    );
    const brandAvailable = new Set(
        listSvgs(BRAND_DIR).map(basenameNoExt),
    );

    // Allowlist: intersection of tokens with available names.
    const phosphorWanted = new Set(
        [...phosphorAvailable].filter(n => tokens.has(n) || FORCE_INCLUDE.has(n)),
    );
    const customWanted = new Set(
        [...customAvailable].filter(n => tokens.has(n) || FORCE_INCLUDE.has(n)),
    );
    // Brand: include all (small list, names are short common words that
    // the min-length filter or context might miss).
    const brandWanted = new Set(brandAvailable);

    console.log(`  phosphor: ${phosphorWanted.size} / ${phosphorAvailable.size} included`);
    console.log(`  custom:   ${customWanted.size} / ${customAvailable.size} included`);
    console.log(`  brand:    ${brandWanted.size} / ${brandAvailable.size} included`);

    const symbols = [];

    // Phosphor: 4 weights per icon.
    for (const name of [...phosphorWanted].sort()) {
        for (const weight of PHOSPHOR_WEIGHTS) {
            const file = path.join(PHOSPHOR_DIR, weight, `${name}.svg`);
            if (!fs.existsSync(file)) continue;
            const { inner, viewBox } = extractSvg(fs.readFileSync(file, 'utf8'));
            symbols.push(makeSymbol(`p-${name}-${weight}`, viewBox, inner));
        }
    }

    // Custom: 4 weights per icon, falling back to the base SVG when a
    // weight-specific file does not exist.
    for (const name of [...customWanted].sort()) {
        const baseFile = path.join(CUSTOM_DIR, `${name}.svg`);
        const baseExists = fs.existsSync(baseFile);
        const baseSvg = baseExists ? fs.readFileSync(baseFile, 'utf8') : null;

        for (const weight of CUSTOM_WEIGHTS) {
            const suffix = weight === 'regular' ? '' : `-${weight}`;
            const file = path.join(CUSTOM_DIR, `${name}${suffix}.svg`);
            let raw;
            if (fs.existsSync(file)) {
                raw = fs.readFileSync(file, 'utf8');
            } else if (baseSvg) {
                raw = baseSvg;
            } else {
                continue;
            }
            const { inner, viewBox } = extractSvg(raw);
            symbols.push(makeSymbol(`c-${name}-${weight}`, viewBox, inner));
        }
    }

    // Brand: single symbol per icon.
    for (const name of [...brandWanted].sort()) {
        const file = path.join(BRAND_DIR, `${name}.svg`);
        if (!fs.existsSync(file)) continue;
        const { inner, viewBox } = extractSvg(fs.readFileSync(file, 'utf8'));
        symbols.push(makeSymbol(`b-${name}`, viewBox, inner));
    }

    // Wrap. display:none keeps the sprite from rendering if anyone ever
    // inlines it directly.
    const sprite =
        '<svg xmlns="http://www.w3.org/2000/svg" style="display:none">' +
        symbols.join('') +
        '</svg>\n';

    fs.writeFileSync(SPRITE_PATH, sprite);

    const manifest = {
        phosphor: [...phosphorWanted].sort(),
        custom: [...customWanted].sort(),
        brand: [...brandWanted].sort(),
    };
    fs.writeFileSync(MANIFEST_PATH, JSON.stringify(manifest, null, 2) + '\n');

    const kb = (sprite.length / 1024).toFixed(1);
    console.log(`  wrote ${path.relative(ROOT, SPRITE_PATH)} (${symbols.length} symbols, ${kb} KB)`);
    console.log(`  wrote ${path.relative(ROOT, MANIFEST_PATH)}`);
    console.log('=== done ===');
}

build();
