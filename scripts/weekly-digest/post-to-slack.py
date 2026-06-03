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
import socket
import sys
import time
import urllib.request

# Conservative ceiling. Slack's hard limit is ~40k chars, but long messages
# render unreliably; keeping chunks well under ~4k is the safe, readable choice.
MAX_CHARS = 3500
POST_URL = "https://slack.com/api/chat.postMessage"
# Per-request socket timeout. Python connects to addresses sequentially with no
# Happy Eyeballs, so this is also the per-address budget -- keep it short.
REQUEST_TIMEOUT = 10


def _force_ipv4():
    """Make getaddrinfo return only IPv4 records.

    slack.com resolves to both IPv4 and IPv6 addresses. On runners without IPv6
    egress, Python's sequential socket.create_connection burns the full socket
    timeout on each unreachable IPv6 address before falling through, stacking up
    to multi-minute "timeouts" on a 10s budget (this hung a real run for ~7.5min
    per attempt). @slack/web-api dodges it via Happy Eyeballs; we don't, so we
    drop AF_INET6 from resolution entirely -- this process only talks to Slack.
    """
    real_getaddrinfo = socket.getaddrinfo

    def ipv4_only(host, port, family=0, type=0, proto=0, flags=0):
        return real_getaddrinfo(host, port, socket.AF_INET, type, proto, flags)

    socket.getaddrinfo = ipv4_only


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


def post_chunk(token, channel, text, retries=3):
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
            with urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT) as resp:
                data = json.loads(resp.read())
            if data.get("ok"):
                return data
            # ok:false is a hard error (bad token, channel, etc.) -- don't retry.
            raise RuntimeError(f"Slack API error: {data.get('error')}")
        # OSError covers URLError, socket timeouts, and connection resets; a
        # RuntimeError (ok:false) is not caught and fails fast.
        except OSError as exc:
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
    _force_ipv4()
    channel = os.environ.get("SLACK_CHANNEL", "#docs-ops")
    if not channel.startswith(("#", "C", "G")):
        channel = f"#{channel}"
    for i, chunk in enumerate(chunks, 1):
        post_chunk(token, channel, chunk)
        print(f"posted message {i}/{len(chunks)} ({len(chunk)} chars)")


if __name__ == "__main__":
    main()
