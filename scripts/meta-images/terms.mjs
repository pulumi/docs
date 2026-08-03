// terms.mjs — virtual pages for the blog taxonomy TERM cards (category + tag
// + series).
//
// Category, tag, and series term pages (/blog/category/<id>/, /blog/tag/<slug>/,
// /blog/series/<slug>/) have no backing content file, so
// generate-meta-images.mjs can't discover them by walking content/. This module
// enumerates them instead: one card per blog category
// (data/blog_categories.yaml), one per distinct tag used by any
// content/blog/*/index.md, and one per series (data/blog_series.yml). Each is
// rendered with the DARK docs-style card ("info" template) — a "Blog" badge, a
// "Category"/"Tag"/"Series" corner label, and the term name as the title — so
// blog terms share the dark field of the blog-post cards (blog.mjs) with no new
// template.
//
// The id is BOTH the output path (assets/images/generated/<id>.png) and the
// runtime lookup key. partials/meta-image-key.html maps a term page to that key
// with `urlize .Data.Term`, so the slug produced here MUST match Hugo's urlize:
//   category/<id>   (category ids are already url-safe slugs)
//   tags/<urlize(tag)>
//   series/<slug>   (series slugs are already url-safe slugs)

import { readFileSync, readdirSync, statSync, existsSync } from "fs"
import { join } from "path"
import { createRequire } from "module"
import matter from "gray-matter"
import { REPO_ROOT, clean } from "./lib.mjs"

const require = createRequire(import.meta.url)
const yaml = require("js-yaml")

const CANVAS_W = 1200
const CANVAS_H = 628
const BLOG_DIR = join(REPO_ROOT, "content", "blog")

// Port of Hugo's `urlize` (helpers.URLize → MakePathSanitized) for term slugs.
// Lowercase; collapse whitespace to a single "-"; keep alphanumerics and the
// unreserved-ish set Hugo preserves (- _ . / ~ # @); percent-encode any other
// non-ASCII byte; drop every remaining ASCII punctuation. Leading/trailing
// hyphens are NOT trimmed (Hugo keeps them). Real blog tags are already slugs,
// so this is a pass-through for all but a couple (e.g. "ci/cd", "vb.net").
function urlize(s) {
  const lower = clean(s).toLowerCase().replace(/\s+/g, "-")
  let out = ""
  for (const ch of lower) {
    if (/[a-z0-9\-_.\/~#@]/.test(ch)) out += ch
    else if (ch.charCodeAt(0) > 127) out += encodeURIComponent(ch).toLowerCase()
  }
  return out
}

// Every distinct tag used by a published (non-draft) blog post, in first-seen
// order. Parsed with the same gray-matter walk the generator uses elsewhere.
function blogTags() {
  const seen = new Map() // slug -> display tag (first spelling wins)
  if (!existsSync(BLOG_DIR)) return seen
  for (const name of readdirSync(BLOG_DIR)) {
    const idx = join(BLOG_DIR, name, "index.md")
    if (!existsSync(idx) || !statSync(idx).isFile()) continue
    let fm
    try { fm = matter(readFileSync(idx, "utf-8")).data } catch { continue }
    if (fm.draft === true) continue
    const tags = Array.isArray(fm.tags) ? fm.tags : fm.tags != null ? [fm.tags] : []
    for (const t of tags) {
      const tag = clean(t)
      if (!tag) continue
      const slug = urlize(tag)
      if (slug && !seen.has(slug)) seen.set(slug, tag)
    }
  }
  return seen
}

// Human-readable title from a tag slug: split on "-"/"/" and title-case words
// (categories keep their proper `name` from the data file). Purely visual — the
// lookup key is the id, so this never affects which page finds the card.
const humanizeTag = (tag) =>
  clean(tag).split(/[-/]/).filter(Boolean).map((w) => w.charAt(0).toUpperCase() + w.slice(1)).join(" ")

// A term card page-object, matching the shape listPages() builds (the generator
// fills in mid/out/key). The DARK "info" card carries a "Blog" badge and a
// "Category"/"Tag"/"Series" corner label; no description → the title fills the
// body.
const termPage = (id, corner, title) => ({
  id,
  template: "info",
  fields: { sectionLabel: "Blog", subSectionLabel: corner, title: clean(title), description: "" },
  w: CANVAS_W,
  h: CANVAS_H,
})

// The virtual term pages: one per blog category, one per distinct tag, one per
// blog series, plus one for the /blog/series/ directory itself (backed by
// content/series/_index.md, which no content walk covers; meta-image-key.html
// resolves that page to the key "series").
export function termPages() {
  const pages = []

  const catsFile = join(REPO_ROOT, "data", "blog_categories.yaml")
  const cats = (yaml.load(readFileSync(catsFile, "utf-8")) || {}).categories || []
  for (const c of cats) {
    if (!c || !c.id) continue
    pages.push(termPage(`category/${c.id}`, "Category", c.name || c.id))
  }

  for (const [slug, tag] of blogTags()) {
    pages.push(termPage(`tags/${slug}`, "Tag", humanizeTag(tag)))
  }

  const seriesFile = join(REPO_ROOT, "data", "blog_series.yml")
  const series = (yaml.load(readFileSync(seriesFile, "utf-8")) || {}).series || []
  for (const s of series) {
    if (!s || !s.slug) continue
    pages.push(termPage(`series/${s.slug}`, "Series", s.title || humanizeTag(s.slug)))
  }
  pages.push(termPage("series", "", "All Series"))

  return pages
}
