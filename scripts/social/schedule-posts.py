#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "python-frontmatter",
#     "requests",
# ]
# ///

"""
Schedule social media posts for new blog content via upload-post.com.

Runs as part of the build-and-deploy workflow after the site deploys.
Detects new or updated blog posts, extracts social copy from frontmatter,
and schedules posts to X (Twitter), LinkedIn, and Bluesky.

Required environment variables:
  UPLOAD_POST_API_KEY       - API key from upload-post.com
  UPLOAD_POST_USER          - Profile username in upload-post.com
  UPLOAD_POST_LINKEDIN_PAGE_ID - LinkedIn organization page ID (optional)

Optional:
  DRY_RUN                   - Set to "true" to log without posting
  SOCIAL_POSTING_HOUR       - Hour to schedule posts (default: 10, i.e. 10am)
  SOCIAL_POSTING_TZ         - Timezone (default: America/New_York)
"""

import os
import subprocess
import sys
from datetime import datetime, date, timedelta

import frontmatter
import requests

API_KEY = os.environ.get("UPLOAD_POST_API_KEY", "")
USER = os.environ.get("UPLOAD_POST_USER", "")
LINKEDIN_PAGE_ID = os.environ.get("UPLOAD_POST_LINKEDIN_PAGE_ID", "")
DRY_RUN = os.environ.get("DRY_RUN", "false").lower() == "true"

API_BASE = "https://api.upload-post.com"
SITE_URL = "https://www.pulumi.com"
POSTING_HOUR = int(os.environ.get("SOCIAL_POSTING_HOUR", "10"))
POSTING_TZ = os.environ.get("SOCIAL_POSTING_TZ", "America/New_York")

# Posts with dates older than this many days are skipped
MAX_AGE_DAYS = 2


def get_changed_blog_posts():
    """Find blog posts added or modified in this push."""
    result = subprocess.run(
        ["git", "diff", "--name-only", "HEAD~1", "HEAD", "--", "content/blog/*/index.md"],
        capture_output=True,
        text=True,
    )
    return [f for f in result.stdout.strip().split("\n") if f]


def parse_post(filepath):
    """Extract frontmatter from a blog post."""
    return frontmatter.load(filepath).metadata


def post_url_from_path(filepath):
    """content/blog/my-post/index.md -> https://www.pulumi.com/blog/my-post/"""
    slug = filepath.replace("content/blog/", "").replace("/index.md", "")
    return f"{SITE_URL}/blog/{slug}/"


def normalize_date(post_date):
    """Convert a frontmatter date value to a date object."""
    if isinstance(post_date, datetime):
        return post_date.date()
    if isinstance(post_date, date):
        return post_date
    if isinstance(post_date, str):
        # Handle "2025-12-09" or "2025-12-09T00:00:00-07:00"
        return datetime.fromisoformat(post_date.replace("Z", "+00:00")).date()
    return None


def is_recent_or_future(post_date):
    """Return True if the post date is within MAX_AGE_DAYS of today or in the future."""
    d = normalize_date(post_date)
    if d is None:
        return False
    today = date.today()
    return d >= today - timedelta(days=MAX_AGE_DAYS)


def scheduled_date_from_post(post_date):
    """Build a scheduled_date ISO string, or None to post immediately.

    Returns None if the post date is today or in the past (post now).
    Returns a future date string if the post date is in the future.
    """
    d = normalize_date(post_date)
    today = date.today()
    if d <= today:
        return None
    return f"{d}T{POSTING_HOUR:02d}:00:00"


def find_scheduled(url):
    """Check if posts with this URL are already scheduled.

    Returns a dict mapping platform -> job_id for matching entries.
    """
    scheduled = {}
    try:
        resp = requests.get(
            f"{API_BASE}/api/uploadposts/schedule",
            headers={"Authorization": f"Apikey {API_KEY}"},
            params={"limit": 50},
        )
        if resp.ok:
            entries = resp.json().get("scheduled_posts", [])
            for entry in entries:
                title = entry.get("title", "") or ""
                if url in title:
                    job_id = entry.get("job_id")
                    for platform in entry.get("platforms", []):
                        if job_id:
                            scheduled[platform] = job_id
    except Exception as e:
        print(f"  Warning: could not check schedule: {e}")
    return scheduled


def already_published(url):
    """Check if a post with this URL has already been published."""
    try:
        resp = requests.get(
            f"{API_BASE}/api/uploadposts/history",
            headers={"Authorization": f"Apikey {API_KEY}"},
        )
        if resp.ok:
            for entry in resp.json().get("history", []):
                title = entry.get("post_title", "") or ""
                if url in title:
                    return True
    except Exception as e:
        print(f"  Warning: could not check history: {e}")
    return False


def schedule_post(platform, title, url, scheduled_date):
    """Schedule a text post via upload-post.com API.

    X/Twitter: URL is appended to text (needed for card unfurling).
    LinkedIn/Bluesky: URL is sent via link_url for a rich preview card.
    """
    data = {
        "user": USER,
        "platform[]": platform,
        "title": f"{title} {url}",
    }
    if scheduled_date:
        data["scheduled_date"] = scheduled_date
        data["timezone"] = POSTING_TZ

    if platform == "twitter":
        text_with_url = f"{title}\n\n{url}"
        data["title"] = text_with_url
        data["x_title"] = text_with_url
    elif platform == "linkedin":
        data["linkedin_title"] = title
        data["linkedin_link_url"] = url
        if LINKEDIN_PAGE_ID:
            data["target_linkedin_page_id"] = LINKEDIN_PAGE_ID
    elif platform == "bluesky":
        data["bluesky_title"] = title
        data["bluesky_link_url"] = url

    if DRY_RUN:
        display = data.get("x_title") or data.get("linkedin_title") or data.get("bluesky_title") or title
        link = data.get("linkedin_link_url") or data.get("bluesky_link_url") or ""
        print(f"  [DRY RUN] Would post to {platform}:")
        print(f"    ---")
        print(f"    {display}")
        if link:
            print(f"    link card: {link}")
        print(f"    ---")
        print(f"    scheduled: {scheduled_date or 'immediately'}")
        return True

    resp = requests.post(
        f"{API_BASE}/api/upload_text",
        headers={"Authorization": f"Apikey {API_KEY}"},
        data=data,
    )

    if resp.ok:
        result = resp.json()
        print(f"  Scheduled on {platform}: request_id={result.get('request_id', 'ok')}")
        return True
    else:
        print(f"  FAILED on {platform}: {resp.status_code} {resp.text}")
        return False


def update_scheduled_post(job_id, platform, copy, url, scheduled_date):
    """Update an existing scheduled post via PATCH."""
    data = {"title": f"{copy} {url}"}
    if scheduled_date:
        data["scheduled_date"] = scheduled_date
        data["timezone"] = POSTING_TZ
    if platform == "twitter":
        text_with_url = f"{copy}\n\n{url}"
        data["title"] = text_with_url
        data["x_title"] = text_with_url
    elif platform == "linkedin":
        data["linkedin_title"] = copy
    elif platform == "bluesky":
        data["bluesky_title"] = copy

    resp = requests.patch(
        f"{API_BASE}/api/uploadposts/schedule/{job_id}",
        headers={"Authorization": f"Apikey {API_KEY}", "Content-Type": "application/json"},
        json=data,
    )
    if resp.ok:
        print(f"  Updated scheduled post (job_id={job_id})")
        return True
    else:
        print(f"  FAILED to update (job_id={job_id}): {resp.status_code} {resp.text}")
        return False


def main():
    if not API_KEY or not USER:
        if DRY_RUN:
            print("DRY RUN: API key/user not set, will show what would be posted.")
        else:
            print("Error: UPLOAD_POST_API_KEY and UPLOAD_POST_USER must be set.")
            sys.exit(1)

    changed = get_changed_blog_posts()
    if not changed:
        print("No blog post changes detected.")
        return

    failures = False

    for filepath in changed:
        print(f"\nProcessing: {filepath}")
        meta = parse_post(filepath)
        url = post_url_from_path(filepath)
        post_date = meta.get("date")
        social = meta.get("social") or {}
        twitter_copy = (social.get("twitter") or "").strip()
        linkedin_copy = (social.get("linkedin") or "").strip()
        bluesky_copy = (social.get("bluesky") or "").strip()

        # Skip old posts
        if not post_date or not is_recent_or_future(post_date):
            print(f"  Skipping: date {post_date} is not recent or future")
            continue

        # Skip TODOs and empty values
        if twitter_copy.upper() == "TODO":
            twitter_copy = ""
        if linkedin_copy.upper() == "TODO":
            linkedin_copy = ""
        if bluesky_copy.upper() == "TODO":
            bluesky_copy = ""

        if not twitter_copy and not linkedin_copy and not bluesky_copy:
            print(f"  Warning: no social copy in frontmatter for {filepath}")
            continue

        # Skip if already published
        if not DRY_RUN and already_published(url):
            print(f"  Skipping: already published {url}")
            continue

        # Check which platforms already have scheduled posts
        existing = {} if DRY_RUN else find_scheduled(url)
        if existing:
            print(f"  Found existing scheduled posts: {existing}")

        scheduled = scheduled_date_from_post(post_date)
        print(f"  URL: {url}")
        if scheduled:
            print(f"  Scheduled for: {scheduled} {POSTING_TZ}")
        else:
            print(f"  Posting immediately (date is today or past)")

        for platform, copy in [("twitter", twitter_copy), ("linkedin", linkedin_copy), ("bluesky", bluesky_copy)]:
            if not copy:
                continue
            job_id = existing.get(platform)
            if job_id:
                if not update_scheduled_post(job_id, platform, copy, url, scheduled):
                    failures = True
            else:
                if not schedule_post(platform, copy, url, scheduled):
                    failures = True

    if failures:
        print("\nSome posts failed to schedule. Check output above.")
        sys.exit(1)

    print("\nDone.")


if __name__ == "__main__":
    main()
