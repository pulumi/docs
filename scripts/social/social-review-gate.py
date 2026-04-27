#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml>=6.0"]
# ///
"""Decide whether to skip a social-media-review run.

Skip when no blog file's `social:` frontmatter block changed between the
prior reviewed SHA and the current head SHA. Comparison is on the parsed
YAML subtree, so cosmetic diffs (whitespace, key order, comment additions,
block-style changes) do not trigger a re-review.

Output: JSON to stdout. Caller reads `should_skip` and `reason`.
"""

import argparse
import json
import subprocess
import sys

import yaml


def git_show(repo, sha, path):
    r = subprocess.run(
        ["git", "-C", repo, "show", f"{sha}:{path}"],
        capture_output=True, text=True,
    )
    return r.stdout if r.returncode == 0 else None


def parse_social(content):
    if content is None:
        return None
    if not content.startswith("---\n"):
        return {}
    end = content.find("\n---\n", 4)
    if end == -1:
        return {}
    try:
        fm = yaml.safe_load(content[4:end]) or {}
    except yaml.YAMLError:
        return {}
    return fm.get("social", {}) or {}


def changed_blog_files(repo, prior, head, prefix="content/blog/"):
    r = subprocess.run(
        ["git", "-C", repo, "diff", "--name-only", prior, head],
        capture_output=True, text=True, check=True,
    )
    return [
        f for f in r.stdout.splitlines()
        if f.startswith(prefix) and f.endswith("/index.md")
    ]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--prior", required=True)
    ap.add_argument("--head", required=True)
    args = ap.parse_args()

    files = changed_blog_files(args.repo, args.prior, args.head)
    result = {
        "should_skip": True,
        "reason": "",
        "blog_files_changed": files,
        "social_changed_in": [],
    }

    if not files:
        result["reason"] = "no blog files changed since prior review"
        print(json.dumps(result, indent=2))
        return 0

    for f in files:
        prior_social = parse_social(git_show(args.repo, args.prior, f))
        head_social = parse_social(git_show(args.repo, args.head, f))
        if prior_social is None:
            result["social_changed_in"].append(
                {"file": f, "reason": "new file (no prior version)"}
            )
            continue
        if prior_social != head_social:
            result["social_changed_in"].append(
                {"file": f, "reason": "social block differs"}
            )

    if result["social_changed_in"]:
        result["should_skip"] = False
        result["reason"] = "social block changed in one or more blog files"
    else:
        result["reason"] = (
            f"{len(files)} blog file(s) changed, but social block unchanged"
        )

    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
