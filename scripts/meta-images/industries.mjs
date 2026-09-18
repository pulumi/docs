// industries.mjs — virtual pages for the customer INDUSTRY term cards.
//
// Industry term pages (/customers/industry/<slug>/) are a taxonomy whose
// backing content files are stubs under content/industry/, so
// generate-meta-images.mjs doesn't discover them by walking the sections it
// knows about. This module enumerates them instead: one card per industry in
// data/customers_industries.yaml (the single source of truth the linter and the
// term-page templates also read). This is the customer analogue of the blog
// term cards in terms.mjs.
//
// Each card uses the LIGHT docs-style card ("tutorial" template) — a
// "Customers" badge, an "Industry" corner label, and the industry name as the
// title — so industry cards share the light field of the case-study cards
// (the "case-study"/"title" templates) with no new template.
//
// The id is BOTH the output path (assets/images/generated/industry/<id>.png)
// and the runtime lookup key. partials/meta-image-key.html maps an industry
// term page to that key with `urlize .Data.Term`, so the slug produced here
// MUST match Hugo's urlize. Industry ids in the data file are already url-safe
// slugs (financial-services, ai-ml, …), so this is a pass-through.

import { readFileSync } from "fs"
import { join } from "path"
import { createRequire } from "module"
import { REPO_ROOT, clean } from "./lib.mjs"

const require = createRequire(import.meta.url)
const yaml = require("js-yaml")

const CANVAS_W = 1200
const CANVAS_H = 628

// One virtual industry term page per entry in data/customers_industries.yaml.
// The LIGHT "tutorial" card carries a "Customers" badge and an "Industry"
// corner label; the optional per-industry description fills the body under the
// title (omit it and the title stands alone, like the blog term cards).
export function industryPages() {
  const file = join(REPO_ROOT, "data", "customers_industries.yaml")
  const industries = (yaml.load(readFileSync(file, "utf-8")) || {}).industries || []
  const pages = []
  for (const ind of industries) {
    if (!ind || !ind.id) continue
    pages.push({
      id: `industry/${ind.id}`,
      template: "tutorial",
      fields: {
        sectionLabel: "Customers",
        subSectionLabel: "Industry",
        title: clean(ind.name) || ind.id,
        description: clean(ind.description),
      },
      w: CANVAS_W,
      h: CANVAS_H,
    })
  }
  return pages
}
