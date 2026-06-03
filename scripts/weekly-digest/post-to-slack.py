#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Post the combined weekly digest to Slack, split across as many messages as
needed so nothing is truncated.

Slack truncates long messages, so a single long digest gets clipped. This reads
the assembled digest (one document with headings), splits it on line boundaries
into chunks under a safe size, and posts them sequentially via chat.postMessage
so they read as one continuous run in the channel. Mirrors the link checker's
Slack-API posting path (scripts/link-checker/check-links.js): `SLACK_ACCESS_TOKEN`
from ESC, mrkdwn on, link unfurling off.

Usage: post-to-slack.py <digest-file> [--dry-run]
  --dry-run prints the chunk boundaries and count without posting (no token
  needed); used by the workflow's dry_run path.
Env: SLACK_ACCESS_TOKEN (required unless --dry-run), SLACK_CHANNEL (default
  "#docs-ops").
"""

import json
import os
import sys
import time
import urllib.error
import urllib.request

# Conservative ceiling. Slack's hard limit is ~40k chars, but long messages
# render unreliably; keeping chunks well under ~4k is the safe, readable choice.
MAX_CHARS = 3500
POST_URL = "https://slack.com/api/chat.postMessage"


def _split_long_line(line, max_chars):
    """Hard-split a single line that on its own exceeds the chunk ceiling."""
    parts = []
    while len(line) > max_chars:
        parts.append(line[:max_chars])
        line = line[max_chars:]
    parts.append(line)
    return parts


def chunk_text(text, max_chars=MAX_CHARS):
    """Greedily pack lines into chunks <= max_chars, never breaking a line
    except when a single line is itself too long. Pure / testable."""
    units = []
    for line in text.split("\n"):
        units.extend(_split_long_line(line, max_chars))
    chunks = []
    current = ""
    for unit in units:
        candidate = unit if not current else current + "\n" + unit
        if current and len(candidate) > max_chars:
            chunks.append(current)
            current = unit
        else:
            current = candidate
    if current:
        chunks.append(current)
    return [c for c in chunks if c.strip()]


def post_chunk(token, channel, text, retries=4):
    body = json.dumps(
        {"channel": channel, "text": text, "mrkdwn": True, "unfurl_links": False, "as_user": True}
    ).encode("utf-8")
    req = urllib.request.Request(
        POST_URL,
        data=body,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=utf-8",
        },
    )
    delay = 2
    for attempt in range(1, retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read())
            if data.get("ok"):
                return data
            # ok:false is a hard error (bad token, channel, etc.) -- don't retry.
            raise RuntimeError(f"Slack API error: {data.get('error')}")
        except urllib.error.URLError as exc:
            if attempt == retries:
                raise
            sys.stderr.write(f"post attempt {attempt} failed ({exc}); retrying in {delay}s\n")
            time.sleep(delay)
            delay *= 2


def main():
    args = [a for a in sys.argv[1:] if a != "--dry-run"]
    dry_run = "--dry-run" in sys.argv[1:]
    if not args:
        sys.exit("usage: post-to-slack.py <digest-file> [--dry-run]")
    text = open(args[0], encoding="utf-8").read()
    chunks = chunk_text(text)
    if not chunks:
        sys.stderr.write("nothing to post (empty digest)\n")
        return

    if dry_run:
        print(f"Would post {len(chunks)} message(s):")
        for i, chunk in enumerate(chunks, 1):
            print(f"\n----- message {i}/{len(chunks)} ({len(chunk)} chars) -----")
            print(chunk)
        return

    token = os.environ.get("SLACK_ACCESS_TOKEN")
    if not token:
        sys.exit("SLACK_ACCESS_TOKEN is not set")
    channel = os.environ.get("SLACK_CHANNEL", "#docs-ops")
    if not channel.startswith(("#", "C", "G")):
        channel = f"#{channel}"
    for i, chunk in enumerate(chunks, 1):
        post_chunk(token, channel, chunk)
        print(f"posted message {i}/{len(chunks)} ({len(chunk)} chars)")


if __name__ == "__main__":
    main()
