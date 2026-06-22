#!/usr/bin/env python3
#
# trim-cli-nav.py — replace the borrowed full-site left-nav on snapshotted CLI command
# pages with a compact, self-contained command list, prepended with synthetic
# "Docs Home" and "Latest Version" items (both pointing at the LIVE site).
#
# Run by snapshot-cli-docs.sh AFTER intra-links are rewritten to the versioned prefix, so
# the command links inside the nav already start with --version-root. Stdlib only (no CI
# dependency): a surgical regex splice of just the <nav> block — the rest of each page is
# left byte-for-byte unchanged. If the nav class ever changes, this no-ops (full nav kept).
#
import re, argparse, pathlib

ap = argparse.ArgumentParser()
ap.add_argument('--src', required=True)
ap.add_argument('--version-root', required=True)  # e.g. /docs/versioned/pulumi-cli/v3.247.0/
ap.add_argument('--live-root', required=True)      # e.g. /docs/iac/cli/commands/
args = ap.parse_args()

VR = args.version_root if args.version_root.endswith('/') else args.version_root + '/'
NAV_RE = re.compile(r'<nav class="text-sm mt-5 mr-2"[^>]*>.*?</nav>', re.S)
HREF_RE = re.compile(r'href="(' + re.escape(VR) + r'[^"#?]*)"')

def label(href):
    seg = href[len(VR):].rstrip('/').split('/')[-1]
    seg = re.sub(r'^pulumi[_-]?', '', seg)
    return seg.replace('_', ' ') or 'pulumi'

def build(items):
    out = ['<nav class="text-sm mt-5 mr-2 vdocs-cli-nav-wrap">',
           '<a class="vdocs-nav-home" href="/docs/">Docs Home</a>',
           f'<a class="vdocs-nav-latest" href="{args.live_root}">Latest Version</a>',
           '<ul class="vdocs-cli-nav">']
    out += [f'<li><a href="{h}">{label(h)}</a></li>' for h in items]
    out += ['</ul></nav>']
    return ''.join(out)

trimmed = 0
last = 0
for f in pathlib.Path(args.src).rglob('*.html'):
    txt = f.read_text(encoding='utf-8', errors='ignore')
    m = NAV_RE.search(txt)
    if not m:
        continue
    seen = set()
    items = []
    for h in HREF_RE.findall(m.group(0)):
        if '/_vassets/' in h or h in seen:
            continue
        seen.add(h)
        items.append(h)
    if not items:
        continue
    txt = txt[:m.start()] + build(items) + txt[m.end():]
    f.write_text(txt, encoding='utf-8')
    trimmed += 1
    last = len(items)

print(f"trim-cli-nav: trimmed {trimmed} pages, {last} commands in nav")
