#!/usr/bin/env python3
"""merge-claims.py — combine the claim-extraction layers into .candidate-claims.json.

Unions Layer A (`extract-claims.py` → `.candidate-claims-regex.json`) and the
two Layer-B LLM passes (`extract-claims-llm.py` → `.candidate-claims-llm-1.json`
/ `-2.json`) into the single artifact the main review reads as the claim floor.

What it does:
  - Loads each input. Missing / unparseable / error-only input → noted in
    `errors`, not fatal.
  - Anchors each LLM claim's `line_range` to the actual file: if the range is
    out of bounds for the file on disk, it's clamped to the file length and
    flagged `line_range_unverified` with confidence dropped to "low" (gross
    hallucination guard). In-bounds ranges are trusted as-is — the claim
    `text` is a self-contained restatement that deliberately differs from the
    source line, so token-matching the restatement against the line would
    false-positive on correct ranges. The `candidate-claims-coverage`
    validator matches by line-range ± a small window downstream.
  - Dedups by (overlapping line range) AND (token overlap ≥ threshold). Merged
    entries keep the best `text` (prefer an LLM restatement over the regex raw
    line), the union of `found_by`, the union of line ranges, and any
    `source_hint`. Confidence: `high` if `found_by` includes `regex` or two+
    passes found it; otherwise the LLM pass's own confidence.
  - Propagates the LLM passes' `errors` and token `meta` into the output.

False positives are expected and fine — the reviewer triages each entry (see
`references/pre-computation.md`). The floor only needs to be a superset of the
real claims; over-merges and stray entries are tolerable.

Usage:
    merge-claims.py [--regex .candidate-claims-regex.json] \
        [--llm .candidate-claims-llm-1.json --llm .candidate-claims-llm-2.json] \
        [--repo-root .] --out .candidate-claims.json

Output schema:
    {
      "schema_version": 1,
      "claims": [
        {"file": "...", "line_range": "L42" | "L42-47" | "L12, L88",
         "text": "...", "type": "...", "source_hint": "...",  # source_hint optional
         "confidence": "high"|"medium"|"low",
         "found_by": ["regex", "llm-atomic", "llm-holistic"],   # 1+ of these
         "line_range_unverified": true},                        # present only when flagged
        ...
      ],
      "errors": [ ... ],
      "meta": {"regex_claims": N, "llm_claims": N, "merged_claims": N,
               "llm_input_tokens": T, "llm_output_tokens": T,
               "llm_cache_read_input_tokens": T, "llm_cache_creation_input_tokens": T}
    }
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import traceback
from pathlib import Path

SCHEMA_VERSION = 1
TOKEN_OVERLAP_THRESHOLD = 0.34
RANGE_WINDOW = 1  # treat ranges within this many lines as overlapping

_STOPWORDS = {
    "the", "a", "an", "of", "to", "in", "on", "is", "are", "be", "and", "or",
    "for", "with", "that", "this", "it", "its", "by", "as", "at", "from", "was",
    "were", "has", "have", "had", "will", "can", "but", "not", "all", "any",
}

LINE_RANGE_RE = re.compile(r"L(\d+)(?:-(\d+))?")


# ---- loading ---------------------------------------------------------------


def load_json(path: Path) -> tuple[dict | None, str | None]:
    if not path.is_file():
        return None, f"{path.name}: not present"
    try:
        return json.loads(path.read_text(encoding="utf-8")), None
    except (OSError, json.JSONDecodeError) as e:
        return None, f"{path.name}: unreadable ({type(e).__name__}: {e})"


# ---- line-range helpers ----------------------------------------------------


def parse_ranges(line_range: str) -> list[tuple[int, int]]:
    out: list[tuple[int, int]] = []
    for m in LINE_RANGE_RE.finditer(line_range or ""):
        a = int(m.group(1))
        b = int(m.group(2)) if m.group(2) else a
        if b < a:
            a, b = b, a
        out.append((a, b))
    return out or [(0, 0)]


def serialize_ranges(ranges: list[tuple[int, int]]) -> str:
    # Merge overlapping/adjacent, sort, render.
    if not ranges:
        return "L0"
    merged: list[list[int]] = []
    for a, b in sorted(ranges):
        if merged and a <= merged[-1][1] + 1:
            merged[-1][1] = max(merged[-1][1], b)
        else:
            merged.append([a, b])
    parts = [f"L{a}" if a == b else f"L{a}-{b}" for a, b in merged]
    return ", ".join(parts)


def ranges_overlap(ra: list[tuple[int, int]], rb: list[tuple[int, int]], window: int = RANGE_WINDOW) -> bool:
    for a1, b1 in ra:
        for a2, b2 in rb:
            if a1 <= b2 + window and a2 <= b1 + window:
                return True
    return False


# ---- text similarity -------------------------------------------------------


def tokenize(text: str) -> set[str]:
    toks: set[str] = set()
    for raw in re.findall(r"[A-Za-z0-9][A-Za-z0-9._-]*", (text or "").lower()):
        if any(ch.isdigit() for ch in raw):
            toks.add(raw)  # numbers/versions/identifiers: keep regardless of length
        elif len(raw) >= 3 and raw not in _STOPWORDS:
            toks.add(raw)
    return toks


def token_overlap(a: str, b: str) -> float:
    ta, tb = tokenize(a), tokenize(b)
    if not ta or not tb:
        return 0.0
    shared = ta & tb
    if len(shared) < 2:
        return 0.0  # one shared token is never enough to call it the same claim
    return len(shared) / min(len(ta), len(tb))


# ---- anchoring -------------------------------------------------------------


def anchor_llm_claim(claim: dict, repo_root: Path) -> None:
    """Clamp an out-of-bounds line range to the file length; flag it. Mutates `claim`."""
    path = repo_root / claim.get("file", "")
    if not path.is_file():
        return  # can't check; trust as-is (already a degraded case if so)
    try:
        n_lines = len(path.read_text(encoding="utf-8", errors="replace").splitlines())
    except OSError:
        return
    if n_lines == 0:
        return
    ranges = parse_ranges(claim.get("line_range", ""))
    clamped: list[tuple[int, int]] = []
    flagged = False
    for a, b in ranges:
        na = min(max(a, 1), n_lines)
        nb = min(max(b, 1), n_lines)
        if na < nb:
            na, nb = min(na, nb), max(na, nb)
        if (na, nb) != (a, b):
            flagged = True
        clamped.append((na, nb))
    if flagged:
        claim["line_range"] = serialize_ranges(clamped)
        claim["line_range_unverified"] = True
        claim["confidence"] = "low"


# ---- merge -----------------------------------------------------------------


def _is_llm(found_by: list[str]) -> bool:
    return any(fb.startswith("llm-") for fb in (found_by or []))


def merge_into(group: list[dict]) -> dict:
    """Collapse a group of same-claim records into one."""
    # Pick the representative text: prefer an LLM restatement; among those (or
    # if none), prefer the longest text.
    llm_records = [c for c in group if _is_llm(c.get("found_by", []))]
    text_pool = llm_records or group
    rep = max(text_pool, key=lambda c: len(c.get("text", "")))

    found_by: list[str] = []
    for c in group:
        for fb in c.get("found_by", []):
            if fb not in found_by:
                found_by.append(fb)
    # Stable ordering: regex first, then atomic, then holistic, then anything else.
    order = {"regex": 0, "llm-atomic": 1, "llm-holistic": 2}
    found_by.sort(key=lambda fb: (order.get(fb, 9), fb))

    ranges: list[tuple[int, int]] = []
    for c in group:
        ranges.extend(parse_ranges(c.get("line_range", "")))

    source_hint = None
    for c in group:
        if c.get("source_hint"):
            source_hint = c["source_hint"]
            break

    # Type: prefer the representative's type. Only let a regex-layer concrete
    # type (`numerical`/`version`/`url`) win when the representative's type is
    # one of the generic/soft buckets — never override a more-specific LLM type
    # like `attribution`/`entity-spec`/`api-surface`/`quote`.
    soft_types = {"behavior", "feature", "positioning", "comparison", "cross-reference"}
    concrete = {"numerical", "version", "url"}
    type_ = rep.get("type", "behavior")
    if type_ in soft_types:
        for c in group:
            if "regex" in c.get("found_by", []) and c.get("type") in concrete:
                type_ = c["type"]
                break

    # Confidence: high if regex found it OR ≥2 passes found it; else the LLM's own.
    if "regex" in found_by or len(found_by) >= 2:
        confidence = "high"
    else:
        confidence = rep.get("confidence", "medium")

    out = {
        "file": rep.get("file", ""),
        "line_range": serialize_ranges(ranges),
        "text": rep.get("text", "").strip(),
        "type": type_,
        "confidence": confidence,
        "found_by": found_by,
    }
    if source_hint:
        out["source_hint"] = source_hint
    if any(c.get("line_range_unverified") for c in group):
        out["line_range_unverified"] = True
        # An unverified anchor on every contributing record means we shouldn't
        # claim high confidence purely from pass-count.
        if all(c.get("line_range_unverified") for c in llm_records) and "regex" not in found_by:
            out["confidence"] = "low"
    return out


def merge_claims(all_records: list[dict]) -> list[dict]:
    """Group records by (overlapping line range within the same file) AND
    (token overlap ≥ threshold); collapse each group."""
    # Bucket by file first.
    by_file: dict[str, list[dict]] = {}
    for r in all_records:
        by_file.setdefault(r.get("file", ""), []).append(r)

    merged: list[dict] = []
    for _file, recs in by_file.items():
        # Greedy single-linkage clustering.
        clusters: list[list[dict]] = []
        cluster_ranges: list[list[tuple[int, int]]] = []
        for r in recs:
            r_ranges = parse_ranges(r.get("line_range", ""))
            placed = False
            for i, cl in enumerate(clusters):
                if not ranges_overlap(r_ranges, cluster_ranges[i]):
                    continue
                # Does r's text overlap any member's text enough?
                if any(token_overlap(r.get("text", ""), m.get("text", "")) >= TOKEN_OVERLAP_THRESHOLD for m in cl):
                    cl.append(r)
                    cluster_ranges[i] = cluster_ranges[i] + r_ranges
                    placed = True
                    break
            if not placed:
                clusters.append([r])
                cluster_ranges.append(list(r_ranges))
        for cl in clusters:
            merged.append(merge_into(cl))
    # Sort for stable output: by file, then by first line.
    def sort_key(c: dict):
        rs = parse_ranges(c.get("line_range", ""))
        first = min((a for a, _ in rs), default=0)
        return (c.get("file", ""), first, c.get("type", ""))
    merged.sort(key=sort_key)
    return merged


# ---- driver ----------------------------------------------------------------


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--regex", default=".candidate-claims-regex.json", help="Layer-A regex artifact")
    p.add_argument("--llm", action="append", default=None,
                   help="Layer-B LLM-pass artifact (repeatable). Default: .candidate-claims-llm-1.json + -2.json")
    p.add_argument("--repo-root", default=".", help="Repo root (for anchoring LLM line ranges)")
    p.add_argument("--out", default=".candidate-claims.json", help="Output JSON path")
    args = p.parse_args()

    repo_root = Path(args.repo_root).resolve()
    out_path = Path(args.out)
    llm_paths = args.llm if args.llm is not None else [".candidate-claims-llm-1.json", ".candidate-claims-llm-2.json"]

    errors: list[str] = []
    all_records: list[dict] = []
    regex_count = 0
    llm_count = 0
    token_meta = {"llm_input_tokens": 0, "llm_output_tokens": 0,
                  "llm_cache_read_input_tokens": 0, "llm_cache_creation_input_tokens": 0}

    # Layer A (regex).
    regex_doc, err = load_json(Path(args.regex))
    if err:
        errors.append(f"regex layer {err}")
    elif isinstance(regex_doc, dict):
        for e in regex_doc.get("errors", []) or []:
            errors.append(f"regex layer: {e}")
        for c in regex_doc.get("claims", []) or []:
            if not isinstance(c, dict):
                continue
            c = dict(c)
            c["found_by"] = ["regex"]
            c.setdefault("confidence", "high")
            all_records.append(c)
            regex_count += 1

    # Layer B (LLM passes).
    for lp in llm_paths:
        doc, err = load_json(Path(lp))
        if err:
            errors.append(f"llm pass {err}")
            continue
        if not isinstance(doc, dict):
            continue
        for e in doc.get("errors", []) or []:
            errors.append(f"llm pass [{doc.get('pass', '?')}]: {e}")
        meta = doc.get("meta", {}) or {}
        token_meta["llm_input_tokens"] += int(meta.get("input_tokens", 0) or 0)
        token_meta["llm_output_tokens"] += int(meta.get("output_tokens", 0) or 0)
        token_meta["llm_cache_read_input_tokens"] += int(meta.get("cache_read_input_tokens", 0) or 0)
        token_meta["llm_cache_creation_input_tokens"] += int(meta.get("cache_creation_input_tokens", 0) or 0)
        pass_name = doc.get("pass", "?")
        for c in doc.get("claims", []) or []:
            if not isinstance(c, dict):
                continue
            if not (c.get("line_range") and c.get("text") and c.get("type")):
                continue
            c = dict(c)
            if not c.get("found_by"):
                c["found_by"] = [f"llm-{pass_name}"]
            c.setdefault("confidence", "medium")
            anchor_llm_claim(c, repo_root)
            all_records.append(c)
            llm_count += 1

    merged = merge_claims(all_records)

    meta = {"regex_claims": regex_count, "llm_claims": llm_count, "merged_claims": len(merged), **token_meta}
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps({
        "schema_version": SCHEMA_VERSION,
        "claims": merged,
        "errors": errors,
        "meta": meta,
    }, indent=2) + "\n")
    print(
        f"merge-claims: {regex_count} regex + {llm_count} llm → {len(merged)} merged claim(s) "
        f"({len(errors)} error note(s)) → {out_path}",
        file=sys.stderr,
    )
    return 0


def safe_main() -> int:
    try:
        return main()
    except SystemExit:
        raise
    except BaseException as e:  # noqa: BLE001
        out_path = None
        for i, a in enumerate(sys.argv):
            if a == "--out" and i + 1 < len(sys.argv):
                out_path = Path(sys.argv[i + 1])
            elif a.startswith("--out="):
                out_path = Path(a.split("=", 1)[1])
        if out_path is None:
            out_path = Path(".candidate-claims.json")
        try:
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(json.dumps({
                "schema_version": SCHEMA_VERSION,
                "claims": [],
                "errors": [f"merge-claims uncaught exception: {type(e).__name__}: {e}"],
                "meta": {"regex_claims": 0, "llm_claims": 0, "merged_claims": 0,
                         "llm_input_tokens": 0, "llm_output_tokens": 0,
                         "llm_cache_read_input_tokens": 0, "llm_cache_creation_input_tokens": 0},
            }, indent=2) + "\n")
        except OSError:
            pass
        traceback.print_exc(file=sys.stderr)
        return 0


if __name__ == "__main__":
    sys.exit(safe_main())
