#!/usr/bin/env python3
"""Tests for publish-gate.py.

Self-contained — run with `python3 test_publish_gate.py` (no pytest dep).
Writes fixture queue/verdict/patch/paths files into a temp dir and shells out
to the script, asserting on exit codes and the emitted outputs (captured via
a GITHUB_OUTPUT file so the test sees exactly what the workflow would).
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPT = HERE / "publish-gate.py"

ARTICLE = "content/docs/iac/concepts/stacks/_index.md"
SLUG = "docs-iac-concepts-stacks"

_failures: list[str] = []
_passes = 0


def check(cond: bool, msg: str) -> None:
    global _passes
    if cond:
        _passes += 1
    else:
        _failures.append(msg)
        print(f"  FAIL: {msg}", file=sys.stderr)


def run_gate(tmp: Path, *, queue=None, verdict=None, patch: str | None = "",
             paths: list[str] | None = None) -> tuple[int, dict[str, str], str]:
    """Run the gate against fixtures; return (exit code, outputs, stderr+stdout)."""
    queue_file = tmp / "queue.json"
    queue_file.write_text(json.dumps(
        queue if queue is not None else {"articles": [
            {"path": ARTICLE, "slug": SLUG, "no_retire": False},
        ]}))
    verdict_file = tmp / "verdict.json"
    verdict_file.unlink(missing_ok=True)
    if verdict is not None:
        verdict_file.write_text(json.dumps(verdict))
    patch_file = tmp / "changes.patch"
    patch_file.unlink(missing_ok=True)
    if patch is not None:
        patch_file.write_text(patch)
    cmd = [sys.executable, str(SCRIPT),
           "--queue", str(queue_file),
           "--verdict", str(verdict_file),
           "--patch", str(patch_file)]
    if paths is not None:
        paths_file = tmp / "changes.paths"
        paths_file.write_bytes(b"\0".join(p.encode() for p in paths) + (b"\0" if paths else b""))
        cmd += ["--paths-from", str(paths_file)]
    out_file = tmp / "github_output"
    out_file.write_text("")
    env = {**os.environ, "GITHUB_OUTPUT": str(out_file)}
    proc = subprocess.run(cmd, capture_output=True, text=True, env=env)
    outputs = {}
    for line in out_file.read_text().splitlines():
        if "=" in line:
            k, v = line.split("=", 1)
            outputs[k] = v
    return proc.returncode, outputs, proc.stdout + proc.stderr


def fixed_verdict(**over) -> dict:
    v = {"verdict": "fixed", "reason": "", "fixes": 2,
         "skipped_findings": 1, "retirement": False}
    v.update(over)
    return v


def main() -> int:
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)

        print("fixed verdict with a non-empty patch publishes")
        code, out, _ = run_gate(tmp, verdict=fixed_verdict(), patch="diff --git a/x b/x\n")
        check(code == 0, f"expected pass, got exit {code}")
        check(out.get("publish") == "true", f"expected publish=true, got {out}")
        check(out.get("branch") == f"content-review/{SLUG}", f"bad branch: {out}")

        print("fixed verdict with an empty patch is a violation")
        code, _, err = run_gate(tmp, verdict=fixed_verdict(), patch="")
        check(code == 1, f"expected exit 1, got {code}")
        check("empty" in err, "expected an empty-patch error")

        print("clean verdict with an empty patch passes and does not publish")
        code, out, _ = run_gate(
            tmp, verdict={"verdict": "clean", "reason": "no findings",
                          "fixes": 0, "skipped_findings": 0, "retirement": False},
            patch="")
        check(code == 0, f"expected pass, got exit {code}")
        check(out.get("publish") == "false", f"expected publish=false, got {out}")

        print("clean verdict with a non-empty patch is a violation")
        code, _, _ = run_gate(
            tmp, verdict={"verdict": "clean", "reason": "no findings",
                          "fixes": 0, "skipped_findings": 0, "retirement": False},
            patch="diff --git a/x b/x\n")
        check(code == 1, f"expected exit 1, got {code}")

        print("skipped verdict passes and does not publish")
        code, out, _ = run_gate(
            tmp, verdict={"verdict": "skipped", "reason": "open PR exists",
                          "fixes": 0, "skipped_findings": 0, "retirement": False},
            patch="")
        check(code == 0 and out.get("publish") == "false",
              f"expected pass/publish=false, got exit {code}, {out}")

        print("absent verdict passes and does not publish")
        code, out, _ = run_gate(tmp, verdict=None, patch="")
        check(code == 0 and out.get("publish") == "false",
              f"expected pass/publish=false, got exit {code}, {out}")

        print("unrecognized verdict is a violation")
        code, _, err = run_gate(tmp, verdict=fixed_verdict(verdict="merged"),
                                patch="diff --git a/x b/x\n")
        check(code == 1, f"expected exit 1, got {code}")
        check("unrecognized verdict" in err, "expected an unrecognized-verdict error")

        print("malformed verdict JSON is a violation")
        bad = tmp / "bad-verdict.json"
        bad.write_text("{not json")
        patch_file = tmp / "changes.patch"
        patch_file.write_text("")
        proc = subprocess.run(
            [sys.executable, str(SCRIPT), "--queue", str(tmp / "queue.json"),
             "--verdict", str(bad), "--patch", str(patch_file)],
            capture_output=True, text=True)
        check(proc.returncode == 1, f"expected exit 1, got {proc.returncode}")

        print("scope: fix patch touching only the article passes")
        code, _, _ = run_gate(tmp, verdict=fixed_verdict(),
                              patch="diff --git a/x b/x\n", paths=[ARTICLE])
        check(code == 0, f"expected pass, got exit {code}")

        print("scope: fix patch touching a shared render-time source passes")
        code, _, _ = run_gate(tmp, verdict=fixed_verdict(),
                              patch="diff --git a/x b/x\n",
                              paths=[ARTICLE, "layouts/shortcodes/notes.html",
                                     "data/versions.json"])
        check(code == 0, f"expected pass, got exit {code}")

        print("scope: fix patch touching a workflow is a violation")
        code, _, err = run_gate(tmp, verdict=fixed_verdict(),
                                patch="diff --git a/x b/x\n",
                                paths=[ARTICLE, ".github/workflows/build-and-deploy.yml"])
        check(code == 1, f"expected exit 1, got {code}")
        check("outside the fix-PR scope" in err, "expected a scope error")

        print("class: deterministic-only categories with small churn")
        small_patch = "diff --git a/x b/x\n" + "-old line\n+new line\n"
        det_applied = [
            {"category": "link", "file": ARTICLE, "lines": [10, 10], "source": "dead link"},
            {"category": "vale", "file": ARTICLE, "lines": [20, 20], "source": "vale:x@L20"},
            {"category": "frontmatter", "file": ARTICLE, "lines": [2, 2], "source": "fm"},
        ]
        code, out, _ = run_gate(tmp, verdict=fixed_verdict(applied=det_applied),
                                patch=small_patch)
        check(code == 0 and out.get("class") == "deterministic",
              f"expected class=deterministic, got {out}")

        print("class: any claim/readthrough category -> judgment")
        for cat in ("claim", "readthrough"):
            mixed = det_applied + [{"category": cat, "file": ARTICLE,
                                    "lines": [30, 31], "source": f"{cat}:x"}]
            code, out, _ = run_gate(tmp, verdict=fixed_verdict(applied=mixed),
                                    patch=small_patch)
            check(code == 0 and out.get("class") == "judgment",
                  f"expected class=judgment for {cat}, got {out}")

        print("class: clarity_flag -> judgment even with deterministic categories")
        code, out, _ = run_gate(
            tmp, verdict=fixed_verdict(applied=det_applied, clarity_flag=True),
            patch=small_patch)
        check(out.get("class") == "judgment", f"expected class=judgment, got {out}")

        print("class: churn over the ceiling -> judgment")
        big_patch = "diff --git a/x b/x\n" + "+line\n" * 41
        code, out, _ = run_gate(tmp, verdict=fixed_verdict(applied=det_applied),
                                patch=big_patch)
        check(out.get("class") == "judgment", f"expected class=judgment, got {out}")

        print("class: empty applied[] -> judgment (nothing to certify)")
        code, out, _ = run_gate(tmp, verdict=fixed_verdict(applied=[]),
                                patch=small_patch)
        check(out.get("class") == "judgment", f"expected class=judgment, got {out}")

        print("class: clean verdict -> none")
        code, out, _ = run_gate(
            tmp, verdict={"verdict": "clean", "reason": "no findings",
                          "fixes": 0, "skipped_findings": 0, "retirement": False},
            patch="")
        check(out.get("class") == "none", f"expected class=none, got {out}")

        print("class: retirement -> judgment (never merges on a bot stamp)")
        code, out, _ = run_gate(
            tmp,
            queue={"articles": [{"path": ARTICLE, "slug": SLUG, "no_retire": False}]},
            verdict=fixed_verdict(retirement=True, applied=det_applied),
            patch=small_patch)
        check(code == 0 and out.get("class") == "judgment",
              f"expected class=judgment for retirement, got exit {code}, {out}")

        print("reported: never publishes, and its patch must be empty")
        reported = {"verdict": "reported", "reason": "claim list recorded",
                    "fixes": 0, "skipped_findings": 0, "retirement": False}
        code, out, _ = run_gate(tmp, verdict=reported, patch="")
        check(code == 0 and out.get("publish") == "false",
              f"expected publish=false for reported, got exit {code}, {out}")
        check(out.get("class") == "none", f"expected class=none, got {out}")

        code, _, err = run_gate(tmp, verdict=reported, patch=small_patch)
        check(code == 1 and "non-empty" in err,
              f"expected a non-empty-patch violation for reported, got {code}")

        print("reported: retirement combination is a violation")
        code, _, err = run_gate(
            tmp,
            queue={"articles": [{"path": ARTICLE, "slug": SLUG, "no_retire": False}]},
            verdict={**reported, "retirement": True}, patch="")
        check(code == 1 and "cannot propose retirement" in err,
              f"expected reported+retirement violation, got {code}")

        print("glowup: publishes on its own branch with class glow-up")
        code, out, _ = run_gate(tmp, verdict=fixed_verdict(verdict="glowup"),
                                patch=small_patch)
        check(code == 0 and out.get("publish") == "true",
              f"expected publish=true, got exit {code}, {out}")
        check(out.get("branch") == f"content-review/glowup-{SLUG}",
              f"expected glowup branch, got {out}")
        check(out.get("glowup") == "true" and out.get("class") == "glow-up",
              f"expected glowup=true class=glow-up, got {out}")

        print("glowup: empty patch is a violation")
        code, _, err = run_gate(tmp, verdict=fixed_verdict(verdict="glowup"), patch="")
        check(code == 1 and "empty" in err, f"expected empty-patch violation, got {code}")

        print("glowup: retirement combination is a violation")
        code, _, err = run_gate(
            tmp,
            queue={"articles": [{"path": ARTICLE, "slug": SLUG, "no_retire": False}]},
            verdict=fixed_verdict(verdict="glowup", retirement=True),
            patch=small_patch)
        check(code == 1 and "cannot also propose retirement" in err,
              f"expected glowup+retirement violation, got {code}")

        print("glowup scope: bundle asset allowed, sibling article and shared source not")
        bundle_asset = ARTICLE.rsplit("/", 1)[0] + "/diagram.png"
        code, _, _ = run_gate(tmp, verdict=fixed_verdict(verdict="glowup"),
                              patch=small_patch, paths=[ARTICLE, bundle_asset])
        check(code == 0, f"bundle asset should pass, got exit {code}")
        sibling = ARTICLE.rsplit("/", 1)[0] + "/other.md"
        code, _, err = run_gate(tmp, verdict=fixed_verdict(verdict="glowup"),
                                patch=small_patch, paths=[ARTICLE, sibling])
        check(code == 1 and "glow-up-PR scope" in err,
              f"sibling article should fail, got exit {code}")
        code, _, err = run_gate(tmp, verdict=fixed_verdict(verdict="glowup"),
                                patch=small_patch,
                                paths=[ARTICLE, "layouts/shortcodes/notes.html"])
        check(code == 1, f"shared render source should fail for glowup, got exit {code}")

        print("scope: fix patch touching a sibling doc is a violation")
        code, _, _ = run_gate(tmp, verdict=fixed_verdict(),
                              patch="diff --git a/x b/x\n",
                              paths=[ARTICLE, "content/docs/iac/concepts/projects/_index.md"])
        check(code == 1, f"expected exit 1, got {code}")

        print("retirement on a retirable page passes with the retire- branch")
        code, out, _ = run_gate(
            tmp, verdict=fixed_verdict(retirement=True),
            patch="diff --git a/x b/x\n",
            paths=[ARTICLE, "content/docs/iac/concepts/projects/_index.md",
                   "scripts/redirects/docs.txt", "data/docs_menu_sections.yml"])
        check(code == 0, f"expected pass, got exit {code}")
        check(out.get("branch") == f"content-review/retire-{SLUG}", f"bad branch: {out}")
        check(out.get("retirement") == "true", f"expected retirement=true, got {out}")

        print("retirement scope excludes non-content paths")
        code, _, _ = run_gate(
            tmp, verdict=fixed_verdict(retirement=True),
            patch="diff --git a/x b/x\n",
            paths=[ARTICLE, "layouts/shortcodes/notes.html"])
        check(code == 1, f"expected exit 1, got {code}")

        print("no_retire: true vetoes a retirement verdict")
        code, _, err = run_gate(
            tmp,
            queue={"articles": [{"path": ARTICLE, "slug": SLUG, "no_retire": True}]},
            verdict=fixed_verdict(retirement=True),
            patch="diff --git a/x b/x\n")
        check(code == 1, f"expected exit 1, got {code}")
        check("no_retire" in err, "expected a no_retire error")

        print("a queue entry missing no_retire is treated as protected")
        code, _, _ = run_gate(
            tmp, queue={"articles": [{"path": ARTICLE, "slug": SLUG}]},
            verdict=fixed_verdict(retirement=True),
            patch="diff --git a/x b/x\n")
        check(code == 1, f"expected exit 1, got {code}")

        print("a queue with zero or many articles is a violation")
        code, _, _ = run_gate(tmp, queue={"articles": []},
                              verdict=fixed_verdict(), patch="diff --git a/x b/x\n")
        check(code == 1, f"expected exit 1, got {code}")
        code, _, _ = run_gate(
            tmp,
            queue={"articles": [{"path": ARTICLE, "slug": SLUG},
                                {"path": "content/docs/other.md", "slug": "other"}]},
            verdict=fixed_verdict(), patch="diff --git a/x b/x\n")
        check(code == 1, f"expected exit 1, got {code}")

    print(f"\n{_passes} checks passed, {len(_failures)} failed")
    return 1 if _failures else 0


if __name__ == "__main__":
    sys.exit(main())
