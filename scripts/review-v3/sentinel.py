#!/usr/bin/env python3
"""The Sentinel — deterministic merge-gate evaluator for the v3 review workflow.

One blocking check-run answers "is this PR mergeable?" from five gates:

  G1 review-ran         a current review exists at head SHA (or none is
                        required: mechanical PRs, fork PRs; a trivial PR
                        may stand on triage's prose-check comment)
  G2 findings-answered  every 🚨/❓ finding on the author card carries a
                        REVIEW_STATE disposition (or is checked off)
  G3 right-approver     a human approver who can clear the lane: a member of
                        every matrix-required team, or — under
                        `approval.scope: any-team` — of any routing team, or
                        a repo admin when `approval.admins_satisfy` is on
  G4 deploy-evidence    a change on `staging_evidence.paths` carries a green
                        staging/pulumi-test-io commit status at the current
                        head SHA, posted by a trusted writer. That list is
                        narrow on purpose — only what can break `pulumi up`,
                        since a PR's own build already runs the pipeline in
                        preview mode. NOT the same set as `domain:infra`:
                        the matrix answers who reviews, this answers what
                        must be applied to be believed
  G5 oversized-ack      review:oversized PRs replace G1/G2 with an explicit
                        `sentinel:oversized-ack` in the approving review body

One config-driven shortcut sits around the gates
(`.github/review-routing.yml`): `not_governed` lanes (Dependabot, the
generated-docs regens) conclude success with no gates evaluated. Those are
safe to exempt only because something else already posts a real approval and
arms auto-merge for them — see that file's NOT GOVERNED section.

There used to be a second one, the `auto_approve` clean-brief rule, which
let a listed bot author pass G3 with no human approval at all. It was
deleted: nothing consumed the `auto_approved` flag it set, and GitHub's
required-review rule does not read this config, so the rule only ever made
G3 report a pass the merge box disagreed with. `mechanical` lost the same
power at the same time — it now skips the model review, never the approver.
`review:prose-flagged` still demotes a mechanical PR to substantive.

Everything here is a pure function of GitHub API state plus the base-ref
routing config: NO model, NO AWS, and — because the workflow runs on
`pull_request_target` with write permissions — NO checkout or execution of
PR code, ever (test_sentinel.py asserts the workflow keeps that invariant).

Conclusion mapping is where merge gates silently rot, so it is explicit:
`success` only when every gate is ok; any red ⇒ `failure`; any gate that
ERRORED (a team-membership lookup failed, the state block is corrupt) ⇒
`action_required` — never `neutral`/`skipped`, which GitHub counts as
PASSING for a required check. `neutral` is reserved for drafts and for
report-only mode, where the real verdict rides inside the summary. Report-only
is not a silent mode: the pinned status comment is maintained on every PR in
both modes, leading with a preview banner that says the check blocks nothing
yet and that it soon will (`render_status_comment`). Only the ⛔ author-card
strip stays enforcing-only — that one edits someone else's comment.

`review:waived` is the break-glass: the check concludes success with a loud
banner naming the waiving actor — except gate G4, which has no waiver (the
proposal's "no waiver, no shortcut" for infra; the incident path when
staging itself is broken is an admin-bypass merge, which rulesets log).

"External contribution" means the head repo is a fork (or a deleted
fork) — never the author's permission level: a GitHub App such as
workprentice answers `none` on the collaborator endpoint yet pushes
same-repo branches that get the full review, and treating those as
external skipped G1/G2 on every one of them (2026-09-12 → 09-14). A PR
whose head-repo fact can't be read is internal (the stricter gates).

`review:trivial` short-circuits the review lane, and `review:prose-flagged`
(triage's Haiku/Vale pass) demotes the PR from mechanical — so without a
stand-in G1 would stay red forever on a PR nothing will ever review. The
stand-in is triage's own `<!-- TRIAGE_PROSE -->` comment: with it present
G1/G2 pass (advisory nits only, nothing to answer) and G3 still wants the
human approver the demotion asked for.

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
# Every role comment the Sentinel reads — author card, reviewer brief,
# legacy pages, its own status comment — must come from the bot that writes
# them. See `_find_comment` for what a missing provenance check cost.
BOT_LOGIN = "github-actions[bot]"
STAGING_STATUS_CONTEXT = "staging/pulumi-test-io"
# Identities whose `staging/pulumi-test-io` status the Sentinel will take as
# evidence. Anyone with push access can write a commit status, so an
# unattributed one is not evidence of anything.
STAGING_STATUS_WRITERS = frozenset({BOT_LOGIN, "pulumi-bot"})
# The workflow `/deploy-staging` dispatches, and the one G4 verifies against
# directly when the commit status is missing. See `_staging_evidence`.
STAGING_WORKFLOW_FILE = "testing-build-and-deploy.yml"
OVERSIZED_ACK = "sentinel:oversized-ack"
# The pinned status comment is maintained on EVERY PR the Sentinel evaluates,
# report-only included — see `render_status_comment` for the preview banner
# that carries the "this is not blocking you yet" disclaimer. There used to be
# a `sentinel:preview` opt-in label here that made report-only mode write the
# comment for a canary cohort only (the content-review, glow-up, and
# link-sweep lanes labelled themselves). It was retired 2026-09-21: a dry run
# nobody sees is a dry run that proves nothing, and the one cohort it did
# cover had a workflow for an author. Anything still applying that label is
# inert; nothing reads it.
BREAK_GLASS = (
    "override: a member of a routing team (`.github/review-routing.yml` `teams:`) "
    "can apply `review:waived` (logged)"
)

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
            ["gh", *args], text=True, capture_output=True, env=env,
        )
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

    def get_repo_permission(self, user: str) -> str:
        """The user's effective permission on the repo: admin/write/read/none.

        Used only by the `approval.admins_satisfy` rule in G3. The endpoint
        wants push access, which the default GITHUB_TOKEN does not have."""
        return self._org_scoped_lookup(
            f"repos/{self.repo}/collaborators/{user}/permission", ".permission",
            f"repo permission ({self.repo}/{user})")

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
    # already applied and already working — while the check-run next to it
    # said success. A gate surface that contradicts the gate is the failure
    # the `_GATE_BLURB` phrasebook exists to prevent.
    waived: bool = False

    def to_json(self) -> dict:
        return {
            "conclusion": self.conclusion,
            "title": self.title,
            "summary": self.summary,
            "head_sha": self.head_sha,
            "would_be": self.would_be,
            "gates": [{"gate": g.name, "status": g.status, "message": g.message} for g in self.gates],
            "blocking_ids": self.blocking_ids,
            "mechanical": self.mechanical,
            "governed": self.governed,
        }


# ---- Helpers ------------------------------------------------------------


def _find_comment(comments: list[dict], marker: str) -> dict | None:
    """The bot-authored comment carrying `marker`, oldest first.

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
    the WRITER already enforces and that two siblings already check:
    `pinned-comment.sh`'s `list_role_comments` requires the marker to be an
    exact line among the body's first three, and `resolve-handler.py:222`
    requires `login == github-actions[bot]`. The far less load-bearing
    triage-prose comment was already read this way; this function was the
    one place that checked neither, so it is now the only reader and both
    markers come through it.
    """
    for c in comments:
        if (c.get("user") or {}).get("login") != BOT_LOGIN:
            continue
        # Exact line, first three lines — `list_role_comments`'s rule. A
        # marker merely quoted inside a body is not a role comment.
        lines = [ln.strip() for ln in (c.get("body") or "").splitlines()[:3]]
        if marker in lines:
            return c
    return None


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
        # anchor below stops a quoted marker, but not a forged page.
        if (c.get("user") or {}).get("login") != BOT_LOGIN:
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
# Named, not inlined, so `test_label_event_filter_covers_every_label_the_
# evaluator_reads` can derive the workflow's trigger list from the evaluator
# instead of restating it.
OVERSIZED_LABEL = "review:oversized"
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
    cancelled runner, a lost token or a hand-run deploy that never went
    through `/deploy-staging` all leave a green deploy with no status. The
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
        # …which made the one gate the config calls "no waiver, no shortcut"
        # a one-line bypass. The run record below cannot be forged that way,
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


def _waive_state(gh: Gh, config: routing.Config, labels: set[str]) -> tuple[bool, str]:
    """Is the waive label present AND applied by someone entitled to apply it?

    The label alone is not the waive. A waive skips every gate but G4, so
    the authority to apply one has to be at least the authority to approve
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
        return False, "could not read who applied the waive label — not honored"
    for team_ref in sorted(set(config.teams.values())):
        org, slug = _team_org_slug(team_ref)
        try:
            if gh.get_team_membership(org, slug, actor) == "active":
                return True, actor
        except SentinelDataError:
            return False, (
                f"could not verify whether @{actor} may waive (team lookup "
                "failed) — not honored"
            )
    return False, (
        f"@{actor} is not an active member of any routing team "
        "(`.github/review-routing.yml` `teams:`) — waive not honored"
    )


# ---- Evaluation ---------------------------------------------------------


def _stamp_report_only(verdict: Verdict) -> Verdict:
    """Turn a real verdict into its report-only twin, in place.

    Report-only has three surfaces and they have to agree: the check-run's
    conclusion (`neutral`, which GitHub counts as passing), its title and
    summary in the merge box, and the pinned status comment. `would_be` is
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
    resolution = routing.resolve_lanes(paths, mechanical, claims, config, link_only=link_only_diff(files))

    # External-contributor lane = fork head repo. Fail closed: no head-repo
    # fact in the payload means the stricter (internal) gates apply.
    external = _is_external(pr)
    skip_gates = set((config.external_contributors or {}).get("skip_gates") or []) if external else set()

    author_card = _find_comment(comments, AUTHOR_MARKER)
    brief = _find_comment(comments, BRIEF_MARKER)
    legacy = _find_legacy_comment(comments) if author_card is None else None
    oversized = OVERSIZED_LABEL in labels
    trivial = TRIVIAL_LABEL in labels
    triage_prose = _find_comment(comments, TRIAGE_PROSE_MARKER) if trivial else None
    trivial_standin = False  # set when triage's prose comment satisfies G1

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
    elif trivial and triage_prose is not None and author_card is None and legacy is None:
        # The review lane skipped this PR as trivial; prose-flagged (or a
        # classifier disagreement) keeps it out of the mechanical lane. Triage
        # posted the prose nits it found — that comment is the review. Only
        # for a PR that never got a review: a card or legacy comment at any
        # head keeps the PR on the review track (a stale card with open
        # findings must not pass on the trivial label).
        trivial_standin = True
        gates.append(Gate(
            "G1 review-ran", "ok",
            "trivial change — triage's prose check stands in for the review "
            "(advisory nits in the triage comment)",
        ))
    elif trivial and author_card is None and legacy is None:
        gates.append(Gate(
            "G1 review-ran", "red",
            f"No current review for `{head_sha[:9]}` — the review lane skipped this "
            "PR as `review:trivial`, and triage's prose-check comment is missing. "
            "Comment `@claude #new-review` to run a full review, or a maintainer "
            "removes `review:trivial` and pushes.",
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
                    "G2 findings-answered", "error",
                    f"{len(unnumbered)} blocking finding(s) still carry the "
                    "`F?` placeholder, so they have no id to answer — the "
                    "review did not finish numbering. Re-run it with "
                    "`@claude #new-review`.",
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
                    "G2 findings-answered", "red",
                    f"{len(undecided)} finding(s) undecided ({ids}) — fix and push, "
                    f"or reply with your reasoning, e.g. "
                    f"`@claude F3 is wrong because <why> #update-review` or "
                    f"`@claude I know what I'm doing, mark everything resolved #update-review`.",
                ))
            else:
                gates.append(Gate("G2 findings-answered", "ok", "every finding answered"))
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
                "G2 findings-answered", "error",
                f"the legacy review is {legacy['review_pages']} comments and "
                f"page(s) {', '.join(str(k) for k in missing)} could not be read — "
                "re-run the review (`@claude #new-review`) rather than merge over an unread one.",
            ))
        else:
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
    elif trivial_standin:
        gates.append(Gate("G2 findings-answered", "ok", "trivial — no findings to answer"))
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
    # An approval is of a COMMIT, not of a PR. The old comment above said
    # "stale-on-push is the ruleset's dismissal job" — but AGENTS.md records
    # that server-side branch protection is not in place yet, and nothing in
    # `.github/` configures dismissal, so nothing was doing that job.
    # Without this, the sequence is: get a clean one-line change approved,
    # push the payload, let the review lane post a fresh card, and all five
    # gates are green on an approval nobody re-gave.
    #
    # Keep the pre-push approvals to tell the author WHY the gate is red —
    # "your approval predates the push" is a different message from "nobody
    # has approved", and the second one is a lie to someone staring at a
    # green checkmark on the PR.
    # Strict equality, not `in (None, head_sha)`: GitHub always sends
    # `commit_id` on a review, so an absent one is a malformed payload, and
    # "count it as current" would be fail-open on the gate that guarantees a
    # human. An approval we cannot place at this head does not clear G3.
    stale_approvers = [r for r in approvers if r.get("commit_id") != head_sha]
    approvers = [r for r in approvers if r.get("commit_id") == head_sha]
    # The subset of `approvers` whose approval actually clears G3 — filled in
    # below. G5 reads it so the oversized ack cannot come from a bystander.
    qualified_approvers: list[dict] = []
    if not resolution.roles:
        # A zero-file PR (a branch whose commits net to no diff, or one
        # already merged into base) is the only way here. It used to report
        # `ok`, which made G3 — the one gate that guarantees a human — pass
        # with no human, and combined with a forged card that was a fully
        # green Sentinel with nobody involved. There is nothing to review,
        # so there is also nothing to approve: `skip` says that honestly
        # without manufacturing a pass.
        gates.append(Gate(
            "G3 right-approver", "skip", "no changed paths to route",
        ))
    else:
        missing: list[str] = []
        errors: list[str] = []
        # `resolution.any_team` means one team is enough instead of all of
        # them — repo-wide under `approval.scope: any-team`, or for a
        # link-only sweep under `link_only.approval: any-team`. The matrix
        # roles stay on the record either way: they are still who triage
        # requests and who the SLA sweep chases, and with `any-team` the
        # request is the ONLY thing putting the right eyes on the PR — which
        # is what makes `overrides:` (who gets asked) load-bearing rather
        # than cosmetic.
        all_teams = [config.teams[r] for r in sorted(config.teams)]
        required = (all_teams if resolution.any_team
                    else [config.teams.get(role, "") for role in sorted(resolution.roles)])
        satisfied_any = False
        for team_ref in required:
            org, slug = _team_org_slug(team_ref)
            satisfied = False
            for r in approvers:
                login = (r.get("user") or {}).get("login") or ""
                try:
                    if gh.get_team_membership(org, slug, login) == "active":
                        satisfied = True
                        qualified_approvers.append(r)
                        break
                except SentinelDataError as exc:
                    errors.append(str(exc))
            if satisfied:
                satisfied_any = True
                if resolution.any_team:
                    break  # one team clears it; no need to ask about the rest
            elif not errors:
                missing.append(team_ref)
        if resolution.any_team:
            # One team is enough; only an empty set is a miss.
            missing = [] if satisfied_any else ["any review team"]
        # A repo admin can merge past a red check anyway, so with
        # `approval.admins_satisfy` the gate says so rather than reporting a
        # block the repo does not impose on them. Consulted only when the
        # team rule already came up short, so the ordinary PR costs no extra
        # API calls.
        admin_approver = ""
        if missing and not errors and routing.admins_satisfy(config):
            for r in approvers:
                login = (r.get("user") or {}).get("login") or ""
                try:
                    if gh.get_repo_permission(login) == "admin":
                        admin_approver = login
                        qualified_approvers.append(r)
                        break
                except SentinelDataError as exc:
                    errors.append(str(exc))
        # `errors and not satisfied_any`: a transient 5xx on ONE approver's
        # membership lookup used to poison a verdict another approver had
        # already settled — the gate reported `error`/action_required with a
        # qualifying approval sitting right there. Only report the failure
        # when it is actually load-bearing.
        if errors and not satisfied_any:
            gates.append(Gate(
                "G3 right-approver", "error",
                "Couldn't verify the approver's team membership or repo role — "
                "re-run the check. " + errors[0],
            ))
        elif admin_approver:
            gates.append(Gate(
                "G3 right-approver", "ok",
                # No `@` — this message also renders in the pinned status
                # comment, where a mention would ping the approver on every
                # re-evaluation.
                f"approved by repository administrator `{admin_approver}`",
            ))
        elif missing:
            names = ", ".join(f"**{m}**" for m in missing)
            if resolution.any_team:
                names += " (" + ", ".join(all_teams) + ")"
            admin_clause = (" or a repository administrator"
                            if routing.admins_satisfy(config) else "")
            stale_clause = ""
            if stale_approvers:
                who = ", ".join(sorted(
                    f"`{(r.get('user') or {}).get('login')}`" for r in stale_approvers))
                stale_clause = (
                    f" {who} approved an earlier commit; re-approve at "
                    f"`{head_sha[:9]}`."
                )
            gates.append(Gate(
                "G3 right-approver", "red",
                f"Needs approval from a member of {names}{admin_clause} — no "
                f"qualifying human approval at this head (bot approvals never "
                f"count).{stale_clause}",
            ))
        else:
            gates.append(Gate(
                "G3 right-approver", "ok",
                "a routing-team member approved" if resolution.any_team
                else "matrix-required approval present"))

    # G4 infra-evidence ---------------------------------------------------
    if resolution.staging_evidence_required:
        witness = _staging_evidence(gh, head_sha)
        if witness:
            gates.append(Gate("G4 infra-evidence", "ok", witness))
        else:
            gates.append(Gate(
                "G4 infra-evidence", "red",
                f"This PR changes the deploy itself: no successful staging "
                f"deploy at `{head_sha[:9]}`. One is dispatched automatically "
                "when such a PR opens or pushes (`staging-deploy-auto.yml`); if "
                "it never ran or it failed, a tools-team member can comment "
                "`/deploy-staging` to retry. (Not waivable.)",
            ))
    else:
        # NOT "no infra paths": `domain:infra` and
        # `staging_evidence.paths` are different questions now, and a PR can
        # be squarely infra (`scripts/redirects/`, an unrelated workflow)
        # without touching anything the deploy runs. Saying "no infra paths"
        # on such a PR would be false in the one cell a reader checks.
        gates.append(Gate(
            "G4 infra-evidence", "skip",
            "no changed path affects the deploy",
        ))

    # G5 oversized-ack ----------------------------------------------------
    if oversized:
        # `approvers` is already filtered to humans at this head. It is NOT
        # filtered to the team that satisfied G3, so the ack must come from
        # someone whose approval actually counts — `qualified_approvers` is
        # populated by G3 above. Before this, anyone with read access could
        # post an APPROVED review carrying the magic string while a genuine
        # team member clicked plain Approve, and a self-applied
        # `review:oversized` (nothing verifies the PR is oversized) had
        # already skipped G1 and G2.
        acked = any(OVERSIZED_ACK in (r.get("body") or "")
                    for r in qualified_approvers)
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
    waived, waive_note = _waive_state(gh, config, labels)
    any_error = any(g.status == "error" for g in gates)
    reds = [g for g in gates if g.status == "red"]
    infra_red = any(g.name.startswith("G4") and g.status == "red" for g in gates)

    # `waived` is tested BEFORE `any_error` on purpose. It used to be the
    # other way round, which made the break-glass inert in exactly the
    # outage it exists for: an expired PULUMI_BOT_TOKEN errors G3 on every
    # PR, so every PR sat at action_required and no waive could move any of
    # them — while the summary still printed a "WAIVED / gates bypassed"
    # banner over a blocked conclusion. G4 remains unwaivable either way.
    if waived:
        if infra_red:
            conclusion = "failure"
            title = "Waived, but infra evidence has no waiver"
        else:
            conclusion = "success"
            title = "WAIVED"
    elif any_error:
        conclusion = "action_required"
        title = "Couldn't evaluate — action required"
    elif reds:
        conclusion = "failure"
        title = f"{len(reds)} gate(s) red"
    else:
        conclusion = "success"
        title = "All gates green"

    # ---- Summary --------------------------------------------------------
    parts: list[str] = []
    if waived:
        parts.append(f"## ⚠️ WAIVED by @{waive_note}\n\nMerge gates bypassed via `review:waived` "
                     "(logged). The table below shows what the verdict would have been.")
        if infra_red:
            parts.append("**Infra staging evidence is NOT waivable** — gate G4 stands red.")
    elif waive_note:
        # The label is on the PR but didn't authorize. Say so loudly: a
        # refused waive that reads as "nothing happened" invites a second
        # one from the same person.
        parts.append(
            f"## ⚠️ `review:waived` NOT honored\n\n{waive_note}. The gates below stand."
        )
    if brief:
        parts.append(_strip_brief_for_summary(brief.get("body") or ""))
    if external:
        parts.append(
            "_External contribution: the automated review does not run for external "
            "contributions — the approving reviewer's review is the review._"
        )
    if mechanical:
        parts.append(
            "_Classified mechanical under the tightened bar — no model review required. "
            "A human approver is still required._"
        )
    if trivial_standin:
        parts.append(
            "_Trivial change: triage's prose-check comment stands in for the review; "
            "a human approver is still required._"
        )
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
        mechanical=mechanical, waived=waived,
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


# ---- Pinned status comment ----------------------------------------------

# How each quiet state opens its cell. A red gate speaks for itself — its own
# message carries the remediation — so only the quiet states need a
# phrasebook, and each one is completed by the gate's own message rather than
# replacing it.
#
# It used to REPLACE it, and a green gate rendered as the bare words "Nothing
# to do." That is how PR #21698 came to show a green G3 right-approver with
# no approving review from anybody on the PR: the gate had passed under the
# since-deleted `auto_approve` clean-brief rule, and the one cell that could
# have said so said "Nothing to do." instead. A merge gate that reports a
# pass without its reason is indistinguishable from one that is broken, so
# the reason ships with the verdict now.
_GATE_BLURB = {
    "ok": "Nothing to do",
    "skip": "Doesn't apply to this PR",
    "error": "Couldn't be evaluated — re-run the Sentinel check",
}

_STATUS_ICON = {"ok": "✅", "red": "🔴", "error": "🟠", "skip": "➖"}


def render_status_comment(verdict: Verdict) -> str:
    """The pinned 'where this PR stands' comment.

    Deliberately free of timestamps and run ids: the body is a pure
    function of the verdict, so a re-evaluation that changes nothing
    produces a byte-identical body and `update_status_comment` skips the
    PATCH. A comment that edits itself on every push is the notification
    noise v3 exists to remove.
    """
    preview = bool(verdict.would_be)
    heading = ("## Sentinel — merge gate status (preview)" if preview
               else "## Sentinel — merge gate status")
    lines = [STATUS_MARKER, heading, ""]

    if preview:
        # Both halves, in this order, and neither is optional: informational
        # today, enforced soon. Half one alone teaches everyone to scroll past
        # the comment, and enforcement day is then the first time anyone reads
        # a gate row; half two alone reads as a PR that is blocked. Half one
        # says "safe to ignore for now", never "you can merge anyway" — the
        # gate surface is no place to coach someone past a red row. And
        # neither half calls a red row the author's homework: G3 is an
        # approval and G4 a deploy, so the rows are a sign-off checklist, and
        # only some of them are ever the author's to clear.
        lines += [
            "> [!WARNING]",
            "> ## ⚠️ Preview mode — this check is NOT blocking your merge",
            "> ",
            f"> The Sentinel is in **preview (report-only) mode**: its check-run concludes "
            f"`neutral` whatever the gates below say, so nothing here gates this PR. The rows "
            f"are informational and **safe to ignore for now**. It *would* have concluded "
            f"`{verdict.would_be}`.",
            "> ",
        ]
        # The enforcement half promises "every row below", so it only goes
        # above a gate table. A gateless comment (not governed) has no rows
        # to turn green, and nothing about it changes on enforcement day.
        if verdict.governed and verdict.gates:
            lines += [
                "> **This will be enforced in the near future.** Once it is, every row below "
                "has to be green before this PR can merge. The rows are the sign-offs a merge "
                "needs — some yours, some a reviewer's or a deploy's. Tell us in `#docs` if one "
                "looks wrong.",
            ]
        else:
            lines += [
                "> **This will be enforced in the near future.** Tell us in `#docs` if "
                "anything here looks wrong.",
            ]
        lines += [""]

    if not verdict.governed or not verdict.gates:
        lines += [(verdict.base_summary or verdict.summary).split("\n\n")[0], ""]
        return "\n".join(lines).rstrip() + "\n"

    blocking = [g for g in verdict.gates if g.status in ("red", "error")]
    # In preview mode `conclusion` is always `neutral` and the real answer
    # lives in `would_be`, so read the effective one — otherwise a waived PR
    # in preview falls through to the "N gates need attention" headline the
    # waive branch exists to prevent.
    effective = verdict.would_be or verdict.conclusion
    if verdict.waived and effective == "success":
        # Say what the check-run says. The rows below still show what the
        # gates found — that is the audit trail a waive is supposed to leave
        # — but the headline must not tell an author they are blocked when
        # they are not, nor recommend the break-glass twice.
        lines += [
            "**Waived — this PR can merge.** `review:waived` is applied and "
            "honored; the gates below are the record of what it bypassed.",
            "",
        ]
    elif blocking:
        # Tense matters here, and only here: in preview nothing is blocking
        # anything, so a headline reading "before this can merge" hands the
        # banner directly above it a contradiction to lose.
        lines += [
            (f"**{len(blocking)} of {len(verdict.gates)} gates would block this "
             f"merge once the Sentinel is enforced.**" if preview else
             f"**{len(blocking)} of {len(verdict.gates)} gates need attention "
             f"before this can merge.**"),
            "",
        ]
    else:
        lines += ["**All gates green — nothing would block this merge.**" if preview
                  else "**All gates green — nothing is blocking this merge.**", ""]

    lines += ["| | Gate | What it needs |", "|---|---|---|"]
    for g in verdict.gates:
        if g.status in ("red", "error"):
            need = g.message
        else:
            # "Nothing to do: matrix-required approval present." — the blurb
            # answers the column, the gate's own message says why, and a
            # reader can tell a satisfied gate from a mis-evaluated one.
            need = f"{_GATE_BLURB[g.status]}: {g.message}."
        # One cell, one line: a literal newline would break the row.
        need = " ".join(need.split())
        lines.append(f"| {_STATUS_ICON[g.status]} | **{g.name}** | {need} |")
    lines.append("")

    if (not verdict.waived
            and any(g.status == "red" and not g.name.startswith("G4") for g in blocking)):
        # Not BREAK_GLASS verbatim — that string is written to follow a gate
        # message ("… — override: a member of …") and reads as a doubled
        # "override:" when it opens a sentence of its own.
        lines += [
            "_Break glass: a member of a routing team "
            "(`.github/review-routing.yml` `teams:`) can apply `review:waived`, "
            "which is logged._",
            "",
        ]
    if any(g.name.startswith("G4") and g.status == "red" for g in verdict.gates):
        lines += ["_Infra staging evidence has no waiver._", ""]

    lines += [f"<sub>Evaluated at head `{verdict.head_sha[:9]}`.</sub>"]
    return "\n".join(lines).rstrip() + "\n"


def update_status_comment(gh: Gh, verdict: Verdict,
                          comments: list[dict] | None = None) -> bool:
    """Upsert the pinned status comment. Idempotent; returns True on write."""
    comments = comments if comments is not None else gh.list_issue_comments()
    body = render_status_comment(verdict)
    existing = _find_comment(comments, STATUS_MARKER)
    if existing is None:
        gh.post_issue_comment(body)
        return True
    if (existing.get("body") or "").strip() == body.strip():
        return False
    gh.patch_issue_comment(existing["id"], body)
    return True


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
        help="Maintain the pinned gate-status comment. Both modes do, on every "
             "PR; in report-only mode the comment leads with a preview banner "
             "saying it blocks nothing yet.",
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
    # steps were skipped and NOTHING was written — and because check-runs
    # are keyed on (name, head sha), whatever was published earlier at this
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
    # publish_guard.py protects the CHECK-RUN, and runs as a later workflow
    # step — but the two comment writes below happen inside this process,
    # before the guard has said anything. So a run evaluating head A while
    # the author pushes B could finish second and rewrite both comments to
    # A's verdict, after which the guard correctly declined to publish the
    # check-run: a green check next to two comments saying the opposite, and
    # nothing rewrites them until an unrelated event, because
    # `render_status_comment` is a pure function of the verdict.
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
                # Every PR the Sentinel evaluates, in both modes. Report-only
                # used to write only for a `sentinel:preview` cohort; the
                # comment now carries its own preview banner instead, which
                # is what makes showing it everywhere safe (and showing it
                # everywhere is what makes the dry run worth running).
                # Best-effort for the same reason as the strip: a locked
                # comment or a secondary rate limit must not suppress the
                # verdict.
                try:
                    update_status_comment(gh, verdict, comments=comments)
                except SentinelDataError as exc:
                    print(f"::warning::could not maintain the status comment: {exc}",
                          file=sys.stderr)
    print(json.dumps(verdict.to_json(), indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
