#!/usr/bin/env python3
"""Post-process gradle javadoc's generated Java SDK reference HTML for SEO/AEO.

The stock Javadoc doclet (JDK 17) ships no editable theme template in this
repo -- scripts/gen_javadoc.sh runs `gradle javadoc` against the external
pulumi-java checkout as-is and only overwrites search.js afterward -- so,
like the Node.js TypeDoc reference generator's fix, this cannot hook into a
template and instead parses each already generated page and, for every page
it recognizes:

  1. Injects a self-referencing <link rel="canonical">, computed from the
     file's own on-disk path relative to the output directory. A trailing
     "index.html" is stripped first so the package-index landing page
     canonicalizes to the same trailing-slash form the rest of the site
     links to (docs/reference/pkg/java/, not .../index.html) -- today both
     serve byte-identical content with no canonical at all, a live
     duplicate-URL pair.
  2. Replaces Javadoc's own generic, colliding meta descriptions
     ("package index", "class index", "declaration: package: com.pulumi,
     interface: Context", identical in shape across every class/interface
     in a package) with a per-page description built from the page's own
     content: the class/interface/enum's own lead Javadoc comment (found in
     its <section class="class-description"> block) for a class page, a
     dedicated hand-written description for the handful of shared pages
     that carry no real prose at all (root index, allclasses-index,
     allpackages-index, overview-tree, deprecated-list, constant-values,
     serialized-form, help-doc, index-all), and a synthesized description
     for package-summary/package-tree pages, since this SDK's packages ship
     no package-info.java doc comment for the doclet to render.
  3. Injects one APIReference JSON-LD block, matching the shape the
     Node.js (TypeDoc) and .NET (DocFX) reference generators use, built
     with json.dumps so a doc comment containing quotes/backslashes/
     </script> can never break out of the <script> element.
  4. Strips the version-pinned title suffix Javadoc always emits
     ("Context (pulumi 1.37.3 API)") and replaces it with a stable,
     brand-consistent form that does not need re-editing on every SDK
     release ("Context | Pulumi Java SDK Reference").

Uses the file's fully-qualified name (derived from its on-disk path, e.g.
com.pulumi.core.Output from com/pulumi/core/Output.html, or
com.pulumi.core.Output.ListBuilder for a nested class) in descriptions and
the JSON-LD headline, not just the bare leaf name Javadoc's own <h1>/<title>
carry, since two different packages can and do share a leaf class name.

Idempotent by default: a file that already has a <link rel="canonical"> is
left untouched on a normal run. Pass --force to reprocess already-processed
files in place. The client-side redirect stub overview-summary.html (it
303s to index.html via `window.location.replace`, and already carries its
own correct relative canonical) is always left alone, force or not, since
reprocessing it would replace that correct relative canonical with an
incorrect self-referencing absolute one.

Usage: javadoc_seo_postprocess.py <output_dir> <base_url> [--force]

Example: javadoc_seo_postprocess.py \
    static-prebuilt/docs/reference/pkg/java \
    https://www.pulumi.com/docs/reference/pkg/java
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
_META_DESC_RE = re.compile(
    r'(<meta name="description" content=")(.*?)(">)', re.DOTALL
)
_VERSION_SUFFIX_RE = re.compile(
    r"\s*\(pulumi\s+[^)]*\s+API\)\s*\Z", re.IGNORECASE
)
_TITLE_BRAND_SUFFIX = " | Pulumi Java SDK Reference"
_TITLE_BRAND_SUFFIX_RE = re.compile(
    re.escape(_TITLE_BRAND_SUFFIX) + r"\Z"
)
_CLASS_DESC_SECTION_RE = re.compile(
    r'<section class="class-description"[^>]*>(.*?)</section>', re.DOTALL
)
_BLOCK_DIV_RE = re.compile(r'<div class="block">(.*?)</div>', re.DOTALL)
_TAG_RE = re.compile(r"<[^>]+>")
_REDIRECT_MARKER = "index-redirect-page"

# Javadoc's own generic, colliding descriptions -- a derived or synthesized
# description must never contain any of these, since letting one through
# would silently reintroduce the exact duplicate-content problem this
# script exists to fix.
_BOILERPLATE_SUBSTRINGS = (
    "declaration:",
    "package index",
    "class index",
    "class tree",
    "tree: package:",
    "deprecated elements",
    "serialized forms",
    "summary of constants",
    "index redirect",
)

# Root-level pages (no real prose of their own) get a dedicated,
# hand-written description instead of anything derived from the page.
_SPECIAL_PAGE_DESCRIPTIONS = {
    "index.html": (
        "API reference index for the Pulumi Java SDK (com.pulumi) -- browse "
        "every package, class, interface, and enum."
    ),
    "allclasses-index.html": (
        "Full alphabetical index of every class, interface, enum, and "
        "annotation type in the Pulumi Java SDK API reference."
    ),
    "allpackages-index.html": (
        "Index of every package in the Pulumi Java SDK (com.pulumi) API "
        "reference."
    ),
    "overview-tree.html": (
        "Class hierarchy overview for the Pulumi Java SDK API reference, "
        "showing inheritance across every package."
    ),
    "deprecated-list.html": (
        "Deprecated classes, methods, and fields across the Pulumi Java "
        "SDK API reference, with links to their replacements."
    ),
    "constant-values.html": (
        "Constant field values declared across the Pulumi Java SDK API "
        "reference."
    ),
    "serialized-form.html": (
        "Serialized form of every Serializable class in the Pulumi Java "
        "SDK API reference."
    ),
    "help-doc.html": (
        "How to read and navigate the Pulumi Java SDK API reference, "
        "generated by Javadoc."
    ),
    "index-all.html": (
        "Alphabetical index of every package, class, method, and field in "
        "the Pulumi Java SDK API reference."
    ),
}

_BRANDED_SUFFIX = " Java API reference for the Pulumi Java SDK."


def _strip_tags(fragment: str) -> str:
    return html.unescape(_TAG_RE.sub(" ", fragment))


def _clean(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def _truncate(text: str, limit: int = 155) -> str:
    if len(text) <= limit:
        return text
    cut = text[:limit].rsplit(" ", 1)[0]
    return cut.rstrip(",.;:") + "\u2026"


def _contains_boilerplate(text: str) -> bool:
    lowered = text.lower()
    return any(marker in lowered for marker in _BOILERPLATE_SUBSTRINGS)


def _jsonld_safe(payload: dict) -> str:
    # Guard against a doc comment literally containing "</script>", which
    # would otherwise terminate the script element early. Compact
    # separators keep the injected block to roughly one line per file
    # instead of many, so a future regeneration's diff stays reviewable.
    return json.dumps(payload, separators=(",", ":")).replace("</", "<\\/")


def _class_lead_comment(text: str) -> str | None:
    """Return the class/interface/enum/annotation's own lead Javadoc
    comment text, stripped of tags, or None if the page carries none
    (a page with only inherited members and no doc comment of its own)."""
    section_match = _CLASS_DESC_SECTION_RE.search(text)
    if not section_match:
        return None
    block_match = _BLOCK_DIV_RE.search(section_match.group(1))
    if not block_match:
        return None
    cleaned = _clean(_strip_tags(block_match.group(1)))
    return cleaned or None


def _fqcn_from_rel(rel_path: str) -> str:
    """Fully-qualified name from an on-disk path under com/, e.g.
    com.pulumi.core.Output from com/pulumi/core/Output.html, or
    com.pulumi.core.Output.ListBuilder for a nested class file."""
    p = Path(rel_path)
    return ".".join(p.parts[:-1] + (p.stem,))


def _package_from_rel(rel_path: str) -> str:
    """Dotted package name from a package-summary.html/package-tree.html
    path, e.g. com.pulumi.core from com/pulumi/core/package-summary.html."""
    return ".".join(Path(rel_path).parts[:-1])


def _build_description(path: Path, rel_path: str) -> tuple[str, str]:
    """Return (description, headline) for a page. Never lets a
    Javadoc-boilerplate substring through -- a derivation that would
    contain one falls back to the synthesized, name-based form instead."""
    depth_parts = rel_path.split("/")
    filename = depth_parts[-1]

    if len(depth_parts) == 1:
        special = _SPECIAL_PAGE_DESCRIPTIONS.get(filename)
        if special is not None:
            title_match = _TITLE_RE.search(path.read_text(encoding="utf-8"))
            headline = (
                _VERSION_SUFFIX_RE.sub(
                    "", html.unescape(title_match.group(1)).strip()
                )
                if title_match
                else filename
            )
            return special, headline
        # Unknown root-level page (e.g. a future doclet addition): fall
        # through to the generic synthesized form below rather than ever
        # leaving Javadoc's own boilerplate meta description in place.
        return (
            "API reference for the Pulumi Java SDK (com.pulumi).",
            filename,
        )

    if filename in ("package-summary.html", "package-tree.html"):
        package = _package_from_rel(rel_path)
        if filename == "package-tree.html":
            description = (
                f"Class hierarchy for the {package} package in the Pulumi "
                f"Java SDK API reference."
            )
        else:
            description = (
                f"API reference for the {package} package in the Pulumi "
                f"Java SDK, part of Pulumi's infrastructure as code "
                f"platform."
            )
        return _truncate(description), package

    # A class/interface/enum/annotation-type page.
    fqcn = _fqcn_from_rel(rel_path)
    text = path.read_text(encoding="utf-8")
    lead_comment = _class_lead_comment(text)
    if lead_comment and not _contains_boilerplate(lead_comment):
        base = f"{fqcn}: {lead_comment}"
        with_suffix = f"{base}{_BRANDED_SUFFIX}"
        description = with_suffix if len(with_suffix) <= 155 else base
    else:
        description = f"API reference for {fqcn} in the Pulumi Java SDK."
    return _truncate(_clean(description)), fqcn


def _canonical_rel(rel: str) -> str:
    # The package-index landing page must canonicalize to the trailing-
    # slash form the rest of the site links to and canonicalizes with;
    # leaving "index.html" in would have it declare a second, different
    # canonical URL than the one actually crawled and linked to.
    if rel == "index.html" or rel.endswith("/index.html"):
        return rel[: -len("index.html")]
    return rel


def process_file(path: Path, rel_path: str, canonical_url: str, force: bool = False) -> bool:
    text = path.read_text(encoding="utf-8")
    if _REDIRECT_MARKER in text:
        return False  # client-side redirect stub; already correct, always skip
    if not force and 'rel="canonical"' in text:
        return False  # already processed
    if "</head>" not in text.lower():
        return False  # not a normal content page

    if force:
        # A prior run may have left its own canonical/JSON-LD in place;
        # strip them before re-injecting so --force never duplicates tags.
        text = re.sub(r'<link rel="canonical"[^>]*/?>', "", text)
        text = re.sub(
            r'<script type="application/ld\+json">.*?</script>', "", text, flags=re.DOTALL
        )

    title_match = _TITLE_RE.search(text)
    raw_title = html.unescape(title_match.group(1)).strip() if title_match else rel_path
    # Idempotent regardless of whether this is a fresh or a --force rerun:
    # strip our own previously appended brand suffix first (a no-op if it
    # is not present), then Javadoc's version-pinned suffix, then
    # re-append the brand suffix exactly once.
    stripped_title = _TITLE_BRAND_SUFFIX_RE.sub("", raw_title)
    stripped_title = _VERSION_SUFFIX_RE.sub("", stripped_title).strip()
    new_title = f"{stripped_title}{_TITLE_BRAND_SUFFIX}"
    if title_match:
        text = (
            text[: title_match.start(1)]
            + html.escape(new_title)
            + text[title_match.end(1) :]
        )

    description, headline = _build_description(path, rel_path)
    description_attr = html.escape(description, quote=True)

    def _fix_meta_desc(match: "re.Match[str]") -> str:
        return f"{match.group(1)}{description_attr}{match.group(3)}"

    new_text, desc_subs = _META_DESC_RE.subn(_fix_meta_desc, text, count=1)
    if desc_subs == 0:
        added_desc_tag = f'<meta name="description" content="{description_attr}"/></head>'
        new_text = _HEAD_CLOSE_RE.sub(lambda _m: added_desc_tag, new_text, count=1)

    schema: dict = {
        "@context": "https://schema.org",
        "@type": "APIReference",
        "headline": headline,
        "description": description,
        "url": canonical_url,
        "programmingLanguage": "Java",
        "executableLibraryName": "com.pulumi",
        "about": {
            "@type": "SoftwareSourceCode",
            "name": "com.pulumi",
            "programmingLanguage": "Java",
            "codeRepository": "https://github.com/pulumi/pulumi-java",
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
    new_text = _HEAD_CLOSE_RE.sub(lambda _m: script_block, new_text, count=1)

    path.write_text(new_text, encoding="utf-8")
    return True


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("base_url")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Reprocess files that already carry a canonical link/JSON-LD "
        "(needed after a fix to this script itself).",
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
        f"javadoc_seo_postprocess: updated {processed} file(s), "
        f"skipped {skipped} (already processed or not a content page) under {out_dir}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
