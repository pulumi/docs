#!/usr/bin/env python3
"""Tests for compose-pr-body.py (assemble-then-judge PR-body draft)."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "compose_pr_body", Path(__file__).resolve().parent / "compose-pr-body.py"
)
c = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(c)

failures: list[str] = []


def check(name: str, cond: bool) -> None:
    if cond:
        print(f"ok: {name}")
    else:
        failures.append(name)
        print(f"FAIL: {name}", file=sys.stderr)


QUEUE = {
    "traffic": {"available": True, "period": "2026-06", "source": "CLICKSTREAM.FCT_PAGEVIEWS"},
    "articles": [{
        "path": "content/docs/iac/concepts/functions/resource-methods.md",
        "url": "/docs/iac/concepts/functions/resource-methods/",
        "lane": "priority", "tier": 1, "no_retire": True,
        "monthly_visits": 384, "last_reviewed": None, "attempts": 0, "score": 278.3,
    }],
}

# A contradicted high-confidence claim (-> fix), an unverifiable claim (-> defer).
VERIFIED = {
    "verdicts": [
        {"claim_id": "c3", "line_range": "L34", "text": "C# signature GetKubeconfig(Cluster.GetKubeconfigArgs? args)",
         "verdict": "contradicted", "confidence": "high",
         "evidence": "dotnet SDK defines flat ClusterGetKubeconfigArgs", "source": "pulumi/pulumi-eks: sdk/dotnet/Cluster.cs"},
        {"claim_id": "c5", "line_range": "L52", "text": "Python signature includes profile_name",
         "verdict": "unverifiable", "confidence": "low",
         "evidence": "verifier did not converge", "source": "(no source pointer)"},
        {"claim_id": "c2", "text": "TS signature", "verdict": "verified", "confidence": "high",
         "evidence": "matches", "source": "sdk/nodejs/cluster.ts"},
    ],
}
# One mechanical Vale (difficulty qualifier -> fix), one style (passive -> defer).
VALE = [
    {"file": "x.md", "line": 67, "rule": "Pulumi.Difficulty", "category": "difficulty qualifier",
     "severity": "warning", "message": "'Simple' judges difficulty for the reader"},
    {"file": "x.md", "line": 12, "rule": "Google.Passive", "category": "passive voice",
     "severity": "suggestion", "message": "consider active voice"},
]
# One local_repair (-> fix), one reconception (-> defer).
READTHROUGH = {
    "ran": True,
    "findings": [
        {"line_range": "L40", "failure_mode": "missing-step", "anchor_quote": "run pulumi up",
         "fix_class": "local_repair", "proposed_fix": "add a login step before L40"},
        {"line_range": "L1-90", "failure_mode": "purpose-mismatch", "anchor_quote": "Configure access",
         "fix_class": "reconception", "proposed_fix": "split architecture half into its own page"},
    ],
}
FRONTMATTER = {"files": [{"path": "x.md",
    "alias_collisions": [{"alias": "/docs/dupe/"}],
    "menu_parents": [{"menu_name": "concepts", "parent": "functions", "parent_exists_in_menu": False}]}]}

out = c.compose(QUEUE, VERIFIED, VALE, READTHROUGH, FRONTMATTER)

# All six required sections present (record-review's check_pr_body expects these).
for sec in ["Why this page", "Fixes applied", "Findings not applied",
            "Screenshot check", "Rendered content", "Verification"]:
    check(f"section present: {sec}", f"## {sec}" in out)

# Auto-merge notice is a prominent IMPORTANT alert at the very top.
check("auto-merge notice present", "> [!IMPORTANT]" in out and "auto-merge" in out.lower())
check("auto-merge notice is at the top", out.lstrip().startswith("> [!IMPORTANT]"))
check("auto-merge notice warns approving merges", "approving this pr will merge it" in out.lower())

# Provenance composed (real visits, not narrated).
check("provenance shows real visits", "384 monthly visits" in out)

# High-confidence findings land as fix stubs.
check("contradicted high-confidence claim -> fix row", "c3" in out.split("## Findings not applied")[0])
check("mechanical Vale -> fix row", "difficulty qualifier" in out.split("## Findings not applied")[0])
check("local_repair readthrough -> fix row", "missing-step" in out.split("## Findings not applied")[0])
check("alias collision -> fix row", "alias collision" in out.split("## Findings not applied")[0])

# Judgment-level findings land as deferral stubs.
deferral_block = out.split("## Findings not applied")[1].split("## Screenshot")[0]
check("unverifiable claim -> deferral", "c5" in deferral_block)
check("style Vale -> deferral", "passive voice" in deferral_block)
check("reconception readthrough -> deferral", "purpose-mismatch" in deferral_block)
check("legacy menu parent -> deferral", "menu parent" in deferral_block)

# TODO markers for the model to fill; lint placeholder for the gate to stamp.
check("fix rows carry <TODO>", "<TODO: correction" in out)
check("deferrals carry <TODO>", "<TODO: why judgment-level>" in deferral_block)
check("screenshot/rendered are <TODO>", out.count("<TODO") >= 4)
check("lint result is a stamped placeholder", c.LINT_PLACEHOLDER in out)
# The "do not edit" hint must live in an HTML comment, not leak to readers, and
# the label is `make lint` only (build isn't stamped here).
check("no reader-facing 'do not edit' instruction", "do not edit this line" not in out)
lint_line = next(l for l in out.splitlines() if c.LINT_PLACEHOLDER in l)
check("lint hint rides in an HTML comment", "<!--" in lint_line.split(c.LINT_PLACEHOLDER, 1)[1])
check("lint label is make-lint-only (no make build)", "make build`:" not in lint_line)

# Verification inventory is deterministic.
check("inventory counts verdicts", "3 verdict(s); 1 contradicted/mismatch, 1 unverifiable" in out)

# Graceful degradation: all artifacts missing still yields a valid full draft.
bare = c.compose(QUEUE, None, None, None, None)
for sec in ["Why this page", "Fixes applied", "Findings not applied",
            "Screenshot check", "Rendered content", "Verification"]:
    check(f"degraded draft still has {sec}", f"## {sec}" in bare)
check("degraded fixes section notes no stubs", "No high-confidence fix candidates" in bare)
check("degraded inventory marks missing", ".verified-claims.json`: missing" in bare)

# Errored artifact is surfaced in Verification.
errd = c.compose(QUEUE, {"verdicts": [], "errors": ["verify-claims failed"]}, [], {"ran": False, "findings": []}, {})
check("errored artifact surfaced", "Artifacts that failed" in errd and "verified-claims" in errd)


# ---- gated screenshot / rendered sections -----------------------------------
#
# When the source provably has nothing to look at, the composer fills these
# sections deterministically (no <TODO>) so the worker skips the pass + build.

def _between(text: str, start: str, end: str) -> str:
    return text.split(start, 1)[1].split(end, 1)[0]

# Skip case: no images, only render-safe chrome.
skip = c.compose(QUEUE, None, None, None, None,
                 {"has_images": False, "needs_render_pass": False,
                  "shortcodes": ["notes"], "nonchrome_shortcodes": [], "image_count": 0})
shot_skip = _between(skip, "## Screenshot check", "## Rendered content")
rend_skip = _between(skip, "## Rendered content", "## Verification")
check("gated screenshot states No images", "No images." in shot_skip)
check("gated screenshot carries no <TODO>", "<TODO" not in shot_skip)
check("gated rendered states Skipped", "Skipped —" in rend_skip)
check("gated rendered names the safe shortcode", "`notes`" in rend_skip)
check("gated rendered carries no <TODO>", "<TODO" not in rend_skip)

# Run case: an image and a content-bearing shortcode -> both passes still TODO.
run = c.compose(QUEUE, None, None, None, None,
                {"has_images": True, "needs_render_pass": True,
                 "shortcodes": ["chooser", "langfile"], "nonchrome_shortcodes": ["langfile"],
                 "image_count": 2})
shot_run = _between(run, "## Screenshot check", "## Rendered content")
rend_run = _between(run, "## Rendered content", "## Verification")
check("ungated screenshot keeps <TODO>", "<TODO" in shot_run)
check("ungated screenshot hints image count", "2 image reference(s)" in shot_run)
check("ungated rendered keeps <TODO>", "<TODO" in rend_run)
check("ungated rendered names the trigger shortcode", "`langfile`" in rend_run)

# Default-safe: no gate info -> both passes run (TODO), nothing silently skipped.
nogate = c.compose(QUEUE, None, None, None, None, None)
check("no gate -> screenshot TODO", "<TODO" in _between(nogate, "## Screenshot check", "## Rendered content"))
check("no gate -> rendered TODO", "<TODO" in _between(nogate, "## Rendered content", "## Verification"))


# ---- flag-only low-CTR pathway ------------------------------------------------
#
# A low_ctr_flag on the queue entry pre-stubs exactly one "Search opportunity"
# deferral (fix: False, reason pre-composed) — never a fix row.

FLAGGED_QUEUE = {
    "traffic": {"available": True, "period": "2026-06"},
    "reader_signals": {
        "available": True,
        "gsc": {"available": True, "median_ctr": 0.031, "max_impressions": 88012},
        "feedback": {"available": True},
    },
    "articles": [{
        **QUEUE["articles"][0],
        "signals": {
            "gsc": {"impressions": 15234, "ctr": 0.0205, "opportunity": 0.41,
                    "multiplier": 1.1025, "low_ctr_flag": True},
            "feedback": {"yes": 4, "no": 9, "neg_rate": 0.6923, "multiplier": 1.27},
        },
    }],
}
flagged = c.compose(FLAGGED_QUEUE, None, None, None, None)
flag_fixes = _between(flagged, "## Fixes applied", "## Findings not applied")
flag_defer = _between(flagged, "## Findings not applied", "## Screenshot check")
check("low-CTR flag -> exactly one Search opportunity deferral",
      flag_defer.count("Search opportunity") == 1)
check("low-CTR deferral never lands as a fix row", "Search opportunity" not in flag_fixes)
check("low-CTR deferral carries the figures",
      "15,234 impressions at 2.05% CTR vs. corpus median 3.10%" in flag_defer)
check("low-CTR deferral reason pre-composed (no TODO)",
      "flag-only by design" in flag_defer and "/seo-analyze" in flag_defer)
check("provenance carries the Search line", "**Search:** 15,234 impressions" in flagged)

# No flag (or no signals at all) -> no Search opportunity row anywhere.
check("unflagged queue has no Search opportunity row", "Search opportunity" not in out)
unflagged = c.compose({**FLAGGED_QUEUE, "articles": [{
    **FLAGGED_QUEUE["articles"][0],
    "signals": {"gsc": {"impressions": 15234, "ctr": 0.05, "opportunity": 0.0,
                        "multiplier": 1.0, "low_ctr_flag": False}, "feedback": None},
}]}, None, None, None, None)
check("healthy-CTR queue has no Search opportunity row", "Search opportunity" not in unflagged)

# Notice swap (publish-job mode for judgment-class PRs): replaces the
# composed auto-merge notice, idempotent, and no-ops safely on odd bodies.
import tempfile

with tempfile.TemporaryDirectory() as _td:
    _body = Path(_td) / "body.md"
    _body.write_text(out)
    check("composed body carries the auto-merge notice", c.AUTOMERGE_NOTICE in out)
    c.replace_notice(_body, "judgment")
    swapped = _body.read_text()
    check("swap replaces the auto-merge notice", c.AUTOMERGE_NOTICE not in swapped)
    check("swap inserts the judgment notice", c.JUDGMENT_NOTICE in swapped)
    check("swap keeps the rest of the body", "## Why this page" in swapped)
    c.replace_notice(_body, "judgment")
    check("swap is idempotent", _body.read_text() == swapped)
    _noticeless = Path(_td) / "noticeless.md"
    _noticeless.write_text("## Why this page\n")
    c.replace_notice(_noticeless, "judgment")
    check("swap no-ops without failing when no notice is present",
          _noticeless.read_text() == "## Why this page\n")

# Glow-up body: banked backlog pre-stubbed, taxonomy sweep stubbed, notice is
# the human-review one, and the section headings match record-review.py's
# MODE_PR_SECTIONS["glowup"] exactly (the triplication guard).
BACKLOG = {
    "banked": [
        {"id": "pr123-findings-1", "section": "Findings not applied",
         "source_pr": 123, "text": "| claim | L42 | needs interpretation |"},
        {"id": "pr123-findings-2", "section": "Findings not applied",
         "source_pr": 123, "text": "Consider restructuring the intro"},
    ],
    "notes": [],
}
gout = c.compose_glowup(QUEUE, BACKLOG, None, None, None, None)
check("glowup body opens with the human-review notice",
      gout.startswith(c.HUMAN_REVIEW_NOTICE))
check("glowup body never carries the auto-merge notice", c.AUTOMERGE_NOTICE not in gout)
check("banked findings pre-stubbed with source PR",
      "needs interpretation" in gout and "#123" in gout)
check("taxonomy sweep stubbed per category",
      all(f"**{cat}**" in gout for cat in c.GLOWUP_TAXONOMY))
gempty = c.compose_glowup(QUEUE, {"banked": [], "degraded": False,
                                  "notes": ["no review PR has ever used "
                                            "content-review/docs-x; run the "
                                            "taxonomy-only sweep"]},
                          None, None, None, None)
check("a genuinely empty backlog still reads as taxonomy-only",
      "taxonomy-only" in gempty and "WARNING" not in gempty)

# #20984 shipped "No banked findings reachable ... taxonomy-only glow-up" for a
# page whose ledger recorded 17 deferred findings — which reads as "this page
# had nothing outstanding", the opposite of true.
gdeg = c.compose_glowup(QUEUE, {
    "banked": [], "degraded": True, "skipped_findings": 17, "clarity_flag": True,
    "recovery": {"state": "no_prior_prs",
                 "heads_queried": ["content-review/docs-x",
                                   "content-review/retire-docs-x",
                                   "content-review/glowup-docs-x"]},
    "notes": ["no review PR has ever used content-review/docs-x; "
              "run the taxonomy-only sweep"]}, None, None, None, None)
check("#20984: a failed recovery renders a warning, not 'nothing to do'",
      "[!WARNING]" in gdeg and "Backlog recovery failed" in gdeg)
check("#20984: the warning names the count the ledger recorded",
      "17 deferred finding(s)" in gdeg and "clarity flag" in gdeg)
check("#20984: it tells the reader not to read this as a clean page",
      "do not treat this as a clean page" in gdeg)
check("#20984: the old misleading sentence is gone",
      "No banked findings reachable" not in gdeg)
check("a failed recovery shows its work",
      all(h in gdeg for h in ("content-review/docs-x",
                              "content-review/glowup-docs-x")))

gdecl = c.compose_glowup(QUEUE, {"banked": [
    {"id": "pr20984-backlog-1", "section": "Backlog declined", "source_pr": 20984,
     "source": "glowup-declined", "declined_by_pr": 20984,
     "text": "**Claim (c9)** — needs an SME"}], "degraded": False, "notes": []},
    None, None, None, None)
check("previously-declined rows are visibly marked as such",
      "#20984 (declined)" in gdecl and "needs an SME" in gdecl)
check("a record-sourced row with no PR does not render '#None'",
      "#None" not in c.compose_glowup(QUEUE, {"banked": [
          {"id": "findings-f2", "section": "Findings not applied", "source_pr": None,
           "source": "findings-record", "text": "Vale filler (L48)"}],
          "degraded": False, "notes": []}, None, None, None, None))

_rr_spec = importlib.util.spec_from_file_location(
    "record_review", Path(__file__).resolve().parent / "record-review.py")
rr = importlib.util.module_from_spec(_rr_spec)
_rr_spec.loader.exec_module(rr)
check("glowup sections match record-review's MODE_PR_SECTIONS",
      c.GLOWUP_SECTIONS == rr.MODE_PR_SECTIONS["glowup"])
check("every glowup section heading renders in the body",
      all(f"## {s}" in gout for s in c.GLOWUP_SECTIONS))

# ---- backlog reconciliation against the fresh run -----------------------------
#
# The two 2026-09-01 glow-ups a human reviewer rejected, replayed offline over
# trimmed copies of their own `review-snapshot` artifacts (testdata/). The
# composer takes exactly these inputs, so this is the acceptance test.

import json as _json

TD = Path(__file__).resolve().parent / "testdata"


def _load(run: str, name: str):
    return _json.loads((TD / run / name).read_text())


def _section(text: str, name: str) -> str:
    return text.split(f"## {name}", 1)[1].split("\n## ", 1)[0]


# Case 1 — PR #21291 (run 33518039058, convert-hcl.md): `pr20004-findings-4`
# is a July `contradicted (medium)` verdict on "Using the Pulumi MCP server is
# the recommended approach …" that the September run re-verdicted
# `not-a-claim (high)` as c37 at L1228 (id drifted from c23, line from L1115).
# The glow-up executed it anyway. Same run: c7 and c32 were contradicted and
# never surfaced — the body carried only a verdict count.
RUN_A = "glowup-run33518039058"
backlog_a = _load(RUN_A, ".glowup-backlog.json")
body_a = c.compose_glowup(_load(RUN_A, ".content-review-queue.json"), backlog_a,
                          _load(RUN_A, ".verified-claims.json"), None,
                          _load(RUN_A, ".readthrough-findings.json"), None)
exe_a, dec_a = _section(body_a, "Backlog executed"), _section(body_a, "Backlog declined")
check("#21291: pr20004-findings-4 is pre-declined as superseded by re-verification",
      "`pr20004-findings-4`" in dec_a and "superseded by re-verification" in dec_a)
check("#21291: the pre-declined row names the fresh verdict, id and line",
      "`not-a-claim`" in dec_a and "c37" in dec_a and "L1228" in dec_a)
check("#21291: pr20004-findings-4 is absent from the work list",
      "`pr20004-findings-4`" not in exe_a)
item4 = next(b for b in backlog_a["banked"] if b["id"] == "pr20004-findings-4")
check("#21291: the banked item is stamped with its fresh verdict",
      item4["fresh_verdict"]["claim_id"] == "c37" and item4["fresh_verdict"]["verdict"] == "not-a-claim"
      and item4["pre_declined"].startswith("superseded by re-verification"))
check("#21291: c7 (contradicted high) is stubbed as a work row",
      "`fresh-c7`" in exe_a and "contradicted (high)" in exe_a)
check("#21291: c32 (contradicted medium) is stubbed as a work row",
      "`fresh-c32`" in exe_a and "contradicted (medium)" in exe_a)
check("#21291: fresh stubs are sourced 'this run' and carry a TODO",
      "| this run | <TODO" in exe_a)
# Items the fresh run left `unverifiable` (c25/c26/c28 -> c39, c29 -> c43,
# c32 -> c39) are stamped but stay work; so does a Vale nag (never matched)
# and a banked claim the fresh run now CONTRADICTS (c22 -> c36).
check("#21291: banked items whose fresh verdict is unverifiable stay work, stamped",
      all(f"`pr20004-findings-{n}`" in exe_a for n in (6, 7, 8, 9, 12))
      and next(b for b in backlog_a["banked"] if b["id"] == "pr20004-findings-7")["fresh_verdict"]["verdict"] == "unverifiable")
check("#21291: a Vale nag and a banked claim the fresh run contradicts stay work",
      "`pr20004-findings-13`" in exe_a and "`pr20004-findings-2`" in exe_a
      and "c36 `contradicted`" in exe_a)
# Banked `unverifiable` claims the fresh run VERIFIED are superseded too —
# c24 -> c38 verified, c30 -> c44 verified, c31 -> c45 verified.
check("#21291: banked unverifiable claims the fresh run verified are pre-declined",
      all(f"`pr20004-findings-{n}`" in dec_a for n in (5, 10, 11)))
check("#21291: the reconciled backlog records the split",
      set(backlog_a["reconciled"]["pre_declined_ids"]) == {"pr20004-findings-3", "pr20004-findings-4",
                                                          "pr20004-findings-5", "pr20004-findings-10",
                                                          "pr20004-findings-11"}
      and {"fresh-c7", "fresh-c32"} <= {s["id"] for s in backlog_a["reconciled"]["fresh_stubs"]})
check("#21291: the row shows the prior disposition as context, labelled",
      "_(prior disposition:" in exe_a)
# The fresh stub's text starts with collect()'s label so record-page-findings
# resolves an executed stub to its finding by the same prefix match.
labels = {f["label"] for f in c.collect(_load(RUN_A, ".verified-claims.json"), None, None, None)[0]}
check("#21291: fresh stub text starts with collect()'s label for the same verdict",
      all(any(st["text"].startswith(lab) for lab in labels) for st in backlog_a["reconciled"]["fresh_stubs"]))
check("#21291: every stubbed id is accounted for by the accounting check on the draft",
      c.glowup_body_accounting(body_a, backlog_a) == ["Backlog executed still carries a <TODO> marker",
                                                     "Backlog declined still carries a <TODO> marker"])

# Case 2 — PR #21293 (run 33518035360, providers/_index.md): `pr20503-findings-5`
# is a July readthrough "self-redundancy" finding the July agent declined as
# editorial; the fresh readthrough pass raised three findings, none of them
# this one (its self-redundancy is a different one, seven lines away). The
# glow-up executed it and collapsed a definition.
RUN_C = "glowup-run33518035360"
backlog_c = _load(RUN_C, ".glowup-backlog.json")
body_c = c.compose_glowup(_load(RUN_C, ".content-review-queue.json"), backlog_c,
                          _load(RUN_C, ".verified-claims.json"), None,
                          _load(RUN_C, ".readthrough-findings.json"), None)
exe_c, dec_c = _section(body_c, "Backlog executed"), _section(body_c, "Backlog declined")
check("#21293: pr20503-findings-5 is pre-declined (no fresh readthrough counterpart)",
      "`pr20503-findings-5`" in dec_c and "did not re-raise it" in dec_c
      and "`pr20503-findings-5`" not in exe_c)
item5 = next(b for b in backlog_c["banked"] if b["id"] == "pr20503-findings-5")
check("#21293: the readthrough item is stamped absent",
      item5["fresh_verdict"] == {"kind": "readthrough", "status": "absent"})
check("#21293: a different fresh self-redundancy seven lines away is not mistaken for it",
      item5.get("pre_declined") and "superseded" in item5["pre_declined"])
check("#21293: a claim the fresh run still finds unverifiable stays work; a Vale nag too",
      "`findings-f2`" in exe_c and "`pr20503-findings-4`" in exe_c)
check("#21293: the July unverifiable c6 the fresh run verified (c6, L31) is pre-declined",
      "`pr20503-findings-1`" in dec_c and "`findings-f1`" in dec_c)
check("#21293: 0 contradicted verdicts -> no fresh stubs", "`fresh-" not in body_c)

# Synthetic: banked contradicted positioning claim at N vs. fresh not-a-claim
# at N+111 -> pre-declined (text match inside the line window, never by id or
# exact line); fresh contradicted with no banked counterpart -> stubbed.
SYN_BACKLOG = {"banked": [
    {"id": "pr1-findings-1", "section": "Findings not applied", "source_pr": 1, "source": "pr-body",
     "text": "- **Claim (c23, L1115): Using the Pulumi MCP server is the recommended approach for "
             "AI-assisted conversion — contradicted (medium).** — positioning judgment; editorial."},
    {"id": "pr1-findings-2", "section": "Findings not applied", "source_pr": 1, "source": "pr-body",
     "text": "- **Claim (c9, L40): There are two converters in `pulumi convert` that read HCL — "
             "unverifiable.** — could not confirm."},
    {"id": "pr1-findings-3", "section": "Findings not applied", "source_pr": 1, "source": "pr-body",
     "text": "- **Vale weasel word (L18): 'several' is a weasel word.** — style nag."},
], "notes": []}
SYN_VERIFIED = {"verdicts": [
    {"claim_id": "c37", "line_range": "L1226", "verdict": "not-a-claim", "confidence": "high",
     "text": "Using the Pulumi MCP server is the recommended approach for AI-assisted conversion.",
     "type": "positioning"},
    {"claim_id": "c7", "line_range": "L41", "verdict": "contradicted", "confidence": "high",
     "text": "There are two converters in `pulumi convert` that read HCL, selected with the `--from` flag.",
     "type": "api-surface", "evidence": "convert.go has no hcl case"},
    {"claim_id": "c50", "line_range": "L900", "verdict": "contradicted", "confidence": "medium",
     "text": "The listener lands in us-west-2.", "type": "behavior"},
]}
syn = c.compose_glowup(QUEUE, SYN_BACKLOG, SYN_VERIFIED, None, {"ran": True, "findings": []}, None)
syn_exe, syn_dec = _section(syn, "Backlog executed"), _section(syn, "Backlog declined")
check("synthetic: banked contradicted at L1115 vs fresh not-a-claim at L1226 -> pre-declined",
      "`pr1-findings-1`" in syn_dec and "`pr1-findings-1`" not in syn_exe)
check("synthetic: a banked claim the fresh run now contradicts stays work, stamped",
      "`pr1-findings-2`" in syn_exe and "c7 `contradicted`" in syn_exe)
check("synthetic: fresh contradicted with no banked counterpart is stubbed",
      "`fresh-c50`" in syn_exe)
check("synthetic: a Vale nag is neither matched nor declined", "`pr1-findings-3`" in syn_exe)
far = {"verdicts": [{**SYN_VERIFIED["verdicts"][0], "line_range": "L1400"}]}
far_body = c.compose_glowup(QUEUE, _json.loads(_json.dumps(SYN_BACKLOG)), far, None, None, None)
check("synthetic: the same text outside the line window is not matched",
      "`pr1-findings-1`" in _section(far_body, "Backlog executed"))
noart = c.compose_glowup(QUEUE, _json.loads(_json.dumps(SYN_BACKLOG)), None, None, None, None)
check("synthetic: no artifacts -> nothing is pre-declined",
      "Pre-declined" not in _section(noart, "Backlog declined"))
rt_off = c.compose_glowup(QUEUE, {"banked": [{"id": "pr2-findings-1", "source_pr": 2, "source": "pr-body",
    "text": "- **Readthrough self-redundancy (L36, 65-84): rationale restated across two sections.** — editorial."}],
    "notes": []}, None, None, {"ran": False, "findings": []}, None)
check("synthetic: a readthrough pass that did not run supersedes nothing",
      "`pr2-findings-1`" in _section(rt_off, "Backlog executed"))

# Body accounting: the publish gate's refusal rule.
acct_backlog = {"banked": [{"id": "pr1-findings-1", "text": "x"}, {"id": "pr1-findings-2", "text": "y"}],
                "reconciled": {"fresh_stubs": [{"id": "fresh-c7"}]}}
good = ("## Backlog executed\n| `pr1-findings-1` | #1 | done |\n| `fresh-c7` | this run | fixed |\n\n"
        "## Backlog declined\n| `pr1-findings-2` | #1 | no |\n\n## Secondary sweep\n")
check("accounting: every id in exactly one table -> clean", c.glowup_body_accounting(good, acct_backlog) == [])
dropped = good.replace("| `fresh-c7` | this run | fixed |\n", "")
check("accounting: a dropped fresh stub is a violation",
      c.glowup_body_accounting(dropped, acct_backlog) == ["fresh-c7 appears in neither Backlog executed nor Backlog declined"])
both = good.replace("## Secondary sweep", "| `pr1-findings-1` | #1 | also no |\n\n## Secondary sweep")
check("accounting: an id in both tables is a violation",
      any("both" in v for v in c.glowup_body_accounting(both, acct_backlog)))
check("accounting: a leftover <TODO> in either table is a violation",
      any("<TODO>" in v for v in c.glowup_body_accounting(good.replace("| done |", "| <TODO> |"), acct_backlog)))
check("accounting: a body without the two sections is a violation",
      c.glowup_body_accounting("## Why this page\n", acct_backlog))

if failures:
    print(f"\n{len(failures)} failure(s)", file=sys.stderr)
    sys.exit(1)
print("\nall compose-pr-body tests passed")
