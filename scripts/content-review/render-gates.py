#!/usr/bin/env python3
"""Deterministic gates for the content-review screenshot and rendered passes.

The screenshot pass (skill step 4) and the rendered-content pass (skill step 6)
are per-page Opus work that, across every content-review PR to date, has
produced zero applied fixes: the docs pages reviewed reference no content
images, and their render-time content is navigation chrome or the page's own
authored prose, not data-sourced claims. Rather than run both passes (and the
full `make build` the rendered pass depends on) on every article, this computes
— by a cheap source grep — whether either pass has anything to look at. The
composer fills the corresponding PR-body sections deterministically when a gate
is off, and the worker runs the pass only when it is on.

  * has_images — the source body references a content image (a markdown image,
    an `<img>`, or an image-bearing shortcode like `figure`/`video`). The
    generic shared `meta_image` frontmatter card is NOT a content image, so a
    page carrying only that reads as has_images=false.
  * needs_render_pass — the source uses a shortcode/partial/include that can
    inject content the source markdown does not itself show, i.e. ANY shortcode
    not on the render-safe allowlist below. Pages built from plain prose, code
    tabs, callouts, and stepper chrome have no such residue.

Both gates are DEFAULT-SAFE: an unrecognized shortcode trips needs_render_pass
(the pass runs), and the caller treats a missing/unreadable source as "run both
passes" — so the optimization can only ever skip work that is provably absent,
never silently drop a page that might have something to check.

Usage:
    render-gates.py --path content/docs/.../_index.md        # JSON to stdout
    render-gates.py --self-test                              # offline checks
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# Hugo shortcodes that render the page's OWN authored content or pure
# navigation chrome — never data/-sourced or partial-included prose that the
# source markdown does not already contain. A page using ONLY these (or none)
# has no render-time content residue, so the rendered-content pass has nothing
# extra to verify.
#
# CONSERVATIVE BY DESIGN: any shortcode NOT listed here trips the gate, so a new
# or content-bearing shortcode is never silently skipped. Add an entry only
# after confirming it carries no external content. (Deliberately excluded:
# `langfile` and `get-started-install-body`, which embed file/partial content
# the source markdown does not show — exactly the residue the pass exists for.)
RENDER_SAFE_SHORTCODES = {
    "chooser", "choosable",     # language / code tabs — the page's own code
    "notes", "note",            # callout boxes — the page's own text
    "get-started-stepper",      # get-started prev/next navigation chrome
    "tabs", "tab",              # tabbed display of the page's own content
}

# Opening or closing shortcode tag: `{{< name`, `{{% name`, `{{< /name`, etc.
SHORTCODE_RE = re.compile(r"\{\{[<%]\s*/?\s*([A-Za-z0-9_-]+)")

# A content image: markdown image, HTML <img>, or an image-bearing shortcode.
# `meta_image:` frontmatter is intentionally not matched (it's the shared card).
IMAGE_RE = re.compile(r"!\[|<img[\s/>]|\{\{[<%]\s*(?:figure|video|image|img)\b")


def analyze(text: str) -> dict:
    """Compute both gates from an article's raw source markdown."""
    shortcodes = sorted(set(SHORTCODE_RE.findall(text)))
    nonchrome = sorted(s for s in shortcodes if s not in RENDER_SAFE_SHORTCODES)
    image_count = len(IMAGE_RE.findall(text))
    return {
        "shortcodes": shortcodes,
        "nonchrome_shortcodes": nonchrome,
        "needs_render_pass": bool(nonchrome),
        "has_images": image_count > 0,
        "image_count": image_count,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--path", help="article source markdown to analyze")
    ap.add_argument("--self-test", action="store_true", help="run offline checks")
    args = ap.parse_args()

    if args.self_test:
        return self_test()
    if not args.path:
        ap.error("--path is required (or use --self-test)")

    text = Path(args.path).read_text()
    json.dump(analyze(text), sys.stdout, sort_keys=True)
    sys.stdout.write("\n")
    return 0


def self_test() -> int:
    failures = []

    def check(name, cond):
        print(("ok: " if cond else "FAIL: ") + name,
              file=sys.stdout if cond else sys.stderr)
        if not cond:
            failures.append(name)

    plain = analyze("# Title\n\nJust prose and a `code` span.\n\n```go\nx := 1\n```\n")
    check("plain prose: no render pass", plain["needs_render_pass"] is False)
    check("plain prose: no images", plain["has_images"] is False)
    check("plain prose: no shortcodes", plain["shortcodes"] == [])

    safe = analyze(
        "{{< chooser language \"typescript\" >}}\n{{% choosable %}}\ncode\n{{% /choosable %}}\n"
        "{{< /chooser >}}\n{{< notes >}}a note{{< /notes >}}\n{{< get-started-stepper >}}\n"
    )
    check("chrome-only: no render pass", safe["needs_render_pass"] is False)
    check("chrome-only: closing tags add no phantom names",
          safe["shortcodes"] == ["choosable", "chooser", "get-started-stepper", "notes"])

    langfile = analyze("intro\n{{< langfile >}}\n{{< chooser >}}x{{< /chooser >}}\n")
    check("langfile trips the gate", langfile["needs_render_pass"] is True)
    check("langfile is the only non-chrome trigger", langfile["nonchrome_shortcodes"] == ["langfile"])

    install = analyze("{{< get-started-install-body >}}\n")
    check("get-started-install-body trips the gate", install["needs_render_pass"] is True)

    md_img = analyze("Here is a diagram:\n\n![architecture](/images/arch.png)\n")
    check("markdown image: has_images", md_img["has_images"] is True)
    check("markdown image alone: no render pass", md_img["needs_render_pass"] is False)

    html_img = analyze('<img src="/images/x.png" alt="x">\n')
    check("html <img>: has_images", html_img["has_images"] is True)

    figure = analyze("{{< figure src=\"/images/x.png\" >}}\n")
    check("figure shortcode: has_images", figure["has_images"] is True)
    check("figure shortcode: also trips render pass (not chrome)",
          figure["needs_render_pass"] is True)

    meta_only = analyze("---\ntitle: X\nmeta_image: /images/docs/meta-images/docs-meta.png\n---\n\nProse.\n")
    check("meta_image only: not a content image", meta_only["has_images"] is False)

    mixed = analyze("{{< notes >}}n{{< /notes >}}\n{{< langfile >}}\n{{< pulumi-examples >}}\n")
    check("mixed safe+unsafe: only unsafe listed",
          mixed["nonchrome_shortcodes"] == ["langfile", "pulumi-examples"])
    check("mixed: image_count is zero", mixed["image_count"] == 0)

    if failures:
        print(f"\n{len(failures)} failure(s)", file=sys.stderr)
        return 1
    print("\nall render-gates self-tests passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
