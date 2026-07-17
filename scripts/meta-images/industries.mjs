// industries.mjs — virtual pages for the case-study INDUSTRY term cards.
//
// Industry term pages (/case-studies/industry/<slug>/) are a taxonomy with no
// backing content file, so generate-meta-images.mjs can't discover them by
// walking content/. This module enumerates them instead: one card per industry
// in data/case_study_industries.yaml (the single source of truth the linter and
// the term-page templates also read). This is the case-study analogue of the
// blog term cards in terms.mjs.
//
// Each card uses the LIGHT docs-style card ("tutorial" template) — a "Case
// Studies" badge, an "Industry" corner label, and the industry name as the
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

// One virtual industry term page per entry in data/case_study_industries.yaml.
// The LIGHT "tutorial" card carries a "Case Studies" badge and an "Industry"
// corner label; the optional per-industry description fills the body under the
// title (omit it and the title stands alone, like the blog term cards).
export function industryPages() {
  const file = join(REPO_ROOT, "data", "case_study_industries.yaml")
  const industries = (yaml.load(readFileSync(file, "utf-8")) || {}).industries || []
  const pages = []
  for (const ind of industries) {
    if (!ind || !ind.id) continue
    pages.push({
      id: `industry/${ind.id}`,
      template: "tutorial",
      fields: {
        sectionLabel: "Case Studies",
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
