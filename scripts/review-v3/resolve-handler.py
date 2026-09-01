#!/usr/bin/env python3
"""Deterministic handler for the `/resolve` comment command.

`/resolve` is the zero-model way an author answers a review finding — see
`resolve_command.py` for the grammar and `review_state.py` for the
REVIEW_STATE block it writes into. This module is the glue: given one PR
comment event, decide what to do and do it, entirely via `gh api` — no
model call, no AWS.

Dispatch, in order (mirrors the spec in the v3 design doc):

  1. `resolve_command.parse_commands` finds usage errors (bad syntax, unknown
     disposition, a note-required disposition with no note) -> post/replace
     the single `<!-- RESOLVE_ERRORS -->` reply. Exit 0 — a usage mistake is
     not a workflow failure.
  2. No commands, no errors -> prose-answer detection against the bot-owned
     author comment's known finding ids. At most one `<!-- RESOLVE_POINTER
     <actor> -->` reply per actor, ever, on a given PR.
  3. Commands present -> permission gate (PR author, or write/admin/maintain
     collaborator permission; an API failure fails CLOSED, never open).
  4. Apply: build the new disposition state, then merge it against a FRESH
     re-fetch of the author comment immediately before writing — the update
     lane's model step can run for ~10 minutes between fetch and write, and
     a `/resolve` landing in that window must not be lost (see
     review_state.py's module docstring for the full race). A batch may mix
     valid and out-of-range ids: the valid ones still apply (silent +1
     reaction), and an out-of-range id lands in the same `RESOLVE_ERRORS`
     reply used for usage errors — one home for "your /resolve didn't fully
     land," whether the cause was a typo or a stale id.

Structured for testability: `Gh` isolates every `gh api` subprocess call
behind small methods (list/get/create/delete/patch comments, add a reaction,
resolve the PR author, check collaborator permission); `handle()` is the
pure(-ish) core that takes any object satisfying that interface, so tests
substitute an in-memory `StubGh`. `--dry-run` uses the real `Gh` but records
every write into `.actions` instead of executing it, then prints that list —
reads still hit the live API, since deciding what WOULD happen requires the
real state.

Self-contained — run the smoke checks with `python3 resolve-handler.py --self-test`.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
import resolve_command  # noqa: E402
import review_state  # noqa: E402

AUTHOR_MARKER = "<!-- CLAUDE_REVIEW_AUTHOR -->"
BRIEF_MARKER = "<!-- CLAUDE_REVIEW_BRIEF -->"
ERRORS_MARKER = "<!-- RESOLVE_ERRORS -->"

# build-evidence.py owns the deterministic card renderers (header count,
# "Waiting on the author" block). Loaded lazily and best-effort: the state
# block is the record; the counts are display, and a missing renderer must
# never block a disposition from landing.
_BUILD_EVIDENCE = _HERE.parent.parent / ".claude" / "commands" / "docs-review" / "scripts" / "build-evidence.py"


def _load_build_evidence():
    import importlib.util
    if not _BUILD_EVIDENCE.exists():
        return None
    spec = importlib.util.spec_from_file_location("build_evidence", _BUILD_EVIDENCE)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["build_evidence"] = mod
    spec.loader.exec_module(mod)
    return mod


def refresh_cards(author_body: str, brief_body: str | None, state: dict) -> tuple[str, str | None]:
    """Recount the author header and the brief's Waiting block for the new
    dispositions. Returns the inputs unchanged when the renderer is
    unavailable or the card doesn't parse (legacy/minimal bodies)."""
    try:
        be = _load_build_evidence()
        if be is None:
            return author_body, brief_body
        return be.refresh_counts(author_body, brief_body, state)
    except Exception as exc:  # noqa: BLE001 — display refresh is best-effort
        print(f"resolve-handler: card refresh skipped: {exc}", file=sys.stderr)
        return author_body, brief_body
POINTER_MARKER_TMPL = "<!-- RESOLVE_POINTER {actor} -->"


BOT_LOGIN = "github-actions[bot]"
ALLOWED_PERMISSIONS = {"admin", "write", "maintain"}
USAGE = "`/resolve F<n> fixed|refuted|deferred|accepted|not-applicable[: note]`"
CORRUPT_STATE_MSG = (
    "The REVIEW_STATE block on the review comment is corrupt and can't be "
    "updated safely — nothing was changed. Ask a maintainer to regenerate "
    "the review."
)


class PermissionCheckFailed(Exception):
    """Raised by Gh.get_permission when the collaborator-permission API call fails.

    Callers must treat this as NO permission (fail closed) — see the
    permission gate in handle().
    """


# ---- GitHub I/O ---------------------------------------------------------


class Gh:
    """Thin wrapper over `gh api`, isolating subprocess calls for testability.

    Reads always hit the live API, dry-run or not — --dry-run only needs to
    suppress writes, not pretend the world is empty. Every write method
    checks self.dry_run and, when set, records the intended call into
    `.actions` instead of running it.
    """

    def __init__(self, repo: str, pr: int, dry_run: bool = False):
        self.repo = repo
        self.pr = pr
        self.dry_run = dry_run
        self.actions: list[dict] = []

    def _run(self, args: list[str], input_text: str | None = None) -> str:
        result = subprocess.run(
            ["gh", *args], input=input_text, text=True, capture_output=True, check=True,
        )
        return result.stdout

    def list_issue_comments(self) -> list[dict]:
        out = self._run(["api", "--paginate", f"repos/{self.repo}/issues/{self.pr}/comments"])
        return json.loads(out)

    def get_issue_comment(self, comment_id) -> dict:
        out = self._run(["api", f"repos/{self.repo}/issues/comments/{comment_id}"])
        return json.loads(out)

    def get_pr_author(self) -> str:
        out = self._run(["api", f"repos/{self.repo}/pulls/{self.pr}", "--jq", ".user.login"])
        return out.strip()

    def get_permission(self, actor: str) -> str:
        try:
            out = self._run(
                ["api", f"repos/{self.repo}/collaborators/{actor}/permission", "--jq", ".permission"]
            )
        except subprocess.CalledProcessError as exc:
            raise PermissionCheckFailed(str(exc)) from exc
        return out.strip()

    def create_issue_comment(self, body: str) -> str:
        if self.dry_run:
            fake_id = f"dryrun-{len(self.actions)}"
            self.actions.append({"action": "create_comment", "body": body, "id": fake_id})
            return fake_id
        # `-F body=@-` reads the value from stdin so the (untrusted) comment
        # text never has to survive shell interpolation.
        out = self._run(
            [
                "api", "-X", "POST", f"repos/{self.repo}/issues/{self.pr}/comments",
                "-F", "body=@-", "--jq", ".id",
            ],
            input_text=body,
        )
        return out.strip()

    def delete_issue_comment(self, comment_id) -> None:
        if self.dry_run:
            self.actions.append({"action": "delete_comment", "id": comment_id})
            return
        self._run(["api", "-X", "DELETE", f"repos/{self.repo}/issues/comments/{comment_id}"])

    def patch_issue_comment(self, comment_id, body: str) -> None:
        if self.dry_run:
            self.actions.append({"action": "patch_comment", "id": comment_id, "body": body})
            return
        self._run(
            ["api", "-X", "PATCH", f"repos/{self.repo}/issues/comments/{comment_id}", "-F", "body=@-"],
            input_text=body,
        )

    def add_reaction(self, comment_id, content: str = "+1") -> None:
        if self.dry_run:
            self.actions.append({"action": "add_reaction", "id": comment_id, "content": content})
            return
        self._run(
            [
                "api", "-X", "POST",
                f"repos/{self.repo}/issues/comments/{comment_id}/reactions",
                "-f", f"content={content}",
            ]
        )


# ---- pure-ish core --------------------------------------------------------


@dataclass
class HandleResult:
    exit_code: int
    outcome: str  # short tag for logging / tests, not a public contract


def find_marker_comment(comments: list[dict], marker: str) -> dict | None:
    for c in comments:
        if marker in (c.get("body") or ""):
            return c
    return None


def find_author_comment(comments: list[dict]) -> dict | None:
    for c in comments:
        user = c.get("user") or {}
        if AUTHOR_MARKER in (c.get("body") or "") and user.get("login") == BOT_LOGIN:
            return c
    return None


def build_errors_body(errors: list[str]) -> str:
    lines = [ERRORS_MARKER, "", "Couldn't apply `/resolve`:", ""]
    lines += [f"- {e}" for e in errors]
    lines += ["", f"Usage: {USAGE}"]
    return "\n".join(lines)


def post_or_replace(gh: Gh, comments: list[dict], marker: str, body: str) -> None:
    """Post `body` (which must carry `marker`), replacing any prior copy.

    Delete-then-create, mirroring how claude-triage.yml handles
    `<!-- TRIAGE_PROSE -->` — simpler than tracking edit history, and the
    marker means there's never more than one live copy either way.
    """
    existing = find_marker_comment(comments, marker)
    if existing is not None:
        gh.delete_issue_comment(existing["id"])
    gh.create_issue_comment(body)


def handle(pr: int, comment_id, actor: str, body: str, gh: Gh) -> HandleResult:
    parsed = resolve_command.parse_commands(body)

    # ---- 1. usage errors --------------------------------------------------
    if parsed.errors:
        comments = gh.list_issue_comments()
        post_or_replace(gh, comments, ERRORS_MARKER, build_errors_body(parsed.errors))
        return HandleResult(0, "errors")

    # ---- 2. prose-answer detection -----------------------------------------
    if not parsed.commands:
        comments = gh.list_issue_comments()
        author_comment = find_author_comment(comments)
        if author_comment is None:
            return HandleResult(0, "no-review")
        try:
            state = review_state.parse_state(author_comment["body"])
        except ValueError:
            # A corrupt block can't safely tell us known ids; say nothing
            # rather than guess. The commands path (below) is where a
            # corrupt block gets surfaced to the author.
            return HandleResult(0, "corrupt-state-prose-skip")
        state = state or review_state.empty_state()
        known_ids = {f"F{i}" for i in range(1, state["high_water"] + 1)}
        prose_hits = resolve_command.detect_prose_answer(body, known_ids)
        if not prose_hits:
            return HandleResult(0, "no-op")

        pointer_marker = POINTER_MARKER_TMPL.format(actor=actor)
        if find_marker_comment(comments, pointer_marker) is not None:
            return HandleResult(0, "pointer-already-sent")

        fid = prose_hits[0]
        pointer_body = (
            f"{pointer_marker}\n"
            f"Looks like an answer to {fid} — to make it count, reply "
            f"`@claude <your reasoning> #update-review` and the review will "
            f"re-adjudicate it."
        )
        gh.create_issue_comment(pointer_body)
        return HandleResult(0, "pointer-sent")

    # ---- 3. permission gate -------------------------------------------------
    is_author = actor == gh.get_pr_author()
    if not is_author:
        try:
            permission = gh.get_permission(actor)
        except PermissionCheckFailed:
            permission = None  # fail closed: an unreadable permission is no permission
        if permission not in ALLOWED_PERMISSIONS:
            gh.create_issue_comment(
                f"@{actor} — only the PR author or someone with write access to this "
                "repository can resolve findings on this PR."
            )
            return HandleResult(0, "permission-denied")

    # ---- 4. apply -----------------------------------------------------------
    comments = gh.list_issue_comments()
    author_comment = find_author_comment(comments)
    if author_comment is None:
        gh.create_issue_comment("No active review found on this PR yet — there's nothing to `/resolve`.")
        return HandleResult(0, "no-review")

    try:
        state = review_state.parse_state(author_comment["body"])
    except ValueError:
        gh.create_issue_comment(CORRUPT_STATE_MSG)
        return HandleResult(1, "corrupt-state")
    state = state or review_state.empty_state()
    high_water = state["high_water"]

    id_errors: list[str] = []
    targets: list[tuple[str, dict]] = []
    for cmd in parsed.commands:
        if cmd["target"] == "all":
            if high_water < 1:
                id_errors.append("`/resolve all` — no findings exist yet on this PR")
                continue
            # "all" means everything still OPEN. An id the author already
            # answered individually keeps that answer — the first live
            # battery had a bulk `accepted` silently overwrite a careful
            # individual `refuted` (newer-timestamp-wins is the RACE rule,
            # not license for a blanket command to erase specific answers).
            already = set(state.get("findings", {}))
            bulk = [
                (f"F{i}", cmd) for i in range(1, high_water + 1)
                if f"F{i}" not in already
            ]
            if not bulk:
                id_errors.append(
                    "`/resolve all` — every finding already has an answer; "
                    "re-resolve a specific id to change one"
                )
            targets.extend(bulk)
        else:
            n = int(cmd["target"][1:])
            if high_water < 1:
                id_errors.append(f"`{cmd['target']}` — no findings exist yet on this PR")
            elif n < 1 or n > high_water:
                id_errors.append(f"`{cmd['target']}` is out of range — valid ids are F1..F{high_water}")
            else:
                targets.append((cmd["target"], cmd))

    applied = False
    if targets:
        now = datetime.now(timezone.utc)
        new_state = state
        for fid, cmd in targets:
            new_state = review_state.set_disposition(
                new_state, fid, cmd["disposition"],
                actor=actor, note=cmd["note"], bulk=cmd["bulk"], now=now,
            )

        # Re-fetch immediately before writing — the lost-update race
        # review_state.py's docstring describes: the update lane can be
        # mid-flight for ~10 minutes between its own fetch and write.
        fresh_comment = gh.get_issue_comment(author_comment["id"])
        try:
            fresh_state = review_state.parse_state(fresh_comment["body"])
        except ValueError:
            gh.create_issue_comment(CORRUPT_STATE_MSG)
            return HandleResult(1, "corrupt-state-on-write")
        fresh_state = fresh_state or review_state.empty_state()

        merged = review_state.merge_states(fresh_state, new_state)
        new_body = review_state.replace_block(fresh_comment["body"], merged)
        brief_comment = find_marker_comment(comments, BRIEF_MARKER)
        brief_body = gh.get_issue_comment(brief_comment["id"])["body"] if brief_comment else None
        new_body, new_brief = refresh_cards(new_body, brief_body, merged)
        gh.patch_issue_comment(author_comment["id"], new_body)
        if brief_comment and new_brief is not None and new_brief != brief_body:
            gh.patch_issue_comment(brief_comment["id"], new_brief)
        gh.add_reaction(comment_id, "+1")
        applied = True

    if id_errors:
        post_or_replace(gh, comments, ERRORS_MARKER, build_errors_body(id_errors))
        return HandleResult(1, "partial" if applied else "id-errors")

    return HandleResult(0, "applied")


# ---- self-test ------------------------------------------------------------


class StubGh:
    """In-memory stand-in for Gh, sharing its method surface exactly.

    `comments` is keyed by an integer id the caller assigns. `_fresh_override`
    lets a test simulate the lost-update race: a value stashed there is
    served exactly once by get_issue_comment() (and then cleared), standing
    in for a concurrent write that happened between list_issue_comments()
    and the re-fetch — no threads required.
    """

    def __init__(self, pr_author: str = "alice", permissions: dict | None = None, dry_run: bool = False):
        self.pr = 42
        self.dry_run = dry_run
        self._pr_author = pr_author
        self._permissions = permissions or {}
        self._next_id = 1000
        self.comments: dict[int, dict] = {}
        self._fresh_override: dict[int, str] = {}
        self.actions: list[dict] = []
        self.reactions: list[tuple] = []

    def seed_comment(self, body: str, login: str = BOT_LOGIN, user_type: str = "Bot") -> int:
        cid = self._next_id
        self._next_id += 1
        self.comments[cid] = {"id": cid, "body": body, "user": {"login": login, "type": user_type}}
        return cid

    def list_issue_comments(self) -> list[dict]:
        return [dict(c) for c in self.comments.values()]

    def get_issue_comment(self, comment_id) -> dict:
        if comment_id in self._fresh_override:
            body = self._fresh_override.pop(comment_id)
            self.comments[comment_id]["body"] = body
        return dict(self.comments[comment_id])

    def get_pr_author(self) -> str:
        return self._pr_author

    def get_permission(self, actor: str) -> str:
        val = self._permissions.get(actor, "none")
        if val == "ERROR":
            raise PermissionCheckFailed("stub API failure")
        return val

    def create_issue_comment(self, body: str) -> int:
        cid = self._next_id
        self._next_id += 1
        if self.dry_run:
            self.actions.append({"action": "create_comment", "body": body, "id": cid})
            return cid
        self.comments[cid] = {"id": cid, "body": body, "user": {"login": BOT_LOGIN, "type": "Bot"}}
        return cid

    def delete_issue_comment(self, comment_id) -> None:
        if self.dry_run:
            self.actions.append({"action": "delete_comment", "id": comment_id})
            return
        self.comments.pop(comment_id, None)

    def patch_issue_comment(self, comment_id, body: str) -> None:
        if self.dry_run:
            self.actions.append({"action": "patch_comment", "id": comment_id, "body": body})
            return
        self.comments[comment_id]["body"] = body

    def add_reaction(self, comment_id, content: str = "+1") -> None:
        if self.dry_run:
            self.actions.append({"action": "add_reaction", "id": comment_id, "content": content})
            return
        self.reactions.append((comment_id, content))


def _author_body(high_water: int, findings: dict | None = None) -> str:
    state = {"schema": 1, "high_water": high_water, "findings": findings or {}}
    return "## Review\n" + AUTHOR_MARKER + "\n" + review_state.serialize_block(state) + "\n"


def _self_test() -> int:
    failures = []

    def check(name, cond):
        if cond:
            print(f"ok: {name}")
        else:
            failures.append(name)
            print(f"FAIL: {name}", file=sys.stderr)

    # -- valid single command applied + reaction -----------------------------
    gh = StubGh(pr_author="alice")
    author_id = gh.seed_comment(_author_body(3))
    r = handle(42, 9001, "alice", "/resolve F2 refuted: not actually a bug", gh)
    check("valid command exits 0", r.exit_code == 0 and r.outcome == "applied")
    state = review_state.parse_state(gh.comments[author_id]["body"])
    check("F2 recorded", state["findings"]["F2"]["disposition"] == "refuted")
    check("actor recorded", state["findings"]["F2"]["actor"] == "alice")
    check("reaction added", gh.reactions == [(9001, "+1")])

    # -- counts follow dispositions: header + brief Waiting block ------------
    fx = _HERE.parent.parent / ".claude" / "commands" / "docs-review" / "scripts" / "testdata"
    if (fx / "v3-fixture-author.md").exists():
        gh = StubGh(pr_author="alice")
        fx_author = (fx / "v3-fixture-author.md").read_text()
        fx_brief = (fx / "v3-fixture-brief.md").read_text()
        author_id = gh.seed_comment(fx_author)
        brief_id = gh.seed_comment(fx_brief)
        r = handle(42, 9010, "alice", "/resolve F3 accepted: internal figure, shipping as-is", gh)
        check("fixture resolve applies", r.exit_code == 0 and r.outcome == "applied")
        check("author header recounted", "— 2 items block merge" in gh.comments[author_id]["body"])
        check("brief Waiting block shows the answer",
              "✋ accepted as-is by the author" in gh.comments[brief_id]["body"]
              and "(1 more is answered — see State)" in gh.comments[brief_id]["body"])

    # -- bulk all with note applies to F1..high_water, bulk flags ------------
    gh = StubGh(pr_author="alice")
    author_id = gh.seed_comment(_author_body(3))
    r = handle(42, 9002, "alice", "/resolve all accepted: ship it", gh)
    check("bulk all exits 0", r.exit_code == 0)
    state = review_state.parse_state(gh.comments[author_id]["body"])
    check("bulk covers F1..F3", set(state["findings"]) == {"F1", "F2", "F3"})
    check("bulk entries flagged", all(e["bulk"] for e in state["findings"].values()))
    check("bulk disposition applied", all(e["disposition"] == "accepted" for e in state["findings"].values()))

    # -- malformed command -> RESOLVE_ERRORS reply, state untouched ----------
    gh = StubGh(pr_author="alice")
    author_id = gh.seed_comment(_author_body(3))
    original_body = gh.comments[author_id]["body"]
    r = handle(42, 9003, "alice", "/resolve F2 wontfix: nah", gh)
    check("malformed command exits 0", r.exit_code == 0 and r.outcome == "errors")
    errors_comment = find_marker_comment(gh.list_issue_comments(), ERRORS_MARKER)
    check("RESOLVE_ERRORS comment posted", errors_comment is not None)
    check("state untouched by malformed command", gh.comments[author_id]["body"] == original_body)

    # -- id > high_water -> error naming range, state untouched ---------------
    gh = StubGh(pr_author="alice")
    author_id = gh.seed_comment(_author_body(2))
    original_body = gh.comments[author_id]["body"]
    r = handle(42, 9004, "alice", "/resolve F9 fixed", gh)
    check("out-of-range id exits 1", r.exit_code == 1)
    errors_comment = find_marker_comment(gh.list_issue_comments(), ERRORS_MARKER)
    check("out-of-range error names the range", "F1..F2" in errors_comment["body"])
    check("state untouched by out-of-range id", gh.comments[author_id]["body"] == original_body)
    check("no reaction on full rejection", gh.reactions == [])

    # -- prose answer -> pointer once; second prose by same actor -> no repeat
    gh = StubGh(pr_author="alice")
    gh.seed_comment(_author_body(3))
    r1 = handle(42, 9005, "bob", "I think F2 is wrong because the docs say otherwise", gh)
    check("first prose hit posts a pointer", r1.outcome == "pointer-sent")
    pointer_marker = POINTER_MARKER_TMPL.format(actor="bob")
    first_count = sum(1 for c in gh.list_issue_comments() if pointer_marker in c["body"])
    check("exactly one pointer posted", first_count == 1)
    r2 = handle(42, 9006, "bob", "actually F2 is still wrong, see above", gh)
    check("second prose by same actor is a no-op", r2.outcome == "pointer-already-sent")
    second_count = sum(1 for c in gh.list_issue_comments() if pointer_marker in c["body"])
    check("still exactly one pointer for bob", second_count == 1)

    # -- different actor gets their own pointer -------------------------------
    r3 = handle(42, 9007, "carol", "F2 looks wrong to me too", gh)
    check("a different actor gets their own pointer", r3.outcome == "pointer-sent")
    carol_marker = POINTER_MARKER_TMPL.format(actor="carol")
    check("carol's pointer exists", find_marker_comment(gh.list_issue_comments(), carol_marker) is not None)
    check("bob's pointer count unaffected", sum(1 for c in gh.list_issue_comments() if pointer_marker in c["body"]) == 1)

    # -- non-author without write -> refused, state untouched -----------------
    gh = StubGh(pr_author="alice", permissions={"mallory": "read"})
    author_id = gh.seed_comment(_author_body(3))
    original_body = gh.comments[author_id]["body"]
    r = handle(42, 9008, "mallory", "/resolve F1 fixed", gh)
    check("insufficient permission refused", r.outcome == "permission-denied")
    check("refusal does not touch state", gh.comments[author_id]["body"] == original_body)
    check("no reaction on refusal", gh.reactions == [])

    # -- author without write (external contributor) -> allowed ---------------
    gh = StubGh(pr_author="dana", permissions={})  # dana has no listed permission at all
    author_id = gh.seed_comment(_author_body(3))
    r = handle(42, 9009, "dana", "/resolve F1 fixed", gh)
    check("PR author allowed even with no write access", r.exit_code == 0 and r.outcome == "applied")

    # -- API failure on permission check fails closed --------------------------
    gh = StubGh(pr_author="alice", permissions={"mallory": "ERROR"})
    author_id = gh.seed_comment(_author_body(3))
    r = handle(42, 9010, "mallory", "/resolve F1 fixed", gh)
    check("permission API failure fails closed", r.outcome == "permission-denied")

    # -- corrupt REVIEW_STATE -> exit 1, reply, no PATCH -----------------------
    gh = StubGh(pr_author="alice")
    author_id = gh.seed_comment("## Review\n" + AUTHOR_MARKER + "\n<!-- REVIEW_STATE {broken -->\n")
    original_body = gh.comments[author_id]["body"]
    r = handle(42, 9011, "alice", "/resolve F1 fixed", gh)
    check("corrupt state exits 1", r.exit_code == 1 and r.outcome == "corrupt-state")
    check("corrupt state comment not patched", gh.comments[author_id]["body"] == original_body)
    check("no reaction on corrupt state", gh.reactions == [])

    # -- race: fresh fetch has newer F2, ours has F3 -> both survive ----------
    gh = StubGh(pr_author="alice")
    author_id = gh.seed_comment(_author_body(3))
    concurrent_state = review_state.set_disposition(
        review_state.parse_state(gh.comments[author_id]["body"]),
        "F2", "fixed", actor="update-lane",
        now=datetime(2026, 1, 1, tzinfo=timezone.utc),
    )
    concurrent_body = review_state.replace_block(gh.comments[author_id]["body"], concurrent_state)
    gh._fresh_override[author_id] = concurrent_body
    r = handle(42, 9012, "alice", "/resolve F3 refuted: not applicable here", gh)
    check("race scenario applies", r.exit_code == 0)
    final_state = review_state.parse_state(gh.comments[author_id]["body"])
    check("F2 (concurrent) survives", final_state["findings"]["F2"]["disposition"] == "fixed")
    check("F3 (ours) survives", final_state["findings"]["F3"]["disposition"] == "refuted")

    # -- --dry-run writes nothing -----------------------------------------------
    gh = StubGh(pr_author="alice", dry_run=True)
    author_id = gh.seed_comment(_author_body(3))
    original_body = gh.comments[author_id]["body"]
    r = handle(42, 9013, "alice", "/resolve F1 fixed", gh)
    check("dry-run still reports success", r.exit_code == 0)
    check("dry-run does not mutate the comment store", gh.comments[author_id]["body"] == original_body)
    check("dry-run records the intended patch", any(a["action"] == "patch_comment" for a in gh.actions))
    check("dry-run records the intended reaction", any(a["action"] == "add_reaction" for a in gh.actions))
    check("dry-run leaves no real reaction", gh.reactions == [])

    if failures:
        print(f"\n{len(failures)} failure(s)", file=sys.stderr)
        return 1
    print("\nall resolve-handler self-tests passed")
    return 0


# ---- CLI --------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--repo", help="owner/name")
    parser.add_argument("--pr", type=int)
    parser.add_argument("--comment-id")
    parser.add_argument("--comment-body-file")
    parser.add_argument("--actor", help="the commenting GitHub login")
    parser.add_argument("--dry-run", action="store_true", help="print intended actions as JSON, write nothing")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args(argv)

    if args.self_test:
        return _self_test()

    required = {
        "--repo": args.repo,
        "--pr": args.pr,
        "--comment-id": args.comment_id,
        "--comment-body-file": args.comment_body_file,
        "--actor": args.actor,
    }
    missing = [name for name, value in required.items() if value in (None, "")]
    if missing:
        parser.error(f"missing required arguments: {', '.join(missing)}")

    body = Path(args.comment_body_file).read_text()
    gh = Gh(args.repo, args.pr, dry_run=args.dry_run)
    result = handle(args.pr, args.comment_id, args.actor, body, gh)

    if args.dry_run:
        print(json.dumps({"outcome": result.outcome, "actions": gh.actions}, indent=2))
    else:
        print(f"resolve-handler: outcome={result.outcome}")

    return result.exit_code


if __name__ == "__main__":
    sys.exit(main())
