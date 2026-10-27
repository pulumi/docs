"""Domain grouping of pulumi_cloud_sdk.models for the per-symbol reference pages.

The models module has ~950 classes whose docstrings are field lists only, so one page per class
would be thin. Instead each model lands on the page for the API class (Stacks, Organizations, ...)
whose method signatures reach it, directly or through other models' fields. Models reached by more
than one API go to "Shared", unreached ones to "Other". Oversized groups are split alphabetically.
"""
from __future__ import annotations

import collections
import importlib
import inspect
import re

MAX_PER_PAGE = 150
_TOKEN = re.compile(r"\b[A-Z][A-Za-z0-9_]*\b")
_SPECIAL = {"AI": "AI", "AI_Agents": "AI agents", "VCS_Integrations": "VCS integrations", "CloudSetup": "Cloud setup",
            "RegistryPreview": "Registry preview"}


def _title(api_class: str) -> str:
    base = api_class[: -len("Api")] if api_class.endswith("Api") else api_class
    return _SPECIAL.get(base, base)


def group_models(modname: str, symbols: list[tuple[str, str]]) -> list[tuple[str, str, list[tuple[str, str]]]]:
    """Return (slug, page title, symbols) tuples for the given module's symbols."""
    root = modname.rsplit(".", 1)[0]
    mod = importlib.import_module(modname)
    apis = importlib.import_module(root + ".apis")
    kinds = dict((n, k) for k, n in symbols)
    names = set(kinds)

    def refs(text: str) -> set[str]:
        return {t for t in _TOKEN.findall(text) if t in names}

    direct: dict[str, set[str]] = {}
    for an, ac in sorted(vars(apis).items()):
        if not inspect.isclass(ac) or an.startswith("_") or not an.endswith("Api"):
            continue
        found: set[str] = set()
        for mn, m in vars(ac).items():
            if mn.startswith("_") or not callable(m):
                continue
            try:
                sig = inspect.signature(m)
            except (TypeError, ValueError):
                continue
            for p in sig.parameters.values():
                found |= refs(str(p.annotation))
            found |= refs(str(sig.return_annotation))
        direct[an] = found
    child = {n: refs(getattr(mod, n).__dict__.get("__doc__") or "") - {n} for n in names}

    owners: dict[str, list[str]] = collections.defaultdict(list)
    for an, seed in direct.items():
        seen, stack = set(seed), list(seed)
        while stack:
            for c in child[stack.pop()]:
                if c not in seen:
                    seen.add(c)
                    stack.append(c)
        for n in seen:
            owners[n].append(an)

    buckets: dict[str, list[str]] = collections.defaultdict(list)
    for n in sorted(names):
        o = owners.get(n, [])
        buckets[_title(o[0]) if len(o) == 1 else ("Shared" if o else "Other")].append(n)

    out = []
    for title in sorted(buckets):
        members = buckets[title]
        parts = [members[i:i + MAX_PER_PAGE] for i in range(0, len(members), MAX_PER_PAGE)]
        for i, part in enumerate(parts, 1):
            label = title if len(parts) == 1 else f"{title} ({part[0][0].upper()}-{part[-1][0].upper()})" if part[0][0] != part[-1][0] else f"{title} ({part[0][0].upper()})"
            slug = re.sub(r"[^A-Za-z0-9]+", "-", f"{title}-{i}" if len(parts) > 1 else title).strip("-").lower()
            out.append((slug, f"{label} models", [(kinds[n], n) for n in part]))
    return out
