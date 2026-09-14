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
//   - "tutorial"   — the docs card in LIGHT (palette INFO_LIGHT). Used for the
//     case-study industry cards (meta-images/industries.mjs).
//   - "case-study" — LIGHT co-branded card: Pulumi + customer logo lockup with a
//     right-aligned "CASE STUDY" badge and a large title (case-studies).
//   - "events"     — per-size event / workshop card (see meta-images/events.mjs).
//   - "blog"       — DARK blog-post card: the post's feature image bled off the
//     right, faded into the field, with a "Blog" badge + title (meta-images/blog.mjs).
//
// Usage:
//   node scripts/generate-meta-images.mjs            # render changed cards (the build step)
//   make meta-images                                  # same, for local preview
//   OG_ONLY=docs OG_SAMPLE=1 node scripts/...         # one card per nav group (preview)

import { readFileSync, writeFileSync, mkdirSync, readdirSync, existsSync, rmSync, statSync } from "fs"
import { dirname, join, relative } from "path"
import { createHash } from "crypto"
import { Worker } from "worker_threads"
import { cpus } from "os"
import matter from "gray-matter"
import { createRequire } from "module"
import {
  REPO_ROOT, clean, once, intrinsicSize, loadFonts, titleFont,
} from "./meta-images/lib.mjs"
import { eventFieldsFromFrontmatter } from "./meta-images/events.mjs"
import { renderPng, CANVAS_W, CANVAS_H } from "./meta-images/render.mjs"
import { termPages } from "./meta-images/terms.mjs"
import { industryPages } from "./meta-images/industries.mjs"

const require = createRequire(import.meta.url)
const yaml = require("js-yaml")

const CONTENT_DIR = join(REPO_ROOT, "content")
const OUT_ROOT = join(REPO_ROOT, "assets", "images", "generated")
const MANIFEST = join(OUT_ROOT, ".manifest.json")

// Bump when any template changes visually so cached cards regenerate.
// v3: added the og-info (4-field) template + multi-template/recursive support.
// v4: title flipped to LIGHT + optional label badge; added the case-study
//     template (co-branded Pulumi + customer logo lockup). info (docs) unchanged.
// v5: extracted shared primitives to meta-images/lib.mjs (no visual change);
//     added the per-size "events" template + multi-size variants. The cache key
//     now folds in w/h, so this bump re-renders every section's cards once.
// v6: events card polish — vertical speaker stack on landscape, adaptive sizing,
//     no photo halo, 2-up gap (no overlap), role/company in the 1–2 person byline.
const OG_TEMPLATE_VERSION = "6"

// Per-template revision. Bump one of these — instead of OG_TEMPLATE_VERSION —
// when a change is confined to a single card template, so only that template's
// cards re-render and every other section keeps its cache.
//   events r2: byline measured/fitted rather than -webkit-line-clamp'd (it used
//     to be sliced mid-glyph), 3-line budget on square/portrait, names-only
//     byline on square.
const TEMPLATE_REVISION = { events: 2 }

const SAMPLE = !!process.env.OG_SAMPLE // one card per sampleGroupBy group
const ONLY = (process.env.OG_ONLY || "").split(",").map((s) => s.trim()).filter(Boolean)

// Drop a corner/sub label that just repeats the page's own title.
const dropIfEchoesTitle = (sub, title) => (sub && sub.trim().toLowerCase() === title.trim().toLowerCase() ? "" : sub)

// Docs nav-area labels, keyed by the top-level path segment under content/docs/.
const menuLabels = once(() => {
  const raw = yaml.load(readFileSync(join(REPO_ROOT, "data", "docs_menu_sections.yml"), "utf-8"))
  const out = {}
  for (const s of raw || []) if (s && s.menu) out[s.menu] = s.label
  return out
})

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
  {
    // Changelog entries (content/releases/changelog/<slug>.md) get the dark
    // docs "info" card with a "Releases" badge. Scoped to the changelog subtree
    // only — the /releases landing page is intentionally excluded (it gets a
    // custom meta_image later). The changelog _index has build.render=never (no
    // list page renders), so its card would never be referenced; skip it.
    name: "releases/changelog",
    template: "info",
    recursive: true,
    sampleGroupBy: () => "changelog",
    skip: (fm) => fm.build && fm.build.render === "never",
    fields: (fm) => ({ sectionLabel: "Releases", subSectionLabel: "", title: clean(fm.title), description: clean(fm.meta_desc) }),
    valid: (f) => !!f.title,
  },
  {
    // Event / workshop cards (content/events/<slug>/index.md leaf bundles).
    // Individual events → the events card in two sizes (landscape OG meta image
    // + square second og:image). The /events/ index page → a plain title card,
    // landscape only (same treatment as the case-studies index). The
    // /event-meta-image skill produces enriched, committed overrides.
    name: "events",
    template: (fm, id) => (id === "events" ? "title" : "events"),
    recursive: true,
    // Only the events card is size-aware; the title card renders landscape only.
    variantsFor: (template) =>
      template === "events"
        ? [{ suffix: "", w: 1200, h: 628 }, { suffix: ".square", w: 628, h: 628 }]
        : [{ suffix: "", w: 1200, h: 628 }],
    // OG_SAMPLE → one representative EVENT (both variants); exclude the index so
    // the sample exercises the events renderer, not the index title card.
    sampleGroupBy: (id) => (id === "events" ? null : "events"),
    // External events do publish an on-site page, but it's never linked (the
    // events list links straight to the external URL) and is meant to be
    // noindexed — not worth a card; the default og image covers it.
    skip: (fm) => fm.external === true,
    fields: (fm, id) => (id === "events" ? { title: clean(fm.title) } : eventFieldsFromFrontmatter(fm, id)),
    valid: (f) => !!f.title,
  },
  {
    // Blog-post cards (content/blog/<slug>/index.md leaf bundles). Each post's
    // feature_image is pinned to the right and faded into the dark field by the
    // blog template; posts with none get a generic art plate. Non-post pages
    // under blog/ (tag.md) get a generic card too; blog/_index.md
    // keeps its committed, designer-made meta_image and is skipped. A
    // page-level meta_image (custom override) still wins globally, so migrated
    // posts drop theirs.
    name: "blog",
    template: "blog",
    recursive: true,
    skip: (fm) => fm.draft === true,
    // One representative card per kind (with vs without a feature image).
    sampleGroupBy: (id, fields) => (fields.featurePath ? "feature" : "generic"),
    // featureHash folds the image bytes into the cache key so the card
    // regenerates when the feature image changes, while keeping the manifest
    // small (the base64 only exists transiently at render time).
    fields: (fm, id) => {
      const title = clean(fm.title)
      let featurePath = null, featureHash = ""
      const fi = clean(fm.feature_image)
      if (fi) {
        const file = join(CONTENT_DIR, dirname(id), fi.replace(/^\.?\//, ""))
        if (existsSync(file)) {
          featurePath = relative(CONTENT_DIR, file).replace(/\\/g, "/")
          featureHash = createHash("sha1").update(readFileSync(file)).digest("hex")
        }
      }
      return { title, featurePath, featureHash }
    },
    valid: (f) => !!f.title,
  },
]

// --- Customer logo (case-study co-brand) -------------------------------------
// Resolve a frontmatter logo path ("/logos/customers/foo.svg") under static/ to
// a data URI + display dims scaled into the header lockup. Returns null when the
// asset is missing or an unsupported type, so the page is skipped (valid()).
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
// The manifest/cache key is per-OUTPUT (mid = id + variant suffix), and folds in
// the rendered size so the two variants of one page never collide. `r` is the
// template's own revision; JSON.stringify drops it when undefined, so templates
// without one hash exactly as they did before TEMPLATE_REVISION existed.
function cacheKey(page) {
  return createHash("sha1").update(JSON.stringify({ t: page.template, f: page.fields, v: OG_TEMPLATE_VERSION, r: TEMPLATE_REVISION[page.template], w: page.w, h: page.h })).digest("hex")
}
function listPages() {
  const pages = []
  for (const sec of SECTIONS) {
    if (ONLY.length && !ONLY.includes(sec.name)) continue
    const dir = join(CONTENT_DIR, sec.name)
    if (!existsSync(dir)) continue
    const defaultVariants = [{ suffix: "", w: CANVAS_W, h: CANVAS_H }]
    let secPages = []
    for (const file of walkMd(dir, sec.recursive)) {
      const fm = matter(readFileSync(file, "utf-8")).data
      // A page-level meta_image overrides the generated card (see
      // partials/meta-image-url.html), so its generated card would be unused.
      if (clean(fm.meta_image)) continue
      if (sec.skip && sec.skip(fm)) continue
      const id = pageId(file)
      const template = typeof sec.template === "function" ? sec.template(fm, id) : sec.template
      const fields = sec.fields(fm, id)
      if (!sec.valid(fields, template)) continue
      // A section can vary output sizes per page (sec.variantsFor) or for all
      // pages (sec.variants); otherwise it renders the single landscape size.
      const variants = sec.variantsFor ? sec.variantsFor(template) : sec.variants || defaultVariants
      for (const v of variants) {
        const mid = id + v.suffix // manifest / cache id, one per output file
        secPages.push({ id, mid, section: sec.name, template, fields, w: v.w, h: v.h, out: join(OUT_ROOT, `${id}${v.suffix}.png`) })
      }
    }
    if (SAMPLE && sec.sampleGroupBy) {
      // One representative page per group (keeping all of its variants).
      // OG_SAMPLE_LEVEL=N picks a page N path levels below the group's
      // shallowest (0 = landing, 1 = one down).
      const level = parseInt(process.env.OG_SAMPLE_LEVEL || "0", 10)
      const groups = new Map()
      for (const p of secPages) {
        const g = sec.sampleGroupBy(p.id, p.fields)
        if (g == null) continue // excluded from sampling (e.g. a section index)
        if (!groups.has(g)) groups.set(g, [])
        groups.get(g).push(p)
      }
      const depth = (id) => id.split("/").length
      const chosen = new Set()
      for (const arr of groups.values()) {
        const ids = [...new Set(arr.map((p) => p.id))].sort((a, b) => depth(a) - depth(b) || a.localeCompare(b))
        chosen.add(ids.find((id) => depth(id) === depth(ids[0]) + level) || ids[0])
      }
      secPages = secPages.filter((p) => chosen.has(p.id))
    }
    for (const p of secPages) p.key = cacheKey(p)
    pages.push(...secPages)
  }
  // Virtual "terms" section: blog category/tag term pages and case-study
  // industry term pages have no backing file, so their page objects come from
  // termPages()/industryPages() rather than a content walk. They flow through
  // the same mid/out/key/prune machinery as file-backed pages.
  if (!ONLY.length || ONLY.includes("terms")) {
    for (const t of [...termPages(), ...industryPages()]) {
      const page = { id: t.id, mid: t.id, section: "terms", template: t.template, fields: t.fields, w: t.w, h: t.h, out: join(OUT_ROOT, `${t.id}.png`) }
      page.key = cacheKey(page)
      pages.push(page)
    }
  }
  return pages
}

function loadManifest() {
  if (!existsSync(MANIFEST)) return {}
  try { return JSON.parse(readFileSync(MANIFEST, "utf-8")) } catch { return {} }
}

// Card rendering is pure and CPU-bound (Satori + resvg), so a cold run — every
// card uncached, e.g. a fresh checkout or an OG_TEMPLATE_VERSION bump — fans out
// across worker threads. Small batches (the common incremental edit) render
// inline to skip the ~1s of worker startup. Override the worker count with
// OG_WORKERS; force inline with OG_WORKERS=1.
const WORKER_URL = new URL("./meta-images/render-worker.mjs", import.meta.url)
const MAX_WORKERS = Math.max(1, parseInt(process.env.OG_WORKERS || "", 10) || cpus().length - 1)
const PARALLEL_THRESHOLD = 8 // fewer cards than this → render inline

// Each job is the serializable subset of a page the worker needs. The worker
// renders + writes the PNG itself (avoids shipping buffers back) and posts a
// {mid, ok, ms|err} result. Every job settles exactly once; a crashed worker
// fails its in-flight job and, if all workers die, the queue's stragglers, so
// the pool never hangs. Resolves to the array of result records.
function renderPool(jobs, concurrency) {
  return new Promise((resolve) => {
    const results = []
    let next = 0
    let done = false
    if (!jobs.length) return resolve(results)
    const live = new Set()
    const inFlight = new Map() // worker -> job
    const settle = (res) => {
      results.push(res)
      if (results.length === jobs.length) { done = true; for (const w of live) w.terminate(); resolve(results) }
    }
    // Fail a dead worker's in-flight job (if any) and, once every worker is gone,
    // drain the rest of the queue so the pool can never hang. Idempotent per
    // worker via the `live` guard: a worker emits `error` then `exit`, so the
    // second event is a no-op. Skipped entirely once the pool has resolved (the
    // terminate() above makes every live worker emit a non-zero `exit`).
    const failWorker = (w, reason) => {
      if (done || !live.has(w)) return
      const job = inFlight.get(w)
      live.delete(w); inFlight.delete(w)
      if (job) settle({ mid: job.mid, ok: false, err: reason })
      if (!done && !live.size) while (next < jobs.length) settle({ mid: jobs[next++].mid, ok: false, err: "render worker pool exhausted" })
    }
    const pump = (w) => {
      if (next >= jobs.length) { inFlight.delete(w); return } // no work left; idle until the pool resolves
      const job = jobs[next++]
      inFlight.set(w, job)
      w.postMessage({ type: "job", job })
    }
    for (let i = 0; i < Math.min(concurrency, jobs.length); i++) {
      const w = new Worker(WORKER_URL)
      live.add(w)
      w.on("message", (msg) => {
        if (done || msg.type !== "result") return
        inFlight.delete(w)
        settle(msg)
        if (results.length < jobs.length) pump(w)
      })
      w.on("error", (err) => failWorker(w, err?.message || String(err)))
      // A worker that dies without an `error` (non-zero `exit` — e.g. OOM or a
      // native resvg crash) would otherwise leave its in-flight job dangling and
      // hang the pool; catch it here.
      w.on("exit", (code) => { if (code !== 0) failWorker(w, `render worker exited unexpectedly (code ${code})`) })
      pump(w)
    }
  })
}

async function runGenerate(pages) {
  const prev = loadManifest()
  const next = { ...prev }
  const todo = []
  let skipped = 0
  for (const p of pages) {
    next[p.mid] = p.key
    if (prev[p.mid] === p.key && existsSync(p.out)) { skipped++; continue }
    todo.push(p)
  }

  const t0 = Date.now()
  let results
  if (todo.length >= PARALLEL_THRESHOLD && MAX_WORKERS > 1) {
    const workers = Math.min(MAX_WORKERS, todo.length)
    console.log(`meta-images: rendering ${todo.length} cards across ${workers} worker${workers > 1 ? "s" : ""}…`)
    const jobs = todo.map((p) => ({ mid: p.mid, out: p.out, template: p.template, fields: p.fields, w: p.w, h: p.h }))
    results = await renderPool(jobs, workers)
  } else {
    // Small batch: render inline, skipping worker startup cost.
    const fonts = loadFonts()
    await titleFont()
    results = []
    for (const p of todo) {
      const t = Date.now()
      try {
        mkdirSync(dirname(p.out), { recursive: true })
        writeFileSync(p.out, await renderPng(p, fonts))
        results.push({ mid: p.mid, ok: true, ms: Date.now() - t })
      } catch (err) {
        results.push({ mid: p.mid, ok: false, err: err?.message || String(err) })
      }
    }
  }

  const rendered = results.filter((r) => r.ok).length
  const failures = results.filter((r) => !r.ok)
  const renderMs = results.reduce((s, r) => s + (r.ms || 0), 0)
  for (const f of failures) console.error(`  FAILED ${f.mid}: ${f.err}`)

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
    for (const mid of Object.keys(next)) if (!pages.find((p) => p.mid === mid)) delete next[mid]
  }
  mkdirSync(OUT_ROOT, { recursive: true })
  writeFileSync(MANIFEST, JSON.stringify(next, Object.keys(next).sort(), 2) + "\n")
  const totalMs = Date.now() - t0
  console.log(`meta-images: ${rendered} rendered, ${skipped} cached, ${failures.length} failed | ${totalMs}ms total${rendered ? `, ${Math.round(renderMs / rendered)}ms avg` : ""}`)
  // Fail the build only on a total wipeout (every attempted render failed) — a
  // one-off bad page shouldn't block a deploy; it just ships without its
  // generated card. Guard on todo (what we tried this run), not pages: an
  // incremental run leaves most pages cached, so a systemic render failure would
  // never reach pages.length and would ship green with missing cards.
  if (failures.length && failures.length === todo.length) process.exit(1)
}

const pages = listPages()
await runGenerate(pages)
