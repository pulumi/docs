#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';

const DIR = 'assets/fingerprinted/logos/customers';
const WHITE = '#fff';
const LEAVE_ALONE = /^(none|transparent|inherit)$/i;
const MASK_PLACEHOLDER = /<!--derive-on-dark:mask:(\d+)-->/g;

const repaintable = (value) => {
  const v = value.trim();
  return !LEAVE_ALONE.test(v) && !v.startsWith('url(');
};

// A luminance mask uses color as data, so repainting inside one changes which
// parts of the logo exist rather than what color they are.
function liftMasks(svg, into) {
  return svg.replace(/<mask\b[\s\S]*?<\/mask>/g, (mask) => {
    into.push(mask);
    return `<!--derive-on-dark:mask:${into.length - 1}-->`;
  });
}

function restoreMasks(svg, lifted) {
  return svg.replace(MASK_PLACEHOLDER, (_, i) => lifted[Number(i)]);
}

const ids = process.argv.slice(2);
if (ids.length === 0) {
  console.error('usage: node scripts/customers/derive-on-dark.mjs <id> [<id> ...]');
  process.exit(1);
}

let failed = false;
for (const id of ids) {
  const src = path.join(DIR, `${id}.svg`);
  if (!fs.existsSync(src)) {
    console.error(`${id}: ${src} does not exist`);
    failed = true;
    continue;
  }
  let svg = fs.readFileSync(src, 'utf8');
  const unrepaintable = [];

  const liftedMasks = [];
  svg = liftMasks(svg, liftedMasks);

  svg = svg.replace(/\b(fill|stroke)\s*=\s*"([^"]*)"/g, (m, prop, v) =>
    repaintable(v) ? `${prop}="${WHITE}"` : m);
  svg = svg.replace(/\b(fill|stroke|stop-color)\s*:\s*([^;"'}]+)/g, (m, prop, v) =>
    repaintable(v) ? `${prop}:${WHITE}` : m);
  svg = svg.replace(/<stop\b[^>]*\/?>/g, (tag) =>
    /\bstop-color\s*=/.test(tag)
      ? tag.replace(/\bstop-color\s*=\s*"[^"]*"/, `stop-color="${WHITE}"`)
      : tag.replace(/<stop\b/, `<stop stop-color="${WHITE}"`));
  if (/<pattern\b/.test(svg) && /<image\b/.test(svg)) unrepaintable.push('pattern with an <image>');

  const root = /<svg\b[^>]*>/.exec(svg)[0];
  if (!/\bfill\s*=/.test(root)) svg = svg.replace('<svg', `<svg fill="${WHITE}"`);

  svg = restoreMasks(svg, liftedMasks);

  const out = path.join(DIR, `${id}-on-dark.svg`);
  fs.writeFileSync(out, svg);
  const note = unrepaintable.length ? `  (could not repaint: ${unrepaintable.join(', ')} — check on a dark background)` : '';
  console.log(`${id} -> ${out}${note}`);
}
process.exit(failed ? 1 : 0);
