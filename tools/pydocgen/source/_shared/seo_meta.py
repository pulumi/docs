# -*- coding: utf-8 -*-
"""Sphinx extension adding a page-specific meta description, page title, and
APIReference JSON-LD block to the Pulumi Python SDK reference docs
(pulumi, pulumi_policy, pulumi_esc_sdk).

Shared by all three packages' conf.py via a relative sys.path append; keep
this file's behavior generic across all of them rather than hardcoding one
package's specifics.

Canonical URLs are NOT handled here: with ``html_baseurl`` set in conf.py,
Sphinx's own ``dirhtml`` builder already computes the correct
trailing-slash canonical via ``get_target_uri``, and sphinx_rtd_theme's
layout.html renders it from ``pageurl`` with no further help needed.
Verified against Sphinx 9.1.0 + sphinx_rtd_theme in the reduced build
harness before writing this extension.
"""

from __future__ import annotations

import json
import re
from typing import Any

from docutils import nodes
from sphinx.application import Sphinx

_WHITESPACE_RE = re.compile(r"\s+")


def _clean_text(text: str) -> str:
    return _WHITESPACE_RE.sub(" ", text).strip()


def _lead_text(doctree: nodes.document, target_len: int = 140) -> str:
    """Return the page's leading descriptive text for use as a meta
    description: the first non-empty paragraph, plus following paragraphs
    appended (space-joined) while the accumulated text is still short of
    ``target_len``. A short opening docstring (e.g. one sentence) is common
    in these SDKs, and a lone short paragraph makes a thin description,
    so this pulls in following paragraphs to reach a fuller summary
    instead of truncating information that follows. Empty string if the
    page has no paragraphs at all (e.g. auxiliary pages like genindex).
    """
    parts: list[str] = []
    total_len = 0
    for node in doctree.findall(nodes.paragraph):
        text = _clean_text(node.astext())
        if not text:
            continue
        parts.append(text)
        total_len += len(text) + 1
        if total_len >= target_len:
            break
    return " ".join(parts)


def _page_title_text(doctree: nodes.document | None, fallback: str) -> str:
    if doctree is not None:
        title_node = next(doctree.findall(nodes.title), None)
        if title_node is not None:
            text = _clean_text(title_node.astext())
            if text:
                return text
    return _clean_text(fallback)


def _truncate(text: str, limit: int = 155) -> str:
    if len(text) <= limit:
        return text
    cut = text[:limit].rsplit(" ", 1)[0]
    return cut.rstrip(",.;:") + "\u2026"


def _jsonld_safe(payload: dict[str, Any]) -> str:
    # Guard against a docstring literally containing "</script>", which
    # would otherwise terminate the script element early.
    return json.dumps(payload, indent=2).replace("</", "<\\/")


def on_html_page_context(
    app: Sphinx,
    pagename: str,
    templatename: str,
    context: dict[str, Any],
    doctree: nodes.document | None,
) -> None:
    display_name = getattr(app.config, "seo_display_name", None) or app.config.project
    pypi_name = getattr(app.config, "seo_pypi_name", None) or app.config.project
    release = app.config.release or "unknown"

    fallback_title = context.get("title") or pagename
    page_symbol = _page_title_text(doctree, fallback_title)
    seo_page_title = f"{page_symbol} \u2014 {display_name} Python API reference"
    context["seo_page_title"] = seo_page_title

    description = _lead_text(doctree) if doctree is not None else ""
    if not description:
        description = (
            f"API reference for {page_symbol} in {display_name} "
            f"({pypi_name}), version {release}, for Python."
        )
    context["seo_meta_description"] = _truncate(description)

    canonical = context.get("pageurl")
    if canonical:
        schema: dict[str, Any] = {
            "@context": "https://schema.org",
            "@type": "APIReference",
            "headline": seo_page_title,
            "description": context["seo_meta_description"],
            "url": canonical,
            "programmingLanguage": "Python",
            "executableLibraryName": pypi_name,
            "assemblyVersion": release,
            "about": {
                "@type": "SoftwareSourceCode",
                "name": pypi_name,
                "programmingLanguage": "Python",
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
        context["seo_jsonld"] = _jsonld_safe(schema)
    else:
        context["seo_jsonld"] = None


def setup(app: Sphinx) -> dict[str, Any]:
    app.add_config_value("seo_display_name", None, "html")
    app.add_config_value("seo_pypi_name", None, "html")
    app.connect("html-page-context", on_html_page_context)
    return {
        "version": "1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
