#!/usr/bin/env python3
"""migrate-command-text.py — move live review comments to the slash commands.

pulumi/docs#22277 retired `@claude … #update-review` / `#new-review` and the
bare `sentinel:oversized-ack` token in favor of the slash commands
(`/update-review`, `/new-review`, `/oversized-ack`). New comments render the
new text, but the cards and notices already on open PRs still teach the old
shapes, and anyone who follows them gets the redirect reply instead of a
review. This rewrites that text in place.

Like restamp-base-merge.py: deterministic, no model, nothing re-reviewed.
Only the instruction text changes. Markers, the REVIEW_STATE block,
findings, and the composition timestamps are untouched, so pinned-comment.sh
still orders a later refresh over the edited card.

What it touches — issue comments on open PRs that the review machinery
wrote (`BOT_LOGINS`) and that carry one of its markers (`KINDS`). Human
comments, the glow-up autofix's own requests, and the redirect's replies
(which quote the old shape on purpose) are never edited.

What it changes — the ordered `RULES` table: the exact sentences the old
templates rendered first, then the command shapes generally. After the
rules run, anything still matching `RESIDUE_RE` is reported, never guessed
at: a card from a template variant the table doesn't know shows up there.

Usage:
  migrate-command-text.py --repo pulumi/docs [--pr N ...] [--apply]
                          [--report out.md] [--snapshot-dir DIR]
Without --apply it is a dry run: it prints one JSON line per comment it
would change plus a summary, and --report writes a markdown diff of every
edit. With --apply each comment is re-read immediately before its write, so
a card republished since the plan is migrated from its new body. Run it
once, after #22277 merges; running it again changes nothing.
"""

from __future__ import annotations

import argparse
import difflib
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from gh_client import GhClient, GhError  # noqa: E402

DEFAULT_REPO = "pulumi/docs"

# Who writes review comments: the v3 cards, the Sentinel, progress notices,
# and triage are github-actions[bot]; legacy v2 pages were also posted as
# pulumi-bot (sentinel.LEGACY_PAGE_WRITERS) and, before that, claude[bot].
BOT_LOGINS = frozenset({"github-actions[bot]", "pulumi-bot", "claude[bot]"})

# (kind, test) — the first match names the comment in the report.
KINDS: tuple[tuple[str, object], ...] = (
    ("author card", lambda b: "<!-- CLAUDE_REVIEW_AUTHOR -->" in b),
    ("reviewer brief", lambda b: "<!-- CLAUDE_REVIEW_BRIEF -->" in b),
    ("v2 review page", lambda b: b.lstrip().startswith("<!-- CLAUDE_REVIEW ")),
    ("sentinel status", lambda b: b.lstrip().startswith("<!-- SENTINEL_STATUS -->")),
    ("progress notice", lambda b: b.lstrip().startswith("<!-- CLAUDE_PROGRESS -->")),
    ("oversized advisory", lambda b: b.lstrip().startswith("<!-- TRIAGE_OVERSIZED -->")),
    ("staleness warning", lambda b: b.lstrip().startswith("This PR is waiting on you:")),
    ("declined notice", lambda b: "needs write access to this repository, so no review was started" in b),
)
NEVER = ("<!-- REVIEW_COMMAND_REDIRECT -->",)

_CMD = r"(update-review|new-review)"

# Ordered. The exact sentences come first, while their wording is still
# intact; the general shapes after them would otherwise eat their hashtags.
RULES: tuple[tuple[str, re.Pattern, str], ...] = (
    # The author card's orienting alert and the v2 footer.
    ("hashtag tag sentence",
     re.compile(r"A reply without the `#update-review` tag doesn't count\."),
     "A reply without `/update-review` at the start of a line doesn't count."),
    ("hashtag explainer",
     re.compile(r"The `#update-review` hashtag matters — it routes your reply"),
     "`/update-review` has to start a line of your comment — it routes your reply"),
    ("same mention",
     re.compile(r"both work in the same mention\."),
     "both work in the same comment."),
    ("no hashtag",
     re.compile(r"comment `@claude` with no hashtag"),
     "comment `@claude`"),
    # claude-new's declined notice.
    ("declined command",
     re.compile(r"`#new-review` needs write access"),
     "`/new-review` needs write access"),
    # The oversized hand-review ack: triage's advisory and the Sentinel's G5.
    ("oversized ack placement",
     re.compile(r"`sentinel:oversized-ack` anywhere in"),
     "`/oversized-ack` at the start of a line in"),
    ("oversized ack cli",
     re.compile(r"--body sentinel:oversized-ack"),
     "--body /oversized-ack"),
    ("oversized ack token",
     re.compile(r"`sentinel:oversized-ack`"),
     "`/oversized-ack`"),
    # A command in a code span, with or without request text:
    # `@claude F2: <why> #update-review` -> `/update-review F2: <why>`.
    ("code span",
     re.compile(r"`@claude(?:[ \t]+([^`\n]*?))?[ \t]*#" + _CMD + r"`"),
     lambda m: f"`/{m.group(2)}{' ' + m.group(1) if m.group(1) else ''}`"),
    # A reply example on its own line in the "How to answer" fences.
    ("example line",
     re.compile(r"^([ \t]*)@claude[ \t]+(.*?)[ \t]*#" + _CMD + r"[ \t]*$", re.M),
     lambda m: f"{m.group(1)}/{m.group(3)} {m.group(2)}"),
    # Progress and superseded notices: "Mention @claude #x" or, after the
    # code-span rule, "mention `/x`". Commands are commented, not mentioned.
    ("bare mention",
     re.compile(r"\b([Mm])ention @claude #" + _CMD + r"\b"),
     lambda m: f"{'C' if m.group(1) == 'M' else 'c'}omment `/{m.group(2)}`"),
    ("mention verb",
     re.compile(r"\b([Mm])ention `/" + _CMD + r"`"),
     lambda m: f"{'C' if m.group(1) == 'M' else 'c'}omment `/{m.group(2)}`"),
)

# What must not survive. Anything here after the rules is reported — except
# a review-history entry, which records the command someone actually ran at
# the time and stays as written.
RESIDUE_RE = re.compile(r"#(?:update|new)-review\b|sentinel:oversized-ack")
_HISTORY_RE = re.compile(r"^\s*-\s*\d{4}-\d{2}-\d{2}T[\d:]+Z\s+—")


def kind_of(comment: dict) -> str | None:
    """The comment's kind when it is ours to edit, else None."""
    login = ((comment.get("user") or {}).get("login") or "")
    body = comment.get("body") or ""
    if login not in BOT_LOGINS or any(m in body for m in NEVER):
        return None
    for name, test in KINDS:
        if test(body):
            return name
    return None


def migrate(body: str) -> tuple[str, list[str]]:
    """`body` with the retired command text rewritten, and the rules that
    fired. Line endings are kept as they came."""
    fired = []
    for name, pattern, repl in RULES:
        body, n = pattern.subn(repl, body)
        if n:
            fired.append(name)
    return body, fired


def residue(body: str) -> list[str]:
    """Lines that still carry a retired shape after migration, history aside."""
    return [ln.strip() for ln in body.splitlines()
            if RESIDUE_RE.search(ln) and not _HISTORY_RE.match(ln)]


def plan(gh: GhClient, prs: list[int] | None = None) -> dict:
    """Every edit the migration would make, plus residue, without writing."""
    numbers = prs or sorted(p["number"] for p in gh.list_open_prs())
    edits, leftovers, errors = [], [], []
    scanned = 0
    for n in numbers:
        try:
            comments = gh.issue_comments(n)
        except GhError as exc:
            errors.append({"pr": n, "error": str(exc)})
            continue
        for c in comments:
            kind = kind_of(c)
            if kind is None:
                continue
            scanned += 1
            before = c.get("body") or ""
            after, fired = migrate(before)
            left = residue(after)
            if after != before:
                edits.append({"pr": n, "id": c["id"], "kind": kind, "rules": fired,
                              "url": c.get("html_url", ""), "before": before, "after": after})
            if left:
                leftovers.append({"pr": n, "id": c["id"], "kind": kind,
                                  "url": c.get("html_url", ""), "lines": left})
    return {"prs": len(numbers), "scanned": scanned, "edits": edits,
            "residue": leftovers, "errors": errors}


def apply(gh: GhClient, edits: list[dict]) -> list[dict]:
    """Write each planned edit. The comment is re-read first and migrated
    from what is there now, so a card republished since the plan keeps its
    new content; a body that no longer needs it is skipped."""
    results = []
    for e in edits:
        path = f"repos/{gh.repo}/issues/comments/{e['id']}"
        try:
            fresh = gh.get(path) or {}
            current = fresh.get("body") or ""
            after, _ = migrate(current)
            if after == current:
                results.append({"id": e["id"], "pr": e["pr"], "result": "already current"})
                continue
            gh.patch(path, {"body": after})
            results.append({"id": e["id"], "pr": e["pr"], "result": "edited"})
        except GhError as exc:
            results.append({"id": e["id"], "pr": e["pr"], "result": f"error: {exc}"})
    return results


def render_report(p: dict, results: list[dict] | None = None) -> str:
    applied = results is not None
    lines = [
        f"## Review command text migration — {'applied' if applied else 'dry run'}",
        "",
        f"{p['prs']} open PR(s), {p['scanned']} review comment(s) scanned, "
        f"**{len(p['edits'])}** to edit, {len(p['residue'])} with residue, {len(p['errors'])} read error(s).",
        "",
    ]
    if applied:
        tally: dict[str, int] = {}
        for r in results:
            key = r["result"].split(":")[0]
            tally[key] = tally.get(key, 0) + 1
        lines += ["**Writes:** " + ", ".join(f"{k} {v}" for k, v in sorted(tally.items())), ""]
    if p["residue"]:
        lines += ["### Residue (not rewritten — extend RULES or fix by hand)", ""]
        for r in p["residue"]:
            lines.append(f"- #{r['pr']} {r['kind']} {r['url']}")
            lines += [f"  - `{ln[:160]}`" for ln in r["lines"]]
        lines.append("")
    if p["errors"]:
        lines += ["### Read errors", ""] + [f"- #{e['pr']}: {e['error']}" for e in p["errors"]] + [""]
    for e in p["edits"]:
        diff = difflib.unified_diff(e["before"].splitlines(), e["after"].splitlines(),
                                    lineterm="", n=0)
        body = "\n".join(ln for ln in diff if not ln.startswith(("---", "+++", "@@")))
        lines += [f"<details><summary>#{e['pr']} · {e['kind']} · {', '.join(e['rules'])}</summary>",
                  "", e["url"], "", "```diff", body, "```", "", "</details>", ""]
    return "\n".join(lines)


def _self_test() -> int:
    failures = 0

    def check(name: str, cond: bool) -> None:
        nonlocal failures
        print(f"  {'ok ' if cond else 'FAIL'} {name}")
        if not cond:
            failures += 1

    m = lambda s: migrate(s)[0]
    check("alert", m("> **To answer:** push a fix, or reply `@claude F1: <what you fixed> #update-review`. "
                     "A reply without the `#update-review` tag doesn't count. ")
          == "> **To answer:** push a fix, or reply `/update-review F1: <what you fixed>`. "
             "A reply without `/update-review` at the start of a line doesn't count. ")
    check("group question", m("one reply: `@claude F7: <what you checked them against> #update-review`.")
          == "one reply: `/update-review F7: <what you checked them against>`.")
    check("bare code span", m("comment `@claude #update-review`.") == "comment `/update-review`.")
    check("new-review span", m("or `@claude #new-review` for a fresh one") == "or `/new-review` for a fresh one")
    check("example line", m("```text\n   @claude I pushed a fix for F1 #update-review\n```")
          == "```text\n   /update-review I pushed a fix for F1\n```")
    check("explainer", m("The `#update-review` hashtag matters — it routes your reply to this review")
          == "`/update-review` has to start a line of your comment — it routes your reply to this review")
    check("progress notice", m("<!-- CLAUDE_PROGRESS -->\n🤖 @a — review errored. Mention @claude #update-review again to retry.")
          == "<!-- CLAUDE_PROGRESS -->\n🤖 @a — review errored. Comment `/update-review` again to retry.")
    check("mentioned span", m("Flip to draft and back to ready, or mention `@claude #update-review`, to retry.")
          == "Flip to draft and back to ready, or comment `/update-review`, to retry.")
    check("superseded", m("Mention `@claude #new-review` once it settles.") == "Comment `/new-review` once it settles.")
    check("oversized advisory", m("put `sentinel:oversized-ack` anywhere in your **Approve** review's comment, "
                                  "or run `gh pr review 7 --approve --body sentinel:oversized-ack`.")
          == "put `/oversized-ack` at the start of a line in your **Approve** review's comment, "
             "or run `gh pr review 7 --approve --body /oversized-ack`.")
    check("markers and state untouched",
          m("<!-- CLAUDE_REVIEW_AUTHOR -->\n<!-- REVIEW_STATE {\"findings\":{}} -->") ==
          "<!-- CLAUDE_REVIEW_AUTHOR -->\n<!-- REVIEW_STATE {\"findings\":{}} -->")
    once = m("x `@claude F1: y #update-review` z\n   @claude a #update-review")
    check("idempotent", m(once) == once)
    check("residue reported", residue("still says #update-review somewhere") != [])
    check("clean text has no residue", residue(once) == [])
    hist = "- 2026-09-01T01:45:01Z — Re-verified on `@workprentice[bot]`'s `#update-review` (1 new commit)."
    check("review history is left as written", m(hist) == hist and residue(hist) == [])

    bot = {"login": "github-actions[bot]"}
    check("card is ours", kind_of({"user": bot, "body": "<!-- CLAUDE_REVIEW 1/1 -->\n<!-- CLAUDE_REVIEW_AUTHOR -->"}) == "author card")
    check("human comment is not", kind_of({"user": {"login": "alice"}, "body": "<!-- CLAUDE_REVIEW_AUTHOR --> @claude #update-review"}) is None)
    check("redirect reply is not", kind_of({"user": bot, "body": "<!-- REVIEW_COMMAND_REDIRECT -->\n`@claude … #update-review` is retired"}) is None)
    check("glow-up request is not", kind_of({"user": {"login": "pulumi-bot"}, "body": "<!-- glowup-autofix pass=1 -->\n@claude answering\n\n#update-review"}) is None)

    print("migrate-command-text self-test:", "PASS" if failures == 0 else f"{failures} FAILED")
    return 1 if failures else 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--repo", default=DEFAULT_REPO)
    ap.add_argument("--pr", type=int, action="append", help="limit to these PRs (default: every open PR)")
    ap.add_argument("--apply", action="store_true", help="write the edits (default: dry run)")
    ap.add_argument("--report", help="write a markdown report (diffs and residue) here")
    ap.add_argument("--snapshot-dir", help="read from a GhClient snapshot directory instead of GitHub")
    args = ap.parse_args(argv)
    if args.self_test:
        return _self_test()

    gh = GhClient(args.repo, backend="snapshot" if args.snapshot_dir else "auto",
                  snapshot_dir=args.snapshot_dir)
    p = plan(gh, args.pr)
    results = apply(gh, p["edits"]) if args.apply else None

    for e in p["edits"]:
        print(json.dumps({"pr": e["pr"], "id": e["id"], "kind": e["kind"], "rules": e["rules"]}))
    summary = {"mode": "apply" if args.apply else "dry-run", "prs": p["prs"], "scanned": p["scanned"],
               "edits": len(p["edits"]), "residue": len(p["residue"]), "errors": len(p["errors"])}
    if results is not None:
        summary["writes"] = results
    print(json.dumps(summary))
    if args.report:
        with open(args.report, "a", encoding="utf-8") as fh:
            fh.write(render_report(p, results) + "\n")
    failed_writes = results is not None and any(r["result"].startswith("error") for r in results)
    return 1 if (p["errors"] or failed_writes) else 0


if __name__ == "__main__":
    sys.exit(main())
