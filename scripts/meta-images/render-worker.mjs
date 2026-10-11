// render-worker.mjs — worker_threads entry for parallel card rendering.
// Receives {type:"job", job:{mid,out,template,fields,w,h}} messages, renders the
// PNG with the shared render.mjs templates, writes it to `out`, and posts back
// {type:"result", mid, ok, ms} (or ok:false + err). Fonts load once per worker
// (loadFonts/titleFont memoize via once()). {type:"done"} exits the worker.

import { mkdirSync, writeFileSync } from "fs"
import { dirname } from "path"
import { parentPort } from "worker_threads"
import { renderPng } from "./render.mjs"
import { loadFonts } from "./lib.mjs"

const fonts = loadFonts()

parentPort.on("message", async (msg) => {
  if (msg.type === "done") { process.exit(0) }
  const { mid, out, template, fields, w, h } = msg.job
  const t = Date.now()
  try {
    mkdirSync(dirname(out), { recursive: true })
    writeFileSync(out, await renderPng({ template, fields, w, h }, fonts))
    parentPort.postMessage({ type: "result", mid, ok: true, ms: Date.now() - t })
  } catch (err) {
    parentPort.postMessage({ type: "result", mid, ok: false, err: err?.message || String(err) })
  }
})
