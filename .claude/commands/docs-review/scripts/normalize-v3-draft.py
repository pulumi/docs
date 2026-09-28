#!/usr/bin/env python3
"""Deterministic repair of the model-edited v3 cards, run before validation.

v3 has no splicer and no soft floor: a body that fails `validate-pinned.py`
is a hard `review:error` and nothing is published. The first weekend on
repo-wide traffic (2026-09-11 → 09-14) lost 2 of 25 reviews to slips that
are mechanical, not editorial:

* #21603 (and the #21552 sample): the model kept a ❓ row but deleted its
  `#### F<n> · Do this` block (`v3-detail-blocks` "block missing").
* #21585: the model added a ⚠️ row to an EMPTY brief section and hand-wrote
  the table with a four-column header `| | ID | Where | Finding |`
  (`v3-finding-grammar` on the header line). The validator's own hint still
  described the abandoned glyph column at the time.
* #21748 (2026-09-19): the model's one ⚠️ row ran off the end of a long
  Finding cell and never closed — three pipes, not four, so `_split_cells`
  read it as prose and the row failed `v3-finding-grammar`. An advisory nit
  on a PR with no blocking findings cost the entire review.

* #21722 (2026-09-18): the model kept the composed claim quote in the Finding
  cell and put its `**Spurious:**` verdict in a cell of its own — four cells.
* #21759 (2026-09-21): the model's added `F?` row cited `L47–52` with an en
  dash. The row grammar reads a hyphen, so the whole row failed
  `v3-finding-grammar`.
* #21782 (2026-09-21): the model added an `F?` row to a card composed as
  "nothing blocks merge" and rewrote the header to "1 item needs an answer".
  The count is build-evidence.py's to recompute, but it only recognizes the
  composed header shape, so `v3-blocking-count` refused the card first.

This script fixes exactly those shapes, in place, and nothing else. It is
idempotent, needs no model, and always exits 0 — a repair it cannot make
with certainty is left alone for the validator to refuse. Every repair is
logged as a `::warning::` (so the run shows what changed) and recorded in a
JSON summary (`--summary`) that rides in the post-edit-debug artifact.

Rules:

1. Finding tables (author 🚨/❓, brief ⚠️): a header whose non-empty cells
   are ID / Where / Finding, in any spacing and with any leading empty or
   glyph cell, becomes the composer's `| ID | Where | Finding |`; the
   separator under it becomes `|---|---|---|`; a data row that starts with an
   empty or glyph cell followed by `**F<n>**` / `**F?**` loses that cell.
   Rows already in the right shape are never touched.
2. Unclosed rows (author 🚨/❓, brief ⚠️): a line that opens with `|` but
   never closes gets its final `|` back — but only when the closed line is
   something the grammar recognizes (a finding row, the three-column header,
   a separator, or a row the leading-cell rule above can then fix). Anything
   else stays unclosed for the validator to refuse.
3. Line-range dashes (author 🚨/❓, brief ⚠️): a data row that fails the
   grammar only because its Where cell spells a range `L47–52` (en dash, em
   dash, or minus sign) gets the hyphen back. Only the Where cell is
   touched, and only when the row then parses.
4. Split Finding cell (author 🚨/❓, brief ⚠️): a four-cell data row whose
   first two cells are a valid ID and Where has its last two cells joined
   with ` — `, the separator the composer itself puts between a claim quote
   and its verdict. Only when the joined row parses.
5. Author header: a `## Author action guide v<N> — …` line whose tail is not
   one of the composer's two shapes is rewritten to the composed shape with
   the card's open 🚨+❓ row count. build-evidence.py recomputes the count
   after validation either way; this only restores a shape it can find.
6. Missing detail blocks (author card only): every numbered, un-dispositioned
   `| **F<n>** |` row under 🚨 / ❓ without a `#### F<n> · Do this` block gets
   one regenerated from the row itself (Line from the row's quoted span or
   the evidence base, Why from the finding cell, Fix as a bucket-appropriate
   single instruction), placed in row order among the section's blocks.

Usage:
  normalize-v3-draft.py --author-file .review-draft-author.md \
      --brief-file .review-draft-brief.md \
      [--evidence-base .review-evidence-base.json] [--summary out.json]
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules.setdefault(name, mod)
    spec.loader.exec_module(mod)
    return mod


cr = _load("nv_compose_review", HERE / "compose-review.py")
vp = _load("nv_validate_pinned", HERE / "validate-pinned.py")

AUTHOR_SECTIONS = ("🚨 Fix or disagree", "❓ Questions for you")
BRIEF_SECTIONS = ("⚠️ Check these before approving",)

# A leading cell that is empty or a status glyph — the abandoned first
# column. Anything else in that position is content and is left alone.
_GLYPH_CELL_RE = re.compile(r"^\s*(?:[⬜☐☑️✅✔️🛡️❌🔲🔳]|\[[ xX]\])?\s*$")
_ID_CELL_RE = re.compile(r"^\s*\*\*(F\d+|F\?)\*\*\s*$")
_HEADER_CELLS = ("id", "where", "finding")
_QUOTE_SPAN_RE = re.compile(r"\*[\"“](?P<q>.+?)[\"”]\*")
_LEADING_SEP_RE = re.compile(r"^\s*[—–-]\s*")

_RANGE_DASH_RE = re.compile(r"\bL(\d+)\s*[–—−]\s*(\d+)\b")
_AUTHOR_HEADER_LINE_RE = re.compile(r"^## Author action guide v(?P<rev>\d+) — ")

FIX_BY_BUCKET = {
    "❓ Questions for you": (
        "Reply with the source for the quoted line, or accept / refute it "
        "per **How to answer** below."
    ),
    "🚨 Fix or disagree": (
        "Correct the quoted line so it matches the finding above, then push."
    ),
}


class Repairs:
    def __init__(self) -> None:
        self.items: list[dict] = []

    def add(self, rule: str, doc: str, where: str, detail: str) -> None:
        self.items.append({"rule": rule, "doc": doc, "where": where, "detail": detail})
        print(f"::warning::normalize-v3-draft: {rule} <{doc} {where}> — {detail}")


# ---------------------------------------------------------------- tables --

def _split_cells(line: str) -> list[str] | None:
    """Cells of a `| a | b |` line, honoring `\\|` escapes. None when the
    line is not a table row."""
    s = line.strip()
    if not s.startswith("|") or not s.endswith("|") or len(s) < 2:
        return None
    inner = s[1:-1]
    cells: list[str] = []
    cur: list[str] = []
    i = 0
    while i < len(inner):
        ch = inner[i]
        if ch == "\\" and i + 1 < len(inner) and inner[i + 1] == "|":
            cur.append("\\|")
            i += 2
            continue
        if ch == "|":
            cells.append("".join(cur))
            cur = []
        else:
            cur.append(ch)
        i += 1
    cells.append("".join(cur))
    return cells


def _is_separator(line: str) -> bool:
    return bool(cr._TABLE_SEPARATOR_RE.match(line.strip()))


def _looks_like_header(cells: list[str]) -> bool:
    words = [c.strip().lower() for c in cells if c.strip()]
    return tuple(words) == _HEADER_CELLS


def _close_row(line: str) -> str | None:
    """A finding-table line that lost its closing `|`, closed — or None when
    appending one doesn't produce something the grammar recognizes.

    The Finding cell is written last and is by far the longest, so it is the
    one the model runs off the end of (#21748). Closing the line is only
    safe when the result parses, which leaves every other unclosed line —
    a genuinely truncated row, a prose line that happens to start with a
    pipe — to the validator.
    """
    s = line.rstrip()
    if not s.startswith("|") or len(s) < 2:
        return None
    if s.endswith("|") and not s.endswith("\\|"):
        return None                                  # already closed
    candidate = s + " |"
    if _is_separator(candidate):
        return cr.FINDING_TABLE_SEPARATOR
    cells = _split_cells(candidate)
    if cells is None:
        return None
    if _looks_like_header(cells) or cr.parse_finding_line(candidate) is not None:
        return candidate
    # Still carrying the abandoned leading status cell: closing the line is
    # what lets the row-leading-cell rule below see it at all.
    if len(cells) == 4 and _GLYPH_CELL_RE.match(cells[0]) and _ID_CELL_RE.match(cells[1]):
        return candidate
    return None


def _normalize_tables(lines: list[str], sections: tuple[str, ...], doc: str,
                      rep: Repairs) -> list[str]:
    body = "\n".join(lines)
    out = list(lines)
    for heading in sections:
        span = vp.find_section(body, heading)
        if span is None:
            continue
        start, end = span
        i = start + 1
        while i < end:
            line = out[i]
            if line.startswith("#### "):
                break  # the Style suggestions H4 ends the finding rows
            if not line.startswith("|"):
                i += 1
                continue
            cells = _split_cells(line)
            if cells is None:
                closed = _close_row(line)
                if closed is None:
                    i += 1
                    continue
                out[i] = line = closed
                cells = _split_cells(line)
                rep.add("row-unclosed", doc, f"line {i + 1}",
                        "closed a table row that was missing its final `|`")
            if _is_separator(line):
                i += 1
                continue
            if _looks_like_header(cells):
                if line.strip() != cr.FINDING_TABLE_HEADER:
                    out[i] = cr.FINDING_TABLE_HEADER
                    rep.add("table-header", doc, f"line {i + 1}",
                            "rewrote a hand-built header to the composer's three-column shape")
                if i + 1 < end and _is_separator(out[i + 1]) \
                        and out[i + 1].strip() != cr.FINDING_TABLE_SEPARATOR:
                    ncols = len(_split_cells(out[i + 1]) or [])
                    if ncols != 3:
                        out[i + 1] = cr.FINDING_TABLE_SEPARATOR
                        rep.add("table-separator", doc, f"line {i + 2}",
                                f"rewrote a {ncols}-column separator to three columns")
                i += 1
                continue
            # Data row with an abandoned leading status cell.
            if len(cells) == 4 and _GLYPH_CELL_RE.match(cells[0]) \
                    and _ID_CELL_RE.match(cells[1]):
                new = "| " + " | ".join(c.strip() for c in cells[1:]) + " |"
                if cr.parse_finding_line(new) is not None:
                    out[i] = new
                    rep.add("row-leading-cell", doc, f"line {i + 1}",
                            "dropped the leading status cell from a finding row")
            # Finding cell split in two by a stray pipe (quote | verdict).
            cells = _split_cells(out[i])
            if cells is not None and len(cells) == 4 and _ID_CELL_RE.match(cells[0]) \
                    and cells[2].strip() and cells[3].strip():
                new = "| " + " | ".join(
                    [cells[0].strip(), cells[1].strip(),
                     cells[2].strip() + " — " + cells[3].strip()]) + " |"
                if cr.parse_finding_line(new) is not None:
                    out[i] = new
                    rep.add("finding-cell-split", doc, f"line {i + 1}",
                            "joined a Finding cell the model split in two with a stray `|`")
            # Where cell spelling a line range with a typographic dash.
            cells = _split_cells(out[i])
            if cells is not None and len(cells) == 3 and _ID_CELL_RE.match(cells[0]) \
                    and cr.parse_finding_line(out[i]) is None \
                    and _RANGE_DASH_RE.search(cells[1]):
                cells[1] = _RANGE_DASH_RE.sub(r"L\1-\2", cells[1])
                new = "|" + "|".join(cells) + "|"
                if cr.parse_finding_line(new) is not None:
                    out[i] = new
                    rep.add("range-dash", doc, f"line {i + 1}",
                            "rewrote a typographic dash in the row's line range to a hyphen")
            i += 1
    return out


# ---------------------------------------------------------------- header --

def _normalize_header(lines: list[str], rep: Repairs) -> list[str]:
    """Restore the composed header shape when the model reworded its tail.
    The count written here is the card's own open-row count — one of the
    counts `v3-blocking-count` accepts — and build-evidence.py recomputes it
    from the final findings before publish."""
    body = "\n".join(lines)
    if vp.V3_AUTHOR_HEADER_RE.search(body):
        return lines
    out = list(lines)
    for i, line in enumerate(out):
        m = _AUTHOR_HEADER_LINE_RE.match(line)
        if not m:
            continue
        n = 0
        for heading in AUTHOR_SECTIONS:
            for _, _, parsed in vp.v3_finding_rows(body, heading):
                if parsed is None or not vp._V3_REWRITTEN_RE.match(parsed["body"]):
                    n += 1
        if n:
            tail = f"{n} item blocks merge" if n == 1 else f"{n} items block merge"
        else:
            tail = "nothing blocks merge"
        out[i] = f"## Author action guide v{m.group('rev')} — {tail}"
        rep.add("author-header", "author", f"line {i + 1}",
                f"restored the composed header shape (was: {line.strip()[:80]!r})")
        break
    return out


# --------------------------------------------------------- detail blocks --

def _block_spans(lines: list[str], start: int, end: int) -> list[tuple[str, int, int]]:
    """(id, first line, exclusive end) of every `#### F<n> · Do this` block
    between start and end, fence-aware; the end excludes trailing blanks."""
    spans: list[tuple[str, int, int]] = []
    cur_id, cur_start = None, -1
    fenced = False

    def close(upto: int) -> None:
        nonlocal cur_id, cur_start
        if cur_id is None:
            return
        e = upto
        while e > cur_start + 1 and not lines[e - 1].strip():
            e -= 1
        spans.append((cur_id, cur_start, e))
        cur_id, cur_start = None, -1

    for i in range(start, end):
        line = lines[i]
        if line.lstrip().startswith("```"):
            fenced = not fenced
            continue
        if fenced:
            continue
        m = vp._V3_DETAIL_HEADING_RE.match(line)
        if m:
            close(i)
            cur_id, cur_start = m.group(1), i
            continue
        if cur_id is not None and (line.startswith("### ") or line.startswith("#### ")
                                   or line.startswith("<!-- REVIEW_STATE")
                                   or line.startswith("<sub>") or line.startswith(cr.EVIDENCE_LINE_PREFIXES)
                                   or line.startswith(cr.V3_BROWSER_HINT_PREFIX)):
            close(i)
    close(end)
    return spans


def _quote_from_row(body: str) -> str | None:
    m = _QUOTE_SPAN_RE.search(body)
    if m and m.group("q").strip():
        return m.group("q").strip()
    return None


def _why_from_row(body: str) -> str:
    rest = _QUOTE_SPAN_RE.sub("", body, count=1).strip()
    rest = _LEADING_SEP_RE.sub("", rest).strip()
    return rest or body.strip()


def _render_block(fid: str, heading: str, parsed: dict, evidence: dict | None) -> list[str]:
    # The evidence record's claim text first: an author-card cell carries
    # only a short excerpt (compose-review.AUTHOR_CELL_TRUNC), and this
    # bullet promises the line verbatim.
    quote = str((evidence or {}).get("text") or "").strip() or None
    if quote is None:
        quote = _quote_from_row(parsed["body"])
    if quote is None:
        where = f"`{parsed['file']}`" if parsed.get("file") else "the flagged line"
        if parsed.get("ref"):
            where += f" {parsed['ref']}"
        quote = f"(see {where} — the finding below names the line)"
    why = _why_from_row(parsed["body"])
    fix = FIX_BY_BUCKET.get(heading, FIX_BY_BUCKET["🚨 Fix or disagree"])
    return [
        f"#### {fid} · Do this",
        "",
        f"- **Line (verbatim):** {quote}",
        f"- **Why:** {why}",
        f"- **Fix:** {fix}",
    ]


def _restore_blocks(lines: list[str], evidence_by_id: dict[str, dict],
                    rep: Repairs) -> list[str]:
    body = "\n".join(lines)
    existing_ids = {bid for bid, _ in vp._v3_detail_blocks(body)}
    out = list(lines)
    # Walk sections bottom-up so earlier insertions don't shift later spans.
    for heading in reversed(AUTHOR_SECTIONS):
        span = vp.find_section("\n".join(out), heading)
        if span is None:
            continue
        start, end = span
        rows: list[tuple[int, str, dict]] = []
        for lineno, raw, parsed in vp.v3_finding_rows("\n".join(out), heading):
            if parsed is None or parsed["id"] == "F?":
                continue
            if vp._V3_REWRITTEN_RE.match(parsed["body"]):
                continue  # dispositioned: build-evidence drops it, no block wanted
            rows.append((lineno - 1, parsed["id"], parsed))
        missing = [(idx, fid, p) for idx, fid, p in rows if fid not in existing_ids]
        if not missing:
            continue
        order = [fid for _, fid, _ in rows]
        # Insert in reverse row order so each insertion point stays valid.
        for idx, fid, parsed in reversed(missing):
            spans = _block_spans(out, start, end)
            by_id = {bid: (s, e) for bid, s, e in spans}
            later = [order[k] for k in range(order.index(fid) + 1, len(order)) if order[k] in by_id]
            block = _render_block(fid, heading, parsed, evidence_by_id.get(fid))
            if later:
                pos = by_id[later[0]][0]
                out[pos:pos] = [*block, ""]
            elif spans:
                pos = max(e for _, _, e in spans)
                out[pos:pos] = ["", *block]
            else:
                # Right after the table's last row.
                last = idx
                while last + 1 < end and out[last + 1].startswith("|"):
                    last += 1
                out[last + 1:last + 1] = ["", *block]
            existing_ids.add(fid)
            rep.add("detail-block", "author", fid,
                    "regenerated the missing `#### … · Do this` block from the row")
            body = "\n".join(out)
            span = vp.find_section(body, heading)
            start, end = span if span else (start, end)
    return out


# ---------------------------------------------------------------- driver --

def normalize(author: str, brief: str | None, evidence_base: dict | None,
              rep: Repairs) -> tuple[str, str | None]:
    a_lines = author.splitlines()
    a_lines = _normalize_tables(a_lines, AUTHOR_SECTIONS, "author", rep)
    a_lines = _normalize_header(a_lines, rep)
    evidence_by_id: dict[str, dict] = {}
    for f in (evidence_base or {}).get("findings", []) or []:
        if isinstance(f, dict) and f.get("id"):
            evidence_by_id[str(f["id"])] = f
    a_lines = _restore_blocks(a_lines, evidence_by_id, rep)
    new_author = "\n".join(a_lines) + ("\n" if author.endswith("\n") else "")
    new_brief = brief
    if brief is not None:
        b_lines = _normalize_tables(brief.splitlines(), BRIEF_SECTIONS, "brief", rep)
        new_brief = "\n".join(b_lines) + ("\n" if brief.endswith("\n") else "")
    return new_author, new_brief


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--author-file", required=True, type=Path)
    ap.add_argument("--brief-file", type=Path)
    ap.add_argument("--evidence-base", type=Path)
    ap.add_argument("--summary", type=Path, help="write a JSON list of repairs here")
    args = ap.parse_args(argv)

    rep = Repairs()
    try:
        author = args.author_file.read_text(encoding="utf-8")
        brief = args.brief_file.read_text(encoding="utf-8") \
            if args.brief_file and args.brief_file.is_file() else None
        evidence_base = None
        if args.evidence_base and args.evidence_base.is_file():
            try:
                evidence_base = json.loads(args.evidence_base.read_text(encoding="utf-8"))
            except (OSError, ValueError):
                evidence_base = None
        new_author, new_brief = normalize(author, brief, evidence_base, rep)
        if new_author != author:
            args.author_file.write_text(new_author, encoding="utf-8")
        if brief is not None and new_brief != brief:
            args.brief_file.write_text(new_brief, encoding="utf-8")
    except Exception as exc:  # noqa: BLE001 — never turn a repair into a failure
        print(f"::warning::normalize-v3-draft: skipped ({type(exc).__name__}: {exc})")
        rep.items.append({"rule": "error", "doc": "-", "where": "-", "detail": str(exc)})
    if args.summary:
        try:
            args.summary.write_text(json.dumps({"repairs": rep.items}, indent=2) + "\n",
                                    encoding="utf-8")
        except OSError as exc:
            print(f"::warning::normalize-v3-draft: could not write summary: {exc}")
    print(f"normalize-v3-draft: {len(rep.items)} repair(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
