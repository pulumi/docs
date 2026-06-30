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
// Templates (all from the Figma "Social assets — banners" file):
//   - "title"      — centered title on the LIGHT brand field (what-is, migrate,
//     partner, topics, and the case-studies index). Simple frame.
//   - "info"       — 4-field DARK docs card (section badge, corner label, title,
//     description) — docs only. Palette INFO_DARK; same layout as "tutorial".
//   - "tutorial"   — the docs card in LIGHT (palette INFO_LIGHT): "Tutorial" /
//     "Glossary" badge, the parent collection's name in the corner for
//     sub-pages, title + description.
//   - "case-study" — LIGHT co-branded card: Pulumi + customer logo lockup with a
//     right-aligned "CASE STUDY" badge and a large title (case-studies).
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
// v4: title flipped to LIGHT + optional label badge; added the case-study
//     template (co-branded Pulumi + customer logo lockup). info (docs) unchanged.
const OG_TEMPLATE_VERSION = "4"

const SAMPLE = !!process.env.OG_SAMPLE // one card per sampleGroupBy group
const ONLY = (process.env.OG_ONLY || "").split(",").map((s) => s.trim()).filter(Boolean)

const clean = (v) => (v == null ? "" : v.toString().trim())
// Drop a corner/sub label that just repeats the page's own title.
const dropIfEchoesTitle = (sub, title) => (sub && sub.trim().toLowerCase() === title.trim().toLowerCase() ? "" : sub)
// Lazy single-init memo. Caches the first result (a value or a promise) forever.
const once = (fn) => { let v, done = false; return () => (done ? v : ((v = fn()), (done = true), v)) }

// --- Brand colors (dark mode; inlined from the Pulumi brand palette) ---------
// Used only by the "info" template (docs). The light templates use LIGHT below.
const COLORS = {
  bg: "#231f33", // violet 50 (dark)
  fg: "#ffffff", // utility foreground
  violet: "#c3bdff", // violet 700 (dark) — badge bg, description, title accent
  serviceBlack: "#1f1b21",
  divider: "#492e8e", // violet muted (dark)
}

// --- Brand colors (light cards: "title" + "case-study"). Tokens from the Figma
// "Social assets — banners" light frames (file LL0EBmlsbsDRXFQbWnM16n). --------
const LIGHT = {
  bg: "#f5f5ff", // violet background
  fg: "#1f1b21", // utility foreground — title
  muted: "#6a6675", // utility foreground muted — description / sub-label
  badgeBg: "#5a30c5", // violet primary — badge fill
  badgeFg: "#ffffff", // on-violet text
  divider: "#dedbff", // violet muted — header divider
}

// Role-based palettes for the shared docs-style template (infoTree). INFO_DARK
// reproduces the original docs card byte-for-byte; INFO_LIGHT is the tutorials
// variant. logo is bundled in since the dark/light cards use different marks.
const INFO_DARK = { bg: COLORS.bg, fg: COLORS.fg, badgeBg: COLORS.violet, badgeFg: COLORS.serviceBlack, desc: COLORS.violet, divider: COLORS.divider, subLabel: COLORS.fg, logo: null }
const INFO_LIGHT = { bg: LIGHT.bg, fg: LIGHT.fg, badgeBg: LIGHT.badgeBg, badgeFg: LIGHT.badgeFg, desc: LIGHT.muted, divider: LIGHT.divider, subLabel: LIGHT.fg, logo: null }

// Docs nav-area labels, keyed by the top-level path segment under content/docs/.
const menuLabels = once(() => {
  const raw = yaml.load(readFileSync(join(REPO_ROOT, "data", "docs_menu_sections.yml"), "utf-8"))
  const out = {}
  for (const s of raw || []) if (s && s.menu) out[s.menu] = s.label
  return out
})

// Title of the tutorial collection a sub-page belongs to (e.g. for
// "tutorials/pulumi-fundamentals/create-a-pulumi-project" → "Pulumi
// Fundamentals", read from tutorials/pulumi-fundamentals/_index.md). Returns ""
// for root/standalone tutorials (< 3 path segments), which get no corner label.
const _collTitle = new Map()
function collectionTitle(id) {
  // Use the LOGICAL path: leaf bundles store a trailing "/index" in their id
  // (tutorials/foo/index), which must not count as a sub-page level — otherwise
  // a standalone tutorial reads its own index.md and labels itself.
  const parts = id.replace(/\/index$/, "").split("/") // tutorials/<collection>/<sub...>
  if (parts.length < 3) return ""
  const key = `${parts[0]}/${parts[1]}`
  if (_collTitle.has(key)) return _collTitle.get(key)
  let title = ""
  for (const f of ["_index.md", "index.md"]) {
    const p = join(CONTENT_DIR, parts[0], parts[1], f)
    if (existsSync(p)) { const d = matter(readFileSync(p, "utf-8")).data; title = clean(d.linktitle || d.title); break }
  }
  _collTitle.set(key, title)
  return title
}

// Shared shape for the plain centered-title sections (what-is + the small
// marketing sections). They differ only in name and recursion.
const titleSection = (name, recursive) => ({
  name,
  template: "title",
  recursive,
  fields: (fm) => ({ title: clean(fm.title) }),
  valid: (f) => !!f.title,
})

// --- Section configuration ---------------------------------------------------
// id is the content-relative path with .md and trailing /_index stripped, e.g.
// "what-is/what-is-yaml" or "docs/iac/concepts/inputs-outputs".
const SECTIONS = [
  titleSection("what-is", false),
  {
    name: "tutorials",
    template: "tutorial", // light docs-style card
    recursive: true,
    sampleGroupBy: (id) => id.split("/")[1] || "(root)",
    // Tutorial badge + the parent collection's name in the corner for sub-pages
    // (root/standalone tutorials get no corner label). Glossary entries live
    // under tutorials/ but are definitions, so they get a "Glossary" badge.
    fields: (fm, id) => {
      const glossary = /(^|\/)glossary(\/|$)/.test(id)
      const title = clean(fm.title)
      const sub = glossary ? "" : dropIfEchoesTitle(collectionTitle(id), title)
      return { sectionLabel: glossary ? "Glossary" : "Tutorial", subSectionLabel: sub, title, description: clean(fm.meta_desc) }
    },
    valid: (f) => !!f.title,
  },
  {
    name: "case-studies",
    // Section index → plain "Case Studies" title card; individual studies → the
    // co-branded case-study card.
    template: (fm, id) => (id === "case-studies" ? "title" : "case-study"),
    recursive: false,
    fields: (fm, id) =>
      id === "case-studies"
        ? { title: clean(fm.title) || "Case Studies" }
        : { title: clean(fm.title), companyLogo: customerLogo(fm.customer_logo) },
    // Individual studies need a resolvable customer logo; the root title card doesn't.
    valid: (f, t) => !!f.title && (t === "title" || !!f.companyLogo),
  },
  // Small marketing sections converted from off-brand meta images to light title cards.
  titleSection("migrate", true),
  titleSection("partner", true),
  titleSection("topics", true),
  {
    name: "docs",
    template: "info",
    recursive: true,
    sampleGroupBy: (id) => id.split("/")[1] || "(root)", // nav area
    fields: (fm, id) => {
      const title = clean(fm.title)
      // Hide the sub-section label on top-level landing pages, where the nav-area
      // label and the page title coincide.
      const sub = dropIfEchoesTitle(menuLabels()[id.split("/")[1]] || "", title)
      return { sectionLabel: "Docs", subSectionLabel: sub, title, description: clean(fm.meta_desc) }
    },
    valid: (f) => !!f.title,
  },
]

// --- Fonts: Satori needs TTF/OTF/WOFF (NOT woff2) ----------------------------
const FONT_SPECS = [
  { name: "Inter", file: join(FONT_DIR, "inter-regular.woff"), weight: 400, style: "normal" },
  { name: "Inter", file: join(FONT_DIR, "inter-semibold.woff"), weight: 600, style: "normal" },
  { name: "Monaspace Neon", file: join(ASSET_DIR, "monaspace-neon-regular.ttf"), weight: 400, style: "normal" },
]
const loadFonts = once(() => FONT_SPECS.map((s) => ({ name: s.name, data: readFileSync(s.file), weight: s.weight, style: s.style })))

// Inter Semibold parsed for title measurement (lazy: parsed on first render).
// once() caches the in-flight promise so the font is parsed exactly once.
const titleFont = once(async () => {
  const { default: opentype } = await import("opentype.js")
  const b = readFileSync(join(FONT_DIR, "inter-semibold.woff"))
  return opentype.parse(b.buffer.slice(b.byteOffset, b.byteOffset + b.byteLength))
})

const svgDataUri = (file) => `data:image/svg+xml;base64,${readFileSync(join(ASSET_DIR, file)).toString("base64")}`
const ACCENTS = svgDataUri("og-bg.svg")
const LINES_BOTTOM = svgDataUri("lines-bottom.svg")
const LOGO = svgDataUri("pulumi-logo-horizontal-color-dark.svg") // light text → dark cards
const LOGO_LIGHT = svgDataUri("pulumi-logo-horizontal-color-light.svg") // dark text → light cards
INFO_DARK.logo = LOGO
INFO_LIGHT.logo = LOGO_LIGHT

// --- Customer logo (case-study co-brand) -------------------------------------
// Resolve a frontmatter logo path ("/logos/customers/foo.svg") under static/ to
// a data URI + display dims scaled into the header lockup. Returns null when the
// asset is missing or an unsupported type, so the page is skipped (valid()).
function intrinsicSize(buf, lower) {
  if (lower.endsWith(".png")) {
    // PNG IHDR: width/height are big-endian uint32 at byte offsets 16 and 20.
    if (buf.length >= 24) return { w: buf.readUInt32BE(16), h: buf.readUInt32BE(20) }
  } else if (lower.endsWith(".svg")) {
    const s = buf.toString("utf-8")
    const vb = s.match(/viewBox\s*=\s*["']\s*[-\d.]+\s+[-\d.]+\s+([\d.]+)\s+([\d.]+)/i)
    if (vb) return { w: parseFloat(vb[1]), h: parseFloat(vb[2]) }
    const w = s.match(/\bwidth\s*=\s*["']([\d.]+)/i)
    const hh = s.match(/\bheight\s*=\s*["']([\d.]+)/i)
    if (w && hh) return { w: parseFloat(w[1]), h: parseFloat(hh[1]) }
  }
  return { w: 200, h: 60 } // fallback ratio
}
// Customer logos live under assets/fingerprinted/ (routed through Hugo's
// fingerprinted-img partial on the case-study page); a few also sit in static/.
const LOGO_ROOTS = [join(REPO_ROOT, "assets", "fingerprinted"), join(REPO_ROOT, "static")]
function customerLogo(p, { maxH = 52, maxW = 260 } = {}) {
  const rel = clean(p).replace(/^\//, "")
  if (!rel) return null
  const file = LOGO_ROOTS.map((r) => join(r, rel)).find((f) => existsSync(f))
  if (!file) return null
  const lower = rel.toLowerCase()
  const mime = lower.endsWith(".svg") ? "image/svg+xml" : lower.endsWith(".png") ? "image/png" : null
  if (!mime) return null
  const buf = readFileSync(file)
  const { w, h } = intrinsicSize(buf, lower)
  let dw = (w / h) * maxH, dh = maxH
  if (dw > maxW) { dw = maxW; dh = (h / w) * maxW }
  return { uri: `data:${mime};base64,${buf.toString("base64")}`, w: Math.round(dw), h: Math.round(dh) }
}

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
// Largest fontPx in [minFont,maxFont] whose wrapped title fits boxW. The line
// budget is either a fixed maxLines, or — when boxH is given — derived from the
// available height at each font size (90% of the box, leaving a margin). The
// returned lineClamp is a generous safety net (maxLines, or the full-height line
// count at the chosen size).
function fitTitle(font, title, { maxFont, minFont, boxW, maxLines, boxH, lsEm = -0.05 }) {
  const words = title.split(/\s+/).filter(Boolean)
  const heightLines = (f, frac) => Math.max(1, Math.floor((boxH * frac) / (1.1 * f)))
  for (let f = maxFont; f >= minFont; f--) {
    const lines = wrapLines(font, words, f, boxW * 0.98, lsEm)
    const widest = Math.max(0, ...lines.map((l) => lineWidth(font, l, f, lsEm)))
    const budget = boxH ? heightLines(f, 0.9) : maxLines
    if (widest <= boxW * 0.98 && lines.length <= budget) {
      return { fontSize: f, lineClamp: boxH ? heightLines(f, 1) : maxLines }
    }
  }
  return { fontSize: minFont, lineClamp: boxH ? heightLines(minFont, 1) : maxLines }
}
// Hard-truncate text to maxLines at fontPx/maxW, appending an ellipsis. Satori's
// -webkit-line-clamp doesn't reliably bound height inside a centered fixed box,
// so we clamp the string itself as a guarantee against overflow.
function clampText(font, text, fontPx, maxW, maxLines, lsEm = -0.05) {
  const words = text.split(/\s+/).filter(Boolean)
  const lines = wrapLines(font, words, fontPx, maxW, lsEm)
  if (lines.length <= maxLines) return text
  let last = lines[maxLines - 1]
  while (last.includes(" ") && lineWidth(font, `${last}…`, fontPx, lsEm) > maxW) {
    last = last.slice(0, last.lastIndexOf(" "))
  }
  return `${lines.slice(0, maxLines - 1).join(" ")} ${last}…`.trim()
}

// --- JSX-shaped tree helper (no React) ---------------------------------------
function h(type, props, ...children) {
  const flat = children.flat(Infinity).filter((c) => c !== null && c !== undefined && c !== false)
  return { type, props: { ...(props ?? {}), children: flat.length === 0 ? undefined : flat.length === 1 ? flat[0] : flat } }
}

// Rounded "pill" badge with uppercase mono label (section badge / "Case Study").
const badge = (text, bg, fg) =>
  h("div", { style: { display: "flex", alignItems: "center", justifyContent: "center", backgroundColor: bg, borderRadius: 9999, padding: "8px 18px" } },
    h("div", { style: { fontFamily: "Monaspace Neon", fontSize: 24, lineHeight: 1, letterSpacing: 1.2, textTransform: "uppercase", color: fg } }, text))

// Shared style for a clamped, centered-weight card title.
const titleTextStyle = (fontSize, lineClamp) => ({
  display: "-webkit-box", WebkitBoxOrient: "vertical", WebkitLineClamp: lineClamp,
  overflow: "hidden", fontSize, fontWeight: 600, lineHeight: 1.1, letterSpacing: -fontSize * 0.05,
})

// --- Template: "title" (what-is, migrate, partner, topics, case-studies index)
// — centered title on the light brand field. ----------------------------------
const T_PAD_X = 152
const T_BOX_W = CANVAS_W - 2 * T_PAD_X
const T_BOX_H = 363
async function titleTree(fields) {
  // Largest font (96..40) whose wrapped title fits 90% of the box height;
  // lineClamp uses the full-height line count as a safety net.
  const font = await titleFont()
  const fit = fitTitle(font, fields.title, { maxFont: 96, minFont: 40, boxW: T_BOX_W, boxH: T_BOX_H })
  return h("div", { style: { width: CANVAS_W, height: CANVAS_H, position: "relative", display: "flex", backgroundColor: LIGHT.bg, fontFamily: "Inter" } },
    h("img", { src: ACCENTS, width: CANVAS_W, height: CANVAS_H, style: { position: "absolute", top: 0, left: 0, width: CANVAS_W, height: CANVAS_H } }),
    h("div", { style: { position: "absolute", top: 45, left: 0, width: CANVAS_W, display: "flex", justifyContent: "center" } },
      h("img", { src: LOGO_LIGHT, height: 60, style: { height: 60 } })),
    h("div", { style: { position: "absolute", top: 122, left: 0, width: CANVAS_W, height: T_BOX_H, display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", padding: `0 ${T_PAD_X}px` } },
      h("div", { style: { ...titleTextStyle(fit.fontSize, fit.lineClamp), textOverflow: "ellipsis", color: LIGHT.fg, textAlign: "center" } }, fields.title)))
}

// --- Template: docs-style card — section-label badge, optional corner label,
// title, description. Palette-driven: INFO_DARK = "info" (docs); INFO_LIGHT =
// "tutorial" (tutorials). -----------------------------------------------------
const I_LEFT = 30
const I_W = 1140
const I_HEADER_TOP = 25 // scooted up 20px from the Figma 45
const I_HEADER_BOTTOM = I_HEADER_TOP + 60 + 24 + 1 // logo row + gap + divider
const I_LINES_TOP = CANVAS_H - 159 // top of the bottom accent strip
const SUB_LABEL_MAX = 30 // corner label char cap (mono); longer → ellipsis
async function infoTree(fields, P) {
  const { sectionLabel, title, description } = fields
  const subSectionLabel = fields.subSectionLabel && fields.subSectionLabel.length > SUB_LABEL_MAX
    ? `${fields.subSectionLabel.slice(0, SUB_LABEL_MAX - 1).trimEnd()}…`
    : fields.subSectionLabel
  const font = await titleFont()
  const maxLines = description ? 2 : 3
  const fit = fitTitle(font, title, { maxFont: 64, minFont: 40, boxW: I_W, maxLines })
  const titleText = clampText(font, title, fit.fontSize, I_W * 0.98, fit.lineClamp)
  const descText = description ? clampText(font, description, 32, 1088, 3, 0) : ""
  return h("div", { style: { width: CANVAS_W, height: CANVAS_H, position: "relative", display: "flex", backgroundColor: P.bg, fontFamily: "Inter" } },
    h("img", { src: LINES_BOTTOM, width: CANVAS_W, height: 159, style: { position: "absolute", left: 0, top: I_LINES_TOP, width: CANVAS_W, height: 159 } }),
    // Header (top): logo + section-label badge, corner label, divider.
    h("div", { style: { position: "absolute", top: I_HEADER_TOP, left: I_LEFT, width: I_W, display: "flex", flexDirection: "column", gap: 24 } },
      h("div", { style: { display: "flex", width: I_W, alignItems: "center", justifyContent: "space-between" } },
        h("div", { style: { display: "flex", alignItems: "center", gap: 24 } },
          h("img", { src: P.logo, width: 241, height: 60, style: { width: 241, height: 60 } }),
          sectionLabel ? badge(sectionLabel, P.badgeBg, P.badgeFg) : null),
        subSectionLabel ? h("div", { style: { fontFamily: "Monaspace Neon", fontSize: 28, letterSpacing: 1.4, textTransform: "uppercase", color: P.subLabel } }, subSectionLabel) : null),
      h("div", { style: { width: I_W, height: 1, backgroundColor: P.divider } })),
    // Body: title + description, vertically centered between header and lines.
    h("div", { style: { position: "absolute", left: I_LEFT, top: I_HEADER_BOTTOM, width: I_W, height: I_LINES_TOP - I_HEADER_BOTTOM, display: "flex", flexDirection: "column", justifyContent: "center", gap: 16 } },
      h("div", { style: { ...titleTextStyle(fit.fontSize, fit.lineClamp), color: P.fg } }, titleText),
      descText ? h("div", { style: { display: "-webkit-box", WebkitBoxOrient: "vertical", WebkitLineClamp: 3, overflow: "hidden", fontSize: 32, fontWeight: 400, lineHeight: 1.3, color: P.desc, width: 1088 } }, descText) : null))
}

// --- Template: "case-study" — co-branded header (Pulumi + customer logo on the
// left, "CASE STUDY" badge right) on the light field, with a large title that
// fills the area below the divider (no description). ---------------------------
async function caseStudyTree(fields) {
  const { title, companyLogo } = fields // companyLogo: { uri, w, h } | null
  const font = await titleFont()
  const fit = fitTitle(font, title, { maxFont: 92, minFont: 44, boxW: I_W, maxLines: 3 })
  const titleText = clampText(font, title, fit.fontSize, I_W * 0.98, fit.lineClamp)
  return h("div", { style: { width: CANVAS_W, height: CANVAS_H, position: "relative", display: "flex", backgroundColor: LIGHT.bg, fontFamily: "Inter" } },
    h("img", { src: LINES_BOTTOM, width: CANVAS_W, height: 159, style: { position: "absolute", left: 0, top: I_LINES_TOP, width: CANVAS_W, height: 159 } }),
    // Header: Pulumi + "+" + customer logo (left), "CASE STUDY" badge (right).
    h("div", { style: { position: "absolute", top: I_HEADER_TOP, left: I_LEFT, width: I_W, display: "flex", flexDirection: "column", gap: 24 } },
      h("div", { style: { display: "flex", width: I_W, alignItems: "center", justifyContent: "space-between", height: 60 } },
        h("div", { style: { display: "flex", alignItems: "center", gap: 24 } },
          h("img", { src: LOGO_LIGHT, height: 52, style: { height: 52 } }),
          companyLogo ? h("div", { style: { fontSize: 36, fontWeight: 400, lineHeight: 1, color: LIGHT.muted } }, "+") : null,
          companyLogo ? h("img", { src: companyLogo.uri, width: companyLogo.w, height: companyLogo.h, style: { width: companyLogo.w, height: companyLogo.h } }) : null),
        badge("Case Study", LIGHT.badgeBg, LIGHT.badgeFg)),
      h("div", { style: { width: I_W, height: 1, backgroundColor: LIGHT.divider } })),
    // Body: title only, vertically centered between header and bottom lines.
    h("div", { style: { position: "absolute", left: I_LEFT, top: I_HEADER_BOTTOM, width: I_W, height: I_LINES_TOP - I_HEADER_BOTTOM, display: "flex", flexDirection: "column", justifyContent: "center" } },
      h("div", { style: { display: "flex", fontSize: fit.fontSize, fontWeight: 600, lineHeight: 1.1, letterSpacing: -fit.fontSize * 0.05, color: LIGHT.fg } }, titleText)))
}

const TEMPLATES = {
  title: titleTree,
  info: (f) => infoTree(f, INFO_DARK),
  tutorial: (f) => infoTree(f, INFO_LIGHT),
  "case-study": caseStudyTree,
}

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
      const template = typeof sec.template === "function" ? sec.template(fm, id) : sec.template
      const fields = sec.fields(fm, id)
      if (!sec.valid(fields, template)) continue
      secPages.push({ id, section: sec.name, template, fields, out: join(OUT_ROOT, `${id}.png`) })
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
    const walkPng = (d) => {
      for (const n of existsSync(d) ? readdirSync(d) : []) {
        const f = join(d, n)
        if (statSync(f).isDirectory()) walkPng(f)
        else if (f.endsWith(".png") && !keep.has(f)) rmSync(f)
      }
    }
    walkPng(OUT_ROOT)
    for (const id of Object.keys(next)) if (!pages.find((p) => p.id === id)) delete next[id]
  }
  mkdirSync(OUT_ROOT, { recursive: true })
  writeFileSync(MANIFEST, JSON.stringify(next, Object.keys(next).sort(), 2) + "\n")
  const totalMs = Date.now() - t0
  console.log(`meta-images: ${rendered} rendered, ${skipped} cached, ${failures.length} failed | ${totalMs}ms total${rendered ? `, ${Math.round(renderMs / rendered)}ms avg` : ""}`)
  // Fail the build only on a total wipeout (every page failed) — a one-off bad
  // page shouldn't block a deploy; it just ships without its generated card.
  if (failures.length && failures.length === pages.length) process.exit(1)
}

const pages = listPages()
await runGenerate(pages)
