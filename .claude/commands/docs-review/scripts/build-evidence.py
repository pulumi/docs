#!/usr/bin/env python3
"""build-evidence.py — turn the model-edited v3 drafts back into evidence.

Runs after the model edits `.review-draft-author.md` / `.review-draft-brief.md`
(surface v3) and before the credentialed publish job records anything. It is
the fail-closed half of the round-trip contract: the composer renders finding
table rows with `render_finding_line`, the model edits the cells in place, and
this script parses them back with the same grammar (`parse_finding_line`) — a row
that stopped parsing is a contract violation and exits 2, never a silent drop.

What it emits:
  --output       the final `.review-evidence.json` — findings re-read from the
                 drafts (text as the model left it, buckets by section, model
                 promotions honored, `F?` additions numbered), everything else
                 carried from the composer's `.review-evidence-base.json`,
                 summary/confidence/history refreshed from the brief.
  --author-out / --brief-out
                 cleaned publish bodies: `**Spurious:**` / `**Mis-sourced:**`
                 rewrites are filed into evidence `triaged` and dropped from
                 the cards, `**Pre-existing:**` rewrites move to the evidence
                 `preexisting` bucket (the brief's 💡 count line is updated),
                 `F?` ids become real ids, and the author header's blocking
                 count is recomputed.

Bucket monotonicity is enforced here: a base finding may move up
(reviewer-check → author-answer → outstanding) but never down; a vanished
finding (in the base, in no draft, not rewritten as Spurious/Mis-sourced/
Pre-existing) exits 2 — the model must disposition findings, not delete them.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
_REVIEW_V3_DIR = HERE.parents[3] / "scripts" / "review-v3"


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules.setdefault(name, mod)
    spec.loader.exec_module(mod)
    return mod


cr = _load("compose_review", HERE / "compose-review.py")
review_state = _load("review_state", _REVIEW_V3_DIR / "review_state.py")

# Section heading → bucket. The author card's two blocking sections and the
# brief's reviewer section are the only places finding bullets may live.
AUTHOR_SECTIONS = {
    "### 🚨 Fix or disagree": "outstanding",
    "### ❓ Questions for you": "author-answer",
}
BRIEF_SECTIONS = {
    "### ⚠️ Check these before approving": "reviewer-check",
}
# Rank for the never-demote check.
_BUCKET_RANK = {"reviewer-check": 0, "author-answer": 1, "outstanding": 2, "preexisting": 0}

# Lines that end a finding section or a `#### F<n> · Do this` block. Shared by
# every walker here and in apply-update.py so nothing composer-owned that sits
# between the last table and the REVIEW_STATE block (the browser hint, the 📎
# evidence line, the <sub> stamp, the marker comments) can be swallowed into a
# section span and dropped on re-render — which is exactly what took the 📎
# line off the author card on the first live #update-review (2026-09-01).
_SECTION_TERMINATORS = (
    "### ", "#### ", "<!-- REVIEW_STATE", "<!-- AUTHOR_STATE", "<!-- CLAUDE_REVIEW",
    "<sub>", "📎 ",
)


def is_section_terminator(line: str) -> bool:
    return line.startswith(_SECTION_TERMINATORS) or line.startswith(cr.V3_BROWSER_HINT_PREFIX)

# Anchored at the start of the parsed body: the contract is "REWRITE the
# bullet body as `**Spurious:** …`", and the composer's own TODO instructions
# quote these labels mid-string — a floating search would file every unedited
# stub as triaged (caught by test_build_evidence_on_fixtures).
_SPURIOUS_RE = re.compile(r"^(?:\*[\"']?.{0,160}?[\"']?\*\s+—\s+)?\*\*(Spurious|Mis-sourced):\*\*\s*(?P<note>.*)$")
_PREEXISTING_RE = re.compile(r"^(?:\*[\"']?.{0,160}?[\"']?\*\s+—\s+)?\*\*Pre-existing:\*\*\s*(?P<note>.*)$")
_PREEXISTING_COUNT_RE = re.compile(r"(💡 \*\*Pre-existing issues in touched files:\*\* )\d+")
_HEADER_RE = re.compile(r"^## Author action guide v(?P<rev>\d+) — (?:\d+ items? blocks? merge|nothing blocks merge)\s*$")
_SUMMARY_RE = re.compile(r"^> \*\*Summary:\*\*\s*(?P<text>.+)$")
_DETAIL_HEADING_RE = re.compile(r"^#### (?P<id>F\d+|F\?) · Do this\s*$")


def collect_detail_blocks(body: str) -> tuple[dict[str, tuple[int, int]], dict[str, str]]:
    """(id → (start_line, end_line)) spans and (id → text) for every
    `#### F<n> · Do this` block. Fence-aware: a ``` fence suspends the
    heading scan so replacement text inside a Fix block can't terminate or
    start a span. An `F?` block is a ContractViolation (model-added rows get
    no block — ids aren't assigned yet)."""
    lines = body.splitlines()
    spans: dict[str, tuple[int, int]] = {}
    texts: dict[str, str] = {}
    cur: str | None = None
    start = 0
    fenced = False

    def close(end: int) -> None:
        nonlocal cur
        if cur is not None:
            spans[cur] = (start, end)
            texts[cur] = "\n".join(lines[start + 1:end]).strip()
            cur = None

    for i, line in enumerate(lines):
        if line.lstrip().startswith("```"):
            fenced = not fenced
            continue
        if fenced:
            continue
        m = _DETAIL_HEADING_RE.match(line)
        if m:
            close(i)
            if m.group("id") == "F?":
                raise ContractViolation(
                    "author: a `#### F? · Do this` block — model-added F? rows get no "
                    "detail block; keep their cell terse (ids are assigned by build-evidence)")
            if m.group("id") in spans:
                raise ContractViolation(f"author: duplicate detail block for {m.group('id')}")
            cur = m.group("id")
            start = i
            continue
        if cur is not None and is_section_terminator(line):
            close(i)
    close(len(lines))
    return spans, texts
_CONF_ROW_RE = re.compile(r"^> \| (?P<dim>[^|]+) \| (?P<level>[^|]+) \|")


class ContractViolation(Exception):
    pass


def _sections(body: str, headings: dict[str, str]) -> list[tuple[str, int, int]]:
    """(bucket, start_line, end_line) spans for each known section."""
    lines = body.splitlines()
    spans = []
    current = None
    for i, line in enumerate(lines):
        matched = next((b for h, b in headings.items() if line.startswith(h)), None)
        if matched is not None:
            if current:
                spans.append((current[0], current[1], i))
            current = (matched, i + 1)
        elif is_section_terminator(line):
            if current:
                spans.append((current[0], current[1], i))
                current = None
    if current:
        spans.append((current[0], current[1], len(lines)))
    return spans


def _walk(body: str, headings: dict[str, str], where: str):
    """Yield (bucket, line_index, parsed_or_None, raw_line) for candidate lines."""
    lines = body.splitlines()
    for bucket, start, end in _sections(body, headings):
        for i in range(start, end):
            raw = lines[i]
            if raw.startswith("|"):
                if cr.is_table_furniture(raw):
                    continue
                parsed = cr.parse_finding_line(raw)
                if parsed is None:
                    raise ContractViolation(
                        f"{where}: unparseable finding row in {bucket} section: {raw!r}"
                    )
                yield bucket, i, parsed, raw
            elif raw.startswith("- "):
                # Bullets can never be finding rows any more. The ⚠️ section
                # may carry plain advisory prose bullets the model leaves
                # for the reviewer — untracked by design (no id, no
                # REVIEW_STATE entry, not a finding); they stay in the
                # published brief verbatim. A bullet that LOOKS like a
                # finding (F-id or checkbox) is a grammar break anywhere,
                # and blocking sections tolerate no prose bullets at all.
                # Mirrors validate-pinned's v3-finding-grammar rule exactly.
                looks_like_finding = bool(
                    re.match(r"^\s*-\s*(\[[ x]\]|\*\*F[\d?]+\*\*)", raw)
                )
                if bucket == "reviewer-check" and not looks_like_finding:
                    continue
                raise ContractViolation(
                    f"{where}: unparseable finding line in {bucket} section: {raw!r}"
                )


def build(author_body: str, brief_body: str, base: dict) -> tuple[dict, str, str]:
    high_water = int(base.get("high_water", 0))
    base_findings = {f["id"]: f for f in base.get("findings", [])}

    findings: list[dict] = []
    triaged: list[dict] = list(base.get("triaged", []))
    drop_lines: dict[str, set[int]] = {"author": set(), "brief": set()}
    renumber: dict[str, dict[int, str]] = {"author": {}, "brief": {}}
    seen_ids: set[str] = set()

    for doc_name, body, headings in (
        ("author", author_body, AUTHOR_SECTIONS),
        ("brief", brief_body, BRIEF_SECTIONS),
    ):
        for bucket, idx, parsed, raw in _walk(body, headings, doc_name):
            fid = parsed["id"]
            if fid == "F?":
                high_water += 1
                fid = f"F{high_water}"
                renumber[doc_name][idx] = fid
            if fid in seen_ids:
                raise ContractViolation(f"{doc_name}: finding {fid} appears twice across the drafts")
            seen_ids.add(fid)
            prior = base_findings.get(fid)
            if prior and _BUCKET_RANK[bucket] < _BUCKET_RANK.get(prior["bucket"], 0):
                raise ContractViolation(
                    f"{doc_name}: {fid} demoted from {prior['bucket']} to {bucket} — promote-only"
                )
            body_text = parsed["body"]
            m = _SPURIOUS_RE.search(body_text)
            if m:
                triaged.append({
                    "id": fid,
                    "kind": m.group(1).lower(),
                    "file": parsed["file"] or (prior or {}).get("file") or "(unknown)",
                    "note": m.group("note").strip() or body_text,
                    "from_bucket": (prior or {}).get("bucket") or bucket,
                })
                drop_lines[doc_name].add(idx)
                continue
            record = {
                "id": fid,
                "bucket": bucket,
                "file": parsed["file"] or (prior or {}).get("file") or "(unknown)",
                "text": body_text or (prior or {}).get("text") or raw,
                "origin": (prior or {}).get("origin") or "model",
                "status": (prior or {}).get("status") or "open",
                "disposition": (prior or {}).get("disposition"),
            }
            pm = _PREEXISTING_RE.search(body_text)
            if pm:
                record["bucket"] = "preexisting"
                record["text"] = pm.group("note").strip() or body_text
                drop_lines[doc_name].add(idx)
            lines_nums = cr._lines_from_ref(parsed["ref"])
            if lines_nums:
                record["lines"] = lines_nums
            elif prior and prior.get("lines"):
                record["lines"] = prior["lines"]
            findings.append(record)

    vanished = [
        fid for fid in base_findings
        if fid not in seen_ids and base_findings[fid].get("bucket") != "preexisting"
    ]
    if vanished:
        raise ContractViolation(
            f"finding(s) {', '.join(sorted(vanished))} in the evidence base but in neither draft "
            "and not rewritten as **Spurious:** / **Mis-sourced:** / **Pre-existing:** — "
            "findings are dispositioned, never deleted"
        )

    # Detail blocks: every block pairs with an open blocking row on the
    # author card; blocks of dropped (Spurious/Pre-existing) rows are dropped
    # with them; surviving blocks are mirrored onto the finding record for
    # the evidence page.
    block_spans, block_texts = collect_detail_blocks(author_body)
    open_author_ids = {f["id"] for f in findings
                       if f["bucket"] in ("outstanding", "author-answer")}
    renumbered_ids = set(renumber["author"].values())
    for bid, span in block_spans.items():
        if bid in open_author_ids or bid in renumbered_ids:
            continue
        dropped_here = any(f.get("id") == bid for f in triaged) or any(
            f["id"] == bid and f["bucket"] == "preexisting" for f in findings)
        if dropped_here:
            drop_lines["author"].update(range(span[0], span[1]))
        else:
            raise ContractViolation(
                f"author: detail block for {bid} has no open 🚨/❓ row — a "
                "block never outlives its finding (resolve/disposition the row "
                "and delete its block together)")
    for f in findings:
        if f["id"] in block_texts and f["bucket"] in ("outstanding", "author-answer"):
            f["detail"] = block_texts[f["id"]]

    # REVIEW_STATE must have survived the model edit intact; its dispositions
    # win over anything carried from the base.
    state = review_state.parse_state(author_body)
    if state is None:
        raise ContractViolation("author draft lost its REVIEW_STATE block")
    for fid, entry in state.get("findings", {}).items():
        for f in findings:
            if f["id"] == fid:
                f["disposition"] = entry

    # Summary + confidence from the brief (the model fills the TIP block there).
    summary = None
    confidence = dict(base.get("confidence") or {})
    for line in brief_body.splitlines():
        sm = _SUMMARY_RE.match(line)
        if sm and "<TODO" not in sm.group("text"):
            summary = sm.group("text").strip()
        cm = _CONF_ROW_RE.match(line)
        if cm:
            dim = cm.group("dim").strip()
            level = cm.group("level").strip()
            if dim != "Dimension" and not level.startswith(":") and "<TODO" not in level:
                confidence[dim] = level

    evidence = dict(base)
    evidence["findings"] = findings
    evidence["triaged"] = triaged
    evidence["high_water"] = max(high_water, state.get("high_water", 0))
    evidence["confidence"] = confidence
    evidence["summary"] = summary if summary else base.get("summary")
    history = list(base.get("history") or [])
    if history and summary:
        history[-1] = dict(history[-1], summary=cr.trunc(summary, 160))
    evidence["history"] = history

    author_out = _collapse_empty_tables(
        _clean(author_body, drop_lines["author"], renumber["author"]), AUTHOR_SECTIONS)
    brief_out = _collapse_empty_tables(
        _clean(brief_body, drop_lines["brief"], renumber["brief"]), BRIEF_SECTIONS)
    brief_out = refresh_facts_line(brief_out, findings)
    # A model-added `F?` row got a real id above; the author card's
    # REVIEW_STATE high-water mark must move with it, or every later reader
    # (validate-pinned's grammar rule, /resolve's range check) rejects the id
    # (fork PR 245, 2026-09-01: brief carried F1 against high_water 0).
    if evidence["high_water"] != state.get("high_water", 0):
        author_out = review_state.replace_block(
            author_out, dict(state, high_water=evidence["high_water"]))
    n_blocking = sum(1 for f in findings if f["bucket"] in ("outstanding", "author-answer"))
    author_out = _fix_header(author_out, n_blocking)
    n_pre = sum(1 for f in findings if f["bucket"] == "preexisting")
    brief_out = _PREEXISTING_COUNT_RE.sub(lambda m: m.group(1) + str(n_pre), brief_out)
    # The Waiting-on-the-author block is composer-owned: regenerate it from
    # the FINAL findings + dispositions so model edits (promotions included)
    # can never leave it stale.
    brief_out = cr.replace_waiting_block(
        brief_out, findings, state.get("findings", {}))
    return evidence, author_out, brief_out


_FACTS_RE = re.compile(r"^- \*\*Facts:\*\* (?P<n>\d+) factual claims? checked(?: — (?P<rest>.*?))?\.$", re.M)


def _is_claim_finding(f: dict) -> bool:
    origin = str(f.get("origin") or "")
    if origin.startswith("verdict:"):
        return True
    # Degraded refresh (no prior evidence): origin is unknown, but a verdict
    # row always opens with the italic claim quote the composer renders.
    return origin == "model" and str(f.get("text") or "").lstrip().startswith(("*\"", "*“", "*'"))


def refresh_facts_line(brief_body: str, findings: list[dict]) -> str:
    """Re-derive the brief's rubber-stamp **Facts** bullet from the refreshed
    evidence findings. The totals (claims checked, verified clean) are fixed
    at compose time and kept; what moves is how many claim findings are still
    open on the author's card vs. parked in the ⚠️ list vs. settled (resolved,
    conceded, or filed as spurious/pre-existing). Both lanes drift without
    it: the first live refresh still said "2 open" with one left, and a fresh
    v1 said "3 open" after the model filed two rows as spurious."""
    m = _FACTS_RE.search(brief_body)
    if not m:
        return brief_body
    checked = int(m.group("n"))
    rest = m.group("rest") or ""
    mx = re.search(r"(\d+) verified clean", rest)
    x = int(mx.group(1)) if mx else 0
    claims = [f for f in findings if _is_claim_finding(f)]
    author_open = sum(1 for f in claims
                      if f.get("bucket") in ("outstanding", "author-answer")
                      and f.get("status") == "open" and not f.get("disposition"))
    flagged = sum(1 for f in claims if f.get("bucket") == "reviewer-check")
    settled = max(checked - x - author_open - flagged, 0)
    parts: list[str] = []
    if x:
        parts.append(f"{x} verified clean")
    if author_open:
        parts.append(f'{author_open} open on the author\'s card ("Waiting on the author" above)')
    if flagged:
        parts.append(f"{flagged} flagged in the ⚠️ list")
    if settled:
        parts.append(f"{settled} settled — see the evidence page")
    noun = "factual claim" if checked == 1 else "factual claims"
    line = f"- **Facts:** {checked} {noun} checked"
    if parts:
        line += " — " + ", ".join(parts)
    return brief_body[:m.start()] + line + "." + brief_body[m.end():]



_EMPTY_SENTINEL = {
    "outstanding": cr._V3_EMPTY_OUTSTANDING,
    "author-answer": cr._V3_EMPTY_QUESTIONS,
    "reviewer-check": cr._V3_EMPTY_CHECKS,
}


def _collapse_empty_tables(body: str, headings: dict[str, str]) -> str:
    """A section whose every row was filed off the card keeps only its table
    furniture after _clean(); render the composer's empty sentinel instead
    (fresh v1 on fork PR 242 showed a header-only 🚨 table)."""
    lines = body.splitlines()
    edits: list[tuple[int, int, list[str]]] = []
    for bucket, start, end in _sections(body, headings):
        content = [ln for ln in lines[start:end] if ln.strip()]
        if content and all(ln.startswith("|") and cr.is_table_furniture(ln) for ln in content):
            sentinel = _EMPTY_SENTINEL.get(bucket, "")
            if bucket == "reviewer-check":
                # The span ends AT the stances H4 when one follows; the
                # sentinel must not claim nothing needs a human eye then.
                sentinel = cr.empty_checks_sentinel(end < len(lines) and lines[end].startswith(cr.STANCES_HEADING))
            edits.append((start, end, ["", sentinel, ""]))
    for start, end, new in sorted(edits, reverse=True):
        lines[start:end] = new
    return "\n".join(lines) + ("\n" if body.endswith("\n") else "")


def _clean(body: str, drop: set[int], renumber: dict[int, str]) -> str:
    lines = body.splitlines()
    out: list[str] = []
    for i, line in enumerate(lines):
        if i in drop:
            # also swallow the blank spacer that follows a dropped bullet
            if out and out[-1] == "" and i + 1 < len(lines) and lines[i + 1] == "":
                continue
            continue
        if i in renumber:
            line = line.replace("**F?**", f"**{renumber[i]}**", 1)
        out.append(line)
    return "\n".join(out) + ("\n" if body.endswith("\n") else "")


def open_author_findings(author_body: str) -> list[dict]:
    """The author card's 🚨/❓ rows as {id, bucket, text} — the shape
    render_waiting_block() and count_blocking() take."""
    return [{"id": parsed["id"], "bucket": bucket, "text": parsed["body"]}
            for bucket, _i, parsed, _raw in _walk(author_body, AUTHOR_SECTIONS, "author")]


def count_blocking(findings: list[dict], state_findings: dict) -> int:
    """Rows that still hold the merge: on the author card AND without a
    REVIEW_STATE disposition. Mirrors validate-pinned's v3 count-buckets, so
    the header, the Waiting table, and the label can't disagree."""
    return sum(1 for f in findings
               if f.get("bucket") in ("outstanding", "author-answer")
               and not isinstance(state_findings.get(f["id"]), dict))


def refresh_counts(author_body: str, brief_body: str | None, state: dict | None) -> tuple[str, str | None]:
    """Recompute everything that depends on dispositions after REVIEW_STATE
    changes: the author header's blocking count and the brief's "Waiting on
    the author" block. Shared by apply-update.py (update lane) and
    resolve-handler.py (/resolve lane) — before this, a `/resolve F1
    accepted` left both saying "1 item blocks merge" (2026-09-01 smoke)."""
    findings = open_author_findings(author_body)
    sf = (state or {}).get("findings", {}) or {}
    author_body = _fix_header(author_body, count_blocking(findings, sf))
    if brief_body is not None:
        brief_body = cr.replace_waiting_block(brief_body, findings, sf)
        # The Facts bullet moves too (an accepted ❓ is no longer "open").
        # No evidence object here (the /resolve lane is uncredentialed), so
        # rows stand in: origin "model" + the claim-quote heuristic.
        rows = [dict(f, origin="model", status="open", disposition=sf.get(f["id"])) for f in findings]
        rows += [{"id": p["id"], "bucket": b, "text": p["body"], "origin": "model", "status": "open",
                  "disposition": sf.get(p["id"])}
                 for b, _i, p, _r in _walk(brief_body, BRIEF_SECTIONS, "brief")]
        brief_body = refresh_facts_line(brief_body, rows)
    return author_body, brief_body


def _fix_header(body: str, n_blocking: int, rev: int | None = None) -> str:
    """Recompute the header's blocking count; `rev` bumps the display
    revision (the update lane passes it — initial-lane fixes keep v1)."""
    lines = body.splitlines()
    for i, line in enumerate(lines):
        m = _HEADER_RE.match(line)
        if m:
            if n_blocking:
                noun = "item blocks" if n_blocking == 1 else "items block"
                verb = f"{n_blocking} {noun} merge"
            else:
                verb = "nothing blocks merge"
            out_rev = rev if rev is not None else int(m.group("rev"))
            lines[i] = f"## Author action guide v{out_rev} — {verb}"
            # The orienting callout directly under the header follows the
            # count: swap IMPORTANT ⇄ NOTE when it crosses zero.
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines) and lines[j].startswith("> [!"):
                k = j
                while k < len(lines) and lines[k].startswith(">"):
                    k += 1
                lines[j:k] = cr.render_author_orient(n_blocking)
            break
    return "\n".join(lines) + ("\n" if body.endswith("\n") else "")


def _self_test() -> int:
    ts = "2026-08-31T18:00:00Z"
    base = {
        "schema_version": 1, "repo": "pulumi/docs", "pr": 1, "head_sha": "a" * 40,
        "run_id": "t", "generated_at": ts, "high_water": 3,
        "findings": [
            {"id": "F1", "bucket": "outstanding", "file": "a.md", "text": "t1", "origin": "verdict:contradicted", "status": "open", "disposition": None, "lines": [8]},
            {"id": "F2", "bucket": "author-answer", "file": "a.md", "text": "t2", "origin": "verdict:unverifiable", "status": "open", "disposition": None},
            {"id": "F3", "bucket": "reviewer-check", "file": "a.md", "text": "t3", "origin": "verdict:framing-drift", "status": "open", "disposition": None},
        ],
        "trail": [], "investigation_log": {}, "triaged": [], "history": [{"ts": ts, "summary": "initial", "sha": "aaaa"}],
        "confidence": {"facts": "TODO"}, "summary": None,
    }
    state_block = review_state.serialize_block(dict(review_state.empty_state(), high_water=3))
    author = "\n".join([
        "<!-- CLAUDE_REVIEW 1/1 -->", "<!-- CLAUDE_REVIEW_AUTHOR -->",
        "## Author action guide v1 — 2 items block merge", "",
        "### 🚨 Fix or disagree", "",
        "| ID | Where | Finding |", "|---|---|---|",
        "| **F1** | `a.md` L8 | the model's edited fix prose |",
        "| **F2** | `a.md` L9 | promoted question now a blocker |",
        "| **F?** | `a.md` | a brand new model finding |", "",
        "### ❓ Questions for you", "",
        "_No open questions for you._", "",
        "📎 **Full evidence:** %%EVIDENCE_URL%%", "", state_block, "",
    ]) + "\n"
    brief = "\n".join([
        "<!-- CLAUDE_REVIEW_BRIEF -->", "## Reviewer's guide v1 — not for the author", "",
        "> **Summary:** A tidy little PR about a.md.", "",
        "> | Dimension | Level | Notes |", "> | :--- | :---: | :--- |", "> | facts | HIGH |  |", "",
        "### ⚠️ Check these before approving", "",
        "| ID | Where | Finding |", "|---|---|---|",
        "| **F3** | `a.md` L12 | **Spurious:** the comparison was against stale data |", "",
        "💡 **Pre-existing issues in touched files:** 0 — x", "",
        "📎 **Full evidence:** %%EVIDENCE_URL%%", "",
    ]) + "\n"

    ev, author_out, brief_out = build(author, brief, base)
    ids = {f["id"]: f for f in ev["findings"]}
    assert set(ids) == {"F1", "F2", "F4"}, ids.keys()
    assert ids["F2"]["bucket"] == "outstanding", "promotion honored"
    assert ids["F4"]["origin"] == "model" and ids["F4"]["bucket"] == "outstanding"
    assert ev["high_water"] == 4
    assert any(t["id"] == "F3" and t["kind"] == "spurious" for t in ev["triaged"])
    assert "**F4**" in author_out and "F?" not in author_out
    assert "F3" not in brief_out.split("💡")[0].split("⚠️")[1], "spurious bullet dropped from brief"
    assert ev["summary"] == "A tidy little PR about a.md."
    assert ev["confidence"]["facts"] == "HIGH"
    assert ev["history"][-1]["summary"] == "A tidy little PR about a.md."
    assert "## Author action guide v1 — 3 items block merge" in author_out

    # demotion: F1 rendered in the brief's ⚠️ → violation
    demoted_brief = brief.replace(
        "| **F3** | `a.md` L12 | **Spurious:** the comparison was against stale data |",
        "| **F1** | `a.md` L8 | softened down |\n| **F3** | `a.md` L12 | **Spurious:** stale data |",
    )
    demoted_author = author.replace("| **F1** | `a.md` L8 | the model's edited fix prose |\n", "")
    try:
        build(demoted_author, demoted_brief, base)
    except ContractViolation as e:
        assert "demoted" in str(e), e
    else:
        raise AssertionError("demotion must be a contract violation")

    # vanish: F2 removed without a rewrite → violation
    vanished_author = author.replace("| **F2** | `a.md` L9 | promoted question now a blocker |\n", "")
    try:
        build(vanished_author, brief, base)
    except ContractViolation as e:
        assert "F2" in str(e)
    else:
        raise AssertionError("vanished finding must be a contract violation")

    # unparseable finding-shaped line → violation
    broken = author.replace("| **F1** |", "| *F1* |")
    try:
        build(broken, brief, base)
    except ContractViolation as e:
        assert "unparseable" in str(e)
    else:
        raise AssertionError("unparseable line must be a contract violation")

    # pre-existing rewrite moves bucket + updates the brief count
    pre_author = author.replace(
        "| **F1** | `a.md` L8 | the model's edited fix prose |",
        "| **F1** | `a.md` L8 | **Pre-existing:** broken before this PR |",
    )
    ev2, author_out2, brief_out2 = build(pre_author, brief, base)
    assert {f["id"]: f["bucket"] for f in ev2["findings"]}["F1"] == "preexisting"
    assert "**Pre-existing issues in touched files:** 1" in brief_out2
    assert "F1" not in author_out2.split("### 🚨")[1].split("### ❓")[0]

    # A model-added F? row on the brief: numbered, and the author card's
    # REVIEW_STATE high-water mark follows.
    fx_author = (HERE / "testdata" / "v3-fixture-author.md.txt").read_text()
    fx_brief = (HERE / "testdata" / "v3-fixture-brief.md.txt").read_text()
    fx_base = json.loads((HERE / "testdata" / "v3-fixture-evidence-base.json").read_text())
    added = cr.render_finding_row("F?", ref="L9", file="content/docs/iac/x.md",
                                  body="model-added reviewer check")
    brief_plus = fx_brief.replace("### ⚠️ Check these before approving\n\n",
                                  "### ⚠️ Check these before approving\n\n"
                                  + cr.FINDING_TABLE_HEADER + "\n" + cr.FINDING_TABLE_SEPARATOR + "\n" + added + "\n\n", 1)
    ev_plus, a_plus, b_plus = build(fx_author, brief_plus, fx_base)
    new_id = f"F{ev_plus['high_water']}"
    assert f"**{new_id}**" in b_plus and "**F?**" not in b_plus, "F? numbered"
    assert review_state.parse_state(a_plus)["high_water"] == ev_plus["high_water"], "author high_water follows"

    # refresh_counts: a disposition takes a row out of the blocking count on
    # both cards without moving it.
    fx_author = (HERE / "testdata" / "v3-fixture-author.md.txt").read_text()
    fx_brief = (HERE / "testdata" / "v3-fixture-brief.md.txt").read_text()
    fx_state = review_state.parse_state(fx_author) or review_state.empty_state()
    from datetime import datetime, timezone
    fx_state = review_state.set_disposition(
        fx_state, "F3", "accepted", actor="alice", note="ship it",
        now=datetime(2026, 9, 1, 20, 0, tzinfo=timezone.utc))
    ra, rb = refresh_counts(review_state.replace_block(fx_author, fx_state), fx_brief, fx_state)
    assert "— 2 items block merge" in ra, "header excludes the accepted row"
    fx_all = fx_state
    for fid in ("F1", "F2"):
        fx_all = review_state.set_disposition(
            fx_all, fid, "accepted", actor="alice", note="ship it",
            now=datetime(2026, 9, 1, 20, 1, tzinfo=timezone.utc))
    ra_all, _ = refresh_counts(review_state.replace_block(fx_author, fx_all), None, fx_all)
    assert "— nothing blocks merge" in ra_all and "> [!NOTE]" in ra_all and "needs your answers" not in ra_all, "callout swaps at zero"
    ra_back, _ = refresh_counts(ra_all, None, None)
    assert "> [!IMPORTANT]" in ra_back and "needs your answers" in ra_back, "and swaps back"
    assert "✋ accepted as-is by the author" in rb and "(1 more is answered — see State)" in rb, rb
    assert "1 settled — see the evidence page" in rb or "Facts:" not in fx_brief, rb
    ra0, _ = refresh_counts(fx_author, None, None)
    assert "— 3 items block merge" in ra0

    print("build-evidence self-test passed")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--author-body")
    ap.add_argument("--brief-body")
    ap.add_argument("--base")
    ap.add_argument("--output")
    ap.add_argument("--author-out", help="cleaned author body for publish (optional)")
    ap.add_argument("--brief-out", help="cleaned brief body for publish (optional)")
    args = ap.parse_args()
    if args.self_test:
        return _self_test()
    if not (args.author_body and args.brief_body and args.base and args.output):
        ap.error("--author-body, --brief-body, --base, --output are required")
    try:
        evidence, author_out, brief_out = build(
            Path(args.author_body).read_text(),
            Path(args.brief_body).read_text(),
            json.loads(Path(args.base).read_text()),
        )
    except ContractViolation as e:
        print(f"::error::build-evidence: {e}", file=sys.stderr)
        return 2
    except (OSError, json.JSONDecodeError, ValueError) as e:
        print(f"::error::build-evidence: bad input: {e}", file=sys.stderr)
        return 2
    Path(args.output).write_text(json.dumps(evidence, indent=2) + "\n")
    if args.author_out:
        Path(args.author_out).write_text(author_out)
    if args.brief_out:
        Path(args.brief_out).write_text(brief_out)
    print(f"build-evidence: wrote {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
