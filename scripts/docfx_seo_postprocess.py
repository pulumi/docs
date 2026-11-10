#!/usr/bin/env python3
"""Post-process docfx's generated .NET SDK reference HTML for SEO/AEO.

Runs AFTER scripts/run_docfx.sh's lowercasing pass, so every file's final,
served relative path is already known and stable. For each generated HTML
page (skipping redirect stubs, which never carry our placeholder) this:

  1. Replaces the __pulumi_seo_canonical__ placeholder (emitted by
     docfx/pulumi-template/partials/head.tmpl.partial in the canonical
     <link>, the og:url meta tag, and the JSON-LD "url" field) with the
     real absolute URL computed from the file's own on-disk path — so the
     canonical can never mismatch the served, lowercased URL.
  2. Truncates the meta description (and og:description, when present) to
     a word boundary at ~155 characters, the practical length before
     Google's SERP snippet truncates mid-sentence or mid-code. This also
     collapses any remaining whitespace runs left over from XML doc
     comments.
  3. Injects an APIReference JSON-LD block in place of the
     <!-- PULUMI_SEO_JSONLD_PLACEHOLDER --> comment, built with
     json.dumps so arbitrary quote/backslash/newline characters in a
     class's doc comment can never break out of the <script> block —
     unlike a hand-assembled JSON literal in the Mustache template would.

The JSON-LD names the SDK the pages document. That identity comes from the
docfx config's build.globalMetadata (_pulumiSdkName, _pulumiSdkLibrary,
_pulumiSdkRepository), the same place the head partial reads
_pulumiSdkName from, so the two can't disagree. A key the config omits
falls back to the IaC .NET SDK's value.

Usage: docfx_seo_postprocess.py <output_dir> <base_url>
    [--docfx-config PATH] [--sdk-version VERSION]

Example: docfx_seo_postprocess.py static-prebuilt/docs/reference/pkg/dotnet \
    https://www.pulumi.com/docs/reference/pkg/dotnet
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from pathlib import Path

# Lowercase on purpose: run_docfx.sh lowercases every relative href before
# this runs, so an uppercase placeholder in the canonical <link> would no
# longer match.
CANONICAL_PLACEHOLDER = "__pulumi_seo_canonical__"
JSONLD_PLACEHOLDER = "<!-- PULUMI_SEO_JSONLD_PLACEHOLDER -->"

# globalMetadata key -> value for the IaC .NET SDK, used when a config
# doesn't set the key.
SDK_IDENTITY_DEFAULTS = {
    "_pulumiSdkName": "Pulumi",
    "_pulumiSdkLibrary": "Pulumi",
    "_pulumiSdkRepository": "https://github.com/pulumi/pulumi-dotnet",
}

_TITLE_RE = re.compile(r"<title>(.*?)</title>", re.DOTALL)
_META_DESC_RE = re.compile(
    r'(<meta name="description" content=")(.*?)(">)', re.DOTALL
)
_OG_DESC_RE = re.compile(
    r'(<meta property="og:description" content=")(.*?)(">)', re.DOTALL
)


def truncate_description(raw_html_value: str, limit: int = 155) -> str:
    """Decode HTML entities, collapse whitespace, and truncate to a word
    boundary at ``limit`` characters (measured on the decoded, rendered
    text — the same thing a human or a search engine would count), then
    re-encode for safe embedding back into an HTML attribute."""
    decoded = html.unescape(raw_html_value)
    decoded = re.sub(r"\s+", " ", decoded).strip()
    if len(decoded) > limit:
        cut = decoded[:limit]
        last_space = cut.rfind(" ")
        if last_space > 0:
            cut = cut[:last_space]
        decoded = cut.rstrip(",.;:") + "\u2026"
    return html.escape(decoded, quote=True)


def jsonld_safe(payload: dict) -> str:
    # Guard against a doc comment literally containing "</script>", which
    # would otherwise terminate the script element early.
    return json.dumps(payload, indent=2).replace("</", "<\\/")


def load_sdk_identity(docfx_config: Path | None) -> dict[str, str]:
    identity = dict(SDK_IDENTITY_DEFAULTS)
    if docfx_config is not None:
        config = json.loads(docfx_config.read_text(encoding="utf-8"))
        metadata = config.get("build", {}).get("globalMetadata", {})
        identity.update({k: metadata[k] for k in identity if metadata.get(k)})
    return identity


def process_file(
    path: Path,
    canonical_url: str,
    sdk_version: str | None,
    sdk_identity: dict[str, str],
) -> bool:
    text = path.read_text(encoding="utf-8")
    if CANONICAL_PLACEHOLDER not in text:
        # Redirect stub or a page our head partial never touched.
        return False

    text = text.replace(CANONICAL_PLACEHOLDER, canonical_url)

    title_match = _TITLE_RE.search(text)
    headline = html.unescape(title_match.group(1)).strip() if title_match else canonical_url

    description_text = None

    def _fix_meta_desc(match: "re.Match[str]") -> str:
        nonlocal description_text
        truncated = truncate_description(match.group(2))
        description_text = html.unescape(truncated)
        return f"{match.group(1)}{truncated}{match.group(3)}"

    text = _META_DESC_RE.sub(_fix_meta_desc, text, count=1)

    def _fix_og_desc(match: "re.Match[str]") -> str:
        truncated = truncate_description(match.group(2))
        return f"{match.group(1)}{truncated}{match.group(3)}"

    text = _OG_DESC_RE.sub(_fix_og_desc, text, count=1)

    if JSONLD_PLACEHOLDER in text:
        schema: dict = {
            "@context": "https://schema.org",
            "@type": "APIReference",
            "headline": headline,
            "url": canonical_url,
            "programmingLanguage": ".NET",
            "executableLibraryName": sdk_identity["_pulumiSdkLibrary"],
            "about": {
                "@type": "SoftwareSourceCode",
                "name": sdk_identity["_pulumiSdkName"],
                "programmingLanguage": ".NET",
                "codeRepository": sdk_identity["_pulumiSdkRepository"],
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
        if sdk_version:
            schema["assemblyVersion"] = sdk_version
        if description_text:
            schema["description"] = description_text
        script_block = f'<script type="application/ld+json">\n{jsonld_safe(schema)}\n</script>'
        text = text.replace(JSONLD_PLACEHOLDER, script_block)

    path.write_text(text, encoding="utf-8")
    return True


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("base_url")
    parser.add_argument("--docfx-config", type=Path, default=None)
    parser.add_argument("--sdk-version", default=None)
    args = parser.parse_args(argv)

    base_url = args.base_url.rstrip("/")
    out_dir: Path = args.output_dir
    if not out_dir.is_dir():
        print(f"ERROR: output dir not found: {out_dir}", file=sys.stderr)
        return 1

    sdk_identity = load_sdk_identity(args.docfx_config)

    processed = 0
    for html_path in sorted(out_dir.rglob("*.html")):
        rel = html_path.relative_to(out_dir).as_posix()
        canonical_url = f"{base_url}/{rel}"
        if process_file(html_path, canonical_url, args.sdk_version, sdk_identity):
            processed += 1

    print(f"docfx_seo_postprocess: updated {processed} file(s) under {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
