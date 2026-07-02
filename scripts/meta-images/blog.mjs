// blog.mjs — the branded blog-post social card.
//
// One Satori renderer (blogTree) draws the landscape 1200x628 OpenGraph card for
// a blog post from already-resolved inputs (title + optional feature-image path).
// It replaces the committed, skill-composited meta.png: blog posts now get a
// build-time card like docs / events / case-studies (via generate-meta-images.mjs).
//
// Layout mirrors the retired Python composite
// (.claude/commands/blog-*/scripts/compose_meta_image.py, "meta mode"): the
// post's feature image (1884x1256) is scaled to the full 628 height and pinned to
// the right so it bleeds off the right edge; a left-to-right violet-black gradient
// scrim fades it into the dark field; the "Blog" badge, the fitted title, and the
// Pulumi wordmark sit in the cleared left column. Posts with no feature_image fall
// back to a bundled generic art plate (blog-generic.png) — changing that asset is
// NOT reflected in the cache key (it isn't a field), so bump OG_TEMPLATE_VERSION
// if you swap it.

import { join } from "path"
import {
  REPO_ROOT, ASSET_DIR, clean, h, fitTitle, clampText, titleTextStyle,
  titleFont, badge, svgDataUri, fileToImage, once,
} from "./lib.mjs"

const CANVAS_W = 1200
const CANVAS_H = 628

// --- Brand tokens (dark field; same palette as the docs "info" card) ---------
const C = {
  bg: "#231f33", // violet 50 (dark) — canvas + gradient color
  title: "#ffffff", // utility foreground
  badgeBg: "#c3bdff", // violet 700 (dark) — "Blog" pill fill
  badgeFg: "#1f1b21", // service black — on-lavender text
}

// The Pulumi wordmark for the dark card (light-on-dark mark), height 44 (≈176
// wide at the mark's 425x106 aspect — visually identical to the retired 175x44
// meta-logo.png), sitting 40px above the bottom edge at the left margin.
const LOGO = svgDataUri("pulumi-logo-horizontal-color-dark.svg")
const LOGO_H = 44
const LOGO_W = Math.round((425 / 106) * LOGO_H) // 176

// Left-to-right scrim over the feature image: opaque bg to ~37.5%, fully
// transparent by ~54.5% (measured from the retired meta-overlay.png). Clears the
// left column so the badge/title/logo read on the dark field.
const SCRIM = "linear-gradient(90deg, rgba(35,31,51,1) 0%, rgba(35,31,51,1) 37.5%, rgba(35,31,51,0) 54.5%)"

// Bundled generic feature plate (1884x1256) for posts with no feature_image.
const genericImage = once(() =>
  fileToImage(join(ASSET_DIR, "blog-generic.png"), { fit: false }))

const LEFT = 90 // left margin (matches the retired composite)
const TITLE_TOP = 64
const TITLE_BOX_W = 700
const TITLE_BOX_H = 380

// fields: { title, featurePath? }  (featurePath is content-relative, e.g.
// "blog/<slug>/feature.png"; resolved lazily here so the base64 never lives in
// the manifest — the field carries only path + content hash).
export async function blogTree(fields) {
  const font = await titleFont()

  // Resolve the feature image (or the bundled generic plate) at render time.
  let img = fields.featurePath
    ? fileToImage(join(REPO_ROOT, "content", fields.featurePath), { fit: false })
    : null
  if (!img) img = genericImage()

  // Scale to the full canvas height and pin to the right so it bleeds off-edge,
  // reproducing the composite's placement (x=493 for a standard 3:2 plate).
  const dispW = img ? Math.round((img.iw / img.ih) * CANVAS_H) : CANVAS_W
  const left = CANVAS_W - dispW + 60 + 175

  const title = clean(fields.title)
  const fit = fitTitle(font, title, { maxFont: 96, minFont: 48, boxW: TITLE_BOX_W, boxH: TITLE_BOX_H })
  const titleStr = clampText(font, title, fit.fontSize, TITLE_BOX_W * 0.98, fit.lineClamp)

  return h("div", { style: { width: CANVAS_W, height: CANVAS_H, position: "relative", display: "flex", backgroundColor: C.bg, fontFamily: "Inter", overflow: "hidden" } },
    // Feature image (right-pinned, full height, clipped by the root overflow).
    img ? h("img", { src: img.uri, width: dispW, height: CANVAS_H, style: { position: "absolute", top: 0, left, width: dispW, height: CANVAS_H } }) : null,
    // Gradient scrim.
    h("div", { style: { position: "absolute", top: 0, left: 0, width: CANVAS_W, height: CANVAS_H, display: "flex", backgroundImage: SCRIM } }),
    // Left column: "Blog" badge + fitted title.
    h("div", { style: { position: "absolute", top: TITLE_TOP, left: LEFT, width: TITLE_BOX_W, display: "flex", flexDirection: "column", alignItems: "flex-start", gap: 24 } },
      badge("Blog", C.badgeBg, C.badgeFg),
      h("div", { style: { ...titleTextStyle(fit.fontSize, fit.lineClamp), color: C.title, width: TITLE_BOX_W } }, titleStr)),
    // Pulumi wordmark, bottom-left.
    h("img", { src: LOGO, width: LOGO_W, height: LOGO_H, style: { position: "absolute", top: CANVAS_H - LOGO_H - 40, left: LEFT, width: LOGO_W, height: LOGO_H } }))
}
