#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "boto3",
#     "python-frontmatter",
#     "requests",
# ]
# ///

"""
Schedule social media posts for new blog content via upload-post.com.

Runs via a separate workflow (schedule-social.yml) triggered after
successful builds. Detects new or updated blog posts by diffing from the
last-processed commit SHA (stored in S3 state), extracts social copy from
frontmatter, and schedules posts to X, LinkedIn, and Bluesky.

Platform strategy:
  - X: Text post with URL in the body text. X crawls the URL in the tweet
    to render a link card with og:image. Do NOT also send link_url or
    upload-post.com creates a two-tweet thread.
  - Bluesky: Text post with link_url for card crawling (URL not in body).
  - LinkedIn: Photo post with the blog's meta image attached and URL in
    body. LinkedIn doesn't render link cards via upload-post.com's
    link_url, so we send the image explicitly. Uses upload_photos endpoint.

Scheduling logic:
  - Uses the Hugo post's frontmatter date to determine when to post.
  - Future-dated posts are scheduled for that date at SOCIAL_POSTING_HOUR
    (default: 10am Eastern).
  - Posts dated today or earlier are posted immediately.
  - Posts older than MAX_AGE_DAYS (2) are skipped entirely.

Idempotency:
  - State is tracked in an S3 JSON file (SOCIAL_STATE_BUCKET/posted.json).
  - The state file stores both posted slug+platform combos and the last
    processed commit SHA, making the script self-contained.
  - Before posting, the script checks whether a slug+platform combo has
    already been posted. After a successful post, the entry is recorded.
  - Fails closed: if state cannot be loaded, the script aborts rather
    than risk double-posting.

Required environment variables:
  UPLOAD_POST_API_KEY       - API key from upload-post.com
  SOCIAL_STATE_BUCKET       - S3 bucket for tracking posted state

Optional:
  DRY_RUN                   - Set to "true" to log without posting
  SOCIAL_POSTING_HOUR       - Hour to schedule posts (default: 10, i.e. 10am)
  SOCIAL_POSTING_TZ         - Timezone (default: America/New_York)

TODO:
  1. Once upload-post.com fixes LinkedIn link card crawling, switch
     LinkedIn to upload_text with link_url (like Bluesky).
  2. Flip PROD_MODE = True and connect official Pulumi accounts.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
from collections import defaultdict
from datetime import datetime, date, timedelta, timezone
from pathlib import Path
from typing import Any, Literal

import boto3
import frontmatter
import requests

Platform = Literal["x", "linkedin", "bluesky"]
PostResult = str | bool | None  # URL string, True (dry run), or None (failure)
State = dict[str, Any]

API_KEY = os.environ.get("UPLOAD_POST_API_KEY", "")
DRY_RUN = os.environ.get("DRY_RUN", "false").lower() == "true"
STATE_BUCKET = os.environ.get("SOCIAL_STATE_BUCKET", "")
STATE_KEY = "posted.json"

# --- Configuration ---
# Flip to True when ready to post to official Pulumi accounts.
PROD_MODE = False

if PROD_MODE:
    USER = "pulumi"
    LINKEDIN_PAGE_ID = "18103664"
else:
    USER = "pulumi-test"
    LINKEDIN_PAGE_ID = "113012346"

X_ENABLED = True
LINKEDIN_ENABLED = True
BLUESKY_ENABLED = True

PLATFORM_ENABLED = {
    "x": X_ENABLED,
    "linkedin": LINKEDIN_ENABLED,
    "bluesky": BLUESKY_ENABLED,
}

API_BASE = "https://api.upload-post.com"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
GITHUB_REPO = os.environ.get("GITHUB_REPOSITORY", "pulumi/docs")
SITE_URL = "https://www.pulumi.com"
POSTING_HOUR = int(os.environ.get("SOCIAL_POSTING_HOUR", "10"))
POSTING_TZ = os.environ.get("SOCIAL_POSTING_TZ", "America/New_York")

# Posts with dates older than this many days are skipped
MAX_AGE_DAYS = 2

# Platform character limits.
CHAR_LIMITS = {
    "x": 280,
    "bluesky": 300,
    "linkedin": 3000,
}

# Frontmatter uses "twitter" for familiarity, but the API platform is "x".
PLATFORM_KEYS = {"twitter": "x", "linkedin": "linkedin", "bluesky": "bluesky"}


# --- S3 state management ---

def load_state() -> State:
    """Load posted state from S3. Aborts on errors to prevent double-posting."""
    if not STATE_BUCKET:
        if DRY_RUN:
            print("  DRY RUN: no state bucket, using empty state")
            return {"posts": {}}
        print("Error: SOCIAL_STATE_BUCKET must be set.")
        sys.exit(1)
    s3 = boto3.client("s3")
    try:
        resp = s3.get_object(Bucket=STATE_BUCKET, Key=STATE_KEY)
        return json.loads(resp["Body"].read())
    except s3.exceptions.NoSuchKey:
        return {"posts": {}}
    except Exception as e:
        if DRY_RUN:
            print(f"  DRY RUN: could not load state ({e}), using empty state")
            return {"posts": {}}
        print(f"Error: could not load state from S3: {e}")
        print("Aborting to prevent duplicate posts. Will retry on next deploy.")
        sys.exit(1)


def save_state(state: State) -> None:
    """Save posted state to S3. Fails hard to prevent duplicate posts on next run."""
    if not STATE_BUCKET:
        return
    try:
        s3 = boto3.client("s3")
        s3.put_object(
            Bucket=STATE_BUCKET,
            Key=STATE_KEY,
            Body=json.dumps(state, indent=2),
            ContentType="application/json",
        )
        print(f"  State saved to s3://{STATE_BUCKET}/{STATE_KEY}")
    except Exception as e:
        print(f"Error: could not save state to S3: {e}")
        print("Posts were sent but state was NOT saved. Fix manually to prevent duplicates.")
        sys.exit(1)


MAX_RETRIES = 3


def is_posted(state: State, slug: str, platform: Platform) -> bool:
    """Check if a slug+platform combo has already been posted."""
    return platform in state.get("posts", {}).get(slug, {})


def is_abandoned(state: State, slug: str) -> bool:
    """Check if a post has exceeded the retry limit."""
    return state.get("posts", {}).get(slug, {}).get("_failures", 0) >= MAX_RETRIES


def record_posted(state: State, slug: str, platform: Platform) -> None:
    """Record that a slug+platform combo has been posted."""
    if slug not in state["posts"]:
        state["posts"][slug] = {}
    state["posts"][slug][platform] = datetime.now(timezone.utc).isoformat()


def record_failure(state: State, slug: str) -> None:
    """Increment the failure count for a post."""
    if slug not in state["posts"]:
        state["posts"][slug] = {}
    state["posts"][slug]["_failures"] = state["posts"][slug].get("_failures", 0) + 1


def slug_from_path(filepath: str) -> str:
    """content/blog/my-post/index.md -> /blog/my-post/"""
    slug = filepath.replace("content/blog/", "").replace("/index.md", "")
    return f"/blog/{slug}/"


# --- Blog post detection ---

def get_head_sha() -> str | None:
    """Get the current HEAD commit SHA."""
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        capture_output=True,
        text=True,
    )
    return result.stdout.strip() if result.returncode == 0 else None


def get_changed_blog_posts(state: State) -> list[str] | None:
    """Find blog posts added or modified since the last processed commit.

    Uses last_sha from the S3 state file to diff against HEAD. This makes the
    script self-contained — it doesn't depend on the push event context, so it
    works with workflow_run, workflow_dispatch, or cron triggers.

    Falls back to HEAD~20 if no last_sha is stored (first run). The 2-day
    age check limits what actually gets posted.
    """
    base = state.get("last_sha", "HEAD~20")
    result = subprocess.run(
        ["git", "diff", "--name-only", base, "HEAD", "--", "content/blog/*/index.md"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"Warning: git diff from {base} failed, falling back to HEAD~20")
        result = subprocess.run(
            ["git", "diff", "--name-only", "HEAD~20", "HEAD", "--", "content/blog/*/index.md"],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            print(f"Error: git diff failed: {result.stderr.strip()}")
            return None
    return [f for f in result.stdout.strip().split("\n") if f]


def parse_post(filepath: str) -> dict[str, Any]:
    """Extract frontmatter from a blog post."""
    return frontmatter.load(filepath).metadata


def post_url_from_path(filepath: str) -> str:
    """content/blog/my-post/index.md -> https://www.pulumi.com/blog/my-post/"""
    slug = filepath.replace("content/blog/", "").replace("/index.md", "")
    return f"{SITE_URL}/blog/{slug}/"


def meta_image_path(filepath: str) -> str | None:
    """Find the meta image for a blog post. Returns path or None."""
    blog_dir = Path(filepath).parent
    for name in ["meta.png", "meta.jpg"]:
        img = blog_dir / name
        if img.exists():
            return str(img)
    return None


def find_pr_number(filepath: str, since_sha: str | None = None) -> int | None:
    """Find the PR number that introduced a file.

    Uses the GitHub API to find the most recent commit that touched the file,
    then looks up which PR that commit belongs to. This works reliably on
    reruns (unlike git log parsing, which depends on the SHA range).

    Falls back to git log commit message parsing if the API is unavailable.
    """
    if GITHUB_TOKEN:
        try:
            # Find the most recent commit that touched this file
            resp = requests.get(
                f"https://api.github.com/repos/{GITHUB_REPO}/commits",
                headers={
                    "Authorization": f"token {GITHUB_TOKEN}",
                    "Accept": "application/vnd.github+json",
                },
                params={"path": filepath, "per_page": 1},
                timeout=10,
            )
            if resp.ok and resp.json():
                sha = resp.json()[0]["sha"]
                # Find PRs associated with this commit
                pr_resp = requests.get(
                    f"https://api.github.com/repos/{GITHUB_REPO}/commits/{sha}/pulls",
                    headers={
                        "Authorization": f"token {GITHUB_TOKEN}",
                        "Accept": "application/vnd.github+json",
                    },
                    timeout=10,
                )
                if pr_resp.ok and pr_resp.json():
                    return pr_resp.json()[0]["number"]
        except Exception as e:
            print(f"  Warning: GitHub API PR lookup failed ({e}), falling back to git log")

    # Fallback: parse commit messages for (#NNN)
    if since_sha:
        result = subprocess.run(
            ["git", "log", f"{since_sha}..HEAD", "--pretty=format:%s", "--", filepath],
            capture_output=True,
            text=True,
        )
        if result.returncode == 0 and result.stdout:
            for line in result.stdout.strip().split("\n"):
                match = re.search(r"\(#(\d+)\)", line)
                if match:
                    return int(match.group(1))

    result = subprocess.run(
        ["git", "log", "--pretty=format:%s", "-1", "--", filepath],
        capture_output=True,
        text=True,
    )
    if result.returncode == 0 and result.stdout:
        match = re.search(r"\(#(\d+)\)", result.stdout)
        if match:
            return int(match.group(1))
    return None


def comment_on_pr(pr_number: int, body: str) -> None:
    """Post a comment on a GitHub PR."""
    if not GITHUB_TOKEN:
        print(f"  No GITHUB_TOKEN, skipping PR comment on #{pr_number}")
        return
    resp = requests.post(
        f"https://api.github.com/repos/{GITHUB_REPO}/issues/{pr_number}/comments",
        headers={
            "Authorization": f"token {GITHUB_TOKEN}",
            "Accept": "application/vnd.github+json",
        },
        json={"body": body},
        timeout=30,
    )
    if resp.ok:
        print(f"  Commented on PR #{pr_number}")
    else:
        print(f"  Warning: failed to comment on PR #{pr_number}: {resp.status_code}")


def normalize_date(post_date: date | datetime | str | None) -> date | None:
    """Convert a frontmatter date value to a date object."""
    if isinstance(post_date, datetime):
        return post_date.date()
    if isinstance(post_date, date):
        return post_date
    if isinstance(post_date, str):
        return datetime.fromisoformat(post_date.replace("Z", "+00:00")).date()
    return None


def is_recent_or_future(post_date: date | datetime | str | None) -> bool:
    """Return True if the post date is within MAX_AGE_DAYS of today or in the future."""
    d = normalize_date(post_date)
    if d is None:
        return False
    today = date.today()
    return d >= today - timedelta(days=MAX_AGE_DAYS)


def scheduled_date_from_post(post_date: date | datetime | str | None) -> str | None:
    """Build a scheduled_date ISO string, or None to post immediately."""
    d = normalize_date(post_date)
    if d is None:
        return None
    today = date.today()
    if d <= today:
        return None
    return f"{d}T{POSTING_HOUR:02d}:00:00"


# --- upload-post.com API ---

class PostFailed(Exception):
    """Raised when upload-post.com reports that a post failed."""
    pass


def _poll_for_result(request_id: str, platform: Platform, timeout_secs: int = 120) -> str | None:
    """Poll the status/history API to find the post URL after publishing.

    Polls with exponential backoff (5s, 10s, 20s, ...) up to timeout_secs.
    Raises PostFailed immediately if the API reports the post failed.
    """
    delay = 5
    elapsed = 0
    while elapsed < timeout_secs:
        time.sleep(delay)
        elapsed += delay
        try:
            resp = requests.get(
                f"{API_BASE}/api/uploadposts/status",
                headers={"Authorization": f"Apikey {API_KEY}"},
                params={"request_id": request_id},
                timeout=30,
            )
            if resp.ok:
                data = resp.json()
                for result in data.get("results", []):
                    if result.get("platform") == platform:
                        if result.get("url"):
                            return result["url"]
                        if result.get("success") is False:
                            raise PostFailed(result.get("error") or result.get("error_message") or "unknown error")
        except PostFailed:
            raise
        except Exception:
            pass
        try:
            resp = requests.get(
                f"{API_BASE}/api/uploadposts/history",
                headers={"Authorization": f"Apikey {API_KEY}"},
                timeout=30,
            )
            if resp.ok:
                for entry in resp.json().get("history", []):
                    if entry.get("request_id") == request_id and entry.get("platform") == platform:
                        if entry.get("success") is False:
                            raise PostFailed(entry.get("error_message", "unknown error"))
                        url = entry.get("post_url")
                        if url:
                            return url
        except PostFailed:
            raise
        except Exception:
            pass
        delay = min(delay * 2, 30)
    return None


def _print_result(platform: Platform, request_id: str, scheduled_date: str | None) -> str | None:
    """Print the result of a successful post. Returns the post URL or a fallback string.

    Always returns a truthy value for immediate posts (the API accepted it, so it went out).
    Returns None only if the post failed (API rejected it) — caller should treat as failure.
    """
    if scheduled_date:
        print(f"  ✓ {platform}: scheduled for {scheduled_date} {POSTING_TZ}")
        return "scheduled"
    try:
        post_url = _poll_for_result(request_id, platform)
    except PostFailed as e:
        print(f"  ✗ {platform}: rejected by platform — {e}")
        return None
    if post_url:
        print(f"  ✓ {platform}: {post_url}")
        return post_url
    print(f"  ✓ {platform}: posted (could not retrieve URL, request_id={request_id})")
    return "posted"


def build_payload(platform: Platform, copy: str, url: str, media_paths: list[str], scheduled_date: str | None) -> dict[str, str]:
    """Build the upload-post.com request payload for any platform and media type.

    URL handling per platform:
      - X: URL in body text (X crawls it for a card). Do NOT also send link_url
        or upload-post.com creates a thread.
      - Bluesky (no media): link_url only (not in body text) — renders a card
      - Bluesky (with media): URL in body text (link_url not supported with media)
      - LinkedIn: URL appended to body text (link_url cards don't work)
    """
    bluesky_text_only = platform == "bluesky" and not media_paths
    if url and url not in copy and not bluesky_text_only:
        body = f"{copy}\n\n{url}"
    else:
        body = copy

    data = {
        "user": USER,
        "platform[]": platform,
        "title": body,
    }

    if url and bluesky_text_only:
        data["link_url"] = url

    if platform == "x":
        data["x_title"] = body
    elif platform == "linkedin":
        data["linkedin_description"] = body
        data["visibility"] = "PUBLIC"
        if LINKEDIN_PAGE_ID:
            data["target_linkedin_page_id"] = LINKEDIN_PAGE_ID
    elif platform == "bluesky":
        data["bluesky_title"] = body

    if scheduled_date:
        data["scheduled_date"] = scheduled_date
        data["timezone"] = POSTING_TZ

    return data


def send_post(platform: Platform, data: dict[str, str], media_paths: list[str], scheduled_date: str | None) -> PostResult:
    """Send a post to upload-post.com. Picks endpoint based on media type."""
    videos = [p for p in media_paths if is_video(p)] if media_paths else []
    images = [p for p in media_paths if not is_video(p)] if media_paths else []

    if DRY_RUN:
        kind = "video" if videos else "photos" if images else "text"
        print(f"  [DRY RUN] Would post {kind} to {platform}:")
        for p in videos + images:
            print(f"    media: {p}")
        print(f"    {data.get('title', '')[:100]}...")
        if data.get("link_url"):
            print(f"    link_url: {data['link_url']}")
        print(f"    scheduled: {scheduled_date or 'immediately'}")
        return True

    headers = {"Authorization": f"Apikey {API_KEY}"}

    if videos:
        with open(videos[0], "rb") as f:
            resp = requests.post(
                f"{API_BASE}/api/upload",
                headers=headers,
                data=data,
                files={"video": (os.path.basename(videos[0]), f)},
                timeout=120,
            )
    elif images:
        mime_types = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg",
                      "gif": "image/gif", "webp": "image/webp"}
        opened = []
        files = []
        for p in images:
            ext = Path(p).suffix.lstrip(".").lower()
            f = open(p, "rb")
            opened.append(f)
            files.append(("photos[]", (os.path.basename(p), f, mime_types.get(ext, "image/png"))))
        try:
            resp = requests.post(
                f"{API_BASE}/api/upload_photos",
                headers=headers,
                data=data,
                files=files,
                timeout=60,
            )
        finally:
            for f in opened:
                f.close()
    else:
        resp = requests.post(
            f"{API_BASE}/api/upload_text",
            headers=headers,
            data=data,
            timeout=30,
        )

    if not resp.ok:
        print(f"  FAILED on {platform}: {resp.status_code} {resp.text}")
        return None

    result = resp.json()
    request_id = result.get("request_id", "")

    direct_url = result.get("results", {}).get(platform, {}).get("url")
    if direct_url:
        if scheduled_date:
            print(f"  ✓ {platform}: scheduled for {scheduled_date} {POSTING_TZ}")
        else:
            print(f"  ✓ {platform}: {direct_url}")
        return direct_url

    post_url = _print_result(platform, request_id, scheduled_date)
    return post_url


def is_video(filepath: str | Path) -> bool:
    """Check if a file is a video based on extension."""
    return Path(filepath).suffix.lower() in {".mp4", ".mov", ".avi", ".webm", ".mkv"}


def schedule_post(platform: Platform, copy: str, url: str, media_paths: list[str], scheduled_date: str | None) -> PostResult:
    """Build payload and send a post. Returns post URL or None."""
    data = build_payload(platform, copy, url, media_paths, scheduled_date)
    return send_post(platform, data, media_paths, scheduled_date)


# --- Main ---

def main() -> None:
    if not API_KEY:
        if DRY_RUN:
            print("DRY RUN: API key not set, will show what would be posted.")
        else:
            print("Error: UPLOAD_POST_API_KEY must be set.")
            sys.exit(1)

    state = load_state()

    changed = get_changed_blog_posts(state)
    if changed is None:
        print("Error: could not determine changed blog posts. Aborting.")
        sys.exit(1)
    if not changed:
        print("No blog post changes detected.")
        head = get_head_sha()
        if head and head != state.get("last_sha"):
            state["last_sha"] = head
            save_state(state)
        return

    failures = False
    posted_urls: list[tuple[str, Platform, PostResult]] = []
    posts_by_file: defaultdict[str, list[tuple[Platform, PostResult]]] = defaultdict(list)

    for filepath in changed:
        if not Path(filepath).exists():
            print(f"\nSkipping deleted file: {filepath}")
            continue

        slug = slug_from_path(filepath)

        # Check abandonment before parsing (avoids crash on broken frontmatter)
        if is_abandoned(state, slug):
            print(f"\nSkipping {filepath}: exceeded {MAX_RETRIES} retries")
            continue

        print(f"\nProcessing: {filepath}")
        meta = parse_post(filepath)
        url = post_url_from_path(filepath)
        post_date = meta.get("date")
        social = meta.get("social") or {}
        image_path = meta_image_path(filepath)

        # Skip old posts
        if not post_date or not is_recent_or_future(post_date):
            print(f"  Skipping: date {post_date} is not recent or future")
            continue

        # Build per-platform (copy, media_paths) — LinkedIn gets the meta image,
        # X and Bluesky get text-only posts with link cards.
        platforms: dict[Platform, tuple[str, list[str]]] = {}
        for fm_key, platform in PLATFORM_KEYS.items():
            copy = str(social.get(fm_key) or "").strip()
            if copy.upper() == "TODO":
                copy = ""
            if copy:
                if platform == "linkedin" and image_path:
                    platforms[platform] = (copy, [image_path])
                else:
                    platforms[platform] = (copy, [])

        if not platforms:
            print(f"  Warning: no social copy in frontmatter for {filepath}")
            continue

        scheduled = scheduled_date_from_post(post_date)
        print(f"  URL: {url}")
        if scheduled:
            print(f"  Scheduled for: {scheduled} {POSTING_TZ}")
        else:
            print(f"  Posting immediately (date is today or past)")

        post_had_failure = False
        for platform, (copy, media_paths) in platforms.items():
            if not PLATFORM_ENABLED.get(platform):
                continue

            # Validate character limits.
            # X always appends URL to body text. Media posts on any platform
            # append URL to body. Bluesky text-only posts use link_url instead.
            limit = CHAR_LIMITS.get(platform)
            appends_url = url and url not in copy and (
                platform == "x"
                or (platform == "linkedin" and not media_paths)
                or bool(media_paths)
            )
            if appends_url:
                url_len = 23 if platform == "x" else len(url)
                text_len = len(copy) + 2 + url_len
            else:
                text_len = len(copy)
            if limit and text_len > limit:
                print(f"  SKIPPING {platform}: copy is {text_len} chars, limit is {limit}")
                failures = True
                continue

            if is_posted(state, slug, platform):
                print(f"  Skipping {platform}: already posted (per state file)")
                continue

            post_url = schedule_post(platform, copy, url, media_paths, scheduled)
            if post_url:
                record_posted(state, slug, platform)
                save_state(state)
                posted_urls.append((url, platform, post_url))
                posts_by_file[filepath].append((platform, post_url))
            else:
                post_had_failure = True

        if post_had_failure:
            record_failure(state, slug)
            save_state(state)
            if is_abandoned(state, slug):
                print(f"  Giving up on {slug} after {MAX_RETRIES} failed runs")
            else:
                failures = True

    # Write summary
    if posted_urls:
        print("\n--- Posted ---")
        for blog_url, platform, post_url in posted_urls:
            print(f"  {platform}: {post_url}")

        summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
        if summary_path:
            with open(summary_path, "a") as f:
                f.write("## Social media posts\n\n")
                f.write("| Blog post | Platform | Post |\n")
                f.write("|---|---|---|\n")
                for blog_url, platform, post_url in posted_urls:
                    slug = blog_url.replace(SITE_URL, "")
                    if isinstance(post_url, str) and post_url.startswith("http"):
                        f.write(f"| {slug} | {platform} | [link]({post_url}) |\n")
                    else:
                        f.write(f"| {slug} | {platform} | {post_url} |\n")

        for filepath, results in posts_by_file.items():
            pr_number = find_pr_number(filepath, since_sha=state.get("last_sha"))
            if not pr_number:
                print(f"  Could not find PR for {filepath}, skipping comment")
                continue
            lines = ["📣 Social media posts are live for this blog post:\n"]
            for platform, post_url in results:
                if isinstance(post_url, str) and post_url.startswith("http"):
                    lines.append(f"- **{platform}**: {post_url}")
                else:
                    lines.append(f"- **{platform}**: posted (link not available)")
            comment_on_pr(pr_number, "\n".join(lines))

    if failures:
        print("\nSome posts failed to schedule. Not advancing last_sha so they are retried.")
        print("Successfully posted platforms are recorded and won't be duplicated.")
        sys.exit(1)

    # Only advance last_sha when everything succeeded
    head = get_head_sha()
    if head:
        state["last_sha"] = head
        save_state(state)

    print("\nDone.")


def post_file(filepath: str, platforms_filter: list[Platform] | None = None) -> None:
    """Post a single file directly, bypassing git diff and state.

    Used for testing and one-off posts. No state tracking or PR comments.
    """
    if not API_KEY:
        if DRY_RUN:
            print("DRY RUN: API key not set, will show what would be posted.")
        else:
            print("Error: UPLOAD_POST_API_KEY must be set.")
            sys.exit(1)

    filepath = str(filepath)
    if not Path(filepath).exists():
        print(f"Error: file not found: {filepath}")
        sys.exit(1)

    meta = parse_post(filepath)
    url = post_url_from_path(filepath)
    image_path = meta_image_path(filepath)
    social = meta.get("social") or {}

    platforms: dict[Platform, tuple[str, list[str]]] = {}
    for fm_key, platform in PLATFORM_KEYS.items():
        copy = str(social.get(fm_key) or "").strip()
        if copy.upper() == "TODO":
            copy = ""
        if copy:
            if platform == "linkedin" and image_path:
                platforms[platform] = (copy, [image_path])
            else:
                platforms[platform] = (copy, [])

    if platforms_filter:
        platforms = {p: v for p, v in platforms.items() if p in platforms_filter}

    if not platforms:
        print("No social copy found in file.")
        sys.exit(1)

    post_date = meta.get("date")
    scheduled = scheduled_date_from_post(post_date)

    print(f"Posting: {filepath}")
    print(f"  URL: {url}")
    for platform, (copy, media_paths) in platforms.items():
        print(f"  {platform}: {copy[:80]}...")
        if media_paths:
            for m in media_paths:
                print(f"    media: {m}")

    state: State = {"posts": {}}
    posted_urls: list[tuple[str, Platform, PostResult]] = []

    for platform, (copy, media_paths) in platforms.items():
        if not PLATFORM_ENABLED.get(platform):
            continue
        post_url = schedule_post(platform, copy, url, media_paths, scheduled)
        if post_url:
            posted_urls.append((url, platform, post_url))

    if posted_urls:
        print("\n--- Posted ---")
        for blog_url, platform, post_url in posted_urls:
            print(f"  {platform}: {post_url}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Schedule social media posts for blog content")
    parser.add_argument(
        "--post", metavar="FILE",
        help="Post a single file directly (bypasses git diff and state)",
    )
    parser.add_argument(
        "--platform", action="append", choices=["x", "linkedin", "bluesky"],
        help="Limit to specific platform(s) (can be repeated)",
    )
    args = parser.parse_args()

    if args.post:
        post_file(args.post, platforms_filter=args.platform)
    else:
        main()
