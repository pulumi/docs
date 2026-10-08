#!/usr/bin/env python3
"""One-time repair: synthesize findings records for reviews that predate them.

CONTEXT. A fix-lane review banks the judgment-level findings it declines to
apply, and the glow-up lane comes back later to execute them. Until 2026-08-20
the only durable trace of a banked finding was a COUNTER in the ledger
(`skipped_findings`) plus the review PR's body prose. `record-page-findings.py`
closed that on 2026-08-20 by writing a structured record to the ledger bucket's
`findings/` prefix — but only forward.

Measured against the live ledger on 2026-08-25 (146 entries, 115 carrying a
banked signal):

    19  have a findings record          -> recover cleanly
    46  have only a review PR body      -> recoverable, but only from prose
    50  have NEITHER                    -> unrecoverable, the count is unbacked

This script is for the middle 46. It reads each page's prior review PRs the way
`build-glowup-backlog.py` does at glow-up time, and writes what it finds as a
findings record — so the backlog survives someone tidying a markdown table, and
`select-glowup.py`'s recoverability check can see it without a GitHub round
trip. Nothing here can help the 50: those reasons were never written down
anywhere, and only a fresh review replaces them (which is what the glow-up
lane's `repairs` route now arranges).

NOT A WORKFLOW. Run it by hand, once. A scheduled version would be a second,
weaker writer competing with `record-page-findings.py` — which has the review's
own artifacts and its verdict, where this has only prose someone typed for a
human. Records written here carry `"synthetic": true` so the two can never be
confused in a later audit.

Extraction is `build-glowup-backlog.py`'s, imported rather than reimplemented:
the same heading vocabulary, the same lane-aware section choice, the same
noise/trailer filters, the same cross-PR de-duplication. That file has absorbed
several rounds of live-run fixes and a second copy of its parser would rot.

Every synthesized finding is `applied: false` by construction — the banked
sections are, by definition, what the review did NOT apply.

Usage:
    backfill-findings-records.py --ledger-dir .ledger-cache \
        --findings-dir .findings-cache [--out-dir .backfilled] \
        [--uri s3://<bucket>/findings/] [--limit N] [--dry-run]
    backfill-findings-records.py --self-test
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

SCHEMA_VERSION = 1

# The scraper, imported by path (hyphenated filename, main() guarded) — the
# select-glowup.py pattern. Reusing it is the point: one parser, one place.
_spec = importlib.util.spec_from_file_location(
    "build_glowup_backlog", HERE / "build-glowup-backlog.py")
_bgb = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_bgb)


def log(msg: str) -> None:
    print(f"backfill-findings-records: {msg}", file=sys.stderr)


def warn(msg: str) -> None:
    print(f"::warning::backfill-findings-records: {msg}", file=sys.stderr)


# A banked line arrives as one of two shapes: the composer's bullet
# (`- **Label** — why it was deferred`) or a table row (`| Label | why |`).
# Splitting them into label/detail is what makes the record readable by
# `banked_from_findings`, which renders "<label> — <detail>" back out.
_LIST_MARKER_RE = re.compile(r"^[-*+]\s+")
_DASH_SPLIT_RE = re.compile(r"\s+(?:—|–|--)\s+")


def parse_row(line: str) -> tuple[str, str]:
    """(label, detail) for one banked line. Never raises; label may be ''."""
    text = _LIST_MARKER_RE.sub("", str(line or "").strip())
    if text.startswith("|"):
        cells = [c.strip() for c in text.strip("|").split("|")]
        label, detail = (cells[0] if cells else ""), " — ".join(c for c in cells[1:] if c)
    else:
        parts = _DASH_SPLIT_RE.split(text, maxsplit=1)
        label, detail = parts[0].strip(), (parts[1].strip() if len(parts) > 1 else "")
    # Strip the composer's emphasis so the label reads as the finding, not as
    # markdown. `_dedupe_key` keys on the label, so this also keeps a bolded
    # row and a plain one from banking twice.
    label = label.strip().strip("*_").strip()
    return label, detail


def scrape(slug: str, numbers: list[int], pr_json: str | None
           ) -> tuple[list[dict], list[dict], dict]:
    """(banked lines, source PRs, recovery block) for one page."""
    prs, recovery = _bgb.discover_prs(slug, numbers, pr_json)
    banked: list[dict] = []
    for pr in prs:
        head = pr.get("headRefName") or ""
        number = int(pr.get("number") or 0)
        for section, lines in _bgb.extract_sections(
                pr.get("body") or "", _bgb.sections_for(head)).items():
            for line in lines:
                _bgb._bank(banked, {
                    "id": f"pr{number}-{len(banked) + 1}",
                    "section": section,
                    "source_pr": number,
                    # A glow-up's "Backlog declined" rows carry decline history
                    # the plain rows don't; _bank prefers them on collision, so
                    # the marker has to be set here for that to work.
                    "source": ("glowup-declined"
                               if section == "Backlog declined" else "pr-body"),
                    "text": line,
                })
    return banked, prs, recovery


def build_record(path: str, slug: str, entry: dict, banked: list[dict],
                 prs: list[dict]) -> dict:
    findings = []
    for i, item in enumerate(banked, start=1):
        label, detail = parse_row(item["text"])
        if not label:
            continue
        findings.append({
            "id": f"b{i}",
            "label": label,
            "detail": detail,
            # Where it came from, not what kind of finding it is: the PR body
            # records neither the pre-step that found it nor its category, and
            # inventing either would put a guess in the system of record.
            "source": item["source"],
            "category": None,
            "line_range": None,
            "fix_candidate": False,
            # By construction: these are the sections of what was NOT applied.
            "applied": False,
        })
    return {
        "schema_version": SCHEMA_VERSION,
        "slug": slug,
        "path": path,
        # The review this was banked by, not today — the record describes that
        # review, and a fresh date would make it outrank a real one.
        "reviewed_at": entry.get("reviewed_at"),
        # Unknown, and deliberately not filled with HEAD: the record describes
        # a review of some older commit, and naming the wrong one is worse
        # than naming none.
        "commit": "",
        "verdict": entry.get("status"),
        "counts": {"total": len(findings), "applied": 0, "deferred": len(findings)},
        # The tell. A record written by record-page-findings.py has the
        # review's own artifacts behind it; this one has prose typed for a
        # human. An audit must always be able to tell them apart.
        "synthetic": True,
        "source_prs": [{"number": int(p.get("number") or 0), "url": p.get("url")}
                       for p in prs],
        "findings": findings,
    }


def candidates(ledger_dir: Path, findings_dir: Path | None) -> list[tuple[str, str, dict]]:
    """(path, slug, entry) for every ledger entry that needs a record and
    might still have one recoverable."""
    out = []
    for f in sorted(ledger_dir.glob("*.json")):
        try:
            entry = json.loads(f.read_text())
        except (OSError, json.JSONDecodeError):
            warn(f"{f.name} unreadable; skipped")
            continue
        if not isinstance(entry, dict):
            continue
        slug = entry.get("slug") or f.stem
        path = entry.get("path") or ""
        if findings_dir and (findings_dir / f"{slug}.json").is_file():
            continue  # already has the real thing
        banked = int(entry.get("skipped_findings") or 0)
        if banked <= 0 and not entry.get("clarity_flag"):
            continue  # nothing was ever banked, so there is nothing to recover
        if not (entry.get("pr_number") or entry.get("last_pr_number")):
            continue  # the unrecoverable 50 — no PR body to read
        out.append((path, slug, entry))
    return out


def run(args) -> int:
    ledger_dir = Path(args.ledger_dir)
    if not ledger_dir.is_dir():
        warn(f"{ledger_dir} is not a directory")
        return 1
    findings_dir = Path(args.findings_dir) if args.findings_dir else None
    todo = candidates(ledger_dir, findings_dir)
    if args.limit:
        todo = todo[: args.limit]
    log(f"{len(todo)} entry/entries with a banked count, no record, and a PR to read")

    out_dir = Path(args.out_dir) if args.out_dir else None
    if out_dir and not args.dry_run:
        out_dir.mkdir(parents=True, exist_ok=True)

    written = empty = 0
    for path, slug, entry in todo:
        numbers = [int(n) for n in (entry.get("pr_number"), entry.get("last_pr_number"))
                   if n]
        banked, prs, recovery = scrape(slug, numbers, args.pr_json)
        record = build_record(path, slug, entry, banked, prs)
        if not record["findings"]:
            # Recovering nothing is a real answer, not a failure — the PR body
            # may have carried only noise, or the query may have failed. Say
            # which, and write nothing: an empty record would look like a
            # reviewed page with no debt and stop the page ever being repaired.
            empty += 1
            log(f"{slug}: recovered nothing [{recovery.get('state')}]; no record written")
            continue
        written += 1
        body = json.dumps(record, indent=2) + "\n"
        if args.dry_run:
            print(f"--- {slug}.json ({len(record['findings'])} finding(s)) ---")
            print(body)
            continue
        if out_dir:
            (out_dir / f"{slug}.json").write_text(body)
        if args.uri:
            _upload(record, args.uri)
        log(f"{slug}: {len(record['findings'])} finding(s) from "
            f"{len(record['source_prs'])} PR(s)")

    log(f"done: {written} record(s) {'previewed' if args.dry_run else 'written'}, "
        f"{empty} recovered nothing")
    return 0


def _upload(record: dict, uri: str) -> None:
    import subprocess
    key = f"{uri.rstrip('/')}/{record['slug']}.json"
    proc = subprocess.run(["aws", "s3", "cp", "-", key, "--quiet"],
                          input=json.dumps(record, indent=2) + "\n",
                          text=True, capture_output=True)
    if proc.returncode != 0:
        warn(f"upload to {key} failed: {proc.stderr.strip()[:200]}")
    else:
        log(f"uploaded {key}")


def self_test() -> int:
    passes, failures = 0, []

    def check(label, ok):
        nonlocal passes
        if ok:
            passes += 1
            print(f"ok: {label}")
        else:
            failures.append(label)
            print(f"FAIL: {label}", file=sys.stderr)

    # --- row parsing ------------------------------------------------------
    check("a composer bullet splits into label and reason",
          parse_row("- **'all of' is too wordy** — style nit, left for a rewrite")
          == ("'all of' is too wordy", "style nit, left for a rewrite"))
    check("a table row splits on the pipes",
          parse_row("| Screenshot is stale | shows the old nav |")
          == ("Screenshot is stale", "shows the old nav"))
    check("a bare line is all label, no detail",
          parse_row("Diagram needs redrawing") == ("Diagram needs redrawing", ""))
    check("emphasis is stripped so a bolded and a plain row dedupe alike",
          parse_row("- **Same finding** — a")[0] == parse_row("Same finding — b")[0])
    check("an en dash separates too",
          parse_row("Label – reason") == ("Label", "reason"))

    # --- scraping, with gh fully stubbed out -------------------------------
    # `--pr-json` is a FILE (build-glowup-backlog's contract), which is also
    # what suppresses every gh call — the property this suite depends on.
    import tempfile
    tmpdir = tempfile.TemporaryDirectory()
    tmp = Path(tmpdir.name)

    def pr_file(name: str, payload: list) -> str:
        f = tmp / name
        f.write_text(json.dumps(payload))
        return str(f)

    pr_json = pr_file("fix-prs.json", [{
        "number": 20953, "url": "https://example/20953",
        "headRefName": "content-review/docs-concepts-alpha",
        "body": ("## Fixes applied\n- Fixed a typo\n\n"
                 "## Findings not applied\n"
                 "- **'all of' is too wordy** — style, deferred\n"
                 "- **Diagram is stale** — needs a redraw\n\n"
                 "## Screenshot check\nNo images. The page references none.\n"),
    }])
    banked, prs, recovery = scrape("docs-concepts-alpha", [20953], pr_json)
    check("banked rows come from the deferred section only",
          len(banked) == 2 and all("wordy" in b["text"] or "Diagram" in b["text"]
                                   for b in banked))
    check("'Fixes applied' is never banked — that work landed",
          not any("typo" in b["text"] for b in banked))
    check("the composer's no-images pre-fill is noise, not a finding",
          not any("No images" in b["text"] for b in banked))
    check("recovery state is reported", recovery.get("state") == "recovered")

    entry = {"reviewed_at": "2026-07-02", "status": "reviewed",
             "skipped_findings": 2, "pr_number": 20953}
    rec = build_record("content/docs/concepts/alpha.md", "docs-concepts-alpha",
                       entry, banked, prs)
    check("every synthesized finding is deferred, never applied",
          all(f["applied"] is False for f in rec["findings"])
          and rec["counts"] == {"total": 2, "applied": 0, "deferred": 2})
    check("the record is marked synthetic", rec["synthetic"] is True)
    check("it is dated to the review it describes, not to today",
          rec["reviewed_at"] == "2026-07-02")
    check("no commit is invented for a review of an unknown commit",
          rec["commit"] == "")
    check("the source PRs are recorded",
          [p["number"] for p in rec["source_prs"]] == [20953])

    # The whole point: build-glowup-backlog must read back what we wrote.
    read_back = _bgb.banked_from_findings(rec)
    check("build-glowup-backlog recovers the findings from the record",
          len(read_back) == 2
          and any("'all of' is too wordy — style, deferred" == b["text"]
                  for b in read_back))

    # --- a glow-up PR's declined rows are debt too --------------------------
    g_json = pr_file("glowup-prs.json", [{
        "number": 21001, "url": "https://example/21001",
        "headRefName": "content-review/glowup-docs-concepts-alpha",
        "body": "## Backlog executed\n- Rewrote the intro\n\n"
                "## Backlog declined\n- **Diagram is stale** — out of scope\n",
    }])
    g_banked, _, _ = scrape("docs-concepts-alpha", [21001], g_json)
    check("a glow-up's declined rows are banked under its own headings",
          len(g_banked) == 1 and g_banked[0]["source"] == "glowup-declined")
    check("a glow-up's executed rows are not — that work landed",
          not any("Rewrote" in b["text"] for b in g_banked))

    # --- candidate selection ----------------------------------------------
    with tempfile.TemporaryDirectory() as td:
        led = Path(td) / "ledger"
        fnd = Path(td) / "findings"
        led.mkdir()
        fnd.mkdir()

        def put(slug, **kw):
            (led / f"{slug}.json").write_text(json.dumps(
                {"slug": slug, "path": f"content/docs/{slug}.md", **kw}))

        put("has-record", skipped_findings=3, pr_number=1)
        (fnd / "has-record.json").write_text("{}")
        put("recoverable", skipped_findings=3, pr_number=2)
        put("last-pr-only", skipped_findings=3, pr_number=0, last_pr_number=3)
        put("stranded", skipped_findings=3, pr_number=0)
        put("nothing-banked", skipped_findings=0, pr_number=4)
        put("clarity-only", skipped_findings=0, clarity_flag=True, pr_number=5)
        got = sorted(slug for _, slug, _ in candidates(led, fnd))
        check("a page that already has a record is left alone",
              "has-record" not in got)
        check("the 50 stranded pages are out of scope — no PR to read",
              "stranded" not in got)
        check("a page that banked nothing is not a candidate",
              "nothing-banked" not in got)
        check("clarity_flag alone still counts as banked debt",
              "clarity-only" in got)
        check("both PR pointers are honored",
              got == ["clarity-only", "last-pr-only", "recoverable"])

    tmpdir.cleanup()
    print(f"\n{passes} passed, {len(failures)} failed")
    return 1 if failures else 0


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--ledger-dir", default=".ledger-cache")
    p.add_argument("--findings-dir", default=".findings-cache",
                   help="existing findings/ records; entries that have one are skipped")
    p.add_argument("--out-dir", default="",
                   help="write synthesized records here")
    p.add_argument("--uri", default="",
                   help="s3://<bucket>/findings/ to upload to (skipped when empty)")
    p.add_argument("--pr-json", default=None,
                   help="inject the discovered PR set (testing); suppresses gh")
    p.add_argument("--limit", type=int, default=0, help="stop after N entries")
    p.add_argument("--dry-run", action="store_true",
                   help="print the records instead of writing or uploading")
    p.add_argument("--self-test", action="store_true", help="run built-in smoke checks")
    args = p.parse_args()
    if args.self_test:
        return self_test()
    if not args.dry_run and not args.out_dir and not args.uri:
        p.error("nothing to do: pass --dry-run, --out-dir, or --uri")
    return run(args)


if __name__ == "__main__":
    sys.exit(main())
