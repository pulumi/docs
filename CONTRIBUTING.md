# Contributing Pulumi Documentation

## Draft-first pull requests

Open new PRs as **drafts** while you iterate. Automated review (style, accuracy, fact-check) fires only when you mark a PR **ready for review**, so a draft-first flow:

- Keeps your branch out of the noisy "every push triggers a review" loop.
- Lets you push iteratively without spamming the PR with new comments each time.
- Means the eventual review reflects your finished thinking, not a half-finished commit.

While you're iterating, consider running `/docs-review` locally — it runs the same style/accuracy pipeline as the automated bot, but stays in your conversation and never posts to GitHub. Catching findings here is cheaper than catching them after the pinned review fires.

When you're ready, use the **Ready for review** button on the PR page. Triage runs again to refresh labels, then the full review fires once and pins its findings to a single comment at the top of the PR. New commits afterward mark the review **stale**. A small push that only touches the lines the review flagged refreshes the review automatically; anything larger won't auto-rerun — mention `@claude #update-review` in a comment to refresh, or transition through draft and back to ready.

If your change is genuinely trivial (a typo, a one-line fix), opening directly as ready is fine — the pipeline will short-circuit on the `review:trivial` label.

## AI-assisted contributions

The repository runs a tiered review pipeline on every PR. AI-assisted contributors should know how it works so they can collaborate with it instead of fighting it.

### The v3 review surface (staged rollout)

The review is moving from one monolithic pinned comment to the **v3 surface**, enabled per-repo by the `REVIEW_V3_COMMENTS` variable. Everything below this section describes the v2 monolith and stays accurate for PRs reviewed before the flip and for repos where the flag is off. What changes under v3:

- **Two comments instead of one.** An **author card** ("Author action guide") lists only what you must act on — one-line `🚨 Fix or disagree` and `❓ Questions for you` rows (both block merge), each with a `#### F<n> · Do this` block underneath (the flagged line verbatim, why, and exactly one required fix — replacement text in a copyable fenced block), plus inline ✏️ style suggestions. A separate **reviewer's guide** tells your reviewer what the PR contains, what's still waiting on you, what to check, and what's machine-verified. The bulk — the verification trail, investigation log, review history — lives on a linked **evidence page**, not in the comments.
- **Every finding has a stable ID** (`F1`, `F2`, …) and every blocking finding needs an answer before merge — fix, disagree, or accept. Fix it and push (the card shows a 🔄 banner within a minute when your push triggers the automatic re-review), or reply naming the ID:

  ```
  @claude F2: the 40% figure comes from the Q3 interview series #update-review
  @claude F2: accepting as-is — shipping for the launch, follow-up filed #update-review
  @claude accepting all open items — <reason> #update-review
  ```

  Either way your answer counts: the review marks the item resolved, or holds it with a 🛡️ note for your reviewer — it stops blocking merge in both cases. The `#update-review` hashtag is what routes the reply; a bare `@claude` is ad-hoc help and unblocks nothing.
- **The Sentinel check** is the one merge gate: review ran at your head SHA, every blocking finding answered, the right team approved (per `.github/review-routing.yml`), and infra changes carry a green staging deploy. Its red states name the exact fix, and any write-access human can apply `review:waived` as the logged break-glass (infra staging evidence excepted — that has no waiver). While `REVIEW_V3_SENTINEL` isn't enabled, the check is report-only.
- **Truly mechanical changes need no human at all** — the tightened bar in `classify_mechanical` (`triage-classify.py`): ≤10 added / ≤30 deleted lines, ≤2 docs/blog files, no structural or code changes, only resolving internal-link additions, frontmatter keys limited to `updated`/`tags`, and no prose-claim signal. Everything else routes to the lane the matrix names.

The disposition vocabulary, the outcome table, and "work the review to zero" below all apply unchanged — v3 just gives each finding an ID and a one-line way to answer it.

### What ready-for-review triggers

Transitioning to **Ready for review** triggers:

1. A re-triage to refresh labels (domain, trivial / frontmatter-only short-circuits, prose-flagged signal if applicable).
1. The full Claude review (currently `claude-opus-5`), composed per touched domain. Findings post to a single pinned comment at the top of the PR — overflow is appended as additional pinned comments tagged `<!-- CLAUDE_REVIEW N/M -->`.

Mark the PR ready when you're done iterating, not when you start. Each ready-transition produces one full review run; thrashing through draft → ready → draft burns review budget and produces stale pinned comments.

### Author a clean commit history

If the PR was AI-drafted, leave the AI authoring trailers in commit messages (`Co-Authored-By: Claude ...`, `Generated with Claude Code`, etc.). Stripping them to disguise authorship is bad form and does not change which review runs.

### After review — three paths to refresh

A pinned review goes **stale** when you push new commits after it ran. One case refreshes itself: when the review had outstanding findings and your push is small (≤80 changed lines) and touches only the flagged lines — the "I fixed what you flagged" push — a deterministic gate auto-fires the scoped `#update-review` path with no mention needed. Everything else stays stale until you refresh explicitly. Three ways:

1. **`@claude` mention** — hashtag-driven routing. The re-entrant pipeline branches on what you put after `@claude`:
    - **`@claude #update-review`** — refresh the pinned review against the current PR head. Runs `claude-opus-5`. Three patterns the update path understands, all of which can appear in the same mention (the pipeline addresses any embedded asks inline before re-rendering the review):
        - **Fix-response** ("I addressed your feedback"): re-verifies the previous outstanding findings against the new diff and moves the resolved ones into ✅ Resolved.
        - **Dispute** ("I disagree with the X finding because Y"): re-examines the disputed finding with your evidence; either concedes cleanly or explains why it's keeping the finding.
        - **Re-verify** (no specific request beyond the hashtag): re-checks outstanding findings only.
    - **`@claude` alone, no hashtag** — ad-hoc questions, code fixes, or one-off requests. Tag mode: the action handles it directly with its own animated tracking comment. Doesn't touch the pinned review. Use this when you want help, not a re-review.
1. **Transition through draft and back to ready** — re-triggers the full initial review. Use this when the PR has changed substantially since the last review.
1. **Wait for the human reviewer** — Cam's local `pr-review` skill reads the pinned comment as source of truth and refreshes it during adjudication if needed.

#### Power-user escape hatch: `@claude #new-review`

Rare. Use when the pinned-review state is corrupted (the 1/M comment was manually deleted, the comment sequence is malformed, the review is stuck in a wrong state that `#update-review` can't reconcile). Clears every existing `<!-- CLAUDE_REVIEW N/M -->` comment and dispatches a fresh initial review from scratch — same workflow that fires on ready-for-review, just bypassing the trivial / frontmatter-only / draft / bot-author skips. Don't use it for routine refreshes; `#update-review` is the right tool for those.

### Working the review to zero

A review is finished when every finding it raised has an outcome — not when the 🚨 count hits zero. The pinned comment carries three actionable buckets and they are all yours: **🚨 Outstanding** (must be resolved or refuted before merge), **⚠️ Low-confidence** (doesn't block, still needs a decision), and the **✏️ style suggestions** posted inline on the Files-changed tab. 💡 Pre-existing is the one optional bucket — that's not debt this PR created.

Five outcomes count as done, and no others:

| Outcome | When | What it takes |
|---|---|---|
| **Fixed** | The finding is right | Push the change. A small push that lands only on flagged lines refreshes the review by itself |
| **Refuted** | The finding is wrong | Dispute it in a `@claude #update-review` mention, with evidence. The model concedes cleanly or explains why it's holding |
| **Deferred** | Real, but out of scope here | File an issue and link it in the PR thread |
| **Accepted** | Shipping as-is on purpose | Say why, in the PR. An accepted blocker that nobody explained reads as an oversight |
| **Not applicable** | The finding mis-anchored | Say what it actually points at. Several of these in one review usually means the review went stale — refresh it |

This matters past your own PR. After a PR closes, `scrape-review-outcomes.py` derives what happened to each finding and aggregates it into the Monday `#docs-ops` digest, which is how the review's severity rules get tuned. A finding you fixed but never refreshed scrapes as ignored; a finding you disagreed with but never disputed scrapes as ignored too. Both push the pipeline toward flagging *more*, not less.

Working the list by hand is fine. If you'd rather not, **`/address-review`** does it with you: it watches for the review to land, enumerates every item — inline style suggestions included — into one checklist, walks them a finding at a time with a proposed fix for each, batches the fixes into a single push, and writes the `#update-review` mention. It won't call the PR done while anything is undecided. The same check standalone:

```bash
python3 .claude/commands/docs-review/scripts/review-worklist.py --pr <N> \
  --state .review-worklist-<N>.json --require-clean
```

### Don't fight the pinned comment

The `<!-- CLAUDE_REVIEW N/M -->` comments are managed by the pipeline. Don't delete them — the re-entrant skill expects to find and edit them in place. If you accidentally delete the 1/M summary, the next run posts fresh at the bottom of the timeline; recoverable but ugly.

**Don't hide them either.** Marking the pinned comment resolved (**Hide** → *Resolved*) collapses it but leaves it in place, so a later `#update-review` edits a comment nobody can see: the job runs green, posts its "🤖 Review updated" progress note, and the refreshed review never appears. The publish path now unhides the comment before patching, but the mutation can be refused by the token's scopes — if a refresh looks like a no-op, check whether the pinned comment is collapsed and unhide it. Use the ✅ Resolved section inside the review to track what you've addressed; that's what it's for.

The pinned comment is also the pipeline's outcome ledger: after a PR closes, a weekly scrape derives what happened to each finding (fixed, conceded, disputed, or merged over) and aggregates it into the Monday `#docs-ops` digest, which is how the review's severity rules get tuned over time.

### Trivial, frontmatter-only, and oversized short-circuits

Three label-driven short-circuits skip the full Claude review (linters still run):

- **`review:trivial`** — ≤10 added lines, prose-only body changes, ≤2 docs/blog `.md` files, no frontmatter changes, no link changes, no code blocks. Typo fixes, wording polish, small same-claim sweeps across siblings, and removal-dominant cleanup (no upper bound on deletions). Marketing/website pages (`domain:website`) get full review regardless of size.
- **`review:frontmatter-only`** — any number of docs/blog `.md` files where every change is inside the frontmatter block. Aliases sweeps, `draft: false` flips, `meta_desc` rewrites, social copy edits.
- **`review:oversized`** — more than 15K changed lines, or more than 150 changed files. At that scale the bulk is invariably generated output: the review can't finish inside its job timeout and wouldn't add value to generated lines anyway. Triage posts a `<!-- TRIAGE_OVERSIZED -->` advisory comment suggesting the hand-written source be split into its own PR. `@claude #new-review` force-overrides the skip.

For both categories, triage runs a focused spelling/grammar pass on the relevant diff slice. If it finds anything, it posts a single advisory comment listing the concerns AND applies `review:prose-flagged` so reviewers don't miss it. The short-circuit label still applies and the full review still skips. This is a guard against rubber-stamping — a typo "fix" that introduces a typo, or a `meta_desc` rewrite with a wrong-word substitution, gets flagged before merge.

Classification is deterministic and lives in `.claude/commands/docs-review/scripts/triage-classify.py` — domain (path-precedence), triviality, and frontmatter-only detection are all path/grep rules. The model is invoked only for the prose check, only when the shell pre-classifies as trivial or frontmatter-only.

## Documentation structure

The mapping from documentation page to section and table-of-contents (TOC) is stored largely in each page's front matter, leveraging [Hugo Menus](https://gohugo.io/content-management/menus/). Menus for the CLI commands and API reference are specified in `./config.toml`.

## Hugo tips

### Short codes

To share common content across articles, use [Hugo Shortcodes](https://gohugo.io/content-management/shortcodes/). Place a .html file in the [layouts/shortcodes] folder. To include it in a page, use syntax `{{< my-shortcode >}}`

For example, our custom [`cleanup`](layouts/shortcodes/cleanup.html) shortcode can be included in .md files, to include common text about cleaning up stack resources:

```plain
{{< cleanup >}}
```

HTML layouts can include other layouts inside the [layouts/partials](layouts/partials) directory, e.g.:

```plain
{{ partial "head.html" . }}
```

### Front matter

Front matter is defined as a YAML block at the top of a Markdown document that defines metadata about the page. Pulumi docs pages often include the following front matter variables:

- `aliases`: A list of relative URLs that should point to the content in this page. When moving or renaming a page, you must add an `alias` entry for the old path of the page relative to the `content/` folder.
- `allow_long_title`: Set to `true` in order disable length validation on the `title` attribute.
- `block_external_search_index`: Set to `true` to prevent crawlers from indexing the page.
- `h1`: If specified, the `<h1>` at the top of the page will use this value instead of the value in the `title` attribute.
- `menu`: Specifies where a page appears in the document navigation tree.
- `meta_desc`: Required (unless `redirect_to` is set), at least 50 characters, no longer than 160 characters. This displays as the description of the page in web search results.
- `meta_image`: Blog posts only. Relative path to an OpenGraph image (1200×628) for social media previews and the blog home page. The image must be a PNG file for compatibility.
- `feature_image`: Blog posts only. Relative path to a high-resolution hero image (1884×1256) displayed at the top of the blog post page.
- `meta_title`: If specified, the meta title (for OpenGraph) will use this value instead of the value in the `title` attribute.
- `redirect_to`: The relative or absolute URL of a permanent redirect.
- `sitemap_exclude`: Set to `true` to omit the page from the generated `sitemap.xml` without affecting crawling or indexing (unlike `block_external_search_index`, which also adds a `noindex` directive). Use this only for pages whose canonical URL is already declared, with an accurate `lastmod`, in a different sitemap that is submitted to Google (for example, a page that is a build-time placeholder for a URL actually served and indexed from a different origin).
- `title`: Required (unless `redirect_to` is set), 60 characters or less. This controls the default value for the `<title>` tag as well at the top level `<h1>` in the document.
- `title_tag`: If specified, the `<title>` tag on the rendered call will use this value instead of the `title` attribute.

You can also define arbitrary front-matter variable in the YAML section at the top of a file and refer to that same value in the page content. For instance, the you could add the following front matter `foo: "bar"`, and then reference the variable in markdown with the syntax `{{< param foo >}}`.

For more information, see [Front Matter](https://gohugo.io/content-management/front-matter/) in the Hugo docs.
