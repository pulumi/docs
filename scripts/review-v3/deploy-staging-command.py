#!/usr/bin/env python3
"""Decide what a `/deploy-staging` PR comment does, and word the bot's reply.

`/deploy-staging` is how a person asks for the pulumi-test.io deploy that
Sentinel gate G4 verifies, when the auto lane (`staging-deploy-auto.yml`)
didn't produce one: its dispatch failed, or the PR predates it. The gate
used to tell people to dispatch "Build and deploy testing" by hand, which
sits one click from the PRODUCTION "Build and deploy" in the Actions
sidebar, and on pulumi/docs#22524 someone dispatched production at an
unmerged branch. A comment can only ever reach staging.

`staging-deploy-command.yml` runs this from the default branch, after the
shared command gate has decided the comment carries a live command. This
script reads everything else from the API — the PR's CURRENT head (never a
SHA from the event), the commenter's role, the staging workflow's state, and
the head's existing deploy evidence — and decides one of:

  deploy   dispatch `staging-deploy.sh` at the head branch, exactly as the
           auto lane does;
  reply    don't, and say why: not a PR, no write access, closed, a fork,
           staging deploys turned off, this head already deployed, or a
           deploy of it already running.

Checks run in that order, so the cheapest refusal that applies is the one a
person sees, and nobody without write access learns anything about the PR's
deploy state.

Failure policy. A read that decides WHETHER this is allowed (the PR, the
commenter's role) fails closed: no deploy, and a reply that says the check
couldn't be made. A read that only decides whether a deploy is REDUNDANT
(statuses, run history, workflow state) fails open: the person asked, and a
redundant staging deploy costs a few minutes of a shared stack, which is the
same trade the Sentinel's own G4 copy makes ("the command is safe to
repeat").

NO PR CODE, EVER. Every fact comes from `gh api` as data; this script reads
no working tree and runs nothing from the PR. It never dispatches anything
itself either: the workflow calls `staging-deploy.sh`, whose only dispatch
target is `STAGING_WORKFLOW_FILE`.

Entry points:

  plan     --repo R --pr N --commenter LOGIN --reply-out FILE
           Prints `action=deploy|reply`, `reason=<key>`, `head_sha`,
           `head_ref` in GITHUB_OUTPUT form; writes the reply for `reply`.
  started  --repo R --sha SHA --commenter LOGIN [--run-url URL] --reply-out FILE
           Writes the "deploy started" reply (the run link, or the
           workflow's runs page when the run couldn't be located).
  failed   --repo R --sha SHA --commenter LOGIN --detail TEXT --job-url URL --reply-out FILE
           Writes the "couldn't start it" reply.
  --self-test

Exit status is 0 for every decision; only a usage error is non-zero.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass

# The ONLY workflow a `/deploy-staging` may lead to. The production deploy
# is `build-and-deploy.yml`; `test_deploy_staging_command.py` pins that
# `staging-deploy.sh` dispatches this file and nothing else, and that these
# constants match the Sentinel's.
STAGING_WORKFLOW_FILE = "testing-build-and-deploy.yml"
PRODUCTION_WORKFLOW_FILE = "build-and-deploy.yml"
STAGING_STATUS_CONTEXT = "staging/pulumi-test-io"
# Whose green status counts as evidence, as in sentinel.STAGING_STATUS_WRITERS:
# anyone with push access can write a commit status.
STAGING_STATUS_WRITERS = frozenset({"github-actions[bot]", "pulumi-bot"})
WRITE_ROLES = frozenset({"admin", "maintain", "write"})
IN_FLIGHT = frozenset({"queued", "in_progress", "waiting", "requested", "pending"})
REPLY_MARKER = "<!-- DEPLOY_STAGING_REPLY -->"

assert STAGING_WORKFLOW_FILE != PRODUCTION_WORKFLOW_FILE

_SHA_RE = re.compile(r"^[0-9a-f]{40}$")
# A ref reaches GITHUB_OUTPUT and `gh` argv. git already forbids control
# characters and spaces in a ref; refuse anything that slipped past that
# rather than reason about what it would do downstream.
_SAFE_REF_RE = re.compile(r"^[^\x00-\x20\x7f]+$")


@dataclass
class Decision:
    action: str          # deploy | reply
    reason: str          # a stable key, for logs and tests
    reply: str = ""
    head_sha: str = ""
    head_ref: str = ""


def _who(commenter: str) -> str:
    return f"@{commenter} — " if commenter else ""


def _say(commenter: str, text: str) -> str:
    return f"{REPLY_MARKER}\n🤖 {_who(commenter)}{text}"


def runs_page(repo: str) -> str:
    return f"https://github.com/{repo}/actions/workflows/{STAGING_WORKFLOW_FILE}"


def role_of(permission: dict | None) -> str:
    """The commenter's repository role. `role_name` distinguishes maintain
    and triage; the legacy `permission` field folds them into write/read."""
    if not permission:
        return "none"
    return str(permission.get("role_name") or permission.get("permission") or "none").lower()


def decide(
    *,
    repo: str,
    commenter: str,
    pr: dict | None,
    pr_error: str = "",
    permission: dict | None,
    permission_error: str = "",
    workflow_state: str = "",
    statuses: list[dict] | None = None,
    runs: list[dict] | None = None,
) -> Decision:
    """Pure: everything the workflow read, in; what to do and say, out."""
    if pr_error == "not_found" or (pr is not None and not pr.get("head")):
        return Decision("reply", "not_a_pr", _say(
            commenter, "this isn't a pull request, so there's nothing to deploy to staging."))
    if pr_error or pr is None:
        return Decision("reply", "pr_unreadable", _say(
            commenter, "couldn't read this PR, so no staging deploy started. Try again in a minute."))
    if permission_error:
        return Decision("reply", "permission_unreadable", _say(
            commenter, "couldn't confirm you have write access, so no staging deploy started. "
            "Try again in a minute."))
    role = role_of(permission)
    if role not in WRITE_ROLES:
        return Decision("reply", "no_write_access", _say(
            commenter, "starting a staging deploy needs write access to this repository, so "
            "nothing ran. Ask someone with write access to post the command."))
    if pr.get("state") != "open" or pr.get("merged"):
        return Decision("reply", "closed", _say(
            commenter, "this PR is closed, so no staging deploy started."))

    head = pr.get("head") or {}
    head_repo = (head.get("repo") or {}).get("full_name") or ""
    if head_repo != repo:
        return Decision("reply", "fork", _say(
            commenter, "this PR's branch lives in a fork, and fork code isn't deployed to the "
            "shared staging stack from a comment. Ask in `#docs` for a tools-team deploy."))
    sha = str(head.get("sha") or "")
    ref = str(head.get("ref") or "")
    if not _SHA_RE.match(sha) or not _SAFE_REF_RE.match(ref):
        return Decision("reply", "pr_unreadable", _say(
            commenter, "couldn't read this PR's head, so no staging deploy started."))
    sha7 = sha[:7]

    if workflow_state and workflow_state != "active":
        return Decision("reply", "disabled", _say(
            commenter, f"staging deploys are turned off ([`{STAGING_WORKFLOW_FILE}`]"
            f"({runs_page(repo)}) is `{workflow_state}`), so none can start. Ask in `#docs`; "
            "turning it back on needs a repo admin."), sha, ref)

    for s in statuses or []:
        if (s.get("context") == STAGING_STATUS_CONTEXT and s.get("state") == "success"
                and ((s.get("creator") or {}).get("login") or "") in STAGING_STATUS_WRITERS):
            link = s.get("target_url") or runs_page(repo)
            return Decision("reply", "already_deployed", _say(
                commenter, f"`{sha7}` already has a successful staging deploy ([details]({link})), "
                "so nothing new started."), sha, ref)
    for r in runs or []:
        if r.get("head_sha") not in (None, sha):
            continue
        if r.get("status") == "completed" and r.get("conclusion") == "success":
            return Decision("reply", "already_deployed", _say(
                commenter, f"`{sha7}` already has a successful staging deploy "
                f"([run {r.get('id')}]({r.get('html_url') or runs_page(repo)})), "
                "so nothing new started."), sha, ref)
    for r in runs or []:
        if r.get("head_sha") not in (None, sha):
            continue
        if r.get("status") in IN_FLIGHT:
            return Decision("reply", "already_running", _say(
                commenter, f"a staging deploy of `{sha7}` is already running "
                f"([run {r.get('id')}]({r.get('html_url') or runs_page(repo)})), "
                "so nothing new started."), sha, ref)

    return Decision("deploy", "deploy", "", sha, ref)


def render_started(repo: str, sha: str, commenter: str, run_url: str = "") -> str:
    link = run_url or runs_page(repo)
    return _say(commenter, f"Staging deploy started for `{sha[:7]}`: {link}")


def render_failed(repo: str, sha: str, commenter: str, detail: str, job_url: str) -> str:
    detail = (detail or "the dispatch failed").strip().rstrip(".")
    return _say(commenter, f"couldn't start a staging deploy for `{sha[:7]}`: {detail}. "
                f"[Job log]({job_url})")


# ---- API reads ------------------------------------------------------------

def _gh_api(path: str) -> tuple[object | None, str]:
    """`gh api` as (json, error). error is "not_found" for a 404."""
    p = subprocess.run(["gh", "api", path], capture_output=True, text=True)
    if p.returncode != 0:
        msg = (p.stderr or p.stdout or "").strip()
        print(f"::warning::gh api {path}: {msg[:300]}", file=sys.stderr)
        return None, "not_found" if "404" in msg or "Not Found" in msg else (msg or "error")
    try:
        return json.loads(p.stdout or "null"), ""
    except json.JSONDecodeError as exc:
        return None, f"bad json: {exc}"


def gather_and_decide(repo: str, pr_number: str, commenter: str) -> Decision:
    pr, pr_err = _gh_api(f"repos/{repo}/pulls/{pr_number}")
    perm: object | None = None
    perm_err = ""
    if not pr_err:
        perm, perm_err = _gh_api(f"repos/{repo}/collaborators/{commenter}/permission")
        if perm_err == "not_found":  # not a collaborator at all
            perm, perm_err = {"permission": "none"}, ""
    early = decide(repo=repo, commenter=commenter, pr=pr if isinstance(pr, dict) else None,
                   pr_error=pr_err, permission=perm if isinstance(perm, dict) else None,
                   permission_error=perm_err)
    if early.action == "reply" or not early.head_sha:
        return early

    sha = early.head_sha
    wf, _ = _gh_api(f"repos/{repo}/actions/workflows/{STAGING_WORKFLOW_FILE}")
    statuses, _ = _gh_api(f"repos/{repo}/commits/{sha}/statuses?per_page=100")
    runs, _ = _gh_api(f"repos/{repo}/actions/workflows/{STAGING_WORKFLOW_FILE}/runs"
                      f"?head_sha={sha}&per_page=100")
    return decide(
        repo=repo, commenter=commenter, pr=pr, permission=perm,
        workflow_state=str((wf or {}).get("state") or "") if isinstance(wf, dict) else "",
        statuses=statuses if isinstance(statuses, list) else [],
        runs=(runs or {}).get("workflow_runs") or [] if isinstance(runs, dict) else [],
    )


# ---- CLI ------------------------------------------------------------------

def _write(path: str, text: str) -> None:
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text + "\n")


def _cmd_plan(args: argparse.Namespace) -> int:
    if not re.fullmatch(r"[0-9]+", args.pr or ""):
        print("::error::--pr must be numeric", file=sys.stderr)
        return 2
    d = gather_and_decide(args.repo, args.pr, args.commenter)
    if d.reply:
        _write(args.reply_out, d.reply)
    print(f"action={d.action}")
    print(f"reason={d.reason}")
    print(f"head_sha={d.head_sha}")
    print(f"head_ref={d.head_ref}")
    return 0


def _self_test() -> int:
    failures = 0

    def check(name: str, cond: bool) -> None:
        nonlocal failures
        print(f"  {'ok ' if cond else 'FAIL'} {name}")
        if not cond:
            failures += 1

    R = "pulumi/docs"
    SHA = "a" * 40
    pr = {"state": "open", "merged": False,
          "head": {"sha": SHA, "ref": "me/infra", "repo": {"full_name": R}}}
    w = {"role_name": "write", "permission": "write"}

    def d(**kw):
        base = dict(repo=R, commenter="alice", pr=pr, permission=w, workflow_state="active",
                    statuses=[], runs=[])
        base.update(kw)
        return decide(**base)

    check("a writer on a fresh head deploys", d().action == "deploy")
    check("the deploy carries the API head", (d().head_sha, d().head_ref) == (SHA, "me/infra"))
    check("maintain may deploy", d(permission={"role_name": "maintain", "permission": "write"}).action == "deploy")
    check("admin may deploy", d(permission={"role_name": "admin"}).action == "deploy")
    check("triage may not", d(permission={"role_name": "triage", "permission": "read"}).reason == "no_write_access")
    check("read may not", d(permission={"permission": "read"}).reason == "no_write_access")
    check("no collaborator record may not", d(permission=None).reason == "no_write_access")
    check("unreadable role fails closed", d(permission_error="boom").reason == "permission_unreadable")
    check("not a PR", d(pr=None, pr_error="not_found").reason == "not_a_pr")
    check("unreadable PR fails closed", d(pr=None, pr_error="503").reason == "pr_unreadable")
    check("closed PR", d(pr=dict(pr, state="closed")).reason == "closed")
    check("merged PR", d(pr=dict(pr, merged=True)).reason == "closed")
    fork = dict(pr, head=dict(pr["head"], repo={"full_name": "someone/docs"}))
    check("fork PR", d(pr=fork).reason == "fork")
    check("deleted fork PR", d(pr=dict(pr, head=dict(pr["head"], repo=None))).reason == "fork")
    check("a reader learns nothing about a fork", d(pr=fork, permission={"permission": "read"}).reason
          == "no_write_access")
    check("disabled workflow", d(workflow_state="disabled_manually").reason == "disabled")
    check("unreadable workflow state still deploys", d(workflow_state="").action == "deploy")
    green = {"context": STAGING_STATUS_CONTEXT, "state": "success",
             "creator": {"login": "github-actions[bot]"}, "target_url": "https://x/1"}
    check("trusted green status skips", d(statuses=[green]).reason == "already_deployed")
    check("untrusted green status does not", d(statuses=[dict(green, creator={"login": "mallory"})]).action
          == "deploy")
    check("a red status does not", d(statuses=[dict(green, state="error")]).action == "deploy")
    ok_run = {"id": 7, "head_sha": SHA, "status": "completed", "conclusion": "success", "html_url": "https://x/7"}
    check("a successful run skips", d(runs=[ok_run]).reason == "already_deployed")
    check("a failed run is retried", d(runs=[dict(ok_run, conclusion="failure")]).action == "deploy")
    check("a running deploy skips", d(runs=[dict(ok_run, status="in_progress", conclusion=None)]).reason
          == "already_running")
    check("another head's run is ignored", d(runs=[dict(ok_run, head_sha="b" * 40)]).action == "deploy")
    check("a ref with a newline is refused",
          d(pr=dict(pr, head=dict(pr["head"], ref="x\ny"))).action == "reply")
    check("a short sha is refused", d(pr=dict(pr, head=dict(pr["head"], sha="abc"))).action == "reply")
    started = render_started(R, SHA, "alice", "https://github.com/pulumi/docs/actions/runs/9")
    check("started reply names sha7 and the run",
          "Staging deploy started for `aaaaaaa`: https://github.com/pulumi/docs/actions/runs/9" in started)
    check("started reply falls back to the runs page", runs_page(R) in render_started(R, SHA, "alice"))
    every = [d(**kw).reply for kw in (
        {"permission": None}, {"pr": fork}, {"workflow_state": "disabled_manually"},
        {"statuses": [green]}, {"pr": None, "pr_error": "not_found"})] + [started]
    check("every reply starts with the marker", all(r.startswith(REPLY_MARKER) for r in every))
    check("no reply carries a runnable command", not any(
        re.search(r"^[ \t]{0,3}/[a-z]", r, re.M) for r in every))
    check("no reply names production", not any(PRODUCTION_WORKFLOW_FILE in r.replace(STAGING_WORKFLOW_FILE, "")
                                               for r in every))
    print("deploy-staging-command self-test:", "PASS" if failures == 0 else f"{failures} FAILED")
    return 1 if failures else 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--self-test", action="store_true")
    sub = parser.add_subparsers(dest="cmd")

    pl = sub.add_parser("plan", help="decide what a /deploy-staging comment does")
    pl.add_argument("--repo", required=True)
    pl.add_argument("--pr", required=True)
    pl.add_argument("--commenter", required=True)
    pl.add_argument("--reply-out", required=True)

    st = sub.add_parser("started", help="write the 'deploy started' reply")
    st.add_argument("--repo", required=True)
    st.add_argument("--sha", required=True)
    st.add_argument("--commenter", default="")
    st.add_argument("--run-url", default="")
    st.add_argument("--reply-out", required=True)

    fa = sub.add_parser("failed", help="write the 'could not start it' reply")
    fa.add_argument("--repo", required=True)
    fa.add_argument("--sha", required=True)
    fa.add_argument("--commenter", default="")
    fa.add_argument("--detail", default="")
    fa.add_argument("--job-url", required=True)
    fa.add_argument("--reply-out", required=True)

    args = parser.parse_args(argv)
    if args.self_test:
        return _self_test()
    if args.cmd == "plan":
        return _cmd_plan(args)
    if args.cmd == "started":
        _write(args.reply_out, render_started(args.repo, args.sha, args.commenter, args.run_url))
        return 0
    if args.cmd == "failed":
        _write(args.reply_out, render_failed(args.repo, args.sha, args.commenter, args.detail, args.job_url))
        return 0
    parser.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
