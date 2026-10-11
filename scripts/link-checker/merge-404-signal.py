#!/usr/bin/env python3
"""Merge the reader-signals real-404 export into the link checker's results.

Deterministic workflow step (never model-run) that runs between
`make check_links` and the check-links workflow's broken-count gate. The
crawler finds links that are broken *on our own pages*; the reader-signals
export's `not_found` section (server-log 404 hits) finds URLs readers actually
request that don't exist — external referrers, bookmarks, stale search results
— which no crawl of our own pages can see. Merging the two lets the existing
fix-broken-links triage work both lists at once, highest-traffic first.

What it does to `.broken-links.json` (in place):

1. Annotates existing `internal` entries whose destination path appears in
   `not_found` with `"hits": N` (real reader traffic on that breakage).
2. Appends one entry per `not_found` path with hits >= MIN_HITS that no
   crawler entry already covers: `{"source": "(server logs)", "destination":
   "https://www.pulumi.com<path>", "reason": "REAL_404", "hits": N}` — capped
   at MAX_APPENDED per run so one bad export can't flood the triage.
3. Sorts `internal` by hits descending (entries without hits keep their
   relative order at the end), so triage works high-traffic-first.

No HTTP probing happens here: the fix-broken-links skill re-verifies every
entry before touching anything, which also guards against a stale export.

Degrades to a no-op (exit 0, file untouched) when the signals file is missing,
unreadable, or has no `not_found` section — the pre-export steady state.

Usage:
    merge-404-signal.py [--signals .reader-signals.json] [--broken .broken-links.json]
    merge-404-signal.py --self-test
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

SITE = "https://www.pulumi.com"
MIN_HITS = 50  # server-log 404s below this are long-tail noise; skip
MAX_APPENDED = 25  # flood guard: one bad export can't swamp the triage


def log(msg: str) -> None:
    print(f"merge-404-signal: {msg}", file=sys.stderr)


def norm_path(url_or_path: str) -> str:
    """Normalize a URL or path to a bare site-relative path with trailing slash."""
    s = (url_or_path or "").strip()
    if "://" in s:
        s = urlparse(s).path
    s = s.split("#", 1)[0].split("?", 1)[0]
    if not s.startswith("/"):
        s = "/" + s
    # Normalize to trailing slash except for file-like paths (e.g. /foo.html).
    if not s.endswith("/") and not re.search(r"\.[A-Za-z0-9]{1,5}$", s):
        s += "/"
    return s


def load_not_found(signals_file: Path) -> dict[str, int]:
    """{normalized path: hits} from the export, or {} when absent/malformed."""
    if not signals_file.is_file():
        return {}
    try:
        data = json.loads(signals_file.read_text(errors="replace"))
    except (OSError, json.JSONDecodeError):
        return {}
    if not isinstance(data, dict):
        return {}
    section = (data.get("signals") or {}).get("not_found")
    if not isinstance(section, dict) or not isinstance(section.get("paths"), dict):
        return {}
    out: dict[str, int] = {}
    for path, row in section["paths"].items():
        try:
            hits = int(float((row or {}).get("hits", 0)))
        except (TypeError, ValueError, AttributeError):
            continue
        if hits > 0:
            p = norm_path(str(path))
            out[p] = max(out.get(p, 0), hits)
    return out


def merge(broken: dict, not_found: dict[str, int]) -> tuple[dict, int, int]:
    """Return (merged results, annotated count, appended count)."""
    internal = broken.get("internal")
    if not isinstance(internal, list):
        internal = []
        broken["internal"] = internal

    covered: set[str] = set()
    annotated = 0
    for entry in internal:
        if not isinstance(entry, dict):
            continue
        dest = norm_path(str(entry.get("destination", "")))
        covered.add(dest)
        if dest in not_found:
            entry["hits"] = not_found[dest]
            annotated += 1

    appendable = sorted(
        ((hits, path) for path, hits in not_found.items()
         if hits >= MIN_HITS and path not in covered),
        key=lambda t: (-t[0], t[1]),
    )
    dropped = max(len(appendable) - MAX_APPENDED, 0)
    for hits, path in appendable[:MAX_APPENDED]:
        internal.append({
            "source": "(server logs)",
            "destination": f"{SITE}{path}",
            "reason": "REAL_404",
            "hits": hits,
        })
    if dropped:
        log(f"appended cap reached: dropped {dropped} lower-traffic real-404 path(s) "
            f"(they'll resurface next run if still 404ing)")

    # Highest reader impact first; unhit crawler entries keep their relative
    # order at the end (sorted() is stable).
    internal.sort(key=lambda e: -(e.get("hits") or 0) if isinstance(e, dict) else 0)

    return broken, annotated, len(appendable[:MAX_APPENDED])


def run(signals_path: Path, broken_path: Path) -> int:
    not_found = load_not_found(signals_path)
    if not not_found:
        log(f"no usable not_found section in {signals_path}; leaving {broken_path} untouched")
        return 0
    if not broken_path.is_file():
        log(f"{broken_path} not found; leaving it untouched (nothing to merge into)")
        return 0
    try:
        broken = json.loads(broken_path.read_text())
    except (OSError, json.JSONDecodeError) as e:
        log(f"{broken_path} unreadable ({e}); leaving it untouched")
        return 0
    if not isinstance(broken, dict):
        log(f"{broken_path} has an unexpected shape; leaving it untouched")
        return 0

    merged, annotated, appended = merge(broken, not_found)
    broken_path.write_text(json.dumps(merged, indent=2) + "\n")
    log(f"annotated {annotated} crawler entr(ies) with hits, appended {appended} "
        f"REAL_404 entr(ies) from {len(not_found)} server-log path(s)")
    return 0


def self_test() -> int:
    failures = []

    def check(name, cond):
        if not cond:
            failures.append(name)
            print(f"FAIL: {name}", file=sys.stderr)
        else:
            print(f"ok: {name}")

    check("norm_path strips origin and adds slash",
          norm_path("https://www.pulumi.com/docs/old") == "/docs/old/")
    check("norm_path keeps file-like paths slashless",
          norm_path("/docs/foo.html") == "/docs/foo.html")
    check("norm_path drops fragment and query",
          norm_path("/docs/a/?x=1#frag") == "/docs/a/")

    nf = {"/docs/gone/": 210, "/docs/tail/": 3, "/docs/covered/": 90}
    broken = {
        "generated": "2026-07-09T15:00:00Z",
        "internal": [
            {"source": "https://www.pulumi.com/docs/x/",
             "destination": "https://www.pulumi.com/docs/covered/", "reason": "HTTP_404"},
            {"source": "https://www.pulumi.com/docs/y/",
             "destination": "https://www.pulumi.com/docs/unrelated/", "reason": "HTTP_404"},
        ],
        "external": [],
    }
    merged, annotated, appended = merge(json.loads(json.dumps(broken)), nf)
    internal = merged["internal"]
    check("crawler entry covered by logs gets hits", annotated == 1
          and any(e.get("hits") == 90 and "covered" in e["destination"] for e in internal))
    check("high-traffic uncovered path appended as REAL_404", appended == 1
          and any(e.get("reason") == "REAL_404" and e.get("hits") == 210 for e in internal))
    check("below-MIN_HITS path not appended",
          not any("tail" in e.get("destination", "") for e in internal))
    check("sorted by hits desc", [e.get("hits") for e in internal] == [210, 90, None])
    check("external untouched", merged["external"] == [])

    # Cap: MAX_APPENDED+10 eligible paths -> exactly MAX_APPENDED appended.
    many = {f"/docs/gone-{i:03d}/": 1000 + i for i in range(MAX_APPENDED + 10)}
    merged, _, appended = merge({"internal": [], "external": []}, many)
    check("appended list capped", appended == MAX_APPENDED
          and len(merged["internal"]) == MAX_APPENDED)
    check("cap keeps the highest-hit paths",
          merged["internal"][0]["hits"] == 1000 + MAX_APPENDED + 9)

    # Alias/dup handling inside not_found (same path twice via norm) keeps max.
    check("not_found normalizes and keeps max", load_not_found_from(
        {"signals": {"not_found": {"paths": {
            "/docs/a": {"hits": 5}, "/docs/a/": {"hits": 9}}}}}) == {"/docs/a/": 9})

    # Degradation shapes.
    check("missing not_found section -> {}", load_not_found_from({"signals": {}}) == {})
    check("garbage rows skipped", load_not_found_from(
        {"signals": {"not_found": {"paths": {"/x/": "nope", "/y/": {"hits": "abc"},
                                             "/z/": {"hits": 60}}}}}) == {"/z/": 60})

    if failures:
        print(f"\n{len(failures)} failure(s)", file=sys.stderr)
        return 1
    print("\nall merge-404-signal self-tests passed")
    return 0


def load_not_found_from(obj: dict) -> dict[str, int]:
    """Self-test helper: run load_not_found against an in-memory object."""
    import tempfile

    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump(obj, f)
        name = f.name
    try:
        return load_not_found(Path(name))
    finally:
        Path(name).unlink()


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--signals", default=".reader-signals.json")
    p.add_argument("--broken", default=".broken-links.json")
    p.add_argument("--self-test", action="store_true", help="run built-in smoke checks")
    args = p.parse_args()
    if args.self_test:
        return self_test()
    return run(Path(args.signals), Path(args.broken))


if __name__ == "__main__":
    sys.exit(main())
