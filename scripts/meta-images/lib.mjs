// lib.mjs — shared primitives for the meta-image renderers.
//
// Renderer-agnostic helpers used by both scripts/generate-meta-images.mjs (the
// build-time card generator) and scripts/meta-images/events.mjs (the events
// card, shared by the generator and the /event-meta-image authoring skill).
// Keeping these here means there is exactly one copy of the JSX tree helper,
// the opentype text measurement, font loading, and image-sizing logic.

import { readFileSync, existsSync, statSync } from "fs"
import { resolve, dirname, join } from "path"
import { fileURLToPath } from "url"

const __dirname = dirname(fileURLToPath(import.meta.url))
export const REPO_ROOT = resolve(__dirname, "..", "..")
export const ASSET_DIR = join(__dirname, "assets")
export const FONT_DIR = join(REPO_ROOT, "static", "fonts")

export const clean = (v) => (v == null ? "" : v.toString().trim())
// Lazy single-init memo. Caches the first result (a value or a promise) forever.
export const once = (fn) => { let v, done = false; return () => (done ? v : ((v = fn()), (done = true), v)) }

// --- JSX-shaped tree helper (no React) ---------------------------------------
export function h(type, props, ...children) {
  const flat = children.flat(Infinity).filter((c) => c !== null && c !== undefined && c !== false)
  return { type, props: { ...(props ?? {}), children: flat.length === 0 ? undefined : flat.length === 1 ? flat[0] : flat } }
}

// --- Shared text measurement (opentype) --------------------------------------
export function lineWidth(font, str, fontPx, lsEm = -0.05) {
  return font.getAdvanceWidth(str, fontPx, { kerning: false }) + lsEm * fontPx * Math.max(0, str.length - 1)
}
export function wrapLines(font, words, fontPx, maxW, lsEm) {
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
export function fitTitle(font, title, { maxFont, minFont, boxW, maxLines, boxH, lsEm = -0.05 }) {
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
export function clampText(font, text, fontPx, maxW, maxLines, lsEm = -0.05) {
  const words = text.split(/\s+/).filter(Boolean)
  const lines = wrapLines(font, words, fontPx, maxW, lsEm)
  if (lines.length <= maxLines) return text
  let last = lines[maxLines - 1]
  while (last.includes(" ") && lineWidth(font, `${last}…`, fontPx, lsEm) > maxW) {
    last = last.slice(0, last.lastIndexOf(" "))
  }
  return `${lines.slice(0, maxLines - 1).join(" ")} ${last}…`.trim()
}

// Shared style for a clamped card title (negative letter-spacing tracks size).
export const titleTextStyle = (fontSize, lineClamp) => ({
  display: "-webkit-box", WebkitBoxOrient: "vertical", WebkitLineClamp: lineClamp,
  overflow: "hidden", fontSize, fontWeight: 600, lineHeight: 1.1, letterSpacing: -fontSize * 0.05,
})

// Rounded "pill" badge with uppercase mono label (section badge / "Case Study").
export const badge = (text, bg, fg) =>
  h("div", { style: { display: "flex", alignItems: "center", justifyContent: "center", backgroundColor: bg, borderRadius: 9999, padding: "8px 18px" } },
    h("div", { style: { fontFamily: "Monaspace Neon", fontSize: 24, lineHeight: 1, letterSpacing: 1.2, textTransform: "uppercase", color: fg } }, text))

// Sniff the real image type from magic bytes (NOT the file extension — some
// repo photos are PNGs saved as .jpg, which a decoder would reject if mislabeled).
export function sniffImageType(buf) {
  if (buf.length >= 4 && buf[0] === 0x89 && buf[1] === 0x50 && buf[2] === 0x4e && buf[3] === 0x47) return "png"
  if (buf.length >= 3 && buf[0] === 0xff && buf[1] === 0xd8 && buf[2] === 0xff) return "jpeg"
  if (buf.length >= 12 && buf.toString("ascii", 0, 4) === "RIFF" && buf.toString("ascii", 8, 12) === "WEBP") return "webp"
  const head = buf.slice(0, 512).toString("utf-8")
  if (head.includes("<svg") || (head.includes("<?xml") && head.includes("svg"))) return "svg"
  return null
}
const TYPE_MIME = { png: "image/png", jpeg: "image/jpeg", webp: "image/webp", svg: "image/svg+xml" }

// --- Image intrinsic size (for aspect-correct logo scaling) ------------------
// `lower` is kept for callers that pass it, but the format is detected from the
// bytes so a wrong/missing extension still resolves the right reader.
export function intrinsicSize(buf, _lower) {
  const t = sniffImageType(buf)
  if (t === "png" && buf.length >= 24) return { w: buf.readUInt32BE(16), h: buf.readUInt32BE(20) }
  if (t === "svg") {
    const s = buf.toString("utf-8")
    const vb = s.match(/viewBox\s*=\s*["']\s*[-\d.]+\s+[-\d.]+\s+([\d.]+)\s+([\d.]+)/i)
    if (vb) return { w: parseFloat(vb[1]), h: parseFloat(vb[2]) }
    const w = s.match(/\bwidth\s*=\s*["']([\d.]+)/i)
    const hh = s.match(/\bheight\s*=\s*["']([\d.]+)/i)
    if (w && hh) return { w: parseFloat(w[1]), h: parseFloat(hh[1]) }
  }
  if (t === "jpeg") {
    // Walk JPEG markers to the first SOF segment (width/height at payload+3/+1).
    for (let i = 2; i + 9 < buf.length;) {
      if (buf[i] !== 0xff) { i++; continue }
      const marker = buf[i + 1]
      if (marker >= 0xc0 && marker <= 0xcf && marker !== 0xc4 && marker !== 0xc8 && marker !== 0xcc) {
        return { h: buf.readUInt16BE(i + 5), w: buf.readUInt16BE(i + 7) }
      }
      if (marker === 0xd8 || marker === 0xd9 || (marker >= 0xd0 && marker <= 0xd7)) { i += 2; continue }
      i += 2 + buf.readUInt16BE(i + 2)
    }
  }
  return { w: 200, h: 60 } // fallback ratio
}

// Read a bundled asset (under ASSET_DIR) as a base64 SVG data URI.
export const svgDataUri = (file) => `data:image/svg+xml;base64,${readFileSync(join(ASSET_DIR, file)).toString("base64")}`

// Resolve an image file at any of `roots` (or an absolute/cwd-relative path) to
// a data URI plus sizes, scaled into a max box. Returns null when missing or an
// unsupported type. Used for customer/company logos and presenter photos. The
// result carries both the fitted display size (w/h) and the source's intrinsic
// size (iw/ih) so callers that scale to their own height can preserve aspect.
export function fileToImage(p, { roots = [], maxH = 52, maxW = 260, fit = true } = {}) {
  const raw = clean(p)
  if (!raw) return null
  if (raw.startsWith("data:")) return { uri: raw, w: maxW, h: maxH, iw: maxW, ih: maxH }
  const rel = raw.replace(/^\//, "")
  const candidates = [raw, ...roots.map((r) => join(r, rel))]
  const file = candidates.find((f) => f && existsSync(f) && statSync(f).isFile())
  if (!file) return null
  const buf = readFileSync(file)
  // Trust the bytes, not the extension (repo has PNGs named *.jpg, etc.).
  const type = sniffImageType(buf)
  const mime = type ? TYPE_MIME[type] : null
  if (!mime) return null
  const uri = `data:${mime};base64,${buf.toString("base64")}`
  const { w, h: ih } = intrinsicSize(buf, file.toLowerCase())
  if (!fit) return { uri, w: maxW, h: maxH, iw: w, ih }
  let dw = (w / ih) * maxH, dh = maxH
  if (dw > maxW) { dw = maxW; dh = (ih / w) * maxW }
  return { uri, w: Math.round(dw), h: Math.round(dh), iw: w, ih }
}

// --- Fonts: Satori needs TTF/OTF/WOFF (NOT woff2) ----------------------------
export const FONT_SPECS = [
  { name: "Inter", file: join(FONT_DIR, "inter-regular.woff"), weight: 400, style: "normal" },
  { name: "Inter", file: join(FONT_DIR, "inter-semibold.woff"), weight: 600, style: "normal" },
  { name: "Monaspace Neon", file: join(ASSET_DIR, "monaspace-neon-regular.ttf"), weight: 400, style: "normal" },
]
export const loadFonts = once(() => FONT_SPECS.map((s) => ({ name: s.name, data: readFileSync(s.file), weight: s.weight, style: s.style })))

// Inter Semibold parsed for title measurement (lazy: parsed on first render).
// once() caches the in-flight promise so the font is parsed exactly once.
export const titleFont = once(async () => {
  const { default: opentype } = await import("opentype.js")
  const b = readFileSync(join(FONT_DIR, "inter-semibold.woff"))
  return opentype.parse(b.buffer.slice(b.byteOffset, b.byteOffset + b.byteLength))
})
