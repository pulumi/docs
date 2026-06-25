# Content-review PR body template

You do **not** author this body from scratch. The workflow composes
`.pr-body-draft.md` (via `compose-pr-body.py`) — every section present, the
facts rendered, each pre-found finding pre-bucketed with a `<TODO>`. **Edit that
draft** and pass it to `gh pr create --body-file .pr-body-draft.md`. This file is
the reference for what each section must contain; the re-lint gate checks that
every `##` heading survives. Keep the diff to high-confidence fixes —
judgment-level items belong in *Findings not applied*, not in the diff.

The sections, and what's yours vs. the composer's:

## Why this page

Rendered by the composer from the selection queue (lane, strategic tier, traffic
figure + report period, last-reviewed). **Leave verbatim** — its figures are
authoritative; do not re-narrate it.

## Fixes applied

Pre-stubbed by the composer with one row per high-confidence finding. Keep a row
ONLY for a fix you actually applied (fill its Correction); move the rest to
*Findings not applied*. If zero fixes were applied this section is empty and no
PR should exist.

| Claim / finding | Authoritative source | Correction |
| --- | --- | --- |
|  |  |  |

## Findings not applied

Pre-stubbed with the lower-confidence findings; add any row you moved down from
*Fixes applied*. One line of reasoning each (why it's judgment-level, not a
high-confidence fix).

For the judgment-level items above, run `/glow-up <path>`.

## Screenshot check

Gated — the composer pre-fills "No images." when the source references no
content images, and you leave it as-is. Only when this section carries a
`<TODO>` (the page has images) do you run the pass and report per image:
current / stale (what differs) / unverifiable, plus any aging reference
screenshots (see `references/screenshot-verification.md`).

## Rendered content

Gated — the composer pre-fills "Skipped" when the source uses no content-bearing
shortcode/partial/include (it names the triggering shortcode when one is
present). Only when this section carries a `<TODO>` do you run `make build` and
the rendered pass, then report its outcomes — residue claims checked in the HTML
view, the markdown view's shortcode-template status, and any shared-source
(shortcode / partial / data) findings with their page-reach
("also rendered on N other pages").

## Verification

The composer renders the pre-step artifact inventory here. The `make lint`
result is **not** yours to assert: leave the `<!-- LINT-RESULT -->` line
untouched — the workflow's re-lint gate stamps it with the authoritative
outcome. Note any pre-step that failed or was missing.
