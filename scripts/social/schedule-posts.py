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
  - X/Bluesky: Text post with link_url for card crawling. The platform
    crawls the URL and renders a link card with og:image. No URL needed
    in the post body. Uses upload_text endpoint.
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
  - The state file stores both posted URL+platform combos and the last
    processed commit SHA, making the script self-contained.
  - Before posting, the script checks whether a URL+platform combo has
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
     LinkedIn to upload_text with link_url (like X/Bluesky).
  2. Flip PROD_MODE = True and connect official Pulumi accounts.
"""

import json
import os
import re
import subprocess
import sys
import time
from collections import defaultdict
from datetime import datetime, date, timedelta, timezone
from pathlib import Path

import boto3
import frontmatter
import requests

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


# --- S3 state management ---

def load_state():
    """Load posted state from S3. Aborts on errors to prevent double-posting."""
    if not STATE_BUCKET:
        if DRY_RUN:
            print("  DRY RUN: no state bucket, using empty state")
            return {"posts": {}}
        print("Error: SOCIAL_STATE_BUCKET must be set.")
        sys.exit(1)
    try:
        s3 = boto3.client("s3")
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


def save_state(state):
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


def is_posted(state, slug, platform):
    """Check if a URL+platform combo has already been posted."""
    return platform in state.get("posts", {}).get(slug, {})


def is_abandoned(state, slug):
    """Check if a post has exceeded the retry limit."""
    return state.get("posts", {}).get(slug, {}).get("_failures", 0) >= MAX_RETRIES


def record_posted(state, slug, platform):
    """Record that a URL+platform combo has been posted."""
    if slug not in state["posts"]:
        state["posts"][slug] = {}
    state["posts"][slug][platform] = datetime.now(timezone.utc).isoformat()


def record_failure(state, slug):
    """Increment the failure count for a post."""
    if slug not in state["posts"]:
        state["posts"][slug] = {}
    state["posts"][slug]["_failures"] = state["posts"][slug].get("_failures", 0) + 1


def slug_from_path(filepath):
    """content/blog/my-post/index.md -> /blog/my-post/"""
    slug = filepath.replace("content/blog/", "").replace("/index.md", "")
    return f"/blog/{slug}/"


# --- Blog post detection ---

def get_head_sha():
    """Get the current HEAD commit SHA."""
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        capture_output=True,
        text=True,
    )
    return result.stdout.strip() if result.returncode == 0 else None


def get_changed_blog_posts(state):
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


def parse_post(filepath):
    """Extract frontmatter from a blog post."""
    return frontmatter.load(filepath).metadata


def post_url_from_path(filepath):
    """content/blog/my-post/index.md -> https://www.pulumi.com/blog/my-post/"""
    slug = filepath.replace("content/blog/", "").replace("/index.md", "")
    return f"{SITE_URL}/blog/{slug}/"


def meta_image_path(filepath):
    """Find the meta image for a blog post. Returns path or None."""
    blog_dir = Path(filepath).parent
    for name in ["meta.png", "meta.jpg"]:
        img = blog_dir / name
        if img.exists():
            return str(img)
    return None


def find_pr_number(filepath, since_sha=None):
    """Find the PR number that introduced a blog post file.

    Scopes the search to commits between since_sha and HEAD when available,
    so we find the PR that triggered this run rather than an older one.
    Falls back to the most recent commit touching the file.
    """
    if since_sha:
        result = subprocess.run(
            ["git", "log", f"{since_sha}..HEAD", "--pretty=format:%s", "--", filepath],
            capture_output=True,
            text=True,
        )
        if result.returncode == 0 and result.stdout:
            # Check each commit in the range for a PR number
            for line in result.stdout.strip().split("\n"):
                match = re.search(r"\(#(\d+)\)", line)
                if match:
                    return int(match.group(1))

    # Fall back to most recent commit touching the file
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


def comment_on_pr(pr_number, body):
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


def normalize_date(post_date):
    """Convert a frontmatter date value to a date object."""
    if isinstance(post_date, datetime):
        return post_date.date()
    if isinstance(post_date, date):
        return post_date
    if isinstance(post_date, str):
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
    """Build a scheduled_date ISO string, or None to post immediately."""
    d = normalize_date(post_date)
    if d is None:
        return None
    today = date.today()
    if d <= today:
        return None
    return f"{d}T{POSTING_HOUR:02d}:00:00"


# --- upload-post.com API ---

def _poll_for_result(request_id, platform, retries=4, delay=3):
    """Poll the status/history API to find the post URL after publishing."""
    # Try the status endpoint first (works for upload_photos async responses)
    for _ in range(retries):
        time.sleep(delay)
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
                    if result.get("platform") == platform and result.get("url"):
                        return result["url"]
        except Exception:
            pass
        # Fall back to history
        try:
            resp = requests.get(
                f"{API_BASE}/api/uploadposts/history",
                headers={"Authorization": f"Apikey {API_KEY}"},
                timeout=30,
            )
            if resp.ok:
                for entry in resp.json().get("history", []):
                    if entry.get("request_id") == request_id and entry.get("platform") == platform:
                        url = entry.get("post_url")
                        if url:
                            return url
        except Exception:
            pass
    return None


def _print_result(platform, request_id, scheduled_date):
    """Print the result of a successful post. Returns the post URL if available."""
    if scheduled_date:
        print(f"  ✓ {platform}: scheduled for {scheduled_date} {POSTING_TZ}")
        return None
    post_url = _poll_for_result(request_id, platform)
    if post_url:
        print(f"  ✓ {platform}: {post_url}")
    else:
        print(f"  ✓ {platform}: posted (request_id={request_id})")
    return post_url



def post_text(platform, copy, url, scheduled_date):
    """Post via upload_text. link_url generates a card with og:image — no URL needed in body."""
    data = {
        "user": USER,
        "platform[]": platform,
        "title": copy,
        "link_url": url,
    }
    if platform == "x":
        data["x_title"] = copy
    elif platform == "bluesky":
        data["bluesky_title"] = copy
    if scheduled_date:
        data["scheduled_date"] = scheduled_date
        data["timezone"] = POSTING_TZ

    if DRY_RUN:
        print(f"  [DRY RUN] Would post text to {platform}:")
        print(f"    {copy[:100]}...")
        print(f"    link_url: {url}")
        print(f"    scheduled: {scheduled_date or 'immediately'}")
        return True

    resp = requests.post(
        f"{API_BASE}/api/upload_text",
        headers={"Authorization": f"Apikey {API_KEY}"},
        data=data,
        timeout=30,
    )

    if resp.ok:
        post_url = _print_result(platform, resp.json().get("request_id", ""), scheduled_date)
        return post_url or "posted"
    else:
        print(f"  FAILED on {platform}: {resp.status_code} {resp.text}")
        return None


def post_photo(platform, copy, url, image_path, scheduled_date):
    """Post via upload_photos with image attached. Used for LinkedIn where link_url cards don't work."""
    text_with_url = f"{copy}\n\n{url}" if url not in copy else copy
    data = {
        "user": USER,
        "platform[]": platform,
        "title": text_with_url,
    }
    if platform == "linkedin":
        data["linkedin_description"] = text_with_url
        if LINKEDIN_PAGE_ID:
            data["target_linkedin_page_id"] = LINKEDIN_PAGE_ID

    if scheduled_date:
        data["scheduled_date"] = scheduled_date
        data["timezone"] = POSTING_TZ

    if DRY_RUN:
        print(f"  [DRY RUN] Would post photo to {platform}:")
        print(f"    image: {image_path}")
        print(f"    {copy[:80]}...")
        print(f"    scheduled: {scheduled_date or 'immediately'}")
        return True

    if not image_path:
        print(f"  Warning: no meta image found, skipping {platform}")
        return None

    mime = "image/jpeg" if image_path.endswith(".jpg") else "image/png"
    with open(image_path, "rb") as f:
        resp = requests.post(
            f"{API_BASE}/api/upload_photos",
            headers={"Authorization": f"Apikey {API_KEY}"},
            data=data,
            files={"photos[]": (os.path.basename(image_path), f, mime)},
            timeout=60,
        )

    if resp.ok:
        result = resp.json()
        request_id = result.get("request_id", "")
        platform_result = result.get("results", {}).get(platform, {})
        direct_url = platform_result.get("url")
        if direct_url:
            if scheduled_date:
                print(f"  ✓ {platform}: scheduled for {scheduled_date} {POSTING_TZ}")
            else:
                print(f"  ✓ {platform}: {direct_url}")
            return direct_url or "posted"
        else:
            post_url = _print_result(platform, request_id, scheduled_date)
            return post_url or "posted"
    else:
        print(f"  FAILED on {platform}: {resp.status_code} {resp.text}")
        return None


def schedule_post(platform, copy, url, image_path, scheduled_date):
    """Route to the right posting method per platform. Returns post URL or None."""
    if platform == "linkedin":
        return post_photo(platform, copy, url, image_path, scheduled_date)
    return post_text(platform, copy, url, scheduled_date)


# --- Main ---

def main():
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
        # Still update last_sha so we don't re-diff the same range next time
        head = get_head_sha()
        if head and head != state.get("last_sha"):
            state["last_sha"] = head
            save_state(state)
        return

    failures = False
    posted_urls = []  # (blog_url, platform, post_url) for summary
    posts_by_file = defaultdict(list)  # filepath -> [(platform, post_url)]

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
        # Frontmatter uses "twitter" key for familiarity, but API platform is "x"
        x_copy = str(social.get("twitter") or "").strip()
        linkedin_copy = str(social.get("linkedin") or "").strip()
        bluesky_copy = str(social.get("bluesky") or "").strip()

        # Skip old posts
        if not post_date or not is_recent_or_future(post_date):
            print(f"  Skipping: date {post_date} is not recent or future")
            continue

        # Skip TODOs and empty values
        if x_copy.upper() == "TODO":
            x_copy = ""
        if linkedin_copy.upper() == "TODO":
            linkedin_copy = ""
        if bluesky_copy.upper() == "TODO":
            bluesky_copy = ""

        if not x_copy and not linkedin_copy and not bluesky_copy:
            print(f"  Warning: no social copy in frontmatter for {filepath}")
            continue



        image_path = meta_image_path(filepath)
        scheduled = scheduled_date_from_post(post_date)
        print(f"  URL: {url}")
        if scheduled:
            print(f"  Scheduled for: {scheduled} {POSTING_TZ}")
        else:
            print(f"  Posting immediately (date is today or past)")

        post_had_failure = False
        for platform, copy in [("x", x_copy), ("linkedin", linkedin_copy), ("bluesky", bluesky_copy)]:
            if not copy:
                continue
            if not PLATFORM_ENABLED.get(platform):
                continue

            # Validate character limits
            # LinkedIn includes URL in body (photo post); X/Bluesky use link_url
            limit = CHAR_LIMITS.get(platform)
            if platform == "linkedin":
                text_len = len(copy) if url in copy else len(copy) + 2 + len(url)
            else:
                text_len = len(copy)
            if limit and text_len > limit:
                print(f"  SKIPPING {platform}: copy is {text_len} chars, limit is {limit}")
                failures = True
                continue

            # Primary idempotency check: S3 state
            if is_posted(state, slug, platform):
                print(f"  Skipping {platform}: already posted (per state file)")
                continue

            post_url = schedule_post(platform, copy, url, image_path, scheduled)
            if post_url:
                record_posted(state, slug, platform)
                save_state(state)
                posted_urls.append((url, platform, post_url))
                posts_by_file[filepath].append((platform, post_url))
            else:
                post_had_failure = True

        # Record one failure per post per run (not per platform)
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

        # Write GitHub Actions job summary if available
        summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
        if summary_path:
            with open(summary_path, "a") as f:
                f.write("## Social media posts\n\n")
                f.write("| Blog post | Platform | Post |\n")
                f.write("|---|---|---|\n")
                for blog_url, platform, post_url in posted_urls:
                    slug = blog_url.replace(SITE_URL, "")
                    if post_url.startswith("http"):
                        f.write(f"| {slug} | {platform} | [link]({post_url}) |\n")
                    else:
                        f.write(f"| {slug} | {platform} | {post_url} |\n")

        # Comment on the PRs that introduced these blog posts
        for filepath, results in posts_by_file.items():
            pr_number = find_pr_number(filepath, since_sha=state.get("last_sha"))
            if not pr_number:
                print(f"  Could not find PR for {filepath}, skipping comment")
                continue
            lines = [f"📣 Social media posts are live for this blog post:\n"]
            for platform, post_url in results:
                if isinstance(post_url, str) and post_url.startswith("http"):
                    lines.append(f"- **{platform}**: {post_url}")
                else:
                    lines.append(f"- **{platform}**: posted")
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


if __name__ == "__main__":
    main()
