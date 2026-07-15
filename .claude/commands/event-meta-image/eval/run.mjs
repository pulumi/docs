#!/usr/bin/env node
// run.mjs — headless LLM eval for the /event-meta-image skill.
//
// For each (fixture x model) it runs the skill non-interactively via
//   claude -p "/event-meta-image <prompt>" --model <id> --output-format json --dangerously-skip-permissions
// then asserts on the deterministic artifacts the model produced (the config.json
// it wrote + the five PNGs it rendered), NOT on any prose. This catches a model
// ignoring the skill's defaults — e.g. adding a button it shouldn't, dropping a
// speaker, or producing the wrong sizes.
//
// Usage:
//   node .claude/commands/event-meta-image/eval/run.mjs                  # core fixtures, target model (opus)
//   node .claude/commands/event-meta-image/eval/run.mjs --models haiku,sonnet,opus,fable   # cost spread
//   node .claude/commands/event-meta-image/eval/run.mjs --fixture button-requested
//   node .claude/commands/event-meta-image/eval/run.mjs --no-web        # skip live-web fixtures
//   node .claude/commands/event-meta-image/eval/run.mjs --web-strict    # let web fixtures gate the exit code
//   node .claude/commands/event-meta-image/eval/run.mjs --keep          # leave output dirs for inspection
//
// Exit code is non-zero if any *core* assertion failed for any tested model
// (web fixtures gate only under --web-strict; `soft` fixtures never gate).

import { readFileSync, existsSync, rmSync, readdirSync, mkdirSync } from "fs";
import zlib from "zlib";
import { spawnSync } from "child_process";
import { dirname, join, resolve } from "path";
import { fileURLToPath } from "url";

const HERE = dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = resolve(HERE, "../../../..");
const RENDERER = "scripts/meta-images/render-event.mjs";
const CLAUDE_BIN = process.env.CLAUDE_BIN || "claude";

// alias -> { id, in$/1M, out$/1M }. Output price dominates a generation task and
// drives the cost ranking; input price is shown for completeness.
const MODELS = {
    haiku: { id: "claude-haiku-4-5-20251001", in: 1, out: 5 },
    sonnet: { id: "claude-sonnet-5", in: 3, out: 15 },
    opus: { id: "claude-opus-4-8", in: 5, out: 25 },
    fable: { id: "claude-fable-5", in: 10, out: 50 },
};

const EXPECTED_SIZES = ["1200x628", "628x628", "1200x675", "1080x1080", "540x960"].sort();

// ---- args -------------------------------------------------------------------
const argv = process.argv.slice(2);
const getOpt = (name, def) => {
    const i = argv.indexOf(name);
    return i >= 0 && argv[i + 1] ? argv[i + 1] : def;
};
const hasFlag = name => argv.includes(name);
const models = getOpt("--models", "opus")
    .split(",")
    .map(s => s.trim())
    .filter(Boolean);
const fixtureFilter = getOpt("--fixture", null);
const noWeb = hasFlag("--no-web");
const webStrict = hasFlag("--web-strict");
const keep = hasFlag("--keep");

for (const m of models)
    if (!MODELS[m]) {
        console.error(`unknown model alias: ${m} (known: ${Object.keys(MODELS).join(", ")})`);
        process.exit(2);
    }

const spec = JSON.parse(readFileSync(join(HERE, "fixtures.json"), "utf-8"));
let fixtures = spec.fixtures;
if (fixtureFilter) {
    const want = new Set(fixtureFilter.split(",").map(s => s.trim()));
    fixtures = fixtures.filter(f => want.has(f.id));
}
if (noWeb) fixtures = fixtures.filter(f => !f.web);
if (!fixtures.length) {
    console.error("no fixtures selected");
    process.exit(2);
}

// ---- helpers ----------------------------------------------------------------
function pngSize(path) {
    const buf = readFileSync(path);
    if (buf.length < 24 || buf.readUInt32BE(0) !== 0x89504e47) return null; // not a PNG
    return `${buf.readUInt32BE(16)}x${buf.readUInt32BE(20)}`;
}

// Minimal PNG decoder (8-bit RGB/RGBA, non-interlaced — what resvg-js emits).
// Returns { width, height, ch, data } or null if unsupported/undecodable.
function decodePNG(path) {
    const buf = readFileSync(path);
    if (buf.length < 8 || buf.readUInt32BE(0) !== 0x89504e47) return null;
    let pos = 8,
        width = 0,
        height = 0,
        depth = 0,
        ctype = 0,
        interlace = 0;
    const idat = [];
    while (pos + 8 <= buf.length) {
        const len = buf.readUInt32BE(pos),
            type = buf.toString("ascii", pos + 4, pos + 8);
        const data = buf.subarray(pos + 8, pos + 8 + len);
        if (type === "IHDR") {
            width = data.readUInt32BE(0);
            height = data.readUInt32BE(4);
            depth = data[8];
            ctype = data[9];
            interlace = data[12];
        } else if (type === "IDAT") idat.push(data);
        else if (type === "IEND") break;
        pos += 12 + len;
    }
    if (depth !== 8 || interlace !== 0 || (ctype !== 6 && ctype !== 2)) return null;
    const ch = ctype === 6 ? 4 : 3;
    const raw = zlib.inflateSync(Buffer.concat(idat));
    const stride = width * ch,
        out = Buffer.alloc(height * stride);
    let ri = 0;
    for (let y = 0; y < height; y++) {
        const f = raw[ri++];
        for (let x = 0; x < stride; x++) {
            const rb = raw[ri++];
            const a = x >= ch ? out[y * stride + x - ch] : 0;
            const b = y > 0 ? out[(y - 1) * stride + x] : 0;
            const c = x >= ch && y > 0 ? out[(y - 1) * stride + x - ch] : 0;
            let v;
            switch (f) {
                case 0:
                    v = rb;
                    break;
                case 1:
                    v = rb + a;
                    break;
                case 2:
                    v = rb + b;
                    break;
                case 3:
                    v = rb + ((a + b) >> 1);
                    break;
                case 4: {
                    const p = a + b - c,
                        pa = Math.abs(p - a),
                        pb = Math.abs(p - b),
                        pc = Math.abs(p - c);
                    v = rb + (pa <= pb && pa <= pc ? a : pb <= pc ? b : c);
                    break;
                }
                default:
                    v = rb;
            }
            out[y * stride + x] = v & 0xff;
        }
    }
    return { width, height, ch, data: out };
}

// Count "ink" pixels (meaningfully off the #f5f5ff card background) in the
// partner-logo band of a 1200x628 landscape card — the strip to the right of
// the Pulumi mark + "+" separator, within the bottom logo row. A visible partner
// logo lands 3k-6k ink here; an invisible (white / dark-mode) logo lands ~0.
function partnerInk(img) {
    const { width, height, ch, data } = img;
    const x0 = Math.round(width * 0.24),
        x1 = Math.round(width * 0.62);
    const y0 = height - 90,
        y1 = height - 30;
    let n = 0;
    for (let y = y0; y < y1; y++)
        for (let x = x0; x < x1; x++) {
            const i = (y * width + x) * ch;
            if (Math.abs(data[i] - 245) + Math.abs(data[i + 1] - 245) + Math.abs(data[i + 2] - 255) > 60) n++;
        }
    return n;
}
const LOGO_VISIBLE_MIN = 400; // calibrated: visible logos ~3100-5600 ink, invisible = 0

function cacheGlob(basename) {
    const dir = join(HERE, "..", "assets", "logos");
    if (!existsSync(dir)) return [];
    return readdirSync(dir)
        .filter(f => f.replace(/\.[^.]+$/, "") === basename)
        .map(f => join(dir, f));
}
const rmCacheLogo = basename => cacheGlob(basename).forEach(p => rmSync(p, { force: true }));

function includesAll(hay, needles) {
    const h = (hay || "").toString().toLowerCase();
    return (needles || []).every(n => h.includes(n.toLowerCase()));
}

// Re-run the shared renderer once (1200x628) on the model-written config. This
// reproduces the skill's own resolution + render with the real resolver, so
// "could not resolve" warnings surface as a failure — and the produced PNG is
// reused for the logo-visibility check. Caller deletes `tmp`.
function renderProbe(cfgAbs) {
    const tmp = join(REPO_ROOT, ".context", "event-images", "eval", "_probe.png");
    const r = spawnSync("node", [RENDERER, "--config", cfgAbs, "--size", "1200x628", "--out", tmp], { cwd: REPO_ROOT, encoding: "utf-8" });
    const warned = /could not resolve/i.test((r.stderr || "") + (r.stdout || ""));
    return { tmp, rendered: r.status === 0, ok: r.status === 0 && !warned, detail: r.status !== 0 ? `renderer exit ${r.status}` : warned ? "could-not-resolve warning" : "" };
}

function runSkill(prompt, modelId, outRel) {
    const full = `/event-meta-image ${prompt.replace(/OUTDIR/g, outRel)}`;
    const r = spawnSync(CLAUDE_BIN, ["-p", full, "--model", modelId, "--output-format", "json", "--dangerously-skip-permissions"], {
        cwd: REPO_ROOT,
        encoding: "utf-8",
        timeout: 15 * 60 * 1000,
        maxBuffer: 64 * 1024 * 1024,
    });
    let cost = null,
        runErr = null;
    if (r.error) runErr = String(r.error);
    try {
        const j = JSON.parse(r.stdout);
        cost = typeof j.total_cost_usd === "number" ? j.total_cost_usd : null;
        if (j.is_error) runErr = runErr || "claude reported is_error";
    } catch {
        runErr = runErr || "could not parse claude --output-format json output";
    }
    return { cost, runErr };
}

// ---- assertions for one fixture run ----------------------------------------
function assertFixture(fx, outAbs) {
    const checks = [];
    const add = (name, ok, detail = "") => checks.push({ name, ok, detail });

    const cfgPath = join(outAbs, "config.json");
    if (!existsSync(cfgPath)) {
        add("config.json written", false, `missing at ${cfgPath}`);
        return checks;
    }
    add("config.json written", true);

    let cfg;
    try {
        cfg = JSON.parse(readFileSync(cfgPath, "utf-8"));
    } catch (e) {
        add("config.json parses", false, String(e));
        return checks;
    }
    add("config.json parses", true);

    const e = fx.expect || {};
    if (e.showButton !== undefined) add(`showButton == ${e.showButton}`, !!cfg.showButton === e.showButton, `got ${!!cfg.showButton}`);
    if (e.speakers !== undefined) {
        const n = (cfg.speakers || []).length;
        add(`speakers == ${e.speakers}`, n === e.speakers, `got ${n}`);
    }
    if (e.logosInclude)
        for (const needle of e.logosInclude) {
            const hit = (cfg.logos || []).some(l => l.toLowerCase().includes(needle.toLowerCase()));
            add(`logos include "${needle}"`, hit, hit ? "" : `got ${JSON.stringify(cfg.logos || [])}`);
        }
    if (e.additionalTextIncludes)
        for (const needle of e.additionalTextIncludes)
            add(`byline includes "${needle}"`, includesAll(cfg.additionalText, [needle]), `got ${JSON.stringify(cfg.additionalText || "")}`);

    // One card PNG per expected size (filename-agnostic). Ignore stray PNGs whose
    // size isn't a card size — the skill saves fetched source photos (headshots)
    // into the same dir per Step 3, and those must not count against the five cards.
    const pngs = existsSync(outAbs) ? readdirSync(outAbs).filter(f => f.endsWith(".png")) : [];
    const sizes = pngs.map(f => pngSize(join(outAbs, f))).filter(Boolean);
    const counts = {};
    for (const s of sizes) if (EXPECTED_SIZES.includes(s)) counts[s] = (counts[s] || 0) + 1;
    const allOnce = EXPECTED_SIZES.every(s => counts[s] === 1);
    const cardTotal = Object.values(counts).reduce((a, b) => a + b, 0);
    const nonCard = sizes.length - cardTotal;
    add(
        "five card PNGs at correct sizes",
        allOnce && cardTotal === 5,
        `card sizes: ${Object.keys(counts).sort().join(", ") || "none"}${nonCard ? ` (+${nonCard} non-card asset ignored)` : ""}`,
    );

    const probe = renderProbe(cfgPath);
    add("renders with no unresolved assets", probe.ok, probe.detail);

    // Logo visibility: a resolved logo can still be invisible (a white / dark-mode
    // asset on the near-white card). If a non-Pulumi partner logo is expected or
    // present, it must actually paint ink on the card — resolution alone isn't enough.
    const partnerExpected =
        (e.logosInclude || []).some(l => l.toLowerCase() !== "pulumi") || (cfg.logos || []).some(l => l.toLowerCase() !== "pulumi" && !l.toLowerCase().includes("/pulumi"));
    if (partnerExpected && probe.rendered) {
        const img = decodePNG(probe.tmp);
        if (!img) add("partner logo visible on card", true, "skipped — render not decodable");
        else {
            const n = partnerInk(img);
            add("partner logo visible on card", n >= LOGO_VISIBLE_MIN, `ink=${n} (min ${LOGO_VISIBLE_MIN})`);
        }
    }
    rmSync(probe.tmp, { force: true });

    return checks;
}

// ---- run --------------------------------------------------------------------
console.log(`repo: ${REPO_ROOT}`);
console.log(`models: ${models.join(", ")}   fixtures: ${fixtures.map(f => f.id).join(", ")}\n`);

const results = {}; // model -> { rows:[{fx, passed, gating, cost, checks}], cost }
let hardFail = false;

for (const alias of models) {
    const { id } = MODELS[alias];
    results[alias] = { rows: [], cost: 0 };
    console.log(`\n===== ${alias} (${id}) =====`);
    for (const fx of fixtures) {
        // With --keep, namespace output by model so every model's cards survive
        // (otherwise later models clobber earlier ones in the shared per-fixture dir).
        const outRel = keep ? join(spec.outBase, fx.id, alias) : join(spec.outBase, fx.id);
        const outAbs = join(REPO_ROOT, outRel);
        rmSync(outAbs, { recursive: true, force: true });
        mkdirSync(outAbs, { recursive: true });
        if (fx.web && fx.forceMissLogo) rmCacheLogo(fx.forceMissLogo); // force a real fetch

        process.stdout.write(`  ${fx.id} ... `);
        const { cost, runErr } = runSkill(fx.prompt, id, outRel);
        const checks = runErr ? [{ name: "skill run", ok: false, detail: runErr }] : assertFixture(fx, outAbs);

        if (fx.web && fx.forceMissLogo) rmCacheLogo(fx.forceMissLogo); // keep committed cache clean
        if (!keep) rmSync(outAbs, { recursive: true, force: true });

        const passed = checks.every(c => c.ok);
        // A fixture gates the exit code unless it's soft, or it's a web fixture and we're not in --web-strict.
        const gating = !fx.soft && (!fx.web || webStrict);
        if (!passed && gating) hardFail = true;
        if (cost != null) results[alias].cost += cost;

        const tag = fx.web ? "web" : "core";
        console.log(`${passed ? "PASS" : gating ? "FAIL" : "warn"} (${tag}${cost != null ? `, $${cost.toFixed(4)}` : ""})`);
        for (const c of checks) if (!c.ok) console.log(`      ✗ ${c.name}${c.detail ? ` — ${c.detail}` : ""}`);
        results[alias].rows.push({ fx, passed, gating, cost, checks });
    }
}

// ---- summary + cost ranking -------------------------------------------------
console.log(`\n\n===== summary =====`);
const rank = models
    .map(alias => {
        const rows = results[alias].rows;
        const core = rows.filter(r => !r.fx.web);
        const web = rows.filter(r => r.fx.web);
        const corePass = core.filter(r => r.passed).length;
        const webPass = web.filter(r => r.passed).length;
        return {
            alias,
            corePass,
            coreTotal: core.length,
            webPass,
            webTotal: web.length,
            allCore: corePass === core.length,
            cost: results[alias].cost,
            out: MODELS[alias].out,
        };
    })
    .sort((a, b) => (a.allCore !== b.allCore ? (a.allCore ? -1 : 1) : a.cost - b.cost));

const pad = (s, n) => String(s).padEnd(n);
console.log(`${pad("model", 9)}${pad("core", 8)}${pad("web", 8)}${pad("out $/1M", 10)}${pad("run $", 10)}verdict`);
for (const r of rank) {
    const verdict = r.allCore ? "core PASS" : "core FAIL";
    console.log(
        `${pad(r.alias, 9)}${pad(`${r.corePass}/${r.coreTotal}`, 8)}${pad(r.webTotal ? `${r.webPass}/${r.webTotal}` : "-", 8)}${pad(`$${r.out}`, 10)}${pad(
            `$${r.cost.toFixed(4)}`,
            10,
        )}${verdict}`,
    );
}
const cheapest = rank.find(r => r.allCore);
if (cheapest) console.log(`\nCheapest model passing all core fixtures: ${cheapest.alias} (out $${cheapest.out}/1M, this run $${cheapest.cost.toFixed(4)})`);
else console.log(`\nNo tested model passed all core fixtures.`);

process.exit(hardFail ? 1 : 0);
