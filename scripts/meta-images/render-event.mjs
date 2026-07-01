// render-event.mjs — CLI for the /event-meta-image authoring skill.
//
// Renders ONE event card at ONE size from a JSON config, using the shared
// eventsTree renderer. The skill writes a single config and loops the five
// sizes, e.g.:
//
//   node scripts/meta-images/render-event.mjs --config cfg.json --size 1200x628 --out meta.png
//
// Config schema (all fields optional except title):
//   {
//     "overline": "WORKSHOP",                // uppercased automatically
//     "title": "Advanced CI/CD for AWS",     // required
//     "secondaryTitle": "",                  // hidden unless set
//     "additionalText": "With Jane Doe - Staff Engineer, Acme",
//     "showButton": false,                   // "Register" pill, hidden by default
//     "buttonText": "Register",
//     "speakers": ["/images/people/jane.jpg", "/abs/path.png", "data:image/png;base64,..."],
//     "logos":    ["pulumi", "/abs/acme.svg"]   // "pulumi" → bundled brand mark
//   }
//
// Photo / logo entries resolve as: data: URI (passthrough) → path relative to
// the config file → repo path (/images/…, static/, assets/fingerprinted/, etc.)
// → absolute path. External (web/LinkedIn) lookups are the skill's job: it saves
// the file and passes the path here.

import { readFileSync, writeFileSync, mkdirSync } from "fs"
import { dirname, resolve } from "path"
import satori from "satori"
import { Resvg } from "@resvg/resvg-js"
import { loadFonts } from "./lib.mjs"
import { eventsTree, resolvePhoto, resolveLogo, presentersLine } from "./events.mjs"

function parseArgs(argv) {
  const out = {}
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i]
    if (a === "--config") out.config = argv[++i]
    else if (a === "--size") out.size = argv[++i]
    else if (a === "--out") out.out = argv[++i]
  }
  if (!out.config || !out.size || !out.out) {
    console.error("usage: render-event.mjs --config <cfg.json> --size <WxH> --out <file.png>")
    process.exit(2)
  }
  const m = /^(\d+)x(\d+)$/.exec(out.size.trim())
  if (!m) { console.error(`bad --size ${out.size} (expected WxH, e.g. 1200x628)`); process.exit(2) }
  out.w = parseInt(m[1], 10)
  out.h = parseInt(m[2], 10)
  return out
}

const args = parseArgs(process.argv.slice(2))
const cfgPath = resolve(args.config)
const cfgDir = dirname(cfgPath)
const cfg = JSON.parse(readFileSync(cfgPath, "utf-8"))

// Resolve photos / logos, with the config's directory as an extra search root
// so authors can drop assets next to the config and reference them relatively.
const speakers = (cfg.speakers || [])
  .map((p) => resolvePhoto(p, [cfgDir]))
  .filter(Boolean)
  .map((uri) => ({ uri }))
for (const p of cfg.speakers || []) if (!resolvePhoto(p, [cfgDir])) console.error(`  warning: could not resolve speaker photo: ${p}`)

const logos = (cfg.logos && cfg.logos.length ? cfg.logos : ["pulumi"])
  .map((p) => resolveLogo(p, [cfgDir]))
  .filter(Boolean)
for (const p of cfg.logos || []) if (!resolveLogo(p, [cfgDir])) console.error(`  warning: could not resolve logo: ${p}`)

// additionalText may be supplied directly, or derived from a presenters list.
const additionalText = cfg.additionalText != null ? cfg.additionalText
  : cfg.presenters ? presentersLine(cfg.presenters)
  : ""

const fields = {
  overline: (cfg.overline || "").toString().trim().toUpperCase(),
  title: (cfg.title || "").toString().trim(),
  secondaryTitle: (cfg.secondaryTitle || "").toString().trim(),
  additionalText,
  logos,
  speakers,
  showButton: !!cfg.showButton,
  buttonText: cfg.buttonText,
}

if (!fields.title) { console.error("config.title is required"); process.exit(2) }

const tree = await eventsTree(fields, { w: args.w, h: args.h })
const svg = await satori(tree, { width: args.w, height: args.h, fonts: loadFonts() })
const png = new Resvg(svg, { fitTo: { mode: "width", value: args.w } }).render().asPng()
mkdirSync(dirname(resolve(args.out)), { recursive: true })
writeFileSync(resolve(args.out), png)
console.log(`rendered ${args.w}x${args.h} → ${args.out}`)
