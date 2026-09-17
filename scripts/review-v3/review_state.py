#!/usr/bin/env python3
"""Shared parser/serializer/merger for the REVIEW_STATE block.

REVIEW_STATE is the disposition source of truth for the v3 review workflow: a
single-line HTML comment embedded in the bot-owned author-facing pinned
comment, carrying every finding's answer (fixed / refuted / deferred /
accepted / not-applicable / author-accepted). It lives on the PR — not in
S3 — because the Sentinel must read it uncredentialed, from fork PRs,
atomically with the findings it answers; the credentialed record job
mirrors it one-way into `pr-review/<pr>/latest.json` for telemetry.

`author-accepted` (issue #21640) is never typed by a human; resolve-handler
derives it whenever the resolving actor is the PR author and the disposition
they typed is one of AUTHOR_COLLAPSIBLE. The entry keeps the author's actual
answer in `original_disposition` — needed both to weigh the note-required
check against the answer that was actually given, and to show the human
approver what the author waved through rather than just that they did.

Three writers share this module and MUST merge rather than overwrite:
`review-resolve.yml` (the deterministic `/resolve` command), the update lane
(`apply-update.py`), and nothing else. Merging is per finding-id with the
newest `updated_at` winning — the update lane's model step can take ~10
minutes between fetching the comment and writing it back, and a `/resolve`
landing in that window must survive (the lost-update race from the v3 design
review).

Serialization escapes `<` and `>` inside the JSON payload: an HTML comment
terminates at the first `-->`, so a disposition note containing one would
otherwise truncate the block and destroy every recorded answer.

Block shape (always one line):
  <!-- REVIEW_STATE {"schema":1,"high_water":7,"findings":{"F3":{...}}} -->
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone

SCHEMA = 1
DISPOSITIONS = ("fixed", "refuted", "deferred", "accepted", "not-applicable", "author-accepted")
# The disposition a human may type in a `/resolve` comment. `author-accepted`
# is never typed directly — resolve-handler.py derives it from USER_DISPOSITIONS
# plus the actor's identity (see AUTHOR_COLLAPSIBLE below), so it is excluded
# here to keep it out of the user-facing grammar.
USER_DISPOSITIONS = ("fixed", "refuted", "deferred", "accepted", "not-applicable")
# The subset of USER_DISPOSITIONS that collapse into `author-accepted` when
# the resolving actor is the PR author (issue #21640): the author's own word
# on a judgment call, not a verified fix, so it must stay visible to the
# human approver instead of reading exactly like a maintainer's answer.
# `fixed` is excluded — a real code change, not a disposition to relabel.
AUTHOR_COLLAPSIBLE = ("refuted", "deferred", "accepted", "not-applicable")
NOTE_REQUIRED = ("deferred", "accepted", "not-applicable")
FINDING_ID_RE = re.compile(r"^F\d+$")
BLOCK_RE = re.compile(r"<!-- REVIEW_STATE (\{.*?\}) -->")


def empty_state() -> dict:
    return {"schema": SCHEMA, "high_water": 0, "findings": {}}


def parse_state(body: str) -> dict | None:
    """Extract the REVIEW_STATE block from a comment body.

    Returns None when no block is present. Raises ValueError on a block that
    exists but does not decode or validate — a corrupt block must be surfaced,
    never silently treated as empty (that would un-answer every finding).
    """
    m = BLOCK_RE.search(body)
    if not m:
        if "<!-- REVIEW_STATE" in body:
            raise ValueError("REVIEW_STATE marker present but block is malformed/truncated")
        return None
    try:
        state = json.loads(m.group(1))
    except json.JSONDecodeError as exc:
        raise ValueError(f"REVIEW_STATE block is not valid JSON: {exc}") from exc
    problems = validate_state(state)
    if problems:
        raise ValueError("REVIEW_STATE block invalid: " + "; ".join(problems))
    return state


def validate_state(state: object) -> list[str]:
    problems: list[str] = []
    if not isinstance(state, dict):
        return ["state is not an object"]
    if state.get("schema") != SCHEMA:
        problems.append(f"schema must be {SCHEMA}")
    hw = state.get("high_water")
    if not isinstance(hw, int) or hw < 0:
        problems.append("high_water must be a non-negative integer")
    findings = state.get("findings")
    if not isinstance(findings, dict):
        problems.append("findings must be an object")
        return problems
    for fid, entry in findings.items():
        prefix = f"findings[{fid}]"
        if not FINDING_ID_RE.match(fid):
            problems.append(f"{prefix}: id must match F<n>")
        if not isinstance(entry, dict):
            problems.append(f"{prefix}: must be an object")
            continue
        disposition = entry.get("disposition")
        if disposition not in DISPOSITIONS:
            problems.append(f"{prefix}: disposition must be one of {DISPOSITIONS}")
        original_disposition = entry.get("original_disposition")
        if disposition == "author-accepted":
            if original_disposition not in AUTHOR_COLLAPSIBLE:
                problems.append(
                    f"{prefix}: original_disposition must be one of {AUTHOR_COLLAPSIBLE} "
                    f"when disposition is 'author-accepted'"
                )
        elif original_disposition is not None:
            problems.append(f"{prefix}: original_disposition only applies to 'author-accepted'")
        # The note requirement follows the disposition the actor actually
        # answered with. `author-accepted` collapses four dispositions —
        # including `refuted`, which never requires a note — into one value,
        # so keying the check off the collapsed value would either demand a
        # note `refuted` never needed or (worse) waive the note `accepted`
        # always needed. original_disposition keeps the bar exactly where it
        # was before the collapse.
        note_check = original_disposition if disposition == "author-accepted" else disposition
        if note_check in NOTE_REQUIRED and not str(entry.get("note", "")).strip():
            problems.append(f"{prefix}: disposition '{note_check}' requires a note")
        if not str(entry.get("actor", "")).strip():
            problems.append(f"{prefix}: actor is required")
        ts = entry.get("updated_at")
        if not isinstance(ts, str) or _parse_ts(ts) is None:
            problems.append(f"{prefix}: updated_at must be an ISO-8601 timestamp")
        if "bulk" in entry and not isinstance(entry["bulk"], bool):
            problems.append(f"{prefix}: bulk must be a boolean")
        unknown = set(entry) - {
            "disposition", "note", "actor", "sha", "bulk", "updated_at", "original_disposition",
        }
        if unknown:
            problems.append(f"{prefix}: unknown keys {sorted(unknown)}")
    return problems


def _parse_ts(value: str) -> datetime | None:
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (ValueError, AttributeError):
        return None


def merge_states(base: dict, other: dict) -> dict:
    """Per-finding merge; the newer updated_at wins, ties keep base.

    Neither input is mutated. high_water is the max of both — it only grows.
    """
    merged = {
        "schema": SCHEMA,
        "high_water": max(base.get("high_water", 0), other.get("high_water", 0)),
        "findings": dict(base.get("findings", {})),
    }
    for fid, entry in other.get("findings", {}).items():
        existing = merged["findings"].get(fid)
        if existing is None:
            merged["findings"][fid] = entry
            continue
        existing_ts = _parse_ts(existing.get("updated_at", "")) or datetime.min.replace(tzinfo=timezone.utc)
        entry_ts = _parse_ts(entry.get("updated_at", "")) or datetime.min.replace(tzinfo=timezone.utc)
        if entry_ts > existing_ts:
            merged["findings"][fid] = entry
    return merged


def set_disposition(
    state: dict,
    finding_id: str,
    disposition: str,
    *,
    actor: str,
    note: str = "",
    sha: str = "",
    bulk: bool = False,
    now: datetime | None = None,
    original_disposition: str | None = None,
) -> dict:
    """Return a new state with one disposition applied (validated).

    `original_disposition` is required (and must be in AUTHOR_COLLAPSIBLE)
    when `disposition` is `author-accepted`, and forbidden otherwise — see
    the matching rule in validate_state.
    """
    if disposition not in DISPOSITIONS:
        raise ValueError(f"unknown disposition '{disposition}'")
    if disposition == "author-accepted":
        if original_disposition not in AUTHOR_COLLAPSIBLE:
            raise ValueError(
                f"'author-accepted' requires original_disposition in {AUTHOR_COLLAPSIBLE}"
            )
    elif original_disposition is not None:
        raise ValueError("original_disposition only applies to 'author-accepted'")
    note_check = original_disposition if disposition == "author-accepted" else disposition
    if note_check in NOTE_REQUIRED and not note.strip():
        raise ValueError(f"disposition '{note_check}' requires a note")
    if not FINDING_ID_RE.match(finding_id):
        raise ValueError(f"bad finding id '{finding_id}'")
    if not actor.strip():
        raise ValueError("actor is required")
    ts = (now or datetime.now(timezone.utc)).isoformat().replace("+00:00", "Z")
    entry = {"disposition": disposition, "actor": actor, "updated_at": ts, "bulk": bulk}
    if note.strip():
        entry["note"] = note.strip()
    if sha:
        entry["sha"] = sha
    if original_disposition is not None:
        entry["original_disposition"] = original_disposition
    new_state = {
        "schema": SCHEMA,
        "high_water": state.get("high_water", 0),
        "findings": dict(state.get("findings", {})),
    }
    new_state["findings"][finding_id] = entry
    return new_state


def serialize_block(state: dict) -> str:
    problems = validate_state(state)
    if problems:
        raise ValueError("refusing to serialize invalid state: " + "; ".join(problems))
    payload = json.dumps(state, sort_keys=True, separators=(",", ":"))
    payload = payload.replace("<", "\\u003c").replace(">", "\\u003e")
    return f"<!-- REVIEW_STATE {payload} -->"


def replace_block(body: str, state: dict) -> str:
    """Swap the block in a comment body, or append one if absent."""
    block = serialize_block(state)
    if BLOCK_RE.search(body):
        return BLOCK_RE.sub(lambda _: block, body, count=1)
    return body.rstrip("\n") + "\n" + block + "\n"


def _self_test() -> int:
    now = datetime(2026, 8, 31, 12, 0, tzinfo=timezone.utc)
    earlier = datetime(2026, 8, 31, 11, 0, tzinfo=timezone.utc)

    state = set_disposition(empty_state(), "F3", "refuted", actor="cam", note="flag exists", now=now)
    block = serialize_block(state)
    assert "-->" not in block[len("<!-- REVIEW_STATE ") : -len(" -->")], "payload must not contain -->"
    body = f"## Review\n{block}\n"
    parsed = parse_state(body)
    assert parsed is not None and parsed["findings"]["F3"]["disposition"] == "refuted"

    hostile = set_disposition(
        empty_state(), "F1", "accepted", actor="cam", note="see --> and <script> here", now=now
    )
    round_tripped = parse_state("x\n" + serialize_block(hostile) + "\ny")
    assert round_tripped is not None
    assert round_tripped["findings"]["F1"]["note"] == "see --> and <script> here"

    base = set_disposition(empty_state(), "F1", "fixed", actor="update-lane", now=earlier)
    other = set_disposition(empty_state(), "F1", "refuted", actor="author", note="n", now=now)
    assert merge_states(base, other)["findings"]["F1"]["disposition"] == "refuted"
    assert merge_states(other, base)["findings"]["F1"]["disposition"] == "refuted"

    tie_a = set_disposition(empty_state(), "F2", "fixed", actor="a", now=now)
    tie_b = set_disposition(empty_state(), "F2", "deferred", actor="b", note="n", now=now)
    assert merge_states(tie_a, tie_b)["findings"]["F2"]["disposition"] == "fixed", "tie keeps base"

    try:
        set_disposition(empty_state(), "F9", "accepted", actor="cam")
    except ValueError:
        pass
    else:
        raise AssertionError("accepted without a note must be rejected")

    # author-accepted: the collapsed disposition an author's own /resolve
    # produces (issue #21640) — original_disposition required, and the note
    # requirement follows the ORIGINAL disposition, not the collapsed one.
    aa = set_disposition(
        empty_state(), "F5", "author-accepted", actor="alice",
        note="will fix in a follow-up", original_disposition="accepted", now=now,
    )
    assert aa["findings"]["F5"]["disposition"] == "author-accepted"
    assert aa["findings"]["F5"]["original_disposition"] == "accepted"
    round_tripped_aa = parse_state("x\n" + serialize_block(aa) + "\ny")
    assert round_tripped_aa is not None
    assert round_tripped_aa["findings"]["F5"]["original_disposition"] == "accepted"

    # original_disposition 'refuted' never required a note — that must still
    # hold true after the collapse.
    aa_refuted = set_disposition(
        empty_state(), "F6", "author-accepted", actor="alice",
        original_disposition="refuted", now=now,
    )
    assert "note" not in aa_refuted["findings"]["F6"]

    try:
        set_disposition(empty_state(), "F7", "author-accepted", actor="alice",
                        note="x", original_disposition="accepted")
    except ValueError:
        raise AssertionError("author-accepted 'accepted' with a note must be accepted, not rejected")

    try:
        set_disposition(empty_state(), "F8", "author-accepted", actor="alice",
                        original_disposition="accepted")
    except ValueError:
        pass
    else:
        raise AssertionError("author-accepted collapsing 'accepted' without a note must be rejected")

    try:
        set_disposition(empty_state(), "F10", "author-accepted", actor="alice", note="n")
    except ValueError:
        pass
    else:
        raise AssertionError("author-accepted with no original_disposition must be rejected")

    try:
        set_disposition(empty_state(), "F11", "fixed", actor="alice", original_disposition="accepted")
    except ValueError:
        pass
    else:
        raise AssertionError("original_disposition on a non-author-accepted entry must be rejected")

    assert "author-accepted" not in USER_DISPOSITIONS
    assert set(AUTHOR_COLLAPSIBLE) <= set(USER_DISPOSITIONS)

    assert parse_state("no block here") is None
    try:
        parse_state("<!-- REVIEW_STATE {broken -->")
    except ValueError:
        pass
    else:
        raise AssertionError("corrupt block must raise, not read as empty")

    replaced = replace_block(body, set_disposition(state, "F4", "fixed", actor="cam", now=now))
    assert len(BLOCK_RE.findall(replaced)) == 1
    reparsed = parse_state(replaced)
    assert reparsed is not None and set(reparsed["findings"]) == {"F3", "F4"}

    print("review_state self-test passed")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        return _self_test()
    parser.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
