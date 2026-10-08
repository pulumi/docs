#!/usr/bin/env node
// Screenshot one or more URLs (or local files) with Playwright's bundled
// Chromium. Used by act.py --render for the preview pages and by
// test_render.py / the skill to eyeball the board.
//
//   NODE_PATH=/opt/node22/lib/node_modules node screenshot.mjs OUT.png URL [--width 1280] [--height 900] [--dark] [--full]
//
// Playwright is not in the repo's node_modules; resolve it from NODE_PATH
// (the web session's global install) or a PLAYWRIGHT_MODULE path.
import { createRequire } from "node:module";
import path from "node:path";

const require = createRequire(import.meta.url);
function loadPlaywright() {
  const candidates = [process.env.PLAYWRIGHT_MODULE, "playwright", "/opt/node22/lib/node_modules/playwright"].filter(Boolean);
  for (const c of candidates) {
    try { return require(c); } catch (e) { /* try the next */ }
  }
  throw new Error("playwright not found; set NODE_PATH or PLAYWRIGHT_MODULE");
}

const args = process.argv.slice(2);
const positional = [];
const opts = { width: 1280, height: 900, dark: false, full: false };
for (let i = 0; i < args.length; i++) {
  const a = args[i];
  if (a === "--width") opts.width = parseInt(args[++i], 10);
  else if (a === "--height") opts.height = parseInt(args[++i], 10);
  else if (a === "--dark") opts.dark = true;
  else if (a === "--full") opts.full = true;
  else positional.push(a);
}
const [out, url] = positional;
if (!out || !url) {
  console.error("usage: screenshot.mjs OUT.png URL [--width N] [--height N] [--dark] [--full]");
  process.exit(2);
}
const target = /^https?:\/\//.test(url) ? url : "file://" + path.resolve(url);
const { chromium } = loadPlaywright();
const browser = await chromium.launch({ executablePath: process.env.CHROMIUM_PATH || undefined });
try {
  const page = await browser.newPage({ viewport: { width: opts.width, height: opts.height }, colorScheme: opts.dark ? "dark" : "light" });
  await page.goto(target, { waitUntil: "networkidle", timeout: 60000 }).catch(() => page.goto(target, { waitUntil: "load", timeout: 60000 }));
  await page.screenshot({ path: out, fullPage: opts.full });
  console.log(out);
} finally {
  await browser.close();
}
