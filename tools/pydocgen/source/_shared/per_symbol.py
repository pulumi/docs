"""Per-symbol page generation for the Pulumi Python SDK reference docs.

Instead of one monolithic automodule page per package, this extension writes
one small .rst stub per public class and function into <srcdir>/api/ at
builder-init time (the directory is gitignored; nothing generated is committed
as source). Each stub uses plain autodoc directives, so cross-reference ids
(for example ``pulumi.Output.apply``) are identical to the legacy single-page
ids and only the page they live on changes.

It also, at build-finished:
  * writes sitemap.xml listing the content pages (no genindex/search),
  * writes _static/legacy-anchors.json mapping each legacy anchor id to its new
    page, consumed by the small redirect script in layout.html so old
    ``/pulumi/#pulumi.Output.apply`` links keep landing on the right symbol.

conf.py options:
  per_symbol_modules   list of dotted module names to split.
  per_symbol_honor_all bool; when True a module's __all__ limits the symbols.
  per_symbol_sitemap_min_words int; generated pages with fewer rendered words are left out of sitemap.xml (default 25).
"""
from __future__ import annotations

import importlib
import inspect
import json
import re
import shutil
from pathlib import Path
from typing import Any
from xml.sax.saxutils import escape

from sphinx.application import Sphinx


def _public_symbols(modname: str, honor_all: bool) -> list[tuple[str, str]]:
    """Return sorted (kind, name) pairs for public classes and functions."""
    mod = importlib.import_module(modname)
    root = modname.split(".")[0]
    names = list(getattr(mod, "__all__", [])) if honor_all and hasattr(mod, "__all__") else list(vars(mod))
    out = []
    for name in sorted(set(names)):
        if name.startswith("_"):
            continue
        obj = getattr(mod, name, None)
        if not (inspect.isclass(obj) or inspect.isfunction(obj)):
            continue
        if not str(getattr(obj, "__module__", "")).startswith(root):
            continue
        if inspect.isclass(obj):
            kind = "exception" if issubclass(obj, BaseException) else "class"
        else:
            kind = "function"
        out.append((kind, name))
    return out


def _first_line(modname: str, name: str) -> str:
    obj = getattr(importlib.import_module(modname), name)
    if inspect.isclass(obj):
        # Own docstring only; an inherited one (for example a mixin's __repr__
        # text) would describe a different class.
        doc = inspect.cleandoc(obj.__dict__.get("__doc__") or "")
    else:
        doc = inspect.getdoc(obj) or ""
    line = doc.strip().split("\n\n")[0].replace("\n", " ").strip()
    line = re.sub(r":\w+:`~?([^`]*)`", r"\1", line).replace("`", "")
    if len(line) > 140:
        line = line[:137].rsplit(" ", 1)[0] + "..."
    return re.sub(r"([\\*_|])", r"\\\1", line)


def _generate(app: Sphinx) -> None:
    modules = app.config.per_symbol_modules
    if not modules:
        return
    api = Path(app.srcdir) / "api"
    if api.exists():
        shutil.rmtree(api)
    api.mkdir()
    overview = []
    for modname in modules:
        symbols = _public_symbols(modname, app.config.per_symbol_honor_all)
        overview.append(f"{modname}\n{'=' * len(modname)}\n")
        # Restores the legacy #module-<modname> anchors and py-modindex/.
        overview.append(f".. py:module:: {modname}\n")
        overview.append(f"Classes and functions in ``{modname}``.\n")
        overview.append(".. list-table::\n   :class: per-symbol-index\n   :widths: 35 65\n")
        entries = []
        for kind, name in symbols:
            full = f"{modname}.{name}"
            directive = {"class": "autoclass", "exception": "autoexception"}.get(kind, "autofunction")
            body = f".. {directive}:: {full}\n"
            if kind != "function":
                body += "   :members:\n"
            title = f"{full}"
            (api / f"{full}.rst").write_text(f"{title}\n{'=' * len(title)}\n\n{body}", encoding="utf-8")
            entries.append(full)
            overview.append(f"   * - :doc:`{full} <api/{full}>`\n     - {_first_line(modname, name)}\n")
        overview.append(f"\n.. toctree::\n   :hidden:\n   :caption: {modname}\n\n" + "".join(f"   api/{e}\n" for e in entries))
    (Path(app.srcdir) / "api" / "overview.inc").write_text("\n".join(overview), encoding="utf-8")


def _is_thin(app: Sphinx, docname: str, min_words: int) -> bool:
    """True for generated per-symbol pages with too little rendered text to be worth indexing.

    The pages are still built and linked; they are only left out of sitemap.xml.
    """
    if not docname.startswith("api/") or min_words <= 0:
        return False
    return len(app.env.get_doctree(docname).astext().split()) < min_words


def _finish(app: Sphinx, exception: Exception | None) -> None:
    if exception or app.builder.name != "dirhtml" or not app.config.per_symbol_modules:
        return
    base = (app.config.html_baseurl or "").rstrip("/") + "/"
    out = Path(app.outdir)
    min_words = app.config.per_symbol_sitemap_min_words
    docs = sorted(d for d in app.env.found_docs if d != "search" and not _is_thin(app, d, min_words))
    urls = []
    for d in docs:
        path = "" if d == "index" else d + "/"
        urls.append(base + path)
    xml = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    xml += [f"  <url><loc>{escape(u)}</loc></url>" for u in urls]
    xml.append("</urlset>")
    (out / "sitemap.xml").write_text("\n".join(xml) + "\n", encoding="utf-8")

    # Symbols that moved off the landing page; anchors that stay on index
    # (module-<name>) need no redirect.
    legacy = {
        name: entry.docname + "/"
        for name, entry in app.env.domaindata["py"]["objects"].items()
        if entry.docname != "index"
    }
    (out / "_static" / "legacy-anchors.json").write_text(json.dumps(legacy, sort_keys=True, separators=(",", ":")), encoding="utf-8")


def _page_url(app: Sphinx, pagename: str, templatename: str, context: dict, doctree: Any) -> None:
    """Give sphinx_rtd_theme a correct dirhtml canonical URL.

    Sphinx 7.x builds ``pageurl`` with the .html out_suffix even under dirhtml, which
    yields a canonical that does not match the served URL. Override it.
    """
    context["per_symbol_modules_enabled"] = bool(app.config.per_symbol_modules)
    if not app.config.html_baseurl or app.builder.name != "dirhtml":
        return
    base = app.config.html_baseurl.rstrip("/") + "/"
    if pagename == "index":
        context["pageurl"] = base
    elif pagename.endswith("/index"):
        context["pageurl"] = base + pagename[: -len("index")]
    else:
        context["pageurl"] = base + pagename + "/"


def _add_static(app: Sphinx, config: Any) -> None:
    config.html_static_path.append(str(Path(__file__).parent / "static"))


def setup(app: Sphinx) -> dict[str, Any]:
    app.add_config_value("per_symbol_modules", [], "env")
    app.add_config_value("per_symbol_honor_all", False, "env")
    app.add_config_value("per_symbol_sitemap_min_words", 25, "env")
    app.connect("config-inited", _add_static)
    app.add_css_file("per_symbol.css")
    app.connect("builder-inited", _generate)
    app.connect("build-finished", _finish)
    app.connect("html-page-context", _page_url)
    return {"version": "1.0", "parallel_read_safe": True, "parallel_write_safe": True}
