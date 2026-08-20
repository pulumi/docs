#!/usr/bin/env python3
"""Assemble an ~80%-done content-review PR body from the pre-step artifacts.

The content-review counterpart to docs-review's `compose-review.py`, and the
same design frame: **the composer ASSEMBLES, the model JUDGES.** Instead of
letting the review model free-write the whole PR body from a bare template (it
narrated provenance it couldn't see and re-listed findings it might omit or
mis-source), this runs as a workflow step after the pre-computation pipeline and
writes `.pr-body-draft.md` — a structurally complete body with every section
present, the factual parts rendered verbatim, and one stub bullet per pre-found
finding carrying a `<TODO>` marker. The model then EDITS the draft: it keeps the
fix rows it actually applied (filling the correction), moves the rest to
"Findings not applied" with a reason, and fills the `<TODO>` observations.

What the composer renders (facts — never the model's to invent):

  * A top `> [!IMPORTANT]` auto-merge notice — every fix PR is armed for
    auto-merge by the re-lint gate, so the body flags that approving merges it.
  * "Why this page" — verbatim from the selection queue (via render-provenance).
  * "Fixes applied" / "Findings not applied" — one stub per pre-found finding
    from `.verified-claims.json` (contradicted/mismatch/unverifiable claims),
    `.vale-findings.json`, `.readthrough-findings.json`, and
    `.frontmatter-validation.json`, pre-bucketed by a conservative
    high-confidence rule. The model re-buckets and writes the prose.
  * "Verification" — a deterministic pre-step artifact inventory, plus a
    `<!-- LINT-RESULT -->` placeholder the workflow's re-lint gate stamps with
    the authoritative `make lint` result (so lint status is never self-reported).

What stays the model's (left as `<TODO>`): which stub is a real fix, the
correction prose, and the one-line deferral reasons. The "Screenshot check" and
"Rendered content" sections are filled deterministically (via render-gates) when
the source provably has nothing to look at — no content images, and no
content-bearing shortcode/partial/include — and otherwise left as a `<TODO>` for
the model to run that pass. This is what lets the worker skip the screenshot
pass and the `make build` + rendered pass on the pages that don't need them.

Degrades gracefully: a missing or errored artifact renders its section in a
degraded form with a note, never a crash. The draft always contains every
required `##` heading so the downstream section check passes.

Usage:
    compose-pr-body.py --queue .content-review-queue.json --out .pr-body-draft.md
        [--verified-claims .verified-claims.json] [--vale-findings .vale-findings.json]
        [--readthrough .readthrough-findings.json] [--frontmatter .frontmatter-validation.json]
        [--repo-root .]
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

# Reuse the provenance renderer (single source of truth for "Why this page").
_spec = importlib.util.spec_from_file_location(
    "render_provenance", HERE / "render-provenance.py"
)
_rp = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_rp)

# Reuse the render/screenshot gate logic (single source of truth for whether the
# screenshot and rendered-content passes have anything to look at).
_spec_g = importlib.util.spec_from_file_location("render_gates", HERE / "render-gates.py")
_rg = importlib.util.module_from_spec(_spec_g)
_spec_g.loader.exec_module(_rg)

LINT_PLACEHOLDER = "<!-- LINT-RESULT -->"

# Rendered at the top of every fix PR so a reviewer can't miss that approving
# the PR merges it. The re-lint gate arms GitHub auto-merge (squash) once the
# PR is promoted to ready; `master` requires an approval + the build check, so
# the PR merges the moment those are satisfied.
AUTOMERGE_NOTICE = (
    "> [!IMPORTANT]\n"
    "> **This PR is set to auto-merge (squash).** Once it has an approving review "
    "and the required build check passes, GitHub will merge it automatically — "
    "**approving this PR will merge it.** To prevent that, disable auto-merge "
    "(or convert the PR back to a draft) before approving."
)

# The body is composed BEFORE the model runs, but the auto-merge class is
# derived from the verdict at publish time (publish-gate.py `classify`). The
# publish job swaps the notice above for this one — deterministically, via
# `--replace-notice judgment` — on judgment-class PRs, so the body never
# promises an auto-merge the workflow didn't arm. AUTOMERGE_NOTICE therefore
# describes deterministic-class PRs only.
JUDGMENT_NOTICE = (
    "> [!IMPORTANT]\n"
    "> **This PR requires a human review decision — auto-merge is NOT armed.** "
    "Its fixes include judgment-class changes (claim corrections, structural "
    "repairs), so approving does not merge it by itself: the PR-review sweep "
    "arms auto-merge only after its own gates pass, or a human merges manually."
)

# The glow-up lane's notice: these PRs are the product of a whole-page rehab
# and exist to be human-reviewed. Auto-merge is never armed and the review
# sweep never stamps them; it assigns the reviewers instead.
HUMAN_REVIEW_NOTICE = (
    "> [!IMPORTANT]\n"
    "> **Glow-up PR — human review required.** Auto-merge is never armed on "
    "glow-up PRs and the automated PR-review sweep never approves them; it "
    "assigns the reviewers. Adjudicate the Backlog executed / Backlog declined "
    "tables below and merge manually."
)

# Glow-up body sections — keep in lockstep with record-review.py's
# MODE_PR_SECTIONS["glowup"] (test_compose_pr_body.py cross-imports both).
GLOWUP_SECTIONS = [
    "Why this page",
    "Backlog executed",
    "Backlog declined",
    "Secondary sweep",
    "Screenshot check",
    "Verification",
]

# The interactive /glow-up command's improvement taxonomy
# (.claude/commands/glow-up.md §5) — the secondary sweep the model runs after
# working the banked backlog.
GLOWUP_TAXONOMY = [
    "Style improvements",
    "Structural fixes",
    "Code formatting",
    "Terminology corrections",
    "Link improvements",
    "Image and diagram improvements",
    "Content enhancements",
]

# Related but distinct: the `blocker:` rule list in
# .claude/commands/docs-review/scripts/vale-deterministic-fixes.yaml drives
# which Vale findings the PR review renders as 🚨 blockers. This set is keyed
# on category (not rule) and decides fix-vs-defer for the content-review PR
# body; keep the two aligned when adding correctness-class rules.
# Vale categories whose fix has exactly one correct form and preserves meaning —
# safe to pre-bucket as a fix candidate. Everything else (passive voice,
# wordiness, hedging, em-dash density, tone, punctuation style …) starts as a
# deferral; the model promotes any it decides to apply.
HIGH_CONF_VALE = {
    "spelling", "nomenclature", "substitution", "inclusive language",
    "repeated word", "spacing", "agreement", "plurals", "difficulty qualifier",
}


def read_json(path: Path | None):
    if not path or not path.is_file():
        return None
    try:
        return json.loads(path.read_text())
    except (OSError, json.JSONDecodeError):
        return None


# ---- finding collection -----------------------------------------------------
#
# Each finding becomes a dict {label, source, detail, fix}: `label` names it,
# `source` is the authoritative pointer for the Fixes table, `detail` is a short
# context line for the deferral list, `fix` is True when it is pre-bucketed as a
# high-confidence fix candidate. `errors` accumulates artifacts that failed.


def _truncate(s: str, n: int = 160) -> str:
    s = " ".join((s or "").split())
    return s if len(s) <= n else s[: n - 1] + "…"


def _fmt_int(n) -> str:
    try:
        return f"{int(n):,}"
    except (TypeError, ValueError):
        return str(n)


def collect(verified, vale, readthrough, frontmatter) -> tuple[list[dict], list[str]]:
    findings: list[dict] = []
    errors: list[str] = []

    # Verified claims: contradicted/mismatch @ high confidence -> fix candidate;
    # contradicted/mismatch @ lower confidence or unverifiable -> deferral.
    if isinstance(verified, dict):
        if verified.get("errors"):
            errors.append("verified-claims")
        for v in verified.get("verdicts") or []:
            verdict = (v.get("verdict") or "").lower()
            conf = (v.get("confidence") or "").lower()
            if verdict in ("contradicted", "mismatch", "framing-drift"):
                loc = v.get("line_range") or ""
                tag = " — framing drift (value accurate, meaning drifted)" if verdict == "framing-drift" else ""
                findings.append({
                    "label": f"Claim ({v.get('claim_id', '?')}{', ' + loc if loc else ''}): "
                             f"{_truncate(v.get('text', ''))}{tag}",
                    "source": _truncate(v.get("source", ""), 200) or "(no source pointer)",
                    "detail": _truncate(v.get("evidence", "")),
                    "fix": conf == "high",
                    # Structured location, for consumers that need to match a
                    # finding to an applied fix (record-page-findings.py). The
                    # renderers read label/source/detail/fix and ignore these.
                    "category": "claim",
                    "line_range": v.get("line_range") or "",
                })
            elif verdict == "unverifiable":
                # Distinguish a retryable turn-budget failure from a genuine
                # no-source unverifiable — the two must never read identically
                # downstream (a budget failure is worth retrying; "no source
                # exists" is not).
                cap = bool(v.get("turn_cap_exhausted"))
                tag = " — unverifiable (verifier turn budget exhausted; retryable)" if cap else " — unverifiable"
                findings.append({
                    "label": f"Claim ({v.get('claim_id', '?')}): {_truncate(v.get('text', ''))}{tag}",
                    "source": _truncate(v.get("source", ""), 200) or "(verifier did not converge)",
                    "detail": _truncate(v.get("evidence", "")) or "verification did not converge",
                    "fix": False,
                    "category": "claim",
                    "line_range": v.get("line_range") or "",
                })
    elif verified is not None:
        errors.append("verified-claims (unexpected shape)")

    # Vale: high-confidence mechanical categories -> fix candidate; style -> deferral.
    if isinstance(vale, list):
        for f in vale:
            cat = (f.get("category") or "style").lower()
            line = f.get("line")
            loc = f"L{line}" if line else ""
            findings.append({
                "label": f"Vale {cat}{' (' + loc + ')' if loc else ''}: {_truncate(f.get('message', ''))}",
                "source": "`STYLE-GUIDE.md` (Vale)",
                "detail": _truncate(f.get("message", "")),
                "fix": cat in HIGH_CONF_VALE,
                "category": "vale",
                "line_range": f"L{line}" if isinstance(line, int) else "",
            })
    elif vale is not None:
        errors.append("vale-findings (unexpected shape)")

    # Readthrough: local_repair -> fix candidate; reconception -> deferral (flag only).
    if isinstance(readthrough, dict):
        if readthrough.get("errors"):
            errors.append("readthrough")
        for f in readthrough.get("findings") or []:
            fix_class = (f.get("fix_class") or "reconception").lower()
            loc = f.get("line_range") or ""
            findings.append({
                "label": f"Readthrough {f.get('failure_mode', 'finding')}"
                         f"{' (' + loc + ')' if loc else ''}: \"{_truncate(f.get('anchor_quote', ''), 100)}\"",
                "source": "readthrough coherence pass",
                "detail": _truncate(f.get("proposed_fix", "")),
                "fix": fix_class == "local_repair",
                "category": "readthrough",
                "line_range": loc,
            })
    elif readthrough is not None:
        errors.append("readthrough (unexpected shape)")

    # Frontmatter: alias collisions are real violations (fix); menu-parent gaps
    # are usually legacy patterns (defer for a human).
    if isinstance(frontmatter, dict):
        for ffile in frontmatter.get("files") or []:
            for col in ffile.get("alias_collisions") or []:
                findings.append({
                    "label": f"Frontmatter alias collision: `{col.get('alias', '?')}`",
                    "source": "`.frontmatter-validation.json`",
                    "detail": _truncate(json.dumps(col)),
                    "fix": True,
                    "category": "frontmatter",
                    "line_range": "",
                })
            for mp in ffile.get("menu_parents") or []:
                if mp.get("parent_exists_in_menu") is False:
                    findings.append({
                        "label": f"Frontmatter menu parent `{mp.get('parent', '?')}`"
                                 f" (menu `{mp.get('menu_name', '?')}`) not found",
                        "source": "`.frontmatter-validation.json`",
                        "detail": "parent_exists_in_menu: false — often a legacy secondary-menu pattern; verify before changing",
                        "fix": False,
                        "category": "frontmatter",
                        "line_range": "",
                    })

    return findings, errors


# ---- section rendering ------------------------------------------------------


def render_fixes(findings: list[dict]) -> str:
    fixes = [f for f in findings if f["fix"]]
    head = (
        "## Fixes applied\n\n"
        "<!-- Pre-stubbed from high-confidence pre-step findings. Keep a row ONLY\n"
        "     for a fix you actually applied and fill its Correction; move every\n"
        "     row you did not apply down to \"Findings not applied\" with a reason. -->\n\n"
        "| Claim / finding | Authoritative source | Correction |\n"
        "| --- | --- | --- |\n"
    )
    if not fixes:
        return head + "| _No high-confidence fix candidates pre-stubbed._ | | |\n"
    rows = "".join(
        f"| {f['label']} | {f['source']} | <TODO: correction, or move to Findings not applied> |\n"
        for f in fixes
    )
    return head + rows


def render_deferrals(findings: list[dict], path: str) -> str:
    deferrals = [f for f in findings if not f["fix"]]
    head = (
        "## Findings not applied\n\n"
        "<!-- One line of reasoning each (why it's judgment-level, not a\n"
        "     high-confidence fix). Add any rows you moved down from above. -->\n\n"
    )
    if deferrals:
        # A finding may carry a pre-composed `reason` (deterministic deferrals,
        # e.g. the flag-only Search Console row); otherwise the model fills it.
        body = "".join(
            f"- **{f['label']}** — {f.get('reason') or '<TODO: why judgment-level>'}"
            + (f" _(context: {f['detail']})_" if f["detail"] else "")
            + "\n"
            for f in deferrals
        )
    else:
        body = "- _Nothing judgment-level was pre-found. Add any finding you chose not to apply._\n"
    footer = (f"\nThe items above are banked for the automated glow-up lane, "
              f"which executes a page's accumulated deferrals under human "
              f"review — or run `/glow-up {path}` to work them now.\n")
    return head + body + footer


def render_screenshot(gates: dict | None) -> str:
    """Pre-fill the section when the source has no content images; else a TODO.

    Gates default-safe: a missing/None gate falls back to the model-run TODO.
    """
    head = "## Screenshot check\n\n"
    if gates and not gates.get("has_images", True):
        return head + (
            "No images. The page source references no screenshots, diagrams, or other "
            "content images (only the generic shared `meta_image` card, if any), so there "
            "is nothing to verify. _(Determined from the source; the screenshot pass was "
            "skipped.)_"
        )
    n = (gates or {}).get("image_count")
    hint = f" {n} image reference(s) detected in source." if n else ""
    return head + (
        f"<TODO: per image — current / stale (what differs) / unverifiable; "
        f'or "No images." if the page references none.{hint}>'
    )


def render_rendered_content(gates: dict | None) -> str:
    """Pre-fill "Skipped" when the source has no content-bearing includes.

    Plain prose, code tabs, callouts, and stepper chrome assemble no content the
    source markdown doesn't already show, so there is no render-time residue to
    check and no `make build` needed. A non-chrome shortcode (or a missing gate)
    falls back to the model-run TODO.
    """
    head = "## Rendered content\n\n"
    if gates and not gates.get("needs_render_pass", True):
        sc = gates.get("shortcodes") or []
        used = (
            "only render-safe chrome (" + ", ".join(f"`{s}`" for s in sc) + ")"
            if sc else "no shortcodes, partials, or includes"
        )
        return head + (
            f"Skipped — the page source uses {used}, so the rendered HTML and markdown "
            "carry no content beyond the source prose (nothing data-sourced or "
            "partial-included to fact-check). No `make build` or rendered pass required. "
            "_(Determined from the source.)_"
        )
    trig = ", ".join(f"`{s}`" for s in (gates or {}).get("nonchrome_shortcodes", [])[:8])
    hint = f" Content-bearing shortcode(s) requiring the pass: {trig}." if trig else ""
    return head + (
        f"<TODO: run `make build`, then check the HTML view for render-time content "
        f"(shortcode/partial/`data`-sourced) and verify any checkable claims in that residue, "
        f"or confirm clean.{hint}>"
    )


def render_verification(artifacts: dict, errors: list[str]) -> str:
    lines = ["## Verification\n\n"]
    # The re-lint gate swaps LINT_PLACEHOLDER for the authoritative result. The
    # "do not edit" hint rides in a trailing HTML comment so it guides the model
    # but never renders in the published body; the label is `make lint` only —
    # build isn't stamped here (it's left to the PR's normal CI).
    lines.append(
        f"- `make lint`: {LINT_PLACEHOLDER} <!-- stamped by the workflow re-lint gate; leave this line as-is -->\n"
    )
    lines.append("- Pre-step artifacts:\n")
    for name, summary in artifacts.items():
        lines.append(f"  - `{name}`: {summary}\n")
    if errors:
        lines.append(
            f"- ⚠️ Artifacts that failed or had an `errors` field: {', '.join(sorted(set(errors)))}. "
            "Note the gap and review with what's available.\n"
        )
    return "".join(lines)


def artifact_inventory(verified, vale, readthrough, frontmatter) -> dict:
    inv: dict[str, str] = {}

    if isinstance(verified, dict):
        vs = verified.get("verdicts") or []
        contra = sum(1 for v in vs if (v.get("verdict") or "").lower() in ("contradicted", "mismatch"))
        unver = sum(1 for v in vs if (v.get("verdict") or "").lower() == "unverifiable")
        inv[".verified-claims.json"] = f"{len(vs)} verdict(s); {contra} contradicted/mismatch, {unver} unverifiable"
    else:
        inv[".verified-claims.json"] = "missing"

    inv[".vale-findings.json"] = f"{len(vale)} finding(s)" if isinstance(vale, list) else "missing"

    if isinstance(readthrough, dict):
        fnd = readthrough.get("findings") or []
        ran = readthrough.get("ran")
        inv[".readthrough-findings.json"] = f"ran={ran}, {len(fnd)} finding(s)"
    else:
        inv[".readthrough-findings.json"] = "missing"

    if isinstance(frontmatter, dict):
        files = frontmatter.get("files") or []
        cols = sum(len(f.get("alias_collisions") or []) for f in files)
        inv[".frontmatter-validation.json"] = f"{len(files)} file(s); {cols} alias collision(s)"
    else:
        inv[".frontmatter-validation.json"] = "missing"

    return inv


def low_ctr_finding(queue: dict) -> dict | None:
    """The flag-only Search Console deferral, when selection flagged the page.

    Always `fix: False`: a low CTR is a signal for a human to look at the
    title/meta_desc (via /seo-analyze), never something the worker rewrites —
    meta rewrites are the canonical slop risk this pipeline is built to avoid.
    """
    a = (queue.get("articles") or [{}])[0]
    g = (a.get("signals") or {}).get("gsc") or {}
    if not g.get("low_ctr_flag"):
        return None
    median = ((queue.get("reader_signals") or {}).get("gsc") or {}).get("median_ctr")
    detail = f"{_fmt_int(g.get('impressions'))} impressions at {g.get('ctr', 0) * 100:.2f}% CTR"
    if median:
        detail += f" vs. corpus median {median * 100:.2f}%"
    return {
        "label": "Search opportunity: high impressions with below-median CTR — "
                 "the title/meta_desc may under-sell this page in search",
        "source": "Search Console (reader-signals export)",
        "detail": detail,
        "reason": "flag-only by design — title/meta_desc rewrites are a human call (`/seo-analyze`)",
        "fix": False,
    }


def compose(queue: dict, verified, vale, readthrough, frontmatter, gates=None) -> str:
    path = ((queue.get("articles") or [{}])[0]).get("path", "")
    findings, errors = collect(verified, vale, readthrough, frontmatter)
    lcf = low_ctr_finding(queue)
    if lcf:
        findings.append(lcf)
    inv = artifact_inventory(verified, vale, readthrough, frontmatter)

    return "\n".join([
        AUTOMERGE_NOTICE,
        "",
        _rp.render(queue).rstrip(),
        "",
        render_fixes(findings).rstrip(),
        "",
        render_deferrals(findings, path).rstrip(),
        "",
        render_screenshot(gates).rstrip(),
        "",
        render_rendered_content(gates).rstrip(),
        "",
        render_verification(inv, errors).rstrip(),
        "",
    ])


def compose_glowup(queue: dict, backlog: dict | None, verified, vale,
                   readthrough, frontmatter, gates=None) -> str:
    """The glow-up PR body draft: banked backlog pre-stubbed, taxonomy sweep
    stubbed, same assemble-then-judge contract as the fix body."""
    inv = artifact_inventory(verified, vale, readthrough, frontmatter)
    _, errors = collect(verified, vale, readthrough, frontmatter)

    try:
        provenance = _rp.render(queue).rstrip()
    except Exception:  # noqa: BLE001 — a provenance hiccup must not block the draft
        provenance = "## Why this page\n\n_Selected by the glow-up backlog score._"

    banked = (backlog or {}).get("banked") or []
    notes = (backlog or {}).get("notes") or []
    executed = ["## Backlog executed\n"]
    executed.append(
        "<!-- One row per banked finding you executed; move the rest to "
        "Backlog declined with a one-line reason. Every banked item must land "
        "in one of the two tables. -->\n")
    if banked:
        executed.append("| Banked finding | Source PR | What changed |")
        executed.append("| --- | --- | --- |")
        for b in banked:
            text = str(b.get("text", "")).replace("|", "\\|")
            src = f"#{b.get('source_pr')}" if b.get("source_pr") else "findings record"
            # A previously-declined row is real debt, but the reviewer needs to
            # see that a glow-up already turned it down once — otherwise a
            # decline loop looks like fresh work every cycle.
            if b.get("source") == "glowup-declined":
                src += " (declined)"
            executed.append(f"| {text} | {src} | <TODO> |")
    elif backlog and backlog.get("degraded"):
        # The counters that selected this page could not be backed by anything.
        # Saying "taxonomy-only glow-up" here — as this did before — reads as
        # "the page had nothing outstanding", which is the opposite of true.
        n = int((backlog or {}).get("skipped_findings") or 0)
        flag = " and a clarity flag" if (backlog or {}).get("clarity_flag") else ""
        why = "; ".join(notes) if notes else "no prior review PR could be read"
        executed.append("> [!WARNING]")
        executed.append(f"> **Backlog recovery failed.** The ledger records {n} "
                        f"deferred finding(s){flag} for this page, but none could be "
                        f"recovered ({why}). This run is a taxonomy sweep only. The "
                        "backlog is preserved and the page stays eligible for a "
                        "later glow-up — do not treat this as a clean page.")
        heads = (backlog.get("recovery") or {}).get("heads_queried") or []
        if heads:
            executed.append("")
            executed.append("_Heads queried: "
                            + ", ".join(f"`{h}`" for h in heads) + "._")
    else:
        executed.append("_No banked backlog for this page"
                        + (f" ({'; '.join(notes)})" if notes else "")
                        + " — taxonomy-only glow-up._")

    declined = [
        "## Backlog declined\n",
        "<TODO: banked findings you decided against, one line of reasoning each — "
        'or "None.">',
    ]

    sweep = ["## Secondary sweep\n"]
    sweep.append("<!-- The /glow-up taxonomy, applied after the backlog. Note what "
                 'you changed per category, or "No changes." -->\n')
    for cat in GLOWUP_TAXONOMY:
        sweep.append(f"- **{cat}**: <TODO>")

    return "\n".join([
        HUMAN_REVIEW_NOTICE,
        "",
        provenance,
        "",
        "\n".join(executed),
        "",
        "\n".join(declined),
        "",
        "\n".join(sweep),
        "",
        render_screenshot(gates).rstrip(),
        "",
        render_verification(inv, errors).rstrip(),
        "",
    ])


def replace_notice(body_file: Path, kind: str) -> int:
    """Swap the composed AUTOMERGE_NOTICE for the class-appropriate notice,
    in place. Deterministic and idempotent: already-swapped bodies no-op, and
    a body carrying neither notice (shouldn't happen — the compose fallback
    emits AUTOMERGE_NOTICE too) warns without failing the publish."""
    notices = {"judgment": JUDGMENT_NOTICE}
    replacement = notices[kind]
    try:
        body = body_file.read_text()
    except OSError as e:
        print(f"::warning::compose-pr-body: {body_file} unreadable ({e}); "
              "notice not swapped", file=sys.stderr)
        return 0
    if replacement in body:
        print(f"compose-pr-body: {kind} notice already present; no-op", file=sys.stderr)
        return 0
    if AUTOMERGE_NOTICE not in body:
        print(f"::warning::compose-pr-body: auto-merge notice not found in "
              f"{body_file}; notice not swapped", file=sys.stderr)
        return 0
    body_file.write_text(body.replace(AUTOMERGE_NOTICE, replacement, 1))
    print(f"compose-pr-body: swapped auto-merge notice -> {kind}", file=sys.stderr)
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--queue")
    p.add_argument("--out", help="output path (default: stdout)")
    p.add_argument("--verified-claims", default=".verified-claims.json")
    p.add_argument("--vale-findings", default=".vale-findings.json")
    p.add_argument("--readthrough", default=".readthrough-findings.json")
    p.add_argument("--frontmatter", default=".frontmatter-validation.json")
    p.add_argument("--repo-root", default=".")
    p.add_argument("--replace-notice", choices=["judgment"],
                   help="swap the composed auto-merge notice in --body-file for "
                        "this class's notice, then exit (publish-job mode)")
    p.add_argument("--body-file",
                   help="the PR body draft to edit in place (with --replace-notice)")
    p.add_argument("--mode", choices=["fix", "glowup"], default="fix",
                   help="body template: the fix lane's (default) or the glow-up lane's")
    p.add_argument("--backlog", default=".glowup-backlog.json",
                   help="glow-up backlog JSON (build-glowup-backlog.py output; glowup mode)")
    args = p.parse_args()

    if args.replace_notice:
        if not args.body_file:
            p.error("--replace-notice requires --body-file")
        return replace_notice(Path(args.body_file), args.replace_notice)
    if not args.queue:
        p.error("--queue is required (unless --replace-notice)")

    root = Path(args.repo_root)
    queue = json.loads(Path(args.queue).read_text())

    # Compute the screenshot/rendered gates from the article source. Default-safe:
    # an unreadable source leaves gates=None, and the renderers fall back to the
    # model-run TODO (both passes run) rather than skipping anything.
    gates = None
    src = (queue.get("articles") or [{}])[0].get("path", "")
    try:
        if src and (root / src).is_file():
            gates = _rg.analyze((root / src).read_text())
            print(
                f"compose-pr-body: gates — has_images={gates['has_images']}, "
                f"needs_render_pass={gates['needs_render_pass']} "
                f"(shortcodes: {', '.join(gates['shortcodes']) or 'none'})",
                file=sys.stderr,
            )
    except OSError:
        gates = None

    if args.mode == "glowup":
        body = compose_glowup(
            queue,
            read_json(root / args.backlog),
            read_json(root / args.verified_claims),
            read_json(root / args.vale_findings),
            read_json(root / args.readthrough),
            read_json(root / args.frontmatter),
            gates,
        )
    else:
        body = compose(
            queue,
            read_json(root / args.verified_claims),
            read_json(root / args.vale_findings),
            read_json(root / args.readthrough),
            read_json(root / args.frontmatter),
            gates,
        )
    if args.out:
        Path(args.out).write_text(body)
        print(f"compose-pr-body: wrote {args.out}", file=sys.stderr)
    else:
        sys.stdout.write(body)
    return 0


if __name__ == "__main__":
    sys.exit(main())
