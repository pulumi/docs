#!/usr/bin/env python3
#
# trim-cli-nav.py — strip the borrowed live-site chrome from snapshotted CLI command pages
# so the archive is a self-contained, JS-free static artifact. Three surgical passes, each a
# no-op if its hook is absent (so the rest of the page stays byte-for-byte unchanged):
#
#   1. LEFT NAV — replace the full-site docs mega-menu with a compact, self-contained command
#      list, prepended with synthetic "Docs Home" + "Latest Version" items (both pointing at
#      the LIVE site). Run AFTER intra-links are rewritten to the versioned prefix, so the
#      command links inside the nav already start with --version-root.
#
#   2. RIGHT-RAIL ACTIONS/FEEDBACK — drop the live-only widgets that are meaningless (or dead)
#      on a frozen snapshot: the "Edit this Page" / "Request a Change" links (they point into
#      the LIVE GitHub source), the "Copy Page" <pulumi-llm-menu> and <pulumi-top-button> web
#      components (their defining JS is the site bundle, which the snapshot strips, so they
#      never upgrade), and the "Was this page helpful?" feedback widget (#docsFeedbackContainer,
#      which the same stripped JS never reveals). The "On this page" ToC is KEPT.
#
#   3. TABLE OF CONTENTS — the ToC <ul> is populated at runtime by theme/src/ts/misc.ts, which
#      the snapshot strips, so it ships empty and renders blank. Rebuild it statically here,
#      mirroring misc.ts exactly: every <h2>/<h3> with an id and text becomes
#      <li class="h2|h3"><a href="#id">…</a></li> (honoring data-link-title), injected into
#      the desktop AND mobile lists. CSS shows the populated list with no JS.
#
# Stdlib only (no CI dependency): regex splices + a small balanced-tag remover. No HTML parser.
#
import re, argparse, pathlib, html

ap = argparse.ArgumentParser()
ap.add_argument('--src', required=True)
ap.add_argument('--version-root', required=True)  # e.g. /docs/versioned/pulumi-cli/v3.247.0/
ap.add_argument('--live-root', required=True)      # e.g. /docs/iac/cli/commands/
args = ap.parse_args()

VR = args.version_root if args.version_root.endswith('/') else args.version_root + '/'
NAV_RE = re.compile(r'<nav class="text-sm mt-5 mr-2"[^>]*>.*?</nav>', re.S)
HREF_RE = re.compile(r'href="(' + re.escape(VR) + r'[^"#?]*)"')

# Right-rail chrome to strip (pass 2). The feedback <ul> has no nested <ul>, so a non-greedy
# match is safe; #docsFeedbackContainer nests <div>s, so it needs the balanced remover below.
FEEDBACK_UL_RE = re.compile(r'<ul[^>]*\btable-of-contents-feedback\b[^>]*>.*?</ul>', re.S)
TOPBTN_RE = re.compile(r'<pulumi-top-button>\s*</pulumi-top-button>', re.I)

# ToC (pass 3): the empty desktop+mobile lists, and the content headings that feed them.
TOC_LIST_RE = re.compile(r'(<ul[^>]*\btable-of-contents-list\b[^>]*>)\s*(</ul>)')
HEADING_RE = re.compile(r'<(h[23])\b([^>]*)>(.*?)</\1>', re.S)


def attr(attrs, name):
    m = re.search(r'\b' + re.escape(name) + r'="([^"]*)"', attrs)
    return m.group(1) if m else None


def strip_balanced(txt, open_token, tag):
    """Remove a <tag …open_token…>…</tag> block honoring nesting (regex can't balance)."""
    start = txt.find(open_token)
    if start < 0:
        return txt
    tok = re.compile(r'<\s*(/?)' + re.escape(tag) + r'\b', re.I)
    depth = 0
    pos = start
    while True:
        m = tok.search(txt, pos)
        if not m:
            return txt  # malformed; leave untouched
        if m.group(1):
            depth -= 1
            if depth == 0:
                gt = txt.find('>', m.end())
                return txt if gt < 0 else txt[:start] + txt[gt + 1:]
        else:
            depth += 1
        pos = m.end()


def build_toc(txt):
    """Mirror misc.ts generateOnThisPage(): h2/h3 with id+text → ToC <li>s."""
    items = []
    for m in HEADING_RE.finditer(txt):
        tag, attrs, inner = m.group(1), m.group(2), m.group(3)
        hid = attr(attrs, 'id')
        if not hid:
            continue
        if 'no-anchor' in (attr(attrs, 'class') or ''):  # the "On this page" heading itself
            continue
        link_title = attr(attrs, 'data-link-title')
        text = link_title if link_title else re.sub(r'<[^>]+>', '', inner)
        text = html.unescape(text).strip()
        if not text:
            continue
        items.append(f'<li class="{tag}"><a href="#{html.escape(hid, quote=True)}">'
                     f'{html.escape(text)}</a></li>')
    return ''.join(items)


def trim_nav(txt):
    m = NAV_RE.search(txt)
    if not m:
        return txt, 0
    seen, items = set(), []
    for h in HREF_RE.findall(m.group(0)):
        if '/_vassets/' in h or h in seen:
            continue
        seen.add(h)
        items.append(h)
    if not items:
        return txt, 0
    nav = ['<nav class="text-sm mt-5 mr-2 vdocs-cli-nav-wrap">',
           '<a class="vdocs-nav-home" href="/docs/">Docs Home</a>',
           f'<a class="vdocs-nav-latest" href="{args.live_root}">Latest Version</a>',
           '<ul class="vdocs-cli-nav">']
    nav += [f'<li><a href="{h}">{nav_label(h)}</a></li>' for h in items]
    nav += ['</ul></nav>']
    return txt[:m.start()] + ''.join(nav) + txt[m.end():], len(items)


def nav_label(href):
    seg = href[len(VR):].rstrip('/').split('/')[-1]
    # The bare version-root self-link is the commands index, not a command — without this it
    # would render as a second "pulumi" entry alongside the `pulumi` root command.
    if seg == '':
        return 'Overview'
    return re.sub(r'^pulumi[_-]?', '', seg).replace('_', ' ') or 'pulumi'


trimmed = stripped = toced = last = 0
for f in pathlib.Path(args.src).rglob('*.html'):
    orig = txt = f.read_text(encoding='utf-8', errors='ignore')

    # Pass 2: strip dead right-rail chrome first, so removed blocks can't feed the ToC scan.
    new = FEEDBACK_UL_RE.sub('', txt)
    new = TOPBTN_RE.sub('', new)
    new = strip_balanced(new, '<div id="docsFeedbackContainer"', 'div')
    if new != txt:
        txt = new
        stripped += 1

    # Pass 3: rebuild the ToC from the page's headings, into the empty desktop+mobile lists.
    # A page with no id'd headings (e.g. the commands index) gets no list; mirror misc.ts's
    # found==false branch and hide the "On this page" box rather than leave it empty.
    toc = build_toc(txt)
    if toc:
        txt, n = TOC_LIST_RE.subn(lambda m: m.group(1) + toc + m.group(2), txt)
        if n:
            toced += 1
    else:
        txt = re.sub(r'(<div class="table-of-contents")>', r'\1 style="display:none">', txt)

    # Pass 1: trim the borrowed left nav.
    txt, items = trim_nav(txt)
    if items:
        trimmed += 1
        last = items

    if txt != orig:
        f.write_text(txt, encoding='utf-8')

print(f"trim-cli-nav: nav trimmed {trimmed}, chrome stripped {stripped}, "
      f"toc built {toced} pages; {last} commands in nav")
