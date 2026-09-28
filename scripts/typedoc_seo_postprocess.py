#!/usr/bin/env python3
"""Post-process typedoc's generated Node.js SDK reference HTML for SEO/AEO.

TypeDoc (unlike docfx) ships no editable theme template in this repo — its
default theme is used as-is — so this cannot follow the docfx placeholder
approach (see scripts/docfx_seo_postprocess.py). Instead it parses each
already-generated page and, for every page whose <head> it recognizes:

  1. Injects a self-referencing <link rel="canonical"> computed from the
     file's own on-disk path relative to the output directory, so it can
     never mismatch the served URL.
  2. Replaces the single boilerplate meta description ("Documentation for
     @pulumi/<pkg>", identical across every page in a package today) with
     a per-page description built from the page's own <h1> ("Class API",
     "Function isSecret", ...) and, when the page carries a page-level
     TSDoc comment, that comment's own lead text — mirroring the Sphinx
     Python SDK extension's (tools/pydocgen/source/_shared/seo_meta.py)
     "use the doc's own text when there is any, else synthesize" approach.
  3. Injects one APIReference JSON-LD block, same shape as the Python
     (Sphinx) and .NET (docfx) reference generators use, built with
     json.dumps so a doc comment containing quotes/backslashes/</script>
     can never break out of the <script> element.

Idempotent: running twice never duplicates a tag. A file that already has
a <link rel="canonical"> is left untouched; its json.dumps affordance is
irrelevant since the canonical check runs first and short-circuits.

Only member-level TSDoc comments are excluded from step 2's extraction: a
page-level comment (a class's own doc comment, a function's own doc
comment) always appears before the first <h3> member heading in TypeDoc's
default theme output, so a comment div found at or after the first <h3>
belongs to a member, not the page's own subject, and is not page-level
text worth extracting.

Usage: typedoc_seo_postprocess.py <output_dir> <base_url>

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
_H3_RE = re.compile(r"<h3\b", re.IGNORECASE)
_TAG_RE = re.compile(r"<[^>]+>")
_TITLE_PKG_RE = re.compile(r"@pulumi/([A-Za-z0-9_.-]+)")


def _strip_tags(fragment: str) -> str:
    return html.unescape(_TAG_RE.sub(" ", fragment))


def _clean(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def _truncate(text: str, limit: int = 155) -> str:
    if len(text) <= limit:
        return text
    cut = text[:limit].rsplit(" ", 1)[0]
    return cut.rstrip(",.;:") + "\u2026"


def _jsonld_safe(payload: dict) -> str:
    # Guard against a doc comment literally containing "</script>", which
    # would otherwise terminate the script element early.
    return json.dumps(payload, indent=2).replace("</", "<\\/")


def _page_level_comment(text: str) -> str | None:
    """Return the page's own lead TSDoc comment text, or None if the page
    carries no page-level comment (only member-level ones, or none)."""
    h3_match = _H3_RE.search(text)
    boundary = h3_match.start() if h3_match else len(text)
    match = _TSD_COMMENT_RE.search(text)
    if match is None or match.start() >= boundary:
        return None
    cleaned = _clean(_strip_tags(match.group(1)))
    return cleaned or None


def _package_name(title: str, rel_path: str) -> str:
    match = _TITLE_PKG_RE.search(title)
    if match:
        return match.group(1)
    # Fallback: package name is the first path segment under the output dir.
    return rel_path.split("/", 1)[0]


def process_file(path: Path, rel_path: str, canonical_url: str) -> bool:
    text = path.read_text(encoding="utf-8")
    if 'rel="canonical"' in text:
        return False  # already processed
    if "</head>" not in text.lower():
        return False  # not a normal content page (e.g. a redirect stub)

    title_match = _TITLE_RE.search(text)
    title = html.unescape(title_match.group(1)).strip() if title_match else rel_path
    pkg = _package_name(title, rel_path)

    h1_match = _H1_RE.search(text)
    headline = _clean(_strip_tags(h1_match.group(1))) if h1_match else title

    page_comment = _page_level_comment(text)
    if page_comment:
        description = f"{page_comment} \u2014 @pulumi/{pkg} Node.js SDK API reference for Pulumi."
    else:
        description = (
            f"{headline} in the @pulumi/{pkg} Node.js SDK API reference for Pulumi "
            f"infrastructure as code."
        )
    description = _truncate(description)
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

    schema: dict = {
        "@context": "https://schema.org",
        "@type": "APIReference",
        "headline": headline,
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
        f'<script type="application/ld+json">\n{_jsonld_safe(schema)}\n</script></head>'
    )
    new_text = _HEAD_CLOSE_RE.sub(lambda _m: script_block, new_text, count=1)

    path.write_text(new_text, encoding="utf-8")
    return True


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("base_url")
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
        canonical_url = f"{base_url}/{rel}"
        try:
            if process_file(html_path, rel, canonical_url):
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
