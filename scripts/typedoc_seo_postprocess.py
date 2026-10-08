#!/usr/bin/env python3
"""Post-process typedoc's generated Node.js SDK reference HTML for SEO/AEO.

TypeDoc ships no editable theme template in this repo -- its default theme
is used as-is -- so this cannot hook into a template the way the .NET
(docfx) reference generator's fix does. Instead it parses each already
generated page and, for every page it recognizes:

  1. Injects a self-referencing <link rel="canonical">, computed from the
     file's own on-disk path relative to the output directory, so it can
     never mismatch the served URL. A trailing "index.html" is stripped
     first so a package's landing page canonicalizes to the same
     trailing-slash form the rest of the site links to and canonicalizes
     with (docs/reference/pkg/nodejs/pulumi/pulumi/, not .../index.html).
  2. Replaces the single boilerplate meta description ("Documentation for
     @pulumi/<pkg>", identical across every page in a package today) with
     a per-page description built from the page's own content: its actual
     TSDoc doc comment when it has a genuine page-level one, its qualified
     name for namespace/module pages (whose <h1> only carries the short
     leaf name and would otherwise collide across namespaces that share a
     leaf, e.g. two different "metrics" submodules), a dedicated
     description for the three per-package index/modules/hierarchy pages
     (which share an identical <title> and have no <h1> at all), or a
     synthesized description built from the page's own headline otherwise.
  3. Injects one APIReference JSON-LD block, matching the shape the Python
     (Sphinx) and .NET (docfx) reference generators use, built with
     json.dumps so a doc comment containing quotes/backslashes/</script>
     can never break out of the <script> element.

Idempotent by default: a file that already has a <link rel="canonical"> is
left untouched on a normal run. Pass --force to reprocess already-processed
files in place (needed after a fix to this script itself, since the normal
run_typedoc.sh pipeline never regenerates awsx/kubernetesx/terraform from
source and would otherwise never pick up a corrected description).

Page-level vs. member-level TSDoc comments: TypeDoc's default theme does
not mark every member comment with a uniform, page-independent wrapper, so
extraction bounds the search for the page's own comment at the *earliest*
of several member-introducing landmarks (the first <h3> member heading, a
<div class="tsd-type-declaration"> block, a <ul class="tsd-parameters">
member list, or a <li class="tsd-parameter"> member item) -- a comment
found at or after any of these belongs to a member (a property, a type's
field, a function parameter), not to the page's own subject, and is never
used as that page's description. A class or interface's own doc comment is
looked for first and separately, since TypeDoc always wraps it in its own
<section class="tsd-panel tsd-comment">, which is a stronger, unambiguous
signal than the boundary heuristic below it.

A page-level comment that turns out to be only a bare block-tag header
(TypeDoc renders "@internal" as a bare "Internal" heading with no body, and
"@deprecated" as a "Deprecated" heading followed by the deprecation note)
has that heading text stripped before use, since leaking the tag name
itself into a search snippet ("Internal -- @pulumi/pulumi Node.js SDK...")
describes nothing. If nothing but the heading remains, the page falls
through to the synthesized, headline-based description instead.

Usage: typedoc_seo_postprocess.py <output_dir> <base_url> [--force]

Example: typedoc_seo_postprocess.py \
    static-prebuilt/docs/reference/pkg/nodejs/pulumi \
    https://www.pulumi.com/docs/reference/pkg/nodejs/pulumi
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from pathlib import Path

_HEAD_CLOSE_RE = re.compile(r"</head>", re.IGNORECASE)
_TITLE_RE = re.compile(r"<title>(.*?)</title>", re.DOTALL)
_H1_RE = re.compile(r"<h1[^>]*>(.*?)</h1>", re.DOTALL)
_META_DESC_RE = re.compile(
    r'(<meta name="description" content=")(.*?)("\s*/?>)', re.DOTALL
)
_TSD_COMMENT_RE = re.compile(
    r'<div class="tsd-comment tsd-typography">(.*?)</div>', re.DOTALL
)
_TSD_PANEL_COMMENT_RE = re.compile(
    r'<section class="tsd-panel tsd-comment">(.*?)</section>', re.DOTALL
)
_H3_RE = re.compile(r"<h3\b", re.IGNORECASE)
_TYPE_DECL_RE = re.compile(r'<div class="tsd-type-declaration"', re.IGNORECASE)
_PARAMS_LIST_RE = re.compile(r'<ul class="tsd-parameters"', re.IGNORECASE)
_PARAM_ITEM_RE = re.compile(r'<li class="tsd-parameter"', re.IGNORECASE)
_TAG_DIV_RE = re.compile(r'<div class="tsd-tag-[A-Za-z]+">.*?</div>', re.DOTALL)
_BARE_TAG_H4_RE = re.compile(
    r"<h4[^>]*>\s*(?:Deprecated|Internal|Beta|Alpha|Remarks|Example|Since|See|"
    r"Todo|Throws|Default Value)\b.*?</h4>",
    re.DOTALL | re.IGNORECASE,
)
_SHORTCODE_RE = re.compile(r"\{\{[%<].*?[%>]\}\}", re.DOTALL)
_H1_BADGE_RE = re.compile(r'<code class="tsd-tag[^"]*">.*?</code>', re.DOTALL)
_TAG_RE = re.compile(r"<[^>]+>")
_TITLE_PKG_RE = re.compile(r"@pulumi/([A-Za-z0-9_.-]+)")

_SPECIAL_PAGE_DESCRIPTIONS = {
    "index.html": (
        "API reference index for the @pulumi/{pkg} Node.js SDK -- browse all "
        "classes, interfaces, functions, and types."
    ),
    "modules.html": (
        "All namespaces and modules exported by the @pulumi/{pkg} Node.js "
        "SDK, with links to their full API reference."
    ),
    "hierarchy.html": (
        "Class hierarchy overview for the @pulumi/{pkg} Node.js SDK API "
        "reference."
    ),
}


def _strip_shortcodes(fragment: str) -> str:
    return _SHORTCODE_RE.sub(" ", fragment)


def _strip_tags(fragment: str) -> str:
    return html.unescape(_TAG_RE.sub(" ", _strip_shortcodes(fragment)))


def _clean(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def _truncate(text: str, limit: int = 155) -> str:
    if len(text) <= limit:
        return text
    cut = text[:limit].rsplit(" ", 1)[0]
    return cut.rstrip(",.;:") + "\u2026"


def _jsonld_safe(payload: dict) -> str:
    # Guard against a doc comment literally containing "</script>", which
    # would otherwise terminate the script element early. Compact
    # separators keep the injected block to roughly one line per file
    # instead of ~25, so a future regeneration's diff stays reviewable.
    return json.dumps(payload, separators=(",", ":")).replace("</", "<\\/")


def _strip_block_tags(fragment: str) -> str:
    """Remove bare block-tag headings ("Internal", "Deprecated", ...) and
    their div-wrapped equivalents from a raw comment HTML fragment, leaving
    any real body prose (e.g. a deprecation note) intact."""
    fragment = _TAG_DIV_RE.sub(" ", fragment)
    fragment = _BARE_TAG_H4_RE.sub(" ", fragment)
    return fragment


def _page_level_comment(text: str) -> str | None:
    """Return the page's own lead TSDoc comment text, or None if the page
    carries no page-level comment (only member-level ones, or none)."""
    panel_match = _TSD_PANEL_COMMENT_RE.search(text)
    if panel_match:
        inner = _TSD_COMMENT_RE.search(panel_match.group(1))
        raw = inner.group(1) if inner else panel_match.group(1)
        cleaned = _clean(_strip_tags(_strip_block_tags(raw)))
        return cleaned or None

    boundaries = [
        m.start()
        for m in (
            _H3_RE.search(text),
            _TYPE_DECL_RE.search(text),
            _PARAMS_LIST_RE.search(text),
            _PARAM_ITEM_RE.search(text),
        )
        if m is not None
    ]
    boundary = min(boundaries) if boundaries else len(text)
    match = _TSD_COMMENT_RE.search(text)
    if match is None or match.start() >= boundary:
        return None
    cleaned = _clean(_strip_tags(_strip_block_tags(match.group(1))))
    return cleaned or None


def _package_name(title: str, rel_path: str) -> str:
    match = _TITLE_PKG_RE.search(title)
    if match:
        return match.group(1)
    # Fallback: package name is the first path segment under the output dir.
    return rel_path.split("/", 1)[0]


def _headline_for(path: Path, rel_path: str, title: str, text: str) -> tuple[str, bool]:
    """Return (headline, is_qualified) where is_qualified marks a headline
    already unique enough (a qualified name) that it should not be treated
    as generic filler when composing the synthesized description."""
    if path.parent.name == "modules":
        # A namespace/module page's <h1> only ever carries the short leaf
        # name ("Namespace metrics"), which collides across every namespace
        # that shares that leaf (awsx alone has a dozen "*.metrics"
        # submodules). The filename carries the real, qualified name.
        return path.stem, True
    h1_match = _H1_RE.search(text)
    if h1_match:
        headline = _clean(_strip_tags(_H1_BADGE_RE.sub(" ", h1_match.group(1))))
        if headline:
            return headline, False
    return title, False


def process_file(path: Path, rel_path: str, canonical_url: str, force: bool = False) -> bool:
    text = path.read_text(encoding="utf-8")
    if not force and 'rel="canonical"' in text:
        return False  # already processed
    if "</head>" not in text.lower():
        return False  # not a normal content page (e.g. a redirect stub)

    title_match = _TITLE_RE.search(text)
    title = html.unescape(title_match.group(1)).strip() if title_match else rel_path
    pkg = _package_name(title, rel_path)

    special = _SPECIAL_PAGE_DESCRIPTIONS.get(path.name) if path.parent.name != "modules" else None
    # The three special pages live directly under the package root
    # (pkg/index.html, not pkg/modules/index.html-style nesting), so guard
    # on rel_path depth too: "<pkg>/index.html" has exactly two segments.
    if special is not None and rel_path.count("/") != 1:
        special = None

    headline, headline_is_qualified = _headline_for(path, rel_path, title, text)

    if special is not None:
        description = special.format(pkg=pkg)
    else:
        page_comment = _page_level_comment(text)
        page_comment = _strip_shortcodes(page_comment) if page_comment else page_comment
        if page_comment:
            # Lead with the package context so it survives truncation on a
            # long comment instead of being the trailing clause that gets
            # cut. The branded suffix below is appended only when it fits.
            base = f"@pulumi/{pkg}: {page_comment}"
            with_suffix = f"{base} \u2014 Node.js SDK API reference for Pulumi."
            description = with_suffix if len(with_suffix) <= 155 else base
        elif headline_is_qualified:
            description = (
                f"Namespace {headline} in the @pulumi/{pkg} Node.js SDK API "
                f"reference for Pulumi infrastructure as code."
            )
        else:
            description = (
                f"{headline} in the @pulumi/{pkg} Node.js SDK API reference for Pulumi "
                f"infrastructure as code."
            )
    description = _truncate(_clean(description))
    description_attr = html.escape(description, quote=True)

    def _fix_meta_desc(match: "re.Match[str]") -> str:
        return f"{match.group(1)}{description_attr}{match.group(3)}"

    new_text, desc_subs = _META_DESC_RE.subn(_fix_meta_desc, text, count=1)
    if desc_subs == 0:
        # No existing description meta tag on this page; add one. Use a
        # replacement function, not a replacement string: description_attr
        # (and, below, the JSON-LD block) may contain backslashes that
        # re.sub would otherwise try to interpret as backreferences.
        added_desc_tag = f'<meta name="description" content="{description_attr}"/></head>'
        new_text = _HEAD_CLOSE_RE.sub(lambda _m: added_desc_tag, text, count=1)

    plain_headline = headline if not headline_is_qualified else f"Namespace {headline}"

    schema: dict = {
        "@context": "https://schema.org",
        "@type": "APIReference",
        "headline": plain_headline,
        "description": description,
        "url": canonical_url,
        "programmingLanguage": "TypeScript",
        "executableLibraryName": f"@pulumi/{pkg}",
        "about": {
            "@type": "SoftwareSourceCode",
            "name": f"@pulumi/{pkg}",
            "programmingLanguage": "TypeScript",
        },
        "isPartOf": {
            "@type": "WebSite",
            "name": "Pulumi Docs",
            "url": "https://www.pulumi.com/docs/",
        },
        "publisher": {
            "@type": "Organization",
            "name": "Pulumi",
            "url": "https://www.pulumi.com/",
        },
    }
    script_block = (
        f'<link rel="canonical" href="{canonical_url}"/>'
        f'<script type="application/ld+json">{_jsonld_safe(schema)}</script></head>'
    )
    if force:
        # A prior run may have left its own canonical/JSON-LD in place;
        # strip them before re-injecting so --force never duplicates tags.
        new_text = re.sub(r'<link rel="canonical"[^>]*/>', "", new_text)
        new_text = re.sub(
            r'<script type="application/ld\+json">.*?</script>', "", new_text, flags=re.DOTALL
        )
    new_text = _HEAD_CLOSE_RE.sub(lambda _m: script_block, new_text, count=1)

    path.write_text(new_text, encoding="utf-8")
    return True


def _canonical_rel(rel: str) -> str:
    # Package landing pages must canonicalize to the trailing-slash form
    # the rest of the site links to and canonicalizes with; CloudFront does
    # not redirect the on-disk "index.html" path to it, so leaving it in
    # would have every package's landing page declare a second, different
    # canonical URL than the one actually crawled and linked to.
    if rel == "index.html" or rel.endswith("/index.html"):
        return rel[: -len("index.html")]
    return rel


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("base_url")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Reprocess files that already carry a canonical link/JSON-LD "
        "(needed after a fix to this script, since the pipeline never "
        "regenerates awsx/kubernetesx/terraform from source).",
    )
    args = parser.parse_args(argv)

    base_url = args.base_url.rstrip("/")
    out_dir: Path = args.output_dir
    if not out_dir.is_dir():
        print(f"ERROR: output dir not found: {out_dir}", file=sys.stderr)
        return 1

    processed = 0
    skipped = 0
    for html_path in sorted(out_dir.rglob("*.html")):
        if "assets" in html_path.relative_to(out_dir).parts:
            continue
        rel = html_path.relative_to(out_dir).as_posix()
        canonical_url = f"{base_url}/{_canonical_rel(rel)}"
        try:
            if process_file(html_path, rel, canonical_url, force=args.force):
                processed += 1
            else:
                skipped += 1
        except Exception as exc:  # fail loudly, but keep the file path in view
            print(f"ERROR processing {html_path}: {exc}", file=sys.stderr)
            raise

    print(
        f"typedoc_seo_postprocess: updated {processed} file(s), "
        f"skipped {skipped} (already processed or not a content page) under {out_dir}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
