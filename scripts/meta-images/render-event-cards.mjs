// render-event-cards.mjs — render the DEFAULT event card in all five sizes
// straight from an event's frontmatter, with NO model / LLM involved.
//
// This is the mechanical equivalent of the /event-meta-image skill's default path:
// it maps frontmatter via eventFieldsFromFrontmatter (the SAME mapping the build
// uses) and renders the five committed sizes. Use it when you just want the default
// look from the event's title + presenters — the skill is only needed to ENRICH a
// card with people or partner logos that aren't in frontmatter (which needs a model
// to identify/search for them).
//
//   node scripts/meta-images/render-event-cards.mjs <slug-or-path-to-index.md> [--out <dir>]
//
// <slug-or-path> may be an event slug (resolved to content/events/<slug>/index.md)
// or a direct path to an index.md. Default --out is the event bundle dir (matching
// the skill's event-bound filenames); pass --out to write elsewhere (e.g. a preview
// folder) without touching the bundle. Frontmatter is never modified.

import { readFileSync, mkdirSync, writeFileSync } from "fs"
import { join, resolve, dirname, basename } from "path"
import matter from "gray-matter"
import satori from "satori"
import { Resvg } from "@resvg/resvg-js"
import { loadFonts } from "./lib.mjs"
import { eventsTree, eventFieldsFromFrontmatter } from "./events.mjs"

// Same size → filename mapping the skill writes for event-bound output.
const SIZES = [
  [1200, 628, "meta.png"],
  [628, 628, "meta-square.png"],
  [1200, 675, "meta-landscape-tall.png"],
  [1080, 1080, "meta-square-large.png"],
  [540, 960, "meta-portrait.png"],
]

function parseArgs(argv) {
  const out = { target: null, out: null }
  for (let i = 0; i < argv.length; i++) {
    if (argv[i] === "--out") out.out = argv[++i]
    else if (!out.target) out.target = argv[i]
  }
  return out
}

const args = parseArgs(process.argv.slice(2))
if (!args.target) {
  console.error("usage: render-event-cards.mjs <slug-or-path-to-index.md> [--out <dir>]")
  process.exit(2)
}

const idxPath = args.target.endsWith(".md")
  ? resolve(args.target)
  : resolve("content/events", args.target, "index.md")
const slug = basename(dirname(idxPath))
const fm = matter(readFileSync(idxPath, "utf-8")).data
const fields = eventFieldsFromFrontmatter(fm, slug)
if (!fields.title) { console.error(`no title in frontmatter: ${idxPath}`); process.exit(2) }

const outDir = args.out ? resolve(args.out) : dirname(idxPath)
mkdirSync(outDir, { recursive: true })
const fonts = loadFonts()

for (const [w, h, name] of SIZES) {
  const tree = await eventsTree(fields, { w, h })
  const svg = await satori(tree, { width: w, height: h, fonts })
  const png = new Resvg(svg, { fitTo: { mode: "width", value: w } }).render().asPng()
  writeFileSync(join(outDir, name), png)
  console.log(`rendered ${w}x${h} → ${join(outDir, name)}`)
}
