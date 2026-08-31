#!/usr/bin/env python3
"""The Sentinel — deterministic merge-gate evaluator for the v3 review workflow.

One blocking check-run answers "is this PR mergeable?" from four gates:

  G1 review-ran         a current review exists at head SHA (or none is
                        required: mechanical PRs, external contributions)
  G2 findings-answered  every 🚨/❓ finding on the author card carries a
                        REVIEW_STATE disposition (or is checked off)
  G3 right-approver     a human member of every matrix-required team approved
  G4 infra-evidence     infra paths carry a green staging/pulumi-test-io
                        commit status at the current head SHA
  G5 oversized-ack      review:oversized PRs replace G1/G2 with an explicit
                        `sentinel:oversized-ack` in the approving review body

Everything here is a pure function of GitHub API state plus the base-ref
routing config: NO model, NO AWS, and — because the workflow runs on
`pull_request_target` with write permissions — NO checkout or execution of
PR code, ever (test_sentinel.py asserts the workflow keeps that invariant).

Conclusion mapping is where merge gates silently rot, so it is explicit:
`success` only when every gate is ok; any red ⇒ `failure`; any gate that
ERRORED (a team-membership lookup failed, the state block is corrupt) ⇒
`action_required` — never `neutral`/`skipped`, which GitHub counts as
PASSING for a required check. `neutral` is reserved for drafts and for
report-only mode, where the real verdict rides inside the summary.

`review:waived` is the break-glass: the check concludes success with a loud
banner naming the waiving actor — except gate G4, which has no waiver (the
proposal's "no waiver, no shortcut" for infra; the incident path when
staging itself is broken is an admin-bypass merge, which rulesets log).

I/O lives behind the `Gh` wrapper (subprocess `gh api`, the
resolve-handler.py pattern) so tests substitute a stub. Team-membership
reads need an org-scoped token (the default GITHUB_TOKEN cannot read team
membership): the workflow passes PULUMI_BOT_TOKEN as $GH_TOKEN_TEAM_READ,
used for that one endpoint only.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_REPO_ROOT = _HERE.parent.parent
sys.path.insert(0, str(_HERE))
import review_state  # noqa: E402
import routing  # noqa: E402


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


_DOCS_REVIEW_SCRIPTS = _REPO_ROOT / ".claude" / "commands" / "docs-review" / "scripts"
_compose = _load("sentinel_compose", _DOCS_REVIEW_SCRIPTS / "compose-review.py")
_replay = _load("sentinel_replay", _HERE / "replay-mechanical.py")

AUTHOR_MARKER = _compose.AUTHOR_MARKER
BRIEF_MARKER = _compose.BRIEF_MARKER
FOOTER_SENTINEL = "<!-- CLAUDE_REVIEW_FOOTER -->"
HEAD_MARKER_RE = re.compile(r"<!-- CLAUDE_REVIEW_HEAD ([0-9a-f]{7,40}) -->")
LEGACY_MARKER_RE = re.compile(r"<!-- CLAUDE_REVIEW 1/\d+ -->")
HISTORY_SHA_RE = re.compile(r"\(([0-9a-f]{7,40})\)")
STRIP_OPEN = "<!-- SENTINEL_STRIP -->"
STRIP_CLOSE = "<!-- /SENTINEL_STRIP -->"
STAGING_STATUS_CONTEXT = "staging/pulumi-test-io"
OVERSIZED_ACK = "sentinel:oversized-ack"
BREAK_GLASS = "override: any write-access human can apply `review:waived` (logged)"

CHECK_NAME = "Sentinel"


class SentinelDataError(Exception):
    """An API read failed in a way that must surface as action_required."""


# ---- GitHub I/O ---------------------------------------------------------


class Gh:
    """Thin `gh api` wrapper; every method is stubbed in tests."""

    def __init__(self, repo: str, pr: int):
        self.repo = repo
        self.pr = pr

    def _run(self, args: list[str], token_env: str | None = None) -> str:
        env = None
        if token_env and os.environ.get(token_env):
            env = dict(os.environ)
            env["GH_TOKEN"] = os.environ[token_env]
        result = subprocess.run(
            ["gh", *args], text=True, capture_output=True, check=True, env=env,
        )
        return result.stdout

    def get_pr(self) -> dict:
        return json.loads(self._run(["api", f"repos/{self.repo}/pulls/{self.pr}"]))

    def list_files(self) -> list[dict]:
        out = self._run(["api", "--paginate", f"repos/{self.repo}/pulls/{self.pr}/files"])
        return json.loads(out)

    def list_issue_comments(self) -> list[dict]:
        out = self._run(["api", "--paginate", f"repos/{self.repo}/issues/{self.pr}/comments"])
        return json.loads(out)

    def list_reviews(self) -> list[dict]:
        out = self._run(["api", "--paginate", f"repos/{self.repo}/pulls/{self.pr}/reviews"])
        return json.loads(out)

    def get_commit_statuses(self, sha: str) -> list[dict]:
        out = self._run(["api", "--paginate", f"repos/{self.repo}/commits/{sha}/statuses"])
        return json.loads(out)

    def get_permission(self, actor: str) -> str:
        """Collaborator permission. Failure raises SentinelDataError."""
        try:
            out = self._run(
                ["api", f"repos/{self.repo}/collaborators/{actor}/permission", "--jq", ".permission"]
            )
        except subprocess.CalledProcessError as exc:
            raise SentinelDataError(f"permission lookup failed for {actor}: {exc.stderr.strip()[:200]}") from exc
        return out.strip()

    def get_team_membership(self, org: str, team_slug: str, user: str) -> str:
        """Returns 'active', 'pending', or 'none'.

        A clean 404 means "not a member" (returns 'none'); any other failure
        raises SentinelDataError so G3 errors instead of lying red. Uses the
        org-scoped token when the workflow provides one.
        """
        try:
            out = self._run(
                ["api", f"orgs/{org}/teams/{team_slug}/memberships/{user}", "--jq", ".state"],
                token_env="GH_TOKEN_TEAM_READ",
            )
            return out.strip() or "none"
        except subprocess.CalledProcessError as exc:
            stderr = (exc.stderr or "").strip()
            if "HTTP 404" in stderr or "Not Found" in stderr:
                return "none"
            raise SentinelDataError(
                f"team membership lookup failed ({org}/{team_slug}/{user}): {stderr[:200]}"
            ) from exc

    def get_label_events(self) -> list[dict]:
        out = self._run(
            ["api", "--paginate", f"repos/{self.repo}/issues/{self.pr}/timeline"]
        )
        return [e for e in json.loads(out) if e.get("event") == "labeled"]

    def patch_issue_comment(self, comment_id, body: str) -> None:
        self._run(
            ["api", "--method", "PATCH", f"repos/{self.repo}/issues/comments/{comment_id}",
             "-f", f"body={body}"]
        )


# ---- Gate results -------------------------------------------------------


@dataclass
class Gate:
    name: str
    status: str  # ok | red | error | skip
    message: str


@dataclass
class Verdict:
    conclusion: str
    title: str
    summary: str
    head_sha: str
    gates: list[Gate] = field(default_factory=list)
    would_be: str | None = None
    blocking_ids: list[str] = field(default_factory=list)

    def to_json(self) -> dict:
        return {
            "conclusion": self.conclusion,
            "title": self.title,
            "summary": self.summary,
            "head_sha": self.head_sha,
            "would_be": self.would_be,
            "gates": [{"gate": g.name, "status": g.status, "message": g.message} for g in self.gates],
            "blocking_ids": self.blocking_ids,
        }


# ---- Helpers ------------------------------------------------------------


def _find_comment(comments: list[dict], marker: str) -> dict | None:
    for c in comments:
        if marker in (c.get("body") or ""):
            return c
    return None


def _find_legacy_comment(comments: list[dict]) -> dict | None:
    for c in comments:
        body = c.get("body") or ""
        if LEGACY_MARKER_RE.search(body) and AUTHOR_MARKER not in body:
            return c
    return None


def _body_matches_head(body: str, head_sha: str) -> bool:
    m = HEAD_MARKER_RE.findall(body)
    if m:
        return any(head_sha.startswith(sha) or sha.startswith(head_sha) for sha in m)
    history = HISTORY_SHA_RE.findall(body)
    if history:
        last = history[-1]
        return head_sha.startswith(last) or last.startswith(head_sha)
    return False


def _card_rows(body: str, heading_prefixes: tuple[str, ...]) -> list[dict]:
    """Finding rows from the sections whose ### heading starts with a prefix."""
    rows: list[dict] = []
    in_section = False
    for line in body.splitlines():
        if line.startswith("#### "):
            in_section = False  # Style suggestions H4 ends the finding rows
            continue
        if line.startswith("### "):
            in_section = any(line[4:].startswith(p) for p in heading_prefixes)
            continue
        if line.startswith(FOOTER_SENTINEL):
            break
        if in_section and line.startswith("|"):
            parsed = _compose.parse_finding_line(line)
            if parsed and parsed["id"] != "F?":
                rows.append(parsed)
    return rows


def _strip_brief_for_summary(body: str) -> str:
    lines = []
    for line in body.splitlines():
        if line.startswith(FOOTER_SENTINEL):
            break
        if line.strip() in (BRIEF_MARKER,) or HEAD_MARKER_RE.match(line.strip()):
            continue
        lines.append(line)
    return "\n".join(lines).strip()


def _mechanical_and_claims(pr_detail: dict, files: list[dict]) -> tuple[bool, bool, list[str]]:
    """Run the tightened bar over the reconstructed diff. Fail-closed.

    The claims-overlay signal for routing is derived from the bar's own
    reason strings (pricing-sensitive path or a Layer-A prose hit) rather
    than a second classification pass — one classifier, one vocabulary.
    """
    try:
        diff_text = _replay.build_pr_diff(files)
        pr_data = _replay.build_pr_data(pr_detail, files)
        tc = _replay.tc
        file_diffs = tc.split_files(diff_text)
        file_flags = [tc.classify_file(p, d) for p, d in file_diffs]
        ok, reasons = tc.classify_mechanical(pr_data, file_flags, diff_text, _REPO_ROOT)
        # The marketing claims OVERLAY stacks only on pricing-sensitive
        # changes; an ordinary Layer-A prose hit already makes the PR
        # substantive via the bar and routes to the subject's own approver.
        claims = any("pricing-sensitive" in r for r in reasons)
        return ok, claims, reasons
    except Exception as exc:  # noqa: BLE001 — fail closed, never crash the gate
        return False, False, [f"classifier error (treated as substantive): {exc}"]


def _team_org_slug(team_ref: str) -> tuple[str, str]:
    org, _, slug = team_ref.partition("/")
    return org, slug


# ---- Evaluation ---------------------------------------------------------


def evaluate(gh: Gh, config: routing.Config, *, report_only: bool = False) -> Verdict:
    pr = gh.get_pr()
    head_sha = (pr.get("head") or {}).get("sha") or ""
    labels = {(l.get("name") or "") for l in (pr.get("labels") or [])}
    author = (pr.get("user") or {}).get("login") or ""

    if pr.get("draft"):
        return Verdict(
            conclusion="neutral", title="Draft — not evaluated",
            summary="Draft PRs are not gated; the sentinel evaluates on ready-for-review.",
            head_sha=head_sha,
        )

    files = gh.list_files()
    comments = gh.list_issue_comments()
    reviews = gh.list_reviews()

    mechanical, claims, mech_reasons = _mechanical_and_claims(pr, files)
    paths = [f["filename"] for f in files]
    resolution = routing.resolve_lanes(paths, mechanical, claims, config)

    # External-contributor lane: fail closed — an API failure means the
    # stricter (internal) gates apply.
    external = False
    try:
        external = gh.get_permission(author) not in ("admin", "write", "maintain")
    except SentinelDataError:
        external = False
    skip_gates = set((config.external_contributors or {}).get("skip_gates") or []) if external else set()

    author_card = _find_comment(comments, AUTHOR_MARKER)
    brief = _find_comment(comments, BRIEF_MARKER)
    legacy = _find_legacy_comment(comments) if author_card is None else None
    oversized = "review:oversized" in labels

    gates: list[Gate] = []
    blocking_ids: list[str] = []

    # G1 review-ran -------------------------------------------------------
    if oversized:
        gates.append(Gate("G1 review-ran", "skip", "oversized — see G5"))
    elif "review-ran" in skip_gates:
        gates.append(Gate(
            "G1 review-ran", "skip",
            "external contribution — auto-review does not run for external "
            "contributions; the approving reviewer's review is the review",
        ))
    elif mechanical:
        gates.append(Gate("G1 review-ran", "ok", "mechanical change — no review required"))
    elif author_card and _body_matches_head(author_card.get("body") or "", head_sha):
        gates.append(Gate("G1 review-ran", "ok", f"review current at `{head_sha[:9]}`"))
    elif legacy and _body_matches_head(legacy.get("body") or "", head_sha):
        gates.append(Gate(
            "G1 review-ran", "ok",
            "legacy (v2) review current at head (grandfathered)",
        ))
    else:
        gates.append(Gate(
            "G1 review-ran", "red",
            f"No current review for `{head_sha[:9]}` — push to refresh, comment "
            "`@claude #update-review`, or flip the PR to draft and back to ready.",
        ))

    # G2 findings-answered ------------------------------------------------
    if oversized:
        gates.append(Gate("G2 findings-answered", "skip", "oversized — see G5"))
    elif "findings-answered" in skip_gates:
        gates.append(Gate("G2 findings-answered", "skip", "external contribution"))
    elif mechanical:
        gates.append(Gate("G2 findings-answered", "ok", "no review, no findings"))
    elif author_card:
        body = author_card.get("body") or ""
        try:
            state = review_state.parse_state(body) or review_state.empty_state()
        except ValueError:
            gates.append(Gate(
                "G2 findings-answered", "error",
                "The REVIEW_STATE block on the review comment is corrupt — "
                "ask a maintainer to regenerate the review.",
            ))
            state = None
        if state is not None:
            rows = _card_rows(body, ("🚨", "❓"))
            undecided = [
                r["id"] for r in rows
                if not r["checked"] and r["id"] not in state.get("findings", {})
            ]
            blocking_ids = undecided
            if undecided:
                ids = ", ".join(undecided)
                gates.append(Gate(
                    "G2 findings-answered", "red",
                    f"{len(undecided)} finding(s) undecided ({ids}) — fix and push, "
                    f"or reply with your reasoning, e.g. "
                    f"`@claude F3 is wrong because <why> #update-review` or "
                    f"`@claude I know what I'm doing, mark everything resolved #update-review`.",
                ))
            else:
                gates.append(Gate("G2 findings-answered", "ok", "every finding answered"))
    elif legacy:
        try:
            vp = _load("sentinel_validate_pinned", _DOCS_REVIEW_SCRIPTS / "validate-pinned.py")
            outstanding = len(vp.extract_bucket_bullets(legacy.get("body") or "", "🚨 Outstanding"))
        except Exception as exc:  # noqa: BLE001
            gates.append(Gate("G2 findings-answered", "error", f"legacy comment unparsable: {exc}"))
            outstanding = None
        if outstanding is not None:
            if outstanding > 0:
                gates.append(Gate(
                    "G2 findings-answered", "red",
                    f"{outstanding} 🚨 Outstanding finding(s) on the legacy review — "
                    "work them per CONTRIBUTING §Working the review to zero.",
                ))
            else:
                gates.append(Gate("G2 findings-answered", "ok", "legacy review clean"))
    else:
        gates.append(Gate("G2 findings-answered", "skip", "no review present — see G1"))

    # G3 right-approver ---------------------------------------------------
    latest: dict[str, dict] = {}
    for r in reviews:
        user = (r.get("user") or {}).get("login") or ""
        if user and r.get("state") != "COMMENTED":
            # Oldest-first; keep the last stateful review per user. COMMENTED
            # never voids an approval (matching GitHub's own latestReviews
            # semantics); stale-on-push is the ruleset's dismissal job.
            latest[user] = r
    approvers = [
        r for r in latest.values()
        if r.get("state") == "APPROVED"
        and (r.get("user") or {}).get("type") != "Bot"
        and (r.get("user") or {}).get("login") not in set(config.bots or [])
    ]
    if not resolution.roles:
        gates.append(Gate("G3 right-approver", "ok", "no human approval required (mechanical)"))
    else:
        missing: list[str] = []
        errors: list[str] = []
        for role in sorted(resolution.roles):
            team_ref = config.teams.get(role, "")
            org, slug = _team_org_slug(team_ref)
            satisfied = False
            for r in approvers:
                login = (r.get("user") or {}).get("login") or ""
                try:
                    if gh.get_team_membership(org, slug, login) == "active":
                        satisfied = True
                        break
                except SentinelDataError as exc:
                    errors.append(str(exc))
            if not satisfied and not errors:
                missing.append(team_ref)
        if errors:
            gates.append(Gate(
                "G3 right-approver", "error",
                "Couldn't verify team membership — re-run the check. " + errors[0],
            ))
        elif missing:
            names = ", ".join(f"**{m}**" for m in missing)
            gates.append(Gate(
                "G3 right-approver", "red",
                f"Needs approval from a member of {names} — no qualifying human "
                "approval yet (bot approvals never count).",
            ))
        else:
            gates.append(Gate("G3 right-approver", "ok", "matrix-required approval present"))

    # G4 infra-evidence ---------------------------------------------------
    if resolution.staging_evidence_required:
        statuses = gh.get_commit_statuses(head_sha)
        green = any(
            s.get("context") == STAGING_STATUS_CONTEXT and s.get("state") == "success"
            for s in statuses
        )
        if green:
            gates.append(Gate("G4 infra-evidence", "ok", f"staging deploy green at `{head_sha[:9]}`"))
        else:
            gates.append(Gate(
                "G4 infra-evidence", "red",
                f"Infra change: no green staging deploy at `{head_sha[:9]}` — a "
                "tools-team member comments `/deploy-staging`. (Not waivable.)",
            ))
    else:
        gates.append(Gate("G4 infra-evidence", "skip", "no infra paths"))

    # G5 oversized-ack ----------------------------------------------------
    if oversized:
        acked = any(OVERSIZED_ACK in (r.get("body") or "") for r in approvers)
        if acked:
            gates.append(Gate("G5 oversized-ack", "ok", "reviewer acknowledged the skipped auto-review"))
        else:
            gates.append(Gate(
                "G5 oversized-ack", "red",
                "Oversized PR skipped auto-review — the approving reviewer must "
                f"include `{OVERSIZED_ACK}` in the approval body.",
            ))
    else:
        gates.append(Gate("G5 oversized-ack", "skip", "not oversized"))

    # ---- Conclusion -----------------------------------------------------
    waived = "review:waived" in labels
    any_error = any(g.status == "error" for g in gates)
    reds = [g for g in gates if g.status == "red"]
    infra_red = any(g.name.startswith("G4") and g.status == "red" for g in gates)

    if any_error:
        conclusion = "action_required"
        title = "Couldn't evaluate — action required"
    elif waived:
        if infra_red:
            conclusion = "failure"
            title = "Waived, but infra evidence has no waiver"
        else:
            conclusion = "success"
            title = "WAIVED"
    elif reds:
        conclusion = "failure"
        title = f"{len(reds)} gate(s) red"
    else:
        conclusion = "success"
        title = "All gates green"

    # ---- Summary --------------------------------------------------------
    parts: list[str] = []
    if waived:
        actor = _waive_actor(gh)
        parts.append(f"## ⚠️ WAIVED by @{actor}\n\nMerge gates bypassed via `review:waived` "
                     "(logged). The table below shows what the verdict would have been.")
        if infra_red:
            parts.append("**Infra staging evidence is NOT waivable** — gate G4 stands red.")
    if brief:
        parts.append(_strip_brief_for_summary(brief.get("body") or ""))
    if external:
        parts.append(
            "_External contribution: the automated review does not run for external "
            "contributions — the approving reviewer's review is the review._"
        )
    if mechanical:
        parts.append("_Classified mechanical under the tightened bar — no human review required._")
    table = ["| Gate | Status | Detail |", "|---|---|---|"]
    icon = {"ok": "✅", "red": "🔴", "error": "🟠", "skip": "➖"}
    for g in gates:
        msg = g.message + (f" — {BREAK_GLASS}" if g.status == "red" and not g.name.startswith("G4") else "")
        table.append(f"| {g.name} | {icon[g.status]} {g.status} | {msg} |")
    parts.append("\n".join(table))
    summary = "\n\n".join(p for p in parts if p)

    verdict = Verdict(
        conclusion=conclusion, title=title, summary=summary,
        head_sha=head_sha, gates=gates, blocking_ids=blocking_ids,
    )

    if report_only:
        verdict.would_be = verdict.conclusion
        verdict.summary = f"**REPORT-ONLY — would be: `{verdict.conclusion}`**\n\n" + verdict.summary
        verdict.title = f"Report-only (would be: {verdict.conclusion})"
        verdict.conclusion = "neutral"
    return verdict


def _waive_actor(gh: Gh) -> str:
    try:
        events = gh.get_label_events()
    except Exception:  # noqa: BLE001
        return "unknown"
    actor = "unknown"
    for e in events:
        if (e.get("label") or {}).get("name") == "review:waived":
            actor = (e.get("actor") or {}).get("login") or "unknown"
    return actor


# ---- Status strip -------------------------------------------------------


def update_strip(gh: Gh, verdict: Verdict, comments: list[dict] | None = None) -> bool:
    """Patch the one-line ⛔ strip into the author card. Idempotent."""
    comments = comments if comments is not None else gh.list_issue_comments()
    card = _find_comment(comments, AUTHOR_MARKER)
    if card is None:
        return False
    body = card.get("body") or ""
    if verdict.conclusion in ("failure", "action_required"):
        n = len(verdict.blocking_ids)
        what = f"{n} item(s) block merge" if n else "merge is blocked"
        strip = (f"{STRIP_OPEN}\n⛔ **{what}** — fix and push, or reply "
                 f"`@claude <your reasoning> #update-review`. "
                 f"Details: the Sentinel check below.\n{STRIP_CLOSE}")
    else:
        if STRIP_OPEN not in body:
            return False  # nothing to clear; don't insert an empty pair
        strip = f"{STRIP_OPEN}\n{STRIP_CLOSE}"

    if STRIP_OPEN in body and STRIP_CLOSE in body:
        pattern = re.compile(re.escape(STRIP_OPEN) + r".*?" + re.escape(STRIP_CLOSE), re.DOTALL)
        new_body = pattern.sub(lambda _: strip, body, count=1)
    else:
        lines = body.splitlines()
        insert_at = next((i + 1 for i, l in enumerate(lines) if l.startswith("## ")), 0)
        lines[insert_at:insert_at] = ["", strip]
        new_body = "\n".join(lines)
    if new_body != body:
        gh.patch_issue_comment(card["id"], new_body)
        return True
    return False


# ---- CLI ----------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--repo")
    parser.add_argument("--pr", type=int)
    parser.add_argument("--config", default=str(_REPO_ROOT / ".github" / "review-routing.yml"))
    parser.add_argument("--report-only", action="store_true")
    parser.add_argument("--update-strip", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        import test_sentinel  # noqa: PLC0415 — the pytest file doubles as the harness

        return test_sentinel.run_standalone()

    if not args.repo or not args.pr:
        parser.error("--repo and --pr are required")

    config = routing.load_config(args.config)
    gh = Gh(args.repo, args.pr)
    verdict = evaluate(gh, config, report_only=args.report_only)
    if args.update_strip and not args.report_only and not args.dry_run:
        update_strip(gh, verdict)
    print(json.dumps(verdict.to_json(), indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
