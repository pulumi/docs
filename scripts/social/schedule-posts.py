#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "boto3",
#     "python-frontmatter",
#     "requests",
#     "pulumi-social-core @ git+https://github.com/pulumi/social.git@v0.1.0",
# ]
# ///

"""
Schedule social media posts for new blog content via upload-post.com.

Thin wrapper over pulumi-social-core. This module owns docs-specific config
and Hugo blog-post parsing; everything else (state, API calls, PR comments,
char-limit checks, retries) lives in social_core.

Runs via schedule-social.yml after successful builds. social_core selects
posts whose frontmatter date is due (today, within max_age_days) and not yet
posted (per S3 state), extracts social copy from frontmatter, and posts to X,
LinkedIn, and Bluesky on the day — the blog is already live because this runs
after Build and deploy, so the URL liveness check passes.

See the upstream social_core module for scheduling, idempotency, and error
handling details: https://github.com/pulumi/social
"""

import argparse
import os
import sys
from pathlib import Path

import frontmatter

from social_core import (
    PostEntry,
    SchedulerConfig,
    run_check,
    run_post_file,
    run_schedule,
)


# --- Account / API target ----------------------------------------------------
# Flip to True when ready to post to official Pulumi accounts.
PROD_MODE = True

if PROD_MODE:
    USER = "pulumi"
    LINKEDIN_PAGE_ID = "18103664"
else:
    USER = "pulumi-test"
    LINKEDIN_PAGE_ID = "113012346"

SITE_URL = "https://www.pulumi.com"
POSTS_GLOB = "content/blog/*/index.md"

# Frontmatter uses "twitter" for familiarity, but the API platform is "x".
PLATFORM_KEYS = {"twitter": "x", "linkedin": "linkedin", "bluesky": "bluesky"}


# --- docs-specific entry building -------------------------------------------

def _slug_from_path(filepath: str) -> str:
    """content/blog/my-post/index.md -> /blog/my-post/"""
    idx = filepath.find("content/blog/")
    if idx >= 0:
        filepath = filepath[idx:]
    slug = filepath.replace("content/blog/", "").replace("/index.md", "")
    return f"/blog/{slug}/"


def _post_url_from_path(filepath: str) -> str:
    """content/blog/my-post/index.md -> https://www.pulumi.com/blog/my-post/"""
    return f"{SITE_URL}{_slug_from_path(filepath)}"


def _meta_image_path(filepath: str) -> str | None:
    """Find the meta image sibling to a blog post. Returns path or None."""
    blog_dir = Path(filepath).parent
    for name in ["meta.png", "meta.jpg"]:
        img = blog_dir / name
        if img.exists():
            return str(img)
    return None


def build_entries(changed: list[str]) -> list[PostEntry]:
    """Parse Hugo blog posts into PostEntry records for social_core.

    Always returns an entry per existing file, even when social copy is
    missing — downstream run_check emits a structured "NO social copy"
    marker that the PR-review CI depends on. run_schedule silently skips
    entries with empty platforms.

    Attaches the meta image as LinkedIn media; X/Bluesky stay text-only
    (the platforms crawl the link_url for their own card rendering).
    """
    entries: list[PostEntry] = []
    for filepath in changed:
        if not Path(filepath).exists():
            print(f"Skipping deleted file: {filepath}")
            continue

        meta = frontmatter.load(filepath).metadata
        social = meta.get("social") or {}
        image_path = _meta_image_path(filepath)

        platforms: dict[str, tuple[str, list[str]]] = {}
        for fm_key, platform in PLATFORM_KEYS.items():
            copy = str(social.get(fm_key) or "").strip()
            if copy.upper() == "TODO":
                copy = ""
            if not copy:
                continue
            if platform == "linkedin" and image_path:
                platforms[platform] = (copy, [image_path])
            else:
                platforms[platform] = (copy, [])

        entries.append(
            PostEntry(
                filepath=filepath,
                slug=_slug_from_path(filepath),
                url=_post_url_from_path(filepath),
                date=meta.get("date"),
                platforms=platforms,
            )
        )
    return entries


# --- config assembly --------------------------------------------------------

def _build_config() -> SchedulerConfig:
    return SchedulerConfig(
        api_key=os.environ.get("UPLOAD_POST_API_KEY", ""),
        user=USER,
        linkedin_page_id=LINKEDIN_PAGE_ID,
        state_bucket=os.environ.get("SOCIAL_STATE_BUCKET", ""),
        github_repo=os.environ.get("GITHUB_REPOSITORY", "pulumi/docs"),
        github_token=os.environ.get("GITHUB_TOKEN", ""),
        posts_glob=POSTS_GLOB,
        build_entries=build_entries,
        posting_hour=int(os.environ.get("SOCIAL_POSTING_HOUR", "10")),
        posting_tz=os.environ.get("SOCIAL_POSTING_TZ", "America/New_York"),
        dry_run=os.environ.get("DRY_RUN", "false").lower() == "true",
        site_url=SITE_URL,
    )


# --- CLI --------------------------------------------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Schedule social media posts for blog content")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--post", metavar="FILE",
        help="Post a single file directly (bypasses git diff and state)",
    )
    mode.add_argument(
        "--check", action="store_true",
        help="Check mode: validate pending posts without publishing",
    )
    parser.add_argument(
        "--platform", action="append", choices=["x", "linkedin", "bluesky"],
        help="Limit to specific platform(s) (can be repeated; --post only)",
    )
    args = parser.parse_args()

    cfg = _build_config()

    if args.check:
        base_ref = os.environ.get("BASE_REF", "origin/master")
        sys.exit(run_check(cfg, base_ref))
    elif args.post:
        sys.exit(run_post_file(cfg, args.post, platforms_filter=args.platform))
    else:
        sys.exit(run_schedule(cfg))
