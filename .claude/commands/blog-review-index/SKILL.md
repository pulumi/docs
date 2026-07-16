---
name: blog-review-index
description: Review one existing blog post selected by the daily blog-review workflow and record its known issues into the S3 index. Flag-only — never edits content, never opens PRs. Invoked by the blog-review-index workflow; not user-invocable.
user-invocable: false
---

# Blog Review Index

You are reviewing one existing blog post — not a PR diff — to build the
blog's **known-issues index**. The selection script has already chosen
today's posts; your job is to run the docs-review machinery over the whole
file and record every defensible issue you find as structured findings.

This process is **FLAG-ONLY**. You make **zero edits** to the working tree:

- Do NOT edit the post or any other content file.
- Do NOT run `git commit`, `git push`, or `gh pr create`, and do not create
  branches.
- Your ONLY output is `.blog-review-findings.json` at the repo root.

The workflow's record job asserts the tree is clean after you finish; a
dirty tree invalidates the whole run (recorded `incomplete`, retried later),
so a "quick fix while you're in there" destroys the run's value. Blog fixes
happen elsewhere; this process only *knows things*.

The index's eventual consumer is a decision process that marks rotted,
low-value posts `block_external_search_index: true` (the site's per-page
noindex knob). Your findings and the advisory `noindex_signal` are evidence
for that decision — made later, with traffic thresholds you can't see — not
the decision itself.

## Input

Read `.blog-review-queue.json` from the repo root (written by
`scripts/blog-review/select-posts.py`; the workflow slices it to one post per
run). Shape:

```json
{
  "generated": "2026-07-15T14:30:00+00:00",
  "count": 1,
  "halted": null,
  "traffic": { "available": true, "period": "2026-06", "pages_matched": 640 },
  "reader_signals": { "available": false, "gsc": { "available": false } },
  "posts": [
    { "path": "content/blog/my-post/index.md",
      "url": "/blog/my-post/",
      "slug": "my-post",
      "lane": "priority",
      "post_date": "2021-03-04",
      "monthly_visits": 842,
      "signals": null,
      "last_reviewed": null,
      "attempts": 0,
      "score": 812.5 }
  ]
}
```

- `lane` — `priority` (scored pick) or `manual` (workflow_dispatch override).
- `post_date` — the post's publish date. Calibrate expectations to it: a
  2019 post naming then-current versions is normal; the question is whether
  the content **misleads a reader today**, not whether it aged.
- `signals` / `monthly_visits` — selection facts, not review instructions;
  `null` on a signal-blind run (it never fabricates).
- If `posts` is empty or `halted` is set, write nothing and stop (the
  workflow won't invoke you in that case, but be defensive).

## Pre-computed artifacts

The workflow has ALREADY run the deterministic docs-review pre-computation
over the post (synthetic whole-file diff → claim extraction + verification,
Vale, frontmatter, editorial balance, readthrough). Read these from the repo
root; do NOT regenerate them:

- `.verified-claims.json` — claim verdicts (the fact-check backbone)
- `.candidate-claims.json`, `.fetched-urls.json` — claim provenance
- `.vale-findings.json` — prose-lint findings
- `.frontmatter-validation.json` — frontmatter checks
- `.readthrough-findings.json` — whole-post coherence findings

(The PR-bound editorial-balance detector can't run here; apply the
`docs-review:references:blog` editorial-balance criteria yourself from the
whole-file read when the post is a comparison, listicle, or FAQ.)

If one is missing or carries an `errors` field, note it in your findings
file's issue evidence where relevant and continue with what you have.

## Review procedure

1. Read the whole post (`path` from the queue). Whole-file read is
   mandatory — this is the same posture as
   `docs-review:references:blog`: fact-check-first, heightened scrutiny.
2. Triage the pre-computed artifacts and investigate with the
   `docs-review:references:blog` criteria (fact-check, code correctness,
   product accuracy, editorial balance, category fit, SEO/AEO, links,
   publishing blockers). Verify anything you record: check links you cite as
   dead (WebFetch), check product claims against current docs
   (`content/docs/`), check code against current SDK idioms.
3. Classify every defensible issue into the CLOSED taxonomy in
   `references/issue-taxonomy.md` and assign severity per its rubric. The
   record job validates categories and severities against that closed set —
   an invented category invalidates the run.
4. **Evidence is required per issue.** Each issue must carry concrete,
   checkable evidence (the URL that 404s and what it returns; the claim and
   the authoritative source contradicting it; the deprecated feature and
   where its deprecation is documented). An issue you cannot evidence is an
   opinion — leave it out.
5. Assess the advisory `noindex_signal` per `references/noindex-rubric.md`.
6. Write `.blog-review-findings.json` at the repo root — your ONLY output.
   Shape (JSON Schema in `references/findings-schema.json`):

```json
{
  "schema_version": 1,
  "path": "content/blog/my-post/index.md",
  "slug": "my-post",
  "issues": [
    {
      "id": "dead-link-01",
      "category": "dead-link",
      "severity": "major",
      "summary": "Link to the Kubernetes ingress tutorial 404s",
      "evidence": "https://example.com/tutorial returns HTTP 404 (fetched during this review); no redirect target exists",
      "location": "## Setting up ingress, paragraph 2"
    }
  ],
  "clean": false,
  "noindex_signal": {
    "assessment": "keep",
    "rationale": "Content is dated but accurate; the post still answers its title question correctly."
  }
}
```

- `path`/`slug` must match the queue entry exactly.
- `issues` empty ⇔ `clean: true`. A genuinely clean post is a valid,
  valuable outcome — it advances the staleness clock and records positive
  evidence for keeping the post indexed. Do not pad findings to look
  productive.
- `id` — unique within the file, `<category>-<nn>`.
- `location` — a heading, line range, or section pointer a human can find.

## What NOT to do

- No edits, commits, branches, or PRs (see above).
- No re-running the pre-compute pipeline (`extract-claims*`, `verify-claims`,
  `readthrough`, Vale) — read the artifacts.
- No `make build` and no `make lint` — nothing you do changes the tree, so
  there is nothing to lint.
- No ledger, index, or summary writes — `record-findings.py` owns every S3
  object; you own exactly one local JSON file.
- No style nitpicks as issues: Vale nags, prose taste, and heading-case
  preferences are not index material. The index exists to answer "is this
  post misleading, broken, or worthless to a searcher?" — not "could this
  post be nicer?".
