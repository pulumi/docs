// render.mjs — pure card rendering. Given a page's {template, fields, w, h},
// produce a PNG buffer. Extracted from generate-meta-images.mjs so the main
// generator AND the parallel render worker (render-worker.mjs) share one
// definition of the templates. No page discovery, cache, or I/O policy lives
// here — just Satori (HTML/CSS -> SVG) + resvg (SVG -> PNG).

import satori from "satori"
import { Resvg } from "@resvg/resvg-js"
import {
  h, fitTitle, clampText, titleTextStyle, badge, svgDataUri, titleFont,
} from "./lib.mjs"
import { eventsTree } from "./events.mjs"
import { blogTree } from "./blog.mjs"

export const CANVAS_W = 1200
export const CANVAS_H = 628

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

// --- Bundled SVG assets ------------------------------------------------------
const ACCENTS = svgDataUri("og-bg.svg")
const LINES_BOTTOM = svgDataUri("lines-bottom.svg")
const LOGO = svgDataUri("pulumi-logo-horizontal-color-dark.svg") // light text → dark cards
const LOGO_LIGHT = svgDataUri("pulumi-logo-horizontal-color-light.svg") // dark text → light cards
INFO_DARK.logo = LOGO
INFO_LIGHT.logo = LOGO_LIGHT

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

// Every template takes (fields, { w, h }). The fixed-size light/dark cards
// ignore the size arg (they hard-code CANVAS_W/H); only "events" honors it.
const TEMPLATES = {
  title: titleTree,
  info: (f) => infoTree(f, INFO_DARK),
  tutorial: (f) => infoTree(f, INFO_LIGHT),
  "case-study": caseStudyTree,
  events: eventsTree,
  blog: blogTree,
}

export async function renderPng(page, fonts) {
  const w = page.w || CANVAS_W
  const hgt = page.h || CANVAS_H
  const tree = await TEMPLATES[page.template](page.fields, { w, h: hgt })
  const svg = await satori(tree, { width: w, height: hgt, fonts })
  return new Resvg(svg, { fitTo: { mode: "width", value: w } }).render().asPng()
}
