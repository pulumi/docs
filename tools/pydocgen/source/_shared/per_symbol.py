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
        out.append(("class" if inspect.isclass(obj) else "function", name))
    return out


def _first_line(modname: str, name: str) -> str:
    doc = inspect.getdoc(getattr(importlib.import_module(modname), name)) or ""
    line = doc.strip().split("\n\n")[0].replace("\n", " ").strip()
    if len(line) > 140:
        line = line[:137].rsplit(" ", 1)[0] + "..."
    line = re.sub(r":\w+:`~?([^`]*)`", r"\1", line)
    for ch in "`*|\\":
        line = line.replace(ch, "")
    return re.sub(r"(?<!\w)_|_(?!\w)", "", line)


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
        overview.append(f"Classes and functions in ``{modname}``.\n")
        overview.append(".. list-table::\n   :widths: 35 65\n")
        entries = []
        for kind, name in symbols:
            full = f"{modname}.{name}"
            directive = "autoclass" if kind == "class" else "autofunction"
            body = f".. {directive}:: {full}\n"
            if kind == "class":
                body += "   :members:\n"
            title = f"{full}"
            (api / f"{full}.rst").write_text(f"{title}\n{'=' * len(title)}\n\n{body}", encoding="utf-8")
            entries.append(full)
            overview.append(f"   * - :doc:`{full} <api/{full}>`\n     - {_first_line(modname, name)}\n")
        overview.append("\n.. toctree::\n   :hidden:\n\n" + "".join(f"   api/{e}\n" for e in entries))
    (Path(app.srcdir) / "api" / "overview.inc").write_text("\n".join(overview), encoding="utf-8")


def _finish(app: Sphinx, exception: Exception | None) -> None:
    if exception or app.builder.name != "dirhtml" or not app.config.per_symbol_modules:
        return
    base = (app.config.html_baseurl or "").rstrip("/") + "/"
    out = Path(app.outdir)
    docs = sorted(d for d in app.env.found_docs if d != "search")
    urls = []
    for d in docs:
        path = "" if d == "index" else d + "/"
        urls.append(base + path)
    xml = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    xml += [f"  <url><loc>{escape(u)}</loc></url>" for u in urls]
    xml.append("</urlset>")
    (out / "sitemap.xml").write_text("\n".join(xml) + "\n", encoding="utf-8")

    legacy = {}
    for name, entry in app.env.domaindata["py"]["objects"].items():
        if entry.docname != "index":
            legacy[name] = "" if entry.docname == "index" else entry.docname + "/"
    for name, entry in app.env.domaindata["py"]["modules"].items():
        pass
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


def setup(app: Sphinx) -> dict[str, Any]:
    app.add_config_value("per_symbol_modules", [], "env")
    app.add_config_value("per_symbol_honor_all", False, "env")
    app.connect("builder-inited", _generate)
    app.connect("build-finished", _finish)
    app.connect("html-page-context", _page_url)
    return {"version": "1.0", "parallel_read_safe": True, "parallel_write_safe": True}
