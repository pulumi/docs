# Content-review PR body template

Fill **every** section below and pass the result to `gh pr create --body-file`.
The worker re-lints the branch and checks that each `##` heading here is present
in the PR body; a missing section is flagged (non-blocking) on the PR. Keep the
diff to high-confidence fixes — judgment-level items belong in *Findings not
applied*, not in the diff.

The template starts after this line — copy from the first `##` heading down.

---

## Why this page

Lane, strategic tier, traffic figure + report period, and last-reviewed date
(from the queue entry) — so a reviewer can see how this page was selected.

## Fixes applied

One row per change. If zero fixes were applied this section is empty and no PR
should exist.

| Claim / finding | Authoritative source | Correction |
| --- | --- | --- |
|  |  |  |

## Findings not applied

Every skipped finding with one line of reasoning (why it's judgment-level, not a
high-confidence fix).

For the judgment-level items above, run `/glow-up <path>`.

## Screenshot check

Per image: current / stale (what differs) / unverifiable. Note any aging
reference screenshots (see `references/screenshot-verification.md`).

## Rendered content

Outcomes of the rendered pass — residue claims checked in the HTML view, the
markdown view's shortcode-template status, and any shared-source
(shortcode / partial / data) findings with their page-reach
("also rendered on N other pages").

## Verification

Confirm `make lint` + `make build` passed, and which pre-step artifacts informed
the review (note any pre-step that failed or was missing).
