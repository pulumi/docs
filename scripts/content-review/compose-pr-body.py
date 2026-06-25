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
correction prose, the one-line deferral reasons, and the screenshot / rendered
observations.

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

LINT_PLACEHOLDER = "<!-- LINT-RESULT -->"

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
            if verdict in ("contradicted", "mismatch"):
                loc = v.get("line_range") or ""
                findings.append({
                    "label": f"Claim ({v.get('claim_id', '?')}{', ' + loc if loc else ''}): "
                             f"{_truncate(v.get('text', ''))}",
                    "source": _truncate(v.get("source", ""), 200) or "(no source pointer)",
                    "detail": _truncate(v.get("evidence", "")),
                    "fix": conf == "high",
                })
            elif verdict == "unverifiable":
                findings.append({
                    "label": f"Claim ({v.get('claim_id', '?')}): {_truncate(v.get('text', ''))} — unverifiable",
                    "source": _truncate(v.get("source", ""), 200) or "(verifier did not converge)",
                    "detail": _truncate(v.get("evidence", "")) or "verification did not converge",
                    "fix": False,
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
                })
            for mp in ffile.get("menu_parents") or []:
                if mp.get("parent_exists_in_menu") is False:
                    findings.append({
                        "label": f"Frontmatter menu parent `{mp.get('parent', '?')}`"
                                 f" (menu `{mp.get('menu_name', '?')}`) not found",
                        "source": "`.frontmatter-validation.json`",
                        "detail": "parent_exists_in_menu: false — often a legacy secondary-menu pattern; verify before changing",
                        "fix": False,
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
        body = "".join(
            f"- **{f['label']}** — <TODO: why judgment-level>"
            + (f" _(context: {f['detail']})_" if f["detail"] else "")
            + "\n"
            for f in deferrals
        )
    else:
        body = "- _Nothing judgment-level was pre-found. Add any finding you chose not to apply._\n"
    footer = f"\nFor the judgment-level items above, run `/glow-up {path}`.\n"
    return head + body + footer


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


def compose(queue: dict, verified, vale, readthrough, frontmatter) -> str:
    path = ((queue.get("articles") or [{}])[0]).get("path", "")
    findings, errors = collect(verified, vale, readthrough, frontmatter)
    inv = artifact_inventory(verified, vale, readthrough, frontmatter)

    return "\n".join([
        _rp.render(queue).rstrip(),
        "",
        render_fixes(findings).rstrip(),
        "",
        render_deferrals(findings, path).rstrip(),
        "",
        "## Screenshot check\n\n<TODO: per image — current / stale (what differs) / unverifiable; "
        "or \"No images.\" if the page references none.>",
        "",
        "## Rendered content\n\n<TODO: HTML view + customer-facing markdown view — note any leaked "
        "shortcode syntax or shared-source residue, or confirm clean.>",
        "",
        render_verification(inv, errors).rstrip(),
        "",
    ])


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--queue", required=True)
    p.add_argument("--out", help="output path (default: stdout)")
    p.add_argument("--verified-claims", default=".verified-claims.json")
    p.add_argument("--vale-findings", default=".vale-findings.json")
    p.add_argument("--readthrough", default=".readthrough-findings.json")
    p.add_argument("--frontmatter", default=".frontmatter-validation.json")
    p.add_argument("--repo-root", default=".")
    args = p.parse_args()

    root = Path(args.repo_root)
    queue = json.loads(Path(args.queue).read_text())
    body = compose(
        queue,
        read_json(root / args.verified_claims),
        read_json(root / args.vale_findings),
        read_json(root / args.readthrough),
        read_json(root / args.frontmatter),
    )
    if args.out:
        Path(args.out).write_text(body)
        print(f"compose-pr-body: wrote {args.out}", file=sys.stderr)
    else:
        sys.stdout.write(body)
    return 0


if __name__ == "__main__":
    sys.exit(main())
