#!/usr/bin/env python3
"""The Sentinel — deterministic merge-gate evaluator for the v3 review workflow.

One blocking commit status answers "is this PR mergeable?" from four gates,
each also published as its own informational status (`Sentinel / <gate>`):

  review     a current review exists at head SHA (or none is required:
             mechanical PRs, fork PRs, and the PRs the review lane skips
             by policy — see below)
  findings   every 🚨/❓ finding on the author card carries a REVIEW_STATE
             disposition (or is checked off)
  staging    a change on `staging_evidence.paths` carries a successful
             staging deploy at the current head. That list is narrow on
             purpose — only what can break `pulumi up`, since a PR's own
             build already runs the pipeline in preview mode. NOT the same
             set as `domain:infra`: the matrix answers who reviews, this
             answers what must be applied to be believed
  oversized  review:oversized PRs replace review/findings with an explicit
             `/oversized-ack` in an approving review

The gates used to be numbered G1-G5. G3, the approver gate (who may approve,
which teams, which bots), is gone: it duplicated GitHub branch protection's
required-review rule while disagreeing with it at the edges, threw away an
approval on every push, rebases included, and needed an org-scoped token for
team reads. Branch protection decides who can approve and merge now, Eon
included. The numbers went with it; old comments and logs say G1/G2/G4/G5
for review/findings/staging/oversized.

One config-driven shortcut sits around the gates
(`.github/review-routing.yml`): `not_governed` lanes (Dependabot, the
generated-docs regens) conclude success with no gates evaluated. Those are
safe to exempt only because something else already posts a real approval and
arms auto-merge for them — see that file's NOT GOVERNED section.

`mechanical` skips the model review, never the approval branch protection
asks for. `review:prose-flagged` still demotes a mechanical PR to
substantive.

Everything here is a pure function of GitHub API state plus the base-ref
routing config: NO model, NO AWS, and — because the workflow runs on
`pull_request_target` with write permissions — NO checkout or execution of
PR code, ever (test_sentinel.py asserts the workflow keeps that invariant).

Conclusion mapping is where merge gates silently rot, so it is explicit:
`success` only when every gate is ok; any red ⇒ `failure`; any gate that
ERRORED (a permission lookup failed, the state block is corrupt) ⇒
`action_required` — never `neutral`/`skipped`, which GitHub counts as
PASSING for a required check. When every gate that isn't ok is only
PENDING (the first review is still running, a staging deploy is in flight)
the conclusion is `pending`, published as a pending commit status: it
blocks the merge exactly as a failure does, without a red X for something
nobody needs to act on yet. `neutral` is reserved for drafts and for
report-only mode, where the real verdict rides inside the summary. Report-only
is not a silent mode: the pinned status comment is maintained on every PR in
both modes, leading with a preview banner that says the check blocks nothing
yet and that it soon will (the status descriptions start "Preview"). Only the ⛔ author-card
strip stays enforcing-only — that one edits someone else's comment.

`review:waived` is the break-glass: the check concludes success with a loud
banner naming the waiving actor, whatever is red — G4 included. G4 used to
have no waiver, on the theory that the incident path when staging itself is
broken is an admin-bypass merge. That left a PR whose staging deploy could
not run (the testing workflow had been disabled, #22524) with no lever any
non-admin could pull, and two humans with approvals stuck behind it. A
waive is logged and names who applied it; that is the audit trail, and the
gates still run and still block by default.

"External contribution" means the head repo is a fork (or a deleted
fork) — never the author's permission level: a GitHub App such as
workprentice answers `none` on the collaborator endpoint yet pushes
same-repo branches that get the full review, and treating those as
external skipped G1/G2 on every one of them (2026-09-12 → 09-14). A PR
whose head-repo fact can't be read is internal (the stricter gates).

G1 asks for the review the pipeline means to run, never for one it has
decided not to. claude-code-review.yml skips ready PRs by policy, and each
skip needs its own answer here, or G1 stays red forever on a PR nothing
will ever review, and the only ways out are a waive or a forced full
review of a one-line change (#22417 was waived over a `date:` bump; #22429,
a clean trivial fix, sat red):

  - `review:trivial` / `review:frontmatter-only`. The label is triage's
    word, but anyone with triage access can apply it, so the Sentinel
    re-derives the shape from the diff with triage's own `classify_pr` and
    passes G1 only when the diff really is one of the two. A diff that
    doesn't fit is red, with the fix (`/new-review`). Neither shape implies
    mechanical: that bar is stricter (a deletions cap, the claims signal,
    only `updated`/`tags` in frontmatter), so "a clean trivial PR is
    mechanical anyway" was never safe to assume. Triage posts its
    `<!-- TRIAGE_PROSE -->` comment only when the prose check finds
    something, so the comment is advisory rather than evidence — except
    under `review:prose-flagged`, which promises nits only the comment can
    show, so a flagged PR whose comment is gone stays red.
  - Bot authors the lane skips (`REVIEW_LANE_SKIPPED_BOTS`) on branches it
    doesn't review (`REVIEW_LANE_REVIEWED_BOT_BRANCHES`), e.g. the
    marketing-web editions sync. Mirrored from the workflow; a test pins
    the two together.
  - `review:oversized`, which G5 owns.

Every one of them still needs the approval branch protection asks for: a
skipped review moves the reading to the approver, it never removes it. A review card at any
head keeps a PR on the review track instead, because a stale card with an
open finding must not pass on a skip label.

I/O lives behind the `Gh` wrapper (subprocess `gh api`) so tests
substitute a stub. One read needs an org-scoped token (the default
GITHUB_TOKEN can't read team membership): the waiver's team membership, on a
PR carrying `review:waived`. The workflow fetches PULUMI_BOT_TOKEN from ESC
only then and passes it as $GH_TOKEN_TEAM_READ, used for that endpoint only.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import re
import subprocess
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_REPO_ROOT = _HERE.parent.parent
sys.path.insert(0, str(_HERE))
import publish_guard  # noqa: E402
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
_worklist = None


def worklist():
    """review-worklist.py, loaded lazily and once (it execs two large
    siblings). It owns `PAGE_DELIMITER` / `join_pages`, the one place that
    knows how a split pinned review is put back together -- so the joining
    here is that function, never a second copy of it."""
    global _worklist
    if _worklist is None:
        _worklist = _load("sentinel_review_worklist", _DOCS_REVIEW_SCRIPTS / "review-worklist.py")
    return _worklist

AUTHOR_MARKER = _compose.AUTHOR_MARKER
BRIEF_MARKER = _compose.BRIEF_MARKER
FOOTER_SENTINEL = "<!-- CLAUDE_REVIEW_FOOTER -->"
HEAD_MARKER_RE = re.compile(r"<!-- CLAUDE_REVIEW_HEAD ([0-9a-f]{7,40}) -->")
# One page of a legacy (v2) pinned review. Any k, not just 1: a long review
# is several comments and every one of them is part of it. The marker is the
# body's FIRST line, which is pinned-comment.sh's own contract
# (`list_pinned_comments` reads `.body | split("\n") | .[0]`), so a review
# that merely quotes a marker is not mistaken for one.
LEGACY_PAGE_RE = re.compile(r"^<!-- CLAUDE_REVIEW (\d+)/(\d+) -->\s*$")
HISTORY_SHA_RE = re.compile(r"\(([0-9a-f]{7,40})\)")
STRIP_OPEN = "<!-- SENTINEL_STRIP -->"
STRIP_CLOSE = "<!-- /SENTINEL_STRIP -->"
STATUS_MARKER = "<!-- SENTINEL_STATUS -->"
# Ends every status comment, in both modes and on gateless bodies too. The
# preview banner used to be the only place that named a human channel, so
# enforcing mode — the one where a red row actually blocks — had none.
# Every role comment the Sentinel reads — author card, reviewer brief,
# legacy pages, its own status comment — must come from the bot that writes
# them. See `_find_comment` for what a missing provenance check cost.
BOT_LOGIN = "github-actions[bot]"
STAGING_STATUS_CONTEXT = "staging/pulumi-test-io"
# Identities whose `staging/pulumi-test-io` status the Sentinel will take as
# evidence. Anyone with push access can write a commit status, so an
# unattributed one is not evidence of anything.
STAGING_STATUS_WRITERS = frozenset({BOT_LOGIN, "pulumi-bot"})
# Who may have posted a page of a legacy (v2) review. The initial lane posts
# as github-actions[bot], but the v2 update lane runs claude-code-action with
# PULUMI_BOT_TOKEN, so a page it (re)posted — typically page 2 of a split
# review that grew on refresh — is pulumi-bot's. Reading only the first login
# made G2 report "legacy page 2 unreadable" on #21210, #21487 and #21149.
# The v3 role cards stay github-actions[bot]-only (`_find_comment`): nothing
# but the deterministic publish job ever writes them.
LEGACY_PAGE_WRITERS = frozenset({BOT_LOGIN, "pulumi-bot"})
# The workflow the staging lane dispatches, and the one G4 verifies against
# directly when the commit status is missing. See `_staging_evidence`.
STAGING_WORKFLOW_FILE = "testing-build-and-deploy.yml"
# The PRODUCTION deploy, which sits next to the staging one in the Actions
# sidebar with a near-identical name ("Build and deploy" vs "Build and
# deploy testing"). G4's instructions name it only to warn people off it:
# on #22524 someone looking for the staging deploy dispatched this one at an
# unmerged branch, and only a manual cancel kept it from shipping.
PRODUCTION_WORKFLOW_FILE = "build-and-deploy.yml"
# A review slash command, like `/update-review`: it counts only at the start
# of a line of the approving review's comment (command-gate.py's grammar,
# restated here because this file runs from a sparse checkout of
# scripts/review-v3 and can't import it). It replaced the bare
# `sentinel:oversized-ack` token, which matched anywhere.
OVERSIZED_ACK = "/oversized-ack"
_OVERSIZED_ACK_RE = re.compile(r"^[ \t]{0,3}/oversized-ack(?![\w-])", re.M | re.I)


def _has_oversized_ack(body: str) -> bool:
    return bool(_OVERSIZED_ACK_RE.search((body or "").replace("\r\n", "\n")))


BREAK_GLASS = (
    "override: a member of a routing team (`.github/review-routing.yml` `teams:`) "
    "can apply `review:waived` (logged)"
)




def _waive_can_clear(g: Gate) -> bool:
    """Whether recommending the waive for this gate would work: every red or
    errored gate (no gate reads the org-scoped token the waive needs)."""
    return g.status in ("red", "error")


# The merge box shows the status description and nothing else, so it has to
# answer "why can't I merge?" by itself, in words for someone who has never
# opened this file. "2 gate(s) red" sent people (pulumi/docs#22524) to a
# Details page whose gate table started two-thirds of the way down. Each
# phrase completes "Waiting on …"; the gate's row in the status comment says
# who acts and how. Shared with the author-card strip so the two agree.
def _waiting_on(g: Gate, n_blocking: int) -> str:
    gate = g.name
    cmd = next((f" ({c})" for c in ("/update-review", "/new-review") if c in g.message), "")
    if gate == "review":
        if "changes no files" in g.message:
            return "a diff to review"
        if "hasn't posted yet" in g.message:
            return "the automated review"
        return f"a current review{cmd}"
    if gate == "findings":
        n = n_blocking or "open"
        return f"answers to {n} finding{'' if n_blocking == 1 else 's'} (/update-review)"
    if gate == "staging":
        return "a staging deploy (running)" if g.status == "pending" else "a staging deploy"
    if gate == "oversized":
        return f"{OVERSIZED_ACK} in an approval"
    return g.name


_PLAIN_GATE = {"review": "the review", "findings": "the review's answers",
               "staging": "the staging deploy", "oversized": "the oversized ack"}


def _plain_join(items: list[str]) -> str:
    return " and ".join([", ".join(items[:-1]), items[-1]]) if len(items) > 1 else (items or [""])[0]

CHECK_NAME = "Sentinel"

# One commit status per gate, beside the required `Sentinel` status, so the
# merge box itself says which gate is red and what it wants -- the status
# comment is usually scrolled out of sight, and "Waiting on a and b" in one
# description ran out of room. Only `Sentinel` is required by the ruleset;
# these are informational. Statuses, not check-runs, for the reason
# publish_verdict.py gives (a check-run can land in a superseded suite).
GATE_CONTEXTS = {
    "review": "Sentinel / review",
    "findings": "Sentinel / findings",
    "staging": "Sentinel / staging",
    "oversized": "Sentinel / oversized",
}
STATUS_DESCRIPTION_MAX = 140


def _findings_short(ids: list[str]) -> str:
    shown = " ".join(ids[:4]) + (" …" if len(ids) > 4 else "")
    noun = "finding" if len(ids) == 1 else "findings"
    return f"{len(ids)} open {noun}: fix and push, or /update-review accept {shown}"


def _clip(text: str, limit: int = STATUS_DESCRIPTION_MAX) -> str:
    text = " ".join((text or "").replace("`", "").replace("**", "").split())
    return text if len(text) <= limit else text[:limit - 1] + "…"


def gate_statuses(verdict: "Verdict") -> list[dict]:
    """The per-gate commit statuses for this verdict. Each links where you act
    on it (`Gate.url`, then the verdict's per-gate link, then the PR); None
    only when the PR's URL is unknown, and publish_verdict.py fills in the PR. Skipped gates
    still get one, so a gate that stopped applying at this head turns green
    instead of keeping an old red."""
    out: list[dict] = []
    preview = bool(verdict.would_be)
    for g in verdict.gates:
        gid = g.name
        context = GATE_CONTEXTS.get(gid)
        if not context:
            continue
        if verdict.waived:
            state, desc = "success", f"waived: {g.message}" if g.status != "ok" else g.message
        elif g.status == "pending":
            state, desc = "pending", g.short or "Waiting on " + _waiting_on(g, len(verdict.blocking_ids))
        elif g.status == "red":
            state, desc = "failure", g.short or "Waiting on " + _waiting_on(g, len(verdict.blocking_ids))
        elif g.status == "error":
            state, desc = "error", g.short or "couldn't check -- re-run the Sentinel"
        elif g.status == "skip":
            state, desc = "success", f"n/a: {g.message}"
        else:
            state, desc = "success", g.message
        if preview and state != "success":
            state, desc = "success", f"Preview, not enforced: {desc}"
        out.append({"context": context, "state": state, "description": _clip(desc),
                    "target_url": g.url or verdict.links.get(gid) or verdict.links.get("pr") or None})
    return out


RETRY_SLEEP_S = 3


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
        # Reads retry a transient 5xx twice: one GitHub 500 on `pulls/N`
        # (run 35938827723) was enough to fail a whole evaluation. Writes
        # never retry — a PATCH that timed out may have landed.
        is_read = not any(a in ("-X", "--method") for a in args) and "--input" not in args
        for attempt in range(3 if is_read else 1):
            result = subprocess.run(
                ["gh", *args], text=True, capture_output=True, env=env,
            )
            if result.returncode == 0 or not re.search(r"HTTP 5\d\d", result.stderr or ""):
                break
            if attempt < 2:
                time.sleep(RETRY_SLEEP_S * (attempt + 1))
        if result.returncode != 0:
            # `check=True` would raise CalledProcessError, whose message is
            # the argv and an exit code — gh's actual explanation goes in
            # stderr, which that exception never prints. The permission bug
            # on PR #21642 cost a log dive and a guess for exactly this
            # reason: gh had said what was wrong and the traceback dropped
            # it. Keep the endpoint (the useful half of the argv) and the
            # stderr; drop the body, which is kilobytes of rendered markdown.
            endpoint = next((a for a in args if "/" in a and not a.startswith("-")), " ".join(args[:2]))
            raise SentinelDataError(
                f"gh {args[0]} {endpoint} failed (exit {result.returncode}): "
                f"{(result.stderr or '').strip()[:400] or '<no stderr>'}"
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

    def require_org_read(self) -> None:
        """Fail loudly when this process cannot read org team membership.

        GitHub answers **404** for an org resource the token cannot see,
        which is byte-identical to "not a member". The ESC fetch that
        supplies `GH_TOKEN_TEAM_READ` is `continue-on-error`, so without
        this probe a missing or expired token made every approver read as a
        non-member: every PR in the repo went red with "no qualifying human
        approval yet (bot approvals never count)" — blaming the approver —
        and `review:waived` was refused by the same lookup, because
        `_waive_state` asks the same endpoint. The whole repo deadlocks and
        nothing in the check output points at the token.

        Cheap and idempotent (an env-var read), so every org-scoped
        lookup runs it rather than trusting a single call site to.
        """
        if not os.environ.get("GH_TOKEN_TEAM_READ"):
            raise SentinelDataError(
                "no org-scoped token (GH_TOKEN_TEAM_READ is unset): team "
                "membership cannot be read, and GitHub answers 404 for an "
                "org it cannot see — which is indistinguishable from 'not a "
                "member'. Refusing to report an approval verdict on that. "
                "Check the ESC fetch step."
            )

    def _org_scoped_lookup(self, api_path: str, jq: str, what: str) -> str:
        """An org-scoped GET whose 404 means "no", not "I could not look".

        Both callers below need the same three things and got them by
        copy-paste, which promptly drifted: `get_repo_permission` was
        missing the `require_org_read` probe its own docstring claimed,
        so on a token-less run every approver would have answered "not an
        admin" -- the exact 404-means-two-things conflation the probe
        exists to stop, reintroduced one method below it.

        The rule: a clean 404 is a real answer ("none"); anything else
        raises, so the gate errors rather than reporting a block it could
        not verify."""
        self.require_org_read()
        try:
            out = self._run(["api", api_path, "--jq", jq],
                            token_env="GH_TOKEN_TEAM_READ")
            return out.strip() or "none"
        except SentinelDataError as exc:
            if "HTTP 404" in str(exc) or "Not Found" in str(exc):
                return "none"
            raise SentinelDataError(f"{what} lookup failed: {exc}") from exc

    def get_team_membership(self, org: str, team_slug: str, user: str) -> str:
        """Returns 'active', 'pending', or 'none'."""
        return self._org_scoped_lookup(
            f"orgs/{org}/teams/{team_slug}/memberships/{user}", ".state",
            f"team membership ({org}/{team_slug}/{user})")

    def list_commits(self) -> list[dict]:
        out = self._run(["api", "--paginate", f"repos/{self.repo}/pulls/{self.pr}/commits"])
        return json.loads(out)

    def compare_files(self, base: str, sha: str) -> list[dict]:
        """The files `sha` changes against its merge base with `base` — the
        PR's diff as it stood at that commit."""
        out = self._run(["api", f"repos/{self.repo}/compare/{base}...{sha}"])
        return json.loads(out).get("files") or []

    def get_label_events(self) -> list[dict]:
        out = self._run(
            ["api", "--paginate", f"repos/{self.repo}/issues/{self.pr}/timeline"]
        )
        return [e for e in json.loads(out) if e.get("event") == "labeled"]

    def get_workflow_runs(self, workflow_file: str, head_sha: str) -> list[dict]:
        """Completed runs of one workflow at an EXACT head SHA.

        Server-side filtered on `head_sha`, so this is a handful of rows at
        most and needs no pagination. Not `--paginate`: the runs endpoint
        returns an object, and merging those is a different shape.
        """
        out = self._run([
            "api",
            f"repos/{self.repo}/actions/workflows/{workflow_file}/runs"
            f"?head_sha={head_sha}&status=completed&per_page=100",
        ])
        return json.loads(out).get("workflow_runs") or []

    def get_workflow_state(self, workflow_file: str) -> str:
        """`active`, `disabled_manually`, `disabled_inactivity`, …"""
        return self._run([
            "api", f"repos/{self.repo}/actions/workflows/{workflow_file}", "--jq", ".state",
        ]).strip()

    def get_issue_comment(self, comment_id) -> dict:
        return json.loads(self._run(["api", f"repos/{self.repo}/issues/comments/{comment_id}"]))

    def patch_issue_comment(self, comment_id, body: str) -> None:
        self._run(
            ["api", "--method", "PATCH", f"repos/{self.repo}/issues/comments/{comment_id}",
             "-f", f"body={body}"]
        )

    def post_issue_comment(self, body: str) -> None:
        self._run(
            ["api", "--method", "POST", f"repos/{self.repo}/issues/{self.pr}/comments",
             "-f", f"body={body}"]
        )

    def delete_issue_comment(self, comment_id) -> None:
        self._run(
            ["api", "--method", "DELETE", f"repos/{self.repo}/issues/comments/{comment_id}"]
        )


# ---- Gate results -------------------------------------------------------


@dataclass
class Gate:
    name: str
    status: str  # ok | red | error | skip
    message: str
    # The gate's own commit-status description, which the merge box shows
    # and nothing else does (140 characters). Empty: derived from
    # `_waiting_on` on red, from `message` otherwise. See `gate_statuses`.
    short: str = ""
    # Where this gate's status "Details" link goes: where you act on it.
    # Empty: the verdict's per-gate link, else the PR.
    url: str = ""


@dataclass
class Verdict:
    conclusion: str
    title: str
    summary: str
    head_sha: str
    gates: list[Gate] = field(default_factory=list)
    would_be: str | None = None
    # The summary as it read before `_stamp_report_only` prepended the preview
    # paragraph. The status comment's gateless branches (not governed, no
    # gates) render the summary's first paragraph as their one informative
    # line; after stamping, that first paragraph is the preview text, so the
    # comment repeated its own banner and never said "Not governed — …".
    base_summary: str | None = None
    blocking_ids: list[str] = field(default_factory=list)
    # Facts a downstream auto-merge job keys on, so it never has to re-derive
    # them from the summary text: did the tightened bar call this PR
    # mechanical; is the PR governed at all (False = a not_governed lane, no
    # gates evaluated).
    mechanical: bool = False
    governed: bool = True
    # Whether `review:waived` was honored. The pinned status comment used to
    # read only `gates`, so on a waived PR it announced "2 of 5 gates need
    # attention before this can merge" and recommended the label that was
    # already applied and already working — while the status next to it
    # said success. A gate surface that contradicts the gate is the failure
    # the `_GATE_BLURB` phrasebook exists to prevent.
    waived: bool = False
    # Who applied an honored waive, or why the label was refused. A refusal
    # used to reach only the job summary, so the merge box and the status
    # comment kept inviting the person who had just applied the label to
    # apply it.
    waive_note: str = ""
    # Gate id -> where that gate's commit status links (the author card for
    # G1/G2). A gate with no entry links the workflow run.
    links: dict = field(default_factory=dict)

    def to_json(self) -> dict:
        return {
            "conclusion": self.conclusion,
            "title": self.title,
            "summary": self.summary,
            "head_sha": self.head_sha,
            "would_be": self.would_be,
            "gates": [{"gate": g.name, "status": g.status, "message": g.message} for g in self.gates],
            "gate_statuses": gate_statuses(self),
            "blocking_ids": self.blocking_ids,
            "mechanical": self.mechanical,
            "governed": self.governed,
            "waive_note": self.waive_note,
        }


# ---- Helpers ------------------------------------------------------------


def _find_comment(comments: list[dict], marker: str) -> dict | None:
    """The oldest bot-authored comment carrying `marker` (see `_find_comments`)."""
    found = _find_comments(comments, marker)
    return found[0] if found else None


def _find_comments(comments: list[dict], marker: str) -> list[dict]:
    """Every bot-authored comment carrying `marker`, oldest first.

    More than one means overlapping writers each created their own copy;
    `remove_status_comments` is the one caller that needs to see them all.

    PROVENANCE IS THE WHOLE POINT. This used to match the marker anywhere in
    any comment by anyone, and return the first hit. Comments come back
    oldest-first, so a PR author who posted an ordinary comment containing
    `<!-- CLAUDE_REVIEW_AUTHOR -->` before the review lane posted the real
    card owned G1 and G2 for the life of the PR: `_body_matches_head`
    passed against a head marker they control, `parse_state` read their
    empty state, and `_card_rows` found no findings. Reproduced — a card
    with three unanswered 🚨 went from `G2 red` to `G2 ok, blocking=[]`
    purely on comment ordering. `update_strip` then wrote the ⛔ banner into
    the forgery, so the real card never showed it either.

    The two conditions below are not new inventions; they are the contract
    the WRITER already enforces: `pinned-comment.sh`'s `list_role_comments`
    requires the marker to be an exact line among the body's first three,
    and only `github-actions[bot]` ever posts the card. The far less
    load-bearing triage-prose comment was already read this way; this
    function was the
    one place that checked neither, so it is now the only reader and both
    markers come through it.
    """
    found = []
    for c in comments:
        if (c.get("user") or {}).get("login") != BOT_LOGIN:
            continue
        # Exact line, first three lines — `list_role_comments`'s rule. A
        # marker merely quoted inside a body is not a role comment.
        lines = [ln.strip() for ln in (c.get("body") or "").splitlines()[:3]]
        if marker in lines:
            found.append(c)
    return found


def legacy_pages(comments: list[dict]) -> dict | None:
    """Every comment of a legacy (v2) pinned review, in page order.

    A v2 review too long for one GitHub comment is split across several,
    each stamped `<!-- CLAUDE_REVIEW k/N -->` on its first line. Its section
    tables -- 🚨 Outstanding, ⚠️ Low-confidence, 💡 Pre-existing -- are the
    tail of the document, so on a split review they are on the *later*
    pages: reading page 1 alone reports a review with no findings at all.

    Returns `{"pages": [comment, ...], "total": N, "missing": [k, ...]}`, or
    None when the PR has no legacy review. `missing` is the pages the
    markers promise and GitHub did not return; a caller that finds it
    non-empty has an incomplete review and must not treat it as parsed.
    """
    pages: dict[int, dict] = {}
    total = 0
    for c in comments:
        # Bot-authored only, same rule as `_find_comment`: the first-line
        # anchor below stops a quoted marker, but not a forged page. Both
        # identities the v2 lanes post under count (LEGACY_PAGE_WRITERS).
        if (c.get("user") or {}).get("login") not in LEGACY_PAGE_WRITERS:
            continue
        body = c.get("body") or ""
        # A v3 role card opens with a `1/1` marker of its own, so the role
        # markers still decide which surface a comment belongs to.
        if AUTHOR_MARKER in body or BRIEF_MARKER in body:
            continue
        m = LEGACY_PAGE_RE.match(body.split("\n", 1)[0])
        if not m:
            continue
        k, n = int(m.group(1)), int(m.group(2))
        total = max(total, n)
        pages.setdefault(k, c)   # a duplicate page: the oldest wins, as pinned-comment.sh does
    if not pages:
        return None
    return {"pages": [pages[k] for k in sorted(pages)], "total": total,
            "missing": [k for k in range(1, total + 1) if k not in pages]}


def _find_legacy_comment(comments: list[dict]) -> dict | None:
    """The legacy (v2) review as one comment: the first page's metadata,
    carrying *every* page's body joined in page order.

    Every caller reads `.get("body")` and means "the review". Returning page
    1 alone made a long v2 review look findings-free, which on pulumi/docs
    #21490 turned a `blocked` row into a `judge` row wearing an "approve
    as-is & merge" button, and passed this file's own G2 findings-answered
    gate as "legacy review clean". The whole point of "an unanswered 🚨 is
    blocked, never --force-able" is to stop exactly that.

    `review_pages` and `review_pages_missing` ride along on the returned
    dict so a caller can fail closed when GitHub did not return a page the
    markers promise, rather than parse what happens to be there.
    """
    found = legacy_pages(comments)
    if not found:
        return None
    wl = worklist()
    body = wl.join_pages(wl.PAGE_DELIMITER.join((c.get("body") or "") for c in found["pages"]))
    return {**found["pages"][0], "body": body,
            "review_pages": found["total"], "review_pages_missing": found["missing"]}


def _body_matches_head(body: str, head_sha: str) -> bool:
    m = HEAD_MARKER_RE.findall(body)
    if m:
        return any(head_sha.startswith(sha) or sha.startswith(head_sha) for sha in m)
    history = HISTORY_SHA_RE.findall(body)
    if history:
        last = history[-1]
        return head_sha.startswith(last) or last.startswith(head_sha)
    return False


def _card_rows(body: str, heading_prefixes: tuple[str, ...], *,
               include_unnumbered: bool = False) -> list[dict]:
    """Finding rows from the sections whose ### heading starts with a prefix.

    Rows still carrying the model's `F?` placeholder are dropped unless
    `include_unnumbered` asks for them. That default is a contract two
    siblings rely on and neither states: `sla-sweep.py` counts rows absent
    from REVIEW_STATE as unanswered, and `F?` is never a key in it -- so N
    placeholders would count N times against an author who has no id to
    answer with, feeding `review:author-stalled` and the 21-day auto-close.
    `collect.py` puts them on the /pr-review board. Only G2 wants them, and
    only in order to refuse the card outright, so only G2 asks."""
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
            if parsed and (include_unnumbered or parsed["id"] != "F?"):
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


PROSE_FLAGGED_LABEL = "review:prose-flagged"
TRIVIAL_LABEL = "review:trivial"
FRONTMATTER_ONLY_LABEL = "review:frontmatter-only"
# claude-code-review.yml's bot-author skip, verbatim: these authors' PRs get
# no review unless the head branch starts with one of these prefixes.
# `test_bot_skip_mirrors_the_review_lane` pins both to the workflow text.
REVIEW_LANE_SKIPPED_BOTS = ("pulumi-bot", "dependabot[bot]")
REVIEW_LANE_REVIEWED_BOT_BRANCHES = ("content-review/", "fix/broken-links-", "vale/brand-sync-")
# Named, not inlined, so `test_label_event_filter_covers_every_label_the_
# evaluator_reads` can derive the workflow's trigger list from the evaluator
# instead of restating it.
OVERSIZED_LABEL = "review:oversized"
# Set by the review lanes (claude-code-review.yml, claude-update.yml) inside
# their own runs, so it needs no label-event trigger: the Sentinel already
# re-evaluates on those workflows' `workflow_run` completion, after the label
# lands. `test_label_event_filter_covers_every_label_the_evaluator_reads`
# checks that route instead.
REVIEW_ERROR_LABEL = "review:error"
TRIAGE_PROSE_MARKER = "<!-- TRIAGE_PROSE -->"


def _is_external(pr_detail: dict) -> bool:
    """A fork PR (head repo ≠ base repo, or a deleted fork) is external.

    Fail closed: if the payload doesn't carry the head-repo fact at all, the
    PR is internal and the stricter gates apply. Permission is deliberately
    not consulted — see the module docstring.
    """
    head = pr_detail.get("head") or {}
    if "repo" not in head:
        return False
    head_repo = head.get("repo")
    if head_repo is None:
        return True  # deleted fork: GitHub nulls head.repo
    head_name = (head_repo.get("full_name") or "").lower()
    base_name = (((pr_detail.get("base") or {}).get("repo") or {}).get("full_name") or "").lower()
    if not head_name or not base_name:
        return False
    return head_name != base_name


def _mechanical_and_claims(
    pr_detail: dict, files: list[dict], labels: set[str] | frozenset[str] = frozenset()
) -> tuple[bool, bool, list[str]]:
    """Run the tightened bar over the reconstructed diff. Fail-closed.

    The claims-overlay signal for routing is derived from the bar's own
    reason strings (pricing-sensitive path or a Layer-A prose hit) rather
    than a second classification pass — one classifier, one vocabulary.

    `review:prose-flagged` demotes: triage's prose check (Haiku + Vale) ran
    on a short-circuited PR and found something, so the diff's shape alone
    no longer vouches for it. The bar is pure diff shape and cannot see the
    label, so the demotion lives here, where the labels are in hand.
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
        if ok and PROSE_FLAGGED_LABEL in labels:
            ok = False
            reasons = [f"`{PROSE_FLAGGED_LABEL}`: triage's prose check flagged this PR (demoted to substantive)"]
        return ok, claims, reasons
    except Exception as exc:  # noqa: BLE001 — fail closed, never crash the gate
        return False, False, [f"classifier error (treated as substantive): {exc}"]


def _shortcut_shape(pr_detail: dict, files: list[dict]) -> str | None:
    """The review-lane shortcut the diff itself qualifies for under triage's
    own bar (`classify_pr`): "trivial", "frontmatter-only", or None.

    The skip labels are triage's verdict on this same bar, so re-deriving it
    is what lets G1 honor a skip without trusting a label anyone with triage
    access can apply. Fail-closed: a file GitHub sends without a patch reads
    as binary (no shortcut), and a classifier error is None.
    """
    try:
        diff_text = _replay.build_pr_diff(files)
        pr_data = _replay.build_pr_data(pr_detail, files)
        tc = _replay.tc
        file_flags = [tc.classify_file(p, d) for p, d in tc.split_files(diff_text)]
        shape = tc.classify_pr(pr_data, file_flags)
    except Exception:  # noqa: BLE001 — fail closed, never crash the gate
        return None
    if shape.get("trivial"):
        return "trivial"
    if shape.get("frontmatter_only"):
        return "frontmatter-only"
    return None


def _review_lane_skipped_bot(pr_detail: dict) -> str | None:
    """The author, when the review lane's bot-author rule skips this PR."""
    author = (pr_detail.get("user") or {}).get("login") or ""
    branch = (pr_detail.get("head") or {}).get("ref") or ""
    if author in REVIEW_LANE_SKIPPED_BOTS and not branch.startswith(REVIEW_LANE_REVIEWED_BOT_BRANCHES):
        return author
    return None


def _author_card_nothing_blocks(body: str) -> bool:
    """Does the author card's header say nothing blocks merge?

    Reads the composer's own header line (`## Author action guide vN — …`)
    rather than re-counting rows, so the card and the gate agree by
    construction. Legacy/foreign headers (no such line) are never clean.
    """
    for line in body.splitlines():
        if line.startswith(_compose.AUTHOR_HEADER_PREFIX):
            return _compose.AUTHOR_HEADER_NOTHING_BLOCKS in line
    return False


# ---- link-only diffs -----------------------------------------------------

# A markdown link (text and target), an href, a bare URL, or a site-absolute
# path. Masking these leaves the sentence around them.
URL_TOKEN_RE = re.compile(
    r"\[[^\]\n]*\]\([^)\s]*\)|href=\"[^\"]*\"|https?://[^\s)\"'>]+|(?<![\w/])/[\w./-]*[\w/](?=[\s)\"'>]|$)"
)
_HUNK_HEAD_RE = re.compile(r"^@@ ")


def link_only_diff(files: list[dict]) -> bool:
    """True when every hunk swaps lines that are identical once links are
    masked and case is folded: the same sentence, only the link changed.

    A hunk with unpaired additions or deletions, a file with no patch, or a
    diff that changes nothing is not link-only. This is deliberately narrower
    than `classify_mechanical`'s bar, which counts any modified link as
    substantive: that bar decides whether a change needs a human at all,
    while this one decides whether it needs a *particular lane's* human.
    Shared with the /pr-review queue, which renders it as `shape:link-only`.
    """
    if not files:
        return False
    seen = False
    for f in files:
        patch = f.get("patch")
        if patch is None:
            return False
        added: list[str] = []
        removed: list[str] = []

        def flush() -> bool:
            nonlocal seen
            if len(added) != len(removed):
                return False
            for plus, minus in zip(added, removed):
                if plus == minus:
                    return False
                if URL_TOKEN_RE.sub("<url>", plus).lower() != URL_TOKEN_RE.sub("<url>", minus).lower():
                    return False
                seen = True
            added.clear()
            removed.clear()
            return True

        for line in patch.splitlines():
            if _HUNK_HEAD_RE.match(line):
                if not flush():
                    return False
            elif line.startswith("+"):
                added.append(line[1:])
            elif line.startswith("-"):
                removed.append(line[1:])
        if not flush():
            return False
    return seen


def _team_org_slug(team_ref: str) -> tuple[str, str]:
    org, _, slug = team_ref.partition("/")
    return org, slug


def _staging_evidence(gh: Gh, head_sha: str) -> str | None:
    """Has this exact head been deployed to staging successfully, ever?

    Two independent witnesses, either of which is sufficient:

      1. the `staging/pulumi-test-io` commit status, written by whichever
         lane ran the deploy;
      2. a completed, successful run of the staging workflow itself whose
         head SHA is this one.

    (2) exists because (1) is a *report* of the deploy, not the deploy: the
    status write is a separate API call after `gh run watch` returns, and a
    cancelled runner, a lost token or a dispatch whose `workflow_run`
    cascade never fired all leave a green deploy with no status. The
    run record is the deploy. Checking the status first keeps the common
    path to one API call.

    A failed run-history read is swallowed deliberately: it degrades to "no
    evidence found", which blocks the merge. Raising instead would turn an
    API hiccup into `action_required` on a PR that simply hasn't deployed
    yet — louder, and wrong about which of the two states it is in.

    Returns a human-readable witness, or None when there is no evidence.
    """
    for s in gh.get_commit_statuses(head_sha):
        if s.get("context") != STAGING_STATUS_CONTEXT or s.get("state") != "success":
            continue
        # A commit status needs only push access to write:
        #   gh api repos/OWNER/REPO/statuses/SHA -f state=success \
        #     -f context=staging/pulumi-test-io
        # …which made G4 a one-line bypass that, unlike a waive, nobody
        # sees. The run record below cannot be forged that way,
        # and review-routing.yml already calls it "the authoritative one".
        # Keep the status as a fast path, but only from an identity that
        # could actually have run the deploy.
        creator = ((s.get("creator") or {}).get("login") or "")
        if creator not in STAGING_STATUS_WRITERS:
            continue
        return f"staging status green at `{head_sha[:9]}` (by `{creator}`)"
    try:
        runs = gh.get_workflow_runs(STAGING_WORKFLOW_FILE, head_sha)
    except Exception:  # noqa: BLE001 — see docstring: degrade to "no evidence"
        return None
    for r in runs:
        if r.get("conclusion") == "success":
            return (
                f"staging deploy [run {r.get('id')}]({r.get('html_url')}) succeeded "
                f"at `{head_sha[:9]}`"
            )
    return None


# ---- Pushes that change nothing the gates looked at ----------------------
#
# A merge of the base, or a commit that changes nothing (the "kick CI" empty
# commit), moves the head without changing what the PR does. So does a
# rebase onto a newer base: the commits are new, the PR's own `+`/`-` lines
# are not. G1 carries its review across these (restamp-base-merge.py) and G4
# its staging deploy, because asking for the exact head made clicking
# "Update branch" spend another ~10-minute deploy (#22506), an empty commit
# reset the review and the deploy (#22524), and a rebase to clear a
# changelog conflict reset the review on a one-line PR (#22397). These
# helpers are the one test both gates use; collect.py and
# restamp-base-merge.py read them from here.


def _tree_sha(commit: dict) -> str:
    return ((commit.get("commit") or {}).get("tree") or {}).get("sha") or ""


def _changes_nothing(c: dict, prev: dict) -> bool:
    """`c` is a merge, or a one-parent commit on `prev` with `prev`'s tree."""
    parents = c.get("parents") or []
    if len(parents) >= 2:
        return True
    tree = _tree_sha(c)
    return (bool(tree) and tree == _tree_sha(prev) and len(parents) == 1
            and bool(prev.get("sha")) and parents[0].get("sha") == prev.get("sha"))


def changes_nothing_since(commits: list[dict], sha: str) -> bool:
    """True when `sha` is in the PR's commit list, is not its last commit,
    and every later commit is a merge (two parents) or changes nothing (the
    same tree as the commit before it). Whether a merge brought in only the
    base is `same_diff`'s question, not this one's."""
    shas = [c.get("sha") or "" for c in commits]
    idx = next((i for i, s in enumerate(shas) if s and sha and (s.startswith(sha) or sha.startswith(s))),
               None)
    if idx is None or idx == len(shas) - 1:
        return False
    return all(_changes_nothing(commits[i], commits[i - 1]) for i in range(idx + 1, len(commits)))


def history_allows_carry(commits: list[dict], sha: str) -> bool:
    """Whether the PR's history since `sha` could have left its changes
    alone: `sha` is in the commit list and only merges or no-op commits
    follow it, or `sha` is gone from the list entirely, which is what a
    rebase or other force-push leaves. Either way `same_diff` still has to
    agree before anything carries; this is only the cheap pre-filter. A
    commit list that couldn't be read (empty) answers no."""
    if not commits or not sha:
        return False
    shas = [c.get("sha") or "" for c in commits]
    if not any(s and (s.startswith(sha) or sha.startswith(s)) for s in shas):
        return True
    return changes_nothing_since(commits, sha)


def changed_lines(files: list[dict]) -> dict[str, list[str]]:
    """Per file, the sorted `+`/`-` lines of its patch. Hunk headers and
    context are left out because they move whenever the base moves; the
    changed lines themselves only move when the PR's content does."""
    out: dict[str, list[str]] = {}
    for f in files:
        name = f.get("filename") or f.get("path") or ""
        lines = [ln for ln in (f.get("patch") or "").splitlines()
                 if ln[:1] in "+-" and not ln.startswith(("+++", "---"))]
        out[name] = sorted(lines)
    return out


def same_diff(files_then: list[dict], files_now: list[dict]) -> bool:
    """Whether two snapshots of a PR's files carry the same changes. A merge
    of the base that resolved a conflict by editing a line the PR adds
    changes the content the review read, and must not count as base-only."""
    return changed_lines(files_then) == changed_lines(files_now)


def patchless_file_changed(files_then: list[dict], files_now: list[dict]) -> bool:
    """`same_diff` reads `patch`, which GitHub omits for large and binary
    files, so two patchless snapshots compare equal whatever changed. For
    those, the blob `sha` has to match on both sides; a missing one fails
    closed."""
    then = {(f.get("filename") or f.get("path") or ""): f for f in files_then}
    for f in files_now:
        if f.get("patch"):
            continue
        t = then.get(f.get("filename") or f.get("path") or "")
        if t is None or not f.get("sha") or f.get("sha") != t.get("sha"):
            return True
    return False


_CARRY_CLAUSE = ("since then only base merges, rebases or no-op commits, and the PR's own "
                 "changes are identical")


class _Carry:
    """Answers "is the PR at `sha` the PR at head?" for G4, reading
    the commit list once and only when a gate would otherwise be red. Any
    read that fails answers no, which leaves the gate as strict as before."""

    def __init__(self, gh: Gh, pr: dict, files_now: list[dict]):
        self.gh, self.files_now = gh, files_now
        self.base = (pr.get("base") or {}).get("ref") or ""
        self.head = (pr.get("head") or {}).get("sha") or ""
        self._commits: list[dict] | None = None
        self._answers: dict[str, bool] = {}

    def commits(self) -> list[dict]:
        if self._commits is None:
            try:
                self._commits = self.gh.list_commits()
            except Exception:  # noqa: BLE001 — fail closed: no carry
                self._commits = []
            # A list that doesn't end at the head (read just after a push)
            # can't say what came after; treat it as unreadable.
            if not self._commits or (self._commits[-1].get("sha") or "") != self.head:
                self._commits = []
        return self._commits

    def predecessors(self, limit: int = 3) -> list[str]:
        """The commits the head reaches by nothing but merges and no-op
        commits, newest first, head excluded. Bounded: each costs reads."""
        commits, out = self.commits(), []
        for i in range(len(commits) - 1, 0, -1):
            if not _changes_nothing(commits[i], commits[i - 1]):
                break
            out.append(commits[i - 1].get("sha") or "")
        return [s for s in out if s][:limit]

    def unchanged_since(self, sha: str) -> bool:
        if sha not in self._answers:
            self._answers[sha] = self._unchanged_since(sha)
        return self._answers[sha]

    def _unchanged_since(self, sha: str) -> bool:
        if not sha or not self.base or sha == self.head:
            return False
        if not history_allows_carry(self.commits(), sha):
            return False
        try:
            files_then = self.gh.compare_files(self.base, sha)
        except Exception:  # noqa: BLE001 — fail closed: no carry
            return False
        return same_diff(files_then, self.files_now) and not patchless_file_changed(
            files_then, self.files_now)


def _last_staging_failure(gh: Gh, head_sha: str) -> str:
    """The newest trusted `staging/pulumi-test-io` status at this head, as
    a sentence, when it says the deploy failed or never started; else ''.

    The sweep writes failure/error for a deploy that finished badly, and the
    auto lane writes error for one it couldn't dispatch. Either way the
    reason belongs on the G4 row, not one click away in a job log.
    """
    try:
        statuses = gh.get_commit_statuses(head_sha)
    except Exception:  # noqa: BLE001 — advice only; see _staging_gate
        return ""
    for s in statuses:  # newest first
        if s.get("context") != STAGING_STATUS_CONTEXT:
            continue
        if ((s.get("creator") or {}).get("login") or "") not in STAGING_STATUS_WRITERS:
            continue
        if s.get("state") not in ("failure", "error"):
            return ""
        desc = (s.get("description") or "staging deploy failed").rstrip(".").replace("|", "/")
        url = s.get("target_url")
        return f"**Last staging attempt: {desc}.**" + (f" ([details]({url}))" if url else "") + " "
    return ""


_IN_FLIGHT = frozenset({"queued", "in_progress", "waiting", "requested", "pending"})
_FAILED = frozenset({"failure", "cancelled", "timed_out", "startup_failure"})


def _staging_gate(gh: Gh, pr: dict, head_sha: str) -> Gate:
    """The staging gate when no deploy at this head has succeeded.

    It never asks a person to dispatch a workflow: the "Build and deploy
    testing" / "Build and deploy" names are one click apart in the Actions
    sidebar, and on #22524 someone dispatched production at an unmerged
    branch. The auto lane deploys on open and push, so the gate only says
    which state it is in, and each state's link is where you act:

      running   pending, linking the run
      failed    red, linking the failed run: "Re-run failed jobs" there can
                only redeploy staging
      disabled  red: an admin turns the workflow back on; ask in #docs
      never ran red: comment `/deploy-staging` (the dispatch failed, or the
                PR predates the auto lane)

    A failed read degrades to "never ran": the command is safe to repeat.
    """
    sha = head_sha[:9]
    try:
        runs = gh.get_workflow_runs(STAGING_WORKFLOW_FILE, head_sha)
    except Exception:  # noqa: BLE001 — see docstring
        runs = []
    running = next((r for r in runs if (r.get("status") or "") in _IN_FLIGHT), None)
    if running:
        return Gate("staging", "pending",
                    f"A staging deploy of `{sha}` is running ([run {running.get('id')}]"
                    f"({running.get('html_url')})). When it finishes, `staging-status.yml` re-checks "
                    "this gate within ~10 minutes; nothing to do meanwhile.",
                    short=f"Staging deploy of {sha} is running", url=running.get("html_url") or "")
    failed = next((r for r in runs if (r.get("conclusion") or "") in _FAILED), None)
    if failed:
        return Gate("staging", "red",
                    f"The staging deploy of `{sha}` failed ([run {failed.get('id')}]"
                    f"({failed.get('html_url')})). Open it and click **Re-run failed jobs**; "
                    "a re-run can only redeploy staging.",
                    short="Staging deploy failed: open it and click Re-run failed jobs",
                    url=failed.get("html_url") or "")
    try:
        state = gh.get_workflow_state(STAGING_WORKFLOW_FILE)
    except Exception:  # noqa: BLE001 — see docstring
        state = ""
    if state and state != "active":
        return Gate("staging", "red",
                    f"This PR changes the deploy itself, and staging deploys are turned off "
                    f"(the staging workflow is `{state}`), so none can run. Ask in `#docs`; "
                    "turning it back on needs a repo admin.",
                    short="Staging deploys are turned off: ask in #docs")
    why = _last_staging_failure(gh, head_sha)
    return Gate("staging", "red",
                why + f"This PR changes the deploy itself, and `{sha}` has no staging deploy "
                "yet. Comment `/deploy-staging` on this PR to start one.",
                short="No staging deploy yet: comment /deploy-staging")


def _gate_links(pr: dict, card_url: str) -> dict:
    """Where each gate's status links when the gate has no link of its own:
    the author card for review and findings (that's where they're answered),
    the Files tab for the oversized ack (that's where Approve is), and the
    PR itself for the rest. Never the Sentinel's own run page, which is for
    debugging the Sentinel."""
    pr_url = pr.get("html_url") or ""
    links = {"pr": pr_url}
    if card_url:
        links.update(review=card_url, findings=card_url)
    if pr_url:
        links["oversized"] = f"{pr_url}/files"
    return links


def _waive_state(gh: Gh, config: routing.Config, labels: set[str]) -> tuple[bool, str]:
    """Is the waive label present AND applied by someone entitled to apply it?

    The label alone is not the waive. A waive skips every gate, so the
    authority to apply one has to be at least the authority to approve
    something: the actor must be an ACTIVE member of a team named in
    `teams:` — any of them, not just the one this PR routes to. Scoping it
    to the required team would make a waive exactly as hard to get as the
    approval it bypasses, which defeats the one case it most needs to
    cover (the required approver is the PR's own author).

    Fails closed at every step. The actor can't be read, the membership
    lookup throws, the actor is on no routing team — all of those are "not
    waived", and the returned reason is surfaced so an unauthorized waive
    is visibly refused rather than silently ignored.

    Returns (waived, note) — note is '' when there is no label at all.
    """
    if config.waive.get("label", "review:waived") not in labels:
        return False, ""
    actor = _waive_actor(gh)
    if actor == "unknown":
        return False, "could not read who applied the waive label"
    for team_ref in sorted(set(config.teams.values())):
        org, slug = _team_org_slug(team_ref)
        try:
            if gh.get_team_membership(org, slug, actor) == "active":
                return True, actor
        except SentinelDataError:
            return False, (
                f"could not verify whether @{actor} may waive (team lookup "
                "failed)"
            )
    return False, (
        f"@{actor} is not an active member of any routing team "
        "(`.github/review-routing.yml` `teams:`)"
    )


# ---- Evaluation ---------------------------------------------------------




# Who may supply G5's ack: GitHub's own `author_association` on the review.
# Branch protection still needs a write-access approval to merge; this only
# keeps a passer-by (anyone can review a public repo) from supplying the ack,
# and it needs no API call or org token.
ACK_ASSOCIATIONS = frozenset({"OWNER", "MEMBER", "COLLABORATOR"})


def _oversized_ack(config: routing.Config, reviews: list[dict],
                   head_sha: str, author: str) -> str:
    """The login whose approval at this head carries `/oversized-ack`, or "".
    Not the author, not a bot, and an owner, org member or collaborator."""
    latest: dict[str, dict] = {}
    for r in reviews:
        user = (r.get("user") or {}).get("login") or ""
        if user and r.get("state") != "COMMENTED":
            latest[user] = r
    for login, r in latest.items():
        u = r.get("user") or {}
        if (r.get("state") == "APPROVED" and r.get("commit_id") == head_sha and login != author
                and u.get("type") != "Bot" and login not in set(config.bots or [])
                and (r.get("author_association") or "").upper() in ACK_ASSOCIATIONS
                and _has_oversized_ack(r.get("body") or "")):
            return login
    return ""


def _stamp_report_only(verdict: Verdict) -> Verdict:
    """Turn a real verdict into its report-only twin, in place.

    Report-only has three surfaces and they have to agree: the published
    status (`neutral`, which publish_verdict.py posts as a passing
    `success`), its description in the merge box, and the per-gate statuses
    (`gate_statuses`). `would_be` is
    what every one of them reports, and the only place the true conclusion
    survives, so it is set before `conclusion` is overwritten.
    """
    verdict.would_be = verdict.conclusion
    verdict.base_summary = verdict.summary
    verdict.summary = (
        f"**PREVIEW MODE — informational only, safe to ignore for now. This check "
        f"would be: `{verdict.conclusion}`.** Enforcement is coming: once it lands, "
        f"every gate below has to be green before the PR can merge.\n\n"
        + verdict.summary
    )
    verdict.title = f"Preview — would be: {verdict.conclusion} (not enforced yet)"
    verdict.conclusion = "neutral"
    return verdict


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

    # Automation lanes the Sentinel does not govern (Dependabot, the
    # generated-docs regens): success with the reason on record, no gates
    # evaluated. Logged like a waive so the digest can count them.
    ng_reason = routing.not_governed_reason(config, author, labels)
    if ng_reason:
        verdict = Verdict(
            conclusion="success", title="Not governed",
            summary=(f"**Not governed** — {ng_reason} (`.github/review-routing.yml` "
                     "`not_governed`). This automation lane merges on its own checks; "
                     "the Sentinel evaluates no gates for it."),
            head_sha=head_sha, governed=False,
        )
        if report_only:
            _stamp_report_only(verdict)
        return verdict

    files = gh.list_files()
    comments = gh.list_issue_comments()
    reviews = gh.list_reviews()

    mechanical, claims, mech_reasons = _mechanical_and_claims(pr, files, labels)
    paths = [f["filename"] for f in files]
    resolution = routing.resolve_lanes(paths, mechanical, claims, config)

    # External-contributor lane = fork head repo. Fail closed: no head-repo
    # fact in the payload means the stricter (internal) gates apply.
    external = _is_external(pr)
    skip_gates = set((config.external_contributors or {}).get("skip_gates") or []) if external else set()

    author_card = _find_comment(comments, AUTHOR_MARKER)
    brief = _find_comment(comments, BRIEF_MARKER)
    legacy = _find_legacy_comment(comments) if author_card is None else None
    # The label is the one source of truth. Computing size here instead
    # would flip PRs already reviewed and approved under the normal gates
    # (G1/G2 skipped, G5 newly red), and a forced /new-review could never put
    # an oversized PR back under them. #21936's race — this evaluation ran
    # before triage's label landed — is closed on the triage side: it
    # re-dispatches the Sentinel whenever it moves the label.
    oversized = OVERSIZED_LABEL in labels
    # The lanes the review pipeline skips by policy (module docstring). Only
    # for a PR that never got a review: a card or legacy comment at any head
    # keeps it on the review track.
    never_reviewed = author_card is None and legacy is None
    skip_label = next((lbl for lbl in (TRIVIAL_LABEL, FRONTMATTER_ONLY_LABEL) if lbl in labels), None)
    triage_prose = _find_comment(comments, TRIAGE_PROSE_MARKER) if skip_label else None
    skipped_bot = _review_lane_skipped_bot(pr)
    skip_standin = ""  # names the skipped lane when it satisfies G1
    skip_note = ""     # and the summary line that says so

    gates: list[Gate] = []
    blocking_ids: list[str] = []

    # G1 review-ran -------------------------------------------------------
    if not files:
        # GitHub hasn't computed the diff yet, or the branch nets to nothing.
        # First, because every lane below would otherwise wave it through:
        # the review lane skips it (`empty-diff`), and on a fork PR G1/G2 skip too — a fully green Sentinel with nobody
        # involved, and on a transient empty read, over a real diff.
        gates.append(Gate(
            "review", "red",
            "This PR changes no files, so there is nothing to review. If the diff "
            "is still being computed, push again to re-evaluate.",
        ))
    elif oversized:
        gates.append(Gate("review", "skip", "oversized — see the oversized gate"))
    elif "review-ran" in skip_gates:
        gates.append(Gate(
            "review", "skip",
            "external contribution — auto-review does not run for external "
            "contributions; the approving reviewer's review is the review",
        ))
    elif mechanical:
        gates.append(Gate("review", "ok", "mechanical change — no review required"))
    elif author_card and _body_matches_head(author_card.get("body") or "", head_sha):
        gates.append(Gate("review", "ok", f"review current at `{head_sha[:9]}`"))
    elif legacy and _body_matches_head(legacy.get("body") or "", head_sha):
        gates.append(Gate(
            "review", "ok",
            "legacy (v2) review current at head (grandfathered)",
        ))
    elif skip_label and never_reviewed:
        # The review lane skipped this PR on the label, and it is not
        # mechanical (that bar is stricter). The diff, not the label, decides
        # whether the skip was legitimate.
        shape = _shortcut_shape(pr, files)
        if shape is None:
            gates.append(Gate(
                "review", "red",
                f"No current review for `{head_sha[:9]}` — the review lane skipped this "
                f"PR as `{skip_label}`, but its diff is neither trivial nor "
                "frontmatter-only, so it needs the review. Comment `/new-review` to run it.",
            ))
        elif PROSE_FLAGGED_LABEL in labels and triage_prose is None:
            gates.append(Gate(
                "review", "red",
                f"No current review for `{head_sha[:9]}` — the review lane skipped this "
                f"PR as `{skip_label}`, and triage flagged prose issues "
                f"(`{PROSE_FLAGGED_LABEL}`) but its prose-check comment is missing, so "
                "nobody can see them. Comment `/new-review` to run a full review.",
            ))
        else:
            skip_standin = f"{shape} change"
            if triage_prose is not None:
                gates.append(Gate(
                    "review", "ok",
                    f"{skip_standin} — the review lane skipped it (`{skip_label}`); triage's "
                    "prose check stands in for the review (advisory nits in the triage comment)",
                ))
                skip_note = (f"_{skip_standin.capitalize()}: triage's prose-check comment stands "
                             "in for the review; a human approver is still required._")
            else:
                gates.append(Gate(
                    "review", "ok",
                    f"{skip_standin} — the review lane skipped it (`{skip_label}`) and "
                    "triage's prose check left no nits",
                ))
                skip_note = (f"_{skip_standin.capitalize()}: the review lane skips these, so the "
                             "approving reviewer's review is the review._")
    elif skipped_bot and never_reviewed:
        branch = (pr.get("head") or {}).get("ref") or ""
        skip_standin = f"`{skipped_bot}` automation PR"
        gates.append(Gate(
            "review", "ok",
            f"the review lane does not review `{skipped_bot}` PRs from `{branch}`, so "
            "the approver's review is the review",
        ))
        skip_note = (f"_Automation PR: the review lane does not review `{skipped_bot}` PRs "
                     "from this branch, so the approving reviewer's review is the review._")
    elif never_reviewed and REVIEW_ERROR_LABEL in labels:
        # The first review died before it posted. Nothing is in flight, so
        # this is red (and offers the waive), not "the review is running".
        gates.append(Gate(
            "review", "red",
            "The automated review errored before it posted; comment `/new-review` to retry.",
            short="the automated review errored (/new-review)",
        ))
    elif never_reviewed:
        # The first review is usually still running: the Sentinel posts on
        # open, minutes before the card. Telling the author to run a command
        # here sent them after something that was about to happen anyway.
        # Pending, not red: it blocks the merge all the same, and a red X
        # read as "something broke" for the 10-20 minutes every PR spends here.
        gates.append(Gate(
            "review", "pending",
            "The automated review hasn't posted yet; it starts when the PR is marked "
            "ready for review and usually takes 10-20 minutes. If nothing shows up, "
            "comment `/new-review`.",
            short="the automated review is running",
        ))
    else:
        # Not "push to refresh": a push refreshes the review automatically
        # only when it touches lines a 🚨 finding flagged. On a clean review
        # (#21840) a push just marks it stale, so the advice sent authors
        # round a loop that never closed.
        gates.append(Gate(
            "review", "red",
            f"No current review for `{head_sha[:9]}` — comment "
            "`/update-review <what changed>` to refresh it, or "
            "`/new-review` for a fresh one.",
        ))

    # G2 findings-answered ------------------------------------------------
    if oversized:
        gates.append(Gate("findings", "skip", "oversized — see the oversized gate"))
    elif "findings-answered" in skip_gates:
        gates.append(Gate("findings", "skip", "external contribution"))
    elif mechanical:
        gates.append(Gate("findings", "ok", "no review, no findings"))
    elif author_card:
        body = author_card.get("body") or ""
        try:
            state = review_state.parse_state(body) or review_state.empty_state()
        except ValueError:
            gates.append(Gate(
                "findings", "error",
                "The REVIEW_STATE block on the review comment is corrupt — "
                "ask a maintainer to regenerate the review.",
            ))
            state = None
        if state is not None:
            rows = _card_rows(body, ("🚨", "❓"), include_unnumbered=True)
            unnumbered = [r for r in rows if r["id"] == "F?"]
            if unnumbered:
                # `build-evidence.py` renumbers these before publish and
                # `apply-update.py` treats a survivor as a hard error. G2
                # used to drop them silently, which is the worst of the
                # three readings: a card that escaped renumbering passed
                # as 'every finding answered' with a live blocking
                # finding visible on screen.
                gates.append(Gate(
                    "findings", "error",
                    f"{len(unnumbered)} blocking finding(s) still carry the "
                    "`F?` placeholder, so they have no id to answer — the "
                    "review did not finish numbering. Re-run it with "
                    "`/new-review`.",
                ))
                state = None
        if state is not None:
            undecided = [
                r["id"] for r in rows
                if r["id"] not in state.get("findings", {})
            ]
            blocking_ids = undecided
            if undecided:
                ids = ", ".join(undecided)
                gates.append(Gate(
                    "findings", "red",
                    f"{len(undecided)} finding(s) undecided ({ids}) — fix and push, "
                    f"accept them with `/update-review accept {' '.join(undecided)}`, "
                    f"or reply with your reasoning, e.g. "
                    f"`/update-review {undecided[0]} is wrong because <why>`.",
                    short=_findings_short(undecided),
                ))
            elif not _body_matches_head(body, head_sha):
                # "Every finding answered" about a review of an older diff
                # is a claim about content that may no longer exist, and it
                # sat green beside G1's red "no current review" on #21840.
                # Undecided findings on a stale card stay red above (they
                # are real until someone answers them); an all-answered
                # stale card defers to G1 like a missing one does.
                m = HEAD_MARKER_RE.search(body)
                at = f" at `{m.group(1)[:9]}`" if m else ""
                gates.append(Gate(
                    "findings", "skip",
                    f"the review{at} is not current — see the review gate",
                ))
            else:
                gates.append(Gate("findings", "ok", "every finding answered"))
    elif legacy:
        outstanding = None
        missing = legacy.get("review_pages_missing") or []
        if missing:
            # The review is split across `review_pages` comments and GitHub
            # did not return all of them. Its findings sections are the tail
            # of the document, so what is missing is exactly where the 🚨
            # rows live: counting zero here would pass the gate on a review
            # nobody has read.
            gates.append(Gate(
                "findings", "error",
                f"the legacy review is {legacy['review_pages']} comments and "
                f"page(s) {', '.join(str(k) for k in missing)} could not be read — "
                "re-run the review (`/new-review`) rather than merge over an unread one.",
            ))
        else:
            try:
                vp = _load("sentinel_validate_pinned", _DOCS_REVIEW_SCRIPTS / "validate-pinned.py")
                outstanding = len(vp.extract_bucket_bullets(legacy.get("body") or "", "🚨 Outstanding"))
            except Exception as exc:  # noqa: BLE001
                gates.append(Gate("findings", "error", f"legacy comment unparsable: {exc}"))
                outstanding = None
        if outstanding is not None:
            if outstanding > 0:
                gates.append(Gate(
                    "findings", "red",
                    f"{outstanding} 🚨 Outstanding finding(s) on the legacy review — "
                    "work them per CONTRIBUTING §Working the review to zero.",
                ))
            elif not _body_matches_head(legacy.get("body") or "", head_sha):
                gates.append(Gate("findings", "skip",
                                  "the legacy review is not current — see the review gate"))
            else:
                gates.append(Gate("findings", "ok", "legacy review clean"))
    elif skip_standin:
        gates.append(Gate("findings", "ok", f"{skip_standin} — no findings to answer"))
    else:
        gates.append(Gate("findings", "skip", "no review present — see the review gate"))

    # Shared by G4 (a deploy carries over a base-only head move) and G5.
    carry = _Carry(gh, pr, files)

    # G4 infra-evidence ---------------------------------------------------
    if resolution.staging_evidence_required:
        witness = _staging_evidence(gh, head_sha)
        if not witness:
            # A deploy of a commit the head only merged the base into (or
            # pushed nothing onto) deployed this PR's change; another ~10
            # minutes on the shared stack would re-prove nothing.
            for sha in carry.predecessors():
                try:
                    earlier = _staging_evidence(gh, sha)
                except Exception:  # noqa: BLE001 — fail closed: no carry
                    earlier = None
                if earlier and carry.unchanged_since(sha):
                    witness = f"{earlier}; {_CARRY_CLAUSE}"
                    break
        if witness:
            gates.append(Gate("staging", "ok", witness))
        else:
            gates.append(_staging_gate(gh, pr, head_sha))
    else:
        # NOT "no infra paths": `domain:infra` and
        # `staging_evidence.paths` are different questions now, and a PR can
        # be squarely infra (`scripts/redirects/`, an unrelated workflow)
        # without touching anything the deploy runs. Saying "no infra paths"
        # on such a PR would be false in the one cell a reader checks.
        gates.append(Gate(
            "staging", "skip",
            "no changed path affects the deploy",
        ))

    # G5 oversized-ack ----------------------------------------------------
    if oversized:
        acked = _oversized_ack(config, reviews, head_sha, author)
        if acked:
            gates.append(Gate("oversized", "ok",
                              f"`{acked}` confirmed a hand review with `{OVERSIZED_ACK}`"))
        else:
            # Say who, where, and what doesn't count. The near misses (a PR
            # comment, a line comment, an approval from before the last
            # push) all look like they should work.
            number = pr.get("number") or "<number>"
            gates.append(Gate(
                "oversized", "red",
                "The automated review doesn't run on an oversized PR, so a Pulumi "
                "approver (org member or collaborator) confirms they reviewed it by hand: submit an **Approve** "
                f"review on the latest commit with `{OVERSIZED_ACK}` at the start of a line "
                f"in its comment, or run `gh pr review {number} --approve --body {OVERSIZED_ACK}`. "
                "Already approved? Approve again with it, or edit your approval's comment to "
                "add it. A PR comment, a line comment, or an approval of an earlier commit "
                "doesn't count.",
                short=f"an approval with {OVERSIZED_ACK}",
            ))
    else:
        gates.append(Gate("oversized", "skip", "not oversized"))

    # ---- Conclusion -----------------------------------------------------
    waived, waive_note = _waive_state(gh, config, labels)
    any_error = any(g.status == "error" for g in gates)
    reds = [g for g in gates if g.status in ("red", "pending")]
    hard_red = any(g.status == "red" for g in gates)
    infra_red = any(g.name == "staging" and g.status == "red" for g in gates)

    # `waived` is tested BEFORE `any_error` on purpose. It used to be the
    # other way round, so a gate that errored (one approver's lookup hitting
    # a 5xx, a REVIEW_STATE block that won't parse) held the PR at
    # action_required with an honored waive on it, under a summary printing
    # "WAIVED / gates bypassed". A waive clears every gate, G4 too (see the
    # module docstring for why G4 lost its exemption).
    #
    # What the order can NOT rescue is an outage of the org-scoped token
    # itself (GH_TOKEN_TEAM_READ unset or expired): `_waive_state` checks the
    # waiver's team membership with that token, so it refuses the waive in
    # the same breath. That is fail-closed on purpose — a label anyone with
    # triage could apply must not skip every gate unverified — and it leaves
    # a repo admin's merge as the way through.
    if waived:
        conclusion = "success"
        title = f"Waived by {waive_note}"
    elif any_error:
        conclusion = "action_required"
        errs = [_PLAIN_GATE.get(g.name, g.name) for g in gates if g.status == "error"]
        title = f"Couldn't check {_plain_join(errs)} — re-run the Sentinel check"
    elif reds:
        # Only pending gates left: in flight, nothing to fix. The status is
        # pending, which still blocks the merge (publish_verdict.STATE_FOR).
        conclusion = "failure" if hard_red else "pending"
        title = "Waiting on " + "; ".join(_waiting_on(g, len(blocking_ids)) for g in reds)
    else:
        conclusion = "success"
        title = "All gates green"
    if waive_note and not waived:
        title = f"review:waived refused · {title}"

    # ---- Summary --------------------------------------------------------
    parts: list[str] = []
    if waived:
        parts.append(f"## ⚠️ WAIVED by @{waive_note}\n\nMerge gates bypassed via `review:waived` "
                     "(logged). The table below shows what the verdict would have been.")
        if infra_red:
            parts.append("**The staging gate was red:** this change to the deploy has not been applied "
                         "on staging, so the first production deploy after merge is its "
                         "first real run. Watch it.")
    elif waive_note:
        # The label is on the PR but didn't authorize. Say so loudly: a
        # refused waive that reads as "nothing happened" invites a second
        # one from the same person.
        retry = ("While that lookup fails, a re-applied waive fails the same way, so a repo "
                 "admin merging past the check is the way through." if "lookup failed" in waive_note
                 else "To retry, a routing-team member removes the label and applies it again.")
        parts.append(
            f"## ⚠️ `review:waived` NOT honored\n\n{waive_note}. The gates below stand. {retry}"
        )
    # The gate table comes before the brief: the merge box's Details link
    # lands here, and on #22524 the table started two-thirds of the way down,
    # under a brief whose first line was "Check the ⚠️ items, then approve."
    table = ["| Gate | Status | Detail |", "|---|---|---|"]
    icon = {"ok": "✅", "red": "🔴", "pending": "🟡", "error": "🟠", "skip": "➖"}
    for g in gates:
        msg = g.message + (f" — {BREAK_GLASS}" if not waived and _waive_can_clear(g) else "")
        table.append(f"| {g.name} | {icon[g.status]} {g.status} | {msg} |")
    parts.append("\n".join(table))
    if external:
        parts.append(
            "_External contribution: the automated review does not run for external "
            "contributions — the approving reviewer's review is the review._"
        )
    if mechanical:
        parts.append(
            "_Classified mechanical under the tightened bar — no model review required. "
            "Branch protection still asks for an approval._"
        )
    if skip_note:
        parts.append(skip_note)
    if brief:
        parts.append(_strip_brief_for_summary(brief.get("body") or ""))
    summary = "\n\n".join(p for p in parts if p)

    card_url = (author_card or {}).get("html_url") or ""
    verdict = Verdict(
        conclusion=conclusion, title=title, summary=summary,
        head_sha=head_sha, gates=gates, blocking_ids=blocking_ids,
        mechanical=mechanical, waived=waived, waive_note=waive_note,
        links=_gate_links(pr, card_url),
    )

    if report_only:
        _stamp_report_only(verdict)
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
    if verdict.conclusion in ("failure", "pending", "action_required"):
        n = len(verdict.blocking_ids)
        if n:
            first = verdict.blocking_ids[0] if verdict.blocking_ids else "F1"
            line = (f"⛔ **{n} item(s) block merge** — fix and push, ship as-is with "
                    f"`/update-review accept {first}`, or reply `/update-review {first}: <why>`.")
        else:
            # No finding blocks, so the card right under this line says "nothing
            # blocks merge" and has nothing to fix or answer. "⛔ merge is
            # blocked — fix and push, or reply /update-review" contradicted it
            # and sent authors (workprentice included) after gates only an
            # approver or a deploy can clear. Say what the merge is waiting on;
            # that gate's status in the merge box says who acts.
            # In words, not gate ids: "waiting on G1 review-ran" told nobody
            # what to do.
            what = _plain_join(
                [_waiting_on(g, n) for g in verdict.gates if g.status in ("red", "pending")]
                + [f"a re-run of the Sentinel check ({_PLAIN_GATE.get(g.name, g.name)} "
                   "couldn't be checked)" for g in verdict.gates if g.status == "error"]
            ) or "the merge gate"
            line = f"⏳ **Merge is waiting on {what}.** Each gate's status in the merge box says how."
        strip = f"{STRIP_OPEN}\n{line}\n{STRIP_CLOSE}"
    else:
        if STRIP_OPEN not in body:
            return False  # nothing to clear; don't insert an empty pair
        strip = f"{STRIP_OPEN}\n{STRIP_CLOSE}"

    def with_strip(text: str) -> str:
        if STRIP_OPEN in text and STRIP_CLOSE in text:
            return _STRIP_RE.sub(lambda _: strip, text, count=1)
        lines = text.splitlines()
        insert_at = next((i + 1 for i, l in enumerate(lines) if l.startswith("## ")), 0)
        lines[insert_at:insert_at] = ["", strip]
        return "\n".join(lines)

    if with_strip(body) == body:
        return False
    # The PATCH replaces the whole body, and on the push that starts this run
    # restamp-base-merge.py moves the same card's head marker. Writing from
    # the listing read at the start of the run put the old head back, and G1
    # sat red on a base merge until the 2-hourly reconcile sweep (fork test of
    # pulumi/docs#22555). Re-read, and lay the strip onto what is there now.
    try:
        fresh = gh.get_issue_comment(card["id"]).get("body") or body
    except Exception:  # noqa: BLE001 — the old behavior, not a failure
        fresh = body
    new_body = with_strip(fresh)
    if new_body != fresh:
        gh.patch_issue_comment(card["id"], new_body)
        return True
    return False


_STRIP_RE = re.compile(re.escape(STRIP_OPEN) + r".*?" + re.escape(STRIP_CLOSE), re.DOTALL)


def without_strip(body: str) -> str:
    """`body` with the strip's contents dropped: what the review wrote. The
    strip is the Sentinel's, so a change confined to it is not a change to
    the review (restamp-base-merge.py compares cards this way)."""
    return _STRIP_RE.sub(STRIP_OPEN + STRIP_CLOSE, body or "")


# ---- Pinned status comment ----------------------------------------------

def remove_status_comments(gh: Gh, comments: list[dict] | None = None) -> int:
    """Delete the Sentinel's old pinned status comments; returns how many.

    There used to be one per PR, a gate table re-rendered on every
    evaluation. It duplicated the per-gate statuses in the merge box and the
    author card, and it was the noisiest thing on a PR (#22397: "too much
    text"; a draft got one saying only that drafts aren't gated). Each gate's
    status now says what it wants and links where you act, so the comment
    is gone, and every evaluation removes any copy a PR still carries.
    Only the bot's own comments: one quoting the marker is left alone."""
    comments = comments if comments is not None else gh.list_issue_comments()
    removed = 0
    for c in _find_comments(comments, STATUS_MARKER):
        try:
            gh.delete_issue_comment(c["id"])
            removed += 1
        except SentinelDataError as exc:
            if "HTTP 404" not in str(exc):  # 404: an overlapping run got it first
                print(f"::warning::could not delete status comment {c['id']}: {exc}",
                      file=sys.stderr)
    return removed


# ---- CLI ----------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--repo")
    parser.add_argument("--pr", type=int)
    parser.add_argument("--config", default=str(_REPO_ROOT / ".github" / "review-routing.yml"))
    parser.add_argument("--report-only", action="store_true")
    parser.add_argument("--update-strip", action="store_true")
    parser.add_argument(
        "--status-comment", action="store_true",
        help="Remove the retired pinned gate-status comment from the PR, if it "
             "still carries one (see remove_status_comments).",
    )
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
    # A read failure must PUBLISH action_required, not kill the process.
    # Without this, an uncaught SentinelDataError from get_pr / list_files /
    # list_issue_comments / list_reviews failed the step, so the publish
    # steps were skipped and NOTHING was written — and because the verdict
    # is keyed on (name, head sha), whatever was published earlier at this
    # head stayed the latest. The fail-open sequence: PR green at head H, an
    # approval is dismissed, the re-run 502s, and the stale `success` at H
    # still stands. The docstring above promises action_required for exactly
    # this; it was only true for errors raised *inside* a gate.
    try:
        verdict = evaluate(gh, config, report_only=args.report_only)
    except SentinelDataError as exc:
        verdict = Verdict(
            conclusion="action_required",
            title="Couldn't evaluate — action required",
            summary=(f"The Sentinel could not read the PR's state, so no gate was "
                     f"evaluated. This is not a pass. Re-run the check.\n\n"
                     f"```\n{exc}\n```"),
            head_sha="",
        )
        print(json.dumps(verdict.to_json(), indent=2))
        return 0
    # publish_guard.py protects the STATUS, and runs as a later workflow
    # step — but the two comment writes below happen inside this process,
    # before the guard has said anything. So a run evaluating head A while
    # the author pushes B could finish second and rewrite both comments to
    # A's verdict, after which the guard correctly declined to publish the
    # status: a green check next to two comments saying the opposite, and
    # nothing rewrites them until an unrelated event, because
    # the comments are pure functions of the verdict.
    #
    # One re-read immediately before writing closes it. Cheap, and it is the
    # same question the guard asks, asked at the point that matters.
    if (args.update_strip or args.status_comment) and not args.dry_run:
        try:
            current_head = ((gh.get_pr().get("head") or {}).get("sha") or "")
        except SentinelDataError:
            current_head = verdict.head_sha  # unreadable: don't block the write
        moved = publish_guard.head_moved(verdict.head_sha, current_head) if verdict.head_sha else None
        if moved:
            print(f"::notice::{moved}; not writing comments for a superseded "
                  f"verdict.", file=sys.stderr)
        else:
            # One listing for both writers. Each used to fetch its own, so
            # an enforcing run paginated the comment list three times.
            try:
                comments = gh.list_issue_comments()
            except SentinelDataError as exc:
                print(f"::warning::could not list comments: {exc}", file=sys.stderr)
                comments = None
            if comments is not None:
                if args.update_strip and not args.report_only:
                    # Best-effort: this ran before the verdict was printed, so
                    # a failed PATCH discarded a completed evaluation.
                    try:
                        update_strip(gh, verdict, comments=comments)
                    except SentinelDataError as exc:
                        print(f"::warning::could not update the author-card strip: {exc}",
                              file=sys.stderr)
                # Best-effort for the same reason as the strip: a failed
                # DELETE must not suppress the verdict.
                if args.status_comment:
                    try:
                        remove_status_comments(gh, comments=comments)
                    except SentinelDataError as exc:
                        print(f"::warning::could not remove the old status comment: {exc}",
                              file=sys.stderr)
    print(json.dumps(verdict.to_json(), indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
