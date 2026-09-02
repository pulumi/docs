#!/usr/bin/env python3
"""replay-mechanical.py — measure the v3 mechanical bar against real history.

`triage-classify.py`'s v3 addition, `classify_mechanical`, tightens the bar
for "safe to skip the model entirely" relative to today's `trivial` /
`frontmatter_only` short-circuits in `classify_pr`. Before that bar goes
anywhere near the live workflow, the honest question is "what would it
actually have done to the last N merged PRs?" — how many PRs that used to
get the free pass now need a real read, and (just as important) how many
PRs that never qualified before would now qualify, because the tightened
bar evaluates each condition independently rather than requiring a single
whole-PR shape ("body-only" vs "frontmatter-only").

This script is read-only analysis, never wired into any workflow: it
replays merged history through both classifiers and reports where they
disagree. No PR is touched, no label is written, no comment is posted.

For each of the last N merged PRs (`--limit`, default 200) it fetches the
PR's file list + diff via `gh api` (paginated), reconstructs the unified
diff shape `triage-classify.py`'s `split_files`/`classify_file` expect, and
computes three verdicts:

  - old_trivial            classify_pr(...)["trivial"]           (v2, today)
  - old_frontmatter_only   classify_pr(...)["frontmatter_only"]   (v2, today)
  - new_mechanical         classify_mechanical(...)               (v3)

`--cache-dir DIR` persists every raw `gh api` response as JSON under DIR, so
a rerun with the same `--cache-dir` needs no network at all — useful for
iterating on the report format, or for a reviewer to audit the exact input
a past run saw. Requests are paced with a small delay between PRs (`--gh-
delay`, default 0.3s) to stay a good citizen of the API even at --limit 200
(roughly 2 `gh api` calls per PR: one for PR detail, one — paginated — for
its file list).

Usage:
    replay-mechanical.py [--repo pulumi/docs] [--limit 200]
        [--cache-dir .replay-cache] [--output report.md]
    replay-mechanical.py --self-test
        Run the report pipeline (fetch → classify → aggregate → render)
        against canned fixture PRs. No network.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import subprocess
import sys
import time
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent.parent
TRIAGE_CLASSIFY_PATH = REPO_ROOT / ".claude" / "commands" / "docs-review" / "scripts" / "triage-classify.py"

DEFAULT_REPO = "pulumi/docs"
DEFAULT_LIMIT = 200
DEFAULT_GH_DELAY = 0.3


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


# Single source of truth for classification — never a second copy of the
# domain rules, the trivial/frontmatter-only bar, or the mechanical bar.
# triage-classify.py's main() is __main__-guarded, so importing it here has
# no side effects (see that module's docstring).
tc = _load("triage_classify_for_replay", TRIAGE_CLASSIFY_PATH)


# ---- gh api fetch layer (cache-first, offline-replayable) -------------------


def _cache_path(cache_dir: Path | None, key: str) -> Path | None:
    if cache_dir is None:
        return None
    return cache_dir / f"{key}.json"


def _read_cache(cache_dir: Path | None, key: str):
    cpath = _cache_path(cache_dir, key)
    if cpath is not None and cpath.exists():
        try:
            return json.loads(cpath.read_text())
        except (OSError, json.JSONDecodeError):
            return None
    return None


def _write_cache(cache_dir: Path | None, key: str, data) -> None:
    cpath = _cache_path(cache_dir, key)
    if cpath is None:
        return
    cpath.parent.mkdir(parents=True, exist_ok=True)
    cpath.write_text(json.dumps(data))


def gh_api_json(endpoint: str, *, cache_dir: Path | None, cache_key: str, paginate: bool = False,
                gh_delay: float = 0.0):
    """`gh api <endpoint>` (optionally `--paginate --slurp`), cache-first.

    `--slurp` wraps every page's JSON array into one outer array, so a
    paginated array-returning endpoint always comes back flattened here
    (one list, not a list of per-page lists) — callers never see the paging
    seam. The pacing delay only applies on an actual cache miss (a real
    network call) — a cache hit is free and shouldn't be throttled.
    """
    cached = _read_cache(cache_dir, cache_key)
    if cached is not None:
        return cached
    cmd = ["gh", "api", endpoint]
    if paginate:
        cmd += ["--paginate", "--slurp"]
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    if proc.returncode != 0:
        raise RuntimeError(f"gh api {endpoint} failed: {proc.stderr.strip()[:300]}")
    data = json.loads(proc.stdout)
    if paginate:
        # --slurp gives [[page1 items...], [page2 items...], ...]; flatten.
        flat = []
        for page in data:
            flat.extend(page)
        data = flat
    _write_cache(cache_dir, cache_key, data)
    if gh_delay:
        time.sleep(gh_delay)
    return data


def list_merged_pr_numbers(repo: str, limit: int, *, cache_dir: Path | None, gh_delay: float) -> list[dict]:
    """The most recent `limit` merged PRs, newest first.

    Walks `/pulls?state=closed&sort=updated&direction=desc` a page at a time
    (state=closed includes both merged and closed-without-merging PRs — the
    list endpoint carries no merged-only filter, so this filters client-side
    on `merged_at`) until `limit` merged PRs are collected or PR history is
    exhausted. Each page is its own cache entry, so a --limit increase on a
    later run only fetches the new pages.
    """
    collected: list[dict] = []
    page = 1
    per_page = 100
    # Generous but bounded: stops a pathological repo (huge unmerged-PR
    # backlog) from paging forever looking for `limit` merged ones.
    max_pages = max(20, (limit // per_page + 1) * 4)
    while len(collected) < limit and page <= max_pages:
        cache_key = f"pulls_list_{repo.replace('/', '_')}_p{page}"
        cached = _read_cache(cache_dir, cache_key)
        if cached is not None:
            items = cached
        else:
            endpoint = (f"repos/{repo}/pulls?state=closed&sort=updated"
                        f"&direction=desc&per_page={per_page}&page={page}")
            cmd = ["gh", "api", endpoint]
            proc = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            if proc.returncode != 0:
                raise RuntimeError(f"gh api pulls list page {page} failed: {proc.stderr.strip()[:300]}")
            items = json.loads(proc.stdout)
            _write_cache(cache_dir, cache_key, items)
            if gh_delay:
                time.sleep(gh_delay)
        if not items:
            break
        for item in items:
            if item.get("merged_at"):
                collected.append(item)
                if len(collected) >= limit:
                    break
        page += 1
    return collected[:limit]


def fetch_pr_files(repo: str, number: int, *, cache_dir: Path | None, gh_delay: float) -> list[dict]:
    endpoint = f"repos/{repo}/pulls/{number}/files?per_page=100"
    return gh_api_json(endpoint, cache_dir=cache_dir, cache_key=f"pr_{number}_files",
                        paginate=True, gh_delay=gh_delay)


# ---- Diff reconstruction -----------------------------------------------------
#
# `gh api .../pulls/{n}/files` returns each file's `patch` as bare hunk text
# (starting at `@@ ...`) — no `diff --git` / `---` / `+++` header. triage-
# classify.py's split_files()/classify_file() parse the full unified-diff
# shape (they need the header to detect renames/new/delete/binary and to
# split multi-file diffs apart), so this rebuilds it per file rather than
# adding a second entry point to triage-classify.py for a headerless patch.


def _file_diff_text(f: dict) -> str:
    filename = f["filename"]
    previous = f.get("previous_filename")
    status = f.get("status")  # added | removed | modified | renamed | copied | changed
    header = [f"diff --git a/{previous or filename} b/{filename}"]
    if status == "renamed" and previous:
        header.append("similarity index 100%")
        header.append(f"rename from {previous}")
        header.append(f"rename to {filename}")
    if status == "added":
        header.append("new file mode 100644")
    if status == "removed":
        header.append("deleted file mode 100644")
    patch = f.get("patch")
    if patch is None:
        # No `patch` field: GitHub omits it for binary files AND for diffs
        # too large to render. We can't tell which from the files API alone,
        # so treat both the same conservative way — mark it binary-shaped so
        # classify_mechanical's structural check (rule 2) fails it rather
        # than silently passing a file whose content we never actually saw.
        header.append("GIT binary patch")
        return "\n".join(header) + "\n"
    old_src = "/dev/null" if status == "added" else f"a/{previous or filename}"
    new_src = "/dev/null" if status == "removed" else f"b/{filename}"
    header.append(f"--- {old_src}")
    header.append(f"+++ {new_src}")
    return "\n".join(header) + "\n" + patch + "\n"


def build_pr_diff(files: list[dict]) -> str:
    return "".join(_file_diff_text(f) for f in files)


def build_pr_data(pr_detail: dict, files: list[dict]) -> dict:
    return {
        "additions": pr_detail.get("additions") or 0,
        "deletions": pr_detail.get("deletions") or 0,
        "files": [{"path": f["filename"]} for f in files],
    }


# ---- Classification -----------------------------------------------------


IS_BOT_SUFFIXES = ("[bot]",)
BOT_LOGINS = {"pulumi-bot"}


def is_bot_author(login: str) -> bool:
    if not login:
        return False
    return login in BOT_LOGINS or any(login.endswith(s) for s in IS_BOT_SUFFIXES)


def classify_one(pr_detail: dict, files: list[dict], repo_root: Path) -> dict:
    diff_text = build_pr_diff(files)
    pr_data = build_pr_data(pr_detail, files)
    file_diffs = tc.split_files(diff_text)
    file_flags = [tc.classify_file(p, d, repo_root=repo_root) for p, d in file_diffs]
    old = tc.classify_pr(pr_data, file_flags)
    new_ok, new_reasons = tc.classify_mechanical(pr_data, file_flags, diff_text, repo_root)

    old_category = "trivial" if old["trivial"] else ("frontmatter_only" if old["frontmatter_only"] else "neither")
    new_label = "mechanical" if new_ok else "substantive"
    author = (pr_detail.get("user") or {}).get("login", "")

    return {
        "number": pr_detail.get("number"),
        "title": pr_detail.get("title", ""),
        "url": pr_detail.get("html_url", ""),
        "author": author,
        "is_bot": is_bot_author(author),
        "merged_at": pr_detail.get("merged_at"),
        "additions": pr_data["additions"],
        "deletions": pr_data["deletions"],
        "file_count": len(files),
        "old_category": old_category,
        "new_mechanical": new_ok,
        "new_label": new_label,
        "new_reasons": new_reasons,
        "transition": f"{old_category}→{new_label}",
        # Everything except "neither -> still substantive" is worth a look:
        # trivial/frontmatter-only losing the shortcut, or "neither" gaining
        # one under the tightened-but-independently-evaluated v3 bar.
        "changed": not (old_category == "neither" and not new_ok),
    }


REASON_CATEGORIES: list[tuple[str, str]] = [
    ("outside domain:docs/domain:blog", "domain"),
    ("new/renamed/deleted/binary", "structural"),
    ("additions (", "additions_cap"),
    ("file count (", "files_cap"),
    ("deletions (", "deletions_cap"),
    ("code fence or shortcode", "code_or_shortcode"),
    ("modified or removed link", "link_removed"),
    ("external/non-internal link added", "link_external"),
    ("does not resolve", "link_unresolved"),
    ("frontmatter key(s) outside", "frontmatter_key"),
    ("pricing-sensitive", "pricing_sensitive"),
    ("claim-extraction signal", "claims_signal"),
]


def categorize_reason(reason: str) -> str:
    for needle, label in REASON_CATEGORIES:
        if needle in reason:
            return label
    return "other"


# ---- Report -----------------------------------------------------------------


def _reason_histogram(records: list[dict]) -> Counter:
    counts: Counter = Counter()
    for r in records:
        cats = {categorize_reason(reason) for reason in r["new_reasons"]}
        for c in cats:
            counts[c] += 1
    return counts


def _fmt_histogram(counts: Counter, total: int) -> str:
    if not counts:
        return "_No reasons recorded._\n"
    lines = ["| reason category | PRs (of {}) |".format(total), "|---|---|"]
    for label, n in counts.most_common():
        lines.append(f"| {label} | {n} |")
    return "\n".join(lines) + "\n"


def render_report(records: list[dict], *, repo: str, limit: int, skipped: list[dict]) -> str:
    total = len(records)
    by_transition: dict[str, list[dict]] = {}
    for r in records:
        by_transition.setdefault(r["transition"], []).append(r)

    def n(transition: str) -> int:
        return len(by_transition.get(transition, []))

    old_counts = Counter(r["old_category"] for r in records)
    bots = [r for r in records if r["is_bot"]]
    humans = [r for r in records if not r["is_bot"]]

    lines: list[str] = []
    lines.append(f"# Mechanical bar replay — {repo}")
    lines.append("")
    lines.append(f"Replayed the last **{total}** merged PRs (requested `--limit {limit}`) through "
                  "`classify_pr` (today's `trivial`/`frontmatter_only` bar) and the v3 "
                  "`classify_mechanical` bar. Read-only — no PR was labeled or touched.")
    lines.append("")
    if skipped:
        lines.append(f"_{len(skipped)} PR(s) skipped (fetch/parse error) — see appendix._")
        lines.append("")
    lines.append(f"Author split: **{len(humans)}** human-authored, **{len(bots)}** bot-authored (of {total}).")
    lines.append("")

    lines.append("## Summary")
    lines.append("")
    lines.append("| Old classification | N | → mechanical | → substantive |")
    lines.append("|---|---|---|---|")
    lines.append(f"| trivial | {old_counts.get('trivial', 0)} | {n('trivial→mechanical')} | {n('trivial→substantive')} |")
    lines.append(f"| frontmatter-only | {old_counts.get('frontmatter_only', 0)} | {n('frontmatter_only→mechanical')} | {n('frontmatter_only→substantive')} |")
    lines.append(f"| neither | {old_counts.get('neither', 0)} | {n('neither→mechanical')} | {n('neither→substantive')} |")
    lines.append("")

    lines.append(f"### Why trivial→substantive PRs failed (N={n('trivial→substantive')})")
    lines.append("")
    lines.append(_fmt_histogram(_reason_histogram(by_transition.get("trivial→substantive", [])),
                                 n("trivial→substantive")))

    lines.append(f"### Why frontmatter-only→substantive PRs failed (N={n('frontmatter_only→substantive')})")
    lines.append("")
    lines.append(_fmt_histogram(_reason_histogram(by_transition.get("frontmatter_only→substantive", [])),
                                 n("frontmatter_only→substantive")))

    changed = [r for r in records if r["changed"]]
    lines.append(f"## Per-PR appendix — classification changed (N={len(changed)})")
    lines.append("")
    if not changed:
        lines.append("_No PR's classification changed._")
        lines.append("")
    else:
        lines.append("| # | Title | Author | Old | New | Reasons |")
        lines.append("|---|---|---|---|---|---|")
        for r in sorted(changed, key=lambda r: r["number"] or 0, reverse=True):
            title = (r["title"] or "").replace("|", "\\|")[:80]
            author = r["author"] + (" 🤖" if r["is_bot"] else "")
            reasons = "; ".join(r["new_reasons"]) or "—"
            reasons = reasons.replace("|", "\\|")
            if len(reasons) > 200:
                reasons = reasons[:197] + "..."
            lines.append(f"| [#{r['number']}]({r['url']}) | {title} | {author} | "
                          f"{r['old_category']} | {r['new_label']} | {reasons} |")
        lines.append("")

    if skipped:
        lines.append(f"## Skipped ({len(skipped)})")
        lines.append("")
        lines.append("| # | reason |")
        lines.append("|---|---|")
        for s in skipped:
            lines.append(f"| #{s.get('number', '?')} | {s.get('error', '')} |")
        lines.append("")

    return "\n".join(lines) + "\n"


# ---- Driver -----------------------------------------------------------------


def run(repo: str, limit: int, cache_dir: Path | None, repo_root: Path, gh_delay: float) -> tuple[list[dict], list[dict]]:
    pr_list = list_merged_pr_numbers(repo, limit, cache_dir=cache_dir, gh_delay=gh_delay)
    records: list[dict] = []
    skipped: list[dict] = []
    for item in pr_list:
        number = item["number"]
        try:
            detail_key = f"pr_{number}_detail"
            detail = _read_cache(cache_dir, detail_key)
            if detail is None:
                cmd = ["gh", "api", f"repos/{repo}/pulls/{number}"]
                proc = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
                if proc.returncode != 0:
                    raise RuntimeError(f"gh api pulls/{number} failed: {proc.stderr.strip()[:300]}")
                detail = json.loads(proc.stdout)
                _write_cache(cache_dir, detail_key, detail)
                if gh_delay:
                    time.sleep(gh_delay)
            files = fetch_pr_files(repo, number, cache_dir=cache_dir, gh_delay=gh_delay)
            records.append(classify_one(detail, files, repo_root))
        except Exception as e:  # noqa: BLE001 — one bad PR must not kill the run
            skipped.append({"number": number, "error": f"{type(e).__name__}: {e}"})
    return records, skipped


# ---- Self-test ----------------------------------------------------------------


def _fixture_pr(number: int, title: str, author: str, additions: int, deletions: int,
                 files: list[dict]) -> tuple[dict, list[dict]]:
    detail = {
        "number": number, "title": title, "html_url": f"https://github.com/pulumi/docs/pull/{number}",
        "user": {"login": author}, "merged_at": "2026-08-01T00:00:00Z",
        "additions": additions, "deletions": deletions,
    }
    return detail, files


def _patch_body(path: str, lines: list[str], old_start=40, new_start=40) -> dict:
    added = sum(1 for l in lines if l.startswith("+"))
    removed = sum(1 for l in lines if l.startswith("-"))
    ctx = sum(1 for l in lines if l.startswith(" "))
    header = f"@@ -{old_start},{removed + ctx} +{new_start},{added + ctx} @@"
    return {"filename": path, "status": "modified", "additions": added, "deletions": removed,
            "patch": header + "\n" + "\n".join(lines)}


def self_test() -> int:
    failures: list[str] = []

    def check(cond: bool, msg: str) -> None:
        if not cond:
            failures.append(msg)
            print(f"  FAIL: {msg}", file=sys.stderr)

    repo_root = REPO_ROOT  # a real content/ tree — used for link resolution

    fixtures: list[tuple[dict, list[dict]]] = []

    # 1) trivial -> mechanical: a tiny clean docs body change.
    fixtures.append(_fixture_pr(
        1, "Fix a typo", "alice", 1, 0,
        [_patch_body("content/docs/foo.md", [
            " Some existing paragraph text stays here for context.",
            "+This section explains how stacks organize resources across environments.",
            " Another existing paragraph stays here too for context.",
        ])],
    ))

    # 2) trivial (old) -> substantive (new): 15 deletions, uncapped under v2
    #    trivial (which never looked at deletions) but over v3's new 30-line
    #    deletions cap... actually keep this one at 31 to guarantee it trips
    #    the new deletions cap specifically (v2 trivial requires additions<=10
    #    and doesn't count deletions at all, so a docs file with 0 additions
    #    and 31 deletions is v2-trivial-eligible on every OTHER axis but
    #    isn't literally "trivial" unless it also has <=2 files and no
    #    frontmatter/link/code changes — build it to hit only the deletions
    #    cap).
    del_lines = [f"-Filler paragraph number {i} for the mechanical test fixture." for i in range(1, 32)]
    fixtures.append(_fixture_pr(
        2, "Remove a stale section", "bob", 0, 31,
        [_patch_body("content/docs/bar.md", del_lines)],
    ))

    # 3) frontmatter-only -> mechanical: an `updated` bump alone... except
    #    Layer A's numeric-range regex reads a YYYY-MM-DD date as a numeric
    #    claim (documented in triage-classify.py / test_triage_classify_
    #    mechanical.py), so use a tags-only change instead to land cleanly
    #    in frontmatter-only (old) -> mechanical (new).
    fixtures.append(_fixture_pr(
        3, "Add a tag", "carol", 2, 1,
        [_patch_body("content/docs/baz.md", [
            " title: Something",
            " tags:",
            "-  - iac",
            "+  - iac",
            "+  - stacks",
            " ---",
            " ",
        ], old_start=5, new_start=5)],
    ))

    # 4) frontmatter-only (old) -> substantive (new): a `title` change is
    #    frontmatter-only under v2 (no body change) but outside v3's
    #    {updated, tags} allow-list.
    fixtures.append(_fixture_pr(
        4, "Reword the page title", "dave", 1, 1,
        [_patch_body("content/docs/qux.md", [
            "-title: Old title",
            "+title: Renamed title",
            " meta_desc: Something",
            " ---",
            " ",
        ], old_start=5, new_start=5)],
    ))

    # 5) neither (old) -> mechanical (new): a small body change *and* an
    #    allowed-key frontmatter change together — v2 fails both trivial (has
    #    a frontmatter change) and frontmatter-only (has a body change), so
    #    it's "neither"; v3 evaluates each condition independently and
    #    allows both.
    fixtures.append(_fixture_pr(
        5, "Tweak wording and bump tags", "eve", 3, 1,
        [_patch_body("content/docs/mixed.md", [
            " title: Something",
            " tags:",
            "-  - iac",
            "+  - iac",
            "+  - stacks",
            " ---",
            " ",
        ], old_start=5, new_start=5),
         _patch_body("content/docs/mixed.md", [
            " Some existing paragraph text stays here for context.",
            "+A short added sentence for the mixed-change fixture.",
            " Another existing paragraph stays here too for context.",
        ])],
    ))
    # Fold the two hunks of the same file into one files-list entry with a
    # combined patch, matching what the GitHub files API actually returns
    # (one entry per file, patch = every hunk concatenated).
    detail5, files5 = fixtures[4]
    combined_patch = files5[0]["patch"] + "\n" + files5[1]["patch"]
    files5 = [{"filename": "content/docs/mixed.md", "status": "modified",
               "additions": 2, "deletions": 1, "patch": combined_patch}]
    fixtures[4] = (detail5, files5)

    # 6) A bot-authored PR (dependabot-shaped login) stays classified
    #    correctly and is counted in the bot split.
    fixtures.append(_fixture_pr(
        6, "Bump some dependency", "dependabot[bot]", 1, 1,
        [_patch_body("content/docs/dep.md", [
            " Some existing paragraph text stays here for context.",
            "+A short added sentence for the bot fixture.",
            " Another existing paragraph stays here too for context.",
        ])],
    ))

    # 7) neither -> substantive (unchanged, boring): a large body change.
    big_lines = [f"+Filler paragraph number {i} for the mechanical test fixture." for i in range(1, 20)]
    fixtures.append(_fixture_pr(
        7, "Rewrite the whole guide", "frank", 19, 0,
        [_patch_body("content/docs/big.md", big_lines)],
    ))

    records = [classify_one(detail, files, repo_root) for detail, files in fixtures]

    by_num = {r["number"]: r for r in records}
    check(by_num[1]["transition"] == "trivial→mechanical", f"PR1: {by_num[1]['transition']}")
    check(by_num[2]["old_category"] == "trivial" and by_num[2]["new_mechanical"] is False,
          f"PR2: old={by_num[2]['old_category']} new_mechanical={by_num[2]['new_mechanical']}")
    check(any("deletions" in r for r in by_num[2]["new_reasons"]), f"PR2 reasons: {by_num[2]['new_reasons']}")
    check(by_num[3]["transition"] == "frontmatter_only→mechanical", f"PR3: {by_num[3]['transition']}")
    check(by_num[4]["transition"] == "frontmatter_only→substantive", f"PR4: {by_num[4]['transition']}")
    check(any("frontmatter key" in r for r in by_num[4]["new_reasons"]), f"PR4 reasons: {by_num[4]['new_reasons']}")
    check(by_num[5]["transition"] == "neither→mechanical", f"PR5: {by_num[5]['transition']}")
    check(by_num[6]["is_bot"] is True, "PR6 (dependabot[bot]) detected as bot")
    check(by_num[7]["transition"] == "neither→substantive", f"PR7: {by_num[7]['transition']}")
    check(by_num[7]["changed"] is False, "PR7 (neither->substantive) is NOT in the changed set")
    check(by_num[1]["changed"] is True, "PR1 IS in the changed set")

    report = render_report(records, repo="pulumi/docs", limit=len(records), skipped=[])
    check("Mechanical bar replay" in report, "report has a title")
    # trivial: PR1 (->mechanical), PR2 (->substantive), PR6 (the bot fixture,
    # a one-line body add, is itself old-trivial too -> mechanical).
    check("| trivial | 3 | 2 | 1 |" in report, f"summary row for trivial (3 total, 2->mech, 1->subst) missing.\n{report}")
    check("| frontmatter-only | 2 | 1 | 1 |" in report, "summary row for frontmatter-only missing")
    check("| neither | 2 | 1 | 1 |" in report, "summary row for neither missing")
    check("**1** bot-authored" in report, "bot split line missing/wrong")
    # PR7 (neither->substantive, unchanged) must not appear in the appendix table.
    appendix_start = report.index("Per-PR appendix")
    appendix = report[appendix_start:]
    check("#7" not in appendix, "unchanged PR7 is excluded from the appendix")
    check("#1" in appendix and "#5" in appendix, "changed PRs 1 and 5 appear in the appendix")

    print(f"\n{len(records)} fixture PR(s) classified, {len(failures)} failure(s).")
    return 1 if failures else 0


# ---- Entry point --------------------------------------------------------------


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--repo", default=DEFAULT_REPO, help=f"owner/repo (default {DEFAULT_REPO})")
    p.add_argument("--limit", type=int, default=DEFAULT_LIMIT, help=f"merged PRs to replay (default {DEFAULT_LIMIT})")
    p.add_argument("--cache-dir", help="directory to cache raw gh api responses; reruns with the same dir are offline")
    p.add_argument("--output", help="write the markdown report here (default: stdout)")
    p.add_argument("--repo-root", default=str(REPO_ROOT), help=argparse.SUPPRESS)
    p.add_argument("--gh-delay", type=float, default=DEFAULT_GH_DELAY,
                   help=f"seconds to sleep between gh api calls (default {DEFAULT_GH_DELAY})")
    p.add_argument("--self-test", action="store_true", help="run canned fixtures, no network")
    args = p.parse_args()

    if args.self_test:
        return self_test()

    cache_dir = Path(args.cache_dir).resolve() if args.cache_dir else None
    repo_root = Path(args.repo_root).resolve()

    records, skipped = run(args.repo, args.limit, cache_dir, repo_root, args.gh_delay)
    report = render_report(records, repo=args.repo, limit=args.limit, skipped=skipped)

    if args.output:
        Path(args.output).write_text(report)
        print(f"replay-mechanical: {len(records)} PR(s) classified, {len(skipped)} skipped → {args.output}",
              file=sys.stderr)
    else:
        print(report)
    return 0


if __name__ == "__main__":
    sys.exit(main())
