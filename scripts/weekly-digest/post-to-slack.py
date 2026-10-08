#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Post the weekly digest to Slack, split across as many messages as needed so
nothing is truncated.

The digest is rendered to fit one message (render.py), but Slack truncates long
messages, so a heavy week would get clipped. This reads the rendered digest,
splits it on line boundaries
into chunks under a safe size, and posts them sequentially via chat.postMessage
so they read as one continuous run in the channel. Mirrors the link checker's
Slack-API posting path (scripts/link-checker/check-links.js): `SLACK_ACCESS_TOKEN`
from ESC, mrkdwn on, link unfurling off.

Usage: post-to-slack.py <digest-file> [--thread <thread-file>] [--dry-run]
  --thread posts that file as a reply under the digest (the full lists the
  digest shortened); an empty or missing file posts no reply.
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


def post_chunk(token, channel, text, retries=3, thread_ts=None):
    payload = {"channel": channel, "text": text, "mrkdwn": True, "unfurl_links": False, "as_user": True}
    if thread_ts:
        payload["thread_ts"] = thread_ts
    body = json.dumps(payload).encode("utf-8")
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


def parse_args(argv):
    """(digest_path, thread_path | None, dry_run). Pure / testable."""
    dry_run = "--dry-run" in argv
    rest = [a for a in argv if a != "--dry-run"]
    thread = None
    if "--thread" in rest:
        i = rest.index("--thread")
        if i + 1 >= len(rest):
            sys.exit("--thread needs a file")
        thread = rest[i + 1]
        del rest[i:i + 2]
    if len(rest) != 1:
        sys.exit("usage: post-to-slack.py <digest-file> [--thread <thread-file>] [--dry-run]")
    return rest[0], thread, dry_run


def read_thread(path):
    if not path:
        return []
    try:
        return chunk_text(open(path, encoding="utf-8").read())
    except OSError:
        sys.stderr.write(f"warning: thread file {path} unreadable; posting no reply\n")
        return []


def main():
    digest_path, thread_path, dry_run = parse_args(sys.argv[1:])
    text = open(digest_path, encoding="utf-8").read()
    chunks = chunk_text(text)
    if not chunks:
        sys.stderr.write("nothing to post (empty digest)\n")
        return
    replies = read_thread(thread_path)

    if dry_run:
        print(f"Would post {len(chunks)} message(s) and {len(replies)} thread repl{'y' if len(replies) == 1 else 'ies'}:")
        for i, chunk in enumerate(chunks, 1):
            print(f"\n----- message {i}/{len(chunks)} ({len(chunk)} chars) -----")
            print(chunk)
        for i, chunk in enumerate(replies, 1):
            print(f"\n----- thread reply {i}/{len(replies)} ({len(chunk)} chars) -----")
            print(chunk)
        return

    token = os.environ.get("SLACK_ACCESS_TOKEN")
    if not token:
        sys.exit("SLACK_ACCESS_TOKEN is not set")
    _force_ipv4()
    channel = os.environ.get("SLACK_CHANNEL", "#docs-ops")
    if not channel.startswith(("#", "C", "G")):
        channel = f"#{channel}"
    first = None
    for i, chunk in enumerate(chunks, 1):
        data = post_chunk(token, channel, chunk)
        first = first or data
        print(f"posted message {i}/{len(chunks)} ({len(chunk)} chars)")
    # Replies thread under the first message. chat.postMessage returns the
    # channel's ID; a reply must use it (a #name doesn't resolve for
    # thread_ts). A failed reply is a warning: the digest itself is out.
    ts, channel_id = (first or {}).get("ts"), (first or {}).get("channel") or channel
    if replies and not ts:
        sys.stderr.write("::warning::Slack returned no ts for the digest; skipping the thread reply\n")
        return
    for i, chunk in enumerate(replies, 1):
        try:
            post_chunk(token, channel_id, chunk, thread_ts=ts)
        except (OSError, RuntimeError) as exc:
            sys.stderr.write(f"::warning::thread reply {i}/{len(replies)} failed ({exc}); stopping replies\n")
            return
        print(f"posted thread reply {i}/{len(replies)} ({len(chunk)} chars)")


if __name__ == "__main__":
    main()
