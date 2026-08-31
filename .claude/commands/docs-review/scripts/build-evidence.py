#!/usr/bin/env python3
"""build-evidence.py — turn the model-edited v3 drafts back into evidence.

Runs after the model edits `.review-draft-author.md` / `.review-draft-brief.md`
(surface v3) and before the credentialed publish job records anything. It is
the fail-closed half of the round-trip contract: the composer renders finding
bullets with `render_finding_line`, the model edits them in place, and this
script parses them back with the same grammar (`parse_finding_line`) — a line
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
    "### 🚨 Must fix or refute": "outstanding",
    "### ❓ Only you can answer these": "author-answer",
}
BRIEF_SECTIONS = {
    "### 👀 Check these before approving": "reviewer-check",
}
# Rank for the never-demote check.
_BUCKET_RANK = {"reviewer-check": 0, "author-answer": 1, "outstanding": 2, "preexisting": 0}

# Anchored at the start of the parsed body: the contract is "REWRITE the
# bullet body as `**Spurious:** …`", and the composer's own TODO instructions
# quote these labels mid-string — a floating search would file every unedited
# stub as triaged (caught by test_build_evidence_on_fixtures).
_SPURIOUS_RE = re.compile(r"^(?:\*[\"']?.{0,160}?[\"']?\*\s+—\s+)?\*\*(Spurious|Mis-sourced):\*\*\s*(?P<note>.*)$")
_PREEXISTING_RE = re.compile(r"^(?:\*[\"']?.{0,160}?[\"']?\*\s+—\s+)?\*\*Pre-existing:\*\*\s*(?P<note>.*)$")
_PREEXISTING_COUNT_RE = re.compile(r"(💡 \*\*Pre-existing issues in touched files:\*\* )\d+")
_HEADER_RE = re.compile(r"^## Review — (?:action needed \(\d+ blocking\)|no action needed)( — Last updated .*)$")
_SUMMARY_RE = re.compile(r"^> \*\*Summary:\*\*\s*(?P<text>.+)$")
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
        elif line.startswith("### ") or line.startswith("#### ") or line.startswith("<!-- REVIEW_STATE"):
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
            if not raw.startswith("- "):
                continue
            parsed = cr.parse_finding_line(raw)
            if parsed is None:
                # The 👀 section may carry plain advisory prose notes the
                # model leaves for the reviewer — untracked by design (no
                # id, no REVIEW_STATE entry, not a finding). They stay in
                # the published brief verbatim. Only a bullet that tries to
                # be a finding row must parse; blocking sections have no
                # such latitude. Mirrors validate-pinned's
                # v3-finding-grammar rule exactly.
                looks_like_finding = bool(
                    re.match(r"^\s*-\s*(\[[ x]\]|\*\*F[\d?]+\*\*)", raw)
                )
                if bucket == "reviewer-check" and not looks_like_finding:
                    continue
                raise ContractViolation(
                    f"{where}: unparseable finding line in {bucket} section: {raw!r}"
                )
            yield bucket, i, parsed, raw


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

    author_out = _clean(author_body, drop_lines["author"], renumber["author"])
    brief_out = _clean(brief_body, drop_lines["brief"], renumber["brief"])
    n_blocking = sum(1 for f in findings if f["bucket"] in ("outstanding", "author-answer"))
    author_out = _fix_header(author_out, n_blocking)
    n_pre = sum(1 for f in findings if f["bucket"] == "preexisting")
    brief_out = _PREEXISTING_COUNT_RE.sub(lambda m: m.group(1) + str(n_pre), brief_out)
    return evidence, author_out, brief_out


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


def _fix_header(body: str, n_blocking: int) -> str:
    lines = body.splitlines()
    for i, line in enumerate(lines):
        m = _HEADER_RE.match(line)
        if m:
            verb = f"action needed ({n_blocking} blocking)" if n_blocking else "no action needed"
            lines[i] = f"## Review — {verb}{m.group(1)}"
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
        "## Review — action needed (2 blocking) — Last updated " + ts, "",
        "### 🚨 Must fix or refute (blocks merge)", "",
        "- [ ] **F1** **[L8]** `a.md` — the model's edited fix prose", "",
        "- [ ] **F2** **[L9]** `a.md` — promoted question now a blocker", "",
        "- [ ] **F?** `a.md` — a brand new model finding", "",
        "### ❓ Only you can answer these (blocks merge)", "",
        "_No open questions for you._", "",
        "📎 **Full evidence:** %%EVIDENCE_URL%%", "", state_block, "",
    ]) + "\n"
    brief = "\n".join([
        "<!-- CLAUDE_REVIEW_BRIEF -->", "## Reviewer brief — Last updated " + ts + " (head aaaa)", "",
        "> **Summary:** A tidy little PR about a.md.", "",
        "> | Dimension | Level | Notes |", "> | :--- | :---: | :--- |", "> | facts | HIGH |  |", "",
        "### 👀 Check these before approving", "",
        "- **F3** **[L12]** `a.md` — **Spurious:** the comparison was against stale data", "",
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
    assert "F3" not in brief_out.split("💡")[0].split("👀")[1], "spurious bullet dropped from brief"
    assert ev["summary"] == "A tidy little PR about a.md."
    assert ev["confidence"]["facts"] == "HIGH"
    assert ev["history"][-1]["summary"] == "A tidy little PR about a.md."
    assert "action needed (3 blocking)" in author_out

    # demotion: F1 rendered in the brief's 👀 → violation
    demoted_brief = brief.replace(
        "- **F3** **[L12]** `a.md` — **Spurious:** the comparison was against stale data",
        "- **F1** **[L8]** `a.md` — softened down\n\n- **F3** **[L12]** `a.md` — **Spurious:** stale data",
    )
    demoted_author = author.replace("- [ ] **F1** **[L8]** `a.md` — the model's edited fix prose\n\n", "")
    try:
        build(demoted_author, demoted_brief, base)
    except ContractViolation as e:
        assert "demoted" in str(e), e
    else:
        raise AssertionError("demotion must be a contract violation")

    # vanish: F2 removed without a rewrite → violation
    vanished_author = author.replace("- [ ] **F2** **[L9]** `a.md` — promoted question now a blocker\n\n", "")
    try:
        build(vanished_author, brief, base)
    except ContractViolation as e:
        assert "F2" in str(e)
    else:
        raise AssertionError("vanished finding must be a contract violation")

    # unparseable finding-shaped line → violation
    broken = author.replace("- [ ] **F1** **[L8]**", "- [ ] *F1* [L8]")
    try:
        build(broken, brief, base)
    except ContractViolation as e:
        assert "unparseable" in str(e)
    else:
        raise AssertionError("unparseable line must be a contract violation")

    # pre-existing rewrite moves bucket + updates the brief count
    pre_author = author.replace(
        "- [ ] **F1** **[L8]** `a.md` — the model's edited fix prose",
        "- [ ] **F1** **[L8]** `a.md` — **Pre-existing:** broken before this PR",
    )
    ev2, author_out2, brief_out2 = build(pre_author, brief, base)
    assert {f["id"]: f["bucket"] for f in ev2["findings"]}["F1"] == "preexisting"
    assert "**Pre-existing issues in touched files:** 1" in brief_out2
    assert "F1" not in author_out2.split("### 🚨")[1].split("### ❓")[0]

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
