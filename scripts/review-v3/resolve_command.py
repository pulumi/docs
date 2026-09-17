#!/usr/bin/env python3
"""Grammar for the `/resolve` comment command and the prose-answer detector.

`/resolve` is the zero-model way for an author to answer a review finding —
the deterministic half of the v3 answer loop (`@claude #update-review` is the
adjudicated half). One comment may carry several commands, one per line:

    /resolve F3 refuted: the CLI flag does exist in 3.261
    /resolve F7 fixed
    /resolve all accepted: I know what I'm doing

Rules: dispositions are the review-worklist closed set; `deferred`,
`accepted`, and `not-applicable` require a note; `all` always requires a note
(a bulk answer with no reason is exactly the rubber stamp the telemetry needs
to see explained) and marks every entry `bulk: true`.

The prose detector serves the opposite case: an author who answers a finding
in plain English. Nothing parses prose, the Sentinel stays red, and the author
believes they answered — the worst UX in the v3 design review. When a comment
mentions a known finding id but contains no valid command and no `@claude`
mention, the listener workflow posts one short pointer (rate-limited by the
workflow, not here).

Used by `review-resolve.yml`; state application lives in `review_state.py`.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field

from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
import review_state  # noqa: E402

COMMAND_RE = re.compile(
    r"^\s*/resolve\s+(?P<target>[Ff]\d+|all)\s+(?P<disposition>[a-z-]+)\s*(?::\s*(?P<note>.*\S))?\s*$"
)
FINDING_MENTION_RE = re.compile(r"\bF\d+\b")


@dataclass
class ParseResult:
    commands: list[dict] = field(default_factory=list)  # {target, disposition, note, bulk}
    errors: list[str] = field(default_factory=list)  # human-readable, for the reply


def parse_commands(body: str) -> ParseResult:
    result = ParseResult()
    for line in body.splitlines():
        if not line.lstrip().startswith("/resolve"):
            continue
        m = COMMAND_RE.match(line)
        if not m:
            result.errors.append(
                f"could not parse `{line.strip()}` — expected `/resolve F<n> <disposition>[: note]`"
            )
            continue
        target = m.group("target")
        disposition = m.group("disposition")
        note = (m.group("note") or "").strip()
        bulk = target == "all"
        if disposition not in review_state.DISPOSITIONS:
            result.errors.append(
                f"`{disposition}` is not a disposition — use one of: "
                + ", ".join(review_state.DISPOSITIONS)
            )
            continue
        if bulk and not note:
            result.errors.append(
                "`/resolve all` always needs a reason — `/resolve all "
                f"{disposition}: <why>`"
            )
            continue
        if disposition in review_state.NOTE_REQUIRED and not note:
            result.errors.append(
                f"`{disposition}` needs a reason — `/resolve {target} {disposition}: <why>`"
            )
            continue
        result.commands.append(
            {
                "target": "all" if bulk else target.upper(),
                "disposition": disposition,
                "note": note,
                "bulk": bulk,
            }
        )
    return result


def detect_prose_answer(body: str, known_ids: set[str]) -> list[str]:
    """Finding ids a comment mentions without any parseable command.

    Returns the ids worth a pointer reply — empty when the comment already
    carries a valid `/resolve` line, mentions `@claude` (the update lane will
    handle it), or names no known finding.
    """
    parsed = parse_commands(body)
    if parsed.commands or parsed.errors:
        return []  # a malformed command gets the error reply, not the prose pointer
    if "@claude" in body:
        return []
    mentioned = {m.group(0).upper() for m in FINDING_MENTION_RE.finditer(body)}
    return sorted(mentioned & known_ids)


def _self_test() -> int:
    ok = parse_commands("/resolve F3 refuted: flag exists in 3.261\n/resolve F7 fixed")
    assert not ok.errors and len(ok.commands) == 2
    assert ok.commands[0] == {"target": "F3", "disposition": "refuted", "note": "flag exists in 3.261", "bulk": False}
    assert ok.commands[1]["note"] == "" and ok.commands[1]["disposition"] == "fixed"

    lower = parse_commands("/resolve f12 not-applicable: generated file")
    assert not lower.errors and lower.commands[0]["target"] == "F12"

    bulk = parse_commands("/resolve all accepted: I know what I'm doing")
    assert not bulk.errors and bulk.commands[0]["bulk"] is True

    bare_bulk = parse_commands("/resolve all refuted")
    assert bare_bulk.errors and not bare_bulk.commands, "bulk without a note must be rejected"

    noteless = parse_commands("/resolve F3 accepted")
    assert noteless.errors and not noteless.commands

    bad_disp = parse_commands("/resolve F3 wontfix: nah")
    assert any("not a disposition" in e for e in bad_disp.errors)

    mixed = parse_commands("some prose\n/resolve F1 fixed\nmore prose about F9")
    assert len(mixed.commands) == 1 and not mixed.errors

    known = {"F1", "F2", "F3"}
    assert detect_prose_answer("I think F3 is wrong because the flag exists", known) == ["F3"]
    assert detect_prose_answer("F3 is wrong\n/resolve F3 refuted: flag exists", known) == []
    assert detect_prose_answer("@claude #update-review F3 is wrong", known) == []
    assert detect_prose_answer("F99 is wrong", known) == []
    assert detect_prose_answer("no ids here", known) == []
    malformed = detect_prose_answer("/resolve F2 accepted", known)
    assert malformed == [], "a malformed command gets the error reply path, not the prose pointer"

    print("resolve_command self-test passed")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--parse", metavar="FILE", help="parse commands from a file ('-' = stdin), print JSON")
    args = parser.parse_args()
    if args.self_test:
        return _self_test()
    if args.parse:
        import json

        body = sys.stdin.read() if args.parse == "-" else Path(args.parse).read_text()
        result = parse_commands(body)
        print(json.dumps({"commands": result.commands, "errors": result.errors}, indent=2))
        return 0 if not result.errors else 1
    parser.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
