#!/usr/bin/env python3
"""The act primitive for /pr-review: plan → preview → execute, batch-capable.

    act.py --in .pr-review-queue.json --stamp 21550,21577 --route 21431:@cnunciato \\
           --unblock 21525 --plan-out .pr-review-plan.json          # plan + preview
    act.py --execute .pr-review-plan.json [--dry-run]                # run it

Actions (each a `Step`; every one goes through the same preview, comment
templates and attribution footer). Nothing here is reachable without an
explicit `--act` invocation: the person authorizes the writes by running the
command the board composed, which is why a plan names its PRs one by one:

  --stamp N,N        approve, then squash-merge, after a per-PR preflight run
                     immediately before each merge: head SHA unchanged since
                     the plan, mergeable_state in {clean, blocked}, checks
                     green, no changes-requested review, and no blocking
                     review finding left unanswered. master moves during
                     a batch; the preflight is what makes a batch safe. Bot
                     PRs merge; a human-authored PR is approved only unless
                     --merge-humans (authors merge their own PRs).
                     `N:merge` / `N:no-merge` overrides that default for one
                     PR, so a mixed batch stays a single command. Repeatable;
                     values accumulate.
  --route N:@user|team   request review and post the row's defects (reason
                     codes + judgments) as one comment. Repeatable, and the
                     same PR may appear more than once: `--route N:@a --route
                     N:@b` is one step that requests both (a PR whose lanes
                     need two teams). `N` alone takes the row's own targets.
  --request-changes N    post a CHANGES_REQUESTED review built from the row's
                     judgments (one line-anchored item each, no filler) and
                     apply `needs-author-response`. The author-facing verb the
                     old menus had; the approver's way to say "your turn". A
                     row with no open finding still goes back when a
                     `--reason N=…` says why (red CI, a conflict act.py can't
                     push through); the reason is then the whole review.
  --chain C1         start a collision cluster's chain: stamp the first PR in
                     its merge order (--force when it is a judge row) through
                     the same gates as --stamp, then merge base into the next
                     one so the following run finds it green instead of
                     dirty. The unblock waits on the stamp having merged. One
                     link per run; each link waits on CI.
  --unblock N        merge the base branch into the head as a merge commit
                     (never rebase, never force-push). Only conflict-free
                     merges are pushed; anything else is aborted and reported.
  --fix N            apply the drafted description correction and any
                     one-click ✏️ suggestions, commit, push.
  --close N [--superseded-by M]  close N: with M, a cross-link comment on
                     both; alone, one comment carrying --reason. Closing is
                     the send-back for a workflow-authored PR, which has no
                     author to answer a review. Repeatable; `--superseded-by
                     N:M` scopes M to one of several closes.
  --ask-fix N        comment `@claude fix <ids> #update-review`, naming the
                     row's open findings: the second way out of a PR whose
                     author will never answer its review. `/address-review`
                     is the interactive one -- you walk the findings and push
                     the fixes yourself; this hands the same list to the
                     agent already watching the PR and asks it to refresh the
                     review after. One comment, no push, so unlike the
                     handoff it batches with everything else.
  --refresh N        post `@claude <reason> #update-review`.
  --rerun N          post `@claude <reason> #new-review` (fresh review from scratch).
  --rerun-checks N   re-run the failed jobs of the head's workflow runs (the
                     newest run per workflow that concluded failure); the
                     unblock on a red-CI row. A red commit status has no run
                     to re-run, and the step says so instead of guessing.
  --render N         screenshot the preview pages (screenshot.mjs + Playwright).
  --deploy N         dispatch testing-build-and-deploy.yml at the head branch.
  --reason TEXT | N=TEXT   what to say on a request-changes, refresh, rerun or
                     close. `N=TEXT` scopes it to PR N; bare TEXT is accepted
                     only when exactly one step in the plan takes a reason.

Every comment body, review body and suggestion is rendered at plan time into
the step, and execute sends exactly that: the preview is the writes. Every
write is preceded by a preflight that re-reads the PR (open, head unchanged
since the plan); a failed preflight skips that step and the batch continues.
`--dry-run` runs the preflights and records every write it would make
without sending any of them, and never runs git.

Bot branches: dependabot and the generated-docs regens (pulumi-bot +
`automation/merge`) are never pushed to; workprentice and content-review/*
branches may be, as merge commits. Pushes are made from a temporary detached
worktree, never from the person's checkout. Every comment act.py posts
carries the Claude Code attribution footer except the approval review body,
which follows references/message-templates.md (one line, no process
narration).

GitHub goes through gh_client.GhClient (gh / REST token / snapshot); git
through the small `Git` wrapper here so tests stub both. Deterministic, no
model calls — the drafted description fix and the judgments come in on the
queue, written by the judge step before this runs.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_REPO_ROOT = _HERE.parent.parent
sys.path.insert(0, str(_HERE))
import collect  # noqa: E402
import gh_client  # noqa: E402
from gh_client import GhClient, GhError, norm_login  # noqa: E402

FOOTER = "\n\n---\n_Generated by [Claude Code](https://claude.ai/code)_"
STAMP_STATES = ("clean", "blocked")
DEPLOY_WORKFLOW = "testing-build-and-deploy.yml"
SHOTS_DIR = _REPO_ROOT / ".pr-review-shots"
PLAN_SCHEMA = 2  # 2: every body is rendered into step.args at plan time; steps can `requires` another
COMMIT_TRAILER_ENV = "PR_REVIEW_COMMIT_TRAILER"  # e.g. "Co-Authored-By: …"; appended to commits act.py makes
# A PR takes one decision; two of these on the same PR contradict each other.
DECISION_KINDS = ("stamp", "request-changes", "close", "route")
# The steps a --reason can land on. A close with --superseded-by writes its own.
REASON_KINDS = ("request-changes", "refresh", "rerun", "close")
# The Sentinel concludes failure until an approval exists, so it can't gate
# the approval it waits for. It is left out of the pre-approval rollup and
# polled on its own between the approval and the merge.
SENTINEL_CHECK = "sentinel"
SENTINEL_WAIT_S = 90
SENTINEL_POLL_S = 10
# A conflicted --unblock used to fail into the run's stdout and nowhere else:
# nothing was written, so the next collect saw the same `mergeable:dirty` and
# the board offered the same "merge base & retry" button, forever. The marker
# carries the head the merge was attempted against, so collect can tell a
# conflict that still stands from one a later push already settled.
UNBLOCK_CONFLICT_MARKER = "<!-- PR_REVIEW_UNBLOCK_CONFLICT -->"


class ActError(Exception):
    pass


@dataclass
class Step:
    kind: str
    pr: int
    args: dict = field(default_factory=dict)
    expect_head: str = ""
    title: str = ""
    author: str = ""
    author_type: str = "bot"
    branch: str = ""
    verdict: str = ""
    note: str = ""


@dataclass
class Plan:
    schema: int
    repo: str
    created_at: str
    options: dict
    steps: list[Step]

    def to_json(self) -> dict:
        return {"schema": self.schema, "repo": self.repo, "created_at": self.created_at,
                "options": self.options, "steps": [asdict(s) for s in self.steps]}

    @classmethod
    def from_json(cls, d: dict) -> "Plan":
        if d.get("schema") != PLAN_SCHEMA:
            raise ActError(f"plan schema {d.get('schema')} is not {PLAN_SCHEMA}; re-plan with this act.py")
        return cls(d["schema"], d["repo"], d["created_at"], d.get("options") or {}, [Step(**s) for s in d["steps"]])


@dataclass
class Result:
    step: Step
    ok: bool
    message: str
    writes: list[dict] = field(default_factory=list)


# ---- policy -----------------------------------------------------------------


def push_allowed(pr: dict) -> tuple[bool, str]:
    """Which bot branches may be pushed to (see references/action-menus.md)."""
    login = norm_login((pr.get("author") or {}).get("login"))
    labels = set(pr.get("labels") or [])
    if login.startswith("dependabot"):
        return False, "dependabot PRs are regenerated, never edited"
    if login == "pulumi-bot" and "automation/merge" in labels:
        return False, "generated-docs regens are regenerated, never edited"
    if (pr.get("head") or {}).get("is_fork"):
        return False, "fork head: no push access"
    return True, "merge commits only, never rebase or force-push"


def approval_body(author_type: str, trust: str = "high", note: str = "") -> str:
    """references/message-templates.md: bot 1 sentence, internal ≤2,
    external ≤3 (welcome only for a first-timer). No footer, no process."""
    if author_type == "bot":
        body = "Approved."
    elif author_type == "external":
        body = "Thanks! LGTM." + (" Welcome to Pulumi. 🎉" if trust == "low" else " 🎉")
    else:
        body = "LGTM."
    if note:
        body += " " + note.strip()
    return body


def with_footer(body: str) -> str:
    return body.rstrip() + FOOTER


# ---- planning ------------------------------------------------------------------


def _listed(v) -> list:
    """argparse `append` gives a list; a test or an older caller may pass one value."""
    if v is None:
        return []
    return list(v) if isinstance(v, (list, tuple)) else [v]


def _split_stamps(spec) -> list[tuple[int, str | None]]:
    """`21598,21600:no-merge` → [(21598, None), (21600, "no-merge")]. The
    suffix is a per-PR override of the merge default, so one command can
    approve a mixed batch and say for each row whether it merges. `--stamp`
    repeats, so `spec` may be a list of such values; they flatten in order."""
    out: list[tuple[int, str | None]] = []
    for value in _listed(spec):
        for part in re.split(r"[,\s]+", str(value).strip()):
            if not part:
                continue
            num, _, mode = part.lstrip("#").partition(":")
            if mode and mode not in ("merge", "no-merge"):
                raise ActError(f"--stamp {part}: the only per-PR modes are :merge and :no-merge")
            out.append((int(num), mode or None))
    return out


REASON_SCOPED_RE = re.compile(r"^#?(\d+)=(.*)$", re.S)


def _split_reasons(values) -> tuple[dict[int, str], list[str]]:
    """`N=text` is scoped to PR N; anything else is a bare reason. Returns
    (scoped by PR, bare list). Two scoped values for one PR is a contradiction."""
    scoped: dict[int, str] = {}
    bare: list[str] = []
    for v in _listed(values):
        m = REASON_SCOPED_RE.match(str(v).strip())
        if not m:
            bare.append(str(v).strip())
            continue
        n, text = int(m.group(1)), m.group(2).strip()
        if n in scoped and scoped[n] != text:
            raise ActError(f"--reason {n}=…: two different reasons for #{n}")
        scoped[n] = text
    return scoped, bare


def _split_supersedes(values, closes: list[int]) -> dict[int, int]:
    """`--superseded-by M` (only with exactly one --close) or `--superseded-by
    N:M` (repeatable) → {N: M}."""
    out: dict[int, int] = {}
    for v in _listed(values):
        s = str(v).strip().lstrip("#")
        if ":" in s:
            n, _, m = s.partition(":")
            n, m = int(n), int(m.lstrip("#"))
        else:
            if len(closes) != 1:
                raise ActError(f"--superseded-by {s}: with {len(closes)} --close values, say which one as --superseded-by N:{s}")
            n, m = closes[0], int(s)
        if n not in closes:
            raise ActError(f"--superseded-by {n}:{m}: #{n} is not being closed (--close {n})")
        if n in out and out[n] != m:
            raise ActError(f"--superseded-by {n}:…: two different supersessions for #{n}")
        out[n] = m
    return out


def _dedupe(steps: list[Step]) -> list[Step]:
    """The board composer never repeats a fragment, but a typed command can:
    an identical (kind, pr) repeat is dropped silently, and a PR carrying two
    different decisions — or the same kind with different arguments — is a
    contradiction the plan refuses rather than posts twice."""
    out: list[Step] = []
    seen: dict[tuple[str, int], Step] = {}
    decisions: dict[int, str] = {}
    for s in steps:
        key = (s.kind, s.pr)
        prev = seen.get(key)
        if prev is not None:
            strip = ("chain", "requires")
            if {k: v for k, v in prev.args.items() if k not in strip} == {k: v for k, v in s.args.items() if k not in strip}:
                continue
            raise ActError(f"#{s.pr}: --{s.kind} given twice with different arguments; pick one")
        if s.kind in DECISION_KINDS:
            other = decisions.get(s.pr)
            if other and other != s.kind:
                raise ActError(f"#{s.pr}: --{other} and --{s.kind} contradict each other; a PR takes one decision")
            decisions[s.pr] = s.kind
        seen[key] = s
        out.append(s)
    return out


def row_route_targets(pr: dict) -> list[str]:
    """The row's own route targets: `route_targets` when the analyzer wrote
    it, else every `--route N:@x` fragment of the row's route action."""
    if pr.get("route_targets"):
        return list(pr["route_targets"])
    a = next((a for a in pr.get("actions") or [] if a["id"] == "route"), None)
    if not a:
        return []
    if a.get("targets"):
        return list(a["targets"])
    return re.findall(r"--route\s+\d+:(\S+)", a.get("cmd") or "")


def plan(queue: dict, args: argparse.Namespace) -> Plan:
    by = {p["number"]: p for p in queue.get("prs") or []}

    def pr_of(n: int) -> dict:
        if n not in by:
            raise ActError(f"#{n} is not in the queue; re-run collect (drafts and filtered rows are never acted on)")
        return by[n]

    def step(kind: str, n: int, **kw) -> Step:
        pr = pr_of(n)
        return Step(kind, n, kw, expect_head=(pr.get("head") or {}).get("sha") or "", title=pr.get("title") or "",
                    author=(pr.get("author") or {}).get("login") or "", author_type=(pr.get("author") or {}).get("type") or "bot",
                    branch=(pr.get("head") or {}).get("ref") or "", verdict=pr.get("verdict") or "")

    def stamp_step(n: int, mode: str | None, *, force: bool, chain: str | None = None) -> Step:
        """The one code path for approving a row: --stamp and --chain both
        come through here, so the chain gets the plan-time blocker check the
        stamp has."""
        pr = pr_of(n)
        if pr.get("verdict") != "stamp" and not force:
            raise ActError(f"#{n} is {pr.get('verdict')}, not stamp — pass --force to approve as-is ({', '.join(pr.get('reasons') or [])})")
        if pr.get("verdict") == "blocked":
            raise ActError(f"#{n} is blocked ({', '.join(pr.get('blockers') or [])}); unblock it first")
        author = pr.get("author") or {}
        is_bot = author.get("type") == "bot"
        # A bot PR exists to be merged; a person's PR is theirs to merge. The
        # per-PR mode beats both that default and the blanket flags.
        if mode:
            merge = mode == "merge"
        else:
            merge = not args.no_merge and (is_bot or args.merge_humans)
        note = args.approve_note or ""
        s = step("stamp", n, merge=merge, note=note,
                 body=approval_body(author.get("type") or "bot", author.get("etiquette_trust") or "high", note))
        if chain:
            s.args["chain"] = chain
        if merge:
            open_ids = unanswered_blockers(pr.get("review") or {})
            if open_ids:
                raise ActError(refuse_merge_over_findings(n, open_ids))
            s.note = ""
        elif mode == "no-merge":
            s.note = "approve only (asked not to merge)"
        elif is_bot:
            s.note = "approve only (--no-merge)"
        else:
            s.note = "approve only (human author; --stamp N:merge or --merge-humans to merge)"
        return s

    closes = [int(n) for n in _listed(args.close)]
    scoped_reasons, bare_reasons = _split_reasons(args.reason)
    supersedes = _split_supersedes(args.superseded_by, closes)

    steps: list[Step] = []
    for n, mode in _split_stamps(args.stamp):
        steps.append(stamp_step(n, mode, force=bool(args.force)))
    routes: dict[int, list[str]] = {}
    for spec in _listed(args.route):
        n, _, target = str(spec).lstrip("#").partition(":")
        pr = pr_of(int(n))
        targets = [target] if target else list(row_route_targets(pr))
        if not targets:
            raise ActError(f"--route {spec}: no target and the row has no route action")
        for t in targets:
            t = "@" + t.lstrip("@")
            if t not in routes.setdefault(int(n), []):
                routes[int(n)].append(t)
    for n, targets in routes.items():
        # One step per PR however many targets: one review request carrying
        # every reviewer, one comment.
        steps.append(step("route", n, target=", ".join(targets), targets=targets,
                          comment=_defect_comment(pr_of(n), " and ".join(targets))))
    for n in _listed(args.request_changes):
        pr = pr_of(n)
        if not ask_lines(pr) and n not in scoped_reasons and not bare_reasons:
            raise ActError(f"--request-changes {n}: nothing to send back — no open findings on the row, "
                           f"no judgment carries an ask, and no --reason {n}=\"…\" says why")
        if not can_revise(pr) and not args.force:
            login = (pr.get("author") or {}).get("login") or "the author"
            raise ActError(f"--request-changes {n}: @{login} is a workflow, not an author — it will never read the review. "
                           f"Fix it here (--fix {n}) or close it (--close {n} --reason \"…\") and let the lane re-queue.")
        steps.append(step("request-changes", n, reason=""))
    for cid in _listed(args.chain):
        c = next((c for c in queue.get("clusters") or [] if c["id"] == cid), None)
        if not c:
            raise ActError(f"--chain {cid}: no such cluster in the queue")
        r = c.get("recommendation") or {}
        if r.get("kind") != "chain":
            raise ActError(f"--chain {cid}: the cluster's recommendation is {r.get('kind') or 'none'}, not chain ({r.get('say', '')})")
        first, nxt = r["first"], r.get("next")
        st = stamp_step(first, None, force=True, chain=cid)
        steps.append(st)
        if nxt and st.args["merge"]:
            ok, why = push_allowed(pr_of(nxt))
            if not ok:
                raise ActError(f"--chain {cid}: next link #{nxt} can't be pushed to: {why}")
            # The next link only needs unblocking once the first has landed
            # on master; if the stamp is refused, merging master into it
            # would just be a push nobody asked for.
            steps.append(step("unblock", nxt, chain=cid, requires=["stamp", first]))
    for n in _listed(args.unblock):
        pr = pr_of(n)
        ok, why = push_allowed(pr)
        if not ok:
            raise ActError(f"--unblock {n}: {why}")
        steps.append(step("unblock", n))
    for n in _listed(args.fix):
        pr = pr_of(n)
        ok, why = push_allowed(pr)
        draft = pr.get("fix_draft") or {}
        has_desc = bool(draft.get("kind") == "description" and draft.get("body"))
        suggestions = planned_suggestions(pr)
        if not (has_desc or suggestions):
            raise ActError(f"--fix {n}: nothing to apply — no drafted description and no one-click suggestions on the row")
        if suggestions and not ok:
            raise ActError(f"--fix {n}: {why}")
        steps.append(step("fix", n, description=has_desc, body=draft.get("body") if has_desc else None,
                          suggestions=suggestions))
    for n in closes:
        pr_of(n)
        m = supersedes.get(n)
        if m:
            pr_of(m)
            steps.append(step("close", n, superseded_by=m, reason=None,
                              comment=with_footer(f"Closing in favor of #{m}, which covers the same change."),
                              supersede_comment=with_footer(f"Supersedes #{n}, closed as a duplicate.")))
        else:
            steps.append(step("close", n, superseded_by=None, reason=None))
    for n in _listed(args.ask_fix):
        pr = pr_of(n)
        items = ask_fix_items(pr)
        if not items:
            raise ActError(f"--ask-fix {n}: no open findings to name — nothing to ask for")
        steps.append(step("ask-fix", n, items=items))
    for n in _listed(args.refresh):
        pr = pr_of(n)
        steps.append(step("refresh", n, reason=next((r for r in pr.get("reasons") or [] if r.startswith("review:")), "the review is stale")))
    for n in _listed(args.rerun):
        pr = pr_of(n)
        status = ((pr.get("review") or {}).get("status") or "ABSENT").lower().replace("_", "-")
        steps.append(step("rerun", n, reason={"error": "the last review run failed", "absent": "no review ran on this PR",
                                              "triage-prose": "only the triage prose check ran"}.get(status, f"the review is {status}")))
    for n in _listed(args.rerun_checks):
        steps.append(step("rerun-checks", n))
    for n in _listed(args.render):
        steps.append(step("render", n, pages=(pr_of(n).get("preview") or {}).get("pages") or []))
    for n in _listed(args.deploy):
        steps.append(step("deploy", n))
    if not steps:
        raise ActError("nothing to do: pass --stamp / --route / --unblock / --fix / --close / --ask-fix / --refresh / --rerun / --rerun-checks / --render / --deploy")
    steps = _dedupe(steps)
    _assign_reasons(steps, by, scoped_reasons, bare_reasons)
    for s in steps:
        _render_bodies(s, by[s.pr])
    return Plan(PLAN_SCHEMA, queue.get("repo") or gh_client.DEFAULT_REPO, datetime.now(timezone.utc).isoformat(timespec="seconds"),
                {"merge_humans": bool(args.merge_humans), "no_merge": bool(args.no_merge), "force": bool(args.force)}, steps)


def _takes_reason(s: Step) -> bool:
    return s.kind in REASON_KINDS and not (s.kind == "close" and s.args.get("superseded_by"))


def _assign_reasons(steps: list[Step], by: dict, scoped: dict[int, str], bare: list[str]) -> None:
    """Put each --reason on the one step it belongs to. `N=text` goes to
    every reason-taking step on #N. Bare text goes to the single step that
    needs one — a request-changes, refresh, rerun, or a close on a PR with an
    author; a generated row's close writes its own from the judgments and
    takes a reason only when it is scoped to it explicitly. Anything else is
    an ambiguity the plan refuses instead of guessing."""
    for n, text in scoped.items():
        targets = [s for s in steps if s.pr == n and _takes_reason(s)]
        if not targets:
            raise ActError(f"--reason {n}=…: no step on #{n} takes a reason (request-changes, refresh, rerun, or close without --superseded-by)")
        for s in targets:
            s.args["reason"] = text
    if len(bare) > 1:
        raise ActError("more than one bare --reason; scope each as --reason N=\"…\"")
    if bare:
        wants = [s for s in steps if _takes_reason(s) and s.pr not in scoped
                 and (s.kind != "close" or can_revise(by[s.pr]))]
        if not wants:
            raise ActError("--reason given, but no step in the plan takes one (request-changes, refresh, rerun, or close on a PR with an author)")
        if len(wants) > 1:
            names = ", ".join(f"{s.kind} #{s.pr}" for s in wants)
            raise ActError(f"--reason applies to more than one step ({names}); scope it as --reason N=\"…\"")
        wants[0].args["reason"] = bare[0]
    for s in steps:
        if s.kind == "close" and not s.args.get("superseded_by") and not s.args.get("reason"):
            if can_revise(by[s.pr]):
                # Closing someone's PR without saying why is the one thing worse
                # than sitting on it. A workflow-authored row writes its own.
                raise ActError(f"--close {s.pr}: needs --superseded-by M, or --reason {s.pr}=\"…\" saying why it is closing")
            s.args["reason"] = close_reason(by[s.pr])


def _render_bodies(s: Step, pr: dict) -> None:
    """Every body the step will send, fixed now so a re-collect between the
    plan and the execute can't change what goes out."""
    if s.kind == "request-changes":
        s.args["body"] = request_changes_body(pr, s.args.get("reason") or "")
    elif s.kind == "close" and not s.args.get("superseded_by"):
        s.args["comment"] = with_footer(s.args["reason"])
    elif s.kind == "ask-fix":
        s.args["comment"] = ask_fix_body(pr, s.args["items"])
    elif s.kind == "refresh":
        s.args["comment"] = with_footer(f"@claude {s.args['reason']} #update-review")
    elif s.kind == "rerun":
        s.args["comment"] = with_footer(f"@claude {s.args['reason']} #new-review")


def _body_head(body, width: int = 100) -> str:
    text = body.get("body") if isinstance(body, dict) and isinstance(body.get("body"), str) else json.dumps(body)
    first = (text or "").strip().splitlines()[0] if (text or "").strip() else ""
    return first[:width] + ("…" if len(first) > width else "")


def _indent(text: str, pad: str = "       ") -> list[str]:
    return [pad + ln for ln in text.splitlines()]


def preview(plan_: Plan, queue: dict | None = None) -> str:
    lines = [f"Plan · {plan_.repo} · {len(plan_.steps)} step(s)", ""]
    for i, s in enumerate(plan_.steps, 1):
        head = s.expect_head[:7]
        lines.append(f"{i}. {s.kind.upper():<8} #{s.pr} {s.title}  (@{s.author}, head {head})")
        if s.kind == "stamp":
            lines.append(f"     preflight: open, head == {head}, mergeable_state ∈ {STAMP_STATES}, checks green (Sentinel aside), "
                         "no changes-requested by anyone else" + (", no unanswered 🚨 finding" if s.args.get("merge") else ""))
            lines.append(f"     POST review APPROVE: \"{s.args.get('body') or approval_body(s.author_type, note=s.args.get('note', ''))}\"")
            if s.args.get("merge"):
                lines.append(f"     wait for the Sentinel check (≤{SENTINEL_WAIT_S}s), then PUT merge (squash)")
            else:
                lines.append(f"     no merge — {s.note}")
            if s.args.get("chain"):
                lines.append(f"     [chain {s.args['chain']}: first link]")
        elif s.kind == "route":
            lines.append(f"     preflight: open, head == {head}")
            lines.append(f"     request review from {s.args['target']}; comment:")
            lines += _indent(s.args["comment"])
        elif s.kind == "request-changes":
            lines.append(f"     preflight: open, head == {head}")
            lines.append("     POST review CHANGES_REQUESTED + label needs-author-response; body:")
            lines += _indent(s.args["body"])
        elif s.kind == "unblock":
            lines.append(f"     preflight: open, head == {head}, origin/{s.branch} == {head} after fetch")
            lines.append(f"     git: worktree at origin/{s.branch}, merge origin/master --no-ff, push HEAD:{s.branch} (abort on conflict)"
                         + (f"  [chain {s.args['chain']}: next link; skipped unless stamp #{s.args['requires'][1]} merges]"
                            if s.args.get("chain") else ""))
        elif s.kind == "fix":
            lines.append(f"     preflight: open, head == {head}")
            if s.args.get("description"):
                lines.append(f"     PATCH pull body: {_body_head({'body': s.args.get('body')})}")
            sugg = s.args.get("suggestions") or []
            if sugg:
                lines.append(f"     git: worktree at origin/{s.branch}, apply {len(sugg)} suggestion(s) bottom-up, commit, push HEAD:{s.branch}"
                             " (a suggestion whose comment is outdated on the head is skipped)")
                for sg in sugg:
                    span = f"L{sg['start_line']}-{sg['line']}" if sg.get("start_line") and sg["start_line"] != sg["line"] else f"L{sg['line']}"
                    lines.append(f"       · {sg['path']} {span} → {_body_head({'body': sg['replacement']}, 80) or '(delete)'}")
        elif s.kind == "close":
            lines.append(f"     preflight: open, head == {head}")
            if s.args.get("superseded_by"):
                lines.append(f"     comment on #{s.pr}: {_body_head({'body': s.args['comment']})}")
                lines.append(f"     comment on #{s.args['superseded_by']}: {_body_head({'body': s.args['supersede_comment']})}")
                lines.append(f"     PATCH #{s.pr} state=closed")
            else:
                lines.append(f"     comment on #{s.pr}:")
                lines += _indent(s.args["comment"])
                lines.append(f"     PATCH #{s.pr} state=closed")
        elif s.kind == "ask-fix":
            lines.append(f"     preflight: open, head == {head}")
            lines.append(f"     comment on #{s.pr} ({len(s.args['items'])} finding(s); one comment, nothing pushed):")
            lines += _indent(s.args["comment"])
        elif s.kind in ("refresh", "rerun"):
            lines.append(f"     preflight: open, head == {head}")
            lines.append(f"     comment: {_body_head({'body': s.args['comment']})} (+ footer)"
                         + (" — clears the cards, fresh review from scratch" if s.kind == "rerun" else ""))
        elif s.kind == "rerun-checks":
            lines.append(f"     preflight: open, head == {head}")
            lines.append(f"     GET actions/runs?head_sha={head}; POST actions/runs/<id>/rerun-failed-jobs for each newest failed run per workflow")
        elif s.kind == "render":
            lines.append(f"     screenshot {len(s.args.get('pages') or [])} preview page(s) → {SHOTS_DIR}/{s.pr}/")
        elif s.kind == "deploy":
            lines.append(f"     preflight: open, head == {head}")
            lines.append(f"     dispatch {DEPLOY_WORKFLOW} @ {s.branch}")
    lines += ["", "Run: act.py --execute <plan.json>   (add --dry-run to run the preflights and print every write it would make, sending none)"]
    return "\n".join(lines) + "\n"


# ---- git ------------------------------------------------------------------------


class Git:
    """Thin subprocess wrapper; every method is stubbed in tests. Branch work
    happens in a detached worktree (`add_worktree`) so the person's checkout
    — its branch, its unpushed commits, its dirty files — is never touched."""

    def __init__(self, repo_root: Path = _REPO_ROOT):
        self.root = repo_root

    def run(self, *args: str, check: bool = True) -> subprocess.CompletedProcess:
        return subprocess.run(["git", *args], cwd=self.root, text=True, capture_output=True, check=check)

    def fetch(self, *refs: str) -> None:
        self.run("fetch", "origin", *refs)

    def rev_parse(self, ref: str) -> str:
        return self.run("rev-parse", ref).stdout.strip()

    def add_worktree(self, ref: str) -> "Git":
        """A fresh detached worktree at `ref`, in a temp dir; the returned Git
        is rooted there. Remove it with `remove_worktree`."""
        tmp = Path(tempfile.mkdtemp(prefix="pr-review-wt-"))
        path = tmp / "wt"
        self.run("worktree", "add", "--detach", str(path), ref)
        return Git(path)

    def remove_worktree(self, wt: "Git") -> None:
        """`--force`: whatever the worktree holds — a half-applied fix, a
        conflicted merge — is discarded with it."""
        self.run("worktree", "remove", "--force", str(wt.root), check=False)
        shutil.rmtree(wt.root.parent, ignore_errors=True)
        self.run("worktree", "prune", check=False)

    def merge(self, ref: str) -> bool:
        """True when the merge completed; False when it stopped on conflicts."""
        return self.run("merge", "--no-ff", "--no-edit", ref, check=False).returncode == 0

    def conflicted_files(self) -> list[str]:
        return [l for l in self.run("diff", "--name-only", "--diff-filter=U").stdout.splitlines() if l]

    def add(self, *paths: str) -> None:
        self.run("add", "--", *paths)

    def commit(self, message: str) -> str:
        self.run("commit", "-m", message)
        return self.run("rev-parse", "HEAD").stdout.strip()

    def push(self, branch: str) -> None:
        self.run("push", "origin", f"HEAD:{branch}")  # never --force


def apply_suggestion(root: Path, path: str, start_line: int, end_line: int, replacement: str) -> None:
    f = root / path
    lines = f.read_text().splitlines(keepends=True)
    new = [l if l.endswith("\n") else l + "\n" for l in replacement.splitlines()]
    lines[start_line - 1:end_line] = new
    f.write_text("".join(lines))


SUGGESTION_RE = re.compile(r"```suggestion\n(.*?)```", re.S)


def planned_suggestions(pr: dict) -> list[dict]:
    """The row's one-click suggestions as the plan carries them: id, path,
    the line span the queue knows, and the replacement text. collect.py keeps
    only `line` (falling back to `original_line`) and drops `start_line`, so
    the span here is provisional; `live_suggestions` re-reads the raw review
    comment at execute time for the authoritative one and to drop a comment
    the head has outdated."""
    out = []
    for sg in pr.get("one_click_suggestions") or []:
        m = SUGGESTION_RE.search(sg.get("body") or "")
        if not m or not sg.get("path") or not sg.get("line"):
            continue
        end = int(sg["line"])
        out.append({"id": sg.get("id"), "path": sg["path"], "line": end,
                    "start_line": int(sg.get("start_line") or end), "replacement": m.group(1)})
    return out


def live_suggestions(gh: GhClient, number: int, planned: list[dict]) -> tuple[list[dict], list[str]]:
    """Re-anchor each planned suggestion on the raw review comment: `line`
    null means GitHub has marked it outdated on the current head, so it is
    skipped instead of applied at its original line; `start_line` (multi-line
    suggestions) comes only from here. Returns (applicable, skipped reasons)."""
    raw = {c.get("id"): c for c in gh.review_comments(number)}
    live, skipped = [], []
    for sg in planned:
        c = raw.get(sg.get("id"))
        if c is None:
            skipped.append(f"{sg['path']} L{sg['line']}: review comment {sg.get('id')} is gone")
            continue
        if not c.get("line"):
            skipped.append(f"{sg['path']} L{sg['line']}: outdated on the current head")
            continue
        end = int(c["line"])
        live.append({**sg, "path": c.get("path") or sg["path"], "line": end, "start_line": int(c.get("start_line") or end)})
    return live, skipped


def commit_message(subject: str) -> str:
    trailer = os.environ.get(COMMIT_TRAILER_ENV, "").strip()
    return subject + (f"\n\n{trailer}" if trailer else "")


# ---- execution --------------------------------------------------------------------


def preflight_head(gh: GhClient, s: Step) -> tuple[bool, str, dict]:
    """The check every write runs first: the PR is still open and its head is
    the one the plan was made against. Anything else means the board this
    step came from is stale — re-collect and re-plan."""
    detail = collect.fetch_detail(gh, s.pr)
    head = (detail.get("head") or {}).get("sha") or ""
    if detail.get("state", "open") != "open":
        return False, f"head-state: PR is {detail.get('state')}", detail
    if s.expect_head and head != s.expect_head:
        return False, f"head-moved: planned {s.expect_head[:7]}, now {head[:7]} — re-collect and re-plan", detail
    return True, "ok", detail


def _is_sentinel(run: dict) -> bool:
    return (run.get("name") or "").strip().lower() == SENTINEL_CHECK


def preflight(gh: GhClient, s: Step) -> tuple[bool, str, dict]:
    """Re-fetch the PR immediately before merging. master moves during a
    batch and a squash earlier in this run can dirty a later PR."""
    ok, msg, detail = preflight_head(gh, s)
    if not ok:
        return ok, msg, detail
    head = (detail.get("head") or {}).get("sha") or ""
    ms = detail.get("mergeable_state") or "unknown"
    if ms not in STAMP_STATES:
        return False, f"mergeable_state={ms}", detail
    runs = [r for r in gh.check_runs(head) if not _is_sentinel(r)]
    checks = collect.checks_rollup(runs, gh.commit_statuses(head), gh.workflow_paths(head))
    if checks["state"] != "green":
        return False, f"checks {checks['state']}: {', '.join(checks['failing'] or checks['pending'])}", detail
    # Latest review per user wins. The approver's own changes-requested is
    # superseded by the approval this step is about to post, so it is not a
    # blocker; anyone else's is.
    me = norm_login(gh.me())
    latest: dict[str, str] = {}
    for r in sorted(gh.reviews(s.pr), key=lambda r: r.get("submitted_at") or ""):
        if ((r.get("user") or {}).get("type") or "") != "Bot" and r.get("state") in ("APPROVED", "CHANGES_REQUESTED"):
            latest[(r.get("user") or {}).get("login") or ""] = r["state"]
    who = [u for u, st in latest.items() if st == "CHANGES_REQUESTED" and not (me and norm_login(u) == me)]
    if who:
        return False, f"changes requested by {', '.join(who)}", detail
    if s.args.get("merge"):
        # Re-read the review cards, not the queue's copy of them: a review can
        # land or re-render between the plan and this moment without moving the
        # head, so a row that planned clean can arrive here with open findings.
        try:
            author_c, brief_c, _ = collect.find_review_comments(gh.issue_comments(s.pr))
        except GhError as e:
            return False, f"could not re-read the review cards ({e}) — not merging over an unverified review", detail
        author_body = (author_c or {}).get("body") or ""
        missing = (author_c or {}).get("review_pages_missing") or []
        if missing:
            # A split (v2) review whose later comments did not come back:
            # its findings sections are the tail of the document, so "no
            # open findings" here would mean "none arrived", not "none".
            return False, (f"the review is {author_c.get('review_pages')} comments and page(s) "
                           f"{', '.join(str(k) for k in missing)} could not be read — not merging over "
                           "a review this step cannot see whole"), detail
        if author_body:
            review = collect.parse_review(author_body, (brief_c or {}).get("body") or "", s.pr, gh.repo)
            if review.get("counts_shortfall"):
                return False, ("the review's own tally declares more findings than its sections parsed into "
                               f"({review['counts_shortfall']}) — not merging over a review that arrived incomplete"), detail
            open_ids = unanswered_blockers(review)
            if open_ids:
                return False, f"{len(open_ids)} unanswered blocking finding(s) on the review: {', '.join(open_ids)}", detail
    return True, "ok", detail


def wait_for_sentinel(gh: GhClient, head: str, sleep=time.sleep) -> tuple[bool, str]:
    """After the approval, before the merge: the Sentinel re-evaluates on the
    review event, so give it a bounded wait and refuse the merge if it lands
    red. Absent, neutral or green all proceed; still pending at the deadline
    refuses — re-running the step retries the merge without re-approving."""
    attempts = SENTINEL_WAIT_S // SENTINEL_POLL_S
    for attempt in range(attempts + 1):
        runs = [r for r in gh.check_runs(head) if _is_sentinel(r)]
        if not runs:
            return True, "no Sentinel check on the head"
        run = max(runs, key=collect._run_order)
        if run.get("status") == "completed":
            c = run.get("conclusion") or ""
            if c in collect.FAILED_CONCLUSIONS:
                return False, f"Sentinel check concluded {c}"
            return True, f"Sentinel {c or 'completed'}"
        if attempt < attempts:
            sleep(SENTINEL_POLL_S)
    return False, f"Sentinel check still pending after {SENTINEL_WAIT_S}s; re-run the step to retry the merge"


def open_items(pr: dict) -> list[dict]:
    return [i for i in (pr.get("review") or {}).get("items") or []
            if not i.get("disposition") and i.get("bucket") not in ("style", "pre-existing", "preexisting")]


def ask_lines(pr: dict) -> list[str]:
    """The row's open items as line-anchored bullets: the judgments when the
    judge step ran, else the findings still open on the card. A judgment the
    approver already decided (`RESOLVABLE`) has nothing for the author to do,
    so it rides along only when it carries an explicit `ask`: its `decision`
    is the approver's question, and posting it would invite the author to
    change what the approver decided to leave alone. A finding the judge
    step never reached is still open, so it is listed from the card after
    the judged ones: a partial judgment must not drop it from the review."""
    judgments = pr.get("judgments") or []
    lines = []
    judged = set()
    for j in judgments:
        judged.add((j.get("finding_id") or "").strip())
        where = f"`{j['file']}` L{j['line']}: " if j.get("file") and j.get("line") else ""
        ask = (j.get("ask") or "").strip()
        if not ask and j.get("disposition") not in RESOLVABLE:
            ask = (j.get("decision") or "").strip()
        if ask:
            lines.append(f"- {where}{ask}")
    for i in open_items(pr):
        if (i.get("id") or "").strip() in judged:
            continue
        where = f"`{i['file']}` {i.get('anchor') or ''}: " if i.get("file") else f"{i.get('anchor') or ''}: "
        lines.append(f"- {where}{(i.get('summary') or i.get('text') or '').strip()}")
    return lines


def request_changes_body(pr: dict, note: str = "") -> str:
    """references/message-templates.md, Request changes row: line-anchored
    issues, no filler; the bot variant names the issue and what to change.
    A judgment's `ask` is the author-facing sentence; `decision` (the
    question the approver answered) stands in when there is no `ask`, except
    on a judgment the approver already decided (see `ask_lines`). The
    `note` is the approver's rationale and never leaves the board. Open
    findings fill in when the judge step didn't run on the row."""
    lines = []
    if note.strip():
        lines.append(note.strip())
    lines.extend(ask_lines(pr))
    atype = (pr.get("author") or {}).get("type")
    if atype == "external":
        lines = ["Thanks for this. A few things before it can merge:", ""] + lines + ["", "Mention @claude if you need help."]
    elif atype == "bot":
        lines.append("")
        lines.append("Answer each with `@claude F<n>: <reason> #update-review`, or push the fix.")
    return "\n".join(lines).strip()


def _defect_comment(pr: dict, target: str) -> str:
    lines = [f"Routing to {target}: this is a {'/'.join(pr.get('domains') or ['?'])} change, not mine to approve."]
    # Only what a reviewer acts on. The queue's own proxies (desc:, brief:,
    # blog:, cluster:, review:) are noise to anyone who isn't running it.
    defects = [r for r in pr.get("reasons") or [] if r.split(":")[0] in
               ("warnings", "outstanding", "directional", "duplicate", "merging-over")]
    if defects:
        lines.append("")
        lines.append("What the queue flagged:")
        lines += [f"- `{d}`" for d in defects]
    for j in pr.get("judgments") or []:
        lines.append("")
        head = f"**{j.get('finding_id') or ''}** {j.get('decision') or ''}".strip()
        lines.append(head)
        if j.get("deep_link"):
            lines.append(f"  {j['deep_link']}")
        if j.get("disposition"):
            lines.append(f"  suggested: {j['disposition']}")
    return with_footer("\n".join(lines))


def execute(plan_: Plan, gh: GhClient, git: Git | None = None, *, queue: dict | None = None,
            dry_run: bool = False, repo_root: Path = _REPO_ROOT, node: str = "node", sleep=time.sleep) -> list[Result]:
    """Run the plan. Every body comes from the step; `queue` is accepted for
    older callers and unused. In dry-run the client records each write it
    would make instead of sending it, and git is never run."""
    del queue
    if dry_run:
        gh = gh.dry()
    results: list[Result] = []
    merged: set[int] = set()
    done_ok: set[tuple[str, int]] = set()
    for s in plan_.steps:
        before = len(gh.writes)
        try:
            req = s.args.get("requires")
            if req and (tuple(req) not in done_ok or (req[0] == "stamp" and req[1] not in merged)):
                ok, msg = False, f"skipped: waits on {req[0]} #{req[1]}, which did not {'merge' if req[0] == 'stamp' else 'succeed'}"
            elif s.kind == "stamp":
                ok, msg, did_merge = _stamp(gh, s, dry_run=dry_run, sleep=sleep)
                if did_merge:
                    merged.add(s.pr)
            elif s.kind == "route":
                ok, msg = _route(gh, s)
            elif s.kind == "request-changes":
                ok, msg = _request_changes(gh, s)
            elif s.kind == "unblock":
                ok, msg = _unblock(gh, git or Git(repo_root), s, dry_run=dry_run)
            elif s.kind == "fix":
                ok, msg = _fix(gh, git or Git(repo_root), s, dry_run=dry_run)
            elif s.kind == "close":
                ok, msg = _close(gh, s)
            elif s.kind in ("ask-fix", "refresh", "rerun"):
                ok, msg = _mention(gh, s)
            elif s.kind == "rerun-checks":
                ok, msg = _rerun_checks(gh, s)
            elif s.kind == "render":
                ok, msg = _render(s, node=node)
            elif s.kind == "deploy":
                ok, msg = _deploy(gh, s)
            else:
                ok, msg = False, f"unknown step kind {s.kind}"
        except (GhError, ActError, subprocess.CalledProcessError, OSError) as exc:
            ok, msg = False, f"{type(exc).__name__}: {exc}"
        if ok and dry_run and not msg.startswith("dry-run"):
            msg = f"dry-run: would have {msg}"
        if ok:
            done_ok.add((s.kind, s.pr))
        results.append(Result(s, ok, msg, gh.writes[before:]))
    return results


def _already_commented(comments: list[dict], me: str, body: str) -> bool:
    return any(norm_login((c.get("user") or {}).get("login")) == me and (c.get("body") or "").strip() == body.strip()
               for c in comments) if me else False


def _already_approved(reviews: list[dict], me: str, head: str) -> bool:
    return any(norm_login((r.get("user") or {}).get("login")) == me and r.get("state") == "APPROVED"
               and (not r.get("commit_id") or r["commit_id"] == head) for r in reviews) if me else False


def _stamp(gh: GhClient, s: Step, *, dry_run: bool = False, sleep=time.sleep) -> tuple[bool, str, bool]:
    """(ok, message, merged). A stamp that failed partway — the approval
    posted, the merge refused — is picked up where it stopped on a re-run:
    an approval this login already posted at this head is not posted again."""
    ok, msg, detail = preflight(gh, s)
    if not ok:
        return False, f"preflight refused: {msg}", False
    head = (detail.get("head") or {}).get("sha") or s.expect_head
    me = norm_login(gh.me())
    skipped = []
    approval = s.args.get("body") or approval_body(s.author_type, "high", s.args.get("note", ""))
    if _already_approved(gh.reviews(s.pr), me, head):
        skipped.append("already approved at this head")
    else:
        gh.create_review(s.pr, "APPROVE", approval)
    tail = f" [{'; '.join(skipped)}]" if skipped else ""
    if not s.args.get("merge"):
        return True, "approved (not merged)" + tail, False
    if dry_run:
        tail += " [Sentinel wait skipped: no approval was posted]"
    else:
        ok, why = wait_for_sentinel(gh, head, sleep)
        if not ok:
            return False, f"approved, not merged: {why}" + tail, False
    gh.merge(s.pr, head, "squash")
    return True, "approved and squash-merged" + tail, True


def unanswered_blockers(review: dict) -> list[str]:
    """Blocking findings on the review with no answer recorded on the card.

    This is the bar `/pr-review` merges against, and it is deliberately not
    something --force reaches. A judge row's other gates (size, shape:infra, a
    human author) are an approver's call to make; an open 🚨 is the review
    still waiting on the author, and squash-merging past it destroys the
    only chance to hear from them. The author answers — a fix, or
    `@claude <why> #update-review` — and the approver's judgments never
    stand in for that.
    """
    return [i["id"] for i in review.get("items") or []
            if i.get("blocking") and not i.get("disposition")]


def refuse_merge_over_findings(n: int, open_ids: list[str]) -> str:
    """There is no flag that turns this off, deliberately. A finding the
    author won't answer goes back to them; a real emergency is
    `review:waived`, the Sentinel's logged break-glass."""
    return (f"#{n} has {len(open_ids)} unanswered blocking review finding(s): {', '.join(open_ids)}. "
            f"Merging would walk over the review, and --force does not cover this. "
            f"The author answers them (a fix, or `@claude <why> #update-review`): "
            f"`--request-changes {n}` sends it back, or `--ask-fix {n}` / `--close {n}` on a PR a workflow opened. "
            f"To approve without merging, `--stamp {n}:no-merge`.")


RESOLVABLE = ("fixed", "refuted", "accepted", "not-applicable")  # the approver's call is made; `deferred` is the author's
FINDING_ID_RE = re.compile(r"F\d+")


def ask_fix_items(pr: dict) -> list[dict]:
    """The open findings an `@claude fix …` mention should name.

    The review's own open rows: no disposition, and never a style or
    pre-existing one. Those two buckets are marked optional by the review
    itself, and a mention that asked for them would turn "take it or leave
    it" into a push."""
    review = pr.get("review") or {}
    items = review.get("items") or []
    out = [{"id": (i.get("id") or "").strip(), "summary": (i.get("summary") or "").strip()}
           for i in items
           if not i.get("disposition") and i.get("bucket") not in ("style", "pre-existing", "preexisting")]
    if review.get("surface") == "v3":
        # On a v3 card the ⚠️ rows live in the brief, not in `items`.
        disposed = {i["id"] for i in items if i.get("disposition")}
        seen = {o["id"] for o in out}
        out += [{"id": w["id"], "summary": (w.get("body") or "").strip()}
                for w in review.get("warning_rows") or []
                if w.get("id") and w["id"] not in disposed and w["id"] not in seen]
    return [o for o in out if o["id"]]


def _and_join(parts: list[str]) -> str:
    if len(parts) <= 1:
        return parts[0] if parts else ""
    if len(parts) == 2:
        return f"{parts[0]} and {parts[1]}"
    return ", ".join(parts[:-1]) + f" and {parts[-1]}"


def ask_fix_body(pr: dict, items: list[dict]) -> str:
    """`@claude fix F1 and F3 #update-review`, then what each id is.

    The ids go on the mention line because that is the instruction; the
    summaries follow it so a person scrolling the thread can read what was
    asked for without opening the card. One mention does both halves -- fix,
    then re-review -- which is what the pipeline's `#update-review` is for."""
    ids = _and_join([i["id"] for i in items])
    lines = [f"@claude fix {ids} #update-review", ""]
    for i in items:
        summary = " ".join((i["summary"] or "").split())
        lines.append(f"- **{i['id']}**" + (f" — {summary[:200]}{'…' if len(summary) > 200 else ''}" if summary else ""))
    return with_footer("\n".join(lines))


def _route(gh: GhClient, s: Step) -> tuple[bool, str]:
    ok, msg, _ = preflight_head(gh, s)
    if not ok:
        return False, f"preflight refused: {msg}"
    targets = [t.lstrip("@") for t in (s.args.get("targets") or [s.args["target"]])]
    users = [t for t in targets if "/" not in t]
    teams = [t.split("/", 1)[1] for t in targets if "/" in t]
    gh.request_reviewers(s.pr, users, teams)
    gh.comment(s.pr, s.args["comment"])
    return True, "review requested from " + ", ".join(f"@{t}" for t in targets)


def _run_key(run: dict) -> tuple:
    return (int(run.get("run_number") or 0), int(run.get("run_attempt") or 0), run.get("created_at") or "")


def failed_workflow_runs(runs: list[dict]) -> list[dict]:
    """The newest run of each workflow on a head, kept only when it concluded
    failure. A run a concurrency group cancelled sits beside the run that
    replaced it (collect.checks_rollup has the same problem), so an older
    failure under a newer success is not re-run."""
    newest: dict[str, dict] = {}
    for r in runs:
        key = r.get("path") or r.get("name") or str(r.get("workflow_id") or r.get("id"))
        if key not in newest or _run_key(r) >= _run_key(newest[key]):
            newest[key] = r
    return [r for r in newest.values() if r.get("status") == "completed" and (r.get("conclusion") or "") in collect.FAILED_CONCLUSIONS]


def _rerun_checks(gh: GhClient, s: Step) -> tuple[bool, str]:
    ok, msg, detail = preflight_head(gh, s)
    if not ok:
        return False, f"preflight refused: {msg}"
    head = (detail.get("head") or {}).get("sha") or s.expect_head
    failed = failed_workflow_runs(gh.workflow_runs(head))
    if not failed:
        return False, "no failed workflow run on the head — the red check is a commit status or an older run, and there is nothing to re-run"
    for r in failed:
        gh.rerun_failed_jobs(int(r["id"]))
    names = ", ".join((r.get("name") or r.get("path") or str(r.get("id"))) for r in failed)
    return True, f"re-ran the failed jobs of {len(failed)} workflow run(s): {names}"


def _request_changes(gh: GhClient, s: Step) -> tuple[bool, str]:
    ok, msg, _ = preflight_head(gh, s)
    if not ok:
        return False, f"preflight refused: {msg}"
    gh.create_review(s.pr, "REQUEST_CHANGES", s.args["body"])
    gh.add_labels(s.pr, ["needs-author-response"])
    return True, "changes requested; needs-author-response applied"


def _mention(gh: GhClient, s: Step) -> tuple[bool, str]:
    ok, msg, _ = preflight_head(gh, s)
    if not ok:
        return False, f"preflight refused: {msg}"
    gh.comment(s.pr, s.args["comment"])
    return True, {"refresh": "refresh requested",
                  "ask-fix": f"asked @claude to fix {len(s.args.get('items') or [])} finding(s) and refresh the review",
                  }.get(s.kind, "fresh review requested")


def _deploy(gh: GhClient, s: Step) -> tuple[bool, str]:
    ok, msg, _ = preflight_head(gh, s)
    if not ok:
        return False, f"preflight refused: {msg}"
    gh.dispatch_workflow(DEPLOY_WORKFLOW, s.branch)
    return True, f"dispatched {DEPLOY_WORKFLOW} @ {s.branch}"


def _branch_at_expected(git: Git, s: Step) -> tuple[bool, str]:
    """After the fetch: origin/<branch> must still be the head the plan saw,
    or the push would land on top of a commit nobody judged."""
    at = git.rev_parse(f"origin/{s.branch}")
    if s.expect_head and at != s.expect_head:
        return False, f"head-moved on origin/{s.branch}: planned {s.expect_head[:7]}, now {at[:7]} — re-collect and re-plan"
    return True, "ok"


def _unblock(gh: GhClient, git: Git, s: Step, *, dry_run: bool = False) -> tuple[bool, str]:
    if not s.branch:
        return False, "no head branch on the step"
    ok, msg, _ = preflight_head(gh, s)
    if not ok:
        return False, f"preflight refused: {msg}"
    if dry_run:
        return True, f"dry-run: would fetch, merge origin/master into origin/{s.branch} in a worktree, and push HEAD:{s.branch} (no git run)"
    git.fetch("master", s.branch)
    ok, msg = _branch_at_expected(git, s)
    if not ok:
        return False, msg
    wt = git.add_worktree(f"origin/{s.branch}")
    try:
        if wt.merge("origin/master"):
            wt.push(s.branch)
            return True, "merged origin/master into the head branch and pushed"
        conflicts = wt.conflicted_files()
        _report_unblock_conflict(gh, s, conflicts)
        return False, "conflicts need a human: " + ", ".join(conflicts[:8])
    finally:
        git.remove_worktree(wt)  # a conflicted or half-done merge goes with it


def unblock_conflict_body(head: str, base: str, conflicts: list[str]) -> str:
    """What act.py leaves on the PR when the base merge stops on conflicts.

    The files, and the head it was tried against, so the next board render
    can see that this conflict is still the current one rather than a
    settled one -- and so the approver who pressed the button finds out
    somewhere other than the terminal they have already closed."""
    files = "\n".join(f"- `{f}`" for f in conflicts[:20])
    more = f"\n- …and {len(conflicts) - 20} more" if len(conflicts) > 20 else ""
    return with_footer(
        f"{UNBLOCK_CONFLICT_MARKER}\n"
        f"Tried to merge `{base}` into this branch from `/pr-review` and stopped on conflicts, so nothing was "
        f"pushed. The merge is aborted, not half-applied — the branch is exactly as it was at `{head[:7]}`.\n\n"
        f"Conflicted file{'s' if len(conflicts) != 1 else ''}:\n\n{files}{more}\n\n"
        f"Resolving these needs someone who can say which side wins, so `/pr-review` will not offer the base "
        f"merge again while `{head[:7]}` is the head. Merge `{base}` in by hand, or push any commit that settles "
        f"it, and the button comes back.")


def _report_unblock_conflict(gh: GhClient, s: Step, conflicts: list[str]) -> None:
    """Best-effort: the conflict report must never turn a failed merge into a
    raised exception, because the merge failing is the thing worth telling."""
    if not conflicts:
        return
    body = unblock_conflict_body(s.expect_head, s.args.get("base") or "master", conflicts)
    try:
        if not _already_commented(gh.issue_comments(s.pr), norm_login(gh.me()), body):
            gh.comment(s.pr, body)
    except (GhError, OSError):
        pass


def _fix(gh: GhClient, git: Git, s: Step, *, dry_run: bool = False) -> tuple[bool, str]:
    ok, msg, _ = preflight_head(gh, s)
    if not ok:
        return False, f"preflight refused: {msg}"
    done = []
    if s.args.get("description"):
        body = s.args.get("body")
        if not body:
            return False, "no drafted description on the step"
        gh.update_pr(s.pr, body=body)
        done.append("description")
    planned = s.args.get("suggestions") or []
    if planned:
        live, skipped = live_suggestions(gh, s.pr, planned)
        note = f" (skipped {len(skipped)}: {'; '.join(skipped)})" if skipped else ""
        if dry_run:
            done.append(f"{len(live)} suggestion(s) in a worktree at origin/{s.branch}, pushed HEAD:{s.branch} (no git run){note}")
            return True, "dry-run: would have applied " + ", ".join(done)
        if live:
            git.fetch(s.branch)
            ok, msg = _branch_at_expected(git, s)
            if not ok:
                return False, msg
            wt = git.add_worktree(f"origin/{s.branch}")
            try:
                # Bottom-up per file, so applying one suggestion never shifts
                # the line numbers of the ones above it.
                for sg in sorted(live, key=lambda x: (x["path"], -int(x["start_line"]))):
                    apply_suggestion(wt.root, sg["path"], int(sg["start_line"]), int(sg["line"]), sg["replacement"])
                    wt.add(sg["path"])
                wt.commit(commit_message(f"Apply {len(live)} review suggestion(s)"))
                wt.push(s.branch)
            finally:
                git.remove_worktree(wt)  # a failed apply is discarded with the worktree, never left staged anywhere
            done.append(f"{len(live)} suggestion(s){note}")
        elif skipped:
            done.append(f"no suggestions{note}")
    return True, "applied " + ", ".join(done) if done else "nothing applied"


def _close(gh: GhClient, s: Step) -> tuple[bool, str]:
    ok, msg, _ = preflight_head(gh, s)
    if not ok:
        return False, f"preflight refused: {msg}"
    m = s.args.get("superseded_by")
    if not m:
        gh.comment(s.pr, s.args["comment"])
        gh.close_pr(s.pr)
        return True, "closed"
    gh.comment(s.pr, s.args["comment"])
    gh.comment(m, s.args["supersede_comment"])
    gh.close_pr(s.pr)
    return True, f"closed; superseded by #{m}"


def can_revise(pr: dict) -> bool:
    """Mirrors collect.can_revise over a queue row: only an agent bot reads a
    review and pushes a revision; a workflow-authored PR never will."""
    a = pr.get("author") or {}
    if "can_revise" in a:
        return bool(a["can_revise"])
    return a.get("type") != "bot"


def close_reason(pr: dict) -> str:
    """The closing comment for a generated PR: the judgments that made the
    call, in the author-facing voice, and what happens next."""
    body = "\n".join(ask_lines(pr)).strip()
    lead = "Closing this out: it was opened by a workflow run, so there is no author to pick up a review."
    tail = "The lane re-queues the page on its next run; these notes are here for whoever picks it up."
    return "\n\n".join(x for x in (lead, body, tail) if x)


def _render(s: Step, *, node: str = "node") -> tuple[bool, str]:
    pages = s.args.get("pages") or []
    if not pages:
        return False, "no preview pages on the row (no content/*.md changes, or the preview isn't built yet)"
    out_dir = SHOTS_DIR / str(s.pr)
    out_dir.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ)
    env.setdefault("NODE_PATH", "/opt/node22/lib/node_modules")
    shots = []
    for pg in pages:
        url = pg.get("preview_url")
        if not url:
            return False, "preview URL not posted yet (pulumi-bot's preview comment is missing)"
        slug = (pg.get("url") or "").strip("/").replace("/", "_") or "index"
        out = out_dir / f"{slug}.png"
        subprocess.run([node, str(_HERE / "screenshot.mjs"), str(out), url, "--full"], check=True, env=env,
                       capture_output=True, text=True)
        shots.append(str(out))
    return True, f"{len(shots)} screenshot(s) → {out_dir}"


def report(results: list[Result], *, writes: bool = False) -> str:
    """One line per step. A failed step also lists the writes that landed
    before it failed, so "✗ stamp #1" never hides an approval that went out;
    `writes=True` (dry-run) lists every write each step would have made."""
    lines = []
    for r in results:
        mark = "✓" if r.ok else "✗"
        lines.append(f"{mark} {r.step.kind:<8} #{r.step.pr}: {r.message}")
        if r.writes and (writes or not r.ok):
            label = "would" if writes else "landed"
            for w in r.writes:
                lines.append(f"    {label}: {w['method']} {w['path']}  {_body_head(w.get('body'))}")
    n_ok = sum(1 for r in results if r.ok)
    lines.append(f"{n_ok}/{len(results)} step(s) succeeded. Re-collect to refresh the board.")
    return "\n".join(lines) + "\n"


# ---- CLI ---------------------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--in", dest="inp", default=str(_REPO_ROOT / ".pr-review-queue.json"))
    ap.add_argument("--stamp", action="append", help="comma list of PR numbers, each optionally N:merge / N:no-merge (repeatable)")
    ap.add_argument("--route", action="append", help="N:@user or N:@org/team (repeatable; N alone uses the row's route action)")
    ap.add_argument("--request-changes", type=int, action="append", help="send the row's judgments back to the author as a changes-requested review")
    ap.add_argument("--chain", action="append", metavar="C1", help="stamp a cluster's first PR, then unblock the next")
    ap.add_argument("--unblock", type=int, action="append")
    ap.add_argument("--fix", type=int, action="append")
    ap.add_argument("--close", type=int, action="append", help="close N (repeatable)")
    ap.add_argument("--superseded-by", action="append", metavar="M | N:M",
                    help="M with exactly one --close, or N:M to say which close (repeatable)")
    ap.add_argument("--ask-fix", type=int, action="append", dest="ask_fix", metavar="N",
                    help="comment `@claude fix <ids> #update-review`: ask the PR-side agent to fix the row's open "
                         "findings and refresh the review, instead of running /address-review yourself")
    ap.add_argument("--refresh", type=int, action="append")
    ap.add_argument("--rerun", type=int, action="append", help="post `@claude <reason> #new-review`: a fresh review from scratch")
    ap.add_argument("--rerun-checks", type=int, action="append", help="re-run the failed jobs of the head's workflow runs")
    ap.add_argument("--reason", action="append", metavar="TEXT | N=TEXT",
                    help="for --refresh / --rerun: what changed; for --request-changes: an opening line; for --close: why. "
                         "N=TEXT scopes it to PR N; bare TEXT needs exactly one step that takes a reason")
    ap.add_argument("--render", type=int, action="append")
    ap.add_argument("--deploy", type=int, action="append")
    ap.add_argument("--merge-humans", action="store_true", help="squash-merge human-authored stamps too")
    ap.add_argument("--no-merge", action="store_true", help="approve only")
    ap.add_argument("--force", action="store_true", help="stamp a judge row (approve as-is); also sends a review back to a workflow author")
    ap.add_argument("--approve-note", help="one sentence appended to the approval body")
    ap.add_argument("--plan-out", default=str(_REPO_ROOT / ".pr-review-plan.json"))
    ap.add_argument("--execute", metavar="PLAN.json", help="run a plan written earlier")
    ap.add_argument("--dry-run", action="store_true", help="run the preflights and list every write without sending one; never runs git")
    ap.add_argument("--backend", default="auto", choices=("auto", "gh", "rest", "snapshot"))
    ap.add_argument("--snapshot-dir")
    ap.add_argument("--self-test", action="store_true")
    return ap


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.self_test:
        import test_act  # noqa: PLC0415 — the pytest file doubles as the harness
        return test_act.run_standalone()
    queue = json.loads(Path(args.inp).read_text()) if Path(args.inp).exists() else {}
    if args.execute:
        try:
            plan_ = Plan.from_json(json.loads(Path(args.execute).read_text()))
        except ActError as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 2
        gh = GhClient(plan_.repo, args.backend, snapshot_dir=args.snapshot_dir)
        results = execute(plan_, gh, queue=queue, dry_run=args.dry_run)
        sys.stdout.write(report(results, writes=args.dry_run))
        return 0 if all(r.ok for r in results) else 1
    try:
        plan_ = plan(queue, args)
    except ActError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    Path(args.plan_out).write_text(json.dumps(plan_.to_json(), indent=1) + "\n")
    sys.stdout.write(preview(plan_, queue))
    print(f"plan → {args.plan_out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
