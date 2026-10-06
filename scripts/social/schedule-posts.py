#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "boto3",
#     "python-frontmatter",
#     "requests",
#     "pulumi-social-core @ git+https://github.com/pulumi/social.git@v0.2.0",
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

LinkedIn and Bluesky go through upload-post.com. X goes direct through the X
API

  X_CONSUMER_KEY, X_CONSUMER_SECRET, X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET,
  X_USERNAME (optional; only used to build a nicer permalink)

With PROD_MODE off, the X_TEST_* equivalents are read instead. Missing
credentials make X fall back to the manual-posting notice in the PR comment.

See the upstream social_core module for scheduling, idempotency, and error
handling details: https://github.com/pulumi/social
"""

import argparse
import os
import sys
import tempfile
import time
from pathlib import Path

import frontmatter
import requests

from social_core import (
    PostEntry,
    SchedulerConfig,
    run_check,
    run_post_file,
    run_schedule,
)
from x_client import XCredentials, verify_credentials


# --- Account / API target ----------------------------------------------------
# Flip to True when ready to post to official Pulumi accounts.
PROD_MODE = True

if PROD_MODE:
    USER = "pulumi"
    LINKEDIN_PAGE_ID = "18103664"
else:
    USER = "pulumi-test"
    LINKEDIN_PAGE_ID = "113012346"

X_ENV_PREFIX = "X_" if PROD_MODE else "X_TEST_"

# Go-live gate for direct X API posting
X_DIRECT_API_ENABLED = True

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
    """Local path to the post's titled build-time social card (its og:image).

    We want LinkedIn to show the *titled* card (title + feature image, or a
    generic branded plate) — the same image X/Bluesky get by unfurling the link
    — rather than the untitled feature.png hero. social_core uploads LinkedIn
    media as a multipart file, so this must be a real local file, not a URL.

    The card is a gitignored build artifact absent from this job's checkout, but
    it's live at deploy time (this runs after Build and deploy), so fetch it to a
    temp file. It's keyed by the post's directory path (see
    layouts/partials/meta-image-key.html), which is what _slug_from_path yields —
    not the post's URL slug. Returns None if the card can't be fetched, in which
    case LinkedIn falls back to unfurling the link, which still renders the same
    titled card from og:image.
    """
    slug = _slug_from_path(filepath).strip("/")  # e.g. "blog/my-post"
    url = f"{SITE_URL}/images/generated/{slug}/index.png"
    # The card can briefly 404 while the deploy propagates to the CDN; retry a
    # few times, mirroring social_core's link-liveness backoff.
    for attempt in range(3):
        try:
            resp = requests.get(url, timeout=10)
            if resp.status_code == 200:
                fd, tmp = tempfile.mkstemp(suffix=".png")
                with os.fdopen(fd, "wb") as f:
                    f.write(resp.content)
                return tmp
        except requests.RequestException:
            pass
        if attempt < 2:
            time.sleep(5)
    print(f"  Warning: social card not reachable ({url}); "
          "LinkedIn will fall back to link unfurl")
    return None


def build_entries(changed: list[str]) -> list[PostEntry]:
    """Parse Hugo blog posts into PostEntry records for social_core.

    Always returns an entry per existing file, even when social copy is
    missing — downstream run_check emits a structured "NO social copy"
    marker that the PR-review CI depends on. run_schedule silently skips
    entries with empty platforms.

    Attaches the titled build-time social card (fetched from the live site) as
    LinkedIn media; X/Bluesky stay text-only (the platforms crawl the link_url
    for their own card rendering, which resolves to the same card).
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

def _x_direct_api_enabled() -> bool:
    override = os.environ.get("X_DIRECT_API_ENABLED")
    if override is not None:
        return override.strip().lower() in ("1", "true", "yes")
    return X_DIRECT_API_ENABLED


def _x_credentials() -> XCredentials | None:
    """X OAuth 1.0a credentials, or None when any required secret is missing.

    social_core reads None as "no X posting this run" and falls back to the
    manual-posting notice instead of failing the whole run.
    """
    p = X_ENV_PREFIX
    creds = XCredentials(
        consumer_key=os.environ.get(f"{p}CONSUMER_KEY", ""),
        consumer_secret=os.environ.get(f"{p}CONSUMER_SECRET", ""),
        access_token=os.environ.get(f"{p}ACCESS_TOKEN", ""),
        access_token_secret=os.environ.get(f"{p}ACCESS_TOKEN_SECRET", ""),
        username=os.environ.get(f"{p}USERNAME") or None,
    )
    return creds if creds.complete else None


def run_verify_x(cfg: SchedulerConfig) -> int:
    """Preflight the X credentials so a revoked or rotated token fails the run
    before any posting starts. Disabled or unconfigured X is not a failure."""
    if not cfg.x_direct_api_enabled:
        print("X direct posting is disabled for this run — skipping check.")
        return 0
    if cfg.x_credentials is None:
        print(f"::warning::No complete {X_ENV_PREFIX}* credential set — "
              "X posts will fall back to the manual-posting notice.")
        return 0
    ok, detail = verify_credentials(cfg.x_credentials)
    print(f"X credential check: {detail}")
    return 0 if ok else 1


def _build_config() -> SchedulerConfig:
    return SchedulerConfig(
        api_key=os.environ.get("UPLOAD_POST_API_KEY", ""),
        user=USER,
        linkedin_page_id=LINKEDIN_PAGE_ID,
        x_credentials=_x_credentials(),
        x_direct_api_enabled=_x_direct_api_enabled(),
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
    mode.add_argument(
        "--verify-x", action="store_true",
        help="Verify X API credentials and exit",
    )
    parser.add_argument(
        "--platform", action="append", choices=["x", "linkedin", "bluesky"],
        help="Limit to specific platform(s) (can be repeated; --post only)",
    )
    args = parser.parse_args()

    cfg = _build_config()

    if args.verify_x:
        sys.exit(run_verify_x(cfg))
    elif args.check:
        base_ref = os.environ.get("BASE_REF", "origin/master")
        sys.exit(run_check(cfg, base_ref))
    elif args.post:
        sys.exit(run_post_file(cfg, args.post, platforms_filter=args.platform))
    else:
        sys.exit(run_schedule(cfg))
