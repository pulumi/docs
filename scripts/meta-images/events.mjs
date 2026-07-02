// events.mjs — the branded event / workshop social card.
//
// One Satori renderer (eventsTree) draws the card for any of the five output
// sizes from already-resolved inputs (text + photo/logo data-URIs + flags). It
// is shared by two callers:
//   - scripts/generate-meta-images.mjs (build): resolves inputs from event
//     frontmatter via eventFieldsFromFrontmatter -> the auto default (landscape
//     + square), ephemeral/gitignored.
//   - the /event-meta-image authoring skill (via scripts/meta-images/render-event.mjs):
//     resolves enriched inputs (external co-presenters + company logos) -> all
//     five committed PNGs + frontmatter overrides.
//
// Layout mirrors the Figma "Workshop / event images" component
// (file NxH2p90xxLGNxkPTGbZDMA): landscape = text column left + speakers right;
// square = text over speakers; portrait = speakers over text. The 1080x1080
// size reuses the square layout, scaled. Background accent lines come from the
// per-size events-lines-*.svg assets. Photos are color + circular on a violet
// ring (Satori can't reproduce the Figma duotone / mix-blend-luminosity).

import { join } from "path"
import {
  REPO_ROOT, ASSET_DIR, clean, h, fitTitle, clampText, titleTextStyle, titleFont, svgDataUri, fileToImage,
} from "./lib.mjs"

// --- Brand tokens (from the Figma frames / Pulumi palette) -------------------
const C = {
  bg: "#f5f5ff", // brand/violet-background
  title: "#1f1b21", // utility/foreground
  muted: "#6a6675", // utility/foreground-muted
  violet: "#5a30c5", // brand/violet-primary — overline, ring, button
  divider: "#dedbff", // brand/violet-muted — divider
  disc: "#e6e1fb", // speaker placeholder fill (light violet)
}

const LINES = {
  landscape: svgDataUri("events-lines-1200x628.svg"), // 1200x628 (also serves 1200x675, top-aligned)
  square: svgDataUri("events-lines-628x628.svg"), // 628x628 (also serves 1080x1080, scaled)
  portrait: svgDataUri("events-lines-540.svg"), // 540x512 accent band
}

// --- Per-size layout spec ----------------------------------------------------
// Three families. landscape (1200x628 / 1200x675) and portrait (540x960) render
// at their native scale; square (628x628 / 1080x1080) scales every dimension by
// s = w/628 so the 1080 card is a faithful enlargement of the 628 one.
function specFor(w, height) {
  const ratio = w / height
  if (w === 540 || ratio < 0.8) {
    return {
      family: "portrait", s: 1, bg: "portrait", padding: 40, mainGap: 23, textGap: 8,
      overline: { font: 20, ls: 1 }, secondary: { font: 30 }, title: { max: 40, min: 24, maxLines: 3 },
      additional: { font: 20 }, divider: 2, logoH: 40, speaker: 216, speakersRowH: 359,
      button: { h: 72, px: 20, font: 24 },
    }
  }
  if (Math.abs(ratio - 1) < 0.15) {
    const s = w / 628
    const r = (n) => Math.round(n * s)
    return {
      family: "square", s, bg: "square", padding: r(40), mainGap: r(16), textGap: r(8),
      overline: { font: r(20), ls: s }, secondary: { font: r(30) }, title: { max: r(40), min: r(24), maxLines: 3 },
      additional: { font: r(20) }, divider: Math.max(2, r(2)), logoH: r(44), speaker: r(224),
      button: { h: r(72), px: r(20), font: r(24) },
    }
  }
  return {
    family: "landscape", s: 1, bg: "landscape", padding: 40, mainGap: 29, textGap: 16, columnGap: 40,
    overline: { font: 24, ls: 1.2 }, secondary: { font: 36 }, title: { max: 64, min: 34, maxLines: 3 },
    additional: { font: 28 }, divider: 2, logoH: 44, speaker: 224,
    // Right gutter that keeps full-width (speaker-less) text clear of the
    // decorative accent lines in the top-right corner (they begin ~x1017).
    lineGutter: 220,
    button: { h: 82, px: 36, font: 32 },
  }
}

// --- Speakers (circular, color photo on a violet ring) -----------------------
// Photos overlap as an avatar stack — 3+ overlap by 30%, exactly 2 by a slighter
// 12%. stepF = per-additional-circle advance as a fraction of the circle size
// along the stacking axis.
const OVERLAP_F = 0.3 // 3+ photos
const OVERLAP2_F = 0.12 // exactly 2 photos (a slighter overlap)
const stepF = (n) => (n >= 3 ? 1 - OVERLAP_F : 1 - OVERLAP2_F)
const speakerStep = (S, n) => Math.round(S * stepF(n)) // center-to-center advance
const clusterExtent = (S, n) => (n ? S + (n - 1) * speakerStep(S, n) : 0)
// Largest circle (≤ base) such that N stacked fit within `avail`.
function fitSpeakerSize(n, avail, s, base) {
  if (n <= 1) return base
  const maxS = Math.floor(avail / (1 + (n - 1) * stepF(n)))
  return Math.max(Math.round(60 * s), Math.min(base, maxS))
}
function speakerCircle(uri, S, s) {
  const rw = Math.max(2, Math.round(3 * s)) // violet ring thickness
  const inner = S - 2 * rw
  return h("div", { style: { width: S, height: S, borderRadius: 9999, backgroundColor: uri ? C.violet : C.disc, display: "flex", alignItems: "center", justifyContent: "center", flexShrink: 0 } },
    uri ? h("img", { src: uri, width: inner, height: inner, style: { width: inner, height: inner, borderRadius: 9999, objectFit: "cover" } })
        : h("div", { style: { width: inner, height: inner, borderRadius: 9999, backgroundColor: C.disc } }))
}
// Up to five circular speakers. dir="column" stacks vertically (landscape column,
// per Figma); dir="row" stacks horizontally (square / portrait row). Circles
// overlap via a negative margin along the stacking axis (later siblings paint on
// top). The landscape left nudge is applied by the caller via the text width, so
// the photo↔text gap stays constant.
function speakerCluster(speakers, S, s, dir = "row") {
  const n = speakers.length
  if (!n) return null
  const col = dir === "column"
  const m = speakerStep(S, n) - S // between-circle margin (negative = overlap)
  return h("div", { style: { display: "flex", flexDirection: col ? "column" : "row", alignItems: "center", ...(col ? { height: clusterExtent(S, n) } : { width: clusterExtent(S, n) }) } },
    speakers.map((sp, i) =>
      h("div", { style: { display: "flex", ...(col ? { marginTop: i ? m : 0 } : { marginLeft: i ? m : 0 }) } },
        speakerCircle(sp.uri, S, s))))
}
// Landscape vertical-column left nudge, by photo count (per the design). Reserved
// on the right AND removed from the text width, so the text↔photo gap is constant.
const landscapeShift = (n) => (n <= 3 ? 20 : n === 4 ? 40 : 65)

// --- Logo lockup (Pulumi + optional company logos), scaled to logoH, joined by
// a muted "+" the way the co-branded case-study card does. ---------------------
function logosRow(logos, logoH, s) {
  const valid = (logos || []).filter((lg) => lg && lg.uri && lg.iw > 0 && lg.ih > 0)
  if (!valid.length) return null
  const children = []
  valid.forEach((lg, i) => {
    if (i) children.push(h("div", { style: { display: "flex", fontFamily: "Inter", fontSize: Math.round(logoH * 0.62), fontWeight: 400, lineHeight: 1, color: C.muted } }, "+"))
    const dw = Math.round((lg.iw / lg.ih) * logoH)
    children.push(h("img", { src: lg.uri, width: dw, height: logoH, style: { width: dw, height: logoH } }))
  })
  return h("div", { style: { display: "flex", alignItems: "center", gap: Math.round(20 * s) } }, children)
}

function buttonNode(text, spec) {
  return h("div", { style: { display: "flex", alignItems: "center", justifyContent: "center", backgroundColor: C.violet, borderRadius: Math.round(9 * spec.s), height: spec.button.h, paddingLeft: spec.button.px, paddingRight: spec.button.px } },
    h("div", { style: { fontFamily: "Inter", fontWeight: 400, fontSize: spec.button.font, color: C.bg } }, text))
}

// --- Text column (overline, secondary, fitted title, "With…", divider, logos,
// optional button). Shared by all three families; sizes come from spec. The
// title is sized to the leftover vertical space (columnH minus every other row),
// so it never clips in the tighter square / portrait stacks. ------------------
const ADDITIONAL_LH = 1.2
function mainColumn(fields, spec, font, textW, columnH) {
  const g = spec.mainGap
  const overlineH = fields.overline ? Math.ceil(spec.overline.font * 1.1) : 0
  const secondaryH = fields.secondaryTitle ? Math.ceil(spec.secondary.font * 1.1) : 0
  const additionalH = fields.additionalText ? Math.ceil(spec.additional.font * ADDITIONAL_LH * 2) : 0 // reserve 2 lines
  const logosH = fields.logos && fields.logos.length ? spec.logoH : 0
  const buttonH = fields.showButton ? spec.button.h : 0
  // Gaps between visible blocks: title + divider are always present.
  let nBlocks = 2
  for (const present of [overlineH, additionalH, logosH, buttonH]) if (present) nBlocks++
  const gaps = (nBlocks - 1) * g
  const reserved = overlineH + secondaryH + (secondaryH ? spec.textGap : 0) + additionalH + spec.divider + logosH + buttonH + gaps
  const titleBoxH = Math.max(spec.title.min * 1.1, columnH - reserved)

  const title = clean(fields.title)
  const fit = fitTitle(font, title, { maxFont: spec.title.max, minFont: spec.title.min, boxW: textW, boxH: titleBoxH })
  const titleStr = clampText(font, title, fit.fontSize, textW * 0.98, fit.lineClamp)

  const overlineEl = fields.overline
    ? h("div", { style: { fontFamily: "Monaspace Neon", fontSize: spec.overline.font, letterSpacing: spec.overline.ls, textTransform: "uppercase", color: C.violet, lineHeight: 1.1 } }, fields.overline)
    : null
  const secondaryEl = fields.secondaryTitle
    ? h("div", { style: { fontSize: spec.secondary.font, fontWeight: 600, lineHeight: 1.1, color: C.muted, letterSpacing: spec.secondary.font * -0.03, width: "100%" } }, fields.secondaryTitle)
    : null
  const titleEl = h("div", { style: { ...titleTextStyle(fit.fontSize, fit.lineClamp), color: C.title, width: "100%" } }, titleStr)
  const textBlock = h("div", { style: { display: "flex", flexDirection: "column", height: titleBoxH + (secondaryH ? secondaryH + spec.textGap : 0), justifyContent: "center", gap: spec.textGap, overflow: "hidden", width: "100%" } }, secondaryEl, titleEl)
  const additionalEl = fields.additionalText
    ? h("div", { style: { fontFamily: "Inter", fontWeight: 400, fontSize: spec.additional.font, lineHeight: ADDITIONAL_LH, color: C.title, display: "-webkit-box", WebkitBoxOrient: "vertical", WebkitLineClamp: 2, overflow: "hidden", width: "100%" } }, fields.additionalText)
    : null
  const dividerEl = h("div", { style: { width: "100%", height: spec.divider, backgroundColor: C.divider } })
  const logosEl = logosRow(fields.logos, spec.logoH, spec.s)
  const buttonEl = fields.showButton ? buttonNode(clean(fields.buttonText) || "Register", spec) : null
  return h("div", { style: { display: "flex", flexDirection: "column", alignItems: "flex-start", justifyContent: "center", gap: g, width: textW, height: columnH } }, overlineEl, textBlock, additionalEl, dividerEl, logosEl, buttonEl)
}

function bgNode(spec, w, height) {
  if (spec.bg === "landscape") return h("img", { src: LINES.landscape, width: 1200, height: 628, style: { position: "absolute", top: 0, left: 0, width: 1200, height: 628 } })
  if (spec.bg === "square") return h("img", { src: LINES.square, width: w, height: w, style: { position: "absolute", top: 0, left: 0, width: w, height: w } })
  return h("img", { src: LINES.portrait, width: 540, height: 512, style: { position: "absolute", top: 0, left: 0, width: 540, height: 512 } })
}

function frame(w, height, spec, content) {
  return h("div", { style: { position: "relative", width: w, height, display: "flex", flexDirection: "column", backgroundColor: C.bg, fontFamily: "Inter", overflow: "hidden", padding: spec.padding } },
    bgNode(spec, w, height),
    content)
}

// fields: { overline, title, secondaryTitle?, additionalText?, logos:[{uri,iw,ih}],
//           speakers:[{uri}], showButton?, buttonText? }
export async function eventsTree(fields, { w, h: height }) {
  const spec = specFor(w, height)
  const font = await titleFont()
  const innerW = w - 2 * spec.padding
  const innerH = height - 2 * spec.padding
  const speakers = (fields.speakers || []).filter((sp) => sp && sp.uri).slice(0, MAX_SPEAKERS)
  const n = speakers.length

  if (spec.family === "landscape") {
    // Speakers stack VERTICALLY on the right; shrink the circle so N fit the height.
    const sS = n ? fitSpeakerSize(n, innerH, spec.s, spec.speaker) : spec.speaker
    const colW = n ? sS : 0
    // The left nudge is reserved on the right AND removed from the text width, so
    // the photos move left while the text↔photo gap stays a constant columnGap.
    // With no speakers, reserve a gutter so the title clears the top-right lines.
    const shift = n ? landscapeShift(n) : 0
    const textW = n ? innerW - shift - spec.columnGap - colW : innerW - spec.lineGutter
    const main = mainColumn(fields, spec, font, textW, innerH)
    const right = n
      ? h("div", { style: { display: "flex", flexDirection: "column", justifyContent: "center", height: innerH, flexShrink: 0 } }, speakerCluster(speakers, sS, spec.s, "column"))
      : null
    return frame(w, height, spec,
      h("div", { style: { display: "flex", flexDirection: "row", alignItems: "center", width: innerW, height: innerH, gap: spec.columnGap } }, main, right))
  }

  // square / portrait: speakers in a HORIZONTAL row; shrink so N fit the width.
  const sS = n ? fitSpeakerSize(n, innerW, spec.s, spec.speaker) : spec.speaker
  const rowH = n ? sS : 0

  if (spec.family === "square") {
    const padTop = Math.round(20 * spec.s)
    const bottomH = n ? rowH + padTop : 0
    const main = mainColumn(fields, spec, font, innerW, innerH - bottomH)
    const bottom = n
      ? h("div", { style: { display: "flex", alignItems: "center", width: innerW, height: bottomH, paddingTop: padTop, flexShrink: 0 } }, speakerCluster(speakers, sS, spec.s))
      : null
    return frame(w, height, spec,
      h("div", { style: { display: "flex", flexDirection: "column", width: innerW, height: innerH } }, main, bottom))
  }

  // portrait: speakers on top, text below. A gap below the speaker row keeps the
  // text clear of the accent lines that curve down around the photo (space-between
  // pushes the text block to the bottom, mirroring the Figma frame).
  const topH = n ? spec.speakersRowH : 0
  const portraitGap = n ? 64 : 0
  const top = n
    ? h("div", { style: { display: "flex", alignItems: "center", width: innerW, height: topH, flexShrink: 0 } }, speakerCluster(speakers, sS, spec.s))
    : null
  const main = mainColumn(fields, spec, font, innerW, innerH - topH - portraitGap)
  return frame(w, height, spec,
    h("div", { style: { display: "flex", flexDirection: "column", width: innerW, height: innerH, justifyContent: speakers.length ? "space-between" : "flex-start" } }, top, main))
}

// --- Field builders / resolvers ----------------------------------------------
const MAX_SPEAKERS = 5 // photos shown; the byline lists every name regardless

// Byline. One or two presenters include their role/company ("Name - Role, Company"),
// since those fit; three or more list names only (with an Oxford comma, never
// "and N others"). The byline clamps to two lines if it runs long.
export function presentersLine(presenters) {
  const named = (presenters || []).filter((p) => p && clean(p.name))
  if (!named.length) return ""
  const withRole = (p) => { const r = clean(p.role); return r ? `${clean(p.name)} - ${r}` : clean(p.name) }
  if (named.length === 1) return `With ${withRole(named[0])}`
  if (named.length === 2) return `With ${withRole(named[0])} and ${withRole(named[1])}`
  const names = named.map((p) => clean(p.name))
  return `With ${names.slice(0, -1).join(", ")}, and ${names[names.length - 1]}`
}

// The build default's field builder: overline from fm.overline || event_type
// (uppercased), "With…" from presenters, Pulumi logo only, speakers = resolved
// presenter photos (skip blanks).
export function eventFieldsFromFrontmatter(fm, _id) {
  const presenters = Array.isArray(fm.presenters) ? fm.presenters : []
  const speakers = presenters
    .map((p) => p && resolvePhoto(p.photo))
    .filter(Boolean)
    .slice(0, MAX_SPEAKERS)
    .map((uri) => ({ uri }))
  return {
    overline: clean(fm.overline || fm.event_type || "").toUpperCase(),
    title: clean(fm.title),
    secondaryTitle: "",
    additionalText: presentersLine(presenters),
    logos: [resolveLogo("pulumi")].filter(Boolean),
    speakers,
    showButton: false,
  }
}

// static/ holds /images/... photos; content/ holds page-bundle photos published
// at /events/<slug>/<file> (e.g. a colocated co-presenter headshot).
const PHOTO_ROOTS = [join(REPO_ROOT, "static"), join(REPO_ROOT, "content"), REPO_ROOT]
const LOGO_ROOTS = [join(REPO_ROOT, "static", "logos"), join(REPO_ROOT, "static"), join(REPO_ROOT, "assets", "fingerprinted")]

// Resolve a presenter photo (frontmatter path, repo path, absolute path, or
// data: URI) to a data URI. External (web/LinkedIn) lookups are the skill's job.
export function resolvePhoto(pathOrName, extraRoots = []) {
  const img = fileToImage(pathOrName, { roots: [...extraRoots, ...PHOTO_ROOTS], fit: false })
  return img ? img.uri : null
}

// Resolve a company logo to { uri, iw, ih } (intrinsic dims; the renderer scales
// to its per-size logo height). "pulumi" maps to the bundled brand mark.
export function resolveLogo(pathOrName, extraRoots = []) {
  let src = pathOrName
  if (clean(pathOrName).toLowerCase() === "pulumi") src = join(ASSET_DIR, "pulumi-logo-horizontal-color-light.svg")
  const img = fileToImage(src, { roots: [...extraRoots, ...LOGO_ROOTS], maxH: 200, maxW: 4000, fit: true })
  return img ? { uri: img.uri, iw: img.iw, ih: img.ih } : null
}
