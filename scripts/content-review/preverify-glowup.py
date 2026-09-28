#!/usr/bin/env python3
"""preverify-glowup.py — verify a glow-up's edits BEFORE its PR opens, with the
pre-merge review's own claim pipeline, and keep the receipts.

Why this exists. The glow-up lane's pre-steps verify the PRISTINE page (the
synthetic whole-file diff), then the model rewrites it. Nothing checked the
rewrite until the pre-merge review ran on the opened PR, and that review then
caught what the glow-up had introduced: pulumi/docs#21939 changed "three
properties" to "four" when the source declares five, and #21897 changed a
sample CLI summary to "4 changes. 2 unchanged", which `pulumi up` never
prints. Those findings then deadlocked, because the card asks the PR author
(pulumi-bot) to answer.

The fix is to run the review's verifier where the review would: over the
EDITED spans only. `extract-claims-llm.py` at `standard` scrutiny already
extracts only from `+` lines, so feeding it a pristine→edited patch gives the
exact claim set the pre-merge review will see, at a cost proportional to the
edit rather than the page.

Subcommands (all deterministic except the model calls inside the review's own
scripts, which this only orchestrates):

  verify    one round: build the pristine→edited patch, run the review's
            pre-steps over it (URL fetch, regex + atomic + holistic extraction,
            merge, verify-claims), keep only claims that touch an edited line,
            and classify each the way the review's composer buckets it:
              ok        verified (high/medium), matches, not-a-claim
              blocking  contradicted, mismatch, flagged      -> review 🚨
              question  unverifiable                         -> review ❓
              advisory  framing-drift, verified-low          -> review ⚠️
            Each non-ok claim also gets a provenance against the pristine
            page's own verdicts: `introduced` (the edit created or broke it)
            or `carried` (the pristine page already had it; the edit touched
            the line and so re-exposes it to a diff-scoped review). A claim is
            MUST-ADDRESS when it is blocking or question, or an introduced
            framing-drift (a glow-up reads better; it does not say different
            things). Verdicts for claim texts already verified in an earlier
            round are reused (whatever the verdict), so a repair round pays only
            for the text it changed.

  revert    the deterministic backstop after the last round: restore the
            pristine lines of every changed block that still carries a
            must-address claim. The diff only shrinks, so nothing new needs
            verifying.

  receipts  render the "Pre-verification" section of the PR body from the
            round files and the revert record: every claim on an edited line,
            its verdict and source, and what happened to it, plus token cost.
            Also writes the same data as JSON for the evidence trail.

Round files never come from the model. The workflow uploads each one as an
artifact right after writing it and downloads the prior rounds fresh before
the next `verify`, so a model step in between cannot edit the cache into
saying something verified.

Usage:
    preverify-glowup.py verify --article <path> --pristine <file> \
        --pristine-verdicts .verified-claims.json --round N \
        [--prior round-1.json ...] --out .preverify/round-N.json [--dry-run]
    preverify-glowup.py revert --article <path> --pristine <file> \
        --round-file .preverify/round-N.json --out .preverify/reverted.json
    preverify-glowup.py receipts --round-file R1 [--round-file R2 ...] \
        [--reverted .preverify/reverted.json] --body .pr-body-draft.md \
        --out-json .preverify/receipts.json
    preverify-glowup.py --self-test
"""

from __future__ import annotations

import argparse
import difflib
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

SCHEMA_VERSION = 1
HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent.parent
REVIEW_SCRIPTS = REPO_ROOT / ".claude" / "commands" / "docs-review" / "scripts"

OK_VERDICTS = {"verified", "matches", "not-a-claim"}
BLOCKING_VERDICTS = {"contradicted", "mismatch", "flagged"}
QUESTION_VERDICTS = {"unverifiable"}

SECTION = "Pre-verification"
MARKER = "PREVERIFY"
# Where the section goes when the body has no placeholder for it: ahead of the
# first of these headings that exists.
INSERT_BEFORE = ("Screenshot check", "Verification")
TABLE_ROW_CAP = 40
CELL_CAP = 160


# ---------------------------------------------------------------------------
# text and line helpers
# ---------------------------------------------------------------------------

def norm(text: str) -> str:
    """Comparison key for a claim: case- and markup-insensitive."""
    t = re.sub(r"[`*_\[\]()>#|]", " ", str(text or "").lower())
    return " ".join(t.split())


def ratio(a: str, b: str) -> float:
    return difflib.SequenceMatcher(None, norm(a), norm(b), autojunk=False).ratio()


def parse_range(lr) -> tuple[int, int] | None:
    m = re.match(r"^L(\d+)(?:-L?(\d+))?$", str(lr or "").strip())
    if not m:
        return None
    a = int(m.group(1))
    b = int(m.group(2) or a)
    return (min(a, b), max(a, b))


def _lines(text: str) -> list[str]:
    return text.splitlines(keepends=True)


def opcodes(pristine: str, current: str):
    return difflib.SequenceMatcher(None, _lines(pristine), _lines(current),
                                   autojunk=False).get_opcodes()


def changed_lines(pristine: str, current: str) -> set[int]:
    """1-based line numbers in `current` that the edit added or modified. A
    pure deletion marks the line now sitting where the text was removed, since
    removing a qualifier changes what its neighbour says."""
    out: set[int] = set()
    n = len(_lines(current))
    for tag, _i1, _i2, j1, j2 in opcodes(pristine, current):
        if tag == "equal":
            continue
        if j2 > j1:
            out.update(range(j1 + 1, j2 + 1))
        elif n:
            out.add(min(max(j1, 1), n))
    return out


def new_to_old(pristine: str, current: str) -> dict[int, list[int]]:
    """Map each current line to the pristine line(s) it came from."""
    m: dict[int, list[int]] = {}
    for tag, i1, i2, j1, j2 in opcodes(pristine, current):
        for j in range(j1, j2):
            if tag == "equal":
                m[j + 1] = [i1 + (j - j1) + 1]
            else:
                m[j + 1] = list(range(i1 + 1, i2 + 1)) or ([i1] if i1 else [])
    return m


def build_patch(article: str, pristine: str, current: str) -> str:
    """The pristine→edited unified diff, in the shape `git diff` emits (the
    review's scripts parse `diff --git` / `+++ b/<path>` headers)."""
    body = list(difflib.unified_diff(_lines(pristine), _lines(current),
                                     fromfile=f"a/{article}", tofile=f"b/{article}", n=3))
    if not body:
        return ""
    fixed = []
    for ln in body:
        if not ln.endswith("\n"):
            ln += "\n\\ No newline at end of file\n"
        fixed.append(ln)
    return f"diff --git a/{article} b/{article}\n" + "".join(fixed)


# ---------------------------------------------------------------------------
# classification
# ---------------------------------------------------------------------------

def classify(v: dict) -> str:
    verdict = v.get("verdict")
    conf = (v.get("confidence") or "").lower()
    if verdict in BLOCKING_VERDICTS:
        return "blocking"
    if verdict in QUESTION_VERDICTS:
        return "question"
    if verdict == "framing-drift" or (verdict == "verified" and conf == "low"):
        return "advisory"
    if verdict in OK_VERDICTS:
        return "ok"
    # An unknown verdict is not evidence of anything; treat it like the
    # review would treat a claim it couldn't settle.
    return "question"


def counterpart(v: dict, pristine_verdicts: list[dict], n2o: dict[int, list[int]]) -> dict | None:
    """The pristine page's verdict for the same claim, if the whole-file
    pre-step extracted it. Claim ids and line numbers drift between runs, so
    match on text, helped by where the edited lines came from."""
    rng = parse_range(v.get("line_range"))
    old_lines: set[int] = set()
    if rng:
        for ln in range(rng[0], rng[1] + 1):
            old_lines.update(n2o.get(ln, []))
    best, best_score = None, 0.0
    for pv in pristine_verdicts:
        r = ratio(v.get("text", ""), pv.get("text", ""))
        prng = parse_range(pv.get("line_range"))
        near = bool(prng and old_lines and any(prng[0] - 1 <= o <= prng[1] + 1 for o in old_lines))
        score = r + (0.25 if near else 0.0)
        if (r >= 0.8 or (near and r >= 0.5)) and score > best_score:
            best, best_score = pv, score
    return best


def provenance(cls: str, cp: dict | None) -> str:
    if cls == "ok":
        return ""
    if cp is not None and classify(cp) != "ok":
        return "carried"
    return "introduced"


def must_address(cls: str, prov: str, verdict: str) -> bool:
    if cls in ("blocking", "question"):
        return True
    return verdict == "framing-drift" and prov == "introduced"


def action_hint(rec: dict) -> str:
    cls, prov = rec["class"], rec["provenance"]
    if cls == "blocking":
        return ("Correct the text to exactly what the cited source states, or revert this "
                "edit to the pristine text. Do not guess a value the evidence doesn't state.")
    if cls == "question" and prov == "carried":
        return ("The pristine page already carried this unverified claim; your edit re-exposes it "
                "to a diff-scoped review. Revert your edit of these lines unless a source you can "
                "cite now settles it.")
    if cls == "question":
        return ("A glow-up must not add a claim nothing verifies. Revert this edit, or rephrase "
                "so the sentence no longer asserts it.")
    return "Restore the source's framing (scope, qualifiers, tense), or revert this edit."


# ---------------------------------------------------------------------------
# verify
# ---------------------------------------------------------------------------

def _run(cmd: list[str], log: list[str]) -> int:
    p = subprocess.run(cmd, capture_output=True, text=True)
    tail = (p.stderr or p.stdout or "").strip().splitlines()[-1:] or [""]
    log.append(f"{Path(cmd[1]).name}: rc={p.returncode} {tail[0][:200]}")
    return p.returncode


def _load(path: Path, default):
    try:
        return json.loads(path.read_text())
    except (OSError, json.JSONDecodeError):
        return default


def _usage(meta: dict | None) -> dict:
    meta = meta or {}
    keys = ("input_tokens", "output_tokens", "cache_read_input_tokens", "cache_creation_input_tokens")
    alt = {"input_tokens": "llm_input_tokens", "output_tokens": "llm_output_tokens"}
    return {k: int(meta.get(k) or meta.get(alt.get(k, ""), 0) or 0) for k in keys}


def _add(a: dict, b: dict) -> dict:
    return {k: int(a.get(k, 0)) + int(b.get(k, 0)) for k in set(a) | set(b)}


def run_pipeline(article: str, patch_file: Path, work: Path, dry_run: bool,
                 cached: dict[str, dict], changed: set[int],
                 log: list[str]) -> tuple[list[dict], dict, list[str], bool]:
    """Run the review's pre-steps over the patch. Returns (verdicts, usage,
    errors, degraded). Verdicts cover only claims that touch an edited line;
    claims whose text an earlier round already verified reuse that verdict."""
    S = REVIEW_SCRIPTS
    py = sys.executable
    dry = ["--dry-run"] if dry_run else []
    fetched = work / "fetched-urls.json"
    if _run([py, str(S / "extract-urls-and-fetch.py"), "--patch-file", str(patch_file),
             "--out", str(fetched)], log) != 0 or not fetched.exists():
        fetched.write_text("[]")
    rx = work / "claims-regex.json"
    _run([py, str(S / "extract-claims.py"), "--patch-file", str(patch_file), "--out", str(rx)], log)
    procs = []
    for i, pass_name in enumerate(("atomic", "holistic"), 1):
        out = work / f"claims-llm-{i}.json"
        cmd = [py, str(S / "extract-claims-llm.py"), "--patch-file", str(patch_file),
               "--changed-files", article, "--pass", pass_name, "--scrutiny", "standard",
               "--out", str(out), *dry]
        procs.append((out, subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)))
    for out, p in procs:
        _o, e = p.communicate()
        log.append(f"extract-claims-llm.py({out.name}): rc={p.returncode} {(e or '').strip()[-200:]}")
    merged = work / "candidate-claims.json"
    _run([py, str(S / "merge-claims.py"), "--regex", str(rx),
          "--llm", str(work / "claims-llm-1.json"), "--llm", str(work / "claims-llm-2.json"),
          "--out", str(merged)], log)

    errors: list[str] = []
    usage = {"extract": {}, "verify": {}}
    llm_errs = 0
    for i in (1, 2):
        d = _load(work / f"claims-llm-{i}.json", {})
        usage["extract"] = _add(usage["extract"], _usage(d.get("meta")))
        if d.get("errors"):
            llm_errs += 1
            errors += [f"extract-llm-{i}: {e}" for e in d["errors"]][:3]
    cand = _load(merged, {})
    if not isinstance(cand, dict) or "claims" not in cand:
        return [], usage, errors + ["merge-claims produced no candidate list"], True

    def touches(c: dict) -> bool:
        rng = parse_range(c.get("line_range"))
        return bool(rng) and any(ln in changed for ln in range(rng[0], rng[1] + 1))

    todo, reused = [], []
    for c in cand.get("claims") or []:
        if c.get("file") and c.get("file") != article:
            continue
        if not touches(c):
            continue
        hit = cached.get(norm(c.get("text", "")))
        if hit:
            r = dict(hit)
            r.update({"line_range": c.get("line_range"), "cached": True})
            reused.append(r)
        else:
            todo.append(c)

    verdicts: list[dict] = list(reused)
    if todo:
        cand_todo = dict(cand)
        cand_todo["claims"] = todo
        cfile = work / "candidate-claims-todo.json"
        cfile.write_text(json.dumps(cand_todo, indent=2))
        vfile = work / "verified-claims.json"
        _run([py, str(S / "verify-claims.py"), "--in", str(cfile), "--fetched-urls", str(fetched),
              "--out", str(vfile), *dry], log)
        vd = _load(vfile, {})
        usage["verify"] = _usage(vd.get("meta"))
        if vd.get("errors"):
            errors += [f"verify: {e}" for e in vd["errors"]][:5]
        got = vd.get("verdicts") or []
        if not got:
            return verdicts, usage, errors + ["verify-claims produced no verdicts"], True
        verdicts += got
    degraded = llm_errs == 2 and not (cand.get("claims") or [])
    return verdicts, usage, errors, degraded


def cmd_verify(a) -> int:
    article = a.article
    current = Path(article).read_text()
    pristine = Path(a.pristine).read_text()
    pristine_verdicts = (_load(Path(a.pristine_verdicts), {}) or {}).get("verdicts") or [] \
        if a.pristine_verdicts else []
    cached: dict[str, dict] = {}
    for pf in a.prior or []:
        for rec in (_load(Path(pf), {}) or {}).get("claims") or []:
            # Every verdict is reused for byte-identical claim text, failing
            # ones included: re-asking the verifier about an unchanged
            # sentence buys a second sample, not new evidence, and an
            # unchanged failure is what the revert backstop is for.
            if rec.get("text"):
                cached[norm(rec["text"])] = {k: rec[k] for k in rec
                                             if k in ("text", "verdict", "confidence", "evidence",
                                                      "source", "route", "type", "claim_id")}

    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    changed = changed_lines(pristine, current)
    if a.restored_from:
        # Post-open autofix: `pristine` is the PR head and a revert restores
        # master's text. A line put back verbatim is not a new claim; the
        # glow-up is withdrawing one, so it is not this check's to judge.
        base_lines = {ln.strip() for ln in _lines(Path(a.restored_from).read_text()) if ln.strip()}
        cur = _lines(current)
        changed = {n for n in changed
                   if not (0 < n <= len(cur) and cur[n - 1].strip() and cur[n - 1].strip() in base_lines)}
    result = {"schema_version": SCHEMA_VERSION, "round": a.round, "article": article,
              "changed_lines": len(changed), "claims": [], "must_address": 0,
              "degraded": False, "errors": [], "log": [],
              "usage": {"extract": {}, "verify": {}}, "n_cached": 0}
    if changed:
        with tempfile.TemporaryDirectory(prefix="preverify-") as td:
            work = Path(td)
            pf = work / "edited.patch"
            pf.write_text(build_patch(article, pristine, current))
            verdicts, usage, errors, degraded = run_pipeline(
                article, pf, work, a.dry_run, cached, changed, result["log"])
        n2o = new_to_old(pristine, current)
        for i, v in enumerate(verdicts, 1):
            cls = classify(v)
            cp = counterpart(v, pristine_verdicts, n2o) if cls != "ok" else None
            prov = provenance(cls, cp)
            rec = {
                "id": f"r{a.round}-{i}",
                "line_range": v.get("line_range"),
                "text": v.get("text", ""),
                "type": v.get("type"),
                "verdict": v.get("verdict"),
                "confidence": v.get("confidence"),
                "evidence": v.get("evidence", ""),
                "source": v.get("source", ""),
                "route": v.get("route"),
                "class": cls,
                "provenance": prov,
                "cached": bool(v.get("cached")),
                "pristine": ({"verdict": cp.get("verdict"), "line_range": cp.get("line_range"),
                              "text": cp.get("text")} if cp else None),
            }
            rec["must_address"] = must_address(cls, prov, rec["verdict"] or "")
            if rec["must_address"]:
                rec["action"] = action_hint(rec)
            result["claims"].append(rec)
        result.update(usage=usage, errors=errors, degraded=degraded,
                      n_cached=sum(1 for r in result["claims"] if r["cached"]),
                      must_address=sum(1 for r in result["claims"] if r["must_address"]))
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(f"preverify round {a.round}: {len(result['claims'])} claim(s) on "
          f"{result['changed_lines']} edited line(s), {result['n_cached']} reused, "
          f"{result['must_address']} must-address, degraded={result['degraded']}", file=sys.stderr)
    for r in result["claims"]:
        if r["must_address"]:
            print(f"  {r['id']} {r['line_range']} {r['verdict']} ({r['provenance']}): "
                  f"{r['text'][:120]}", file=sys.stderr)
    gh = os.environ.get("GITHUB_OUTPUT")
    if gh:
        with open(gh, "a") as fh:
            fh.write(f"must_address={result['must_address']}\n")
            fh.write(f"degraded={'true' if result['degraded'] else 'false'}\n")
    return 0


# ---------------------------------------------------------------------------
# revert
# ---------------------------------------------------------------------------

def revert_blocks(pristine: str, current: str, targets: list[tuple[str, tuple[int, int]]]
                  ) -> tuple[str, list[dict], list[str]]:
    """Restore pristine text for every changed block overlapping a target
    range. Returns (new text, reverted blocks, unmapped target ids)."""
    a, b = _lines(pristine), _lines(current)
    ops = opcodes(pristine, current)
    picked: dict[int, list[str]] = {}
    unmapped = []
    for tid, (lo, hi) in targets:
        hit = False
        for k, (tag, i1, i2, j1, j2) in enumerate(ops):
            if tag == "equal":
                continue
            span = (j1 + 1, j2) if j2 > j1 else (j1, j1 + 1)
            if span[0] <= hi and lo <= span[1]:
                picked.setdefault(k, []).append(tid)
                hit = True
        if not hit:
            unmapped.append(tid)
    out, blocks = [], []
    for k, (tag, i1, i2, j1, j2) in enumerate(ops):
        if k in picked:
            out.extend(a[i1:i2])
            blocks.append({"current_lines": [j1 + 1, j2], "pristine_lines": [i1 + 1, i2],
                           "removed": "".join(b[j1:j2]), "restored": "".join(a[i1:i2]),
                           "claims": sorted(set(picked[k]))})
        else:
            out.extend(b[j1:j2])
    return "".join(out), blocks, unmapped


def cmd_revert(a) -> int:
    rnd = _load(Path(a.round_file), {}) or {}
    targets = []
    for r in rnd.get("claims") or []:
        rng = parse_range(r.get("line_range"))
        if r.get("must_address") and rng:
            targets.append((r["id"], rng))
    current = Path(a.article).read_text()
    pristine = Path(a.pristine).read_text()
    new, blocks, unmapped = revert_blocks(pristine, current, targets)
    if blocks:
        Path(a.article).write_text(new)
    rec = {"schema_version": SCHEMA_VERSION, "round": rnd.get("round"), "blocks": blocks,
           "unmapped": unmapped}
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(rec, indent=2) + "\n")
    print(f"preverify revert: {len(blocks)} block(s) restored to pristine for "
          f"{len(targets)} must-address claim(s); {len(unmapped)} unmapped", file=sys.stderr)
    return 0


# ---------------------------------------------------------------------------
# receipts
# ---------------------------------------------------------------------------

def _cell(text, cap: int = CELL_CAP) -> str:
    t = " ".join(str(text or "").split()).replace("|", "\\|")
    return t if len(t) <= cap else t[: cap - 1] + "…"


def summarize(rounds: list[dict], reverted: dict | None) -> dict:
    """Fold the round files into one per-claim outcome list."""
    reverted = reverted or {}
    rev_ids = {cid for b in reverted.get("blocks") or [] for cid in b.get("claims") or []}
    final = rounds[-1] if rounds else {}
    final_keys = {norm(r.get("text", "")) for r in final.get("claims") or []}
    rows = []
    # Claims an earlier round flagged whose text is gone by the final round:
    # the repair pass rewrote or reverted them.
    for rnd in rounds[:-1]:
        for r in rnd.get("claims") or []:
            if r.get("must_address") and norm(r.get("text", "")) not in final_keys:
                rows.append({**r, "outcome": f"repaired in round {rnd.get('round')} → {int(rnd.get('round', 0)) + 1} "
                                             f"(was {r.get('verdict')}; re-verified text below)"})
    for r in final.get("claims") or []:
        if r["id"] in rev_ids:
            outcome = f"reverted to the pristine text (still {r.get('verdict')} after the last round)"
        elif r.get("must_address"):
            outcome = "OPEN — could not be reverted automatically"
        elif r.get("class") == "ok":
            outcome = "kept" + (" (verdict reused from an earlier round)" if r.get("cached") else "")
        else:
            outcome = f"kept — {r.get('class')}, non-blocking"
        rows.append({**r, "outcome": outcome})
    usage = {"extract": {}, "verify": {}}
    for rnd in rounds:
        for k in usage:
            usage[k] = _add(usage[k], (rnd.get("usage") or {}).get(k) or {})
    open_n = sum(1 for r in final.get("claims") or [] if r.get("must_address") and r["id"] not in rev_ids)
    degraded = any(rnd.get("degraded") for rnd in rounds)
    return {
        "schema_version": SCHEMA_VERSION,
        "rounds": len(rounds),
        "claims_checked": len(final.get("claims") or []),
        "repaired": sum(1 for r in rows if str(r.get("outcome", "")).startswith("repaired")),
        "reverted_blocks": len(reverted.get("blocks") or []),
        "open": open_n,
        "degraded": degraded,
        "clean": bool(rounds) and not degraded and open_n == 0,
        "errors": sorted({e for rnd in rounds for e in rnd.get("errors") or []})[:10],
        "usage": usage,
        "rows": rows,
        "reverted": reverted.get("blocks") or [],
    }


def render_section(s: dict) -> str:
    marker = {k: s[k] for k in ("schema_version", "clean", "degraded", "rounds", "claims_checked",
                                 "repaired", "reverted_blocks", "open")}
    out = [f"## {SECTION}", "", f"<!-- {MARKER} {json.dumps(marker, sort_keys=True)} -->", ""]
    if not s["rounds"]:
        out.append("> [!WARNING]\n> Pre-verification did not run. Treat every changed claim as unverified.")
        return "\n".join(out) + "\n"
    head = (f"Before this PR opened, the workflow ran the pre-merge review's own claim extraction "
            f"and verification over **the lines this glow-up changed** ({s['rounds']} round(s)). "
            f"{s['claims_checked']} claim(s) on edited lines in the final round")
    tail = []
    if s["repaired"]:
        tail.append(f"{s['repaired']} repaired between rounds")
    if s["reverted_blocks"]:
        tail.append(f"{s['reverted_blocks']} edited block(s) reverted to the pristine text")
    out.append(head + (": " + "; ".join(tail) if tail else "") + ".")
    out.append("")
    if s["degraded"]:
        out.append("> [!WARNING]\n> **Pre-verification was degraded** (a pipeline stage failed; see errors "
                   "below). The verdicts here are incomplete, so a human must check the changed claims.")
        out.append("")
    elif s["open"]:
        out.append(f"> [!WARNING]\n> **{s['open']} claim(s) on edited lines are still unverified or "
                   "contradicted** and could not be reverted automatically. A human must decide them.")
        out.append("")
    else:
        out.append("Every claim on an edited line is verified, reverted, or non-blocking. The "
                   "pre-merge review re-checks this diff independently.")
        out.append("")
    rows = s["rows"]
    if rows:
        tbl = ["| Line | Claim | Verdict | Source | Outcome |", "| --- | --- | --- | --- | --- |"]
        for r in rows[:TABLE_ROW_CAP]:
            verdict = str(r.get("verdict") or "")
            if r.get("confidence"):
                verdict += f" ({r['confidence']})"
            if r.get("provenance"):
                verdict += f", {r['provenance']}"
            tbl.append(f"| {_cell(r.get('line_range'), 20)} | {_cell(r.get('text'))} | {_cell(verdict, 60)} | "
                       f"{_cell(r.get('source'), 120)} | {_cell(r.get('outcome'), 120)} |")
        if len(rows) > TABLE_ROW_CAP:
            tbl.append(f"| … | {len(rows) - TABLE_ROW_CAP} more row(s) in the run's `preverify` artifact | | | |")
        if len(rows) > 10:
            out += ["<details>", f"<summary>All {len(rows)} checked claims</summary>", ""]
            out += tbl + ["", "</details>"]
        else:
            out += tbl
        out.append("")
    if s["reverted"]:
        out.append("**Reverted blocks** (pristine text restored):")
        out.append("")
        for b in s["reverted"][:10]:
            out.append(f"- L{b['current_lines'][0]}-{b['current_lines'][1]} of the edited page, for "
                       f"{', '.join(b['claims'])}: removed “{_cell(b['removed'], 200)}”")
        out.append("")
    u = s["usage"]
    fmt = lambda d: (f"{d.get('input_tokens', 0):,} in / {d.get('output_tokens', 0):,} out"
                     f" / {d.get('cache_read_input_tokens', 0):,} cache-read")
    out.append(f"_Cost: extraction {fmt(u.get('extract') or {})}; verification "
               f"{fmt(u.get('verify') or {})} tokens._")
    if s["errors"]:
        out.append("")
        out.append("_Pipeline errors: " + "; ".join(_cell(e, 120) for e in s["errors"]) + "_")
    return "\n".join(out) + "\n"


def splice_section(body: str, section_md: str) -> str:
    """Replace an existing `## Pre-verification` section, or insert one
    ahead of Screenshot check / Verification, or append."""
    pat = re.compile(rf"^##\s+{re.escape(SECTION)}\s*$.*?(?=^##\s|\Z)", re.M | re.S)
    if pat.search(body):
        return pat.sub(lambda _m: section_md.rstrip() + "\n\n", body, count=1)
    for h in INSERT_BEFORE:
        m = re.search(rf"^##\s+{re.escape(h)}\s*$", body, re.M)
        if m:
            return body[: m.start()] + section_md.rstrip() + "\n\n" + body[m.start():]
    return body.rstrip() + "\n\n" + section_md


def cmd_receipts(a) -> int:
    rounds = [r for r in (_load(Path(p), None) for p in a.round_file or []) if isinstance(r, dict)]
    rounds.sort(key=lambda r: int(r.get("round") or 0))
    reverted = _load(Path(a.reverted), None) if a.reverted else None
    s = summarize(rounds, reverted)
    if a.out_json:
        Path(a.out_json).parent.mkdir(parents=True, exist_ok=True)
        Path(a.out_json).write_text(json.dumps(s, indent=2) + "\n")
    if a.body:
        p = Path(a.body)
        body = p.read_text() if p.exists() else ""
        p.write_text(splice_section(body, render_section(s)))
    print(f"preverify receipts: clean={s['clean']} rounds={s['rounds']} claims={s['claims_checked']} "
          f"repaired={s['repaired']} reverted_blocks={s['reverted_blocks']} open={s['open']} "
          f"degraded={s['degraded']}", file=sys.stderr)
    gh = os.environ.get("GITHUB_OUTPUT")
    if gh:
        with open(gh, "a") as fh:
            fh.write(f"clean={'true' if s['clean'] else 'false'}\n")
    return 0


def read_marker(body: str) -> dict | None:
    """The receipts' machine summary from a PR body (post-open consumers)."""
    m = re.search(rf"<!--\s*{MARKER}\s+(\{{.*?\}})\s*-->", body or "")
    if not m:
        return None
    try:
        return json.loads(m.group(1))
    except json.JSONDecodeError:
        return None


# ---------------------------------------------------------------------------
# self-test
# ---------------------------------------------------------------------------

def self_test() -> int:
    fails = []

    def check(c, msg):
        if not c:
            fails.append(msg)

    pristine = "# T\n\nThe variable has three properties.\n\nKeep me.\n\n    4 changes. 1 unchanged\n"
    current = "# T\n\nThe variable has four properties.\n\nKeep me.\n\n    4 changes. 2 unchanged\n"
    ch = changed_lines(pristine, current)
    check(ch == {3, 7}, f"changed_lines {ch}")
    patch = build_patch("content/x.md", pristine, current)
    check(patch.startswith("diff --git a/content/x.md b/content/x.md\n--- a/content/x.md\n+++ b/content/x.md"),
          "patch header")
    check("+The variable has four properties.\n" in patch, "patch body")
    check(build_patch("content/x.md", pristine, pristine) == "", "empty patch on no edit")
    check(new_to_old(pristine, current)[5] == [5], "equal-line mapping")

    check(classify({"verdict": "contradicted"}) == "blocking", "classify contradicted")
    check(classify({"verdict": "unverifiable"}) == "question", "classify unverifiable")
    check(classify({"verdict": "verified", "confidence": "low"}) == "advisory", "classify verified-low")
    check(classify({"verdict": "verified", "confidence": "high"}) == "ok", "classify verified")
    check(classify({"verdict": "framing-drift"}) == "advisory", "classify framing-drift")

    pv = [{"text": "The variable has three properties.", "verdict": "contradicted", "line_range": "L3"},
          {"text": "Keep me.", "verdict": "verified", "line_range": "L5"}]
    n2o = new_to_old(pristine, current)
    cp = counterpart({"text": "The variable has four properties.", "line_range": "L3"}, pv, n2o)
    check(cp is pv[0], "counterpart by text + position")
    check(provenance("blocking", cp) == "carried", "carried provenance")
    check(provenance("blocking", pv[1]) == "introduced", "introduced when pristine was ok")
    check(provenance("question", None) == "introduced", "introduced with no counterpart")
    check(must_address("advisory", "introduced", "framing-drift"), "introduced drift is must-address")
    check(not must_address("advisory", "carried", "framing-drift"), "carried drift is advisory")
    check(not must_address("advisory", "introduced", "verified"), "verified-low is advisory")

    new, blocks, unmapped = revert_blocks(pristine, current, [("r1-2", (7, 7))])
    check(new == pristine.replace("three", "four"), "revert restores only the targeted block")
    check(len(blocks) == 1 and blocks[0]["claims"] == ["r1-2"] and not unmapped, "revert record")
    _n, _b, unmapped = revert_blocks(pristine, current, [("x", (5, 5))])
    check(unmapped == ["x"], "unchanged-line target is unmapped")
    inserted = pristine.replace("Keep me.\n", "Keep me.\nA brand new claim.\n")
    new, blocks, _u = revert_blocks(pristine, inserted, [("i", (6, 6))])
    check(new == pristine and blocks[0]["restored"] == "", "revert drops a pure insertion")

    r1 = {"round": 1, "claims": [
        {"id": "r1-1", "line_range": "L7", "text": "4 changes. 2 unchanged", "verdict": "contradicted",
         "class": "blocking", "provenance": "introduced", "must_address": True, "source": "diff.go"},
        {"id": "r1-2", "line_range": "L3", "text": "has four properties", "verdict": "verified",
         "confidence": "high", "class": "ok", "provenance": "", "must_address": False, "source": "gh"}],
        "usage": {"extract": {"input_tokens": 100}, "verify": {"input_tokens": 1000}}}
    r2 = {"round": 2, "claims": [
        {"id": "r2-1", "line_range": "L7", "text": "2 unchanged", "verdict": "verified", "confidence": "high",
         "class": "ok", "provenance": "", "must_address": False, "source": "diff.go"},
        {"id": "r2-2", "line_range": "L3", "text": "has four properties", "verdict": "verified",
         "confidence": "high", "class": "ok", "provenance": "", "must_address": False, "cached": True}],
        "usage": {"extract": {"input_tokens": 50}, "verify": {"input_tokens": 200}}}
    s = summarize([r1, r2], None)
    check(s["clean"] and s["repaired"] == 1 and s["open"] == 0, f"summary clean {s['clean']} {s['repaired']}")
    check(s["usage"]["verify"]["input_tokens"] == 1200, "usage summed across rounds")
    r3 = {"round": 1, "claims": [dict(r1["claims"][0])]}
    s = summarize([r3], {"blocks": [{"claims": ["r1-1"], "current_lines": [7, 7], "removed": "x"}]})
    check(s["clean"] and s["reverted_blocks"] == 1, "reverted claim counts as clean")
    s = summarize([r3], None)
    check(not s["clean"] and s["open"] == 1, "unreverted must-address is open")
    check(not summarize([], None)["clean"], "no rounds is never clean")

    sec = render_section(summarize([r1, r2], None))
    body = "## Why this page\n\nx\n\n## Screenshot check\n\ny\n\n## Verification\n\nz\n"
    spliced = splice_section(body, sec)
    check(spliced.index("## Pre-verification") < spliced.index("## Screenshot check"), "inserted before screenshot")
    again = splice_section(spliced, sec)
    check(again.count("## Pre-verification") == 1, "splice is idempotent")
    check(read_marker(spliced)["clean"] is True, "marker round-trips")
    check(read_marker("no marker") is None, "missing marker")

    if fails:
        for f in fails:
            print(f"FAIL: {f}", file=sys.stderr)
        return 1
    print("preverify-glowup self-test: ok", file=sys.stderr)
    return 0


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    if argv[:1] == ["--self-test"]:
        return self_test()
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--self-test", action="store_true")
    sub = p.add_subparsers(dest="cmd", required=True)

    v = sub.add_parser("verify")
    v.add_argument("--article", required=True)
    v.add_argument("--pristine", required=True, help="pristine copy of the article (snapshot)")
    v.add_argument("--pristine-verdicts", help="the whole-file pre-step's .verified-claims.json")
    v.add_argument("--round", type=int, required=True)
    v.add_argument("--prior", action="append", help="earlier round files (verdict cache)")
    v.add_argument("--out", required=True)
    v.add_argument("--restored-from", help="lines matching this file verbatim are restorations, not edits")
    v.add_argument("--dry-run", action="store_true", help="pass --dry-run to the model-calling scripts")

    r = sub.add_parser("revert")
    r.add_argument("--article", required=True)
    r.add_argument("--pristine", required=True)
    r.add_argument("--round-file", required=True)
    r.add_argument("--out", required=True)

    c = sub.add_parser("receipts")
    c.add_argument("--round-file", action="append")
    c.add_argument("--reverted")
    c.add_argument("--body")
    c.add_argument("--out-json")

    a = p.parse_args(argv)
    return {"verify": cmd_verify, "revert": cmd_revert, "receipts": cmd_receipts}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
