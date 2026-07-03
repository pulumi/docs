# Docs Review Automation: An Evaluation

*Date: 2026-07-03. Scope: the pre-merge AI docs review pipeline, the daily existing-content review, and the daily link checker — the workflows under `.github/workflows/`, the skills under `.claude/commands/`, and the scripts under `.claude/commands/docs-review/scripts/` and `scripts/content-review/` that implement them.*

This is a point-in-time assessment answering three questions: does the system accomplish what it sets out to do, what could it do better, and what other automation opportunities exist that would meaningfully raise documentation quality without generating slop or inconveniencing the humans in the loop.

---

## 1. What the system is (brief map)

**Pre-merge review** is a five-workflow state machine keyed on `review:*` labels and a re-entrant pinned comment (`<!-- CLAUDE_REVIEW N/M -->`):

- `claude-triage.yml` — deterministic classifier (`triage-classify.py`: domain routing, triviality, frontmatter-only), with a Haiku prose pass only for short-circuited PRs.
- `claude-code-review.yml` — the main review, chained off triage via `workflow_run`. Heavy deterministic pre-computation (Vale, URL prefetch, three-layer claim extraction, parallel claim verification, readthrough, editorial balance, cross-sibling discovery, frontmatter validation, conditional Hugo build) feeds `compose-review.py`, which assembles an ~80%-complete draft. Opus edits the draft; a validate → splice → re-validate → upsert chain (`validate-pinned.py`, `splicer.py`, `pinned-comment.sh`) publishes it.
- `claude-update.yml` / `claude-new.yml` / `claude.yml` — hashtag-routed refresh paths (`#update-review` re-entrant edit, `#new-review` regenerate, bare `@claude` ad-hoc chat), with documented precedence.

**Daily content review** (`review-existing-content.yml` → `content-review-article.yml`): deterministic selection (`select-articles.py`, weighted fair queuing: `score = importance × staleness`, tiers from `strategic-tiers.yaml`, traffic-weighted) fans out one worker per article. Each worker builds a synthetic whole-file diff, reuses the identical docs-review pre-step pipeline, applies **only five enumerated high-confidence fix categories**, opens one draft PR per article, passes a deterministic re-lint gate before draft→ready promotion (which fires the normal pre-merge review), and records the outcome in an S3 ledger. Human approval is still required to merge.

**Link checking** (`check-links.yml`): daily crawl, zero AI spend on clean days; on failures, a verify-first, dedup-aware triage (alias / S3 redirect / source edit / exclusion / out-of-scope issue) opens one auditable PR and posts to Slack.

---

## 2. Does it accomplish what it sets out to do?

**Substantially yes.** The stated goals — catch wrong information before merge, do it with run-to-run stability, keep existing content from rotting, and do all of this without drowning maintainers — are matched by the architecture unusually well. Five design choices stand out as genuinely working:

1. **Assemble-then-judge.** The doctrine in `references/pre-computation.md` is explicit: "Scripts find structural facts. The agent makes editorial judgments." This targets a *measured* failure mode (cross-sibling detection landed roughly one run in four when left to model attention) rather than a hypothetical one. Discovery moved into deterministic pre-steps; the model's job narrowed to triage and judgment. This is the right division of labor, and the system arrived at it empirically.

1. **Deterministic floors and validators.** `.candidate-claims.json` is a coverage floor the review *must* address (demote with a traced reason, never silently drop), and `validate-pinned.py` (2,774 lines, with a test suite) enforces the output contract — canonical verdict vocabulary, trail↔bucket consistency, no unresolved `<TODO>` tokens, internal-link existence in suggestions. Format and coverage cannot silently degrade between runs, which is the failure mode that erodes trust in LLM reviewers.

1. **Human-respecting output.** One pinned comment edited in place instead of comment spam; append-only review history; a dispute protocol in which "reword is the forbidden path" and maintainer domain knowledge is sufficient evidence to concede; a quote-and-rewrite mandate ("if you can't quote the construction or propose a fix, drop the finding"); "an empty list is the correct, common answer"; a 12-item DO-NOT list banning informational-only findings, double-flagging, and retracted-finding noise. The 🚨 bucket is deliberately kept merge-gate-meaningful.

1. **Cost discipline with empirical self-correction.** Deterministic short-circuits (trivial, frontmatter-only, draft, bot-author, empty-diff); model tiering (Haiku triage, Sonnet extraction/updates, Opus judgment); zero AI spend on clean link-check days and quiet content days. Best evidence of a working feedback culture: `render-gates.py` gated off the screenshot and rendered-content passes after they "produced zero applied fixes" across every content-review PR to date — the system measures its own yield and prunes.

1. **A genuinely conservative daily bot.** Selection is fully deterministic ("the model never chooses what to review"); guardrails are code-enforced (`MAX_OPEN_PRS = 9` halt, `ATTEMPT_CAP = 3` backoff, tier-0 generated content never touched, per-article concurrency); fix application is restricted to five enumerated categories with everything else routed to a flag-only "Findings not applied" section; the workflow re-runs `make lint` itself rather than trusting the model's self-report. Merged output (#20056, #20057, #19741) shows exactly the promised profile: small, factual, auditable corrections.

Throughput is sensible rather than impressive, and that is the correct trade: at 3 articles per weekday over ~820 docs pages, the full corpus sweeps roughly annually, with tier-1/high-traffic pages recurring much faster under the staleness model — bounded by reviewer capacity (the open-PR cap), not by token budget.

**The honest caveat: the pre-merge side can't currently prove its precision.** There is spend telemetry (`per-tool-spend.py`, uploaded execution logs) but no *outcome* telemetry — nothing records how many 🚨/⚠️ findings authors fix, dispute, concede, or ignore. The system is elaborately engineered to avoid slop; whether authors *experience* it that way is unmeasurable from the repo. The content-review side is ahead here (the S3 ledger plus `select-articles.py --stats` gives per-outcome accounting). This gap matters because nearly every tuning decision — the always-🚨 carve-outs, the two-question severity test, the Vale caps — is currently justified by doctrine rather than data.

---

## 3. What could it do better

Ordered by leverage.

### 3.1 Code-enforce the two instruction-only guardrails

Two safety rails exist only as skill prose interpreted by the model:

- **The `no_retire` veto.** Selection stamps `no_retire` correctly into the queue, but nothing programmatically blocks a `content-review/retire-<slug>` branch from being pushed for a protected page. A model that misreads the skill could propose retiring the get-started docs and the only backstop is the human approver.
- **"High-confidence fixes only."** The five-category restriction on what the worker may apply to the diff is entirely model-honored; the only hard gate before draft→ready promotion is `make lint`, which checks well-formedness, not restraint.

Both have cheap deterministic backstops: a workflow step that fails any retire branch whose slug maps to `no_retire: true` in `strategic-tiers.yaml`, and a promotion gate that verifies the applied diff's hunks fall within the line ranges of recorded findings in `.content-review-verdict.json` (out-of-range edits → stay draft, flag for a human). The system's own doctrine — deterministic checks for anything a script can decide — argues for both.

### 3.2 Close the feedback loop on pre-merge findings

Add outcome telemetry: per-tier counts of fixed / disputed / conceded / ignored findings, scrapeable from the pinned comment's own structure (the ✅ Resolved and 🛡️ Disputed annotations already encode it), aggregated into the existing `weekly-digest.yml`. Dispute data should feed back into the always-🚨 carve-out list and the severity rules. This is the single change that converts the system from doctrine-tuned to data-tuned, and it also produces the evidence needed to defend (or prune) the system's considerable complexity.

### 3.3 Fix confirmed drift and dead code — and self-apply the doctrine

- `CONTRIBUTING.md` line 24 still tells contributors the review runs `claude-opus-4-7`; `claude-code-review.yml` pins `claude-opus-4-8`.
- `record-review.py` (lines ~340–347) still emits a `dispatch`/`pr_number`/`head_sha` signal for a "review-dispatch step" the worker workflow explicitly removed (promotion now rides the draft→ready transition). Nothing consumes it, and it tests a status value (`"reviewed"`) outside the recorder's current status vocabulary.

Small items, but pointed ones: a system whose thesis is claim verification should verify its own meta-docs. When a PR touches the review workflows, the infra review domain could cheaply check `CONTRIBUTING.md`/`AGENTS.md` for drifted claims about models, triggers, and thresholds — the same doc-drift check `references/infra.md` already prescribes against `BUILD-AND-DEPLOY.md`.

### 3.4 Alarm on silent degradation

Three inputs degrade gracefully — and silently:

- A missing traffic snapshot flattens selection scoring to tier-only (`importance = tier_w`), quietly erasing intra-tier prioritization. The queue records `traffic.available=false`, but nothing notices when the cross-stack read has been failing for a month.
- Screenshot lane 2 (verifying UI strings against `pulumi/console`) silently becomes `unverifiable` when the repo isn't accessible to the token; no metric tracks how often.
- The holiday gate fails open by design.

Graceful degradation is the right *behavior*; the gap is observability. A one-line staleness note to `#docs-ops` (the Slack plumbing already exists in `check-links.yml`) when any of these has been degraded for more than N days closes it.

### 3.5 Tighten the content worker's security posture

The per-article worker runs with `environment: production` credentials (pulumi-bot push token) and a wide-open `Bash` allowlist (`content-review-article.yml` — adopted after per-command allowlisting rejected 6–21 benign compound commands per run), while consuming artifacts derived from fetched external URLs (`.fetched-urls.json`, web-search verification). The only prompt-injection defense at that layer is instruction-level ("treat attacker-controlled text as data"). The main pre-merge review deliberately runs with *no* push credentials and a tight allowlist — the asymmetry is the finding. `summarize-denials.py` was built precisely to size a real allowlist from denial data and is labeled temporary; finishing that tuning, or splitting the fetch-derived-artifact review phase from the credentialed push phase, would close the gap without re-inflicting the 6–21 denials/run.

### 3.6 Adaptive human-load throttling

`MAX_OPEN_PRS = 9` caps bot-PR *inventory*, but nothing senses whether humans are keeping up. If the median age of open `content-review/*` PRs exceeds a threshold, the dispatcher should reduce its per-run count automatically (and say so in the run summary). This is the missing half of the "don't inconvenience humans" contract: the current cap stops runaway production, but a queue of nine stale bot PRs is still nine nagging review obligations.

### 3.7 Auto-refresh stale reviews when the delta is trivial

On `synchronize`, the review flips to `review:stale` and waits for the author to remember `@claude #update-review` or thrash draft→ready. When a push touches only lines carrying outstanding findings — the overwhelmingly common "I fixed what you flagged" case — auto-firing the scoped Sonnet update path would remove a papercut. Budget-cap it (e.g., only when the push diff is under some size, once per push) so large rewrites still require the explicit, more expensive paths.

---

## 4. New opportunities

Filtered against the two stated constraints: no slop (nothing that generates prose at scale or applies judgment-free rewrites) and no new human burden (findings flow into existing queues and gates, not new obligations).

### 4.1 Persist the claims index → event-driven freshness (biggest lever)

Every review — pre-merge and daily — already extracts, classifies, and verifies claims, then throws the result away. Persisting per-page verified claims in the existing S3 ledger, keyed by entity (CLI flag, version number, price, API surface, product name), unlocks three capabilities the current architecture can't reach:

- **Release-triggered targeted re-verification.** A pulumi/pulumi or major-provider release invalidates exactly the claims that mention the changed surface; only those pages enter the review queue. This converts the O(corpus), time-based annual sweep into event-driven checks that catch rot in days, not months — precisely where docs staleness actually comes from.
- **Cheap nightly re-verification of volatile claims.** Version numbers, prices, and limits can be re-verified from the index without re-extraction — a deterministic-plus-one-Sonnet-call pass, orders of magnitude cheaper than a full page review.
- **Corpus-wide contradiction detection.** Cross-sibling consistency today only covers templated directories. An entity-keyed index surfaces two arbitrary pages asserting different defaults for the same flag — a class of error no current lane can see.

All three feed the existing content-review queue and PR machinery; no new human touchpoints.

### 4.2 Promote recurring model findings into Vale rules

A quarterly meta-process: mine the pinned reviews and ledger for the most-repeated prose findings and codify the top few as Vale rules. This continues the system's own founding move — migrate discovery from model attention to deterministic code — one rule at a time. Each promotion cuts tokens, improves run-to-run consistency, and moves feedback earlier (Vale runs in `make lint-prose`, before any review fires). Requires the outcome telemetry from §3.2 to know which findings recur *and get fixed* (recurring-but-ignored findings should be pruned, not promoted).

### 4.3 Deterministic corpus-wide snippet-parse sweep

`static/programs/` is CI-tested, and PR review checks inline code blocks — but only in touched files. Inline snippets across the other ~800 pages are checked never. A nightly parse/import-resolution floor (no execution, no model) over tier-1/2 pages is cheap, fully deterministic, and zero-slop; findings land as queue-priority boosts for the existing content review rather than their own PRs.

### 4.4 Fragment checking in the link checker

`check-links.js` validates pages, not in-page anchors; `#fragment` links break silently when headings are reworded. The underlying crawler supports hash verification. Deterministic, cheap, and it feeds the existing fix-broken-links triage unchanged.

### 4.5 Real reader signals into selection

The importance term currently uses pageviews alone. Search Console impressions/CTR (pages with high impressions and poor CTR are candidates for title/`meta_desc` attention — flag-only, given how slop-prone meta rewrites are), docs feedback-widget signals if present, and the existing `scripts/detect-new-404s` output would all sharpen both the selection queue and the redirect triage at zero model cost.

### 4.6 A screenshot *proposal* lane — only if data justifies it

The flag-only doctrine for images is correct and should stand. But the environment already provisions Playwright, so a gated job could capture current product screenshots for images flagged stale and attach them to the PR *as proposals a human accepts* — never auto-applied. Gate this on §3.4's lane-2 metrics first: build it only if stale screenshots turn out to be a recurring confirmed finding rather than a theoretical one.

### 4.7 Promote author-time review

The interactive `/docs-review` skill already runs the same pipeline before a PR exists, at conversation scope, with no GitHub side effects. It is barely mentioned in `CONTRIBUTING.md`. Making it a first-class recommendation ("run `/docs-review` before marking ready") shifts findings to the cheapest possible point — before they consume review budget, pinned-comment round-trips, or reviewer attention.

---

## 5. Summary

The system does what it says: it catches factual and structural errors pre-merge with stable, low-noise output, and it sweeps existing content conservatively enough that its merged PRs read like a careful human's small fixes. Its architecture — deterministic discovery, model judgment, validated output, code-enforced budgets — is the load-bearing reason it avoids slop, and the discipline of measuring yield and pruning zero-value passes shows the feedback culture works where data exists.

The gaps are the mirror image of the strengths: a few rails are still doctrine where they could be code (§3.1), the pre-merge side lacks the outcome data to tune itself (§3.2), and degradation is graceful but mute (§3.4). The largest untapped asset is one the system already produces and discards daily — the verified-claims corpus (§4.1), which would turn time-based freshness into event-driven freshness.

One cross-cutting risk deserves naming: scale. Roughly five thousand lines of validator/composer code, seventeen reference documents, and two dozen scripts, with the maintainer-side `pr-review` skill explicitly a single person's local tool. The complexity is currently justified by doctrine; the telemetry loop in §3.2 is also how it gets justified — or pruned — by data.
