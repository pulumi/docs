#!/usr/bin/env python3
"""Deterministic dead-internal-link check over a PR diff.

Every `/docs/...` or `/blog/...` markdown link target on an ADDED line of a
content file is resolved the way the site resolves it: a page file under
`content/`, a file the PR itself adds, or an `aliases:` entry on some page.
Anything that resolves to nothing is a dead link the review must surface as a
🚨 finding — deterministically, not by the model happening to notice.

Why this exists: the Hugo pre-step (`hugo-build-validate.py`) only runs when
templating paths change, so for the ~95% of PRs that are content-only its
artifact is a skip-stub with `link_integrity: []`, and Hugo doesn't validate
plain markdown links anyway (only `ref`/`relref`). Smoke PR #21560 added a
link to a page that doesn't exist; the review quoted the line inside another
finding and never flagged the link.

Output entries are `{file, line, target, reason}`. With `--merge-into
.hugo-build.json` the dead links are appended to that artifact's
`link_integrity` list as `content/<file>:<line>: ...` strings (the shape
`compose-review.py`'s `_hugo_synthetic_verdicts` already parses) and a
`link_check` block records whether the check ran. A crash never fails the
review: `link_check.ran` is false, the error is recorded, and a `::warning::`
is printed — an unrun check must never look like a passed one.

Resolution mirrors `validate-pinned.py`'s `check_internal_link_existence`;
keep the two in step (the validator applies the same rule to the review body).

Usage:
  link-check-diff.py --diff-file pr.diff --repo-root . [--out links.json]
  link-check-diff.py --pr 123 --repo pulumi/docs --merge-into .hugo-build.json
  link-check-diff.py --self-test
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

LINK_RE = re.compile(r"\]\(((?:/docs/|/blog/)[^)\s]+)\)")
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
HUNK_RE = re.compile(r"^@@ -\d+(?:,\d+)? \+(\d+)(?:,\d+)? @@")


def _normalize(href: str) -> str:
    """Strip fragment/query and the trailing slash: `/docs/x/#y?z` -> `/docs/x`."""
    return href.split("#", 1)[0].split("?", 1)[0].rstrip("/")


def _candidates(path: str) -> list[str]:
    rel = "content" + path
    return [f"{rel}.md", f"{rel}/_index.md", f"{rel}/index.md"]


def _alias_exists(repo_root: Path, path: str) -> bool:
    """True when some page under content/ lists `path` in its `aliases:`.
    Same `git grep -e` shape as the validator (the `-e` matters: the pattern
    starts with `-`)."""
    try:
        result = subprocess.run(
            ["git", "grep", "-l", "-e", f"- {path}", "--", "content/"],
            cwd=repo_root, capture_output=True, text=True, timeout=10,
        )
        return bool(result.stdout.strip())
    except (subprocess.SubprocessError, OSError):
        return False


def resolve(target: str, repo_root: Path, added_files: set[str]) -> str | None:
    """Return None when the link resolves, else a one-line reason."""
    if "<" in target or ">" in target:
        return None  # placeholder path in a template example
    path = _normalize(target)
    if not path:
        return None
    cands = _candidates(path)
    if any((repo_root / c).exists() for c in cands):
        return None
    if any(c in added_files for c in cands):
        return None
    if _alias_exists(repo_root, path):
        return None
    return "no page, alias, or PR-added file under content/"


def fenced_lines(text: str) -> set[int]:
    """1-based line numbers that sit inside a fenced code block (fence lines
    included) in the given file text."""
    out: set[int] = set()
    in_fence = False
    for i, line in enumerate(text.splitlines(), start=1):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            out.add(i)
            continue
        if in_fence:
            out.add(i)
    return out


def added_links(diff_text: str, repo_root: Path | None = None) -> tuple[list[tuple[str, int, str]], set[str]]:
    """Walk a unified diff. Return ([(file, new_line_no, target)], added_files).

    Only ADDED lines in `content/**.md` files are scanned; links inside inline
    code spans and fenced code blocks are ignored. Fence state is taken from
    the file at head under `repo_root` (the workflow checks the PR head out),
    because a hunk alone can't tell — a hunk that starts with the closing
    fence of a block opened above it reads inverted (that is exactly how the
    first cut missed #21560's dead link). Without the file on disk the
    hunk-local toggle is the fallback.
    """
    links: list[tuple[str, int, str]] = []
    added_files: set[str] = set()
    cur: str | None = None
    fenced: set[int] | None = None
    new_line = 0
    in_fence = False
    prev_from_dev_null = False
    for raw in diff_text.splitlines():
        if raw.startswith("--- "):
            prev_from_dev_null = raw.strip() == "--- /dev/null"
            continue
        if raw.startswith("+++ "):
            name = raw[4:].strip()
            cur = name[2:] if name.startswith("b/") else name
            if cur == "/dev/null":
                cur = None
            elif prev_from_dev_null:
                added_files.add(cur)
            in_fence = False
            fenced = None
            if cur and repo_root is not None:
                fp = repo_root / cur
                if fp.is_file():
                    try:
                        fenced = fenced_lines(fp.read_text(errors="replace"))
                    except OSError:
                        fenced = None
            continue
        m = HUNK_RE.match(raw)
        if m:
            new_line = int(m.group(1))
            in_fence = False
            continue
        if cur is None:
            continue
        if raw.startswith("-"):
            continue  # removed line: not in the new file
        if raw.startswith("\\"):
            continue  # "\ No newline at end of file"
        body = raw[1:] if raw[:1] in ("+", " ") else raw
        line_no = new_line
        new_line += 1
        if fenced is not None:
            inside = line_no in fenced
        else:
            if FENCE_RE.match(body):
                in_fence = not in_fence
                continue
            inside = in_fence
        if inside or not raw.startswith("+"):
            continue
        if not (cur.startswith("content/") and cur.endswith(".md")):
            continue
        for href in LINK_RE.findall(INLINE_CODE_RE.sub("", body)):
            links.append((cur, line_no, href))
    return links, added_files


def check(diff_text: str, repo_root: Path) -> list[dict]:
    links, added_files = added_links(diff_text, repo_root)
    out: list[dict] = []
    seen: set[tuple[str, int, str]] = set()
    for file, line, target in links:
        key = (file, line, _normalize(target))
        if key in seen:
            continue
        seen.add(key)
        reason = resolve(target, repo_root, added_files)
        if reason:
            out.append({"file": file, "line": line, "target": target, "reason": reason})
    return out


def as_integrity_line(entry: dict) -> str:
    """The `content/<file>:<line>: ...` shape `_hugo_synthetic_verdicts` parses."""
    return (
        f"{entry['file']}:{entry['line']}: dead internal link {entry['target']} "
        f"— {entry['reason']}"
    )


def merge_into(artifact_path: Path, dead: list[dict] | None, checked: int, error: str | None) -> dict:
    """Append dead links to `.hugo-build.json` and record the check's status.

    Creates a minimal artifact when the file is missing so the status is
    recorded regardless of whether the Hugo pre-step ran.
    """
    data: dict = {}
    if artifact_path.is_file():
        try:
            data = json.loads(artifact_path.read_text())
        except (OSError, json.JSONDecodeError):
            data = {}
    if not isinstance(data, dict):
        data = {}
    data.setdefault("schema_version", 1)
    li = data.get("link_integrity")
    if not isinstance(li, list):
        li = []
    if dead:
        li.extend(as_integrity_line(e) for e in dead)
    data["link_integrity"] = li
    stats = data.get("stats")
    if not isinstance(stats, dict):
        stats = {}
    stats["link_integrity_count"] = len(li)
    data["stats"] = stats
    data["link_check"] = {
        "ran": error is None,
        "checked": checked,
        "dead": len(dead or []),
        **({"error": error} if error else {}),
    }
    artifact_path.write_text(json.dumps(data, indent=2) + "\n")
    return data


def gh_pr_diff(repo: str | None, pr: int) -> str:
    cmd = ["gh", "pr", "diff", str(pr)]
    if repo:
        cmd += ["--repo", repo]
    return subprocess.run(cmd, capture_output=True, text=True, check=True, timeout=120).stdout


def _self_test() -> int:
    failures: list[str] = []

    def expect(cond: bool, msg: str) -> None:
        if not cond:
            failures.append(msg)

    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        subprocess.run(["git", "init", "-q"], cwd=root, check=True)
        (root / "content/docs/iac/concepts").mkdir(parents=True)
        head_stacks = (
            "---\ntitle: Stacks\n---\n"
            "```\nfenced context\n```\n"
            "See [config](/docs/iac/concepts/config/) and [old alias](/docs/intro/concepts/config/#top).\n"
            "Dead: [stack references](/docs/iac/concepts/stack-references/).\n"
            "Code: `[x](/docs/nope/)` stays quiet.\n"
            "```\n[fenced](/docs/also-nope/)\n```\n"
            "Template: [t](/docs/<section>/).\n"
            "New page: [new](/docs/iac/concepts/new-page/).\n"
            "External: [gh](https://github.com/pulumi/docs) and [blog dead](/blog/2099/nope/?utm=1).\n"
            "text\n"
        )
        (root / "content/docs/iac/concepts/stacks.md").write_text(head_stacks)
        (root / "content/docs/iac/concepts/config").mkdir()
        (root / "content/docs/iac/concepts/config/_index.md").write_text(
            "---\ntitle: Config\naliases:\n- /docs/intro/concepts/config/\n---\n"
        )
        subprocess.run(["git", "add", "-A"], cwd=root, check=True)
        # The hunk opens on the CLOSING fence of a block that began above it:
        # hunk-local fence tracking would read every added line as fenced.
        diff = """diff --git a/content/docs/iac/concepts/stacks.md b/content/docs/iac/concepts/stacks.md
--- a/content/docs/iac/concepts/stacks.md
+++ b/content/docs/iac/concepts/stacks.md
@@ -6,2 +6,11 @@ fenced context
 ```
+See [config](/docs/iac/concepts/config/) and [old alias](/docs/intro/concepts/config/#top).
+Dead: [stack references](/docs/iac/concepts/stack-references/).
+Code: `[x](/docs/nope/)` stays quiet.
+```
+[fenced](/docs/also-nope/)
+```
+Template: [t](/docs/<section>/).
+New page: [new](/docs/iac/concepts/new-page/).
+External: [gh](https://github.com/pulumi/docs) and [blog dead](/blog/2099/nope/?utm=1).
 text
diff --git a/content/docs/iac/concepts/new-page.md b/content/docs/iac/concepts/new-page.md
new file mode 100644
--- /dev/null
+++ b/content/docs/iac/concepts/new-page.md
@@ -0,0 +1,2 @@
+---
+title: New
"""
        dead = check(diff, root)
        targets = sorted(e["target"] for e in dead)
        expect(targets == ["/blog/2099/nope/?utm=1", "/docs/iac/concepts/stack-references/"],
               f"dead set: {targets}")
        by_target = {e["target"]: e for e in dead}
        expect(by_target["/docs/iac/concepts/stack-references/"]["line"] == 8,
               f"line: {by_target.get('/docs/iac/concepts/stack-references/')}")
        expect(by_target["/blog/2099/nope/?utm=1"]["line"] == 15, "blog line")
        line = as_integrity_line(by_target["/docs/iac/concepts/stack-references/"])
        expect(line.startswith("content/docs/iac/concepts/stacks.md:8: dead internal link"), line)
        # Without the file on disk the same hunk reads inverted: the hunk-local
        # fallback reports the fenced `/docs/also-nope/` link and misses the
        # real ones. That wrong answer is why the on-disk fence map exists.
        links_no_root, _ = added_links(diff, None)
        expect(("content/docs/iac/concepts/stacks.md", 11, "/docs/also-nope/") in links_no_root
               and not any(t == "/docs/iac/concepts/stack-references/" for _, _, t in links_no_root),
               f"fallback should read the hunk inverted: {links_no_root}")

        art = root / ".hugo-build.json"
        art.write_text(json.dumps({"skipped": True, "link_integrity": [], "stats": {"link_integrity_count": 0}}))
        merged = merge_into(art, dead, checked=8, error=None)
        expect(merged["link_check"]["ran"] is True and merged["link_check"]["dead"] == 2, str(merged["link_check"]))
        expect(merged["stats"]["link_integrity_count"] == 2, str(merged["stats"]))
        expect(merged["skipped"] is True, "skipped flag preserved")
        failed = merge_into(art, None, checked=0, error="boom")
        expect(failed["link_check"]["ran"] is False and failed["link_check"]["error"] == "boom",
               str(failed["link_check"]))
        expect(len(failed["link_integrity"]) == 2, "earlier entries kept on a failed re-run")

    if failures:
        for f in failures:
            print(f"FAIL: {f}", file=sys.stderr)
        return 1
    print("link-check-diff self-test: ok")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--diff-file", help="unified diff to scan (default: `gh pr diff --pr`)")
    ap.add_argument("--pr", type=int)
    ap.add_argument("--repo")
    ap.add_argument("--repo-root", default=".")
    ap.add_argument("--out", help="write the dead-link JSON array here (default: stdout)")
    ap.add_argument("--merge-into", help="append results to this .hugo-build.json and record link_check")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args(argv)
    if args.self_test:
        return _self_test()

    repo_root = Path(args.repo_root).resolve()
    dead: list[dict] = []
    checked = 0
    error: str | None = None
    try:
        if args.diff_file:
            diff_text = Path(args.diff_file).read_text()
        elif args.pr:
            diff_text = gh_pr_diff(args.repo, args.pr)
        else:
            ap.error("one of --diff-file or --pr is required")
        links, _ = added_links(diff_text, repo_root)
        checked = len(links)
        dead = check(diff_text, repo_root)
    except Exception as exc:  # noqa: BLE001 — a crash must be recorded, never fail the review
        error = f"{exc.__class__.__name__}: {exc}"
        print(f"::warning::link-check-diff: did not run ({error}); dead internal links were NOT checked",
              file=sys.stderr)

    if args.merge_into:
        merge_into(Path(args.merge_into), dead, checked, error)
    payload = json.dumps(dead, indent=2)
    if args.out:
        Path(args.out).write_text(payload + "\n")
    elif not args.merge_into:
        print(payload)
    if error is None:
        print(f"link-check-diff: {checked} internal link(s) on added lines, {len(dead)} dead", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
