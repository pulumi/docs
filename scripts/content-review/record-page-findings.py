#!/usr/bin/env python3
"""Persist one page's review findings as structured data.

Until this existed, a review's findings survived in exactly two forms:

  * the ledger's `skipped_findings` — an integer, with no record of WHAT
  * the PR body — prose, written for a human

and `build-glowup-backlog.py` recovered them months later by downloading the
PR body and parsing the markdown back into data. That round trip is the
problem this closes:

  * the PR body became load-bearing data, so anyone tidying a table silently
    changed what the glow-up lane would act on;
  * heading-based extraction fails silently — rename a section and the backlog
    just comes back empty;
  * only the LATEST PR is recoverable (branches are reused, so older reviews
    cannot be found), which quietly discarded every earlier review's findings;
  * GitHub became a hard dependency for reading our own bookkeeping.

Nothing new is asked of the model. The findings themselves already exist as
JSON — they are the deterministic pre-step artifacts that `compose-pr-body.py`
stubs the PR body FROM, and this script reuses that module's `collect()` so the
two can never drift on what counts as a finding. The only model-supplied part
is the DISPOSITION, and that is already structured too: the verdict's
`applied[]` array records what was fixed. Everything found and not applied is
the difference between the two.

What is deliberately NOT captured is the model's one-line reason for deferring,
which exists only as PR-body prose. `build-glowup-backlog.py` still reads the
PR body for that, and merges it onto this spine — so this file is strictly more
than the backlog had, never less, and the prose stays enrichment rather than
the system of record.

Output (uploaded to the ledger bucket's `findings/` prefix, beside `ledger/`
and `claims/`):

    {"schema_version": 2, "slug": ..., "path": ..., "reviewed_at": ...,
     "commit": ..., "verdict": "fixed|clean|skipped|glowup",
     "counts": {"total": N, "applied": N, "deferred": N, "superseded": N},
     "findings": [{"id": "f3", "label": ..., "source": ..., "detail": ...,
                   "category": ..., "line_range": ..., "fix_candidate": bool,
                   "applied": bool,
                   "finding": "<the label — what was found>",
                   "prior_disposition": {"status": "applied|deferred|superseded",
                                         "reason": "<the model's one-liner, if any>",
                                         "lane": "fix|glowup"}}, ...]}

Schema v2 (2026-09-01) splits FINDING from PRIOR DISPOSITION. v1 recorded
the finding and an `applied` bit, and the glow-up lane recovered the
reviewer's reason from the PR body and handed the two to the model fused in
one string — which is how PR #21291 promoted an aside inside a decline
reason into a new claim, and PR #21293 executed a finding the July run had
declined as editorial. `finding` is the work; `prior_disposition.reason` is
one earlier reviewer's opinion of it (context, never direction) and comes
from the PR body draft when `--pr-body` is given. `superseded` marks a
finding the glow-up composer pre-declined because this run's re-verification
overruled it; `build-glowup-backlog.py` never banks those again. The v1 keys
are all still written, so a v1 reader keeps working, and a v1 record (no
`prior_disposition`) still reads.

`applied` is decided by LINE OVERLAP against the verdict's `applied[].lines`,
using verify-fix-scope.py's own parser and tolerances — the publish gate
already answers "does this edit fall inside a recorded finding?", so this does
not form a second, looser opinion about it.

Whole-page snapshot semantics, same as `record-claims.py`: a review sees the
entire page, so overwriting `<slug>.json` is always correct.

GLOW-UP RUNS are the exception, and take their disposition from the sentinel's
`executed_ids`/`declined_ids` instead (`--backlog` supplies the id mapping). A
glow-up carries no `applied[]` by design, so the line-overlap match above finds
nothing and would file every finding — including everything the glow-up just
executed — as deferred. Two states mean NO record is written for that run: a
sentinel carrying neither list, and one whose executed ids ALL fail to resolve
to a finding here (a missing backlog snapshot, or labels that have drifted).
Both are the same information state — the disposition is unknown — and the
all-False record that would otherwise be written re-banks everything the
glow-up just finished. A
PARTIAL resolve still writes; so does a glow-up that executed only pr-body
items, which have no counterpart on this record and are expected to resolve to
nothing. When the write is skipped the previous record stands, so `reviewed_at`
can lag the ledger's. That is deliberate: the fix-lane record is the truthful
one, and a stale-but-true record beats a fresh-but-wrong one.

Usage:
    record-page-findings.py --queue .content-review-queue.json \
        --verdict .content-review-verdict.json --out .page-findings.json \
        [--verified-claims .verified-claims.json] [--vale-findings ...] \
        [--readthrough ...] [--frontmatter ...] [--uri s3://.../findings/]
    record-page-findings.py --self-test
"""

from __future__ import annotations

import argparse
import contextlib
import importlib.util
import io
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCHEMA_VERSION = 2


def log(msg: str) -> None:
    print(f"record-page-findings: {msg}", file=sys.stderr)


def warn(msg: str) -> None:
    print(f"::warning::record-page-findings: {msg}", file=sys.stderr)


def _compose():
    """compose-pr-body.py by path — its collect() is the single definition of
    'what counts as a finding', and duplicating it here would guarantee drift
    between the PR body and this record."""
    spec = importlib.util.spec_from_file_location(
        "compose_pr_body", HERE / "compose-pr-body.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def read_json(path: Path | None):
    if path is None or not path.is_file():
        return None
    try:
        return json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as e:
        warn(f"{path} unreadable ({e})")
        return None


def _backlog_mod():
    """build-glowup-backlog.py by path — owns the banked-row grammar
    (`split_finding`), which is how a PR body's deferral bullets and a
    glow-up's declined rows are read back into (finding, reason)."""
    spec = importlib.util.spec_from_file_location(
        "build_glowup_backlog", HERE / "build-glowup-backlog.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _section(body: str, name: str) -> str:
    import re
    m = re.search(rf"^##\s+{re.escape(name)}\s*$(.*?)(?=^##\s|\Z)", body or "", re.M | re.S)
    return m.group(1) if m else ""


def deferral_reasons(body: str | None) -> list[tuple[str, str]]:
    """(finding, reason) pairs from a fix-lane body's "Findings not applied"
    bullets, in order. The composer renders `- **<label>** — <reason>` and
    the label is collect()'s own, so matching back is a prefix test."""
    bgb = _backlog_mod()
    out = []
    for line in _section(body or "", "Findings not applied").splitlines():
        line = line.strip()
        if not line.startswith(("-", "*")) or bgb.TRAILER_RE.search(line):
            continue
        finding, reason = bgb.split_finding(line)
        if finding:
            out.append((finding, reason))
    return out


def declined_reasons(body: str | None) -> dict[str, str]:
    """backlog id -> reason from a glow-up body's "Backlog declined" rows
    (`| \`id\` — … | #pr | <why> |`)."""
    import re
    out: dict[str, str] = {}
    for line in _section(body or "", "Backlog declined").splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        m = re.match(r"^\|\s*`([^`]+)`", line)
        if not m:
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) >= 3:
            out[m.group(1)] = cells[-1]
    return out


def _reason_for(label: str, pairs: list[tuple[str, str]]) -> str:
    lab = (label or "").strip()
    for finding, reason in pairs:
        f = finding.strip()
        if f and lab and (f.startswith(lab) or lab.startswith(f)):
            return reason
    return ""


def attach_dispositions(findings: list[dict], lane: str, body: str | None,
                        backlog: dict | None = None) -> list[dict]:
    """Stamp schema-v2 `finding` / `prior_disposition` on marked findings.

    Fix lane: the reason is the "Findings not applied" bullet whose bold
    label matches. Glow-up: an executed item is applied; a declined item's
    reason is its "Backlog declined" row; an item the composer pre-declined
    (`pre_declined` on the reconciled backlog item) is `superseded`, so the
    next backlog build leaves it out. Everything unmatched is `deferred` with
    an empty reason — v1 semantics, made explicit.
    """
    pairs = deferral_reasons(body) if lane == "fix" else []
    declined = declined_reasons(body) if lane == "glowup" else {}
    banked = {str(b.get("id")): b for b in ((backlog or {}).get("banked") or [])
              if isinstance(b, dict)}
    banked.update({str(s.get("id")): s for s in
                   (((backlog or {}).get("reconciled") or {}).get("fresh_stubs") or [])
                   if isinstance(s, dict)})
    for f in findings:
        label = str(f.get("label") or "")
        f["finding"] = label
        status, reason = ("applied" if f.get("applied") else "deferred"), ""
        if lane == "fix" and not f.get("applied"):
            reason = _reason_for(label, pairs)
        elif lane == "glowup" and not f.get("applied"):
            bid = f.get("_backlog_id")
            item = banked.get(str(bid)) if bid else None
            if item is None:
                # Not resolved by id: find the banked item by label prefix.
                item = next((b for b in banked.values()
                             if str(b.get("text") or "").startswith(label)
                             and b.get("source") in ("findings-record", "fresh-verdict")), None)
            if item is not None:
                if item.get("pre_declined"):
                    status, reason = "superseded", str(item["pre_declined"])
                else:
                    reason = declined.get(str(item.get("id")), "")
        f.pop("_backlog_id", None)
        f["prior_disposition"] = {"status": status, "reason": reason, "lane": lane}
    return findings


def _fix_scope():
    """verify-fix-scope.py by path — the publish gate's line-range parser and
    tolerances. Matching a finding to an applied fix is the SAME question the
    gate already answers (does this edit fall inside a recorded finding?), so
    it gets the same answer here rather than a second, looser opinion."""
    spec = importlib.util.spec_from_file_location(
        "verify_fix_scope", HERE / "verify-fix-scope.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def mark_applied(findings: list[dict], verdict: dict | None) -> list[dict]:
    """Flag each finding the verdict's `applied[]` claims to have fixed.

    Matched on LINE OVERLAP, not on text. `applied[].source` is a free-text
    pointer the model writes ("Claim (c28)", "vale L48"), so substring
    matching on it is a guess — "vale" alone would swallow every Vale finding
    on the page, and a pointer phrased differently would match nothing.
    `applied[].lines` is structured, is already validated by the publish gate
    (an edit outside a recorded finding fails the build), and carries PRE-FIX
    numbering, which is exactly the numbering the artifacts use.

    Tolerances come from verify-fix-scope.py so the two cannot disagree about
    what "inside a finding" means: ±TOL_DEFAULT for claims/vale/frontmatter,
    ±TOL_READTHROUGH for readthrough, whose repairs legitimately move lines
    around more.

    A finding with no line range (frontmatter alias collisions) can never be
    matched positionally, so it falls back to the text pointer — narrow enough
    to be safe because those labels carry the alias itself.
    """
    fs = _fix_scope()
    entries = [a for a in ((verdict or {}).get("applied") or []) if isinstance(a, dict)]
    spans: list[tuple[int, int]] = []
    for a in entries:
        lines = a.get("lines")
        if isinstance(lines, list) and len(lines) == 2 and all(
                isinstance(n, int) and n > 0 for n in lines):
            spans.append((min(lines), max(lines)))
    pointers = [str(a.get("source") or "").strip().lower() for a in entries]

    out = []
    for i, f in enumerate(findings):
        rng = fs.parse_line_range(str(f.get("line_range") or ""))
        if rng:
            tol = (fs.TOL_READTHROUGH if f.get("category") == "readthrough"
                   else fs.TOL_DEFAULT)
            lo, hi = max(1, rng[0] - tol), rng[1] + tol
            hit = any(s <= hi and e >= lo for s, e in spans)
        else:
            label = str(f.get("label") or "").strip().lower()
            hit = any(p and label and (p in label or label[:60] in p) for p in pointers)
        out.append({
            "id": f"f{i + 1}",
            "label": f.get("label", ""),
            "source": f.get("source", ""),
            "detail": f.get("detail", ""),
            "category": f.get("category", ""),
            "line_range": f.get("line_range", ""),
            "fix_candidate": bool(f.get("fix")),
            "applied": hit,
        })
    return out


def head_commit(repo_root: Path) -> str:
    try:
        r = subprocess.run(["git", "-C", str(repo_root), "rev-parse", "HEAD"],
                           capture_output=True, text=True, check=False)
        return r.stdout.strip() if r.returncode == 0 else ""
    except OSError:
        return ""


def mark_from_backlog(findings: list[dict], verdict: dict | None,
                      backlog: dict | None) -> list[dict] | None:
    """Flag findings from a GLOW-UP verdict's own disposition, or None.

    A glow-up carries no `applied[]` — the glow-up scope gate replaces the
    per-hunk check, so there is no line-range attribution to match on, and
    `mark_applied` therefore flags every finding deferred. That is not a
    degraded record, it is a WRONG one: the items the glow-up just executed
    get filed as outstanding, and `build-glowup-backlog.banked_from_findings`
    banks exactly the `applied: false` items, so the next run re-proposes
    finished work. Re-proposing finished work is what erodes trust in the lane.

    The disposition already exists — the model writes the Backlog executed /
    Backlog declined tables from `.glowup-backlog.json` — so the sentinel
    reports those id lists rather than anything being inferred here.

    The ids locate the backlog ITEM; the finding it refers to is then resolved
    by CONTENT. Finding ids are positional (`f1`, `f2`, ... in collect() order)
    and a backlog id encodes the id from the PREVIOUS run's record, built over
    separately collected artifacts. Any shift between the two — an intervening
    fix-lane review applying a fix and removing its finding, which is the
    expected case between glow-ups — renumbers everything after it, so old `f2`
    is new `f1` and an ordinal map would mark the WRONG finding applied. That
    is this function's own failure mode pointed backwards: the executed item
    gets re-banked and an untouched one drops out of the backlog for good.
    `banked_from_findings` builds each item's text as `label` (plus ` — detail`),
    so the label is a prefix of the text and the match is exact, not fuzzy.

    An id that resolves to no finding leaves everything deferred and warns —
    unless NONE of the ids that should have resolved did, which is the same
    information state as a sentinel carrying no lists and takes the same exit.
    That direction is deliberate: re-proposing finished work is irritating and
    visible, while marking the wrong item applied loses real work silently.

    Returns None when the disposition is unknown — the sentinel carries neither
    list, or no executed id that should map to a finding here did — so the
    caller can decline to write rather than write an all-false record. Ids
    naming pr-body items don't count towards that: they have no counterpart on
    this record and are expected to resolve to nothing.
    """
    v = verdict or {}
    if "executed_ids" not in v and "declined_ids" not in v:
        # Every None return from here warns first — the caller's log line defers
        # to that, so a silent exit leaves it pointing at nothing.
        warn("glow-up verdict carries neither executed_ids nor declined_ids; "
             "disposition unknown")
        return None
    executed = {str(i) for i in (v.get("executed_ids") or [])}
    banked = {str(b.get("id")): b for b in ((backlog or {}).get("banked") or [])
              if isinstance(b, dict)}

    labels = [str(f.get("label") or "").strip() for f in findings]
    applied_idx: set[int] = set()
    marked_by: dict[int, str] = {}
    # Executed ids that SHOULD have resolved to a finding on this record —
    # everything except the pr-body items, which are prose with no counterpart
    # here and are expected to resolve to nothing. Only these can tell a total
    # resolution failure from a glow-up that legitimately executed prose.
    resolvable: set[str] = set()
    for bid in sorted(executed):
        item = banked.get(bid)
        if item is None:
            # Unknown id: either the backlog is missing entirely or the sentinel
            # named something that was never banked. Both should have resolved.
            resolvable.add(bid)
            warn(f"executed id {bid!r} is not in the backlog; leaving the "
                 "corresponding finding deferred")
            continue
        # A pr-body-sourced item is prose recovered from a PR description and
        # has no counterpart on this record, so it can never mark a finding.
        # That gap is exactly what the structured record exists to close.
        # A `fresh-verdict` stub is this run's own contradicted/mismatch
        # verdict, composed with collect()'s label as its prefix, so it
        # resolves the same way.
        if item.get("source") not in ("findings-record", "fresh-verdict"):
            continue
        resolvable.add(bid)
        text = str(item.get("text") or "").strip()
        hit = next((i for i, lab in enumerate(labels)
                    if lab and i not in applied_idx and text.startswith(lab)), None)
        if hit is None:
            warn(f"executed backlog item {bid!r} matches no finding on this page "
                 f"({text[:80]!r}); leaving it deferred rather than marking one "
                 "by position")
            continue
        applied_idx.add(hit)
        marked_by[hit] = bid

    # The sentinel named executed items and not one of them resolved — the
    # backlog snapshot is missing or unreadable, or every label has drifted.
    # That is the same information state as a sentinel carrying no lists at
    # all, so it takes the same exit: writing the all-False record this would
    # otherwise produce re-banks everything the glow-up just finished, which
    # is the failure the whole function exists to prevent. A PARTIAL resolve
    # still writes — those findings are genuinely known, and the unresolved
    # ones already warned above.
    if resolvable and not applied_idx:
        warn(f"none of the {len(resolvable)} executed id(s) that should map to a "
             "finding on this record resolved to one; "
             "skipping the write rather than recording this glow-up's own work "
             "as still outstanding")
        return None

    # Declined ids resolve the same way, so a declined finding can carry its
    # row's reason (and a pre-declined one its `superseded` status).
    declined_by: dict[int, str] = {}
    for bid in sorted({str(i) for i in (v.get("declined_ids") or [])}):
        item = banked.get(bid)
        if item is None or item.get("source") not in ("findings-record", "fresh-verdict"):
            continue
        text = str(item.get("text") or "").strip()
        hit = next((i for i, lab in enumerate(labels)
                    if lab and i not in applied_idx and i not in declined_by
                    and text.startswith(lab)), None)
        if hit is not None:
            declined_by[hit] = bid

    out = []
    for i, f in enumerate(findings):
        rec = {
            "id": f"f{i + 1}",
            "label": f.get("label", ""),
            "source": f.get("source", ""),
            "detail": f.get("detail", ""),
            "category": f.get("category", ""),
            "line_range": f.get("line_range", ""),
            "fix_candidate": bool(f.get("fix")),
            "applied": i in applied_idx,
        }
        bid = marked_by.get(i) or declined_by.get(i)
        if bid:
            rec["_backlog_id"] = bid
        out.append(rec)
    return out


def build(queue: dict, verdict: dict | None, artifacts: dict,
          repo_root: Path, backlog: dict | None = None,
          pr_body: str | None = None) -> dict | None:
    articles = queue.get("articles") or []
    if not articles:
        warn("queue has no article; nothing to record")
        return None
    art = articles[0]
    cpb = _compose()
    findings, _errors = cpb.collect(
        artifacts.get("verified"), artifacts.get("vale"),
        artifacts.get("readthrough"), artifacts.get("frontmatter"))
    if (verdict or {}).get("verdict") == "glowup":
        marked = mark_from_backlog(findings, verdict, backlog)
        if marked is None:
            # Writing an all-false record here would file the work the glow-up
            # just did as still outstanding. Skipping leaves the previous
            # record standing, which is stale but true; the next fix-lane
            # review refreshes it from its own artifacts.
            # mark_from_backlog already logged WHICH of its two unknown-
            # disposition states this was; naming one of them here contradicted
            # the other and sent debugging at the model's sentinel when the real
            # cause was a missing backlog snapshot.
            warn("glow-up disposition unknown (see above); skipping the findings "
                 "write rather than recording every finding as deferred")
            return None
        lane = "glowup"
    else:
        marked = mark_applied(findings, verdict)
        lane = "fix"
    marked = attach_dispositions(marked, lane, pr_body, backlog)
    n_applied = sum(1 for f in marked if f["applied"])
    n_super = sum(1 for f in marked if f["prior_disposition"]["status"] == "superseded")
    return {
        "schema_version": SCHEMA_VERSION,
        "slug": art.get("slug", ""),
        "path": art.get("path", ""),
        "reviewed_at": datetime.now(timezone.utc).date().isoformat(),
        "commit": head_commit(repo_root),
        "verdict": (verdict or {}).get("verdict"),
        "counts": {"total": len(marked), "applied": n_applied,
                   "deferred": len(marked) - n_applied - n_super,
                   "superseded": n_super},
        "findings": marked,
    }


def upload(record: dict, uri: str) -> None:
    key = f"{uri.rstrip('/')}/{record['slug']}.json"
    body = json.dumps(record, indent=2) + "\n"
    proc = subprocess.run(["aws", "s3", "cp", "-", key, "--quiet"],
                          input=body, text=True, capture_output=True)
    if proc.returncode != 0:
        warn(f"upload to {key} failed: {proc.stderr.strip()[:200]}")
    else:
        log(f"uploaded findings record to {key}")


def self_test() -> int:
    passes, failures = 0, []

    def check(label, ok):
        nonlocal passes
        if ok:
            passes += 1
            print(f"  ok: {label}")
        else:
            failures.append(label)
            print(f"  FAIL: {label}")

    F = [
        {"label": "Claim (c28, L89): version is 3.157.0", "source": "gh release view",
         "category": "claim", "line_range": "L89", "fix": True},
        {"label": "Vale filler (L48): Don't start with 'There are'.", "source": "vale",
         "category": "vale", "line_range": "L48", "fix": False},
        {"label": "Vale wordiness (L200): 'all of' is too wordy.", "source": "vale",
         "category": "vale", "line_range": "L200", "fix": False},
        {"label": "Readthrough missing-step (L636-640)", "source": "readthrough pass",
         "category": "readthrough", "line_range": "L636-640", "fix": True},
        {"label": "Frontmatter alias collision: `/docs/old-path/`",
         "source": "`.frontmatter-validation.json`", "category": "frontmatter",
         "line_range": "", "fix": True},
    ]

    def applied(*entries):
        return [f["applied"] for f in mark_applied(F, {"applied": list(entries)})]

    check("an applied fix marks the finding at those lines",
          applied({"category": "claim", "lines": [89, 89], "source": "c28"})
          == [True, False, False, False, False])
    check("nothing applied -> everything deferred", applied() == [False] * 5)
    check("a None verdict is not fatal",
          [f["applied"] for f in mark_applied(F, None)] == [False] * 5)

    # THE bug the first cut of this had: `applied[].source` is free text, so
    # substring matching on it let one Vale fix swallow every Vale finding on
    # the page. Line overlap keeps them distinct.
    check("one Vale fix does not swallow the other Vale findings",
          applied({"category": "vale", "lines": [48, 48], "source": "vale"})
          == [False, True, False, False, False])

    check("the gate's tolerance applies (L91 is within +/-2 of L89)",
          applied({"category": "claim", "lines": [91, 91], "source": "x"})[0] is True)
    check("outside the tolerance does not match (L95 is not)",
          applied({"category": "claim", "lines": [95, 95], "source": "x"})[0] is False)
    check("readthrough gets the wider tolerance it needs (L644 vs L636-640)",
          applied({"category": "readthrough", "lines": [644, 644], "source": "x"})[3] is True)
    check("a span overlapping the range at all counts",
          applied({"category": "claim", "lines": [1, 500], "source": "x"})[0] is True)

    # No line range to match on: fall back to the pointer, which for these
    # carries the alias itself and so is specific enough.
    check("a rangeless finding falls back to its text pointer",
          applied({"category": "frontmatter", "lines": [1, 1],
                   "source": "Frontmatter alias collision: `/docs/old-path/`"})[4] is True)
    check("a malformed applied entry is ignored, not crashed on",
          applied({"category": "claim", "lines": "nope", "source": ""}) == [False] * 5)
    check("ids are stable and 1-based",
          [f["id"] for f in mark_applied(F, None)] == ["f1", "f2", "f3", "f4", "f5"])
    check("fix_candidate and location survive onto the record",
          mark_applied(F, None)[3]["line_range"] == "L636-640"
          and mark_applied(F, None)[3]["category"] == "readthrough")
    check("deferred findings are recorded, not dropped",
          len(mark_applied(F, None)) == 5)

    # --- glow-up disposition -------------------------------------------
    # A glow-up has no applied[], so mark_applied would file everything it
    # just executed as still outstanding, and the next glow-up would
    # re-propose finished work.
    # Item text is what banked_from_findings() actually writes: the finding's
    # label, plus " — detail" when there is one. Anything else here would be
    # testing a shape the lane never produces.
    BACKLOG = {"banked": [
        {"id": "findings-f2", "source": "findings-record",
         "text": "Vale filler (L48): Don't start with 'There are'."},
        {"id": "findings-f3", "source": "findings-record",
         "text": "Vale wordiness (L200): 'all of' is too wordy. — editorial polish"},
        {"id": "pr19885-findings-1", "source": "pr-body", "text": "Claim (c17) — unverifiable"},
    ]}

    def glow(**kw):
        v = {"verdict": "glowup", "fixes": 1, "skipped_findings": 1, **kw}
        marked = mark_from_backlog(F, v, BACKLOG)
        return None if marked is None else [f["applied"] for f in marked]

    check("the old line-overlap path would have filed executed work as deferred",
          [f["applied"] for f in mark_applied(F, {"verdict": "glowup", "fixes": 1})]
          == [False] * 5)
    check("executed backlog ids mark their findings applied",
          glow(executed_ids=["findings-f2"], declined_ids=["findings-f3"])
          == [False, True, False, False, False])
    check("declined backlog ids stay deferred",
          glow(executed_ids=[], declined_ids=["findings-f2", "findings-f3"])
          == [False] * 5)
    check("several executed ids all land",
          glow(executed_ids=["findings-f2", "findings-f3"])
          == [False, True, True, False, False])
    check("a sentinel with neither list records nothing at all",
          glow() is None and mark_from_backlog(F, {"verdict": "glowup"}, BACKLOG) is None)
    check("an empty backlog is still a disposition, not a missing one",
          glow(executed_ids=[], declined_ids=[]) == [False] * 5)
    check("executed ids that resolve to nothing at all skip the write",
          glow(executed_ids=["findings-f99", "nonsense"]) is None)
    check("a pr-body-sourced backlog item cannot mark a record finding",
          glow(executed_ids=["pr19885-findings-1"]) == [False] * 5)
    # Without the backlog there is nothing to resolve `findings-f2` AGAINST, and
    # the only way to honour it would be to trust the ordinal — the guess this
    # function stopped making. Writing the all-False record that falls out of
    # that would re-bank the work the glow-up just did, so it takes the same
    # exit as a sentinel carrying no lists at all.
    check("a missing backlog skips the write rather than guessing by position",
          mark_from_backlog(F, {"verdict": "glowup",
                                "executed_ids": ["findings-f2"]}, None) is None)
    check("...and so does an executed set where nothing resolves",
          mark_from_backlog(F, {"verdict": "glowup",
                                "executed_ids": ["findings-f404"]}, BACKLOG) is None)

    # build() logs "disposition unknown (see above)" and defers to this function
    # for WHICH state it was, so a None return that doesn't warn leaves the
    # operator reading a pointer to nothing.
    def none_path_warns(verdict):
        buf = io.StringIO()
        with contextlib.redirect_stderr(buf):
            result = mark_from_backlog(F, verdict, BACKLOG)
        return result is None and "::warning::" in buf.getvalue()

    check("every None return warns first — no id lists at all",
          none_path_warns({"verdict": "glowup"}))
    check("every None return warns first — nothing resolved",
          none_path_warns({"verdict": "glowup", "executed_ids": ["findings-f404"]}))
    check("a PARTIAL resolve still writes — those findings are genuinely known",
          [f["applied"] for f in
           mark_from_backlog(F, {"verdict": "glowup",
                                 "executed_ids": ["findings-f2", "findings-f404"]},
                             BACKLOG)] == [False, True, False, False, False])
    check("declining everything still writes a record, executing nothing",
          [f["applied"] for f in
           mark_from_backlog(F, {"verdict": "glowup", "executed_ids": [],
                                 "declined_ids": ["findings-f2"]}, BACKLOG)]
          == [False] * 5)
    check("the record shape is identical on both paths",
          set(mark_from_backlog(F, {"verdict": "glowup", "executed_ids": []},
                                BACKLOG)[0]) == set(mark_applied(F, None)[0]))
    check("a fix verdict still uses line overlap, untouched",
          applied({"category": "vale", "lines": [48, 48], "source": "vale"})
          == [False, True, False, False, False])

    # Finding ids are positional and the backlog's ids come from the PREVIOUS
    # run's record. If a fix-lane review removed an earlier finding in between,
    # old f2 is new f1 — and an ordinal map would mark the wrong item applied,
    # dropping real work out of the backlog for good.
    SHIFTED = F[1:]  # the intervening review fixed and removed old f1
    shifted_marks = [f["applied"] for f in
                     mark_from_backlog(SHIFTED, {"verdict": "glowup",
                                                 "executed_ids": ["findings-f2"]},
                                       BACKLOG)]
    check("a renumbered finding set still marks the right finding",
          shifted_marks == [True, False, False, False])
    check("and it is the one whose label the backlog item names",
          mark_from_backlog(SHIFTED, {"verdict": "glowup",
                                      "executed_ids": ["findings-f2"]},
                            BACKLOG)[0]["label"].startswith("Vale filler (L48)"))
    check("an item whose only finding is gone skips the write",
          mark_from_backlog(F[3:], {"verdict": "glowup",
                                    "executed_ids": ["findings-f2"]}, BACKLOG) is None)
    check("an executed id absent from the backlog is not silently ignored",
          glow(executed_ids=["findings-f404"]) is None)
    check("a pr-body item alongside a resolving one does not block the write",
          glow(executed_ids=["findings-f2", "pr19885-findings-1"])
          == [False, True, False, False, False])
    check("the detail suffix does not break the label match",
          glow(executed_ids=["findings-f3"])
          == [False, False, True, False, False])
    check("two executed ids cannot both claim the same finding",
          sum(mark_from_backlog(
              F, {"verdict": "glowup",
                  "executed_ids": ["findings-f2", "findings-dup"]},
              {"banked": BACKLOG["banked"] + [
                  {"id": "findings-dup", "source": "findings-record",
                   "text": "Vale filler (L48): Don't start with 'There are'."}]},
          )[i]["applied"] for i in range(5)) == 1)

    print(f"\n{passes} passed, {len(failures)} failed")
    return 1 if failures else 0


def main() -> int:
    p = argparse.ArgumentParser(description="Persist a page's review findings as JSON.")
    p.add_argument("--queue", default=".content-review-queue.json")
    p.add_argument("--verdict", default=".content-review-verdict.json")
    p.add_argument("--verified-claims", default=".verified-claims.json")
    p.add_argument("--vale-findings", default=".vale-findings.json")
    p.add_argument("--readthrough", default=".readthrough-findings.json")
    p.add_argument("--frontmatter", default=".frontmatter-validation.json")
    p.add_argument("--backlog", default="",
                   help="the glow-up work list (.glowup-backlog.json); supplies the "
                        "id -> finding mapping for a glow-up verdict's disposition")
    p.add_argument("--pr-body", default="",
                   help="the PR body draft; supplies each deferred finding's one-line "
                        "reason (fix lane: Findings not applied; glow-up: Backlog declined)")
    p.add_argument("--repo-root", default=".")
    p.add_argument("--out", default=".page-findings.json")
    p.add_argument("--uri", default="", help="s3://bucket/findings/ (skipped when empty)")
    p.add_argument("--self-test", action="store_true")
    args = p.parse_args()
    if args.self_test:
        return self_test()

    queue = read_json(Path(args.queue))
    if not isinstance(queue, dict):
        warn(f"{args.queue} missing or unreadable; nothing recorded")
        return 0
    record = build(
        queue, read_json(Path(args.verdict)),
        {"verified": read_json(Path(args.verified_claims)),
         "vale": read_json(Path(args.vale_findings)),
         "readthrough": read_json(Path(args.readthrough)),
         "frontmatter": read_json(Path(args.frontmatter))},
        Path(args.repo_root),
        backlog=read_json(Path(args.backlog)) if args.backlog else None,
        pr_body=(Path(args.pr_body).read_text() if args.pr_body and Path(args.pr_body).is_file()
                 else None))
    if record is None:
        return 0
    Path(args.out).write_text(json.dumps(record, indent=2) + "\n")
    c = record["counts"]
    log(f"slug={record['slug']} findings={c['total']} "
        f"applied={c['applied']} deferred={c['deferred']} "
        f"superseded={c['superseded']} -> {args.out}")
    if args.uri:
        upload(record, args.uri)
    return 0


if __name__ == "__main__":
    sys.exit(main())
