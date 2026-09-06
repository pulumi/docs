---
name: review-existing-content
description: Review existing documentation pages selected by the daily content-review workflow. Runs the docs-review claim pipeline over whole files via synthetic diffs, applies high-confidence fixes only, and opens one auditable PR per article. Invoked by the review-existing-content workflow; not user-invocable.
user-invocable: false
---

# Review Existing Content

You are reviewing existing documentation pages — not a PR diff. The selection
script has already chosen today's articles; your job is to run the docs-review
machinery over each whole file and apply only the fixes you can defend with an
authoritative source. Everything judgment-level goes in the PR description for
a human, not in the diff.

You run **unprivileged**: the review job holds no push token, so you edit the
working tree only — never `git commit`, `git push`, or `gh pr create`. The
workflow's publish job validates your changes against a deterministic gate
(`scripts/content-review/publish-gate.py`: verdict shape, diff scope,
`no_retire`), derives the branch name from the queue, and opens the PR
(ready when the re-lint passes, draft only on lint failure) with the body you
edited. Changes outside the gate's scope are rejected
wholesale, so keep every edit inside the bounds each step names.

## Input

Read `.content-review-queue.json` from the repo root (written by
`scripts/content-review/select-articles.py`). Shape:

```json
{
  "generated": "2026-06-12T14:00:00+00:00",
  "count": 3,
  "mode": "fix",
  "halted": null,
  "traffic": { "available": true, "period": "2026-05", "pages_matched": 731 },
  "reader_signals": {
    "available": true,
    "gsc": { "available": true, "period": {"start": "2026-03-14", "end": "2026-06-11"},
             "pages_matched": 612, "median_ctr": 0.031, "max_impressions": 88012 },
    "feedback": { "available": true, "pages_matched": 214 }
  },
  "articles": [
    { "path": "content/docs/iac/concepts/stacks/_index.md",
      "url": "/docs/iac/concepts/stacks/",
      "slug": "docs-iac-concepts-stacks",
      "lane": "priority",
      "mode": "fix",
      "tier": 1,
      "no_retire": true,
      "editable": true,
      "monthly_visits": 12345,
      "signals": {
        "gsc": { "impressions": 15234, "ctr": 0.0205, "opportunity": 0.41,
                 "multiplier": 1.1025, "low_ctr_flag": true },
        "feedback": { "yes": 4, "no": 9, "neg_rate": 0.6923, "multiplier": 1.27 }
      },
      "last_reviewed": null,
      "stale_claims": 1,
      "stale_claim_markers": [
        { "entity_key": "version/pulumi-package",
          "claim_text": "Package source is saved to `packages` in Pulumi.yaml as of Pulumi 3.157.0.",
          "verdict": "contradicted",
          "evidence": "CHANGELOG lists \"Save package source to `packages` in Pulumi.yaml on `package add`\" under 3.163.0, not 3.157.0.",
          "source": "gh api repos/pulumi/pulumi/releases",
          "checked_at": "2026-08-15",
          "unresolved_reviews": 0 }
      ],
      "score": 0.91 }
  ]
}
```

- `lane` — `priority` (scored pick) or `manual` (workflow_dispatch override).
- `mode` — `fix` (this procedure), `glowup`, or `report`. A `report` queue
  never reaches you: that lane runs no model (see §Report-only mode).
- `editable` — false only on generated trees, which is why they are never in a
  `fix` queue. Nothing you do should ever need to check it.
- `stale_claims` (when present) — count of this page's volatile claims the
  nightly re-verification found contradicted (see §Claims index below). A
  non-zero count is why the page jumped the queue.
- `stale_claim_markers` (when present) — **those findings in full**, each with
  the `entity_key`, the `claim_text` (the exact sentence the nightly verifier
  checked — search the page for it; a marker without one predates 2026-09 and
  names only the entity), the `verdict`, the `evidence` the nightly verifier
  recorded, the `source` it reached, and `unresolved_reviews` (how many prior
  reviews saw this marker and left it unresolved). **These are the highest-
  priority findings in your queue and you must address every one of them.**
  The nightly lane has already done the expensive part — it identified the
  entity, reached an authoritative source, and wrote down what that source
  says — so start here rather than waiting to see whether your own claim
  extraction happens to re-derive the same finding. It may not: a page boosted
  for a contradicted version pin was once reviewed, reported "0 contradicted"
  across 74 re-extracted claims, and merged an unrelated one-line repair while
  the flagged bug stayed on master.
  A marker carrying `"escalated": true` has already survived two reviews
  unresolved, so it no longer jumps the page to the front of the queue and a
  human may be looking at it — but it is still a live finding and still yours
  to resolve if you can. Treat it like any other marker.
  For each marker, either apply the fix, or establish that the flag was wrong
  (the nightly verdicts are single-sample and do produce false positives —
  a synthetic module path for a locally generated SDK was once flagged as a
  broken import). Then list its `entity_key` in the verdict sentinel's
  `resolved_claims`. A marker you do not resolve is carried onto the next
  review with `unresolved_reviews` incremented, and after two such rounds it
  is escalated for a human — so silently skipping one does not make it go
  away, it just delays it.
- `no_retire` — when true, retirement must never be proposed for this page.
  This is the **hard veto** on retirement — honor it regardless of evidence.
- `reader_signals` / `signals` — Search Console and feedback-widget figures
  from the optional reader-signals export; `null` when the export wasn't
  available for the run (a signal-blind run says so, it never fabricates).
  These fed the selection score and the composed "Why this page" block — they
  are selection facts, not review instructions.
- If `articles` is empty or `halted` is set, do nothing (the workflow won't
  invoke you in that case, but be defensive).
- `traffic.available: false` is not your problem to fix: the dispatcher's
  degradation-health lane (`scripts/content-review/signal-health.py`) tracks
  it — along with pulumi/pulumi-service (console-source) access, the
  holiday feed, and the nightly claims re-verify — and alerts
  #docs-ops after a week of continuous degradation.

Process articles **sequentially**, one at a time, completing each article's
fix set and verdict before starting the next.

## Per-article procedure

### 1. Branch — the workflow owns this

You do not create branches. The publish job derives the **exact** branch name
from the queue entry's `slug` and your verdict's `retirement` flag —
`content-review/<slug>` for a fix, `content-review/retire-<slug>` for a
retirement proposal (see below) — and a deterministic pre-check has already
skipped the run (with a `skipped` verdict) if an open PR owns either branch,
so you never need to check for one.

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
- **Deterministic-fix Vale findings** — findings in `.vale-findings.json` stamped
  `deterministic_fix: true`. The stamp (from the allowlist in
  `.claude/commands/docs-review/scripts/vale-deterministic-fixes.yaml` — fixed
  substitutions, canonical spelling, the closed-set cross-reference heading
  rename) means Vale already knows the exact replacement, so you don't have to
  author one. It does **not** mean apply blindly. For each, apply the
  replacement named in the finding's `message` **only after confirming it
  preserves meaning in this context** — read the surrounding sentence/section.
  Skip and record under "Findings not applied" (with the reason) when the swap
  would change meaning, e.g. `click`→`select` inside "click event", a product
  rename inside a historical quote, or a `See also`/`Related` block whose links
  are actually sequential (that wants **Next steps**, not the rule's default
  **Learn more** — apply the correct heading or flag it, don't mislabel intent).
  This is verify-a-proposed-fix, not compose-a-fix; it is still a judgment.
  Vale findings *without* the flag are style/judgment nags — leave them for the
  human (see `docs-review:references:spelling-grammar`).
- **Readthrough `local_repair` findings** — `.readthrough-findings.json`
  findings with `fix_class: "local_repair"` (per `docs-review:references:readthrough`).
  Apply the finding's `proposed_fix` and nothing beyond it: reorder so a
  prerequisite precedes its use, add a missing definition/step, split a
  mixed-concept H2, delete a genuinely redundant passage, or surface a buried
  outcome. The change stays inside the one page and preserves its purpose — that
  bound is what makes it high-confidence. If applying it would mean touching
  other files or reshaping the whole page, it isn't `local_repair`; treat it as
  `reconception`.

Everything else — `unverifiable` verdicts, low-confidence corrections,
prose-quality findings, structural suggestions, **every readthrough finding with
`fix_class: "reconception"`** (a whole-page rewrite, cross-file split/merge, or
purpose change — flag, never auto-rewrite), anything you'd phrase with
"consider" — goes in the PR description's **Findings not applied** section
(one line of reasoning each), not in the diff. That list is the
almost-made-the-cut record the human reviewer adjudicates. When you flag a
`reconception`, set `clarity_flag: true` in the verdict sentinel (step 8) so the
ledger carries the signal even on an otherwise-clean page.

Record every fix you apply as an entry in the verdict sentinel's `applied`
array (step 8): its category, file, **pre-fix** line range, and a pointer to
the artifact finding it implements. The publish job deterministically verifies
that every hunk in your exported changes falls within the line range of a
recorded finding (`scripts/content-review/verify-fix-scope.py`); an edit
outside the recorded findings fails that gate and nothing is pushed — so if a
change doesn't trace to a finding above, don't make it.

Editing guardrails:

- Never rewrite prose beyond the specific correction.
- Stay inside the publish gate's scope: a fix review may touch only the
  queued article itself plus the shared render-time sources named in step 6
  (`layouts/shortcodes/`, `layouts/partials/`, `data/`); a retirement may
  touch `content/`, `scripts/redirects/`, and `data/docs_menu_sections.yml`.
  Any other changed path makes the gate reject the whole review.
- A `low_ctr_flag` on the queue entry's `signals.gsc` block is **FLAG-ONLY**:
  never rewrite `title` or `meta_desc` in response to it. The composer has
  already pre-stubbed a "Search opportunity" row under Findings not applied —
  keep it (you may add one line of observation, e.g. what the title fails to
  say); a human runs `/seo-analyze` on it. Meta rewrites are the canonical
  slop risk this restriction exists for.
- Ordered lists keep their `1.` numbering; files end with a newline; H1 Title
  Case, H2+ sentence case (see `STYLE-GUIDE.md` — but don't re-case headings
  that aren't otherwise wrong).
- Never edit anything under a tier-0 (generated) path — selection excludes
  them, but be defensive.
- Never add the `automation/merge` label to anything.

### 4. Screenshot / UI pass (only when the page has images)

This pass is **gated**: the workflow pre-fills the PR's "Screenshot check"
section with "No images." when the source references no content images (a
deterministic source check — the shared `meta_image` card doesn't count). Run
this pass only when that section still carries a `<TODO>`. When you do, follow
`references/screenshot-verification.md` for every image the article references.
Verified-stale screenshots are **flagged in the PR description** (Screenshot
check section), never regenerated or deleted by you.

### 5. Validate

`make lint` must pass on your working tree. Fix what it surfaces; if you cannot, drop
the offending change rather than shipping a lint failure. **Do not run `make
build` here** — the full build is left to the PR's normal CI, and step 6 runs it
only on the pages that actually need the rendered pass.

### 6. Rendered content pass (only when the page assembles render-time content)

Source review misses content the page assembles at render time — shared
snippets from shortcodes, values from `data/` files, partial-driven sections.
But most docs pages assemble nothing the source doesn't already show (plain
prose, code tabs, callouts, stepper chrome), so this pass is **gated** too: the
workflow pre-fills the "Rendered content" section with "Skipped" when the source
uses no content-bearing shortcode/partial/include, and leaves a `<TODO>` only
when one is present (it names the triggering shortcode). Run this pass only when
that `<TODO>` is there. When you do, first run `make build` (it produces the
rendered views), then check both:

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

You do **not** check the markdown view (`index.md`) for leaked shortcode
delimiters here. Whether a shortcode renders cleanly to markdown is a property of
the shortcode, not the page, so it's covered once across the whole built corpus
by `scripts/content-review/check-rendered-markdown.py` (run periodically / in CI),
not re-paid per review. Content-*mangling* in the markdown output (a template
that silently drops or rewrites content) is a rendering-pipeline bug for the
templating owner, tracked separately — not something to fix in a content review.

If this pass applied any fix, re-run `make build` and then `make lint` (as
separate commands) before opening the PR.

### 7. PR body — only when you applied a fix

You do not open the PR — the publish job creates the PR to `master` whose body
is `.pr-body-draft.md`, exactly as you leave it. You do **not** write that body
from scratch: the workflow composed it (via `compose-pr-body.py`, the
assemble-then-judge model — the composer ASSEMBLES facts, you JUDGE) with every
section present and each pre-found finding pre-bucketed under a `<TODO>`. **Edit
that draft** in place, resolve every `<TODO>`, and strip the HTML-comment hints.
Before opening the PR the workflow runs the authoritative `make lint` on the
published branch and **opens the PR ready for review only if lint passes** —
opening ready is what triggers triage and the docs review (a clean lint means it
flows through the normal pipeline; a trivial fix is short-circuited there). A
lint failure opens the PR as a draft instead, with a comment for a human; humans
merge. The sections (each is checked for):

- **Auto-merge notice** (top `> [!IMPORTANT]` block): flags how the PR merges.
  **Leave verbatim** — do not move, reword, or remove it. The publish job
  classes the PR from your verdict's `applied[]` categories (deterministic
  fixes arm auto-merge; judgment fixes don't) and deterministically swaps in
  the matching notice — that swap keys on the exact composed text.
- **Why this page**: composed from the selection queue (lane, tier, traffic
  figure + period, Search/Reader-feedback figures when the reader-signals
  export was available, last reviewed). **Leave verbatim** — do not
  re-narrate it.
- **Fixes applied**: pre-stubbed one row per high-confidence finding. Keep a row
  only for a fix you actually applied (fill its Correction); move the rest down.
- **Findings not applied**: pre-stubbed with the lower-confidence findings, plus
  any row you moved down. One line of reasoning each. The composed footer notes
  that these items feed the automated glow-up lane (see §Glow-up mode) — keep
  it: this section is that lane's input, extracted from the PR body by
  `build-glowup-backlog.py`, so write rows a later run can act on.
- **Screenshot check**: per image — current / stale (what differs) /
  unverifiable; note any aging reference screenshots (see
  `references/screenshot-verification.md`).
- **Rendered content**: outcomes of the rendered pass — residue claims
  checked in the HTML view, the markdown view's shortcode-template status,
  and any shared-source (shortcode/partial/data) findings with their
  page-reach ("also rendered on N other pages").
- **Verification**: the composer renders the pre-step artifact inventory; the
  `make lint` result is stamped by the re-lint gate — leave the
  `<!-- LINT-RESULT -->` line untouched. Note any pre-step that failed.

Do **not** record `pr_number` or `head_sha` yourself — the workflow derives
them from the branch it publishes. A clean article (zero applicable fixes)
gets no PR and needs no body edits — set `"verdict": "clean"` in the sentinel
(next step).

### 8. Verdict sentinel — your only structured output

Write `.content-review-verdict.json` at the repo root. This — plus your
working-tree edits and the PR body draft — is all you produce for the
workflow; do not write a ledger or a results file. The workflow derives the
PR facts (existence, number, head SHA) from the branch it publishes, builds
the canonical ledger record, and uploads it to S3 keyed by slug.

```json
{
  "verdict": "fixed",
  "reason": "",
  "fixes": 2,
  "skipped_findings": 2,
  "retirement": false,
  "clarity_flag": true,
  "resolved_claims": ["version/pulumi-package"],
  "applied": [
    { "category": "claim", "file": "content/docs/iac/concepts/stacks/_index.md",
      "lines": [42, 43], "source": "verified-claims:c3" },
    { "category": "link", "file": "content/docs/iac/concepts/stacks/_index.md",
      "lines": [88, 88], "source": "dead link /docs/intro/concepts/state/" }
  ]
}
```

- `verdict`: `"fixed"` (you applied fixes — the publish job opens the PR),
  `"clean"` (zero applicable fixes, no PR), or `"skipped"` (a previous run
  already owns this page's PR — normally stamped by the workflow's
  deterministic pre-check before you even start).
- `reason`: one line — **required** for `clean` and `skipped`; omit/empty for
  `fixed`.
- `fixes`: applied changes; `skipped_findings`: Findings-not-applied count.
- `retirement`: `true` only for a retirement PR (branch
  `content-review/retire-<slug>`).
- `applied`: one entry per applied fix — `category` (one of `claim`, `link`,
  `frontmatter`, `vale`, `readthrough`), `file`, `lines` (`[start, end]`,
  inclusive, **pre-fix** line numbers — the file as it was on master, the same
  numbering the pre-step artifacts use), and `source` (the artifact finding it
  implements, e.g. `verified-claims:<claim_id>`, `vale:<rule>@L<line>`,
  `readthrough:L40-58`, or the dead link's old path). `fixes` should equal
  `len(applied)`. The workflow's scope gate cross-checks these against the
  artifacts and the branch diff; for link fixes (which have no artifact) the
  declared lines must actually carry the link in the pre-fix file.
- `resolved_claims`: optional; the `entity_key` of every
  `stale_claim_markers` entry you resolved this run — fixed, or shown to be a
  false positive (say which, in the PR body). Omit or leave empty when the
  queue item carried no markers. Anything you leave out is carried forward to
  the next review rather than cleared, so this list is the only way a marker
  retires.
- `clarity_flag`: optional; `true` when you flagged a readthrough `reconception`
  for this page. Carries onto the ledger record so the page's structural
  follow-up is durable even when the verdict is `clean` or `fixed` (the
  reconception itself lives in the PR's Findings-not-applied section). Omit when
  there's no reconception to flag.

**Self-check before you finish** (skip for a retirement verdict — the gate
routes those to the retire veto instead): verify your `applied[]` line ranges
exactly the way the publish gate will, using the gate's own script. Stage your
changes the way the export step does, emit a zero-context diff, unstage, and
run it:

```bash
git add -A -- ':!.*' ':!.*/**'
git diff --cached --unified=0 > .self-check.u0.diff
git reset -q
python3 scripts/content-review/verify-fix-scope.py \
    --diff-file .self-check.u0.diff --base-sha HEAD \
    --article <path> --verdict .content-review-verdict.json \
    --artifacts-dir . --out .self-check-report.json
```

Exit 0 (pass or skipped) is required. On exit 2, read `uncovered_hunks` /
`invalid_applied` in the report and either correct the `applied[]` ranges or
revert the out-of-range edit; re-run until it passes. This is the pipeline's
dominant hard-failure mode — a range that doesn't cover its hunk wastes the
whole run at the publish gate, where there is no retry.

If you exit without writing this file, the workflow records the page as
`incomplete`. An incomplete outcome does **not** advance the staleness clock, so
the page stays due and is retried on a later sweep — up to an attempt cap, after
which it backs off for a human. Always write the sentinel, even for a clean or
skipped verdict.

## Glow-up mode

When the queue article carries `"mode": "glowup"` (the dispatcher's daily
glow-up lane), the run is a **whole-page rehab executing the page's banked
review backlog** — not a high-confidence-fix sweep. Everything above applies
except as amended here.

**Input**: `.glowup-backlog.json` at the repo root (built by the workflow via
`scripts/content-review/build-glowup-backlog.py`, then reconciled by
`compose-pr-body.py`): the ledger's `skipped_findings` / `clarity_flag`
counters plus every banked finding extracted from the page's prior review
PRs' "Findings not applied", "Screenshot check", and "Rendered content"
sections, each with a stable `id` and its `source_pr` — plus, for PRs
reviewed on the v3 surface, what the pre-merge *reviewer* found and the page
still carries (`source: pr-review`: findings left open, accepted as-is, or
held over a dispute, and every pre-existing issue it filed). The pre-step
artifacts (claims, Vale, readthrough, frontmatter) are also present and are
your evidence base.

Each banked item is split in two, and the split is the point:

- **`finding`** is the work — what an earlier run found.
- **`prior_disposition`** is one earlier reviewer's reason for leaving it.
  It is **context, never direction**. It tells you why someone hesitated;
  it does not tell you what the page should say, and an aside inside it
  ("the page frames X as primary") is not a finding to execute. Two
  September 2026 glow-ups went wrong exactly here: one promoted such an
  aside into a new superlative claim, the other executed a readthrough
  finding the earlier run had declined as editorial.
- **`fresh_verdict`** is what *this run's* artifacts say about the same
  sentence (matched by text, since claim ids and line numbers drift between
  runs). A banked claim the fresh verifier now calls `not-a-claim` or
  `verified`, and a banked readthrough finding the fresh readthrough pass
  did not re-raise, are **pre-declined by the composer** as "superseded by
  re-verification": their rows are already in the Backlog declined table.
  Leave them as composed and list their ids in `declined_ids`.
- Rows sourced **"this run"** (`fresh-<claim id>`) are fresh
  `contradicted`/`mismatch` verdicts stubbed as work, exactly like the fix
  lane's "Fixes applied" stubs. Fix each, or move it to Backlog declined
  with a reason. The publish gate refuses a body that leaves any stubbed
  row — banked or fresh — out of both tables.

**Procedure**:

1. **Work the backlog first.** Execute every banked finding, or explicitly
   decline it with one line of reasoning. Every item lands in exactly one of
   the PR body's two tables — **Backlog executed** (pre-stubbed, one row per
   item; fill "What changed") or **Backlog declined**. No silent drops.
1. **Then the secondary sweep**: apply the improvement taxonomy from
   `.claude/commands/glow-up.md` §5 — style, structural fixes, code
   formatting, terminology, links, image/diagram flags (flag-only, as ever),
   content enhancements — and record per-category outcomes under
   **Secondary sweep**.
1. **Bounds** (code-enforced by `verify-glowup-scope.py` in the publish job;
   a violation rejects the whole run): only the queued page and its bundle's
   non-markdown assets; at most 400 changed lines; never delete the page;
   never change frontmatter `title`, `aliases`, or `redirect_to`; retirement
   is never a glow-up outcome. Preserve the page's purpose and technical
   accuracy — a glow-up reads better, it does not say different things
   without artifact-backed evidence. In particular, never add superlative or
   ranking language ("fastest", "the recommended", "where to start", "the
   only", "primary") the artifacts don't back.
1. **Validate** with `make lint` as usual, and self-check with the glow-up
   gate instead of verify-fix-scope: stage/diff/unstage as in step 8's
   self-check, then run `verify-glowup-scope.py --diff-file
   .self-check.u0.diff --article <path> --article-blob <pristine-copy>
   --verified-claims .verified-claims.json --out .self-check-report.json`
   (copy the article aside before your first edit). The gate's superlative
   check is a `::warning::`, not a violation, but every warning must be
   acknowledged in the PR body under "Secondary sweep → Content
   enhancements": name the verdict that supports the wording, or remove it.
1. **Verdict sentinel**: `{"verdict": "glowup", "fixes": <executed count>,
   "skipped_findings": <declined count>, "clarity_flag": <bool>,
   "executed_ids": [...], "declined_ids": [...], "retirement": false}` — no
   `applied[]` array; the glow-up gate replaces the per-hunk check.
   `executed_ids` and `declined_ids` are the `id` values from
   `.glowup-backlog.json` for the rows you put in the Backlog executed and
   Backlog declined tables — the same partition, reported as data. Every
   banked id belongs in exactly one of them; both lists are empty only when
   the backlog itself was empty. Without them the findings record cannot
   tell what you executed from what you left, so it records nothing at all
   rather than filing your completed work as still outstanding. State `clarity_flag` explicitly: `false` once you have
   resolved the page's readthrough reconception, `true` while one still
   stands. Omitting it carries the page's existing flag forward unchanged —
   which is the right default, since the flag is usually why the page was
   selected, but it means only you can put it down. If the
   queue article carries `stale_claim_markers`, they are must-address
   findings here exactly as in a fix review: resolve each (fix it, or
   establish the flag was wrong) and list its `entity_key` in the sentinel's
   `resolved_claims`, or it carries forward with `unresolved_reviews`
   incremented.

**What happens downstream**: the publish job derives the branch
`content-review/glowup-<slug>`, classes the PR `glow-up`, and **never arms
auto-merge** — the PR opens ready for human review and the PR-review sweep
assigns the reviewers. The ledger records status `glowup` (a completed
review: it advances the staleness clock and starts the selector's 90-day
glow-up cooldown).

## Report-only mode — no model runs

When the queue article carries `"mode": "report"`, **this skill does not run
and neither do you**. The section is here so the lane is documented where its
siblings are, and so a future change to the worker doesn't quietly wire a model
into it.

The report-only lane (pulumi/docs#20996) visits pages a **generator** owns —
today `content/docs/iac/cli/commands/`, 248 files — where an edit is
overwritten on the generator's next run. Marking such a tree tier 0 used to say
"never select it", and selection is the only thing that ever writes a page's
claim list, so 30% of `content/docs/` had never been fact-checked once. That is
now two separate questions in `references/strategic-tiers.yaml`: `editable`
(may a PR change this file?) and `reviewable` (may we read it and record what
it claims?).

The run is the deterministic claim pipeline and nothing else:

1. The workflow builds the synthetic whole-file diff and runs URL fetch → claim
   extraction (regex + two LLM passes) → merge → verify. Vale, frontmatter,
   cross-sibling, and readthrough are **skipped**: they exist to produce fixes
   for someone to apply, and nothing here applies anything.
1. The workflow writes the verdict sentinel itself —
   `{"verdict": "reported", ...}` — and only when verification actually
   produced verdicts. A degraded verify writes no sentinel, so the ledger
   records the page `incomplete` and it stays due; stamping it `reported`
   would advance the staleness clock on a page nothing had checked.
1. `record-claims.py` persists the claim list to the claims index, which is
   what puts these pages into the nightly volatile re-verify for the first
   time.
1. `report-claims-findings.py` reports the contradictions. They route through
   the same upstream lane the nightly re-verify uses — never marked (no PR here
   could retire the marker), always re-checked, and announced to #docs-ops with
   a prefilled issue against the repo that owns the text, unless
   `references/upstream-claims.yaml` says a human has already filed it.
1. The publish gate enforces the rest: a `reported` verdict with a non-empty
   patch fails closed, and no branch or PR is ever created.

**If you find yourself editing a page in this lane, stop** — the generator will
overwrite it, and the gate will reject the run before anything is pushed. The
fix belongs upstream.

## Retirement proposals

For any article with `"no_retire": false`, retirement is a valid outcome
**instead of** a fix PR when the strict evidence standard below is met.
`no_retire: true` is the primary guardrail and an absolute veto — never propose
retiring such a page no matter how strong the evidence. The veto is
**code-enforced twice** in the publish job, before anything is pushed: the
publish gate rejects a `retirement: true` verdict for a page the queue stamps
`no_retire`, and `scripts/content-review/check-retire-veto.py` independently
re-derives the veto from `strategic-tiers.yaml` and the trusted dispatch
`path` input, so neither a model-edited queue nor a model-edited verdict can
clear it. Retirement is no longer
restricted to a particular lane; it can be proposed on any review that clears
the bar, with the full reasoning documented in the PR.

- **Evidence required (two-sided):** the page appears in the traffic report
  with near-zero views (absence from the report is NOT evidence — the page
  may be new or alias-attributed), **and** GSC impressions/clicks are low
  over its window when that data is present — read them from the queue
  entry's `signals.gsc` block (a `signals: null` run has no GSC evidence, so
  this leg cannot be satisfied); **or** the page is demonstrably
  redundant with a named page (cite `.cross-sibling-discovery.json`). Check
  the page's age in git — never propose retiring a page younger than a year.
- **Retire = redirect, never 404.** The PR must redirect the page to its
  superseding target: add the page's URL to the target's `aliases:` (or an
  S3 redirect under `scripts/redirects/` for non-Hugo paths), update inbound
  internal links in `/docs/`, `/product/`, `/tutorials/`, and remove the
  page + its menu entry. Follow `move-doc` reference mechanics.
- **Branch**: set `"retirement": true` in the verdict sentinel — the publish
  job derives `content-review/retire-<slug>` from it. The PR description
  leads with the full evidence (traffic + GSC numbers and period, redundancy
  target, inbound-link inventory).
- When in doubt, don't propose retirement — review the page normally and
  note the low-traffic observation under Findings not applied.

## Output

The verdict sentinel (step 8), your working-tree edits, and the edited PR body
draft are your only outputs. The workflow publishes the branch, records the
ledger, and drives the docs review from them — there is no results file to
write.

## Claims index and stale-claim boosts

Alongside the ledger record, the workflow persists the page's
`.verified-claims.json` to a **claims index** — one snapshot object per page
at `claims/<slug>.json` in the ledger bucket, written by
`scripts/content-review/record-claims.py`. Each kept claim carries the
`entity_key` / `volatile` fields stamped by the docs-review pipeline
(`entity_key.py`), so downstream consumers can join claims across pages by
the entity they assert something about.

Pages a generator owns reach the index through the **report-only lane**
described above rather than through a review like yours — same script, same
snapshot shape, no edits.

The nightly `claims-reverify.yml` workflow re-checks volatile entities
(version pins, prices, limits) straight from this index
(`scripts/content-review/reverify-claims.py`). When an entity re-verifies
contradicted, every page asserting it gets a `stale_claims` marker in its
ledger entry, and `select-articles.py` boosts those pages to the front of the
next sweep — that is how a page can arrive in your queue the day after a
release changed a fact it states.

None of this is yours to write: this worker's whole-page runs are the index's
**only** writer, and the workflow runs `record-claims.py` itself after your
review. The markers clear automatically when your review's ledger and claims
rewrites land. Do not create, edit, or upload `claims/` objects or
`stale_claims` fields.
