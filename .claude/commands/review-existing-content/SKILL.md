---
name: review-existing-content
description: Review existing documentation pages selected by the daily content-review workflow. Runs the docs-review claim pipeline over whole files via synthetic diffs, applies high-confidence fixes only, and opens one auditable PR per article. Invoked by the review-existing-content workflow; not user-invocable.
user-invocable: false
---

# Review Existing Content

You are reviewing existing documentation pages — not a PR diff. The selection
script has already chosen today's articles; your job is to run the docs-review
machinery over each whole file, apply only the fixes you can defend with an
authoritative source, and open one ready PR per article. Everything
judgment-level goes in the PR description for a human, not in the diff.

## Input

Read `.content-review-queue.json` from the repo root (written by
`scripts/content-review/select-articles.py`). Shape:

```json
{
  "generated": "2026-06-12T14:00:00+00:00",
  "count": 3,
  "halted": null,
  "traffic": { "available": true, "period": "2026-05", "pages_matched": 731 },
  "articles": [
    { "path": "content/docs/iac/concepts/stacks/_index.md",
      "url": "/docs/iac/concepts/stacks/",
      "slug": "docs-iac-concepts-stacks",
      "lane": "priority",
      "tier": 1,
      "no_retire": true,
      "monthly_visits": 12345,
      "last_reviewed": null,
      "score": 0.91 }
  ]
}
```

- `lane` — `priority` (scored pick) or `manual` (workflow_dispatch override).
- `no_retire` — when true, retirement must never be proposed for this page.
  This is the **hard veto** on retirement — honor it regardless of evidence.
- If `articles` is empty or `halted` is set, do nothing (the workflow won't
  invoke you in that case, but be defensive).

Process articles **sequentially**, one at a time, completing each article's
branch and PR before starting the next.

## Per-article procedure

### 1. Branch

From up-to-date `master`, create the branch with the **exact** name
`content-review/<slug>` (the queue entry's `slug`). For a retirement proposal
(see below) use `content-review/retire-<slug>` instead. The
workflow derives the PR from this branch name, so it must match exactly. If an
open PR already exists for that branch name, skip the article entirely and set
`"verdict": "skipped"` in the sentinel (step 8): a previous run owns it.

### 2. Pre-compute (deterministic floor) — the workflow runs this for you

The `content-review-article` workflow generates the synthetic whole-file diff
and runs the docs-review pre-steps **before invoking you**, exactly as the PR
review workflow does. The artifacts are already at the repo root when you
start: `.fetched-urls.json`, `.candidate-claims.json`, `.verified-claims.json`,
`.vale-findings.json`, `.frontmatter-validation.json`, and
`.cross-sibling-discovery.json`. **Read them — do not regenerate them.**

For reference (and for local runs outside CI), the exact pipeline the workflow
executes — scripts live in `.claude/commands/docs-review/scripts/`:

```bash
git diff --no-index /dev/null <path> > .synthetic.patch || true

python3 .claude/commands/docs-review/scripts/extract-urls-and-fetch.py \
    --patch-file .synthetic.patch --out .fetched-urls.json
python3 .claude/commands/docs-review/scripts/extract-claims.py \
    --patch-file .synthetic.patch --out .candidate-claims-regex.json
python3 .claude/commands/docs-review/scripts/extract-claims-llm.py \
    --patch-file .synthetic.patch --changed-files <path> \
    --pass atomic --scrutiny standard --out .candidate-claims-llm-1.json
python3 .claude/commands/docs-review/scripts/extract-claims-llm.py \
    --patch-file .synthetic.patch --changed-files <path> \
    --pass holistic --scrutiny standard --out .candidate-claims-llm-2.json
python3 .claude/commands/docs-review/scripts/merge-claims.py \
    --regex .candidate-claims-regex.json \
    --llm .candidate-claims-llm-1.json --llm .candidate-claims-llm-2.json \
    --out .candidate-claims.json
python3 .claude/commands/docs-review/scripts/verify-claims.py \
    --in .candidate-claims.json --fetched-urls .fetched-urls.json \
    --out .verified-claims.json
python3 .claude/commands/docs-review/scripts/frontmatter-validate.py \
    --changed-files <path> --out .frontmatter-validation.json
python3 .claude/commands/docs-review/scripts/cross-sibling-discover.py \
    --changed-files <path> --out .cross-sibling-discovery.json
```

Run Vale the way the review workflow does, in whole-file mode (no `--pr`):

```bash
vale --no-exit --output=JSON <path> > .vale-raw.json 2>/dev/null || echo '{}' > .vale-raw.json
python3 .claude/commands/docs-review/scripts/vale-findings-filter.py \
    --in .vale-raw.json --out .vale-findings.json || echo '[]' > .vale-findings.json
```

If any artifact is missing or carries an `errors` field, continue with the
artifacts you have and say so in the PR description; never fabricate artifact
contents. (Consult flag names with `--help` if running a script by hand —
do not guess alternate flags.)

### 3. Triage and fix — HIGH-CONFIDENCE ONLY

Read the artifacts and triage per
`docs-review:references:pre-computation`'s contract (scripts find facts; you
make editorial judgments). The bar for **applying** a fix is strict. Apply
only:

- **Contradicted claims with an unambiguous correction** — `.verified-claims.json`
  verdict `contradicted` or `mismatch`, where the authoritative source states
  the correct value outright (a version number, a price, a flag name). If the
  correction requires interpretation, do not apply it.
- **Dead or redirected internal links** — fix to the canonical full path
  (`/docs/...`, never `../`).
- **Frontmatter violations** from `.frontmatter-validation.json` (broken menu
  parent, alias collision).
- **Unambiguous Vale errors** — spelling, repo terminology (per
  `docs-review:references:spelling-grammar`); not style suggestions.

Everything else — `unverifiable` verdicts, low-confidence corrections,
prose-quality findings, structural suggestions, anything you'd phrase with
"consider" — goes in the PR description's **Findings not applied** section
(one line of reasoning each), not in the diff. That list is the
almost-made-the-cut record the human reviewer adjudicates.

Editing guardrails:

- Never rewrite prose beyond the specific correction.
- Ordered lists keep their `1.` numbering; files end with a newline; H1 Title
  Case, H2+ sentence case (see `STYLE-GUIDE.md` — but don't re-case headings
  that aren't otherwise wrong).
- Never edit anything under a tier-0 (generated) path — selection excludes
  them, but be defensive.
- Never add the `automation/merge` label to anything.

### 4. Screenshot / UI pass

Follow `references/screenshot-verification.md` for every image the article
references. Verified-stale screenshots are **flagged in the PR description**
(Screenshot check section), never regenerated or deleted by you.

### 5. Validate and render

`make lint` and `make build` must pass on the branch. Fix what they surface;
if you cannot, drop the offending change rather than shipping a broken
build. The build also produces the rendered views the next step reads.

### 6. Rendered content pass (the customer-facing views)

Source review misses content the page assembles at render time — shared
snippets from shortcodes, values from `data/` files, partial-driven
sections. The customer sees the assembled page, so check both rendered
views `make build` just produced:

**HTML view** — `public/<url path>/index.html`:

1. Extract the main content area's text (skip nav/footer/banner chrome).
2. Compare against the source markdown's prose. Rendered text **absent from
   the source** is shortcode/data-sourced content — extract checkable
   claims from exactly that residue (it's small) and verify them through
   the same lanes as step 3.
3. Trace each residue finding to its origin: the shortcode call in the
   page source → `layouts/shortcodes/<name>.html` / partials / `data/`
   files. A fix at a shared source affects every page that includes it, so
   shared-source corrections meeting the high-confidence bar may be
   applied, and the PR description must flag them as multi-page
   ("also rendered on N other pages" — grep for other callers).

**Markdown view** — `public/<url path>/index.md` (the LLM/agent-facing
render; docs pages cascade `outputs: [HTML, markdown]`, and shortcodes
render through their `layouts/shortcodes/*.markdown.md` templates):

1. Read it and check for leaked shortcode syntax — literal `{{<` / `>}}`
   or `{{%` / `%}}` fragments in the output are the signature of a
   shortcode missing its markdown template.
2. Spot-check that content present in the HTML view isn't silently absent
   here (same missing-template failure, quieter symptom).
3. Fixes here are usually a new/corrected `*.markdown.md` shortcode
   template — shared-source again, same multi-page flagging rule. When the
   right rendering is debatable, it's a Findings-not-applied entry, not a
   fix.

If this pass applied any fix, re-run `make lint && make build` before
opening the PR.

### 7. PR — only when you applied a fix, ready (non-draft)

Open a **ready** PR to `master`. Build the body from
`references/pr-body-template.md` — fill **every** section — and create the PR
with `gh pr create --body-file`. The workflow re-runs `make lint` on your branch
(flipping the PR back to draft if it fails) and dispatches the automated docs
review over it afterward; humans merge. The template's sections (each one is
checked for):

- **Why this page**: lane, tier, traffic figure + report period, last
  reviewed (from the queue entry) — so the reviewer knows how it was chosen.
- **Fixes applied**: table of claim/finding → authoritative source →
  correction, one row per change.
- **Findings not applied**: every skipped finding with one line of reasoning.
  End the section with: "For the judgment-level items above, run
  `/glow-up <path>`."
- **Screenshot check**: per image — current / stale (what differs) /
  unverifiable; note any aging reference screenshots (see
  `references/screenshot-verification.md`).
- **Rendered content**: outcomes of the rendered pass — residue claims
  checked in the HTML view, the markdown view's shortcode-template status,
  and any shared-source (shortcode/partial/data) findings with their
  page-reach ("also rendered on N other pages").
- **Verification**: confirm `make lint` + `make build` passed and which
  pre-step artifacts informed the review (note any pre-step that failed).

Do **not** record `pr_number` or `head_sha` yourself — the workflow derives
them from the branch. A clean article (zero applicable fixes) skips the PR —
set `"verdict": "clean"` in the sentinel (next step).

### 8. Verdict sentinel — your only structured output

Write `.content-review-verdict.json` at the repo root. This is the **only**
file you produce for the workflow — do not write a ledger or a results file.
The workflow derives the PR facts (existence, number, head SHA) from your
branch, builds the canonical ledger record, and uploads it to S3 keyed by slug.

```json
{
  "verdict": "fixed",
  "reason": "",
  "fixes": 4,
  "skipped_findings": 2,
  "retirement": false
}
```

- `verdict`: `"fixed"` (you opened a PR), `"clean"` (zero applicable fixes, no
  PR), or `"skipped"` (a previous run already owns this page's PR).
- `reason`: one line — **required** for `clean` and `skipped`; omit/empty for
  `fixed`.
- `fixes`: applied changes; `skipped_findings`: Findings-not-applied count.
- `retirement`: `true` only for a retirement PR (branch
  `content-review/retire-<slug>`).

If you exit without writing this file, the workflow records the page as
`incomplete`. An incomplete outcome does **not** advance the staleness clock, so
the page stays due and is retried on a later sweep — up to an attempt cap, after
which it backs off for a human. Always write the sentinel, even for a clean or
skipped verdict.

## Retirement proposals

For any article with `"no_retire": false`, retirement is a valid outcome
**instead of** a fix PR when the strict evidence standard below is met.
`no_retire: true` is the primary guardrail and an absolute veto — never propose
retiring such a page no matter how strong the evidence. Retirement is no longer
restricted to a particular lane; it can be proposed on any review that clears
the bar, with the full reasoning documented in the PR.

- **Evidence required (two-sided):** the page appears in the traffic report
  with near-zero views (absence from the report is NOT evidence — the page
  may be new or alias-attributed), **and** GSC impressions/clicks are low
  over its window when that data is present; **or** the page is demonstrably
  redundant with a named page (cite `.cross-sibling-discovery.json`). Check
  the page's age in git — never propose retiring a page younger than a year.
- **Retire = redirect, never 404.** The PR must redirect the page to its
  superseding target: add the page's URL to the target's `aliases:` (or an
  S3 redirect under `scripts/redirects/` for non-Hugo paths), update inbound
  internal links in `/docs/`, `/product/`, `/tutorials/`, and remove the
  page + its menu entry. Follow `move-doc` reference mechanics.
- **Branch** `content-review/retire-<slug>`; PR description leads with the
  full evidence (traffic + GSC numbers and period, redundancy target,
  inbound-link inventory).
- When in doubt, don't propose retirement — review the page normally and
  note the low-traffic observation under Findings not applied.

## Output

The verdict sentinel (step 8) is your only output. The workflow records the
ledger and dispatches the docs review from it and from the branch — there is no
results file to write.
