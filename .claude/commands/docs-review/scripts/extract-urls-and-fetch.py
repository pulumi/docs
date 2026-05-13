#!/usr/bin/env python3
"""Extract external URLs added by a PR's diff and pre-fetch them.

Architecture mirror of `vale-findings-filter.py`: a deterministic workflow
pre-step that lets the docs-review skill consume pre-computed data instead
of dispatching tools at review time. Subdivides the existing "Pass 2"
verification lane into:

    Pass 2 -- consult `.fetched-urls.json` (this script's output)
    Pass 3 -- WebSearch + WebFetch fan-out for external-public claims with
              no URL in the diff

The script is the deterministic floor for Pass 2 -- the model can no longer
claim Pass 2 dispatches that didn't actually happen, because the JSON file
records exactly which URLs the workflow fetched.

Usage:
    extract-urls-and-fetch.py --pr <PR_NUMBER> --out <out.json>

Caps:
    - 30 URLs per review (FETCH_CAP)
    - 10s per fetch (FETCH_TIMEOUT)
    - cache by URL hash in /tmp/extract-urls-cache/

Output schema (flat list, sorted by URL):
    [
      {"url": "https://example.com",
       "status": 200,
       "content_text": "<plain text, capped>",
       "fetch_ms": 412},
      {"url": "https://github.com/owner/repo/blob/main/README.md",
       "fetched_url": "https://raw.githubusercontent.com/owner/repo/main/README.md",
       "status": 200,
       "content_text": "<plain text, capped>",
       "fetch_ms": 380},
      {"url": "https://broken.example",
       "status": 0,
       "content_text": "",
       "fetch_ms": 10000,
       "error": "timeout"},
      ...
    ]

Empty input (no diff, no PR-changed content/(docs|blog) files, no external
URLs) produces an empty list (`[]`), never errors. The script does not call
any APIs except `gh pr diff` and HTTP fetches via urllib.

URL normalization: GitHub and Docker Hub serve SPA / JS-rendered HTML for
their human-facing URLs, which yields ~empty `content_text` after the HTML
strip and silently turns external-fact claims into Pass 3 unverifiable
verdicts. Before fetching, this script rewrites known SPA URLs to their
content-API equivalents:

    github.com/<o>/<r>/blob/<rev>/<path>  → raw.githubusercontent.com/<o>/<r>/<rev>/<path>
    github.com/<o>/<r>/raw/<rev>/<path>   → raw.githubusercontent.com/<o>/<r>/<rev>/<path>
    hub.docker.com/r/<o>/<r>              → hub.docker.com/v2/repositories/<o>/<r>/tags/?page_size=20
    hub.docker.com/_/<r>                  → hub.docker.com/v2/repositories/library/<r>/tags/?page_size=20

The `url` field in the record stays the original (so verifier pattern-
matching against the diff text still works); a `fetched_url` field appears
only when normalization changed the target.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

FETCH_CAP = 30
FETCH_TIMEOUT = 10  # seconds
CONTENT_TEXT_CAP = 8000  # characters per fetch (post-strip)
USER_AGENT = "pulumi-docs-review-fetch/1.0 (+https://github.com/pulumi/docs)"
CACHE_DIR = Path("/tmp/extract-urls-cache")

# Markdown link `[text](url)` and bare-url autolink `<https://...>`.
MD_LINK_RE = re.compile(r"\[([^\]]*)\]\((https?://[^)\s]+)\)")
AUTOLINK_RE = re.compile(r"<(https?://[^>\s]+)>")
BARE_URL_RE = re.compile(r"https?://[\w\-._~:/?#\[\]@!$&'*+,;=%]+")

DIFF_FILE_RE = re.compile(r"^\+\+\+ b/(.+)$")
HUNK_RE = re.compile(r"^@@ -\d+(?:,\d+)? \+(\d+)(?:,(\d+))? @@")

# Normalization patterns (see module docstring). Anchored so we don't over-
# match. Owner / repo / rev capture the URL-safe segment up to the next `/`;
# the path is greedy and stops at a fragment or query.
GITHUB_BLOB_RE = re.compile(
    r"^https://github\.com/([^/\s#?]+)/([^/\s#?]+)/(?:blob|raw)/([^/\s#?]+)/([^\s#?]+)"
)
DOCKERHUB_R_RE = re.compile(
    r"^https://hub\.docker\.com/r/([^/\s#?]+)/([^/\s#?]+)(?:/[^\s#?]*)?"
)
DOCKERHUB_LIBRARY_RE = re.compile(
    r"^https://hub\.docker\.com/_/([^/\s#?]+)(?:/[^\s#?]*)?"
)


def normalize_url(url: str) -> str:
    """Rewrite known SPA / JS-rendered URLs to content-API equivalents.

    Returns the URL unchanged if no rewrite applies. See module docstring
    for the full pattern list.
    """
    m = GITHUB_BLOB_RE.match(url)
    if m:
        owner, repo, rev, path = m.groups()
        return f"https://raw.githubusercontent.com/{owner}/{repo}/{rev}/{path}"
    m = DOCKERHUB_R_RE.match(url)
    if m:
        owner, repo = m.groups()
        return f"https://hub.docker.com/v2/repositories/{owner}/{repo}/tags/?page_size=20"
    m = DOCKERHUB_LIBRARY_RE.match(url)
    if m:
        (repo,) = m.groups()
        return f"https://hub.docker.com/v2/repositories/library/{repo}/tags/?page_size=20"
    return url


def fetch_pr_patch(pr: str) -> str:
    """Fetch the unified diff for the PR via gh."""
    proc = subprocess.run(
        ["gh", "pr", "diff", pr, "--patch"],
        check=True,
        capture_output=True,
        text=True,
    )
    return proc.stdout


def added_lines_in_content(patch: str) -> list[str]:
    """Return `+`-prefixed body lines from content/(docs|blog)/**/*.md only.

    Skips file headers, hunk markers, and removed/context lines. The PR can
    add URLs in any file but we only care about prose files -- code-fence
    URLs in Hugo shortcodes or YAML frontmatter aren't claim sources.
    """
    out: list[str] = []
    current_file: str | None = None
    in_content = False
    for raw in patch.splitlines():
        m = DIFF_FILE_RE.match(raw)
        if m:
            current_file = m.group(1)
            in_content = bool(re.match(r"^content/(docs|blog)/.*\.md$", current_file))
            continue
        if not in_content or current_file is None:
            continue
        if raw.startswith("--- ") or HUNK_RE.match(raw):
            continue
        if raw.startswith("+") and not raw.startswith("+++"):
            out.append(raw[1:])
    return out


def extract_urls(lines: list[str]) -> list[str]:
    """Pull external http(s) URLs out of added lines, deduped, in first-seen order."""
    seen: set[str] = set()
    ordered: list[str] = []
    for line in lines:
        for m in MD_LINK_RE.finditer(line):
            url = m.group(2).rstrip(".,;:")
            if url not in seen:
                seen.add(url)
                ordered.append(url)
        for m in AUTOLINK_RE.finditer(line):
            url = m.group(1).rstrip(".,;:")
            if url not in seen:
                seen.add(url)
                ordered.append(url)
        # Bare URLs only when not already captured by markdown-link / autolink.
        for m in BARE_URL_RE.finditer(line):
            url = m.group(0).rstrip(".,;:)\"")
            if url not in seen:
                seen.add(url)
                ordered.append(url)
    return ordered


def cache_path(url: str) -> Path:
    h = hashlib.sha256(url.encode()).hexdigest()[:16]
    return CACHE_DIR / f"{h}.json"


def fetch_one(url: str) -> dict:
    """Fetch a URL, write to cache, return the record dict.

    `url` is the original URL from the PR diff (preserved on the record so
    verifier pattern-matching against the diff text still works). If
    `normalize_url(url)` produces a different target, we fetch the normalized
    form and add a `fetched_url` field; the cache is keyed on the normalized
    URL so multiple original URLs that normalize to the same target share
    one cache entry.
    """
    fetched = normalize_url(url)
    cached = cache_path(fetched)
    if cached.is_file():
        try:
            record = json.loads(cached.read_text())
            record["url"] = url
            if fetched != url:
                record["fetched_url"] = fetched
            else:
                record.pop("fetched_url", None)
            return record
        except (OSError, json.JSONDecodeError):
            pass

    start = time.monotonic()
    record: dict = {"url": url, "status": 0, "content_text": "", "fetch_ms": 0}
    if fetched != url:
        record["fetched_url"] = fetched
    try:
        req = urllib.request.Request(fetched, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=FETCH_TIMEOUT) as resp:
            status = getattr(resp, "status", 200)
            raw = resp.read(CONTENT_TEXT_CAP * 4)  # over-read; HTML-strip below
            ctype = resp.headers.get("Content-Type", "")
            charset = "utf-8"
            for part in ctype.split(";"):
                part = part.strip().lower()
                if part.startswith("charset="):
                    charset = part.split("=", 1)[1] or "utf-8"
            try:
                text = raw.decode(charset, errors="replace")
            except LookupError:
                text = raw.decode("utf-8", errors="replace")
            stripped = re.sub(r"<script[^>]*>.*?</script>", " ", text, flags=re.DOTALL | re.IGNORECASE)
            stripped = re.sub(r"<style[^>]*>.*?</style>", " ", stripped, flags=re.DOTALL | re.IGNORECASE)
            stripped = re.sub(r"<[^>]+>", " ", stripped)
            stripped = re.sub(r"\s+", " ", stripped).strip()
            record["status"] = status
            record["content_text"] = stripped[:CONTENT_TEXT_CAP]
    except urllib.error.HTTPError as e:
        record["status"] = e.code
        record["error"] = f"http {e.code}: {e.reason}"
    except urllib.error.URLError as e:
        record["error"] = f"url error: {e.reason}"
    except (TimeoutError, OSError) as e:
        record["error"] = f"{type(e).__name__}: {e}"
    record["fetch_ms"] = int((time.monotonic() - start) * 1000)

    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    try:
        cached.write_text(json.dumps(record))
    except OSError:
        pass
    return record


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pr", required=True, help="PR number")
    parser.add_argument("--out", dest="outfile", required=True)
    args = parser.parse_args()

    out_path = Path(args.outfile)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        patch = fetch_pr_patch(args.pr)
    except subprocess.SubprocessError as e:
        print(f"extract-urls-and-fetch: gh pr diff failed: {e}", file=sys.stderr)
        out_path.write_text("[]")
        return 0

    lines = added_lines_in_content(patch)
    urls = extract_urls(lines)
    if not urls:
        out_path.write_text("[]")
        print("extract-urls-and-fetch: no external URLs in PR-added prose", file=sys.stderr)
        return 0

    capped = urls[:FETCH_CAP]
    skipped = len(urls) - len(capped)

    records = [fetch_one(u) for u in capped]
    records.sort(key=lambda r: r["url"])

    out_path.write_text(json.dumps(records, indent=2))
    print(
        f"extract-urls-and-fetch: fetched {len(records)} URL(s) "
        f"(skipped {skipped} over cap) → {out_path}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
