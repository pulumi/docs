#!/usr/bin/env node
import { Resvg } from '@resvg/resvg-js';
import fs from 'node:fs';
import path from 'node:path';

const DIR = 'assets/fingerprinted/logos/customers';
const MEASURE_WIDTH = 1000;
const EDGE_MARGIN_FRACTION = 0.01;
const MIN_INK_ALPHA = 8;
const TIGHT_ENOUGH = 0.02;

// resvg honours a root width/height pair over the viewBox, and a pair whose
// aspect disagrees letterboxes the raster, skewing the bbox mapping.
function sizedByViewBox(svg) {
  return svg.replace(/<svg\b[^>]*>/, tag =>
    tag.replace(/\s(?:width|height)="[^"]*"/g, ''));
}

function measure(svg) {
  const img = new Resvg(sizedByViewBox(svg), { fitTo: { mode: 'width', value: MEASURE_WIDTH }, background: 'rgba(0,0,0,0)' }).render();
  const { width: w, height: h } = img;
  const rgba = img.pixels;
  let minX = w, minY = h, maxX = -1, maxY = -1;
  for (let y = 0; y < h; y++) {
    for (let x = 0; x < w; x++) {
      if (rgba[(y * w + x) * 4 + 3] > MIN_INK_ALPHA) {
        if (x < minX) minX = x;
        if (x > maxX) maxX = x;
        if (y < minY) minY = y;
        if (y > maxY) maxY = y;
      }
    }
  }
  if (maxX < 0) return null;
  return { minX, minY, maxX, maxY, w, h };
}

function viewBox(svg) {
  const m = /viewBox\s*=\s*["']\s*([-\d.eE]+)[,\s]+([-\d.eE]+)[,\s]+([-\d.eE]+)[,\s]+([-\d.eE]+)\s*["']/.exec(svg);
  return m ? { raw: m[0], x: +m[1], y: +m[2], w: +m[3], h: +m[4] } : null;
}

const check = process.argv.includes('--check');
const ids = process.argv.slice(2).filter(a => !a.startsWith('--'));
if (ids.length === 0) {
  console.error('usage: node scripts/customers/trim-logo.mjs [--check] <id> [<id> ...]');
  process.exit(1);
}

function trimRaster(file, check, sharedCrop) {
  const png = fs.readFileSync(file);
  const w = png.readUInt32BE(16);
  const h = png.readUInt32BE(20);
  const wrapped = `<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="${w}" height="${h}">`
    + `<image width="${w}" height="${h}" xlink:href="data:image/png;base64,${png.toString('base64')}"/></svg>`;
  let crop = sharedCrop;
  if (!crop) {
    const b = measure(wrapped);
    if (!b) { console.error(`${path.basename(file)}: renders empty`); return null; }
    const pxPerSampleX = w / b.w, pxPerSampleY = h / b.h;
    crop = {
      left: Math.max(0, Math.round(b.minX * pxPerSampleX)),
      top: Math.max(0, Math.round(b.minY * pxPerSampleY)),
      right: Math.min(w, Math.round((b.maxX + 1) * pxPerSampleX)),
      bottom: Math.min(h, Math.round((b.maxY + 1) * pxPerSampleY)),
    };
  }
  const { left, top, right, bottom } = crop;
  const cw = right - left, ch = bottom - top;
  const trimmed = 1 - (cw * ch) / (w * h);
  const name = path.basename(file);
  if (check || trimmed < TIGHT_ENOUGH) {
    console.log(`${name.padEnd(30)} ${w}x${h} -> ${cw}x${ch}  (${(trimmed * 100).toFixed(0)}% padding)`);
    return crop;
  }
  const cropped = `<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="${cw}" height="${ch}" viewBox="${left} ${top} ${cw} ${ch}">`
    + `<image width="${w}" height="${h}" xlink:href="data:image/png;base64,${png.toString('base64')}"/></svg>`;
  const out = new Resvg(cropped, { fitTo: { mode: 'width', value: cw }, background: 'rgba(0,0,0,0)' }).render();
  fs.writeFileSync(file, out.asPng());
  console.log(`${name.padEnd(30)} ${w}x${h} -> ${cw}x${ch}  (trimmed ${(trimmed * 100).toFixed(0)}%)`);
  return crop;
}

for (const id of ids) {
  const raster = path.join(DIR, `${id}.png`);
  if (fs.existsSync(raster)) {
    const crop = trimRaster(raster, check);
    const rasterDark = path.join(DIR, `${id}-on-dark.png`);
    if (crop && fs.existsSync(rasterDark)) trimRaster(rasterDark, check, crop);
    continue;
  }
  for (const suffix of ['', '-on-dark']) {
    const file = path.join(DIR, `${id}${suffix}.svg`);
    if (!fs.existsSync(file)) continue;
    const svg = fs.readFileSync(file, 'utf8');
    const vb = viewBox(svg);
    if (!vb) { console.error(`${id}${suffix}: no viewBox`); continue; }
    let b;
    try { b = measure(svg); } catch (e) { console.error(`${id}${suffix}: ${e.message}`); continue; }
    if (!b) { console.error(`${id}${suffix}: renders empty`); continue; }

    const unitsPerPxX = vb.w / b.w, unitsPerPxY = vb.h / b.h;
    const marginX = (b.maxX - b.minX + 1) * unitsPerPxX * EDGE_MARGIN_FRACTION;
    const marginY = (b.maxY - b.minY + 1) * unitsPerPxY * EDGE_MARGIN_FRACTION;
    const keepLeftEdge = b.minX === 0;
    const keepTopEdge = b.minY === 0;
    const keepRightEdge = b.maxX === b.w - 1;
    const keepBottomEdge = b.maxY === b.h - 1;
    const left = keepLeftEdge ? vb.x : vb.x + b.minX * unitsPerPxX - marginX;
    const top = keepTopEdge ? vb.y : vb.y + b.minY * unitsPerPxY - marginY;
    const right = keepRightEdge ? vb.x + vb.w : vb.x + (b.maxX + 1) * unitsPerPxX + marginX;
    const bottom = keepBottomEdge ? vb.y + vb.h : vb.y + (b.maxY + 1) * unitsPerPxY + marginY;
    const nw = right - left, nh = bottom - top;

    const trimmed = 1 - (nw * nh) / (vb.w * vb.h);
    const round3 = n => Math.round(n * 1000) / 1000;
    if (check) {
      console.log(`${(id + suffix).padEnd(30)} ${vb.w}x${vb.h} -> ${round3(nw)}x${round3(nh)}  (${(trimmed * 100).toFixed(0)}% padding)`);
      continue;
    }
    if (trimmed < TIGHT_ENOUGH) continue;
    let out = svg.replace(vb.raw, `viewBox="${round3(left)} ${round3(top)} ${round3(nw)} ${round3(nh)}"`);
    out = out.replace(/<svg\b[^>]*>/, tag =>
      tag.replace(/\bwidth="[^"]*"/, `width="${round3(nw)}"`).replace(/\bheight="[^"]*"/, `height="${round3(nh)}"`));
    fs.writeFileSync(file, out);
    console.log(`${(id + suffix).padEnd(30)} ${vb.w}x${vb.h} -> ${round3(nw)}x${round3(nh)}  (trimmed ${(trimmed * 100).toFixed(0)}%)`);
  }
}
