// generate-meta-images.mjs — branded OpenGraph card generator.
//
// Renders one 1200x628 social card per content page in the enabled SECTIONS
// using Satori (HTML/CSS -> SVG) + resvg (SVG -> PNG) and writes them to
// assets/images/generated/<path>.png (path mirrors the content path). Cards are
// EPHEMERAL: generated at build time (a step in scripts/build-site.sh, before
// Hugo) into a gitignored dir — not committed. CI persists the dir with
// actions/cache, and the manifest content-hash skip means only changed pages
// re-render. A page picks up its card automatically via
// partials/meta-image-url.html; a page-level `meta_image` overrides it.
//
// Two templates:
//   - "title" — centered title on the brand field (what-is). Ported from the
//     og-generic Satori template in pulumi/marketing-web.
//   - "info"  — 4-field card (section label, sub-section label, title,
//     description) from the Figma "Social assets — banners" template (docs).
//
// Usage:
//   node scripts/generate-meta-images.mjs            # render changed cards (the build step)
//   make meta-images                                  # same, for local preview
//   OG_ONLY=docs OG_SAMPLE=1 node scripts/...         # one card per nav group (preview)

import { readFileSync, writeFileSync, mkdirSync, readdirSync, existsSync, rmSync, statSync } from "fs"
import { resolve, dirname, join, relative } from "path"
import { fileURLToPath } from "url"
import { createHash } from "crypto"
import satori from "satori"
import { Resvg } from "@resvg/resvg-js"
import matter from "gray-matter"
import { createRequire } from "module"

const require = createRequire(import.meta.url)
const yaml = require("js-yaml")

const __dirname = dirname(fileURLToPath(import.meta.url))
const REPO_ROOT = resolve(__dirname, "..")

const ASSET_DIR = join(__dirname, "meta-images", "assets")
const FONT_DIR = join(REPO_ROOT, "static", "fonts")
const CONTENT_DIR = join(REPO_ROOT, "content")
const OUT_ROOT = join(REPO_ROOT, "assets", "images", "generated")
const MANIFEST = join(OUT_ROOT, ".manifest.json")

const CANVAS_W = 1200
const CANVAS_H = 628

// Bump when any template changes visually so cached cards regenerate.
// v3: added the og-info (4-field) template + multi-template/recursive support.
const OG_TEMPLATE_VERSION = "3"

const SAMPLE = !!process.env.OG_SAMPLE // one card per sampleGroupBy group
const ONLY = (process.env.OG_ONLY || "").split(",").map((s) => s.trim()).filter(Boolean)

// --- Brand colors (dark mode; inlined from the Pulumi brand palette) ---------
const COLORS = {
  bg: "#231f33", // violet 50 (dark)
  fg: "#ffffff", // utility foreground
  violet: "#c3bdff", // violet 700 (dark) — badge bg, description, title accent
  serviceBlack: "#1f1b21",
  divider: "#492e8e", // violet muted (dark)
}

// Docs nav-area labels, keyed by the top-level path segment under content/docs/.
let _menuLabels = null
function menuLabels() {
  if (_menuLabels) return _menuLabels
  const raw = yaml.load(readFileSync(join(REPO_ROOT, "data", "docs_menu_sections.yml"), "utf-8"))
  _menuLabels = {}
  for (const s of raw || []) if (s && s.menu) _menuLabels[s.menu] = s.label
  return _menuLabels
}

// --- Section configuration ---------------------------------------------------
// id is the content-relative path with .md and trailing /_index stripped, e.g.
// "what-is/what-is-yaml" or "docs/iac/concepts/inputs-outputs".
const SECTIONS = [
  {
    name: "what-is",
    template: "title",
    recursive: false,
    fields: (fm) => ({ title: clean(fm.title) }),
    valid: (f) => !!f.title,
  },
  {
    name: "docs",
    template: "info",
    recursive: true,
    sampleGroupBy: (id) => id.split("/")[1] || "(root)", // nav area
    fields: (fm, id) => {
      const title = clean(fm.title)
      let sub = menuLabels()[id.split("/")[1]] || ""
      // Hide the sub-section label when it just repeats the title (top-level
      // landing pages, where the nav-area label and the page title coincide).
      if (sub && sub.trim().toLowerCase() === title.trim().toLowerCase()) sub = ""
      return { sectionLabel: "Docs", subSectionLabel: sub, title, description: clean(fm.meta_desc) }
    },
    valid: (f) => !!f.title,
  },
]

const clean = (v) => (v == null ? "" : v.toString().trim())

// --- Fonts: Satori needs TTF/OTF/WOFF (NOT woff2) ----------------------------
const FONT_SPECS = [
  { name: "Inter", file: join(FONT_DIR, "inter-regular.woff"), weight: 400, style: "normal" },
  { name: "Inter", file: join(FONT_DIR, "inter-semibold.woff"), weight: 600, style: "normal" },
  { name: "Monaspace Neon", file: join(ASSET_DIR, "monaspace-neon-regular.ttf"), weight: 400, style: "normal" },
]
let _fonts = null
function loadFonts() {
  if (!_fonts) _fonts = FONT_SPECS.map((s) => ({ name: s.name, data: readFileSync(s.file), weight: s.weight, style: s.style }))
  return _fonts
}

// Inter Semibold parsed for title measurement (lazy: parsed on first render).
let _titleFont = null
async function titleFont() {
  if (!_titleFont) {
    const { default: opentype } = await import("opentype.js")
    const b = readFileSync(join(FONT_DIR, "inter-semibold.woff"))
    _titleFont = opentype.parse(b.buffer.slice(b.byteOffset, b.byteOffset + b.byteLength))
  }
  return _titleFont
}

const svgDataUri = (file) => `data:image/svg+xml;base64,${readFileSync(join(ASSET_DIR, file)).toString("base64")}`
const ACCENTS = svgDataUri("og-bg.svg")
const LINES_BOTTOM = svgDataUri("lines-bottom.svg")
const LOGO = svgDataUri("pulumi-logo-horizontal-color-dark.svg")

// --- Shared text measurement (opentype) --------------------------------------
function lineWidth(font, str, fontPx, lsEm = -0.05) {
  return font.getAdvanceWidth(str, fontPx, { kerning: false }) + lsEm * fontPx * Math.max(0, str.length - 1)
}
function wrapLines(font, words, fontPx, maxW, lsEm) {
  const lines = []
  let cur = ""
  for (const w of words) {
    const t = cur ? `${cur} ${w}` : w
    if (cur && lineWidth(font, t, fontPx, lsEm) > maxW) {
      lines.push(cur)
      cur = w
    } else cur = t
  }
  if (cur) lines.push(cur)
  return lines
}
// Largest fontPx in [minFont,maxFont] whose wrapped title fits boxW within
// maxLines. lineClamp is returned generous (maxLines) as a safety net.
function fitTitle(font, title, { maxFont, minFont, boxW, maxLines, lsEm = -0.05 }) {
  const words = title.split(/\s+/).filter(Boolean)
  for (let f = maxFont; f >= minFont; f--) {
    const lines = wrapLines(font, words, f, boxW * 0.98, lsEm)
    const widest = Math.max(0, ...lines.map((l) => lineWidth(font, l, f, lsEm)))
    if (widest <= boxW * 0.98 && lines.length <= maxLines) return { fontSize: f, lineClamp: maxLines }
  }
  return { fontSize: minFont, lineClamp: maxLines }
}

// --- JSX-shaped tree helper (no React) ---------------------------------------
function h(type, props, ...children) {
  const flat = children.flat(Infinity).filter((c) => c !== null && c !== undefined && c !== false)
  return { type, props: { ...(props ?? {}), children: flat.length === 0 ? undefined : flat.length === 1 ? flat[0] : flat } }
}

// --- Template: "title" (what-is) — centered title on the brand field ---------
const T_PAD_X = 152
const T_BOX_W = CANVAS_W - 2 * T_PAD_X
const T_BOX_H = 363
async function titleTree(fields) {
  // Largest font (96..40) whose wrapped title fits 90% of the box height;
  // lineClamp uses the full-height line count as a safety net.
  const font = await titleFont()
  const words = fields.title.split(/\s+/).filter(Boolean)
  let chosen = { fontSize: 40, lineClamp: Math.max(1, Math.floor(T_BOX_H / (1.1 * 40))) }
  for (let f = 96; f >= 40; f--) {
    const lines = wrapLines(font, words, f, T_BOX_W * 0.98)
    const widest = Math.max(0, ...lines.map((l) => lineWidth(font, l, f)))
    const fitLines = Math.max(1, Math.floor((T_BOX_H * 0.9) / (1.1 * f)))
    if (widest <= T_BOX_W * 0.98 && lines.length <= fitLines) { chosen = { fontSize: f, lineClamp: Math.max(1, Math.floor(T_BOX_H / (1.1 * f))) }; break }
  }
  return h("div", { style: { width: CANVAS_W, height: CANVAS_H, position: "relative", display: "flex", backgroundColor: COLORS.bg, fontFamily: "Inter" } },
    h("img", { src: ACCENTS, width: CANVAS_W, height: CANVAS_H, style: { position: "absolute", top: 0, left: 0, width: CANVAS_W, height: CANVAS_H } }),
    h("div", { style: { position: "absolute", top: 45, left: 0, width: CANVAS_W, display: "flex", justifyContent: "center" } },
      h("img", { src: LOGO, height: 60, style: { height: 60 } })),
    h("div", { style: { position: "absolute", top: 122, left: 0, width: CANVAS_W, height: T_BOX_H, display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", padding: `0 ${T_PAD_X}px` } },
      h("div", { style: { display: "-webkit-box", WebkitBoxOrient: "vertical", WebkitLineClamp: chosen.lineClamp, overflow: "hidden", textOverflow: "ellipsis", fontSize: chosen.fontSize, fontWeight: 600, lineHeight: 1.1, letterSpacing: -chosen.fontSize * 0.05, color: COLORS.fg, textAlign: "center" } }, fields.title)))
}

// --- Template: "info" (docs) — section label, sub-section, title, description -
const I_LEFT = 30
const I_W = 1140
const I_HEADER_TOP = 25 // scooted up 20px from the Figma 45
const I_HEADER_BOTTOM = I_HEADER_TOP + 60 + 24 + 1 // logo row + gap + divider
const I_LINES_TOP = CANVAS_H - 159 // top of the bottom accent strip
async function infoTree(fields) {
  const { sectionLabel, subSectionLabel, title, description } = fields
  const maxLines = description ? 2 : 3
  const fit = fitTitle(await titleFont(), title, { maxFont: 64, minFont: 40, boxW: I_W, maxLines })
  return h("div", { style: { width: CANVAS_W, height: CANVAS_H, position: "relative", display: "flex", backgroundColor: COLORS.bg, fontFamily: "Inter" } },
    h("img", { src: LINES_BOTTOM, width: CANVAS_W, height: 159, style: { position: "absolute", left: 0, top: I_LINES_TOP, width: CANVAS_W, height: 159 } }),
    // Header (top): logo + section-label badge, sub-section label, divider.
    h("div", { style: { position: "absolute", top: I_HEADER_TOP, left: I_LEFT, width: I_W, display: "flex", flexDirection: "column", gap: 24 } },
      h("div", { style: { display: "flex", width: I_W, alignItems: "center", justifyContent: "space-between" } },
        h("div", { style: { display: "flex", alignItems: "center", gap: 24 } },
          h("img", { src: LOGO, width: 241, height: 60, style: { width: 241, height: 60 } }),
          sectionLabel && h("div", { style: { display: "flex", alignItems: "center", justifyContent: "center", backgroundColor: COLORS.violet, borderRadius: 9999, padding: "8px 18px" } },
            h("div", { style: { fontFamily: "Monaspace Neon", fontSize: 24, lineHeight: 1, letterSpacing: 1.2, textTransform: "uppercase", color: COLORS.serviceBlack } }, sectionLabel))),
        subSectionLabel && h("div", { style: { fontFamily: "Monaspace Neon", fontSize: 28, letterSpacing: 1.4, textTransform: "uppercase", color: COLORS.fg } }, subSectionLabel)),
      h("div", { style: { width: I_W, height: 1, backgroundColor: COLORS.divider } })),
    // Body: title + description, vertically centered between header and lines.
    h("div", { style: { position: "absolute", left: I_LEFT, top: I_HEADER_BOTTOM, width: I_W, height: I_LINES_TOP - I_HEADER_BOTTOM, display: "flex", flexDirection: "column", justifyContent: "center", gap: 16 } },
      h("div", { style: { display: "-webkit-box", WebkitBoxOrient: "vertical", WebkitLineClamp: fit.lineClamp, overflow: "hidden", fontSize: fit.fontSize, fontWeight: 600, lineHeight: 1.1, letterSpacing: -fit.fontSize * 0.05, color: COLORS.fg } }, title),
      description && h("div", { style: { display: "-webkit-box", WebkitBoxOrient: "vertical", WebkitLineClamp: 3, overflow: "hidden", fontSize: 32, fontWeight: 400, lineHeight: 1.3, color: COLORS.violet, width: 1088 } }, description)))
}

const TEMPLATES = { title: titleTree, info: infoTree }

async function renderPng(page, fonts) {
  const tree = await TEMPLATES[page.template](page.fields)
  const svg = await satori(tree, { width: CANVAS_W, height: CANVAS_H, fonts })
  return new Resvg(svg, { fitTo: { mode: "width", value: CANVAS_W } }).render().asPng()
}

// --- Page discovery ----------------------------------------------------------
function walkMd(dir, recursive) {
  const out = []
  for (const name of readdirSync(dir)) {
    const full = join(dir, name)
    const st = statSync(full)
    if (st.isDirectory()) {
      if (recursive) out.push(...walkMd(full, true))
    } else if (name.endsWith(".md")) out.push(full)
  }
  return out
}
function pageId(file) {
  let rel = relative(CONTENT_DIR, file).replace(/\\/g, "/").replace(/\.md$/, "")
  return rel.replace(/\/_index$/, "")
}
function cacheKey(page) {
  return createHash("sha1").update(JSON.stringify({ t: page.template, f: page.fields, v: OG_TEMPLATE_VERSION })).digest("hex")
}
function listPages() {
  const pages = []
  for (const sec of SECTIONS) {
    if (ONLY.length && !ONLY.includes(sec.name)) continue
    const dir = join(CONTENT_DIR, sec.name)
    if (!existsSync(dir)) continue
    let secPages = []
    for (const file of walkMd(dir, sec.recursive)) {
      const fm = matter(readFileSync(file, "utf-8")).data
      // A page-level meta_image overrides the generated card (see
      // partials/meta-image-url.html), so its generated card would be unused.
      if (clean(fm.meta_image)) continue
      const id = pageId(file)
      const fields = sec.fields(fm, id)
      if (!sec.valid(fields)) continue
      secPages.push({ id, section: sec.name, template: sec.template, fields, out: join(OUT_ROOT, `${id}.png`) })
    }
    if (SAMPLE && sec.sampleGroupBy) {
      // One representative page per group. OG_SAMPLE_LEVEL=N picks a page N
      // path levels below the group's shallowest (0 = landing, 1 = one down).
      const level = parseInt(process.env.OG_SAMPLE_LEVEL || "0", 10)
      const groups = new Map()
      for (const p of secPages) {
        const g = sec.sampleGroupBy(p.id)
        if (!groups.has(g)) groups.set(g, [])
        groups.get(g).push(p)
      }
      const depth = (p) => p.id.split("/").length
      secPages = [...groups.values()].map((arr) => {
        arr.sort((a, b) => depth(a) - depth(b) || a.id.localeCompare(b.id))
        return arr.find((p) => depth(p) === depth(arr[0]) + level) || arr[0]
      })
    }
    for (const p of secPages) p.key = cacheKey(p)
    pages.push(...secPages)
  }
  return pages
}

function loadManifest() {
  if (!existsSync(MANIFEST)) return {}
  try { return JSON.parse(readFileSync(MANIFEST, "utf-8")) } catch { return {} }
}

async function runGenerate(pages) {
  const fonts = loadFonts()
  await titleFont()
  const prev = loadManifest()
  const next = { ...prev }
  let rendered = 0, skipped = 0, renderMs = 0
  const failures = []
  const t0 = Date.now()
  for (const p of pages) {
    next[p.id] = p.key
    if (prev[p.id] === p.key && existsSync(p.out)) { skipped++; continue }
    try {
      mkdirSync(dirname(p.out), { recursive: true })
      const t = Date.now()
      writeFileSync(p.out, await renderPng(p, fonts))
      renderMs += Date.now() - t
      rendered++
    } catch (err) {
      failures.push(p.id)
      console.error(`  FAILED ${p.id}: ${err?.message || err}`)
    }
  }
  // Prune only on full runs (not sample/only) to avoid deleting unrelated cards.
  if (!SAMPLE && !ONLY.length) {
    const keep = new Set(pages.map((p) => p.out))
    const walkPng = (d) => { for (const n of existsSync(d) ? readdirSync(d) : []) { const f = join(d, n); statSync(f).isDirectory() ? walkPng(f) : (f.endsWith(".png") && !keep.has(f) && rmSync(f)) } }
    walkPng(OUT_ROOT)
    for (const id of Object.keys(next)) if (!pages.find((p) => p.id === id)) delete next[id]
  }
  mkdirSync(OUT_ROOT, { recursive: true })
  writeFileSync(MANIFEST, JSON.stringify(next, Object.keys(next).sort(), 2) + "\n")
  const totalMs = Date.now() - t0
  console.log(`meta-images: ${rendered} rendered, ${skipped} cached, ${failures.length} failed | ${totalMs}ms total${rendered ? `, ${Math.round(renderMs / rendered)}ms avg` : ""}`)
  if (failures.length && failures.length === pages.length) process.exit(1)
}

const pages = listPages()
await runGenerate(pages)
