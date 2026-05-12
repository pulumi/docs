#!/usr/bin/env python3
"""hugo-build-validate.py — Hugo build pre-step.

Runs Hugo build validation on the PR head + sitemap diff vs base.

Architectural mirror of `frontmatter-validate.py`, `cross-sibling-discover.py`,
and the other workflow pre-steps: a step that emits a JSON artifact the
reviewer agent reads. Hugo is the canonical authority for routing/build
correctness — this artifact gives the agent a structurally-guaranteed build
floor instead of a model-side `make build` it can't run.

Scope (MVP):
- Build errors and warnings from `hugo --renderToMemory` (one full render at HEAD).
- Internal-link integrity: WARN/ERROR lines mentioning `ref`, `shortcode`,
  `unmarshal`, `missing`, `not found`.
- Sitemap diff (added/removed pages) computed from `hugo list all` at HEAD vs
  BASE. Each Hugo invocation runs in a separate worktree to avoid mutating
  the working tree.

What this is NOT:
- A complete build. Asset bundling (CSS/JS) is intentionally skipped — Hugo
  still renders templates and content, which is what catches broken refs
  and missing assets that propagate through the build. The flip side: the
  render WILL emit a handful of CI-environment-only errors because the
  workflow doesn't run `make ensure` first (PostCSS/Hugo-Pipes fingerprint
  failure on `/404`; `data/openapi-spec.json not found`). Those are filtered
  out here — see KNOWN_CI_NOISE_PATTERNS — and reported under
  `suppressed_ci_noise` so the reviewer agent never sees them as findings
  but the suppression is still auditable in the artifact.
- A render-graph dump. Skipped for now; can be added later if a specific
  bug class requires it.
- Authoritative for "changed pages" (URL-stability) detection across runs.
  The MVP emits added/removed only; "changed" is reserved for a follow-up.

See `references/pre-computation.md` for the architectural pattern, and
`references/fact-check.md` §Hugo build artifact for the consumption contract.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

# ---- Hugo invocation -------------------------------------------------------

# Hugo render warnings we surface as link-integrity issues.
LINK_INTEGRITY_PATTERNS = [
    re.compile(r"\bref\b.*\bnot found\b", re.IGNORECASE),
    re.compile(r"\bshortcode\b.*\bunmarshal\b", re.IGNORECASE),
    re.compile(r"\bbroken\b.*\b(ref|link)\b", re.IGNORECASE),
    re.compile(r"\bmissing\b.*\b(asset|image|file|target)\b", re.IGNORECASE),
    re.compile(r"\bcannot find\b", re.IGNORECASE),
]

# CI-environment-only noise. This pre-step renders without `make ensure`
# (asset prep + data fetch are intentionally skipped — see module docstring),
# so Hugo reliably emits a few errors/warnings that are NOT PR-introduced:
#   - PostCSS / Hugo-Pipes asset-pipeline failures (the `/404` page fingerprints
#     a stylesheet that doesn't exist because PostCSS never ran).
#   - `data/openapi-spec.json not found` (the OpenAPI data file is fetched by
#     `make ensure`, not committed).
# Lines matching these are stripped from `errors`/`warnings`/`link_integrity`
# before the artifact is written and collected under `suppressed_ci_noise`.
# Keep these anchored to asset-pipeline / data-fetch signatures so a genuine
# PR-introduced template or shortcode error never gets swallowed.
KNOWN_CI_NOISE_PATTERNS = [
    re.compile(r"error calling (fingerprint|resources\.Fingerprint)", re.IGNORECASE),
    re.compile(r"can ?not be transformed to a resource", re.IGNORECASE),
    re.compile(r"\bPostCSS\b", re.IGNORECASE),
    re.compile(r"resources\.(Fingerprint|PostCSS|PostProcess|ToCSS|Babel|Minify|Concat)", re.IGNORECASE),
    re.compile(r"data/openapi-spec\.json", re.IGNORECASE),
    re.compile(r"\bopenapi:\b.*\bnot found\b", re.IGNORECASE),
]

HUGO_TIMEOUT_RENDER_S = 240
HUGO_TIMEOUT_LIST_S = 90


def _is_ci_noise(line: str) -> bool:
    return any(pat.search(line) for pat in KNOWN_CI_NOISE_PATTERNS)


def run_hugo_render(workdir: Path) -> tuple[list[str], list[str], list[str], int, list[str]]:
    """Run `hugo --renderToMemory`.

    Return (errors, warnings, link_integrity, exit, suppressed_ci_noise) — the
    first three already have CI-environment noise stripped; the last is the
    list of stripped lines, for auditability.
    """
    proc = subprocess.run(
        ["hugo", "--renderToMemory", "--logLevel", "info"],
        cwd=str(workdir),
        capture_output=True,
        text=True,
        timeout=HUGO_TIMEOUT_RENDER_S,
        env={**os.environ, "HUGO_BASEURL": "http://localhost:1313"},
    )
    errors: list[str] = []
    warnings: list[str] = []
    link_integrity: list[str] = []
    suppressed: list[str] = []
    for line in (proc.stderr or "").splitlines():
        line = line.rstrip()
        if not line:
            continue
        if _is_ci_noise(line):
            suppressed.append(line)
            continue
        # Hugo emits ERROR/WARN at the start of log lines under --logLevel info.
        if line.startswith("ERROR"):
            errors.append(line)
        elif line.startswith("WARN"):
            warnings.append(line)
        if any(pat.search(line) for pat in LINK_INTEGRITY_PATTERNS):
            link_integrity.append(line)
    return errors, warnings, link_integrity, proc.returncode, suppressed


def run_hugo_list(workdir: Path) -> list[dict]:
    """Run `hugo list all`. Return list of page records (dicts)."""
    proc = subprocess.run(
        ["hugo", "list", "all"],
        cwd=str(workdir),
        capture_output=True,
        text=True,
        timeout=HUGO_TIMEOUT_LIST_S,
    )
    pages: list[dict] = []
    lines = (proc.stdout or "").splitlines()
    if not lines:
        return pages
    headers = [h.strip() for h in lines[0].split(",")]
    for raw in lines[1:]:
        # CSV with no quoted commas in this codebase's titles in practice;
        # split conservatively to len(headers) fields.
        fields = raw.split(",", len(headers) - 1)
        if len(fields) < len(headers):
            continue
        rec = dict(zip(headers, fields))
        pages.append(rec)
    return pages


# ---- URL normalization (mirrors frontmatter-validate.py contract) ----------


def normalize_url(url: str) -> str:
    """Trim host, ensure leading slash, ensure trailing slash, lowercase host strip."""
    if not url:
        return ""
    url = url.replace("https://www.pulumi.com", "").replace("http://localhost:1313", "")
    if not url.startswith("/"):
        url = "/" + url
    if not url.endswith("/"):
        url = url + "/"
    return url


# ---- Base ref handling -----------------------------------------------------


def resolve_base_sha(pr: str | None, base_sha: str | None, repo: str | None) -> str | None:
    """Return the base SHA. Prefer explicit --base-sha; fall back to gh pr view."""
    if base_sha:
        return base_sha
    if not pr:
        return None
    cmd = ["gh", "pr", "view", pr, "--json", "baseRefOid", "--jq", ".baseRefOid"]
    if repo:
        cmd[3:3] = ["--repo", repo]
    proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
    sha = (proc.stdout or "").strip()
    return sha or None


def materialize_base_worktree(workspace: Path, base_sha: str, dest: Path) -> bool:
    """Create a base-SHA worktree at `dest`. Return True on success."""
    proc = subprocess.run(
        ["git", "worktree", "add", "--detach", str(dest), base_sha],
        cwd=str(workspace),
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        # Likely the base SHA isn't fetched. Try to fetch it once.
        fetch = subprocess.run(
            ["git", "fetch", "--depth=1", "origin", base_sha],
            cwd=str(workspace),
            capture_output=True,
            text=True,
            check=False,
        )
        if fetch.returncode != 0:
            return False
        proc = subprocess.run(
            ["git", "worktree", "add", "--detach", str(dest), base_sha],
            cwd=str(workspace),
            capture_output=True,
            text=True,
            check=False,
        )
    return proc.returncode == 0


def remove_base_worktree(workspace: Path, dest: Path) -> None:
    subprocess.run(
        ["git", "worktree", "remove", str(dest), "--force"],
        cwd=str(workspace),
        capture_output=True,
        check=False,
    )


# ---- Sitemap diff ----------------------------------------------------------


def compute_sitemap_diff(base_pages: list[dict], head_pages: list[dict]) -> dict:
    """Compute added/removed pages between base and head. 'Changed' is
    deferred — the MVP only flags URL set changes."""
    base_urls = {normalize_url(p.get("permalink", "")) for p in base_pages}
    head_urls = {normalize_url(p.get("permalink", "")) for p in head_pages}
    base_urls.discard("")
    head_urls.discard("")
    added = sorted(head_urls - base_urls)
    removed = sorted(base_urls - head_urls)
    return {"added": added, "removed": removed, "changed": []}


# ---- Main ------------------------------------------------------------------


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--pr", help="PR number (used to resolve base SHA via gh pr view)")
    ap.add_argument("--base-sha", help="Explicit base SHA; bypasses gh pr view")
    ap.add_argument("--repo", help="owner/repo for gh pr view (default: gh resolution)")
    ap.add_argument("--out", required=True, help="Output JSON artifact path")
    ap.add_argument(
        "--skip-base",
        action="store_true",
        help="Skip base hugo list (sitemap diff will be empty). For local dev/self-test.",
    )
    args = ap.parse_args()

    workspace = Path.cwd()
    out_path = Path(args.out)

    # 1. Build at HEAD.
    errors: list[str] = []
    warnings: list[str] = []
    link_integrity: list[str] = []
    suppressed_ci_noise: list[str] = []
    exit_code = 0
    try:
        errors, warnings, link_integrity, exit_code, suppressed_ci_noise = run_hugo_render(workspace)
    except subprocess.TimeoutExpired:
        errors.append(f"hugo --renderToMemory timed out after {HUGO_TIMEOUT_RENDER_S}s")
        exit_code = -1
    except FileNotFoundError:
        errors.append("hugo binary not found on PATH")
        exit_code = -1
    except OSError as e:
        errors.append(f"hugo --renderToMemory OSError: {e}")
        exit_code = -1

    # 2. List pages at HEAD.
    head_pages: list[dict] = []
    try:
        head_pages = run_hugo_list(workspace)
    except subprocess.TimeoutExpired:
        errors.append(f"hugo list all (head) timed out after {HUGO_TIMEOUT_LIST_S}s")
    except FileNotFoundError:
        # Already recorded by run_hugo_render's except.
        pass
    except OSError as e:
        errors.append(f"hugo list all (head) OSError: {e}")

    # 3. List pages at BASE in a separate worktree.
    base_pages: list[dict] = []
    base_sha = resolve_base_sha(args.pr, args.base_sha, args.repo)
    if not args.skip_base and base_sha:
        with tempfile.TemporaryDirectory(prefix="hugo-base-") as tmp:
            dest = Path(tmp) / "base"
            ok = materialize_base_worktree(workspace, base_sha, dest)
            if ok:
                try:
                    base_pages = run_hugo_list(dest)
                except subprocess.TimeoutExpired:
                    warnings.append(
                        f"hugo list all (base) timed out after {HUGO_TIMEOUT_LIST_S}s"
                    )
                except FileNotFoundError:
                    pass
                except OSError as e:
                    warnings.append(f"hugo list all (base) OSError: {e}")
                finally:
                    remove_base_worktree(workspace, dest)
            else:
                warnings.append(
                    f"hugo-build-validate: could not materialize base worktree at {base_sha}; sitemap_diff will be empty"
                )

    sitemap_diff = compute_sitemap_diff(base_pages, head_pages)

    # A non-zero Hugo exit with no real errors left after CI-noise filtering is
    # the known `/404` fingerprint failure — flag it as benign so the agent
    # doesn't have to reason about it.
    head_exit_nonzero_is_ci_noise = exit_code != 0 and not errors and bool(suppressed_ci_noise)

    out = {
        "schema_version": 1,
        "head_exit_code": exit_code,
        "head_exit_nonzero_is_ci_noise": head_exit_nonzero_is_ci_noise,
        "errors": errors,
        "warnings": warnings,
        "link_integrity": link_integrity,
        "suppressed_ci_noise": suppressed_ci_noise,
        "sitemap_diff": sitemap_diff,
        "stats": {
            "errors_count": len(errors),
            "warnings_count": len(warnings),
            "link_integrity_count": len(link_integrity),
            "suppressed_ci_noise_count": len(suppressed_ci_noise),
            "head_pages_count": len(head_pages),
            "base_pages_count": len(base_pages),
            "added_pages_count": len(sitemap_diff["added"]),
            "removed_pages_count": len(sitemap_diff["removed"]),
        },
    }
    out_path.write_text(json.dumps(out, indent=2))
    return 0


def safe_main() -> int:
    """Top-level wrapper: never crash. Always emit a JSON artifact, even on
    unexpected exceptions, so the workflow's `||` fallback is reserved for
    cases where the script itself can't even start (ImportError, etc.)."""
    try:
        return main()
    except SystemExit:
        raise
    except BaseException as e:
        # Try to recover the --out path from argv to emit a structured error.
        out_path = None
        argv = sys.argv
        for i, a in enumerate(argv):
            if a == "--out" and i + 1 < len(argv):
                out_path = Path(argv[i + 1])
                break
            if a.startswith("--out="):
                out_path = Path(a.split("=", 1)[1])
                break
        if out_path is not None:
            err_payload = {
                "schema_version": 1,
                "head_exit_code": -1,
                "head_exit_nonzero_is_ci_noise": False,
                "errors": [f"hugo-build-validate uncaught exception: {type(e).__name__}: {e}"],
                "warnings": [],
                "link_integrity": [],
                "suppressed_ci_noise": [],
                "sitemap_diff": {"added": [], "removed": [], "changed": []},
                "stats": {
                    "errors_count": 1,
                    "warnings_count": 0,
                    "link_integrity_count": 0,
                    "suppressed_ci_noise_count": 0,
                    "head_pages_count": 0,
                    "base_pages_count": 0,
                    "added_pages_count": 0,
                    "removed_pages_count": 0,
                },
            }
            try:
                out_path.write_text(json.dumps(err_payload, indent=2))
            except OSError:
                pass
        # Surface the original error to stderr so workflow logs see it.
        import traceback
        traceback.print_exc(file=sys.stderr)
        return 0  # Don't trip the workflow's || fallback; we wrote a useful artifact.


if __name__ == "__main__":
    sys.exit(safe_main())
