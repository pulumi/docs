#!/usr/bin/env python3
"""apply-update.py — deterministic renderer for the v3 update lane.

On a v3 PR, `#update-review` inverts the v2 contract: the model ADJUDICATES
(it writes one structured patch, `.review-update.json`) and this script
RENDERS AND PUBLISHES — the model never touches the published comments. That
deletes the whole class of freehand-render failures the v2 lane needed
splice-spine.py, the effort-medium prohibition, and the provenance
spot-check to contain.

The model's patch is a closed action vocabulary over finding ids:

  resolve   the push fixed it → row moves to ✅ Resolved with the annotation
  concede   the model concedes the finding was wrong → ✅ Resolved with a
            `concede: <reason>` annotation (the exact v2 machine-scraped shape)
  hold      dispute adjudicated against the author → row stays, gains
            `🛡️ **Disputed by <actor> on YYYY-MM-DD, model held.**`
  promote   bucket moves up only (reviewer-check → author-answer →
            outstanding); demotion is rejected
  add       a new finding from the push delta; gets the next F-id
  retext    the finding's body text changes; id and anchor preserved

Disposition mapping (aligned with scrape-review-outcomes.py's v3
classifier, which this must never contradict):
  - `resolve` writes REVIEW_STATE disposition `fixed` (actor `update-lane`,
    sha = the new head): the gate reads it as answered, and the scraper's
    resolved-bucket row reads as `fixed`.
  - `concede` writes NO disposition. The ✅ row's `concede:` annotation IS
    the machine record (CONCEDE_ANNOTATION_RE); writing `refuted` here would
    flip the scraper's dispute adjudication from "conceded" (model yielded)
    to "refuted" (author answer standing un-reviewed) — a different claim.
  - `hold` writes NO disposition: the finding is still open; the author may
    still fix it or `/resolve` it.

The REVIEW_STATE race: a `/resolve` can land while the model works. The
publish chain re-fetches the live author card just before calling this
script, and this script parses REVIEW_STATE from that fresh body and merges
its own action-implied dispositions per finding-id (newest `updated_at`
wins) — never a whole-block overwrite.

Evidence: the trail/investigation log live only in S3, not on the cards, so
the credentialed publish step downloads the prior evidence object and passes
it as --prior-evidence; non-finding content is carried forward verbatim,
findings are replaced by the post-application set, and the history gains one
entry. When the prior object can't be fetched (degraded S3, or a review
published before evidence recording existed) the output carries
`"degraded": "prior-evidence-unavailable"` with an empty trail rather than
failing the whole refresh.

Auto-refresh runs (--auto) are strictly fix-response: `concede`, `hold`, and
`add` actions are dropped with a logged warning — an unattended run must
never adjudicate a dispute or raise new findings.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from datetime import datetime, timezone
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
be = _load("build_evidence", HERE / "build-evidence.py")
review_state = _load("review_state", _REVIEW_V3_DIR / "review_state.py")
validate_evidence_mod = _load("validate_evidence", _REVIEW_V3_DIR / "validate-evidence.py")

ACTIONS = ("resolve", "concede", "hold", "accept", "promote", "add", "retext")
AUTO_FORBIDDEN = ("concede", "hold", "accept", "add")
ADD_BUCKETS = ("outstanding", "author-answer", "reviewer-check")

RESOLVED_HEADING = "### ✅ Resolved since last review"
RESOLVED_PLACEHOLDER = "_No items resolved since the last review._"
# Same placeholder strings the composer uses, so an emptied section reads
# identically whether the initial lane or a refresh emptied it.
SECTION_EMPTY = {
    "outstanding": cr._V3_EMPTY_OUTSTANDING,
    "author-answer": cr._V3_EMPTY_QUESTIONS,
    "reviewer-check": cr._V3_EMPTY_CHECKS,
}
AUTHOR_HEADINGS = {
    "outstanding": "### 🚨 Fix or disagree",
    "author-answer": "### ❓ Questions for you",
}
BRIEF_HEADING = "### ⚠️ Check these before approving"
_BUCKET_RANK = {"reviewer-check": 0, "author-answer": 1, "outstanding": 2}
_HEAD_RE = re.compile(r"<!-- CLAUDE_REVIEW_HEAD [0-9a-f]{7,40} -->")
_AUTHOR_REV_RE = re.compile(r"^## Author action guide v(\d+) — ", re.M)
_BRIEF_HEADER_RE = re.compile(r"^## Reviewer's guide v\d+ — not for the author", re.M)
_SUB_RE = re.compile(r"<sub>(?:Review )?v\d+ · updated [^<]+</sub>")
_HINT_RE = re.compile(r"^_Editing in the browser\?[^\n]*\n(?:\n)?", re.M)
# The 🔄 banner the auto-refresh gate stamps under the markers. This lane
# re-renders from the LIVE body, so the banner must be stripped here — the
# first live auto-refresh published a fresh card still promising a refresh.
_BANNER_RE = re.compile(r"^> 🔄 \*\*Re-review in progress\*\*[^\n]*\n(?:\n)?", re.M)
_EVIDENCE_LINK_RE = re.compile(r"(📎 \*\*Full evidence:\*\* \[[^\]]+\]\()[^)]*(\))")


def set_evidence_url(body: str, url: str) -> str:
    """Point the 📎 line at this refresh's evidence page. The composer's
    token is long gone from a published card, so a refresh must rewrite the
    live URL — on the fork's artifact-only path the link otherwise keeps
    pointing at the FIRST run's artifact forever."""
    if not url:
        return body
    body = body.replace(cr.V3_EVIDENCE_TOKEN if hasattr(cr, "V3_EVIDENCE_TOKEN") else "%%EVIDENCE_URL%%", url)
    return _EVIDENCE_LINK_RE.sub(lambda m: m.group(1) + url + m.group(2), body, count=1)


class UpdateError(Exception):
    """A contract violation in the model's patch — exit 2, never guess."""


# Envelope slips the model has actually made (fork PR 242, 2026-09-01: no
# `schema`, no `case`, the list under `actions`) with an otherwise correct
# adjudication inside. Normalizing them is cheaper than failing the publish
# and stranding the PR on review:error; every repair is logged as a
# ::warning:: so the prompt drift stays visible.
_FINDINGS_ALIASES = ("actions", "entries", "updates", "patch")


def normalize_update(update: dict) -> tuple[dict, list[str]]:
    """Return (normalized copy, list of repairs). Never raises."""
    notes: list[str] = []
    if not isinstance(update, dict):
        return update, notes
    u = dict(update)
    if "findings" not in u:
        for alias in _FINDINGS_ALIASES:
            if isinstance(u.get(alias), list):
                u["findings"] = u.pop(alias)
                notes.append(f"`{alias}` → `findings`")
                break
    if "schema" not in u:
        u["schema"] = 1
        notes.append("`schema` defaulted to 1")
    if u.get("case") is None and isinstance(u.get("findings"), list):
        acts = {e.get("action") for e in u["findings"] if isinstance(e, dict)}
        if acts and acts <= {"resolve", "add"}:
            case = "fix-response"
        elif acts & {"concede", "hold", "accept"}:
            case = "dispute"
        else:
            case = "mixed"
        u["case"] = case
        notes.append(f"`case` inferred as {case}")
    return u, notes


def validate_update(update: dict, known_ids: set[str]) -> list[str]:
    problems: list[str] = []
    if update.get("schema") != 1:
        problems.append("update.schema must be 1")
    if update.get("case") not in ("fix-response", "dispute", "re-verify", "mixed"):
        problems.append(f"update.case {update.get('case')!r} not in the closed set")
    if not str(update.get("history_summary", "")).strip():
        problems.append("update.history_summary is required")
    findings = update.get("findings")
    if not isinstance(findings, list):
        return problems + ["update.findings must be a list"]
    for i, entry in enumerate(findings):
        where = f"findings[{i}]"
        if not isinstance(entry, dict):
            problems.append(f"{where} must be an object")
            continue
        action = entry.get("action")
        if action not in ACTIONS:
            problems.append(f"{where}.action {action!r} not in {ACTIONS}")
            continue
        if action == "add":
            if entry.get("bucket") not in ADD_BUCKETS:
                problems.append(f"{where}: add bucket {entry.get('bucket')!r} not in {ADD_BUCKETS}")
            if not str(entry.get("file", "")).strip() or not str(entry.get("text", "")).strip():
                problems.append(f"{where}: add requires file and text")
        else:
            fid = entry.get("id")
            if not isinstance(fid, str) or not re.match(r"^F\d+$", fid):
                problems.append(f"{where}: {action} requires an F<n> id")
            elif fid not in known_ids:
                problems.append(f"{where}: {fid} is not an open finding on this review")
        if action == "promote" and entry.get("to") not in ("author-answer", "outstanding"):
            problems.append(f"{where}: promote target {entry.get('to')!r} invalid")
        if action in ("concede", "hold", "accept", "promote") and not str(entry.get("reason", "")).strip():
            problems.append(f"{where}: {action} requires a reason")
        if action == "retext" and not str(entry.get("text", "")).strip():
            problems.append(f"{where}: retext requires text")
        if action == "retext" and "detail" in entry:
            detail = entry.get("detail")
            if not isinstance(detail, dict):
                problems.append(f"{where}: retext.detail must be an object {{why, fix[, keep]}}")
            else:
                for key in ("why", "fix"):
                    if not str(detail.get(key, "")).strip():
                        problems.append(f"{where}: retext.detail.{key} is required")
                if "keep" in detail and not str(detail.get("keep", "")).strip():
                    problems.append(f"{where}: retext.detail.keep must be non-empty when present")
        if action == "resolve" and not str(entry.get("annotation", "")).strip():
            problems.append(f"{where}: resolve requires an annotation")
    return problems


def _collect_rows(author_body: str, brief_body: str) -> dict[str, dict]:
    """id → {bucket, doc, parsed, raw} for every open finding row."""
    rows: dict[str, dict] = {}
    for doc, body, headings in (
        ("author", author_body, be.AUTHOR_SECTIONS),
        ("brief", brief_body, be.BRIEF_SECTIONS),
    ):
        for bucket, _idx, parsed, raw in be._walk(body, headings, doc):
            if parsed["id"] == "F?":
                raise UpdateError(f"{doc}: un-numbered F? row on a published card: {raw!r}")
            rows[parsed["id"]] = {"bucket": bucket, "doc": doc, "parsed": parsed, "raw": raw}
    return rows


def _collect_resolved(author_body: str) -> list[str]:
    lines = author_body.splitlines()
    out: list[str] = []
    in_section = False
    for line in lines:
        if line.startswith(RESOLVED_HEADING):
            in_section = True
            continue
        if in_section and be.is_section_terminator(line):
            break
        if in_section and line.startswith("|") and not cr.is_table_furniture(line):
            out.append(line)
    return out


def _render_row(fid: str, ref: str, file: str, body: str,
                link_base: str = "", edit_base: str = "") -> str:
    return cr.render_finding_row(fid, ref=ref, file=file, body=body,
                                 link_base=link_base, edit_base=edit_base)


def _strip_detail_blocks(body: str) -> tuple[str, dict[str, list[str]]]:
    """Remove every `#### F<n> · Do this` block; return (body, id → block lines).

    Blocks are re-inserted after their finding's table at render time, so a
    resolved/conceded finding's block drops and a promoted finding's block
    moves with its row."""
    spans, _texts = be.collect_detail_blocks(body)
    lines = body.splitlines()
    blocks: dict[str, list[str]] = {}
    drop: set[int] = set()
    for fid, (start, end) in spans.items():
        blocks[fid] = lines[start:end]
        drop.update(range(start, end))
        # swallow one leading blank line so stripping is symmetric with insertion
        if start > 0 and start - 1 not in drop and not lines[start - 1].strip():
            drop.add(start - 1)
    kept = [ln for i, ln in enumerate(lines) if i not in drop]
    return "\n".join(kept) + ("\n" if body.endswith("\n") else ""), blocks


# The rubber-stamp **Facts** bullet is re-derived by build-evidence.py
# (shared with the initial lane, which has the same post-disposition drift).
refresh_facts_line = be.refresh_facts_line


def _rebuild_detail_block(fid: str, old: list[str], detail: dict) -> list[str]:
    """A retext with `detail` refreshes the finding's Do-this block: the
    verbatim line is kept (the flagged text didn't change), Why/Fix/keep are
    replaced — same shape as the composer scaffold."""
    verbatim = next((ln for ln in old if ln.startswith("**Line (verbatim):**")), None)
    out = [f"#### {fid} · Do this", ""]
    if verbatim:
        out.append(verbatim)
    out.append(f"**Why:** {str(detail['why']).strip()}")
    out.append(f"**Fix:** {str(detail['fix']).strip()}")
    keep = str(detail.get("keep", "")).strip()
    if keep:
        out += ["", f"**If you'd rather keep it:** {keep}"]
    return out


def apply(
    author_body: str,
    brief_body: str,
    update: dict,
    *,
    head_sha: str,
    actor: str,
    auto: bool,
    repo: str = "",
    pr: int = 0,
    now: datetime | None = None,
    head_repo: str = "",
    head_branch: str = "",
) -> tuple[str, str, dict, dict]:
    """Returns (author_out, brief_out, model_state, applied_report)."""
    now = now or datetime.now(timezone.utc)
    today = now.date().isoformat()
    timestamp = now.replace(microsecond=0).isoformat().replace("+00:00", "Z")
    link_base = (f"https://github.com/{repo}/pull/{pr}/files"
                 if repo and pr else "")
    edit_base = (f"https://github.com/{head_repo}/edit/{head_branch}/"
                 if head_repo and head_branch else "")
    # Display revision: the card's own vN + 1. Equals the evidence history
    # length in the healthy path, and still counts correctly when the prior
    # evidence object was unavailable (degraded update).
    m_rev = _AUTHOR_REV_RE.search(author_body)
    new_rev = (int(m_rev.group(1)) + 1) if m_rev else 2

    author_body = _BANNER_RE.sub("", author_body)
    author_body, detail_blocks = _strip_detail_blocks(author_body)
    rows = _collect_rows(author_body, brief_body)
    resolved_rows = _collect_resolved(author_body)
    state = review_state.parse_state(author_body)
    if state is None:
        raise UpdateError("author card has no REVIEW_STATE block")
    high_water = int(state.get("high_water", 0))

    update, repairs = normalize_update(update)
    if repairs:
        print("::warning::apply-update repaired the patch envelope: " + "; ".join(repairs),
              file=sys.stderr)
    problems = validate_update(update, set(rows))
    if problems:
        raise UpdateError("; ".join(problems))

    actions = list(update.get("findings", []))
    dropped: list[str] = []
    if auto:
        kept = []
        for entry in actions:
            if entry.get("action") in AUTO_FORBIDDEN:
                dropped.append(f"{entry.get('action')} {entry.get('id', '(new)')}")
            else:
                kept.append(entry)
        actions = kept
        if dropped:
            print(
                "::warning::apply-update --auto dropped adjudication action(s): "
                + ", ".join(dropped)
                + " — auto-refresh is strictly fix-response",
                file=sys.stderr,
            )

    disposition_state = review_state.empty_state()
    disposition_state["high_water"] = high_water

    for entry in actions:
        action = entry["action"]
        if action == "add":
            high_water += 1
            fid = f"F{high_water}"
            ref = ""
            lines_val = entry.get("lines")
            if isinstance(lines_val, list) and lines_val:
                ref = f"L{lines_val[0]}"
                if len(lines_val) > 1 and lines_val[1] != lines_val[0]:
                    ref += f"-{lines_val[1]}"
            rows[fid] = {
                "bucket": entry["bucket"],
                "doc": "brief" if entry["bucket"] == "reviewer-check" else "author",
                "parsed": {"id": fid, "ref": ref, "file": entry["file"],
                           "body": entry["text"].strip()},
                "raw": "",
                "added": True,
            }
            continue

        fid = entry["id"]
        row = rows[fid]
        if action == "resolve":
            annotation = entry["annotation"].strip()
            resolved_rows.append(_render_row(
                fid, row["parsed"]["ref"], row["parsed"]["file"],
                f"{row['parsed']['body']} — {annotation}",
                link_base=link_base))
            del rows[fid]
            disposition_state = review_state.set_disposition(
                disposition_state, fid, "fixed",
                actor="update-lane", sha=head_sha[:12], now=now)
        elif action == "concede":
            reason = entry["reason"].strip()
            resolved_rows.append(_render_row(
                fid, row["parsed"]["ref"], row["parsed"]["file"],
                f"{row['parsed']['body']} — concede: {reason}",
                link_base=link_base))
            del rows[fid]
        elif action == "hold":
            # The author answered and the model still disagrees: that is a
            # judgment call for the human reviewer, not a lock on the author.
            # The row moves to the brief's ⚠️ list carrying the canonical
            # shield (scrape-review-outcomes keys on it) plus the hold reason,
            # and the author's answer is recorded as `refuted` so the merge
            # gate stops counting it — the promise footer-author.md makes
            # ("it stops blocking merge in both cases").
            reason = entry["reason"].strip()
            shield = f"🛡️ **Disputed by {actor} on {today}, model held.** {reason}"
            if "model held" not in row["parsed"]["body"]:
                row["parsed"]["body"] = row["parsed"]["body"].rstrip() + " " + shield
            row["bucket"] = "reviewer-check"
            row["doc"] = "brief"
            disposition_state = review_state.set_disposition(
                disposition_state, fid, "refuted",
                actor=actor, note=reason, sha=head_sha[:12], now=now)
        elif action == "accept":
            # The author accepted the finding as-is (the footer's third verb).
            # Their to-do is done — but a knowingly-shipped finding is exactly
            # what the human reviewer should weigh, so the row moves to the
            # brief's ⚠️ list with a ✋ marker, and REVIEW_STATE records
            # `accepted` (bulk-flagged when the mention accepted everything).
            reason = entry["reason"].strip()
            marker = f"✋ **Accepted as-is by {actor} on {today}.** {reason}"
            if "Accepted as-is by" not in row["parsed"]["body"]:
                row["parsed"]["body"] = row["parsed"]["body"].rstrip() + " " + marker
            row["bucket"] = "reviewer-check"
            row["doc"] = "brief"
            disposition_state = review_state.set_disposition(
                disposition_state, fid, "accepted",
                actor=actor, note=reason, sha=head_sha[:12],
                bulk=bool(entry.get("bulk", False)), now=now)
        elif action == "promote":
            target = entry["to"]
            if _BUCKET_RANK[target] <= _BUCKET_RANK[row["bucket"]]:
                raise UpdateError(
                    f"promote {fid}: {row['bucket']} → {target} is not upward — promote-only")
            row["bucket"] = target
            row["doc"] = "author"
        elif action == "retext":
            row["parsed"]["body"] = entry["text"].strip()
            if isinstance(entry.get("detail"), dict) and fid in detail_blocks:
                detail_blocks[fid] = _rebuild_detail_block(fid, detail_blocks[fid], entry["detail"])

    # Merge action-implied dispositions with the LIVE card's state — a
    # /resolve that landed while the model worked survives (newest wins).
    merged_state = review_state.merge_states(state, disposition_state)
    merged_state["high_water"] = max(merged_state["high_water"], high_water)

    author_out = _render_doc(author_body, rows, resolved_rows, doc="author",
                             link_base=link_base, edit_base=edit_base,
                             detail_blocks=detail_blocks)
    if resolved_rows and RESOLVED_HEADING not in author_out:
        # the composer omits ✅ Resolved while empty — insert it on first resolve
        a_lines = author_out.splitlines()
        at = next((i for i, ln in enumerate(a_lines) if ln.startswith("📎 ")), len(a_lines))
        a_lines[at:at] = [RESOLVED_HEADING, "", cr.FINDING_TABLE_HEADER,
                          cr.FINDING_TABLE_SEPARATOR, *resolved_rows, ""]
        author_out = "\n".join(a_lines) + ("\n" if author_out.endswith("\n") else "")
    brief_out = _render_doc(brief_body, rows, resolved_rows, doc="brief",
                            link_base=link_base)

    open_findings = [{"id": fid, "bucket": r["bucket"],
                      "text": r["parsed"]["body"]}
                     for fid, r in sorted(rows.items(), key=lambda kv: int(kv[0][1:]))
                     if r["bucket"] in ("outstanding", "author-answer")]
    brief_out = cr.replace_waiting_block(
        brief_out, open_findings, merged_state.get("findings", {}))
    author_out = review_state.replace_block(author_out, merged_state)
    # Blocking = author-card rows WITHOUT a disposition: a `/resolve F1
    # accepted` that landed before this refresh must not be counted back in.
    n_blocking = be.count_blocking(open_findings, merged_state.get("findings", {}))
    author_out = be._fix_header(author_out, n_blocking, rev=new_rev)
    author_out = _HEAD_RE.sub(f"<!-- CLAUDE_REVIEW_HEAD {head_sha} -->", author_out, count=1)
    brief_out = _BRIEF_HEADER_RE.sub(
        f"## Reviewer's guide v{new_rev} — not for the author", brief_out, count=1)
    new_sub = f"<sub>Review v{new_rev} · updated {timestamp} · head commit {head_sha[:7]}</sub>"
    author_out = _SUB_RE.sub(new_sub, author_out, count=1)
    brief_out = _SUB_RE.sub(new_sub, brief_out, count=1)

    # Section replacement pads with blank lines; without this a card grows a
    # blank line per refresh (observed on the fork after one update).
    author_out = author_out.rstrip("\n") + "\n"
    brief_out = brief_out.rstrip("\n") + "\n"
    report = {
        "blocking": n_blocking,
        "resolved": len(resolved_rows),
        "dropped_in_auto": dropped,
        "high_water": merged_state["high_water"],
        "timestamp": timestamp,
    }
    return author_out, brief_out, merged_state, report


def _render_doc(body: str, rows: dict[str, dict], resolved_rows: list[str], doc: str,
                link_base: str = "", edit_base: str = "",
                detail_blocks: dict[str, list[str]] | None = None) -> str:
    """Re-render the finding sections of one card, everything else verbatim.

    Rows carry no display state — REVIEW_STATE is the state, the section a
    row lives in is the display.
    """
    if doc == "author":
        # The browser hint is re-derived below: present iff the card still
        # has rows to edit (an emptied card kept an orphaned hint on the fork).
        body = _HINT_RE.sub("", body)
    lines = body.splitlines()
    headings = be.AUTHOR_SECTIONS if doc == "author" else be.BRIEF_SECTIONS
    spans = be._sections(body, headings)
    if doc == "author":
        spans = spans + _resolved_span(lines)
    author_rows_left = any(by_bucket_key in ("outstanding", "author-answer")
                           for by_bucket_key in
                           {r["bucket"] for r in rows.values() if r["doc"] == "author"})

    by_bucket: dict[str, list[str]] = {}
    for fid in sorted(rows, key=lambda f: int(f[1:])):
        row = rows[fid]
        if row["doc"] != doc:
            continue
        by_bucket.setdefault(row["bucket"], []).append(_render_row(
            fid, row["parsed"]["ref"], row["parsed"]["file"], row["parsed"]["body"],
            link_base=link_base, edit_base=edit_base))
        by_bucket.setdefault(row["bucket"] + ":ids", []).append(fid)

    def _table(rows_out: list[str]) -> list[str]:
        return [cr.FINDING_TABLE_HEADER, cr.FINDING_TABLE_SEPARATOR, *rows_out]

    replacements: list[tuple[int, int, list[str]]] = []
    for bucket, start, end in spans:
        if bucket == "resolved":
            new_lines = _table(resolved_rows) if resolved_rows else [RESOLVED_PLACEHOLDER]
        else:
            bucket_rows = by_bucket.get(bucket)
            new_lines = _table(bucket_rows) if bucket_rows else [SECTION_EMPTY.get(bucket, "")]
            if doc == "author" and detail_blocks:
                for fid in by_bucket.get(bucket + ":ids", []):
                    if fid in detail_blocks:
                        new_lines = new_lines + [""] + detail_blocks[fid]
            if doc == "author" and bucket == "author-answer" and edit_base and author_rows_left:
                new_lines = new_lines + ["", cr.V3_BROWSER_HINT]
        replacements.append((start, end, [""] + new_lines + [""]))

    for start, end, new_lines in sorted(replacements, reverse=True):
        lines[start:end] = new_lines
    return "\n".join(lines) + ("\n" if body.endswith("\n") else "")


def _resolved_span(lines: list[str]) -> list[tuple[str, int, int]]:
    for i, line in enumerate(lines):
        if line.startswith(RESOLVED_HEADING):
            end = len(lines)
            for j in range(i + 1, len(lines)):
                if be.is_section_terminator(lines[j]):
                    end = j
                    break
            return [("resolved", i + 1, end)]
    return []


def assemble_evidence(
    prior: dict | None,
    author_out: str,
    brief_out: str,
    merged_state: dict,
    update: dict,
    *,
    repo: str,
    pr: int,
    head_sha: str,
    run_id: str,
    timestamp: str,
) -> dict:
    rows = _collect_rows(author_out, brief_out)
    prior_findings = {f["id"]: f for f in (prior or {}).get("findings", [])}
    _spans, detail_texts = be.collect_detail_blocks(author_out)
    findings: list[dict] = []
    for fid in sorted(rows, key=lambda f: int(f[1:])):
        row = rows[fid]
        carried = prior_findings.get(fid, {})
        body_text = row["parsed"]["body"]
        if "model held" in body_text:
            status = "disputed-held"
        elif "Accepted as-is by" in body_text:
            status = "accepted-as-is"
        else:
            status = "open"
        record = {
            "id": fid,
            "bucket": row["bucket"],
            "file": row["parsed"]["file"] or carried.get("file") or "(unknown)",
            "text": row["parsed"]["body"],
            "origin": carried.get("origin") or "model",
            "status": status,
            "disposition": merged_state["findings"].get(fid) or carried.get("disposition"),
        }
        lines_val = cr._lines_from_ref(row["parsed"]["ref"])
        if lines_val:
            record["lines"] = lines_val
        elif carried.get("lines"):
            record["lines"] = carried["lines"]
        detail = detail_texts.get(fid) or carried.get("detail")
        if detail:
            record["detail"] = detail
        findings.append(record)
    # ✅ rows and prior preexisting carry through with their terminal status.
    resolved_ids = set()
    for line in _collect_resolved(author_out):
        parsed = cr.parse_finding_line(line)
        if not parsed or parsed["id"] in rows:
            continue
        resolved_ids.add(parsed["id"])
        carried = prior_findings.get(parsed["id"], {})
        conceded = "concede" in parsed["body"].lower()
        findings.append({
            "id": parsed["id"],
            "bucket": carried.get("bucket") or "outstanding",
            "file": parsed["file"] or carried.get("file") or "(unknown)",
            "text": parsed["body"],
            "origin": carried.get("origin") or "model",
            "status": "conceded" if conceded else "resolved",
            "disposition": merged_state["findings"].get(parsed["id"]) or carried.get("disposition"),
        })
    for fid, f in prior_findings.items():
        if f.get("bucket") == "preexisting" and fid not in rows and fid not in resolved_ids:
            findings.append(f)

    entry = {"ts": timestamp, "summary": update["history_summary"].strip(), "sha": head_sha[:12]}
    evidence = {
        "schema_version": 1,
        "repo": repo,
        "pr": pr,
        "head_sha": head_sha,
        "run_id": run_id,
        "generated_at": timestamp,
        "high_water": merged_state["high_water"],
        "findings": findings,
        "trail": (prior or {}).get("trail", []),
        "investigation_log": (prior or {}).get("investigation_log", {}),
        "history": list((prior or {}).get("history", [])) + [entry],
    }
    for key in ("editorial_balance", "triaged", "style_suggestions_count", "confidence", "summary"):
        if prior and key in prior:
            evidence[key] = prior[key]
    if prior is None:
        evidence["degraded"] = "prior-evidence-unavailable"
    problems = validate_evidence_mod.validate_evidence(evidence)
    if problems:
        raise UpdateError("assembled evidence invalid: " + "; ".join(problems))
    return evidence


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--author-card", required=False)
    parser.add_argument("--brief-card", required=False)
    parser.add_argument("--update", required=False)
    parser.add_argument("--prior-evidence", default=None)
    parser.add_argument("--head-sha", required=False)
    parser.add_argument("--actor", required=False, default="update-lane")
    parser.add_argument("--repo", default="")
    parser.add_argument("--pr", type=int, default=0)
    parser.add_argument("--run-id", default="")
    parser.add_argument("--auto", action="store_true")
    parser.add_argument("--author-out", default=".review-card-author.out.md")
    parser.add_argument("--brief-out", default=".review-card-brief.out.md")
    parser.add_argument("--evidence-out", default=".review-evidence.json")
    parser.add_argument("--head-repo", default="", help="head repo full name for ✏️ edit links")
    parser.add_argument("--head-branch", default="", help="head branch for ✏️ edit links")
    parser.add_argument("--evidence-url", default="", help="URL for the 📎 evidence line on both cards")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        return _self_test()
    for req in ("author_card", "brief_card", "update", "head_sha", "repo", "pr", "run_id"):
        if not getattr(args, req):
            parser.error(f"--{req.replace('_', '-')} is required")

    author_body = Path(args.author_card).read_text()
    brief_body = Path(args.brief_card).read_text()
    try:
        update = json.loads(Path(args.update).read_text())
    except json.JSONDecodeError as exc:
        print(f"apply-update: .review-update.json is not valid JSON: {exc}", file=sys.stderr)
        return 2

    prior = None
    if args.prior_evidence and Path(args.prior_evidence).exists():
        try:
            prior = json.loads(Path(args.prior_evidence).read_text())
        except json.JSONDecodeError:
            print("apply-update: prior evidence unreadable; proceeding degraded", file=sys.stderr)

    try:
        author_out, brief_out, merged_state, report = apply(
            author_body, brief_body, update,
            head_sha=args.head_sha, actor=args.actor, auto=args.auto,
            repo=args.repo, pr=args.pr,
            head_repo=args.head_repo, head_branch=args.head_branch)
        evidence = assemble_evidence(
            prior, author_out, brief_out, merged_state, update,
            repo=args.repo, pr=args.pr, head_sha=args.head_sha,
            run_id=args.run_id, timestamp=report["timestamp"])
        brief_out = refresh_facts_line(brief_out, evidence["findings"])
        author_out = set_evidence_url(author_out, args.evidence_url)
        brief_out = set_evidence_url(brief_out, args.evidence_url)
    except UpdateError as exc:
        print(f"apply-update: contract violation: {exc}", file=sys.stderr)
        return 2

    Path(args.author_out).write_text(author_out)
    Path(args.brief_out).write_text(brief_out)
    Path(args.evidence_out).write_text(json.dumps(evidence, indent=2) + "\n")
    print(json.dumps(report))
    return 0


def _fixture_paths() -> tuple[Path, Path]:
    td = HERE / "testdata"
    return td / "v3-fixture-author.md.txt", td / "v3-fixture-brief.md.txt"


def _self_test() -> int:
    author_p, brief_p = _fixture_paths()
    author = author_p.read_text()
    brief = brief_p.read_text()
    sha = "b" * 40
    update = {
        "schema": 1, "case": "mixed", "history_summary": "resolved F1, held F3",
        "findings": [
            {"id": "F1", "action": "resolve", "annotation": "fixed in b1b2b3"},
            {"id": "F3", "action": "hold", "reason": "evidence: docs say otherwise"},
            {"id": "F4", "action": "promote", "to": "outstanding", "reason": "also in social copy"},
            {"action": "add", "bucket": "reviewer-check", "file": "content/docs/iac/x.md",
             "lines": [200], "text": "new soft mismatch worth a look", "origin": "model"},
        ],
    }
    a_out, b_out, state, report = apply(author, brief, update, head_sha=sha, actor="cam", auto=False,
                                        head_repo="example/docs-fork", head_branch="fix/component-doc")
    assert "**F1**" in a_out and "fixed in b1b2b3" in a_out, "F1 resolved row rendered"
    assert a_out.index("fixed in b1b2b3") > a_out.index(RESOLVED_HEADING)
    assert state["findings"]["F1"]["disposition"] == "fixed"
    assert "model held" in b_out and "Disputed by cam on " in b_out, "held row moved to the brief ⚠️ list"
    assert "docs say otherwise" in b_out, "hold reason rendered beside the shield"
    assert "**F3**" not in a_out.split("<!-- REVIEW_STATE")[0], "held row left the author card"
    assert "#### F3 · Do this" not in a_out, "held row's Do-this block dropped with it"
    assert state["findings"]["F3"]["disposition"] == "refuted", "hold records the author's answer"
    assert state["findings"]["F3"]["note"] == "evidence: docs say otherwise"
    assert a_out.index("**F4**") < a_out.index("### ❓"), "F4 promoted into 🚨"
    assert "**F5**" in b_out and "new soft mismatch" in b_out, "add landed in brief with next id"
    assert f"<!-- CLAUDE_REVIEW_HEAD {sha} -->" in a_out
    assert "## Author action guide v2 — 2 items block merge" in a_out, f"count refreshed and rev bumped: {report}"
    assert a_out.count("📎 **Full evidence:**") == 1, "evidence line survives the re-render"
    assert a_out.count(cr.V3_BROWSER_HINT_PREFIX) == 1, "browser hint survives, exactly once"
    assert "<sub>Review v2 · updated " in a_out and "<sub>Review v2 · updated " in b_out, "sub line rewritten on both cards"
    assert f"· head commit {sha[:7]}</sub>" in a_out and "." not in a_out.split("· updated ")[1].split(" ·")[0], "sub: 7-char sha, no microseconds"
    assert not a_out.endswith("\n\n") and not b_out.endswith("\n\n"), "no trailing blank growth"
    reparsed = review_state.parse_state(a_out)
    assert reparsed is not None and reparsed["high_water"] == 5

    # Racing /resolve survives: author card carries a disposition for F2.
    from datetime import datetime, timezone
    live = review_state.set_disposition(
        review_state.parse_state(author), "F2", "refuted", actor="author", note="n",
        now=datetime(2026, 8, 31, 23, 0, tzinfo=timezone.utc))
    author_live = review_state.replace_block(author, live)
    a2, _b2, state2, _ = apply(author_live, brief, update, head_sha=sha, actor="cam", auto=False)
    assert state2["findings"]["F2"]["disposition"] == "refuted", "racing /resolve merged, not clobbered"
    assert review_state.parse_state(a2)["findings"]["F2"]["disposition"] == "refuted"

    # Auto mode drops adjudication actions but keeps resolve.
    update_auto = {
        "schema": 1, "case": "fix-response", "history_summary": "auto",
        "findings": [
            {"id": "F1", "action": "resolve", "annotation": "fixed in c1c2c3"},
            {"id": "F2", "action": "concede", "reason": "nope"},
        ],
    }
    a3, _b3, state3, r3 = apply(author, brief, update_auto, head_sha=sha, actor="auto-refresh", auto=True)
    assert state3["findings"].get("F1", {}).get("disposition") == "fixed"
    assert "concede: nope" not in a3 and r3["dropped_in_auto"] == ["concede F2"]

    # Demotion rejected; unknown id rejected.
    for bad in (
        {"schema": 1, "case": "mixed", "history_summary": "x",
         "findings": [{"id": "F1", "action": "promote", "to": "author-answer", "reason": "r"}]},
        {"schema": 1, "case": "mixed", "history_summary": "x",
         "findings": [{"id": "F99", "action": "resolve", "annotation": "a"}]},
    ):
        try:
            apply(author, brief, bad, head_sha=sha, actor="x", auto=False)
        except UpdateError:
            pass
        else:
            raise AssertionError(f"expected rejection: {bad}")

    # Evidence assembly: prior carried forward; degraded without prior.
    base = json.loads((HERE / "testdata" / "v3-fixture-evidence-base.json").read_text())
    ev = assemble_evidence(base, a_out, b_out, state, update,
                           repo="pulumi/docs", pr=999, head_sha=sha, run_id="t1",
                           timestamp="2026-08-31T23:30:00Z")
    assert ev["trail"] == base["trail"] and "degraded" not in ev
    assert ev["history"][-1]["summary"] == "resolved F1, held F3"
    f1 = next(f for f in ev["findings"] if f["id"] == "F1")
    assert f1["status"] == "resolved" and f1["disposition"]["disposition"] == "fixed"
    ev2 = assemble_evidence(None, a_out, b_out, state, update,
                            repo="pulumi/docs", pr=999, head_sha=sha, run_id="t1",
                            timestamp="2026-08-31T23:30:00Z")
    assert ev2["degraded"] == "prior-evidence-unavailable" and ev2["trail"] == []

    print("apply-update self-test passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
