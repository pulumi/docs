#!/usr/bin/env python3
"""GitHub adapter shared by the /pr-review queue scripts (collect.py, act.py).

    from gh_client import GhClient
    gh = GhClient("pulumi/docs")            # picks a backend (see below)
    prs = gh.list_open_prs()

Three backends behind one interface, chosen by `backend=`:

- `gh`       — `gh api` subprocess, the house pattern (sentinel.py's `Gh`).
- `rest`     — `urllib` against api.github.com with `GITHUB_TOKEN` /
               `GH_TOKEN`. This is what a Claude Code web session has: no
               `gh` binary, but a token in the environment.
- `snapshot` — a directory of JSON files named after the endpoint, e.g.
               `<dir>/GET/repos/pulumi/docs/pulls/21598.json`. Reads come
               from the files; writes append to `<dir>/writes.jsonl` and
               return an empty dict. Tests run on this backend, and it is
               also how a model session hands MCP-fetched data to the
               scripts without either side knowing about the other.

`backend="auto"` (the default) picks `gh` when the binary is on PATH, else
`rest` when a token is set, else raises. Pass `record_dir=` to any live
backend to mirror every response into the snapshot layout — that is how the
test fixtures were captured and how a stale fixture gets refreshed.

GitHub App authors: the search API needs `author:app/<slug>` for an App —
`author:WorkPrentice` returns nothing, and the login GitHub shows is
`workprentice[bot]`. `search_author_q()` owns that rewrite; `norm_login()`
is the client-side equivalent for filtering a list you already have.

No model calls. Every method is stubbable; nothing here is Pulumi-specific
beyond the default repo.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import shutil
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

API_ROOT = "https://api.github.com"
DEFAULT_REPO = "pulumi/docs"
USER_AGENT = "pulumi-docs-pr-review"
TOKEN_ENVS = ("GITHUB_TOKEN", "GH_TOKEN")


class GhError(Exception):
    """A GitHub call failed. `status` is the HTTP status when known."""

    def __init__(self, message: str, status: int | None = None):
        super().__init__(message)
        self.status = status


class GhNotFound(GhError):
    """A clean 404 — data, not a failure, for callers that treat it that way."""


# ---- login helpers ------------------------------------------------------


def norm_login(login: str | None) -> str:
    """Canonical form of a login for comparisons: `workprentice[bot]`,
    `app/workprentice` and `WorkPrentice` all become `workprentice`."""
    s = (login or "").strip()
    if s.startswith("app/"):
        s = s[len("app/"):]
    if s.endswith("[bot]"):
        s = s[: -len("[bot]")]
    return s.lower()


def is_bot_login(login: str | None, user_type: str | None = None) -> bool:
    s = (login or "")
    return (
        (user_type or "").lower() == "bot"
        or s.endswith("[bot]")
        or s.startswith("app/")
        or s == "pulumi-bot"
    )


def search_author_q(login: str) -> str:
    """The `author:` qualifier for the search API.

    GitHub Apps are searchable only as `author:app/<slug>`; the `[bot]`
    suffix GitHub displays is not part of the slug. A plain user login passes
    through unchanged.
    """
    s = login.strip()
    if s.startswith("app/"):
        return f"author:{s}"
    if s.endswith("[bot]"):
        return f"author:app/{s[: -len('[bot]')]}"
    return f"author:{s}"


# ---- snapshot layout ----------------------------------------------------


def snapshot_path(root: Path, method: str, path: str, params: dict | None) -> Path:
    """`<root>/<METHOD>/<path>[__k=v&k=v].json` — readable, greppable,
    hand-editable. Query params are sorted so the name is stable."""
    p = path.strip("/")
    if params:
        q = urllib.parse.urlencode(sorted((k, str(v)) for k, v in params.items()))
        p = f"{p}__{q}"
    return root / method.upper() / f"{p}.json"


def _concat_json_docs(text: str):
    """Parse one or more concatenated JSON documents (what `gh api
    --paginate` emits for array endpoints) into one value; lists are
    flattened into a single list."""
    dec = json.JSONDecoder()
    idx = 0
    docs = []
    n = len(text)
    while idx < n:
        while idx < n and text[idx].isspace():
            idx += 1
        if idx >= n:
            break
        obj, end = dec.raw_decode(text, idx)
        docs.append(obj)
        idx = end
    if not docs:
        return None
    if len(docs) == 1:
        return docs[0]
    if all(isinstance(d, list) for d in docs):
        return [x for d in docs for x in d]
    return docs


# ---- the client ---------------------------------------------------------


class GhClient:
    def __init__(
        self,
        repo: str = DEFAULT_REPO,
        backend: str = "auto",
        *,
        snapshot_dir: str | Path | None = None,
        record_dir: str | Path | None = None,
        token: str | None = None,
    ):
        self.repo = repo
        self.snapshot_dir = Path(snapshot_dir) if snapshot_dir else None
        self.record_dir = Path(record_dir) if record_dir else None
        self.token = token or next((os.environ[e] for e in TOKEN_ENVS if os.environ.get(e)), None)
        if backend == "auto":
            backend = pick_backend(snapshot_dir=self.snapshot_dir, token=self.token)
        if backend == "snapshot" and not self.snapshot_dir:
            raise GhError("snapshot backend needs snapshot_dir")
        if backend == "rest" and not self.token:
            raise GhError("rest backend needs GITHUB_TOKEN or GH_TOKEN")
        self.backend = backend
        self.writes: list[dict] = []  # every write this client performed (any backend)

    # -- primitives --------------------------------------------------------

    def get(self, path: str, params: dict | None = None, *, paginate: bool = False):
        return self._request("GET", path, params=params, paginate=paginate)

    def post(self, path: str, body: dict | None = None):
        return self._request("POST", path, body=body or {})

    def put(self, path: str, body: dict | None = None):
        return self._request("PUT", path, body=body or {})

    def patch(self, path: str, body: dict | None = None):
        return self._request("PATCH", path, body=body or {})

    def delete(self, path: str):
        return self._request("DELETE", path)

    def _request(self, method, path, *, params=None, body=None, paginate=False):
        params = dict(params or {})
        if paginate and "per_page" not in params:
            params["per_page"] = 100
        if method != "GET":
            self.writes.append({"method": method, "path": path, "body": body})
        if self.backend == "snapshot":
            return self._snapshot_request(method, path, params, body)
        if self.backend == "gh":
            result = self._gh_request(method, path, params, body, paginate)
        else:
            result = self._rest_request(method, path, params, body, paginate)
        if self.record_dir and method == "GET":
            out = snapshot_path(self.record_dir, method, path, params)
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(json.dumps(result, indent=1, sort_keys=True) + "\n")
        return result

    def _snapshot_request(self, method, path, params, body):
        assert self.snapshot_dir is not None
        if method != "GET":
            log = self.snapshot_dir / "writes.jsonl"
            self.snapshot_dir.mkdir(parents=True, exist_ok=True)
            with log.open("a") as fh:
                fh.write(json.dumps({"method": method, "path": path, "body": body}) + "\n")
            return {}
        f = snapshot_path(self.snapshot_dir, method, path, params)
        if not f.exists():
            # Retry without pagination params — a hand-written fixture rarely
            # bothers to spell `per_page=100` into its filename.
            slim = {k: v for k, v in params.items() if k != "per_page"}
            f = snapshot_path(self.snapshot_dir, method, path, slim)
        if not f.exists():
            raise GhNotFound(f"no snapshot for {method} {path} {params or ''} under {self.snapshot_dir}", 404)
        return json.loads(f.read_text())

    def _gh_request(self, method, path, params, body, paginate):
        url = path
        if params:
            url += "?" + urllib.parse.urlencode(sorted(params.items()))
        args = ["gh", "api", url, "--method", method]
        if paginate:
            args.append("--paginate")
        stdin = None
        if body is not None and method != "GET":
            args += ["--input", "-"]
            stdin = json.dumps(body)
        try:
            out = subprocess.run(args, text=True, capture_output=True, check=True, input=stdin).stdout
        except subprocess.CalledProcessError as exc:
            stderr = (exc.stderr or "").strip()
            status = 404 if ("HTTP 404" in stderr or "Not Found" in stderr) else None
            cls = GhNotFound if status == 404 else GhError
            raise cls(f"gh api {method} {path} failed: {stderr[:300]}", status) from exc
        return _concat_json_docs(out) if out.strip() else None

    def _rest_request(self, method, path, params, body, paginate):
        url = f"{API_ROOT}/{path.lstrip('/')}"
        if params:
            url += "?" + urllib.parse.urlencode(sorted(params.items()))
        results = None
        while url:
            data, headers = self._rest_once(method, url, body)
            if not paginate:
                return data
            if isinstance(data, list):
                results = (results or []) + data
            elif isinstance(data, dict) and isinstance(data.get("items"), list):
                # search API: merge the items list, keep the envelope
                if results is None:
                    results = data
                else:
                    results["items"].extend(data["items"])
            else:
                return data
            url = _next_link(headers.get("Link", ""))
        return results

    def _rest_once(self, method, url, body):
        payload = None
        headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {self.token}",
            "User-Agent": USER_AGENT,
            "X-GitHub-Api-Version": "2022-11-28",
        }
        if body is not None and method != "GET":
            payload = json.dumps(body).encode()
            headers["Content-Type"] = "application/json"
        req = urllib.request.Request(url, data=payload, method=method, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                raw = resp.read()
                text = raw.decode("utf-8") if raw else ""
                return (json.loads(text) if text.strip() else None), dict(resp.headers)
        except urllib.error.HTTPError as exc:
            detail = ""
            try:
                detail = exc.read().decode("utf-8", "replace")[:300]
            except Exception:  # noqa: BLE001
                pass
            cls = GhNotFound if exc.code == 404 else GhError
            raise cls(f"{method} {url} -> HTTP {exc.code}: {detail}", exc.code) from exc
        except urllib.error.URLError as exc:
            raise GhError(f"{method} {url} failed: {exc.reason}") from exc

    # -- typed reads -------------------------------------------------------

    def list_open_prs(self) -> list[dict]:
        return self.get(f"repos/{self.repo}/pulls", {"state": "open"}, paginate=True) or []

    def pr(self, number: int) -> dict:
        return self.get(f"repos/{self.repo}/pulls/{number}")

    def pr_files(self, number: int) -> list[dict]:
        return self.get(f"repos/{self.repo}/pulls/{number}/files", paginate=True) or []

    def pr_commits(self, number: int) -> list[dict]:
        return self.get(f"repos/{self.repo}/pulls/{number}/commits", paginate=True) or []

    def issue_comments(self, number: int) -> list[dict]:
        return self.get(f"repos/{self.repo}/issues/{number}/comments", paginate=True) or []

    def review_comments(self, number: int) -> list[dict]:
        return self.get(f"repos/{self.repo}/pulls/{number}/comments", paginate=True) or []

    def reviews(self, number: int) -> list[dict]:
        return self.get(f"repos/{self.repo}/pulls/{number}/reviews", paginate=True) or []

    def requested_reviewers(self, number: int) -> dict:
        return self.get(f"repos/{self.repo}/pulls/{number}/requested_reviewers") or {}

    def check_runs(self, sha: str) -> list[dict]:
        data = self.get(f"repos/{self.repo}/commits/{sha}/check-runs", {"per_page": 100}) or {}
        return data.get("check_runs", []) if isinstance(data, dict) else []

    def commit_statuses(self, sha: str) -> list[dict]:
        return self.get(f"repos/{self.repo}/commits/{sha}/statuses", paginate=True) or []

    def contents(self, path: str, ref: str) -> str | None:
        """Decoded text of a file at `ref`, or None when absent."""
        try:
            data = self.get(f"repos/{self.repo}/contents/{path}", {"ref": ref})
        except GhNotFound:
            return None
        if not isinstance(data, dict) or data.get("encoding") != "base64":
            return None
        return base64.b64decode(data.get("content") or "").decode("utf-8", "replace")

    def org_member(self, org: str, login: str) -> bool | None:
        """True/False for a definitive answer, None when the token can't see
        membership (403) — callers must not assume internal on None."""
        try:
            self.get(f"orgs/{org}/members/{login}")
            return True
        except GhNotFound:
            return False
        except GhError as exc:
            if exc.status in (302, 403):
                return None
            raise

    def team_exists(self, org: str, slug: str) -> bool | None:
        """Whether `org/slug` is a GitHub team the token can see: True/False
        on a definitive answer, None when the token can't read teams (403).
        The route target prefers the team and falls back to a person only on
        False or None, so a team that lands later is picked up on the next
        collect without any config change."""
        try:
            self.get(f"orgs/{org}/teams/{slug}")
            return True
        except GhNotFound:
            return False
        except GhError as exc:
            if exc.status in (302, 403):
                return None
            raise

    def me(self) -> str | None:
        """The token's login (`GET /user`), or None when the backend can't say."""
        try:
            data = self.get("user")
        except GhError:
            return None
        return (data or {}).get("login") if isinstance(data, dict) else None

    def merged_pr_count_by_author(self, login: str) -> int:
        q = f"repo:{self.repo} is:pr is:merged {search_author_q(login)}"
        data = self.get("search/issues", {"q": q, "per_page": 1}) or {}
        return int(data.get("total_count") or 0)

    # -- typed writes ------------------------------------------------------

    def create_review(self, number: int, event: str, body: str) -> dict:
        return self.post(f"repos/{self.repo}/pulls/{number}/reviews", {"event": event, "body": body}) or {}

    def merge(self, number: int, sha: str, method: str = "squash") -> dict:
        return self.put(f"repos/{self.repo}/pulls/{number}/merge", {"sha": sha, "merge_method": method}) or {}

    def comment(self, number: int, body: str) -> dict:
        return self.post(f"repos/{self.repo}/issues/{number}/comments", {"body": body}) or {}

    def update_pr(self, number: int, **fields) -> dict:
        return self.patch(f"repos/{self.repo}/pulls/{number}", fields) or {}

    def add_labels(self, number: int, labels: list[str]) -> dict:
        return self.post(f"repos/{self.repo}/issues/{number}/labels", {"labels": labels}) or {}

    def close_pr(self, number: int) -> dict:
        return self.update_pr(number, state="closed")

    def request_reviewers(self, number: int, reviewers: list[str], team_reviewers: list[str]) -> dict:
        body = {}
        if reviewers:
            body["reviewers"] = reviewers
        if team_reviewers:
            body["team_reviewers"] = team_reviewers
        return self.post(f"repos/{self.repo}/pulls/{number}/requested_reviewers", body) or {}

    def dispatch_workflow(self, workflow_file: str, ref: str, inputs: dict | None = None) -> dict:
        body = {"ref": ref}
        if inputs:
            body["inputs"] = inputs
        return self.post(f"repos/{self.repo}/actions/workflows/{workflow_file}/dispatches", body) or {}


def pick_backend(*, snapshot_dir: Path | None = None, token: str | None = None) -> str:
    if snapshot_dir:
        return "snapshot"
    if shutil.which("gh"):
        return "gh"
    if token:
        return "rest"
    raise GhError("no GitHub backend: install `gh`, or set GITHUB_TOKEN / GH_TOKEN, or pass a snapshot dir")


_LINK_NEXT_RE = re.compile(r'<([^>]+)>;\s*rel="next"')


def _next_link(link_header: str) -> str | None:
    m = _LINK_NEXT_RE.search(link_header or "")
    return m.group(1) if m else None


# ---- CLI ----------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--repo", default=DEFAULT_REPO)
    ap.add_argument("--backend", default="auto", choices=("auto", "gh", "rest", "snapshot"))
    ap.add_argument("--snapshot-dir")
    ap.add_argument("--record-dir", help="mirror live GET responses into this snapshot dir")
    ap.add_argument("--get", metavar="PATH", help="fetch one endpoint and print JSON")
    ap.add_argument("--paginate", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    return ap


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.self_test:
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        import test_gh_client  # noqa: PLC0415 — the pytest file doubles as the harness
        return test_gh_client.run_standalone()
    if not args.get:
        build_parser().print_help()
        return 2
    gh = GhClient(args.repo, args.backend, snapshot_dir=args.snapshot_dir, record_dir=args.record_dir)
    print(json.dumps(gh.get(args.get, paginate=args.paginate), indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
