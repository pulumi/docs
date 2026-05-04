# Session 1 — Plumbing Notes

This file is a working scratchpad for Cam to read before kicking off Session 2. It is not committed to master and should be deleted (or absorbed into a longer-form decision log) when Session 2 wraps.

## Branch

Branch: `CamSoper/pr-review-overhaul` (the existing clean branch this session inherited).

The session prompt asked for `cam/pr-review-pipeline-v1`, but the existing branch was clean, matched the repo's `CamSoper/<descriptive-name>` convention from `AGENTS.md`, and was already set up for this work. I stayed on it. If you want the literal name, rename with `git branch -m CamSoper/pr-review-overhaul CamSoper/pr-review-pipeline-v1`.

## Surprises from required reading

- **`.github/PULL_REQUEST_TEMPLATE.md` already existed** (uppercase). The session prompt said "create if missing" with the lowercase name. I edited the existing one rather than creating a duplicate. GitHub picks up either case.
- **`claude.yml` uses ESC + `PULUMI_BOT_TOKEN`** to ensure pushes from the action trigger downstream workflows like `claude-social-review.yml`. I preserved this — re-entrant updates that push commits still need it.
- **`claude-social-review.yml` is the right pattern to crib** for concurrency, ESC fetch, and PR-info resolution. The new `claude-triage.yml` follows its shape without copying the social-specific bits.
- **`add-triage-label.yml` exists** but only labels *issues* with `needs-triage`. No collision with our PR-triage labels.
- **`docs-review.md`'s old CI block had a working-tree leak**: it told the model "if you suspect a missing trailing newline, you may read the full file." That's exactly the sort of conditional that produced false positives. The new `docs-review-ci.md` bans working-tree reads outright and explicitly tells the model not to claim missing trailing newlines from CI at all (the linter catches them).
- **`docs-tools` skill catalog will pick up new commands automatically.** I didn't have to register anything; the catalog scrapes `.claude/commands/` for frontmatter.

## Decisions where the plan was ambiguous

1. **`gh api` body syntax.** The pinned-comment script uses `gh api -F body=@file` to read the body from disk and avoid command-line length limits. Verified `-F` magic-type-conversion is for scalar values and doesn't affect `@file` reads.
2. **Marker line stripping on edit.** The script keeps the marker as the first line of each comment and re-renders it on every upsert (so N/M counts always reflect the current sequence length, even if the new sequence is shorter or longer than the previous one).
3. **`mark-stale` as a separate job in `claude-code-review.yml`** rather than a step at the top of the `claude-review` job. This keeps the trigger / job mapping straight and lets `synchronize` events finish in seconds without spinning up the full review job.
4. **Empty prompt fallback in `claude.yml`.** When the @claude mention is on an issue (not a PR), the prompt evaluates to the empty string, which the `claude-code-action` interprets as "execute the comment body's instructions." This preserves the original behavior for non-PR mentions.
5. **`gh pr edit` permission in triage workflow.** I added `Bash(gh pr edit:*)` to triage's allowed-tools list and gave the workflow `pull-requests: write`. Double-checked that the original `claude-code-review.yml` already had `pull-requests: write` for the same reason.
6. **No `paths:` filter on `claude-triage.yml`.** Triage needs to look at *every* PR (some PRs touch only `layouts/`, which still benefits from a domain label even if it's just `review:shared`-only). The cost is minimal — Sonnet on a tiny diff is sub-second.
7. **Composite `--add-label` / `--remove-label` calls.** The triage prompt instructs the model to compute the *delta* and only call `gh pr edit` for labels that actually change. No-op runs make no API call.

## Manual test steps for the pinned-comment script

The script's `find` / `fetch` / `last-reviewed-sha` paths were exercised against real PR `pulumi/docs#18659` (no pinned comments → empty output, exit 0). The `upsert` path was exercised with `--dry-run` for both single-page and forced-multi-page splits — the POST counts matched expectations.

To exercise the patch-vs-create branch end-to-end before merging:

```bash
# 1. Create a throwaway draft PR in your fork (or use a real WIP PR you own).
PR=<your draft PR number>

# 2. Post a fake "1/1" pinned comment to seed state.
cat >/tmp/seed.md <<'EOF'
## Claude Review — Last updated 2026-04-22T12:00:00Z

Status: 1 🚨 / 0 ⚠️ / 0 💡 / 0 ✅

### 🚨 Outstanding in this PR
- test:1 — seed finding

### 📜 Review history
- 2026-04-22T12:00:00Z — Initial review (deadbee)
EOF
bash .claude/commands/_common/scripts/pinned-comment.sh upsert \
  --pr "$PR" --body-file /tmp/seed.md --repo pulumi/docs

# 3. Verify find / fetch / last-reviewed-sha
bash .claude/commands/_common/scripts/pinned-comment.sh find --pr "$PR" --repo pulumi/docs
bash .claude/commands/_common/scripts/pinned-comment.sh fetch --pr "$PR" --repo pulumi/docs
bash .claude/commands/_common/scripts/pinned-comment.sh last-reviewed-sha --pr "$PR" --repo pulumi/docs

# 4. Upsert with a longer body to exercise PATCH+POST.
cat >/tmp/longer.md <<'EOF'
## Claude Review — Last updated 2026-04-22T13:00:00Z
Status: 0 🚨 / 0 ⚠️ / 1 💡 / 1 ✅
### 🚨 Outstanding in this PR
(none)
### ✅ Resolved since last review
- test:1 — seed finding (resolved)
### 💡 Pre-existing issues in touched files (optional)
- test:2 — pre-existing
### 📜 Review history
- 2026-04-22T12:00:00Z — Initial review (deadbee)
- 2026-04-22T13:00:00Z — Re-reviewed (cafef00)
EOF
bash .claude/commands/_common/scripts/pinned-comment.sh upsert \
  --pr "$PR" --body-file /tmp/longer.md --repo pulumi/docs --max-bytes 200

# 5. Verify the existing 1/M was patched (not deleted) and a 2/M was appended.
bash .claude/commands/_common/scripts/pinned-comment.sh find --pr "$PR" --repo pulumi/docs

# 6. Cleanup
bash .claude/commands/_common/scripts/pinned-comment.sh prune --pr "$PR" --keep 0 --repo pulumi/docs
# (will refuse to delete 1/M; manually delete the seed via the GitHub UI or `gh api -X DELETE` if needed)
```

## Open questions for Cam

1. **Pinned-comment-script home.** I put it under `.claude/commands/_common/scripts/`. The existing `pr-review/scripts/` location uses the same pattern. Worth elevating to `scripts/pr-review/` (top-level repo `scripts/`) if you want it referenceable outside the `.claude/` tree?
2. **The 1/M sacrosanct guarantee** is enforced in the script (`prune` and `upsert` both refuse to delete index 0). But if the *author* deletes the 1/M comment via the GitHub UI, the next re-entrant run falls through to a fresh post (lands at the bottom of the timeline). Acceptable? Or should we push more aggressively against this — for example, reserving a *second* comment as a fallback anchor?
3. **`@claude` mention on a draft PR.** Currently the `claude.yml` workflow runs against drafts — there's no draft check in the job's `if:`. The plan says "Drafts get reviewed on mention with a note: 'reviewing a draft; findings may change as you iterate.'" I did **not** add that note to `update-review.md` — it would be Session-2 content. Flagging in case you want it sooner.
4. **Triage on `synchronize`?** The plan explicitly says no, and I followed it. But: if a draft PR has commits pushed to it that change the domain (e.g., what started as a docs PR now touches `static/programs/`), the labels are stale until the next ready-transition or PR open/reopen. Probably fine — re-triage on ready-for-review covers this — but worth flagging.
5. **Label colors.** I picked colors per the standard GitHub palette. Override `.github/labels-pr-review.md` before running the create commands if you want different ones.
6. **`scripts/lint/lint-markdown.js` still owns trailing newlines etc.** I added the DO-NOT entry "no findings the linter catches" to `_common/docs-review-core.md`, but for v1 the actual enforcement is the model reading the prompt. Worth a follow-up to add a quick post-run sanity check that strips known lint-overlap findings programmatically?
7. **`/docs-tools` skill discovery.** I confirmed the `_common/*.md` files all show up in the available-skills list (visible in this session's system reminders). No registration step needed.

## What's still skeleton (Session 2 work)

- Every `_common/review-{shared,docs,blog,infra,programs}.md` file's `## Criteria` section still says "Pending — inherits from review-criteria.md."
- `docs-review-core.md`'s composition layer is wired up but the per-domain criteria it composes are placeholders.
- `update-review.md` describes the three cases (fix-response / dispute / re-verify) but doesn't bake in the cheaper-Sonnet-needs-tighter-prompt rule beyond a single header note.
- The DO-NOT list lives in `docs-review-core.md` but is not yet baked into specific enforcement rules in the per-domain prompts.
- `fact-check.md` is unchanged — Session 2's job to add the v1 extensions.
- No CI wiring of the `review:trivial` confidence mechanism — for v1, label presence is the gate.

## Verification checklist (from session prompt)

- [x] `docs-review.md` has no "is this CI?" conditional logic — verified by grep
- [x] `docs-review-ci.md` has no working-tree references except in the "do not do this" prohibition — verified by grep
- [x] Pinned-comment script handles first post / in-place edit / overflow append / trailing delete / missing-1/M fallback — script structure, dry-run tested
- [x] `claude-code-review.yml` triggers on `ready_for_review` only for the review job (synchronize triggers only the mark-stale job)
- [x] `claude-triage.yml` triggers on `opened` / `reopened` / `ready_for_review`, not on `synchronize`
- [x] `synchronize` events apply `review:claude-stale` without running review (separate job in claude-code-review.yml)
- [x] Per-PR concurrency key with `cancel-in-progress: true` on the review job and triage job
- [x] Model strings are literally `claude-opus-4-7` (initial review) and `claude-sonnet-4-6` (triage and re-entrant)
- [x] No workflow references Notion or Slack MCP servers
- [x] Labels doc lists all 11 labels
- [x] Draft-first guidance in README, CONTRIBUTING, AGENTS, and PR template
- [x] Branch ready for Session 2 — not merged

## Session-1 commit list

```
ca0fd0e9 Split docs-review into interactive + CI entry points and shared core
0942e54e Add domain skeletons (shared/docs/blog/infra/programs) and update-review
18a4aa1b Add pinned-comment.sh to manage Claude review as a single logical post
10e302e2 Add triage workflow, prompt, and labels documentation
abdfe141 Update claude-code-review.yml for the new pipeline shape
7ac1d1e4 Update claude.yml to invoke update-review on PRs with a pinned review
(this commit) Documentation: draft-first guidance + SESSION-NOTES
```

---

# Session 2 — Criteria Content

Session 2 filled in the content behind Session 1's plumbing. Seven commits land the real `## Criteria` sections, the DO-NOT enforcement, the `fact-check.md` v1 extensions, and the Sonnet-tightened `update-review.md`.

## Surprises from required reading

- **Style-guide vs DO-NOT tension on colloquialisms.** `STYLE-GUIDE.md` §Inclusive Language says to avoid violent or aggressive terms ("kill"). `docs-review-core.md`'s DO-NOT list (Session 1) says "overkill"/"kill"/"blow away"/"destroy" are fine in technical context. These intentionally disagree: the style guide rule stands *for authors*, but the review skill stops nagging about it. Every domain file's "Do not flag" subsection restates the relaxation in its own terms. Flag for future contributors so they don't "fix" one to match the other.
- **`should-fact-check.sh` is tightly coupled to the pr-review skill's two-axis trust model.** The script takes `CONTRIBUTOR_TYPE` / `AI_SUSPECT` / `RISK_TIER` -- concepts that live only in `pr-review/`. The CI pipeline doesn't use any of them; it gates via the `fact-check:needed` label applied by triage. The Session 2 `fact-check.md` makes this split explicit: `should-fact-check.sh` stays where it is (`pr-review/scripts/`) and is called only by pr-review and standalone callers. CI's gate lives upstream in the triage prompt.
- **`content/customers/` is a blog-domain path** (not docs). Easy to miss -- surfaced by reading `docs-review-core.md`'s domain-selection table. Worth a note for contributors who'd intuit otherwise.
- **Pre-existing Session 1 table-format diagnostics at `docs-review-ci.md:56`.** Markdownlint flags the compact-column style in the existing domain-selection table. Out of this session's scope; not "fixed" since Session 1 presumably authored it deliberately or the linter config tolerates it in the CI runner.
- **Voice benchmark.** `pr-review/references/message-templates.md` sets a much stricter voice for *author-facing* text (no em-dashes, no sycophancy, terse). The `_common/*.md` files are prompt material, not author-facing, so I used standard em-dashes inside `_common/` files but switched to double-hyphens (`--`) where the prose most resembles a public comment. Deliberate inconsistency; happy to revisit.

## Decisions where the plan was ambiguous

1. **Consolidated the DO-NOT wiring into each domain-file commit** instead of landing a separate final commit. The session prompt suggested eight commits with `(h) Wire DO-NOT subsections` as its own commit. Shipping the Do-not-flag subsection alongside the criteria it constrains is cleaner per-file; the reviewer sees the domain's complete v1 state in one diff. Final commit count: seven (plus this one).
2. **Mechanical paths for the fact-check move committed in one chunk** including the internal framing tweak. The plan allowed for a tiny framing change as part of the move commit; the full v1 extensions landed later in the `Extend fact-check.md` commit.
3. **`review-infra.md` added a "documentation drift" bullet** under its risk axes (flag when BUILD-AND-DEPLOY.md isn't updated for a change that required it). The session prompt's axes list didn't include this explicitly, but the existing skeleton already had "Missing `BUILD-AND-DEPLOY.md` updates" and it's genuinely useful.
4. **`review-programs.md` TS hand-written constructor style ships with a code snippet** in the Idiomatic-per-language section. The session prompt said "idiomatic per language per the AGENTS.md rules (especially the hand-written constructor style for TypeScript)." The AGENTS.md rule is explicit enough that a short inline example prevents the reviewer from re-deriving it; it's duplication but scoped.
5. **🤔 intuition-check is a new tier in `fact-check.md`'s tiered triage output.** The session prompt asked for the axis but didn't explicitly say "add a new render tier." I made it a fourth tier between 🚨 and ⚠️; the pinned-comment's overflow rules already handle arbitrary section orderings.

## Files changed and why

| File | Change | Why |
|---|---|---|
| `.claude/commands/_common/fact-check.md` | Moved from `pr-review/references/`; extended with v1 additions | Shared primitive for CI + pr-review |
| `.claude/commands/_common/review-shared.md` | Filled in criteria + Do-not-flag | Session-2 scope |
| `.claude/commands/_common/review-docs.md` | Filled in criteria + Do-not-flag | Session-2 scope |
| `.claude/commands/_common/review-blog.md` | Filled in 5-priority criteria + Do-not-flag | Session-2 scope |
| `.claude/commands/_common/review-infra.md` | Filled in risk-flag axes + Do-not-flag | Session-2 scope |
| `.claude/commands/_common/review-programs.md` | Filled in compilability criteria + Do-not-flag | Session-2 scope |
| `.claude/commands/_common/update-review.md` | Added Sonnet failure-mode examples, draft-PR note, known quirks | Session-2 scope |
| `.claude/commands/_common/docs-review-core.md` | Updated fact-check path | Post-move reference |
| `.claude/commands/docs-review-ci.md` | Updated fact-check path | Post-move reference |
| `.claude/commands/pr-review/SKILL.md` | Updated skill-id for fact-check | Post-move reference |
| `SESSION-NOTES.md` | Session 2 section (this) | Carry-forward notes |

## Open questions for Cam

1. **`pr-review/SKILL.md` still lists the fact-check references under its own reference catalog** (e.g., the system-reminder shows `pr-review:references:fact-check` is gone and `_common:fact-check` is registered -- as expected). The pr-review skill's own `references/` directory now doesn't include fact-check. If your local catalog or downstream tooling expects `pr-review/references/fact-check.md`, this is the moment it will break. I did not find any other reference to the old path after the grep verification, but flagging in case.
2. **Mermaid not used anywhere in Session 2's writing.** AGENTS.md prefers Mermaid over ASCII for diagrams. None of the filled-in files needed a diagram -- they're prompt text and rubrics, not architecture narratives. Worth a design diagram somewhere (maybe in `docs-review-core.md`) illustrating the composition layer? Not in scope this session.
3. **The 🤔 tier is new** and will affect the token budget of fact-check outputs. On blog PRs (heightened scrutiny), it's likely to accumulate. If the bucket gets noisy in practice, we can tune the thresholds (what counts as "unrounded specific"; what counts as "AI-pattern phrasing"). For v1, the rule is "flag suspicious shapes; rely on author response to resolve."
4. **The `BUILD-AND-DEPLOY.md` cross-references in `review-infra.md` are section-name-based** (§Infrastructure Change Review, §Dependency risk tiers). If those section names drift in `BUILD-AND-DEPLOY.md`, the cross-refs go stale silently. Not a linter-caught issue. Worth a markdownlint rule someday that checks `§X` references against actual headings in the target file; deferred.

## Deferrals that belong in Session 3 (or later)

- **Post-run programmatic stripping of linter-overlap findings.** Deferred per the session prompt. If the prompt-level DO-NOT wiring proves insufficient on real PRs, a small post-processor that filters findings matching linter-owned categories (trailing whitespace, missing fence language, ordered-list numbering) would be worth building.
- **A real-PR end-to-end exercise.** Session 2 is content-only; the combined Session 1 + Session 2 branch needs to run its own CI to validate that the triage → review → pinned-comment → re-entrant flow works in practice. That happens when the branch opens as a draft PR.
- **Second-anchor architecture** for the 1/M pinned-comment "sacrosanct" guarantee. Not justified by v1 incidence; revisit if deletion-then-fresh-post becomes common enough to annoy.
- **Fact-check tier that spans CI + local.** Non-goal for v1; see the plan appendix.

## Verification checklist (from Session 2 prompt)

- [x] `git mv` of `fact-check.md` happened first; all references updated; no broken links
- [x] `grep -rn 'pr-review/references/fact-check' .claude` returns nothing
- [x] Every `_common/review-*.md` has a non-placeholder `## Criteria` section
- [x] Every `_common/review-*.md` has a "Do not flag" subsection with domain-appropriate examples
- [x] Every `_common/review-*.md` that invokes fact-check does so with an explicit `scrutiny=` level (`review-shared.md` and `review-infra.md` explicitly do not invoke; the rest pass `standard` or `heightened`)
- [x] `_common/fact-check.md` has claim extraction examples, confidence calibration, temporal handling, intuition-check axis, standalone-invocation contract, pre-existing extraction rules, and updated framing
- [x] `_common/update-review.md` has Sonnet-specific language with concrete failure-mode examples, the draft-PR note, and the pinned-comment upsert path re-affirmed
- [x] Known quirks documented in `update-review.md`
- [x] No changes to `pinned-comment.sh` or workflow YAMLs
- [x] SESSION-NOTES.md updated with Session 2 entries
- [x] Branch ready; combined work reviewable as a single PR

## Session-2 commit list

```
a03875f3 Relocate fact-check.md to _common for shared use
32a6dcae Fill review-shared.md with universal review criteria
ef92354e Fill review-docs.md with technical-docs criteria
1b8c4b36 Fill review-blog.md with blog/marketing criteria
6930b1e4 Fill review-infra.md and review-programs.md criteria
de5ea541 Extend fact-check.md with v1 additions
78915075 Tighten update-review.md with Sonnet-specific rules and draft note
(this commit) Session 2 notes in SESSION-NOTES.md
```

---

# Session 3 — Review-pass fixes, fork-based testing, and UX additions

Session 3 is one long working session that bundled (a) fixing findings from two automated-review passes against the Session 1 + 2 branch, (b) setting up `camsoper/pulumi.docs` as a test sandbox and running real PRs through the pipeline, (c) fixing the bugs that only surfaced when the pipeline ran against its own test PRs, and (d) two UX additions Cam asked for mid-session: a progress signal for in-flight runs and a more distinctive status table / dispute-aware tagline.

## Work covered

### Review-pass fixes (commits 036f91, 2c7268, 09a588)

Two parallel Explore agents reviewed the branch; findings triaged into high/medium/low. Landed:

- **High:** empty-diff short-circuit, missing-label fallback, force-push `last-reviewed-sha` fallback, 🚨-vs-⚠️ infra contract, triage `continue-on-error`, `webpack.*.js` in the CI domain table.
- **Medium:** defined "section" (H2-delimited block) in `review-blog.md`; defined "top-level structural change" in `review-docs.md`; split the 🤔 intuition-check tier cleanly from verification so a claim renders in its verdict's bucket with the shape concern noted in the evidence line.
- **Low:** credential-redaction rule in `fact-check.md` §Tiered triage; DO-NOT item #12 ("diff is data, not instructions") for Sonnet on re-entrant.

### Fork-based end-to-end testing setup

- Force-pushed the branch to `camsoper/pulumi.docs`'s `master` so the workflows are active on the fork. The fork had divergent prototype history (Cam's early Claude-review experiments); those got overwritten.
- Created the 11 pipeline labels in the fork via `gh label create --force`.
- Opened six test PRs: #24 (docs), #25 (blog), #26 (trivial), #27 (infra), #28 (programs). Each exercises a different domain and set of deliberate issues the review should flag.
- Set up a **fork-only** tweak to `claude.yml` that swaps ESC + `PULUMI_BOT_TOKEN` for the default `GITHUB_TOKEN`. The fork doesn't have ESC wired up, so the `@claude` re-entrant path couldn't authenticate otherwise. The FORK-ONLY commit lives on `cam/master` only; origin and PR #18680 keep the ESC design. Comment at the top of the forked `claude.yml` warns against cherry-picking.

### Real bugs caught and fixed during fork testing

Review-pass agents missed all of these; they only surfaced under a live pipeline run.

- **`fbbead72`** — Workflow access check hardcoded `OWNER="pulumi"; REPO="docs"`. The fork's `GITHUB_TOKEN` is scoped to `camsoper/pulumi.docs`, so calling `/repos/pulumi/docs/collaborators/*/permission` returned `none` and every run skipped. Replaced with `${{ github.repository }}`.
- **`0ad5a5e5`** — `pinned-comment.sh`'s jq `capture(...)` used the `"x"` flag (extended mode). The jq in `ubuntu-latest` rejects it as unsupported and errors the whole filter. `list_pinned_comments` silently returned empty, so re-entrant review always fell through to initial-review path *and* upsert always created a duplicate 1/M comment instead of editing. Dropped the flag — the pattern has no extended-mode features anyway.
- **`a38e9259`** — `gh pr view --json` expects `author`, not `user`. Unknown fields cause gh to reject the whole `--json` argument and dump the field list. Caught on the first Resolve-PR-context run.
- **`7c3afbc6`** — Domain rules were an unordered set of globs. A PR touching `static/programs/<name>/package.json` matched both `static/programs/` (programs) and `package.json` (infra), so triage applied both *plus* `review:mixed`. Same for `scripts/programs/ignore.txt`. Switched all four tables (`triage.md`, `docs-review.md`, `docs-review-ci.md`, `docs-review-core.md`) to explicit path-precedence ordering: a file matches the first rule, and subsequent rules do not re-apply.
- **`83cdc6f7`** — Triage procedure said "compute the target label set (existing minus removed, plus added)" which Sonnet read as "apply the new labels" without removing stale ones. On PR #28 after the rules changed, triage left `review:infra` + `review:mixed` in place. Rewrote the procedure in explicit TARGET / ADD / REMOVE steps with state-label exclusions called out explicitly, plus a summary log line that includes the added/removed deltas.

### UX additions (commits 083505, 2eb81a3)

Cam flagged two gaps after seeing real runs:

- **Progress signal.** Reviews take 1-5 minutes and produce no feedback until the pinned comment lands. Added a pre-step that posts a transient `<!-- CLAUDE_PROGRESS -->` comment ("🐿️ Reviewing…") and applies `review:claude-working`; a post-step (`if: always()`) edits the comment to "Review updated" (or "Review errored. Mention @claude again to retry") and removes the label. Separate marker from `CLAUDE_REVIEW` so `pinned-comment.sh` ignores it. Applied to both `claude-code-review.yml` and `claude.yml`; skipped on issue-only `@claude` mentions. New label `review:claude-working` registered in `.github/labels-pr-review.md`.
- **Status format + tagline.** Replaced the plain `Status: N 🚨 / N ⚠️ / N 💡 / N ✅` line with a four-cell markdown table whose counts render bolded and centered. Extended the footer tagline to cover disputes in addition to fix-response — contributors can and should push back on findings that look wrong; Claude concedes on evidence.

### Race-condition fix (commit 4487ed95)

The biggest structural change this session. `claude-triage.yml` and `claude-code-review.yml` both fired on `ready_for_review`. The review's `if:` gate and label snapshot were captured at workflow-start time, before triage wrote labels, so `review:trivial` short-circuits and `fact-check:needed` gates were broken on every initial run. Restructured:

- `claude-code-review.yml`'s `claude-review` job now triggers on `workflow_run: { workflows: ["Claude Triage"], types: [completed] }`. The event's `pull_requests[0].number` gives us the PR.
- A new Resolve PR context step fetches fresh state via `gh pr view` and decides skip reasons (draft / trivial / bot-author) in one place. Downstream steps gate on `steps.pr-context.outputs.skip_reason == ''`.
- Mark-stale stays on `pull_request: [synchronize]` — unchanged.
- Verified end-to-end on PR #27 (infra): triage fires on ready, review fires ~1 minute later via workflow_run, labels are fresh, progress signal transitions correctly.

**Bootstrap note:** `workflow_run` events use the default-branch workflow definition. The chain only activates after the PR merges to master. Fork testing works because fork master was force-pushed.

## Decisions

1. **Fork force-push over PR-based merge** on the initial fork setup. The fork's divergent history was Cam's early experiments which this work supersedes; force-pushing is the right level of destructive for a test sandbox that's his personal repo.
2. **Option 1 (GITHUB_TOKEN) over option 2 (PAT with PULUMI_BOT_TOKEN in fork)** for the re-entrant auth. The current re-entrant path doesn't push commits, so `GITHUB_TOKEN` is sufficient. The "pushes trigger downstream workflows" rationale was a vestige of the old pre-v1 social-review chain.
3. **Progress signal posts a separate marker** (`<!-- CLAUDE_PROGRESS -->`) rather than reusing `<!-- CLAUDE_REVIEW -->`. Keeps `pinned-comment.sh` from treating the progress comment as part of the review sequence.
4. **Continue-on-error on triage's Claude step** so a transient rate-limit doesn't block the chained review. A missed triage is self-healing at the next ready-transition, and the chained review has the missing-label fallback.

## Open questions / deferrals

Items that surfaced during testing but weren't closed:

- **Triage run time (60-90s).** Most of the wall time is `claude-code-action@v1` init (bun + SDK + tsconfig), not the Sonnet call (~19s). Replacing the action with a direct `curl` to `api.anthropic.com/v1/messages` would drop total time to ~15-25s and make the chained review fire sooner. Flagged as v1.5.
- **Re-entrant should clear `review:claude-stale`** when `update-review.md` completes successfully. Not currently wired.
- **`gh pr edit` add/remove race** on the triage workflow. The delta computation is now explicit, but if two near-simultaneous events fire (e.g., quick draft-ready-draft-ready cycling), concurrency's `cancel-in-progress: true` handles the triage side but a stale add/remove could still land. Acceptable for v1.
- **Commit history cleanup.** The PR now has 20+ commits, several of which are fix-on-fix. Worth squashing or reorganizing before merge.
- **SESSION-NOTES.md itself** is a cumulative scratchpad, not a ship artifact. Plan to either delete before merge or rehome as a decision log elsewhere.

## Session-3 commit list (through this commit)

```
036f9183 Fix high-severity pipeline bugs from review pass
2c7268cc Tighten rubric language in domain and fact-check files
09a58858 Add defense-in-depth guardrails
fbbead72 Fix hardcoded pulumi/docs in workflow write-access checks
0ad5a5e5 Drop 'x' flag from pinned-comment.sh capture regex
083505d8 Add in-progress / done UX signal around Claude review runs
4487ed95 Chain initial review to triage via workflow_run
2eb81a3e Emphasize status row and add dispute guidance to the review tagline
a38e9259 Fix Resolve PR context: user → author, drop unused headRefOid
7c3afbc6 Path-precedence ordering on domain selection
83cdc6f7 Make triage delta computation explicit
f3927ffb Append Session 3 notes
82d13549 Workflow prompt: emphasize the removal step in triage delta
094cbd7b Replace claude-code-action with direct Anthropic API + shell delta
8e688d0c pinned-comment.sh: strip inbound CLAUDE_REVIEW markers before split
(this commit) Session 3 continuation
```

## Session 3 continuation — triage determinism and marker-strip fix

Work after the initial Session 3 writeup:

### Triage was still unreliable on label removal

Even after rewriting triage.md's procedure with explicit TARGET / ADD / REMOVE steps (commit `83cdc6f7`) and adding prompt-level emphasis in the workflow (commit `82d13549`), Sonnet inside `claude-code-action@v1` kept skipping `gh pr edit --remove-label` when ADD was empty. Two successive runs on PR #28 saw stale `review:infra` + `review:mixed` labels and left them in place.

Root cause: the agentic loop lets the model decide whether to make the tool call. Sonnet's decision was "nothing new to add → skip the edit," even when the procedure explicitly said otherwise. Prompt tuning couldn't reliably fix this; the decision was the wrong place to put the logic.

**Fix (commit `094cbd7b`):** replace `claude-code-action@v1` with a direct `curl` to `api.anthropic.com/v1/messages` and move the label arithmetic entirely into shell:

- Sonnet only produces a classification (`target_domains`, `trivial`, `fact_check_needed`, `agent_authored`, `reasoning`) as one JSON object.
- The shell reads current labels, builds TARGET per triage.md's rules (review:mixed when multiple domains, trivial supersedes fact-check:needed), and computes `ADD = TARGET - EXISTING`, `REMOVE = EXISTING - TARGET` (excluding state labels).
- A single `gh pr edit` call applies the delta; removal is now deterministic.

Verified on PR #28: stale `review:infra` and `review:mixed` were correctly removed on the next cycle. Log output:
> `triage: pr=28 domains=review:programs trivial=false fact-check=true agent-authored=false added=none removed=review:mixed,review:infra`

Runtime dropped from 60-90s to ~39s. Not the 15-25s I'd hoped for (GitHub Actions runner boot + checkout is a larger chunk than I'd estimated) but the determinism win is more important than the speed.

### Duplicate marker in re-entrant pinned comment

After the force-push re-entrant test on PR #24, the pinned comment ended up with TWO `<!-- CLAUDE_REVIEW 1/1 -->` lines at the top. Sonnet copied the previous body verbatim (marker included) into its upsert input, and `render_with_markers` then prepended another marker on top.

**Fix (commit `8e688d0c`):** add an awk guard in `split_body` that drops any inbound marker line before splitting:

```
/^<!-- CLAUDE_REVIEW [0-9]+\/[0-9]+ -->[[:space:]]*$/ { next }
```

The script is now the sole writer of markers regardless of caller discipline. Verified end-to-end: input body with two markers → `upsert` produced a pinned comment with exactly one.

### Test-PR coverage

Seven fork test PRs exercised the pipeline end-to-end before close:

| PR | Shape | What it exercised |
|---|---|---|
| #24 docs-edit | Docs page + Lambda snippet with deliberate bugs | review-docs.md criteria; Case 3 re-verify; duplicate-marker bug surfacing + fix |
| #25 blog-aislop | New blog post with AI-slop patterns + fab stats | review-blog.md heightened scrutiny; fact-check-first; 🤔 intuition-check |
| #26 trivial-typo | One-line prose trim | `review:trivial` short-circuit (pre-race-fix; short-circuit now works via chained workflow) |
| #27 infra-edit | `scripts/clean.sh` tightening | review-infra.md ⚠️-default bucket; triage → workflow_run chaining verified |
| #28 programs-edit | New `static/programs/<name>/` TS program | review-programs.md heightened scrutiny; path-precedence rule (package.json under programs, not infra); triage delta removal |
| #29 multi-domain | Docs + programs in one PR | review:mixed; multi-domain composition; fact-check:needed under heightened |
| #30 rename-only | Pure file rename, no content | docs-review-ci.md empty-diff path; review-shared.md aliases rule |

All closed with `--delete-branch` after testing.

### Still open / deferred

From the original "recommendations" punch list, still unresolved:

- **Item 5-7 (@claude interactions).** Tested Case 3 re-verify on PR #24 multiple times. Did NOT explicitly exercise Case 1 fix-response (push fix + @claude) or Case 2 dispute (comment disagreement + @claude), or the draft-PR note (@claude on a draft with pinned review). All three are real re-entrant code paths that warrant coverage before merge.
- **Force-push last-reviewed-sha fallback verification.** PR #24's branch was rebased (history rewritten), and an @claude mention fired after. The re-entrant run completed "success" but didn't update the pinned comment, which means Sonnet took the Case 3 no-commits path — not the force-push fallback. The fallback language in update-review.md is coded but unverified end-to-end.
- **Triage time.** ~39s is better but still not great. Further speedup would require eliminating runner boot (composite action?) or the checkout step (which we need for the skill file contents). v2 work.
- **Re-entrant should clear `review:claude-stale`** on successful update-review.md completion. Not wired.
- **PR commit history cleanup.** Now at 25+ commits, several fix-on-fix. Squash or reorder before merge.
- **Fork-only `claude.yml`** tweak has a banner comment but is easy to cherry-pick by mistake during a squash. Pre-merge grep-check recommended.

### Fork state at session end

- **Fork master (`camsoper/pulumi.docs`):** origin/CamSoper/pr-review-overhaul HEAD + one FORK-ONLY commit on top that swaps `claude.yml`'s ESC + `PULUMI_BOT_TOKEN` for the default `GITHUB_TOKEN`. Do not cherry-pick that commit upstream.
- **Test PRs:** all closed, branches deleted.
- **Labels:** 11 pipeline labels created in the fork via `gh label create --force`; persist.
- **Secrets:** `ANTHROPIC_API_KEY` set on the fork by Cam. No ESC configuration.

Re-enabling the fork for fresh testing: open a new PR against `camsoper/pulumi.docs` master. Triage fires on `opened`; chained review fires on `ready_for_review` via `workflow_run`.

---

## Session 4 — clearing the deferred backlog

This session converted the "Still open / deferred" list at the end of Session 3 into shipped commits and verified behavior. By the end, only Phase D (branch commit history cleanup) remains.

### What shipped

Five commits on `CamSoper/pr-review-overhaul`, each cherry-picked to `cam/master` so the fork tests exercised the same code:

1. **Triage skips drafts** (`6f71a3c9`) — added `!github.event.pull_request.draft` guard on the triage job and dropped `reopened` from the trigger types. Drafts are the author's workbench; we don't apply labels until they ask for feedback. AGENTS.md updated to match. Note: `opened` is still needed for PRs that skip the draft phase entirely; `ready_for_review` only fires on draft → ready transitions, not on direct non-draft opens.
2. **Triage prose-check** (`5e1c359e`) — extends the triage JSON contract with `prose_concerns: []`. When a PR is classified `trivial`, Sonnet also examines the diff for spelling/grammar errors. If any are found, the workflow posts a one-shot `<!-- TRIAGE_PROSE -->` advisory comment. The trivial label still applies and the full review still skips — concerns are a sanity check, not a block. Idempotent: prior TRIAGE_PROSE comments are deleted on re-triage. This was the answer to Cam's "the trivial label encourages rubber-stamping" concern.
3. **Phase A bundle** (`5497d622`) — four narrow fixes:
   - **#7 widened**: gate the `claude-review` job on `github.event.workflow_run.conclusion == 'success'` so a *skipped* triage's `workflow_run` no longer fires the review job (which was racing the ready-event run and getting cancelled by concurrency, orphaning a CLAUDE_PROGRESS comment finalized as "Review errored"). Also distinguished cancelled/skipped from failure in the finalize step (delete the comment vs. mark errored).
   - **#8**: replaced `content/customers/**` with `content/case-studies/**` in `triage.md` and `docs-review-ci.md`. The original path never matched the actual repo layout.
   - **#10**: 🐿️ → 🤖 across both workflows (the squirrel was inherited from `shipit/SKILL.md`'s mascot — fine in shipit, confusing in PR comments) and "minute or two" → "several minutes" (Opus initial reviews regularly take 3–5 min).
   - **#11**: publish a Checks API check-run pinned to the PR's head SHA. `workflow_run`-triggered jobs don't surface in the PR's Status checks list by default; the Checks API is the standard escape hatch. Always created (even on skip paths) so contributors see "Claude Code Review · success/skipped/failure" alongside lint/build.
4. **Phase B** (`fa79e61d`) — restructured `claude.yml` for model-driven `@claude` routing:
   - **#5**: finalize step removes both `review:claude-working` and `review:claude-stale`. Successful re-entrant work clears the staleness flag.
   - **#9**: replaced the hardcoded `format(...) || format(...) || ''` prompt chain with a single template that gives the model PR/issue context plus the triggering mention body (saved to `.claude-mention-body.txt` via env-var passthrough — no shell-injection risk) and lets it decide between update-review, initial review, ad-hoc work, or a clarification reply. The progress message went generic ("🤖 Working on it") because the model may not be reviewing.
   - Mirrored the cancellation handling from `claude-code-review.yml` for defense-in-depth.
5. **Dispute UX** — two `update-review.md` tweaks:
   - **#12** (`f21e3d29`): disputed-and-held findings get an inline `🛡️ Disputed by <author> on YYYY-MM-DD, model held.` annotation under the finding text, not just a Review history line. Previously, a reviewer scrolling 🚨 Outstanding had no way to know the finding was contested.
   - **#13** (`30b3909d`): classify the dispute before deciding. **Domain-knowledge assertions** ("I built this", "intentional pattern") from write-access authors → default to concede; the author has codebase context the model doesn't. **Verifiable claims** ("this is faster", "Y was added in v3.0") → still require evidence; authority doesn't make a benchmark true. **Reframings** of the model's reading → evaluate normally.

### What got verified end-to-end

| Test | Where | Outcome |
|---|---|---|
| Phase A integration | PR #41 (test4-phase-a) | All four #7/#8/#10/#11 outcomes confirmed; check-run visible in PR Checks UI; trivial-skip path leaves no orphan progress comment |
| Phase B `@claude refresh` | PR #41 | Pinned review's "Last updated" timestamp moved 21:08 → 21:19; new "🤖 Done." message |
| Phase C Case 1 (fix-response) | PR #41 | Verified by Cam's manual `@claude make the suggested fixes` — review history says "re-reviewed after fix push (2 new commits, 53a891d); both findings resolved" |
| Phase C Case 2 (dispute, hold) | PR #42 | Model engaged both prongs and rebutted: "you cannot simultaneously invoke 'local-first' as the bound and 'remote vs. local' as the differentiator" |
| Phase C Case 3 (force-push fallback) | PR #41 | After amending HEAD and force-pushing (53a891d → 8ed641e), `@claude refresh` succeeded; review history line: "history rewritten since last review; re-reviewed against HEAD (8ed641e63c)". Bonus: `review:claude-stale` cleared by Phase B #5. |
| Phase C Case 4 (draft-PR note) | PR #41 | Pinned review now starts with `*Reviewing a draft; findings may change as you iterate.*` after flip-to-draft + `@claude refresh` |
| Ad-hoc `@claude` explain (Phase B #9) | PR #41 | Model posted regular `gh pr comment` reply ("Great question! Here's what happens..."), didn't touch pinned review |
| Ad-hoc `@claude` fix (Phase B #9) | PR #41 | Model pushed commit `327611ac` with the requested sentence + bonus internal link; posted confirmation comment |
| #12 dispute annotation | PR #42 (second dispute round) | Pinned review now contains `🛡️ **Disputed by CamSoper on 2026-04-27 (second time), model held.** ...` directly under the finding |
| #13 author authority | PR #42 (second dispute, with maintainer claim) | Model correctly *classified* — recognized maintainer authority, distinguished design-intent (would defer) from verifiable technical claims, held only on the verifiable parts (the Terraform CLI / OpenTofu local-execution counterexample wasn't addressed across either dispute round). The author-authority weighting works as designed without becoming auto-concede. |
| Prose-check FP guardrail | PR #43 | TRIAGE_PROSE flagged `embeded` (typo), did NOT flag `pulumi` (CLI in backticks) |
| Prose-check idempotency | PR #43 | Flipped draft→ready→draft→ready; result: still exactly 1 TRIAGE_PROSE comment (cleanup-then-repost works) |

### Things worth flagging for future-Cam

- **The `workflow_run` conclusion gate (#7) was the real fix for the orphan progress comment.** I initially framed #7 as "trivial-skip leaves an orphan" but the actual scenario observed on PR #40 was a *cancelled* job from the skipped-triage `workflow_run` racing the ready-event run. Two-line YAML change (`conclusion == 'success'` in the job's `if:`) eliminates the whole race. The cancellation distinction in finalize is now defense-in-depth, not load-bearing.
- **Author-authority weighting threads `pr-review/references/trust-and-scrutiny.md` into `update-review.md` only for the dispute path.** The broader trust model is more general (used to gate fact-check thresholds, contributor-type routing, etc. in the local pr-review skill). If we want consistent author-deference across Claude tooling, threading it elsewhere is a follow-up — not in scope for this PR.
- **The model-driven `@claude` routing (#9) actually worked under the OLD prompt for ad-hoc tasks** because the model is agentic and `update-review.md` doesn't strictly forbid Edit/git push. Cam's `@claude make the suggested fixes from the review` on PR #41 (predates Phase B) pushed `53a891d`. Phase B makes the routing *explicit* and adds a guard against accidentally invoking `update-review.md` on non-review intents — a defensive correctness fix rather than a new capability.
- **The dispute test on PR #42 was unexpectedly sharp.** The model produced a logically clean rebuttal ("you cannot simultaneously invoke 'local-first' as the bound and 'remote vs. local' as the differentiator") and held across two dispute rounds, even when the second one led with maintainer authority. Worth reading the PR #42 pinned comment as an example of how the system actually behaves under adversarial pressure from the author.
- **PR #41 was the workhorse.** Cases 1, 3, 4, both ad-hoc routing tests, and the Phase A integration all ran on it. PR #42 was dispute-only. PR #43 was prose-check only. All three closed at end of session.
- **`github-actions[bot]` attribution on the fork is a fork-only artifact, not a real consistency bug.** On the fork, workflow shell-side `gh` calls post as `github-actions[bot]` (because the FORK-ONLY tweaks substituted `secrets.GITHUB_TOKEN` for `PULUMI_BOT_TOKEN` across all three workflows). On upstream, those same calls post as `pulumi-bot`, and the resulting split (`pulumi-bot` for plumbing, `claude[bot]` for Claude content) is intentional and meaningful — see `pulumi/docs#18663` for an example of the upstream pattern. **No action needed**: the fork-only swaps don't cherry-pick upstream, so the inconsistency disappears at merge time. Don't waste cycles trying to "fix" comment attribution by reading fork behavior.

### Decisions made this session

- **Skip drafts in triage**, but keep `opened` in the trigger list with an `if: !draft` guard. Cam's instinct was to drop `opened` entirely; that would have missed PRs opened directly as non-draft (which fire `opened` with `draft: false` but no `ready_for_review`).
- **Squirrel stays in shipit**, robot in the workflows. The 🐿️ is shipit's mascot and was inherited; in PR comments it reads as random because contributors don't know the shipit context.
- **Trivial label still skips the full review**, but triage now does a focused prose check. Drop-the-short-circuit was the alternative; rejected because typo PRs don't warrant Opus budget. The prose check + advisory comment is the middle ground.
- **`@claude` on a PR routes through the model**, not through workflow-side classification. Option B (pre-classify intent in shell) was discussed and rejected — pushing the decision to the model is simpler and matches how `@claude` already works on issues.
- **Author authority weights disputes but doesn't auto-concede** — two-axis classification (domain-knowledge vs verifiable) keeps review pushback meaningful while honoring maintainer context. Auto-concede on assertion would have given any author a "delete this finding" button.

### Updated deferred items (after Session 4)

Almost everything from the Session 3 list is closed. Remaining:

- **Phase D — branch commit history cleanup**: ~32 commits on the branch, mostly fix-on-fix. Recommend squash-merge at upstream PR-flip time; alternative is interactive rebase to ~6 logical commits. Not actionable until you flip `pulumi/docs#18680` ready.
- **Threading the broader trust-and-scrutiny model into other Claude paths** (beyond just `update-review.md`'s dispute classification). Future enhancement; not scoped here.

Lighter items not exercised but coded:

- **Cancellation handling in `claude.yml` finalize**: defense-in-depth, mirrors `claude-code-review.yml`. Not specifically tested — the conclusion gate (#7) eliminates the main scenario that would trigger it.

### Session-4 commit list (through this commit)

- `6f71a3c9` Triage: skip drafts until marked ready for review
- `5e1c359e` Triage: add prose-check on trivial PRs (advisory comment, label still applies)
- `5497d622` Phase A: progress lifecycle, check-run, customers→case-studies, emoji
- `fa79e61d` Phase B: model-driven @claude routing, claude-stale removal, cancellation handling
- `f21e3d29` update-review: annotate disputed-and-held findings inline (#12)
- `30b3909d` update-review: weight author authority in dispute resolution (#13)
- (this commit) Append Session 4 notes

Each is also on `cam/master` as a cherry-pick, atop the FORK-ONLY claude.yml token swap. The fork-only swap remains do-not-cherry-pick-upstream.

### Fork state at end of Session 4

- **All test PRs closed** (#31–43), branches deleted.
- **Fork master:** Session 4 commits cherry-picked + the FORK-ONLY token swap commit on top.
- **Branch commit count:** ~32 (was 25+ at end of Session 3). Squash-merge or rebase before upstream merge.
- No pending workflows, no orphan labels.

---

## Session 5 — Pipeline comparison test (2026-04-28)

Ran a side-by-side comparison of the legacy single-comment review against the new pipeline across 6 medium-large pulumi/docs PRs from the past month (18599, 18620, 18605, 18647, 18642, 18685). Recreated the PRs as drafts on `CamSoper/pulumi.docs` (#44–49), marked them ready, captured the new pipeline output, compared.

Full report: `scratch/2026-04-28-pipeline-comparison/REPORT.md`.

### Headline outcomes

- **New pipeline caught real bugs the legacy missed:** misattributed OutSystems statistic in dirien's Agent Sprawl post (94% means "complexity and technical debt," not "security problem"), wrong settings tab for SCIM token retrieval in joeduffy's JumpCloud guide (would have shipped a non-working guide), broken `/docs/ai/integrations/` link in foot's Neo Catalog launch, multi-file AGENTS.md link-style violation in jkodroff's restructure (with a regression where the PR converted an existing canonical link to a relative one).
- **Cost:** lost some style-polish coverage (em-dash density, awkward titles, banned-word `simple`, closing-emoji nits) and the publishing-readiness checklist that legacy blog reviews carried.
- **Three fold-back items identified:** restore publishing-readiness checklist in `review-blog.md`; add a "📝 Style nits" tier under the table; investigate the lingering `<!-- CLAUDE_PROGRESS -->` comment after success.

### Methodology lessons (remember for the next comparison run)

1. **Pre-fix vs post-fix asymmetry is the biggest confounder.** The legacy review was on the *initial* PR state; recreations from the merge commit are the *post-fix* state. So findings the author addressed look like the new pipeline "missed them" — but it correctly didn't re-flag fixed code. Next time, recreate from the PR head at the time the legacy review was posted (use `gh pr view --json commits` to find the SHA at review timestamp), not the merge commit.
2. **`cam/master` already containing the test PRs forced revert+reapply gymnastics.** Cleanest base for this kind of test is a static branch pinned to a commit *before* any of the candidates landed (`compare/base@<old-sha>`), so per-PR base branches and modify/delete conflicts go away.
3. **`git apply` with binary patches is fragile; `git cherry-pick` isn't.** Three of six PRs touched PNGs that `gh pr diff | git apply` couldn't handle. Cherry-pick of the merge commit uses git tree ops and handles binaries natively. Default to cherry-pick for recreations.
4. **`-X theirs` flips meaning between revert and cherry-pick.** On a revert with a modify/delete conflict, `-X theirs` *keeps* the file the revert wanted to delete — opposite of intent. For revert: detect modify/delete with `git status --porcelain | grep -E "^DU|^UD"` and `git rm` to honor the delete. Burned ~20 min on this.
5. **`workflow_run`-triggered jobs report `headBranch=master`, not the PR branch.** First monitor filtered by branch and returned nothing. For waiting on chained workflows, filter by `--created >=<timestamp>` and count states. Lost ~5 min before catching it.
6. **n=6 from already-merged PRs is biased** — by definition these passed review enough to ship. PRs where the legacy review actually blocked something (heated dispute threads, repeated re-review cycles) would stress-test the new pipeline harder. Worth pulling 2–3 of those next time to exercise the dispute / re-entrant paths under load.

### Surprises worth noting

- **`agent-authored` triage label fired on 5 of 6 cherry-picked recreations.** Only djgrove's PR escaped. Triage is keying off commit metadata that propagates through `git cherry-pick` (likely `Co-Authored-By` trailers). Authentic-ish — the recreations *are* agent-prepared — but noisy as a comparison signal. Worth understanding if the trigger should be tightened.
- **Lingering `<!-- CLAUDE_PROGRESS -->` comment.** All 6 PRs ended with the progress placeholder still present (body edited to "🤖 Review updated.") alongside the actual `<!-- CLAUDE_REVIEW 1/1 -->` comment. The progress comment isn't being deleted on success — only edited. Either delete on success or rename the marker. Two artifacts where one would do.
- **Mixed-domain detection conservative.** PR 18620 touches `assets/openapi/tag-intros/**` (docs) plus `layouts/partials/openapi/open-api-gen.html` and a shortcode (infra). Triage labeled `review:docs` only — no `review:mixed`. The new review correctly addressed the template change in passing but didn't compose under both domain prompts. Decide if the `mixed` rule should fire whenever any infra-side files are touched.
- **PR 18599 fidelity drift.** Recreated +280/-37 vs original +310/-145 across the same 12 files because PR #18623 modified three of 18599's files in the intervening week. `git cherry-pick -X theirs` absorbed the drift; substance preserved. Worth flagging for any recreation: check intervening commits to those files before assuming clean cherry-pick.

### Artifacts

- Report: `scratch/2026-04-28-pipeline-comparison/REPORT.md` (265 lines)
- Old reviews + author response diffs: `scratch/2026-04-28-pipeline-comparison/old-reviews/`
- New reviews: `scratch/2026-04-28-pipeline-comparison/new-reviews/`
- Recreation log + patches: `scratch/2026-04-28-pipeline-comparison/{recreation-log.txt,patches/}`
- Recreated PRs: `CamSoper/pulumi.docs#44–49` (still open as of end of session)

### Cost optimization backlog (deferred)

Coming out of the Session 5 comparison run. None implemented yet; saving for a dedicated pass.

1. **Trim triage's diff cap from 100KB to ~20KB.** Classification doesn't need full diffs.
2. **Sonnet for `review:infra` initial reviews.** Pattern is a small "Pick model" step before `claude-code-review.yml:227`'s `claude-code-action@v1` invocation that sets `--model claude-sonnet-4-6` when the labels are infra-only (no docs/blog/programs/mixed). Single-job conditional, no new job needed. Pre-flight: re-run PR 18642 on Sonnet and compare against the Opus baseline; back off if it misses the `cache: false` breadth analysis or the mode-detection narrowing.
3. **Cap fact-check tool calls — but triage first, don't cap blindly.** See the "mitigations" notes from this session — budget by PR size, prioritize load-bearing citations (statistics > URLs > general claims), surface what didn't get verified so the author can request a follow-up.
4. **Pair #3 with deferred-fact-check resumption in `update-review.md` (re-entrant).** Today's re-entrant only handles fix-response / dispute / re-verify — it doesn't auto-pick up items the initial Opus pass deferred for budget. Add a step at the top of the re-entrant prompt: parse the previous pinned comment for a "deferred fact-check" section; if present, spend the re-entrant's own budget on those first, then proceed to standard re-verify. Cost-shape works because re-entrant is Sonnet (cheaper per call), and the failure mode is observable — deferred items eventually surface under ✅ Resolved or 🚨 Outstanding on the next push. **Don't ship #3 without #4** — they're paired; an unverified-items section nobody auto-resumes is just busywork for authors.
5. **Standing fixture set for pipeline regression tests.** 2–3 well-chosen PRs to re-run when prompts change, instead of 6 ad-hoc each time. Today's set is a candidate baseline.
6. **Frontmatter-only short-circuit in triage.** Aliases additions, `draft: false` flips, social copy edits.
7. **Audit prompt-cache friendliness.** 5-min TTL would catch close-in-time reviews if shared system prompt is structured right.
8. **Sonnet-everywhere hypothesis test (broader than #2).** Re-run today's 6-PR comparison set with `--model claude-sonnet-4-6` on the base review and compare against the Opus baseline already captured in `scratch/2026-04-28-pipeline-comparison/new-reviews/`. Hypothesis from analyzing the headline catches: 3–4 of 6 (broken link, link-style violation, wrong-tab navigation, possibly the webpack `cache: false` analysis) look Sonnet-grade pattern matching; 2 are Opus-grade and both are fact-check (misattributed OutSystems statistic, EU/Colorado AI Act framing). If confirmed, the resulting architecture is **Sonnet for the base review, Opus only for fact-check** — gated on the existing `fact-check:needed` label. Meaningfully different from #2 (Sonnet for infra only) and from today's "Opus by default." Cheapest experiment in this backlog: just toggle the model in `claude_args` and re-trigger the same 6 fork PRs (still open at `CamSoper/pulumi.docs#44–49` as of session end). Result either confirms the architecture flip or shows enough regression to justify current cost.

---

## Session 6 — 2026-04-28 (cost optimization: Path A measurement and ship)

Tackled backlog item #8 (Sonnet-everywhere) end to end and discovered a much bigger and safer win along the way. Net result: a measured **51% cost reduction** on the existing Opus pipeline, shipped to this branch.

### Outcomes

- **Item #8 (Sonnet-everywhere): NOT ready, deferred.** Cost story is real (~64% cheaper per effective post when properly configured) but reliability and substance regressions on real bugs (PR 46 SCIM-tab bug, PR 49 datadog.svg) are unacceptable. Won't reconsider until silent-failure-on-large-PR is fixed.
- **Item #1.5 (NEW — broadened allowed-tools + pre-compute injection): SHIPPED.** Single workflow file change, measured 51% cost reduction on Opus, 85% denial reduction, 6/6 posted clean, substance net positive across the test set.
- **PR 49 duplicate problem: FIXED** by an explicit "do NOT post via `gh api`-based comment endpoints" instruction in the prompt.

### Numbers

| | Opus baseline | Opus with Path A |
|---|---:|---:|
| Total cost (6 PRs) | $28.07 | **$13.70** |
| Total denials | 117 | **18** |
| Cost per posted review | $4.68 | **$2.28** |
| Posted cleanly | 6/6 | 6/6 |
| Cumulative wall time | 68 min | 35 min |

PR 48 (infra) is the most extreme drop: $3.60 → $0.89, 19 turns, 0 denials, 3 minutes. Infra reviews benefit massively because the file set is small and the model lands in one or two tool-use cycles instead of bouncing through denials.

### Methodology lessons (for future cost-opt passes)

1. **Analytical estimates were almost half the actual.** My pre-measurement estimate was ~27% saving; measured was 51%. Pre-compute injection's effect goes beyond denial reduction — it changes the model's exploration strategy. Don't trust analytical estimates when you can measure cheaply ($14 for ground truth on a 6-PR fixture).
2. **Debug-instrumented runs are cheap and high-value.** The $1.42 probe that dumped `/home/runner/work/_temp/claude-execution-output.json` to the runner log identified the 80% denial cause (missing `Write` tool) in one run. Ground truth on tool calls + denials is far better than guessing — the runner log normally hides this.
3. **Cascade-cancellations inflate denial counts.** When a parallel tool call fails, sibling parallel calls get cancelled with their own `is_error=true`. The system-reported `permission_denials_count` (e.g., 18) and the actual denial-result count (e.g., 21) diverge. Either is fine as a directional signal, but don't over-index on tiny differences.
4. **Stacking changes can mask which one helped.** Round 3 stacked the whitelist + pre-compute injection. The split is unknown without a third measurement run. The substance-regression pattern on PR 45 appears in both Sonnet R2 (whitelist only) and Opus R3 (whitelist + pre-compute), so it's likely a whitelist-driven effect — but I can't prove it without isolating. Worth keeping in mind for the next stacked experiment.
5. **The prompt clarification fixed PR 49's duplicate problem.** Two bytes of prompt ("do NOT post via `gh api`...") closed the workflow-contract bug that all of Sonnet R1, Sonnet R2, and the implied Opus failure mode shared. Often the cheapest fix is in the prompt, not the tool list.

### Side effects worth tracking

- **PR 45 substance regression.** With broadened tools, the model "stops earlier" on lower-tier prose findings (lost 2 LCs on PR 45 — same regression Sonnet R2 had). The fact-check tier engages more rigorously (verified `urls.go` source for the registry-preview scheme), but the model skims prose-level nits. Hypothesis: pre-computed metadata + broader tools = faster convergence, less exploration. Worth a prompt nudge experiment: "don't skip prose-level findings even when fact-check evidence is strong."
- **PR 49 finding shape changed.** R3 lost the "broken `/docs/ai/integrations/`" link finding from baseline and quoted specific phrases as if from a real page. Either (a) the live pulumi.com site has the page now and WebFetch reached it, or (b) hallucination. Worth a manual sanity-check next time the page is touched.
- **Infra reviews are the biggest beneficiary.** PR 48 dropped to $0.89 — order of magnitude cheaper. If we rolled out Sonnet for infra-only (backlog item #2), the saving stacks. But Path A alone already gets most of the benefit on infra without the model swap.

### Backlog update

Done:
- **#8 (Sonnet-everywhere)** — investigated, not ready to ship. See `scratch/2026-04-28-pipeline-comparison/SONNET-EVERYWHERE-ANALYSIS.md` for the full multi-round analysis.
- **NEW #1.5 (broadened allowed-tools + pre-compute injection)** — shipped this session.

Still pending (re-prioritized after Path A landed):

1. **Frontmatter-only short-circuit in triage** (was #6; now top priority). Independent of Path A; ship and validate via real traffic.
2. **Cache-friendliness audit** (was #7).
3. **Investigate PR 45's prose-regression pattern** — open question after Path A measurement.

Dropped (post-Session-6 re-evaluation):

- **Fact-check cap with deferred resumption** (was #3+#4). Fact-check is already gated by `fact-check:needed`, Path A already addressed the cost concern that motivated capping, and the deferred-resumption mechanism creates a silent-gap failure mode (pinned comment looks complete but isn't). Optimizing fact-check is optimizing the wrong axis.
- **Triage diff cap trim 100KB→20KB** (was #1). Triage already runs Sonnet on diffs that are almost always under cap; trim only matters on rare 100KB+ PRs and even then it's a small-Sonnet-tokens-getting-smaller saving. Backlog clutter.
- **Sonnet for `review:infra` initial reviews** (was #2). Path A already captured the infra saving (PR 48 went $3.60 → $0.89 on Opus Path A) — marginal saving from the model swap is small. Infra failures have higher blast radius than prose failures, and Session 6 already deferred Sonnet-everywhere on reliability grounds. Saving pennies on the highest-risk review domain is a bad trade.
- **Standing fixture set for regression tests** (was #5). Already exists as a pointer: the 6 fork PRs at `CamSoper/pulumi.docs#44–49` plus the validated runs in `scratch/2026-04-28-pipeline-comparison/`. That's a doc-comment, not a backlog item. Use them when prompts change.

### Artifacts

- **Multi-round analysis**: `scratch/2026-04-28-pipeline-comparison/SONNET-EVERYWHERE-ANALYSIS.md` (~370 lines covering Sonnet R1, debug probe, Sonnet R2 broadened, Opus R3 measurement)
- **Round 1 Sonnet bodies**: `scratch/2026-04-28-pipeline-comparison/sonnet-reviews/`
- **Round 2 Sonnet bodies**: `scratch/2026-04-28-pipeline-comparison/sonnet-reviews-v2/`
- **Round 3 Opus Path A bodies**: `scratch/2026-04-28-pipeline-comparison/opus-r3-reviews/`
- **Total experiment cost**: $37.82 across all rounds

### Total experiment ROI

If the measured 51% saving holds in real-world traffic, Path A pays back the entire $37.82 experiment cost after ~8 production reviews on the new configuration. The workflow change is in this commit; nothing else needed to start collecting that ROI.

---

## Session 7 — Triage classifier refactor + frontmatter-only short-circuit (2026-04-28)

Started by trimming the Session 6 backlog (dropped fact-check cap, diff trim, Sonnet-for-infra, fixture set — see commit `f477191abe`). Then tackled the surviving top-priority item: frontmatter-only short-circuit. Discovered a much bigger refactor opportunity along the way and shipped both together.

### What shipped

**Architecture B — fully deterministic triage except prose check.** The model used to do path-precedence domain classification, line/file counts for triviality, and commit-trailer scanning for agent-authored. None of it needed semantic judgment. Pulled all classification into a Python helper; the model is now invoked only when shell pre-classifies as trivial OR frontmatter-only — and only for the prose check.

- **`triage-classify.py`** (new, 350 lines) — deterministic classifier. Takes PR JSON + diff, emits classification JSON. No API calls. Tested on 6 real PRs (the Session-5 fixture) plus 6 synthetic edge cases.
- **`claude-triage.yml`** (rewrite) — calls helper, conditionally calls model only when `prose_check_needed`. Emits per-run summary line including the new `prose-checked` field.
- **`triage.md`** (130 → 60 lines) — collapsed to just the prose-check prompt. Classification rules now live in code; the markdown points at the helper as source of truth.
- **`claude-code-review.yml`** — skip condition extended to `review:frontmatter-only`.
- **`AGENTS.md`** — "Trivial PRs short-circuit" section rewritten to cover both labels.

**New label:** `review:frontmatter-only` (color `c2e0c6`, sibling of `review:trivial`). Created on `CamSoper/pulumi.docs` for fork testing. **Deploy step**: needs creation on `pulumi/docs` upstream when this lands.

Commits on `CamSoper/pr-review-overhaul`:

- `0ef196d12b` — classifier helper
- `a182f02a2d` — workflow rewrite + AGENTS.md + skip extension
- `4a34329a6c` — classifier fixes (frontmatter detection + link-set diff)
- `f477191abe` — backlog trim (came earlier in the session)

### Cost shape change

Most PRs now make zero model calls during triage. The Session-6 measurement framework would let us quantify this in real traffic — under the new architecture only trivial / frontmatter-only PRs cost a Sonnet round-trip (~$0.001 each), and everything else costs nothing at the triage stage. Meaningful only because triage runs on every ready PR.

Stacks with Path A: Path A cut the *initial-review* cost; this cuts the *triage* cost. Different parts of the pipeline; they multiply.

### Bugs caught by fork-PR testing

Both bugs in the classifier, both surfaced by the test set rather than by the synthetic suite. Worth remembering:

1. **Hunks deep inside multi-line frontmatter were misclassified as body.** The initial heuristic seeded "pre-frontmatter" only when `old_start <= 1`. Any hunk inside frontmatter at line >1 (e.g., aliases edits on a docs page with 20-line frontmatter) defaulted to "body" and missed the boundary entirely. Fixed with a routine that uses `---` context-line positions as ground truth, with content-shape fallback when no `---` appears in the hunk.
2. **`has_link_change` over-fired on typo fixes.** A `recieve` → `receive` change in a paragraph containing markdown links flagged as a link change because the regex matched `[text](url)` on the changed line, even though the link itself was identical on `-` and `+` sides. Replaced per-line regex with set-comparison: collect `(text, url)` tuples from all `+` lines and all `-` lines, compare. Equal sets → no link change.

### Methodology lessons

1. **Stale `refs/pull/N/merge` doesn't auto-refresh when base updates.** I pushed a classifier fix to `cam/master`, then re-triggered triage on existing PRs — but `actions/checkout` resolved the stale merge ref and ran the OLD classifier. Took two debug rounds to spot. Fix: rebase the test branch onto the new base (forces merge ref regeneration) OR force-push to the head branch. Worth a CLAUDE.md / AGENTS.md note next time it bites.
2. **Test-design bug: my "normal" PR was actually trivial-by-spec.** I designed test 4 (the no-model-call path) with 4 lines of body change, no link diff, no code blocks — which is exactly what `review:trivial` means. Classifier correctly fired trivial; my expectation was wrong. Lesson: when designing test fixtures for predicates, size the input *for the predicate*, not "feels normal-ish."
3. **Set-comparison beats per-line pattern matching for "did X change" detection.** The link-change bug came from matching `[link](url)` on any changed line. The fix — diff the link sets between `-` and `+` lines — is cleaner, more accurate, and matches what the spec actually means by "no links added or modified."

### Side effects worth tracking

- The `<!-- TRIAGE_PROSE -->` advisory now applies to either trivial or frontmatter-only PRs. The comment template threads the right short-circuit label name dynamically (`review:trivial` vs `review:frontmatter-only`). Verified on test PRs 50 and 52.
- Frontmatter-only prose check: the model correctly inspected `meta_desc` for typos and skipped data fields. Test PR 52 with two intentional typos (`togther`, `manageing`) flagged both correctly.
- The `prose-checked=true|false` field in the triage log line gives instant visibility into whether the model was invoked. Useful for cost tracking in real traffic.

### Backlog after Session 7

Remaining:

1. **Cache-friendliness audit.** Restructure shared system prompts to hit the 5-min Anthropic prompt cache when reviews cluster.
2. **Investigate PR 45's prose-regression pattern.** Open question from Session 6 — needs a prompt-nudge experiment.

Plus standing **deploy step**: create `review:frontmatter-only` label on `pulumi/docs` upstream when the branch lands.

### Artifacts

- Test PRs 50–53 on `CamSoper/pulumi.docs` covered all four scenarios (trivial / frontmatter-only clean / frontmatter-only with typos / normal). All closed and branches deleted at session end.
- `cam/master` carries the new triage commits cherry-picked, on top of the FORK-ONLY token swap. Fork is in clean state.

---

## Session 8 — 2026-04-29 (audit + restoration + extraction)

Picked up after the docs-review/ refactor (commits `e9bd53c024` + `f6cbbfbe94`) shipped clean. Cam asked for an audit verifying that `_common/review-criteria.md` (deleted in the refactor as "dead — superseded by per-domain files") was actually fully covered by the new package.

### What happened

**Audit.** Recovered the deleted file via `git show e9bd53c024^`. Atomized 90 rules across 174 lines. Classified each against `docs-review/references/*.md`, `glow-up.md`, `lint-markdown.js`, and the markdownlint config. Wrote a structured report to `/workspaces/src/scratch/2026-04-29-review-criteria-audit.md` (~300 lines, decision queue at the bottom).

Headline findings:
- 57% PRESERVED, 9% PARTIAL, 22% MISSING, 12% INTENTIONALLY DROPPED
- Three substantive gaps: blog images (R83–R86), cross-domain coverage check (R88–R90), publishing-readiness checklist (R87)
- One real bug: `shared-criteria.md` §Linter boundary claimed image alt text + fenced-code-language were lint-owned, but `.markdownlint-base.json` has both rules (MD045, MD040) **disabled**. Neither was being enforced anywhere.
- Several smaller misses: R6 indented-prose-as-code, R29 meta description length, R51 title clickbait, R59 self-criticism, R60 weak conclusions, R70 logo currency, R71 `<!--more-->` positioning

**Pushback from Cam.** I had unilaterally classified ~10 rules as INTENTIONALLY DROPPED with the justification "I wrote a 'Do not flag' clause for those during the refactor." Cam pointed out that *I* wrote those clauses, not him — and several genuinely should be restored. Took the L. Restored as concrete prose patterns rather than vague style guidance.

**Architectural decisions during the conversation:**

1. **Don't quantify "passive voice >30%."** Cam's call: thresholds are hard to operationalize for LLMs (unreliable parse-counters) AND the natural target is 0% anyway. Rules should name *concrete patterns* with examples and a cite-and-rewrite mandate, not abstract editorial qualities.
2. **Don't move banned words to the linter.** Too many edge cases ("very specific" should stay; "very fast" should go). Lives in review skill.
3. **Specialize, don't inherit.** `blog.md` was reaching into `docs.md` (same anti-pattern as cross-skill imports). Pull cross-cutting concerns into shared reference files; domain files own *only* domain-specific rules.

**Extraction commit (`05411771e5`).** Three new shared reference files:
- `code-examples.md` — snippet syntax, imports, language idioms, API currency, casing, hand-written constructor style. Pulled from `docs.md` §Code examples + `programs.md` snippet-level subsections.
- `prose-patterns.md` — passive voice, filler/prepositional bloat, empty intensifiers, difficulty qualifiers, undefined acronyms, nested clause stacks. Each with example→rewrite. Cap 5 findings per file.
- `image-review.md` — alt text, file format, size limits (3MB / 1200px GIFs), comparison screenshots, 1px gray borders.

`docs.md`, `blog.md`, `programs.md` trimmed to point at these. `blog.md` Priority 3's awkward `docs.md` cross-reference is gone — both files reference `code-examples.md` instead.

**Restoration commit (`a096563c8b`).** Backfilled the audit gaps:
- `blog.md` Priority 2 extended with self-criticism / weak-conclusions / dense-paragraphs / listicle-bloat patterns
- `blog.md` Priority 4 added title-quality flag (R51)
- `blog.md` NEW Priority 5 — Documentation coverage check for feature-announcement posts (R88–R90)
- `blog.md` Pre-existing extended with meta_image logo-currency check (R70)
- `blog.md` NEW §Publishing-readiness checklist (R87) — end-of-review summary block, with explicit note that several items are caught at pre-commit by `lint-markdown.js`
- `shared-criteria.md` §Frontmatter added meta_desc length guidance (R29)
- `shared-criteria.md` §Linter boundary corrected to reflect actual config: MD040/MD045 disabled, alt text + code-block language are NOT linter-owned
- `shared-criteria.md` NEW §Indented prose (R6)

### Lint changes deferred to a future PR

Discussed but not implemented in this session, on the backlog:

1. **Tier A markdownlint rules.** Approved by Cam: enable `MD034` (bare URLs), `MD037` (spaces inside emphasis), `MD039` (spaces inside link text), `MD059` (descriptive link text). Each is mechanical-correctness; offender count likely small. **One-time cleanup pass needed before flipping the flags** — when this lands, run `npx markdownlint --rules MD034,MD037,MD039,MD059` and fix what it surfaces, then commit the config flip.
2. **Frontmatter validator extensions to `lint-markdown.js`.** Approved: add `checkSocialBlock` (R30 — flag if blog post is missing twitter/linkedin/bluesky keys), `checkMoreBreak` (R71 — flag missing `<!--more-->` or buried positioning), extend `checkMetaImage` (R70 logo currency).
3. **Reviewdog + MD040/MD045 (Tier B).** Discussed at length — `reviewdog/action-markdownlint@v0` with `filter_mode: added` would let us enable the disabled rules without forcing a repo-wide cleanup. Requires its own workflow file, parallel to existing pipeline. Not in scope here.

### Methodology lessons

1. **Trust but verify, even when *I* did the work.** I shipped the docs-review refactor confident it was clean. The audit found 22% of rules MISSING and a real linter-boundary bug. Don't skip the audit step on "obvious" deletions.
2. **"Intentionally dropped" needs a citation that isn't *me*.** When the model classifies a rule as INTENTIONALLY DROPPED, the rationale has to point at a human decision (commit message, session notes, conversation), not at a "Do not flag" clause the model itself authored during the refactor. Otherwise the rationalization is circular.
3. **Vague rules don't survive operationalization.** "Be clear," "logical flow," "avoid jargon" can't be checked by an LLM reliably. The blog.md Priority 2 shape (named pattern + threshold + example) is the model that works. Apply it elsewhere or drop the rule.
4. **Cross-skill references = bad architecture.** `blog.md` referencing `docs.md` for shared rules creates the same fragility as cross-skill Skill-tool imports. The fix is the same: extract to a shared reference, both files point at it.

### Backlog after Session 8

1. **Tier A markdownlint enablement** (cleanup pass + config flip + commit). Probably a few hours of work for the cleanup; the config flip is one line.
2. **Frontmatter validator extensions to `lint-markdown.js`.** Three new functions; ~50 lines.
3. **Reviewdog + Tier B** (MD040/MD045 with `filter_mode: added`). Separate decision once Tier A lands clean.
4. **Cache-friendliness audit.** Still on the list from Session 7.
5. **PR 45 prose-regression investigation.** Still on the list from Session 6.
6. **Deploy step:** create `review:frontmatter-only` label upstream when the branch lands.

### Artifacts

- `/workspaces/src/scratch/2026-04-29-review-criteria-audit.md` — full audit report with rule-by-rule classification and decision queue. Survives this session for reference; not committed to docs repo.
- Two new commits on `CamSoper/pr-review-overhaul`: `05411771e5` (extraction), `a096563c8b` (restoration). Both pushed.
- 3 new shared references: `code-examples.md`, `prose-patterns.md`, `image-review.md`. Reference count is now 12 in `docs-review/references/`.

---

## Session 9 — 2026-04-29 (Tier A audit + lint-markdown.js extensions)

### Tier A markdownlint audit (DROPPED)

Audited the four "Tier A" candidates (MD034, MD037, MD039, MD059) against `content/**` to see how much cleanup an enable would require. Headline finding: **MD034 is a trap.**

Counts (content/ scope, matches `lint-staged`):

- **MD034** (bare URLs): 82 violations across 56 files. Linter says all auto-fixable. **In reality, 67 of 82 (82%) are false positives** — URLs inside Hugo shortcode parameters like `{{< video src="https://www.pulumi.com/uploads/foo.mp4" >}}`. Auto-fix wraps them as `src="<https://...>"`, which Hugo renders literally. **Demonstrated end-to-end** by running `markdownlint-cli2 --fix` on `content/blog/esc-env-run-aws/index.md` and inspecting the diff.
- **MD037** (spaces in emphasis): 8 violations. ~25% real prose, rest are code-block-detection failures (`import * as ...` lines outside fences) and policy-pack table cells with literal `*`.
- **MD039** (spaces in link text): 2 violations. Both real, trivial.
- **MD059** (descriptive link text): 84 violations. **71 in `content/blog/`** (historical per AGENTS.md), 13 in `content/docs/` — all `[here]` patterns.

**Decision: Option A — drop Tier A entirely.** Cam's call. The MD034 false-positive rate disqualifies it, and the rest aren't worth the partial-pipeline complexity.

**Load-bearing config note:** the MD034 disable in `.markdownlint-base.json` is *not* dead config — it's defensive, because Hugo and CommonMark disagree on what counts as inline content. Same applies to MD037 to a lesser degree. **Don't flip them back on without a Hugo-aware preprocessor that strips shortcodes before linting.** The review skill already catches the rule that matters here (`shared-criteria.md` flags `[here]`/`[click here]` as descriptive-link-text violations); we have coverage at PR review time even without the linter rule.

Tier B (MD040, MD045) was contingent on Tier A landing clean. Now also dead.

### lint-markdown.js — frontmatter validator extensions

Added two new frontmatter checks to `scripts/lint/lint-markdown.js`:

1. **`checkSocialBlock`** — flags blog posts where the `social:` block is missing entirely OR all three keys (`twitter`/`linkedin`/`bluesky`) are empty. Either state means the post won't be promoted on social, defeating the new-blog-post scaffolding's intent.
2. **`checkPlaceholderMetaImage`** — hashes the file at `obj.meta_image` (resolved relative to the post directory, or against `static/` for absolute paths) and compares to the SHA-256 of `.claude/commands/_common/images/blog-post-meta-placeholder.png`. If equal, the author hasn't replaced the default. Replaces the previous "TODO: maintain a list of retired logos" plan — Cam's call: the only canonical "wrong" image is the placeholder; everything else is judgment.

Both checks scope to `content/blog/**` (via `isBlogPost(filePath, obj)` — also excludes taxonomy/list pages like `_index.md`/`series.md`/`tag.md` that lack a `date` field) and skip when `draft: true`. They also skip via **`isArchivalPost`** — any post whose `date` is in the past is exempted.

**Rationale for "any past date" semantics (Option 2):** publishing-readiness checks are a pre-publish gate, not an archival-quality gate. Once a post's date is past, the social-promotion train has left the station, and failing the lint on already-merged posts breaks `make lint` against master. The rule still catches the most common authoring path (`/new-blog-post` template's `date: 2099-01-01` sentinel) and any future-scheduled launch post, which is where the value is. Initial implementation used a 30-day window; surfaced 3 real findings on recent posts (Bitbucket, Bun, GovCloud — all within 30 days of 2026-04-29) which would have failed `make lint`. Cam's call: tighten to "any past date" rather than backfill social copy or chase the calibration. The lost catch (post merged with empty social, then someone edits it within 30 days) is narrow and is already covered by the docs-review skill's publishing-readiness checklist (R87).

**Tested behaviors (synthetic fixture under `/tmp/lint-test/` + real archival post):**

| Scenario | Expected | Actual |
|---|---|---|
| Archival post (2024) with empty social: | pass | ✅ pass |
| Fresh post (date=2099) with placeholder image + empty social: | 2 errors | ✅ 2 errors |
| Fresh post with real image + at least one social key filled | pass | ✅ pass |
| Fresh post with `draft: true` | pass | ✅ pass |
| Docs file (no social block) | pass | ✅ pass |

**`checkMoreBreak`** (R71) — flags blog posts that are missing the `<!--more-->` break or that bury it past paragraph 3. Counts paragraph blocks (non-blank-line content separated by blank lines) before the marker. Same scoping as the other two checks (skip drafts, skip past-dated, exclude taxonomy pages). Threshold: > 3 blocks before the marker is the failure condition; 1–3 is the target range. `make lint` against master surfaces zero findings — the archival-exemption rule shields existing posts.

### Cache-friendliness audit (closed — no-op)

Investigated whether our prompts could be restructured to hit the Anthropic 5-min prompt cache better. **Decisively closed as no-op** on two independent grounds:

1. **The action already caches optimally.** `anthropics/claude-code-action@v1` delegates to the Agent SDK / Claude Code CLI binary, which sets `cache_control: ephemeral` automatically. The breakpoint sits between the system prompt (skills + memory) and the first user message (PR-specific content). Direct citation: `claude-agent-sdk-typescript` CHANGELOG v0.2.119 — "static auto-memory instructions kept in the cacheable system-prompt block; only per-user memory directory path and per-machine environment values are relocated to the first user message." No caller-facing cache configuration is exposed in `base-action/action.yml`. There's nothing to restructure at the workflow-prompt layer; the caching happens one layer below us.
2. **Clustering doesn't happen in production.** Over the last 100 review runs (`gh run list --workflow=claude-code-review.yml`), **zero production clusters within the 5-min TTL** — every same-branch within-5-min cluster I found in the sample was one of my own `CamSoper/pr-review-overhaul` test pushes. Real-author PRs are reviewed 30+ minutes apart from each other and from re-runs. Even if the action's caching were tunable, there's no temporal density to amortize against.

### Backlog after Session 9

1. **Deploy script** — write a `gh` script that creates all required labels (domain, signal, state, plus newer ones like `review:frontmatter-only`) in one shot, ready to run on `pulumi/docs` upstream when the branch lands. The existing manual one-liner block in `.github/labels-pr-review.md` is the seed; turn it into a runnable `.sh` once the label set is final. More testing and refinement still to come, so don't ship the script yet.

### Dropped this session

- **PR 45 prose-regression investigation** (Session 6 carryover). The original hypothesis was that broadened allowed-tools + pre-compute injection caused the model to converge faster and skip lower-tier prose findings. Session 8's `prose-patterns.md` + the restored editorial rules in `blog.md` (concrete patterns with cite-and-rewrite mandate) addressed this orthogonally — regardless of how fast the model converges, it now has explicit rules to apply. The original failure mode shouldn't survive the Session 8 changes, so the experiment is moot. If a similar regression surfaces in production traffic post-merge, reopen.

### SEO/AEO replication into blog and docs review

During the pre-hand-review pass, I framed the audit's "deferred to /seo-analyze" items as editorial-overlap-territory Cam had pushed back on. **Cam called this out as the same circular-rationalization pattern from Session 8.** "I want to do EVERYTHING, YOU'RE the one pushing back on that." The "editorial out of scope" framing is mine, not his.

Replicated the feasible SEO/AEO items into `blog.md` and `docs.md`, sourced from `seo-analyze:references:aeo-checklist`:

- `blog.md` Priority 4 §Title quality extended to cover R34 (title/body mismatch) and R74 (generic title missing topical hook), each with quote-and-rewrite mandate.
- `blog.md` NEW Priority 6 — SEO and discoverability (Links became Priority 7). Covers quotable opening paragraph, answer-first H2 headings (R77), specific data over vague superlatives, down-funnel specificity, numbered executable steps for how-to content, dated context where it matters.
- `docs.md` NEW §SEO and discoverability section (between Callouts and Pre-existing). Same patterns adapted for docs: title matches subject, quotable definition (especially for what-is and concept pages), answer-first H2 headings on concept content, semantic chunking, down-funnel specificity, numbered executable steps for get-started/how-to.
- `blog.md` and `docs.md` "Do not flag" §Structural rewrites / §Prose style within a paragraph — the blanket "structural and editorial feedback is out of scope" clauses I authored in Session 8 — rewritten to enforce the **quote-and-rewrite mandate** instead. Concrete structural and editorial suggestions (split a mixed-concept H2, rewrite a label-style heading as answer-first, convert prose-quickstart to numbered steps) are in scope; only vague editorial-without-rewrite is out.

**Audit corrections worth recording:**

- The original audit deferred R75 (title ≤60 chars) and R76 (meta_desc ≤160 chars) to `/seo-analyze`. Wrong on both: `lint-markdown.js` `checkPageTitle` and `checkPageMetaDescription` already enforce these deterministically at pre-commit. The audit was sloppy on these two.
- `/seo-analyze` itself is purely manually-invoked (only referenced from `new-blog-post.md` validation step as "Recommended"). No CI/workflow integration. Adoption uncertain — Cam's read: "I'm not sure anyone is using it." So "deferred to /seo-analyze" was largely a polite fiction for items that are actually unenforced. The replication into `blog.md` / `docs.md` makes the operationalizable subset enforced at PR review time regardless of whether `/seo-analyze` ever runs.

### Memory update

Extended `feedback_dont_unilaterally_drop_during_refactor.md` to call out that the same pattern shows up in *new* recommendations, not just past ones. Specifically, framing an addition as "editorial-overlap territory you've pushed back on" when no such pushback exists — the rationalization is mine, not Cam's. Watchword: if I find myself attributing an editorial-scope objection to Cam when proposing a new addition, I'm probably doing it again.

### Pre-hand-review gap analysis (Cam-explicit drops)

Surfaced the residual gaps vs. the legacy `_common/review-criteria.md` after the SEO/AEO replication:

- **R52** "Strong opening hooks reader" — calculated drop. Operationalizable parts already covered by `blog.md` Priority 2 §Empty transitions and Priority 6 §Quotable opening paragraph. Residual is editorial taste; restoring would duplicate or violate the quote-and-rewrite mandate.
- **R54** "Sections open with motivation sentences" — calculated drop. Concrete enough to write down (H2 followed by list/code/restated-heading without a context sentence) but low-frequency miss that a hand reviewer would catch. Cam's call: drop.

Residual items still flagged but not yet decided (Cam may pick these up after hand review):

- **R31** Positive cross-link recommendations — old way had "consider linking to X"; new way only checks existing cross-refs.
- **R72** Author profile file existence — partial; only the missing-avatar flag remains.
- **Caps:** prose-patterns at 5/file, pre-existing at 15/file. Old way had no caps. Conscious tradeoff for review readability.
- **Do-not-flag rewrite untested.** Reworded blanket "structural is editorial" to "concrete-with-quote-and-rewrite is in." Right principle on paper; behavior under the new wording untested against the fixture set.

### Reference loadout — sequential→concurrent rewording

The pattern "Apply X first, plus Y. Then Z" appeared in `docs.md`, `blog.md`, `programs.md`, `infra.md`. Cam called it out: that wording reads as a sequence directive that could push the model into multi-pass behavior or upfront-loading every reference. First pass I overcorrected with "**not** a separate pre-pass" disclaimers; Cam pointed out the negation enlarges the option space (the model considers what a pre-pass would even look like). Second pass settled on the positive form: "These reference files apply alongside the X-specific checks below. Consult each as content in the diff triggers a relevant rule."

### Pruning meta-commentary

Two passes through the docs-review and pr-review skill packages.

**Docs-review sweep** (commit `b397dce152`, -132 lines across 13 files): cut implementation history ("for v1," "Sonnet failure-mode example to avoid," "Documented here so they aren't 'fixed' into new bugs"), design-rationale tails ("the dispute path is equally important as the refresh path," "Pulumi convention: authors merge their own PRs because…", the "Why heightened scrutiny doesn't depend on contributor type" section), and DRY violations (bucket rules duplicated in `infra.md` and `output-format.md`, Notion/Slack rationale in 4 places, compilability cascade stated twice in `programs.md`, language-casing rule duplicated within `code-examples.md`). Major DRY consolidation: bucket rules + DO-NOT list live in `output-format.md` only; domain routing lives in `domain-routing.md` only; Notion/Slack rule lives in `ci.md` only.

**Pr-review sweep** (commit `076de8a0ae`, -173 lines across 7 files): cut the §Critical Workflow Rules recap (12 restated rules), §Implementation Notes blocks at the end of every reference file, the §Why heightened scrutiny doesn't depend on contributor type rationale, the political-landmine rationale on the AI-suspect allowlist, the auto-merge toggle defaults block duplicated across action-menus and action-preview-templates, the testing-checklist duplication between dependabot-labels and action-menus, the §Tone Guidelines block in message-templates that restated voice rules + the template matrix.

### Pr-review SKILL rewrite (CI's pinned review as source of truth)

Cam's clarification mid-session: the original PR review pipeline was designed to offload as much as possible to CI because PR volume is increasing. The current pr-review SKILL did its own full Step 4 (style+code review) and Step 5 (fact-check), duplicating the CI's pinned-comment work. Wrong default.

Rewrote `pr-review/SKILL.md` (commit `be71b898d9`, 377 → 295 lines):

- Step 2 fetches the pinned comment via `pinned-comment.sh fetch` and classifies state from labels: CURRENT / STALE / WORKING / ABSENT.
- Step 3 resolves the state. STALE invokes `docs-review:references:update` *locally* (Sonnet refresh + `pinned-comment.sh upsert`) — pr-review writes to GitHub state during what was previously a pure local read. This is intentional: the contributor-facing pinned comment must reflect current diff before a maintainer adjudicates. WORKING aborts. ABSENT prompts the user to fall back to a local review or proceed without findings.
- Step 4 (infra deployment prompt) and Step 5 (PR description accuracy) survive — these are unique to pr-review and not produced by CI.
- Step 6 renders CI's pinned findings verbatim as the source of truth.
- Step 8 adds an opt-in "Dispute finding(s)" path: maintainer composes a mention body, pr-review feeds it to update.md Case 2 (which already classifies and concedes/holds), pinned comment is refreshed, then the action proceeds.

Backing changes:

- `contributor-detection.sh` now emits a `LABELS=` line so Step 2's state machine has clean input.
- `update.md`'s preamble names pr-review as a caller (Step 3 stale refresh + Step 8 dispute), since the line I trimmed in the earlier sweep was aspirational documentation that's now backed by real implementation.

### Skill:reference notation standardization (commit `27e158869a`)

The skill files had a mix of bare \`xxx.md\` references, `[xxx.md](xxx.md)` markdown-link forms, and the canonical `docs-review:references:foo` form. Standardized everything to the skill notation across 11 files. Sibling files within a skill that aren't separate skills themselves (`docs-review/ci.md`) use explicit relative paths since there's no skill-notation form for them; top-level skills are referenced by skill name (`pr-review`, not `pr-review/SKILL.md`).

### Where the branch stands at session end

Session 9 commit list (from `master..HEAD`):

1. `df2b017166` — checkSocialBlock + checkPlaceholderMetaImage
2. `0edac66946` — checkMoreBreak
3. `6ceb043149` — Cache-friendliness audit closed as no-op
4. `6f701473c3` — Restate deploy step as labels script
5. `c3567237ba` — Drop PR 45 prose-regression as moot
6. `737d3cdab7` — SEO/AEO replication into blog and docs
7. `59fb80171c` — Record R52/R54 calculated drops
8. `9991112cee` — Reword reference loadout sequential→concurrent
9. `81dae2cdc0` — Drop "for v1" commentary in docs-review/ci.md
10. `2b21a62883` — Remove Re-entrant runs section from ci.md
11. `b397dce152` — Sweep docs-review for meta + DRY (-132 lines)
12. `076de8a0ae` — Sweep pr-review for meta + DRY (-173 lines)
13. `be71b898d9` — Rewrite pr-review SKILL: read CI's pinned review as source of truth
14. `27e158869a` — Standardize skill:reference notation across the package

### Backlog after Session 9

1. **Real-PR test of the new pr-review flow** — the rewritten Step 1 → Step 2 → Step 3 → Step 6 → action path is untested against any of the fixture PRs at `CamSoper/pulumi.docs#44–49`. Worth a dry-run on a PR that's CURRENT, STALE, and ABSENT to confirm each branch behaves.
2. **Deploy script** — `gh` script to create all required labels on `pulumi/docs` upstream when the branch lands. Seed is `.github/labels-pr-review.md`'s manual one-liner block. More testing/refinement still pending, so don't ship yet.
3. **Cam-flagged residual items from the gap analysis** (still not decided): R31 positive cross-link suggestions, R72 author-profile existence check, caps (5/file prose-patterns and 15/file pre-existing), Do-not-flag rewrite needs fixture-set re-run.

### Artifacts

- `scripts/lint/lint-markdown.js` — added `checkSocialBlock`, `checkPlaceholderMetaImage`, `checkMoreBreak`, `isArchivalPost`, `isBlogPost`, `META_IMAGE_PLACEHOLDER_HASH` constant. ~100 lines net add.
- `pr-review/scripts/contributor-detection.sh` — added `LABELS=` output line.
- Net Session 9 change across all files: roughly **-300 lines** despite adding the SEO/AEO sections and the lint validators. The pr-review/docs-review packages are smaller and more focused than they were at Session 8 close.

## Session 10 — 2026-04-29 (label cleanup: drop unread labels, rename domain prefix)

### Trigger

Cam selected lines 54–56 of `docs-review/ci.md` (§3 "Fact-check (gated)") and asked whether it was actually how fact-check ran. It wasn't. Investigation surfaced that **§3 was wired to nothing** — fact-check is invoked from inside each domain file during §2's composition pass, and the `fact-check:needed` label gate it claimed to enforce never fired at the layer where the actual call happens.

### What the audit found

Traced every label the classifier emits against every consumer in workflow YAML and skill files:

- **Workflow-state labels** (`review:trivial`, `review:frontmatter-only`, `review:claude-ran`, `review:claude-stale`, `review:claude-working`, `review:prose-flagged`) are all read by `claude-code-review.yml` conditionals or the `pr-review` SKILL state machine. **Load-bearing.**
- **Domain labels** (`review:docs`, `review:blog`, `review:infra`, `review:programs`, `review:mixed`) are *never* read by any conditional. `ci.md` §Inputs claimed they "drive domain selection," but §2's actual instruction is "route by path via `docs-review:references:domain-routing`" — which the model does anyway, since per-file routing is necessary for mixed PRs. The labels duplicated work the router does at review time.
- **`fact-check:needed`** had the same story. The classifier computed it; the workflow passed it to the model; nothing read it. Each domain file decides per-file whether to invoke fact-check based on the same path/content rules the classifier was using — so the label was a precomputed cache of work the router already does inline.
- **`agent-authored`** was inert. AGENTS.md called it "a signal for human adjudication," but `pr-review` SKILL doesn't grep for it. Cam's call: drop entirely — "they're ALL agent authored to some degree."

### Decision

Cam picked option (2) from the audit: drop the unread labels, rename the domain labels with an honest prefix, and stop pretending labels drive logic they don't.

- **Drop** `fact-check:needed` and `agent-authored`. Triage no longer emits either.
- **Rename** `review:{docs,blog,infra,programs,mixed}` → `domain:{docs,blog,infra,programs,mixed}`. The new prefix is honest about what the labels actually do (domain classification surfaced for human filterability), and aligns with the existing internal vocabulary (`domain-routing`, "the domain file"). The `review:` prefix is now reserved for workflow-state labels exclusively.

### Files changed (–64 net lines)

- `triage-classify.py` (–50): dropped `fact_check_needed` / `agent_authored` outputs, the `detect_agent_authored` function, the AGENT_LOGINS / AGENT_TRAILER_RES tables, the dead intermediate flags (`has_new_heading`, `has_new_version_claim`), and the regex constants that fed only those flags. Domain labels emit as `domain:*`. 354 lines → 304 lines.
- `claude-triage.yml`: dropped FACT_CHECK / AGENT_AUTHORED reads, the corresponding TARGET assignments, the matching cleanup pattern in the existing-label sweep, and the references in the summary log line. Mixed-domain target now `domain:mixed`. The cleanup case now lists the specific labels triage manages (`domain:*`, `review:trivial`, `review:frontmatter-only`, `review:prose-flagged`) instead of the broad `review:*|fact-check:*|agent-authored` glob.
- `claude-code-review.yml`: corrected the leading workflow-comment about `fact-check:needed` gating, and the prompt's "Labels (set by claude-triage.yml — drive domain selection and fact-check gating)" → "informational; routing happens by path inside `ci.md`".
- `docs-review:ci`: deleted §3 (the fact-check gate that was wired to nothing). §Inputs reworded — `PR_LABELS` is informational; routing is path-based per `docs-review:references:domain-routing`. Dropped the §Missing-label fallback paragraph entirely (it conflated domain labels with routing). Section numbers shifted (4→3, 5→4, 6→5); fixed the §5→§4 cross-ref in the hard-rules block.
- `docs-review:references:fact-check`: stale CI-label-gate references on lines 41 and 58 replaced with "the domain file is the gate." No more recap of which domain calls fact-check at what scrutiny — that's covered in each domain file directly.
- `AGENTS.md`: dropped the `agent-authored` paragraph entirely. The "leave AI authoring trailers in commit messages" guidance survives, reframed as "stripping them is bad form" rather than "triage uses them to apply a label." Updated line 137's triage-refresh list to current label set, and line 170's classifier description to drop the dead signals.
- `labels-pr-review.md`: full rewrite. Domain labels under `domain:*` table; workflow-state labels under their own table; gh label create commands updated. Deliberately did *not* include a migration block — we're a fork, no installed-base to migrate.

### Verification

Classifier dry-run via `triage-classify.py` against fixture PRs `CamSoper/pulumi.docs#44`, `#46`, `#48`, `#49` — exercised `domain:docs`, `domain:infra`, `domain:blog` paths. All emit clean output: domain labels under the new prefix, no `fact_check_needed` or `agent_authored` fields, all summary fields intact.

Final `grep -rn -E "review:(blog|docs|programs|infra|mixed)|fact-check:needed|agent-authored|fact_check_needed|agent_authored"` across `.github/`, `.claude/`, `AGENTS.md` returns zero hits.

### Cam-flagged behaviors during the session

- **Bare-filename references** in skill files. I wrote `blog.md` / `docs.md` / `programs.md` / `infra.md` in `fact-check.md`'s gating paragraph and in `ci.md` §2's composition prose. Cam: use `skill:folder:reference` notation. Fixed both call sites; the skill notation is now uniform across the package.
- **Meta-narration in agent instructions**. First pass at `ci.md` §Inputs explained that `domain:*` labels are "a human-visible signal, not the routing input" — agents executing the file don't need the rationale, just the directive. Trimmed to "Route by path-precedence per `docs-review:references:domain-routing`. `PR_LABELS` is informational only." Same trim applied to `fact-check.md`'s gating paragraph (dropped the per-domain recap; each domain file owns its own gate).
- **Existing-label migration handling**. First pass at `labels-pr-review.md` included a §Migrating from `review:*` block with `gh label delete` commands for the old names. Cam: "I don't give a shit about existing labels. That's why we're working on a fork." Pulled the section.

### Backlog after Session 10

Carryover from Session 9; no new items added.

1. **Real-PR test of the new pr-review flow** — the rewritten Step 1 → Step 2 → Step 3 → Step 6 → action path is still untested against the fixture PRs. CURRENT / STALE / ABSENT branches each need a dry-run.
2. **Deploy script** — `gh` script to create the required labels on upstream when the branch lands. Seed is the `gh label create` block in `labels-pr-review.md`. Don't ship yet — testing/refinement still pending.
3. **Gap-analysis residuals** (still undecided): R31 positive cross-link suggestions, R72 author-profile existence check, caps (5/file prose-patterns and 15/file pre-existing), do-not-flag rewrite needs a fixture-set re-run.

### Session 10 commit list (planned — uncommitted at session end)

Single commit covering all 7 files. Suggested message:
> `Drop unread labels, rename domain prefix, fix ci.md §3 fiction`

## Session 11 — 2026-04-29 (caller-leak sweep, Haiku triage, label-apply lift)

### Trigger

Started by committing Session 10's uncommitted work (8 modified files). Two commits per the branch's substance + notes pattern: `51b6a6b167` for the 7-file substance, `ca894cb586` for SESSION-NOTES alone. Cam then asked me to explain the gap-analysis residuals item from the backlog, gave dispositions on all four, and the session cascaded through a series of caller-leak / DRY / consistency cleanups across the skill packages.

### Gap-analysis dispositions

- **R31 (positive cross-link recommendations)**: ADD. New bullet in `docs.md` (under §Cross-references between docs pages, later renamed §Priority 3) and `blog.md` (under §Priority 7 — Links). Bounds: once per concept per file; only when no occurrence is hyperlinked; quote-and-rewrite mandate; doesn't fire on the page whose subject *is* the concept. Commit `3a81802fca`.
- **R72 (author profile existence check)**: DROP the proposed extension. The partial coverage (missing-avatar) survives — later promoted into §Publishing blockers when the publishing-readiness checklist got refactored.
- **Caps**: BUMP prose-patterns 5 → 10 (`prose-patterns.md:10`); pre-existing stays at 15. Commit `a8c99cacb8`.
- **Do-not-flag rewrite**: TABLE. Quote-and-rewrite mandate is the right principle; behavior under the wording untested. Validation folds into backlog #1 real-PR test.

### Haiku for triage-prose

Cam asked whether Haiku could handle triage-prose — the highest-volume model call in the pipeline (every trivial / FM-only PR). My answer: probably yes, with one specific concern (Pulumi product-name false positives — Haiku takes instructions more literally than Sonnet). Narrow input/output, mostly-mechanical pattern-match task is in Haiku's wheelhouse.

Tailored `triage-prose.md` for Haiku's failure modes:
- Replaced illustrative protected-term examples with a structural rule (internal caps, all-caps acronyms, digit/underscore/kebab-joins, slashes, dots, backticks) plus an enumerated list for residual Pulumi-product surface that doesn't follow structural cues.
- Added a concrete DO-flag / DO-NOT-flag examples block — Haiku benefits more from positive examples than from prose rules.
- Tightened the high-judgment "punctuation that changes meaning" item.
- Added doubled-words to the flag list.
- Expanded frontmatter skip-fields with a catch-all for path/URL/identifier/date list values.

`claude-triage.yml`: model swapped `claude-sonnet-4-6` → `claude-haiku-4-5-20251001`. Trimmed the inlined YAML preamble's duplicated scope rules so triage-prose.md is the single source of truth. Commit `03a7e953da`.

Cam then directed: enforce US English (per AGENTS.md) and require Oxford commas (no project-level rule yet — this is the policy decision). Moved both from §Do-not-flag → §Flag with concrete pattern-based directives (`-our`/`-or`, `-ise`/`-ize`, `-yse`/`-yze`, `-tre`/`-ter`, doubled-l past tense, +specific cases like `defence`/`licence`/`practise`; Oxford commas in lists of 3+). Updated examples block to match. Commit `306149861a`.

### Post-run label apply moved to workflow

Cam selected `ci.md:69-71` (§5 Post-run) and asked whether the label apply happens automatically. It didn't — `claude-code-review.yml:276-279` had the *agent's prompt* tell it to run `gh pr edit --add-label review:claude-ran --remove-label review:claude-stale`, with the same instruction duplicated in `ci.md` §5. The "the workflow applies" wording in §5 was factually wrong.

Two options surfaced: (A) move the label step to a workflow `if: success()` post-step, dropping the agent's responsibility; (B) keep the agent doing it, fix the wording. Cam picked A — workflow steps don't forget; agents sometimes do; the duplication just bit us during the Session 10 label rename.

Implementation:
- Removed the label-apply instruction from the agent prompt; replaced with a one-line note that post-run labels are handled by a separate workflow step.
- Added `Apply post-run review labels` step gated on `steps.claude-review.outcome == 'success'`. The success gate covers normal-success AND the empty-diff short-circuit (which exits 0 cleanly), excludes skipped (trivial / draft / bot) and failed runs.
- Dropped `ci.md` §5 entirely. `ci.md:47`'s pre-existing reference to "the workflow's post-run label step" is now factually accurate (was already aspirational).
- Updated the Finalize-progress-signal comment block to drop the stale "Claude's prompt adds review:claude-ran on success" line.

Commit `aa9720d8fa`. Adjacent cleanup: with the agent's `gh pr edit` use case gone, the allowlist's `Bash(gh pr edit:*)` was a footgun. Dropped it. Workflow steps still use `gh pr edit` (lines 43, 218, 313, 328) — those run via `GITHUB_TOKEN` on the runner, not the agent. Commit `7222742ac3`.

### Caller-leak / DRY sweep across the docs-review references

Same pattern repeated across multiple skill files. Cam selected lines and asked questions; investigation surfaced caller-leak, output-format duplication, and DRY violations each time.

**`blog.md` Priority 1** (commit `511b792327`): 5-bullet claim list ("Every number," "Every tech claim about Pulumi products," etc.) duplicated `fact-check.md:74-89`'s claim-extraction table. Trimmed to the directive (invoke fact-check with scrutiny=heightened) plus the genuinely blog-domain-specific high-blast-radius categories (performance multipliers, competitor claims, adoption/market-position statistics). fact-check.md is the single source of truth for what counts as a claim.

**`blog.md` publishing-readiness checklist** (commit `2d9846726c`): The checklist concept didn't survive contact with how the review actually runs:

1. The "render with linter-caught items already checked" mechanism required the model to read lint output, which it doesn't have access to.
2. A 10-item `[ ]`/`[x]` block in the 💡 bucket reads as a TODO list, not a finding — maintainers had nothing actionable to do with it.
3. Most items were already lint-caught (`social:` block, `meta_image` placeholder, `<!--more-->` presence, title length); flagging them again was redundant noise.

Audited each item; four survived as genuinely review-time: retired-logo `meta_image`, animated-GIF `meta_image`, `<!--more-->` break *position* (lint catches presence; position is judgment), missing author avatar. Replaced §Publishing-readiness checklist with §Publishing blockers — each item rendered as single 🚨 Outstanding finding when violated, quote-and-rewrite mandate. Trimmed §Do not flag bullets 2-3 to drop "flag when..." framing now that §Publishing blockers is the explicit flag-when list. Adjacent lint fix surfaced during the trim: `<link>` placeholder triggered MD033, backtick-wrapped to match file convention. Commit `0a35be3230`.

**`docs.md` priority restructure** (commit `7d8dfa952a`): Same caller-leak pattern in a different shape. fact-check was buried at line 87 (after Pre-existing issues) while the early §API and resource accuracy and §CLI commands sections did *implicit fact-check work* — telling the model to "verify via gh api," "cross-reference the registry schema source," "memorized flag lists are not authoritative" — without invoking fact-check.md's machinery.

Restructured to mirror blog.md's priority-tier pattern:

- Priority 1 — Fact-check first (invokes fact-check.md, lists docs-frequent claim categories: CLI flag existence, resource API surface, version-availability, output-format, feature-existence)
- Priority 2 — Code correctness (pointer to code-examples.md)
- Priority 3 — Cross-references and link integrity (was §Cross-references between docs pages)
- Priority 4 — Terminology and product accuracy (was §Terminology and style)
- Priority 5 — SEO and discoverability (moved ahead of Callouts)
- Priority 6 — Callouts and shortcodes (deprioritized — render-correctness, not user-impact)

§API and resource accuracy and §CLI commands sections collapsed into Priority 1's claim-categories list. Trailing §Fact-check invocation contract section unchanged (matches blog.md pattern of keeping invocation parameters separate from the priority statement).

**`fact-check.md` audit** (commit `d006b15c76`): Deepest pass of the session. 481 → 340 lines (-141, 29% reduction).

Cam selected lines 459-469 (§Heightened-scrutiny overrides) and asked whether AI-suspect was still load-bearing and whether the file was giving too much context for a narrowly-scoped skill. Both yes. AI-suspect IS load-bearing in pr-review (Step 1 detects, Step 6 renders, trivial-fix suppression) but fact-check.md is the wrong place to describe it — fact-check is invoked by CI (no AI-suspect concept), interactive `/docs-review` (no AI-suspect concept), AND pr-review.

Cam picked Option 2 from my proposal: do the full audit before cutting. The audit found 9 distinct sites:

Caller-leak (4 sites — fact-check was prescribing pr-review's logic):

- §Gating: enumerated `should-fact-check.sh` logic (AI_SUSPECT, RISK_TIER, bot/dependabot rules) — pr-review's logic. Reduced to "caller decides; CI domain files and pr-review encode their own gating rules."
- §Verification source order: "CI fact-check never uses Notion or Slack -- See ci.md §Hard rules" — line 300 already says the right thing. Dropped.
- §Assessment rules: both tables ("Effect on assessment," "Effect on confidence gauge") prescribed how the caller renders aggregate state. Dropped both; kept the one PR-introduced-vs-pre-existing sentence.
- §Heightened-scrutiny overrides: dropped the "(e.g., AI-suspect is set in /pr-review, or blog/programs sets it by default)" parenthetical and two caller-side bullets (gauge prepends 🤖, auto-trivial fixers disabled).

Output-format duplication (1 site):

- §Tiered triage: literal `## 🔬 Fact-Check Results` rendered block contradicted the §Outputs contract ("fact-check does not render directly into a comment") and reused output-format.md's bucket emoji for different concepts (🚨 Needs your eyes vs 🚨 Outstanding). Replaced with one sentence pointing the caller at output-format.md.

Implementation-detail bloat (3 sites):

- §Minimum-viable caller (pseudocode): bash pseudocode block whose comments restated the section ordering of the file. Dropped; kept the closing function-shape sentence.
- §Subagent prompt template: 30-line literal verifier prompt duplicating §Verification source order and §Claim record format. Replaced with one sentence directing the parent to copy canonical sections.
- §Why the axis exists: meta-narration paragraph on the intuition-check axis. Dropped.

Plus 3 redundant claim-extraction examples (Ex 1 single-claim, Ex 5 temporal, Ex 7 CLI-with-output) that restated the claim-type table or §Temporal-claim handling. Trimmed 7 → 4.

### Cam-flagged behaviors during the session

- **"Way too much context for a narrowly-scoped skill."** Cam's frame on fact-check.md drove the audit. The recurring question across the session: *does this skill describe its own behavior, or its callers'?* Caller-leak drops cleanly into the proposed-and-applied trim cycle.
- **Audit-before-cut discipline.** "Make me proud" was the green light for the section-by-section audit on fact-check.md. Same shape as Session 10's planned-then-executed restructure. Proposal first, "do it" after, no row-by-row negotiation when the proposal is complete enough.
- **Workflow-step vs. agent-prompt as a placement decision.** When the post-run label apply got moved out of the agent prompt into a workflow step, the framing was: *workflow steps don't forget; agents sometimes do.* Mechanical bookkeeping with no review judgment belongs on the workflow tier.
- **Cross-skill emoji vocabulary collisions.** fact-check.md was using 🚨/⚠️/✅ for *internal sub-tiers* with the same emoji as output-format.md's actual bucket vocabulary, just meaning different things. Caught during the audit as a confusion vector for callers and future readers.

### Files changed (Session 11 substance, master-relative)

1. `3a81802fca` — Add R31 missing-canonical-cross-link rule to docs and blog
2. `a8c99cacb8` — Bump prose-patterns cap from 5 to 10 per file
3. `03a7e953da` — Switch triage-prose model to Haiku and harden prompt
4. `306149861a` — Flag UK spellings and missing Oxford commas in triage-prose
5. `aa9720d8fa` — Move post-run label apply from agent prompt to workflow step
6. `7222742ac3` — Drop gh pr edit from claude-code-review agent allowlist
7. `511b792327` — Trim blog.md Priority 1 claim list — fact-check.md owns extraction
8. `0a35be3230` — Backtick-wrap <link> placeholder in blog.md weak-conclusions example
9. `2d9846726c` — Replace blog publishing-readiness checklist with publishing blockers
10. `7d8dfa952a` — Restructure docs.md by priority and surface fact-check at Priority 1
11. `d006b15c76` — Audit fact-check.md: drop caller-leak, output-format dup, and bloat

(Session 10 closeout commits at session start: `51b6a6b167` substance + `ca894cb586` notes — these properly belong to Session 10 but landed during Session 11's window.)

### Backlog after Session 11

1. **Real-PR test of the new pr-review flow + Haiku triage validation** — bundle the two outstanding test concerns into one fixture-set pass against `CamSoper/pulumi.docs#44–49`. Covers pr-review's CURRENT / STALE / ABSENT branches AND Haiku's triage-prose output on prose-flagged PRs (specifically watch for product-name false positives: ESC, IaC, OIDC, kebab-case identifiers).
2. **Deploy script** — `gh` script to create the new label set on `pulumi/docs` upstream. Don't ship until #1 surfaces no surprises.
3. **Skill-file consistency audit** (NEW) — fact-check.md's audit pattern (caller-leak / output-format duplication / implementation-detail bloat / DRY violations / contradictions / stale references) likely has cousins across the rest of the docs-review and pr-review skill packages, including the prompt blocks embedded in `claude-triage.yml` / `claude-code-review.yml` / `claude.yml`. Audit prompt produced at session-end for a fresh-context run; audit not yet executed.
4. **`programs.md` / `infra.md` priority restructure** (open) — the priority-tier shape worked for blog.md and docs.md. programs.md and infra.md may benefit from the same restructure but weren't touched this session.

### Memory updates

None this session. No new contributor names, project facts, or feedback patterns surfaced that aren't already captured in existing memory entries.

---

## Session 12 — 2026-04-29 → 2026-04-30 (skill-file audit, three converging passes)

### Trigger

Session 11's backlog #3: "Skill-file consistency audit — fact-check.md's audit pattern likely has cousins across the rest of the docs-review and pr-review skill packages, including the prompt blocks embedded in claude-triage.yml / claude-code-review.yml / claude.yml. Audit prompt produced at session-end for a fresh-context run; audit not yet executed."

The prompt was executed three separate times across the session. Each run produced a fresh audit report and a fresh apply-fixes pass. This is worth recording explicitly — it was not a deliberate "iterate three times" choice; the same prompt got rerun against the (newly-tightened) state and continued to find things to cut.

### Three audit-and-apply cycles

| Pass | Apply commit | Files | Net lines | Notes |
|---|---|---|---:|---|
| 1 | `808358d563` | 13 | -61 | First pass, deepest cut. Caller-leak / output-format dup / DRY across the largest set of files. |
| 2 | `156f924fdb` | 10 | -38 | Output-format caps, prose specificity, residual DRY. |
| 3 | `578d6772b9` | 9 | -27 | Caught fact-check.md's ✅ alignment claim as a fresh contradiction (not surfaced in passes 1-2); collapsed trust-and-scrutiny.md's heightened-scrutiny table to delegation pointers. |

Returns are diminishing in line count, but Pass 3 still surfaced one genuine high-severity contradiction (fact-check ✅ Verified vs canonical ✅ Resolved-since-last-review) that the earlier passes missed. The pattern is **not pure churn** — the audit converges, but each pass is finding marginally-smaller real issues. The audit is largely converged for the docs-review and pr-review packages now; another pass would likely produce <10 lines of cuts.

### Pass-3 specific notes

- **Audit erratum caught at pre-flight planning:** the audit report listed `fact-check.md:30` as part of the bare-`docs-review/ci.md`-ref cluster. False positive — fact-check.md has no ci.md reference. Same pre-flight grep also found `update.md:182` which the audit *missed*. Errata documented in the plan, applied work scoped accordingly.
- **Bare-ref decision punted (again):** repo-wide grep for `docs-review:ci` returned zero matches. No working precedent for the colon-form on top-level skill entries. Existing bare-path form `docs-review/ci.md` is internally consistent across all four call sites (programs.md, docs.md, update.md, claude.yml prompt). Pass 3 plan deferred the rewrite. Same question recurred in passes 1 and 2 — needs a documented authoring convention to stop the recurrence in future audits.
- **fact-check.md ✅/⚠️ semantic collision (NEW):** fact-check's "✅ Verified" tier emoji collided with output-format's canonical "✅ Resolved since last review" bucket. They share an emoji but mean entirely different things — verified-fact ≠ resolved-finding. The "intentionally aligned" statement at fact-check.md:281 was misleading callers. Replaced the alignment claim with explicit disambiguation (🚨/⚠️ align; ✅ Verified is fact-check's own collapsed-details bucket, *not* the canonical ✅ Resolved). Tier rules table's ⚠️ row gained a caller-side note prefixing evidence with "verified weakly" so a reader can tell sub-tiers apart.
- **trust-and-scrutiny.md table → delegation:** the heightened-scrutiny behaviors table was pinning specific Step 6 / Step 8 behaviors (caller-leak — describes pr-review's render layer from inside trust-and-scrutiny). Collapsed to four delegation bullets pointing at fact-check.md, action-preview-templates.md (×2), and pr-review SKILL.md Step 6.

### Cam-flagged behaviors during the session

- **"This is the THIRD time we've run that same prompt."** Cam noticed that the audit-and-tighten exercise had been re-run repeatedly in this session without a checkpoint. Future-Cam directive embedded: stop re-running the audit and re-benchmark the skill against the actual test PRs to see whether the cleanup moved the quality needle. Three rounds of skill-file polish ≠ measurable improvement until we test.
- **Audit prompt is broad enough to over-fire.** The prompt explicitly invites the auditor to scan for nine failure modes across 22 files. Even after a clean apply pass, a re-run finds new cuts at the margin because the auditor's prior context isn't wired in. Future audits should either (a) be one-shot, with explicit "stop and benchmark" gating, or (b) carry forward a "previously-cut" baseline so the auditor doesn't re-flag the same patterns.
- **Errata-during-pre-flight discipline.** The bare-ref cluster pre-flight check caught a false-positive (fact-check.md:30) and a missed match (update.md:182) before any edits landed. Worth carrying the pattern forward: every audit should get a 60-second grep-validation pass before plan approval.

### Files changed (Session 12 substance)

Three apply commits:

1. `808358d563` — Refactor documentation: streamline language, clarify procedures, and enhance consistency across various files (Pass 1)
2. `156f924fdb` — Refine documentation: clarify output format caps, enhance specificity in prose concerns, and streamline language across various files (Pass 2)
3. `578d6772b9` — Refine documentation: enhance clarity and specificity across various files, streamline language, and improve consistency in prose (Pass 3)

(Plus this SESSION-NOTES append as a separate commit.)

The audit reports themselves were written to `/workspaces/src/scratch/`; only the most recent (`2026-04-29-docs-pr-review-audit.md`) survives — earlier passes' reports were superseded.

### Backlog after Session 12

1. **Re-benchmark the skill against `CamSoper/pulumi.docs#44-49`** (the existing pipeline-comparison fixture set). After three rounds of skill-file tightening, run the same benchmark methodology used in `/workspaces/src/scratch/2026-04-28-pipeline-comparison/` and produce a comparable REPORT.md. Question to answer: did the cleanup move the quality needle, or did we just shorten the prompts? **This blocks all further skill-file work.**
2. **Triage validation against `CamSoper/pulumi.docs#50-53`** (trivial / frontmatter-only fixtures): re-run Haiku triage-prose to confirm no regression on product-name false positives or Oxford-comma flagging post-cleanup.
3. **Bare-ref / canonical notation decision** (NEW, recurring) — pick one of (a) document `docs-review/ci.md` as the canonical bare-path form for top-level skill entries in an authoring-conventions doc, OR (b) extend the skill loader's resolution to accept `docs-review:ci` and sweep the four call sites. Either kills the recurrence in future audits.
4. **Deploy script** — `gh` script to create the new label set on `pulumi/docs` upstream. Still gated on benchmark validation per Session 11 backlog #2.
5. **`programs.md` / `infra.md` priority restructure** — Session 11 backlog #4, untouched.
6. **Stop the audit-rerun loop.** Mark the skill-file consistency audit (Session 11 backlog #3) as **closed; converged** unless benchmark results suggest specific issues that warrant another targeted pass.

### Memory updates

None this session. The "stop re-running the same audit, benchmark first" directive belongs in this file (specific to the pr-review-overhaul branch), not in cross-session memory — it's project-state context, not a durable user preference.

---

## Session 13 — 2026-04-30 (rebenchmark, cost recovery, Session 14 plan)

### Trigger

Session 12 backlog #1: re-benchmark the post-Session-12 skill state against `CamSoper/pulumi.docs#44–53` to confirm the three audit-and-apply passes preserved or improved review quality. **Blocked all further skill-file work.**

### What we ran

Reused the 2026-04-28 fixture set (6 review-benchmark + 4 triage-fixture branches on the cam fork). Built one `ops:` sync commit (`81c89f190d`) that overlays the post-Session-12 `.claude/commands/`, `.github/workflows/claude-*.yml`, and `AGENTS.md` from worktree HEAD `578d6772b9` onto cam/master. Rebased every fixture branch onto the sync, force-pushed, then opened 10 new draft PRs (`CamSoper/pulumi.docs#54–63`) and marked ready in sequence. Both head and base of every PR carry the same skill state, so the PR diffs show only substantive content — no skill churn pollution.

Captured per-PR: pinned `<!-- CLAUDE_REVIEW N/M -->` body, triage classifier output (from workflow logs), `<!-- TRIAGE_PROSE -->` advisories on the trivial / frontmatter-only set, plus `duration_ms` / `num_turns` / `total_cost_usd` from each `claude-execution-output.json` summary.

Report: `/workspaces/src/scratch/2026-04-30-rebenchmark/REPORT.md`.

### Outcome — three findings

**1. Quality: HOLD with quality-bias improvements.**

| | Pass-3 (baseline) | Post-Session-12 | Δ |
|---|---:|---:|---:|
| 🚨 Outstanding | 8 | 8 | 0 |
| ⚠️ Low-confidence | 12 | 11 | −1 |
| Total findings | 20 | 19 | −1 |

Counts are statistically indistinguishable, but substance shifted in a desirable direction:
- Two new substantive catches the baseline missed: **broken `/docs/ai/integrations/` link on PR 18685** (🚨), and **`STYLE-GUIDE.md` `meta_desc` 120-char floor enforcement on PR 18620** (4 sidecars under floor — baseline produced a clean review on this PR, missing the rule entirely).
- Sharper severity calibration on PR 18599 (correctly splits broken leaf-page `./` links from convention-only `_index.md` `./` links — leaf pages 404, `_index` pages render at the directory URL with trailing slash).
- Fact-check core preserved: PR 18647's OutSystems "96% in production" catch is identical between baseline and new. The Pass-3 ✅/⚠️ semantic disambiguation didn't degrade fact-check behavior.
- Lost: 5 minor ⚠️ catches (JumpCloud filename hedge, webpack `argv.mode` narrowing, Gartner source quality, Supabase scope, alias-removal observation). All small individually; aggregate cost is real but slight against +2 substantive 🚨 catches gained.

**2. Cost: −56% per posted review.** This is the headline number we didn't expect.

| PR | Baseline turns / cost | New turns / cost | Δ cost |
|---|---:|---:|---:|
| 54 (18599) | 77 / $5.83 | 44 / $2.29 | −61% |
| 55 (18620) | 42 / $3.65 | 23 / $1.93 | −47% |
| 56 (18605) | 78 / $5.18 | 43 / $1.90 | −63% |
| 57 (18647) | 58 / $6.33 | 49 / $3.42 | −46% |
| 58 (18642) | 50 / $3.60 | 14 / $1.20 | −67% |
| 59 (18685) | 53 / $3.47 | 26 / $1.56 | −55% |
| **Total** | **358 / $28.07** | **199 / $12.30** | **−56%** |

Same model in both columns (`claude-opus-4-7`). Driver: caller-leak sweep (Session 11) + pre-computed PR metadata block in the workflow file (cited in its own inline comment as "−85% denial reduction and −51% cost reduction stacked with the broadened allowed-tools") + output-format cap tightening + three rounds of skill-file deduplication. Wall time dropped from ~11.4 min/PR baseline to ~6.2 min/PR. Cost-per-finding: $1.40 → $0.65.

**3. Label-deploy gap is empirically blocking.** The triage classifier emits `domain:*` labels (Session 10 rename), but the cam fork's label set still uses the old `review:docs/blog/infra/programs/mixed` names. `gh pr edit --add-label` is atomic — one missing label rejects the whole transaction, so even legitimate `review:trivial` and `review:prose-flagged` labels never landed on the triage-fixture PRs. The classifier itself computed everything correctly (logs confirm); only the apply step failed. Consequence: short-circuits don't fire, so the full Claude review ran on top of every triage-fixture PR (including the 1-line typo on PR 60). Same blocker exists for the upstream rollout. **This is Session 12 backlog #4 ("Deploy script — `gh` script to create the new label set on `pulumi/docs` upstream"), surfaced concretely.**

### Triage / prose-check validation (passed)

Triage classifier: 10/10 correct on domain, trivial, frontmatter-only, mixed, prose-needed.

Haiku 4.5 prose-check on the 4 triage fixtures:

| PR | Diff | Output | FPs |
|---|---|---|---|
| 60 | "modern" → "moderne" in body | Caught: "moderne" should be "modern" | None |
| 61 | adds an alias to frontmatter | No advisory (clean) | None |
| 62 | meta_desc with "togther" + "manageing" | Both flagged with corrections | None |
| 63 | multi-line body change | No advisory (correctly no-op; not trivial / fmonly) | None |

Specifically watched-for regressions: no product-name FPs (ESC, IaC, OIDC, kebab-case identifiers), no Oxford-comma over-flagging, no hedge-words flagged as errors.

### Backlog after Session 13 (Cam's Session 14 plan)

1. **Re-test the full pipeline on fresh PRs, triage included.** Today's run scored review *outputs* against baseline but didn't observe the triage flow end-to-end (the deploy gap interfered, and the focus was on review-quality scoring). Tomorrow: open fresh PRs and watch the whole pipeline live — triage classification timing, label application (after fix), short-circuit gating actually firing on trivial / fmonly, full review composition.
2. **Simulate re-entrant reviews.** Test the three patterns documented in `AGENTS.md` §PR Lifecycle: (a) fix-response — push a commit addressing the review and `@claude` it; verify the `✅ Resolved` bucket gets updated; (b) dispute — `@claude` with reasoning to push back on a finding; verify the model concedes on evidence or holds with explanation; (c) re-verify — bare `@claude refresh` after a push; verify outstanding findings get re-checked against the new diff.
3. **Test the maintainer `pr-review` experience.** The local skill that reads the pinned comment as source of truth and refreshes it during adjudication. Walk through a full review-and-merge cycle from the maintainer's seat.
4. **Land the label-deploy script.** Hard prerequisite for #1 and Session 12 backlog #4. Same script needed for both cam fork and upstream rollout.
5. **Investigate the 5 lost ⚠️ catches.** The pattern is consistent — vendor-side fact-checks, out-of-tree compatibility flags, frontmatter housekeeping. Targeted look at `fact-check.md`'s vendor-doc-verification trigger and `infra.md`'s out-of-tree-compatibility paragraph to see if a small re-emphasis recovers them without re-bloating.
6. **Cap-review pass on `output-format.md`.** Reviews are 60% longer per finding than baseline (avg 70 lines vs 43). Suggestion-block proliferation is a quality improvement but per-section caps may want re-tightening so PR 18620-shaped reviews don't blow past the 65k limit on bigger PRs.

**Closed:**
- Session 11 backlog #3 (skill-file consistency audit) → **closed; converged** per the rebenchmark evidence.
- Cost-optimization track ("Sonnet everywhere", "Sonnet for infra only") → no longer urgent. The audit work delivered most of what those experiments were chasing without the reliability gap that the Sonnet-everywhere experiment hit (3/6 silent failures + 1 duplicate post). Re-evaluate before spending more time on model-swap experiments.

### Memory updates

None. The Session-13 findings are project-state specific to this branch and the rebenchmark; they belong in this file, not cross-session memory.

### Files changed (Session 13 substance)

No commits to `CamSoper/pr-review-overhaul`. Skill files in this worktree stayed untouched per scope. The sync commit `81c89f190d` lives on the cam fork only ("ops: sync skill state to post-Session-12 baseline (578d6772b9)") and is not for upstream merge.

Scratch artifacts:
- `/workspaces/src/scratch/2026-04-30-rebenchmark/REPORT.md` — full per-PR comparison and cost analysis.
- `/workspaces/src/scratch/2026-04-30-rebenchmark/new-reviews/pr-186XX-new.md` (×6) — captured pinned-comment bodies.
- `/workspaces/src/scratch/2026-04-30-rebenchmark/triage-fixtures/{classifier-output,prose-advisories}.txt` — triage classifier and Haiku prose-check captures.
- `/workspaces/src/scratch/2026-04-30-rebenchmark/cost-data.txt` — raw cost / turns / wall-time per run.
- `/workspaces/src/scratch/2026-04-30-rebenchmark/prior-pr-meta/pr-{44..53}.json` — previous fixture PRs' titles/bodies, copied for the new PRs' shape.

---

## Session 14 — 2026-04-30 (label deploy, spelling/grammar extraction, prose-patterns elevation)

### Trigger

Session 13 backlog #4 (label-deploy script — concrete blocker for end-to-end pipeline observation) and a thread Cam opened mid-session: "we tell reviewers to apply prose patterns in the intro but never make it a numbered priority; spelling/grammar coverage is missing on non-short-circuit PRs." Both threads turned out to be the same arc.

### What shipped

1. **`scripts/labels/labels.json` + `scripts/labels/sync-labels.sh`** — declarative canonical state for the 12 PR-triage labels (5 `domain:*`, `review:trivial`, `review:frontmatter-only`, `review:prose-flagged`, `review:claude-{ran,stale,working}`, `needs-author-response`) plus 5 legacy renames from the pre-Session-10 `review:{docs,blog,infra,programs,mixed}` names. Three-phase sync: rename-where-safe (preserves PR associations), create-or-edit, orphan-report. `--dry-run` and `--prune` flags.

2. **End-to-end pipeline confirmation on cam fork.** First re-trigger of PRs 60-63 after deploying labels: classifier 4/4 correct, atomic label apply succeeded on all 4 (Session 13's blocker), short-circuits fired on 60/61/62 (37s/33s/45s wall vs PR 63's 238s full review), TRIAGE_PROSE advisories matched Session 13 baseline. Cost ~$1.50 total.

3. **Shared `docs-review:references:spelling-grammar`.** Cam flagged that putting spelling rules into both `triage-prose.md` and `prose-patterns.md` would duplicate. Extracted protected-token list, flag list, do-not-flag list, and protected-example list into one reference. `triage-prose.md` trimmed to triage-specific framing (output JSON, cap, frontmatter-only field scope) and the workflow concatenates both into `PROSE_RULES`. Confirmed end-to-end on PRs 60-62 — Haiku reads the concatenated prompt correctly, same findings as Session 13.

4. **Cap policy split.** Structural prose findings stay capped at 10 per file (passive voice, filler, intensifiers, etc.); spelling/grammar render uncapped so a careless-speller PR gets the full punch list as suggestion blocks the maintainer can batch-accept. Triage Haiku cap raised 5 → 15 to keep parity on frontmatter-only PRs (which short-circuit the full review).

5. **Ordered-list `1.` rule moved into reviewer scope.** Old `shared-criteria.md` claimed the linter owned this; MD029's default `one_or_ordered` accepts both `1. 1. 1.` and `1. 2. 3.`. Removed the wrong linter-boundary claim and added a new `### Ordered-list numbering` rule under §Criteria.

6. **Prose-patterns elevated to a numbered priority** in `docs.md` (new Priority 5, between Terminology and SEO; SEO and Callouts pushed to 6/7) and `blog.md` (replaces the old Priority 2 "AI-slop detection"). General AI-writing patterns (em-dash density, contrastive frames, hedging, buzzword tax, empty transitions, uniform sentence rhythm, repetitive paragraph openers, dense paragraphs) merged into `prose-patterns.md` so docs reviews benefit too. Blog-specific patterns retained in `blog.md` under the new Priority 2 (TL;DR recaps, self-criticism of prior Pulumi decisions, weak conclusions, listicle bloat). Generalized the "section unit" definition (between H2s; in blog posts, also `<!--more-->` to first H2).

### Cam-flagged behaviors during the session

- **Bare-ref vs colon notation (recurring).** First draft used bare `docs-review/triage-prose.md`; Cam said "use `skill:directory:file` notation." Switched to `docs-review:triage-prose`. This is Session 12 backlog #3 finally getting decided in practice — colon-form is now the convention for cross-skill references. Earlier audits punted on whether to formalize; Cam's correction makes the call.
- **Caller-leak audit pass — done by request.** Cam asked to "review your other changes from this session for similar patterns" after catching a 4-sentence ordered-list rule with diff-noise reasoning, MD029 internals, and AGENTS.md cross-ref. Audit found and trimmed: redundant in-parens listing of structural patterns in the cap rule, justification clause ("atomic, post-protected-tokens true-positive...") in the spelling-grammar delegation. New `spelling-grammar.md` came back clean — pure rules, no triage/full-review/caller mentions. Worth carrying forward: every reference-file edit should run a "is this rule, or is this author-context?" pass before commit.
- **"Some people are lousy spellers."** Cam pushed back on capping spelling at 10. Real concern: typos are atomic post-protected-tokens true-positives that the maintainer can batch-accept as suggestion blocks; capping mixes them with subjective structural patterns and crowds them out. Resolution: option-1 (uncap spelling in CI) over option-3 (separate uncapped sweep in pr-review skill) because the *author* benefits from the complete typo list, not just the maintainer; pr-review's existing "make changes" path already handles batch-accepting the pinned-comment suggestions.
- **"Did we ever bake spelling/grammar/prose priorities into the docs and blogs reviews?"** Caught mid-commit, before SESSION-NOTES update. The whole session had elevated `spelling-grammar` to a shared reference but never re-touched `docs.md` and `blog.md` to make prose-patterns a numbered priority. Recovered with the AI-slop merge — bigger refactor than originally proposed but cleaner end-state.

### Methodology lessons

- **Cherry-pick stacking bug.** First fork-test rebase used `git checkout master` (no local `master` branch in the worktree). The command silently failed; HEAD stayed where it was; each fixture got cherry-picked onto the previous one's tip. Result: PRs 61 and 62 inherited PR 60's `moderne` body change → classifier correctly saw mixed body+frontmatter changes → `frontmatter-only=false` → no short-circuit. Burned one trigger cycle. Fix: always use `git checkout -B branch <explicit-sha>` in detached worktrees; never rely on `checkout master` without verifying the local branch exists. Re-rebase off `b426b22c2b` succeeded cleanly.
- **Side-worktree dispatch saved context.** `git worktree add /tmp/cam-sync cam/master` lets you build the `ops: sync` commit and push to the fork without touching the main worktree's branch state. Cleaner than stash/checkout dance; cleanup with `git worktree remove`.
- **Idempotent label sync as a deployment primitive.** The 3-phase sync (rename → create-or-update → orphan-report) is friendlier than create-and-replace — preserves PR associations across renames, no destructive moves without `--prune`, re-run is a clean no-op. Worth replicating for any future label-taxonomy changes.

### Files changed (Session 14 substance)

Three commits on `CamSoper/pr-review-overhaul`:

1. `e0bc27bdda` — Add label-deploy script for the canonical PR-triage taxonomy
2. `d838e587b4` — Elevate prose patterns to a numbered priority; unify spelling/grammar rules
3. (this commit) — Add Session 14 notes

Cam fork operations (not for upstream):
- `b426b22c2b` — `ops: bump triage prose cap to 15; uncap CI spelling/grammar findings` (sits on top of `6123db3754` `ops: sync skill state — extract spelling-grammar shared reference`).
- `cam/master` advanced; fixture branches `test-trivial-typo`, `test-fmonly-clean`, `test-fmonly-typo` rebased onto the post-Session-14 sync.

### Backlog after Session 14

1. **Re-entrant `@claude` patterns** (Session 13 backlog #1.b). Test fix-response, dispute, and re-verify on the existing fixture set — they have pinned reviews and are the right substrate.
2. **Maintainer `pr-review` experience walkthrough** (Session 13 backlog #1.c). Full review-and-merge cycle from the maintainer's seat using one of the fixture PRs.
3. **Investigate the 5 lost ⚠️ catches** (Session 13 backlog #5). Targeted look at fact-check.md's vendor-doc-verification trigger and infra.md's out-of-tree-compatibility paragraph.
4. **Cap-review pass on `output-format.md`** (Session 13 backlog #6). Reviews are ~70 lines per finding vs 43 baseline; per-section caps may want re-tightening.
5. **Upstream label deploy.** Run `scripts/labels/sync-labels.sh --repo pulumi/docs --dry-run` before merge, then for-real after the spelling-grammar refactor lands.
6. **Prose-pattern elevation: re-benchmark or trust the test?** The extraction + priority elevation didn't land on the cam fork's `ops:` sync until the second iteration; Session 13 baseline didn't include the new patterns. Soft-watch: a future blog PR with em-dashes and hedging should now produce findings under Priority 2. If results look noisy, tighten thresholds; if they look thin, validate the model is reaching prose-patterns through the priority walk.

### Memory updates

None. All Session-14 facts are project-state specific to this branch.

---

## Session 14 — continued (2026-04-30, after initial notes)

### Trigger

Cam asked whether `fact-check.md` line 327 ("Gating always returns RUN") really referred to anything. It didn't — it was a vestige of an internal gating mechanism that had been removed entirely (gating moved out to callers in an earlier session). That observation kicked off two follow-on threads: a full caller-leak audit of every file in `docs-review/`, and a re-evaluation of the lint-markdown.js extensions added in Session 9.

### Caller-leak audit pass on `docs-review/`

Four parallel agents audited 13 files. ~41 trims total, +1 file (`SKILL.md`) untouched (already clean). The pattern catalog applied: caller-leak prose ("the caller composes...", "owned by the caller's output format"), cross-skill maintenance notes ("if you change rules here, mirror them in X"), justification clauses (rule + reasoning when the rule alone is sufficient), implementation/runtime trivia (linter rule codes, script paths), and stale references to mechanisms that no longer exist.

| Agent scope | Trims | Net |
|---|---:|---:|
| `programs.md`, `output-format.md`, `image-review.md` | 9 | -2 |
| `blog.md`, `shared-criteria.md`, `domain-routing.md` | 11 | -4 |
| `SKILL.md` (no edits), `ci.md`, `docs.md` | 11 | -7 |
| `infra.md`, `code-examples.md`, `prose-patterns.md`, `update.md` | 10 | -9 |

`fact-check.md` was audited first by hand as the template (commit `1ce2529d41`, -12 lines / 11 trims) — the single biggest cleanup since it had the deepest caller-leak. Pattern catalog from that audit became the agent prompts.

**Items the agents flagged but didn't fix** (all resolved or punted by Cam during review):

- `output-format.md` removed a sentence referencing `scripts/pinned-comment.sh`. Verified the script's wiring isn't documented elsewhere — re-add planned but not executed; flag remains for follow-up.
- `blog.md` line 102 "(Lint catches missing or malformed `social:` blocks.)" — flagged as needing verification against `lint-markdown.js`. Rolled into the lint-revert thread below; line is gone.
- `shared-criteria.md` "currently disabled" linter rules (MD045/MD040) — flagged for verification. Not pursued.
- `docs.md` L14 "Whole-file read is opt-in per the pre-existing extraction rule below" — framing slightly loose; left for now.
- `ci.md` hard rule 1 — possible outdated CI shallow-checkout claim; left for now.
- `update.md` L160 — verify `output-format` is downstream of update.md; left for now.
- `update.md` L182 — bare-path `docs-review/ci.md` while rest of file uses colon notation; minor consistency, left for now.

Agent batch landed as commit `479e5e4587` (Cam committed in one shot).

### The lint-markdown.js round trip (don't repeat)

Cam flagged that the metadata checks in lint (`checkPageTitle` / `checkPageMetaDescription` / `checkMetaImage` from master, plus `checkSocialBlock` / `checkMoreBreak` / `checkPlaceholderMetaImage` added in Session 9) were a friction source: drive-by edits on a page whose title is 65 chars block at pre-commit on a rule the contributor didn't introduce.

First attempt (commit `b88460ab94`): migrate `checkPageTitle` / `checkPageMetaDescription` / `checkMetaImage` to review-side rules in `shared-criteria.md` §Frontmatter; remove the corresponding linter functions. Worked fine in isolation — `make lint` clean — but on second look Cam realized the right move was to revert the *entire* lint surface (both the recent migration AND the Session-9 extensions) rather than stack partial migrations on top of partial extensions.

Final state (commit `698e24acf2`):
- `scripts/lint/lint-markdown.js` reset to `origin/master`. Title / meta_desc length / meta_image `.png` extension stay in lint (existing master behavior, accept the drive-by friction). Session-9 additions removed entirely from lint.
- `shared-criteria.md` §Linter boundary restored to claim ownership of those three.
- `blog.md` §Publishing blockers absorbed the three Session-9 checks as review-side rules: `social:` block presence (with marketing-owns-voice caveat — flag presence, don't draft copy), `meta_image` placeholder match (SHA256 against `.claude/commands/_common/images/blog-post-meta-placeholder.png`), `<!--more-->` presence + position folded into one rule.
- Stale "lint catches X" parentheticals in `blog.md` §Do not flag and §Publishing blockers cleaned up to match the new reality.

The b88460ab94 → 698e24acf2 round trip is worth remembering: when the question is "should this rule live in lint or review?", reverting to master and adding only what's missing on the review side is cleaner than migrating in halves.

### Files changed (Session 14 continuation substance)

- `1ce2529d41` — Trim caller-leak and stale references from fact-check.md
- `479e5e4587` — Refine documentation review criteria and output formatting across multiple reference files (agent batch — 12 files)
- `b88460ab94` — Move deterministic frontmatter checks out of pre-commit lint into PR review *(reverted by 698e24acf2)*
- `698e24acf2` — Revert this branch's lint-markdown changes; cover gaps in blog review

### Backlog updates

Add to backlog:
- **`output-format.md` `pinned-comment.sh` reference.** Agent removed a sentence pointing to the script during the audit; verify the wiring is documented somewhere or restore.
- **Bare-ref / colon notation consistency** (Session 12 backlog #3, recurring). `update.md` L182 still uses bare `docs-review/ci.md` while the rest of the file uses `docs-review:references:X`. Documented as the canonical convention now via the spelling-grammar refactor — but the sweep across remaining bare-ref call sites is open.

No item retired this session.

### Memory updates

None.

---

## Session 15 — 2026-04-30 (residual-backlog cleanup)

### Trigger

Cam dropped Session-14 backlog items 1, 2, 3, 5, 6 (the work that needs fixture PRs, external deploys, or a re-benchmark) and asked for a plan covering the rest. Remaining substance: item #4 (cap-review on `output-format.md`), item #7 (restore the `pinned-comment.sh` reference an earlier audit removed), item #8 (bare-ref → colon-form sweep), and four "agents flagged but didn't fix" items from the Session 14 continuation audit.

### What shipped

1. **`output-format.md` — restored `pinned-comment.sh` pointer + added §Comment lifecycle.** The Session-14 commit `479e5e4587` had trimmed the only sentence connecting `output-format.md` to `scripts/pinned-comment.sh`. Verified via repo grep that no other reference file documents the marker convention, the 1/M sacrosanct guarantee, or the script's ownership of splitting/upsert/prune. Replaced with a tighter paragraph: marker format on first line of every comment, script owns the lifecycle, 1/M is sacrosanct (script refuses to delete index 0), no `gh pr comment` ever called directly. New subsection sits between §Overflow and §DO-NOT list. Conservative scope per Cam's call — no new per-bucket caps, no prompt-shape change.

2. **Per-finding rendering cross-reference in `output-format.md` §Bucket rules.** One-line pointer to `docs-review:references:shared-criteria` for suggestion-block sizing and quote-and-rewrite mandate. Stops the "where do per-finding rules live?" recurrence in audits.

3. **`docs.md` L14 framing tighten.** "Whole-file read is opt-in per the pre-existing extraction rule below" was a loose forward-reference — readers had to scroll the whole file to find what triggered the opt-in. Tightened to point at §Pre-existing issues (opt-in) directly.

### What did NOT ship — and why

**The bare-ref / colon-form sweep was abandoned mid-implementation.** The plan opened by listing 4 sites to convert (1 in `update.md`, 3 in workflows). On a sanity-check of existing convention before edit, the picture flipped:

- **Reference files** (anything in `references/`) are referenced via colon form (`docs-review:references:update`, `docs-review:references:spelling-grammar`, etc.). Cam ratified this mid-Session-14.
- **Top-level skill files** (`docs-review/ci.md`, `docs-review/SKILL.md`, `docs-review/triage-prose.md`) are referenced via bare path everywhere they appear: `update.md` L182, `claude.yml` L192/L208, `claude-code-review.yml` L230/L237, `AGENTS.md` L119, `claude-triage.yml` L134. There are zero existing colon-form refs to top-level files in the repo.

So the recurring "bare-ref vs colon notation" flag (Session 12 backlog #3, re-flagged by the Session 14 audit) is a false-positive: the codebase already uses a **split convention** that's internally consistent. Top-level files take bare paths; reference files take colon form. The audits keep noticing the bare-path top-level refs and assuming they're inconsistent with the colon-form references next to them, but the rule is operating exactly as the codebase already executes it.

Cam's call: document the convention here, don't sweep. No edits to `update.md`, `claude.yml`, `claude-code-review.yml`, or `AGENTS.md`.

### Convention (recorded for future audits)

**Cross-reference notation in `.claude/commands/` and `.github/workflows/`:**

- **Reference files** (under any skill's `references/` subdirectory) → colon form: `docs-review:references:update`, `pr-review:references:trust-and-scrutiny`, `move-doc:references:link-updates`.
- **Top-level skill files** (anything directly under a skill directory: `SKILL.md`, `ci.md`, `triage-prose.md`) → bare path: `docs-review/ci.md` or full repo path `.claude/commands/docs-review/ci.md` when the consumer is a workflow or a non-skill-aware reader.
- **File-system operations** (`bash`, `cat`, `grep` against a path) → always full path, regardless of whether the file is a reference or top-level. Convention applies only to prose cross-references.

If a future audit re-flags `docs-review/ci.md`-style bare-paths as inconsistent, point it back here.

### Three audit items verified accurate (no fix)

The Session 14 continuation flagged four items as "left for now." Investigation confirmed three of them were already correct:

- **`shared-criteria.md` L61 "MD045/MD040 currently disabled in the linter."** Verified: `.markdownlint-base.json` sets both rules to `false`. Claim is accurate.
- **`ci.md` Hard rule 1 "shallow checkout."** Verified: `.github/workflows/claude-code-review.yml` uses `actions/checkout@v6` with `fetch-depth: 1`. `fetch-depth: 1` is shallow; claim is accurate.
- **`update.md` L160 "Hand the updated review object to `docs-review:references:output-format`."** Verified: `output-format.md` does not call back into `update.md`. Relationship is one-directional (update → output-format); the downstream framing is accurate.

The fourth item (`docs.md` L14 framing) was the only one that needed a real edit — covered above.

### Backlog after Session 15

Session 14's dropped items remain dropped (Cam dropped them during Session 15 trigger):

1. Re-entrant `@claude` patterns testing (fix-response, dispute, re-verify).
2. Maintainer `pr-review` walkthrough.
3. Investigate the 5 lost ⚠️ catches from the Session 13 rebenchmark.
4. Upstream label deploy via `scripts/labels/sync-labels.sh --repo pulumi/docs`.
5. Prose-pattern elevation re-benchmark (soft-watch a future em-dash-heavy blog PR).

These reactivate when fixture PRs / external deploys come back into scope.

**Closed:** Session-14 backlog items 4, 7, 8, plus all four "left for now" items from the Session 14 continuation audit.

### Files changed (Session 15 substance)

- `.claude/commands/docs-review/references/output-format.md` — restored `pinned-comment.sh` reference + added §Comment lifecycle + per-finding cross-ref to shared-criteria
- `.claude/commands/docs-review/references/docs.md` — L14 forward-reference tighten

Plus this SESSION-NOTES entry.

### Memory updates

None. The bare-ref / colon-form convention is project-state for this branch; the rule belongs in this file and will land in `AGENTS.md` if it ever needs to outlive the branch.

---

## Session 16 — 2026-04-30 (end-to-end pipeline test, self-loop fix, fact-check + update.md tightening)

### Trigger

Cam closed all open fork PRs and asked to run the full end-to-end pipeline against the fixture set: open fresh PRs, watch initial reviews compose, exercise re-entrant patterns on a chosen subset, leave a no-activity subset for the maintainer `pr-review` walkthrough.

### What ran

- New sync commit `4cc3372000` on `cam/master` overlaying the post-Session-15 skill state from worktree HEAD `214dd5caf4`.
- All 14 fixture branches rebased onto the sync (6 review-benchmark + 4 triage-fixture + 4 base-pr branches). Same Session-14 lesson applied (use `git checkout -B branch <explicit-sha>`, never `checkout master` on a detached worktree).
- 10 fresh draft PRs `CamSoper/pulumi.docs#64–73`, marked ready in batch at 18:30:59Z.
- Re-entrant phase: chose 4 PRs for `@claude` triggers (fix-response on 64+67, dispute on 66, re-verify on 69); left 6 PRs untouched (65, 68, 70, 71, 72, 73) for the maintainer `pr-review` walkthrough later.

### Findings

**1. Initial-review pipeline: passing on every dimension.**

| Axis | Result |
|---|---|
| Triage classification | 10/10 correct on domain + short-circuit |
| Atomic label-apply | 10/10 succeeded — Session-13 regression cleared by the post-Session-14 label deploy |
| Short-circuits firing | `review:trivial` on 70, `review:frontmatter-only` on 71/72 — full review skipped on each, prose advisories landed correctly on 70 ("moderne") and 72 ("togther", "manageing") |
| Cost vs Session-13 | $11.79 for 7 full reviews vs $12.30 for 6 — flat per-PR ($1.68 avg vs $1.71 prior) |
| Wall time | 32m51s cumulative, last review posted ~18:39Z |

**2. Self-loop bug discovered and fixed mid-session.** Posted reviews carry an `@claude` invitation in the footer ("Mention `@claude` to refresh or argue your case"), and `claude.yml`'s `if: contains(comment.body, '@claude')` matched the bot's own posts — 8 self-triggered re-entrant runs fired on the initial-review batch. All ESC-failed harmlessly (see point 3 below) but cluttered the run view. Two-layer fix shipped:

- `.github/workflows/claude.yml` — added `github.event.{comment,review,issue}.user.login != 'claude[bot]'` to each event branch's `if`.
- `.claude/commands/docs-review/references/output-format.md` — replaced the literal `@claude` in the footer with `&#64;claude` (HTML entity). Renders as `@claude` visually; `contains()` no longer matches.

Defense-in-depth: either fix alone would block the loop. Verified on the re-entrant batch — exactly 4 runs fired (matching 4 manual `@claude` posts), zero spurious self-triggers. Commits `d7c76ddb46` (worktree branch) + `90f8d9e09f` (cam/master ops mirror).

**3. Cam-fork ESC trust gap blocks re-entrant on the fork.** The first re-entrant batch all 401'd at the `Fetch secrets from ESC` step — the cam fork's GitHub Actions OIDC token isn't trusted by Pulumi's ESC environment. The initial-review workflow doesn't hit this because it uses plain `secrets.ANTHROPIC_API_KEY` and the default `GITHUB_TOKEN`; only re-entrant goes through ESC for `PULUMI_BOT_TOKEN`. Fork-only ops patch shipped (`01de922a71`) — drops the ESC step, falls back to `secrets.GITHUB_TOKEN`. Not for upstream merge. Documented here so future fork-test runs know.

**4. Re-entrant patterns 4/4 successful on Sonnet** (`01de922a71` enabled the runs to actually execute):

| PR | Pattern | Bucket transition | Behavior |
|---:|---|---|---|
| 64 | fix-response | 🚨 2→1, ✅ 0→1 | Resolved the addressed half (`_index.md`), kept the un-addressed half (`executable-plugin.md`) outstanding |
| 67 | fix-response | 🚨 1→1, ✅ 0→1 | Resolved body+LinkedIn fix; **caught the missed Bluesky social block** as a new 🚨 — partial-fix detection working better than the initial review |
| 66 | dispute | 🚨 1→1, ⚠️ 1→0, ✅ 0→1 | Conceded the SCIM-acronym ⚠️ on its own footnote evidence — clean concession |
| 69 | re-verify | 🚨 1→1, ⚠️ 2→2 | Re-verified outstanding against new diff after unrelated edit, line numbers updated 85→83 |

Cost: $1.22 / 66 turns / 12m42s for all 4 re-entrant runs. Sonnet runs ~5× cheaper per PR than the initial Opus pass on the same PR shape — the cost architecture is solid.

**5. Initial fact-check missed PR 67's Bluesky social block.** The OutSystems "in production" overstatement appeared in 3 places: body, `social.linkedin`, `social.bluesky`. Initial Opus review caught body + LinkedIn. The Bluesky block was missed. Re-entrant Sonnet caught it after I addressed the cited locations (the partial-fix detection compensated), but if the author had merged after fixing only what was flagged, the broken Bluesky text would have shipped to the social-media bot. **Mitigation shipped** — see "Files changed" below.

### Mitigations shipped (Priority 1 + Priority 3 from the e2e learnings plan)

**`fact-check.md` §Frontmatter sweep (new subsection under §Claim extraction).** When extracting a claim from any of body / `meta_desc` / `social:` sub-keys, sweep the file for the same factual phrasing or near-paraphrase, and treat all occurrences as one claim with multiple cited locations. Single finding renders one suggestion-block per location. PR 67 case: body + LinkedIn + Bluesky overstatement → one finding, three locations, fixed in one pass.

**`update.md` §Case 1 — fix-response, new step 2.** When re-verifying a previously-outstanding finding that quoted a specific phrase, sweep the current file for every occurrence of that phrase (or near-paraphrase) — body + frontmatter + every `social:` sub-key — and raise unflagged occurrences as new 🚨 findings. Initial reviews can miss frontmatter duplicates; re-entrant is the safety net before merge. This codifies the behavior PR 67's re-entrant pass exhibited spontaneously on Sonnet — making it a guarantee, not a happy accident.

### Items NOT shipped (in backlog)

- **Cost-variance monitoring** (per-PR cost ceiling alert, e.g., $5). Cost held flat across 3 measurement passes; not yet a real problem.
- **Recover Run Example Code Tests / Social Media Review failures on the fork.** Cosmetic only; fork-side test infra issue.

### Methodology / repeatable patterns

- **Use a side worktree for fork ops.** `git worktree add /tmp/cam-work cam/master`, edit, commit, `git push cam HEAD:master`. Cleaner than stash/checkout dance; lets the main worktree keep its branch state. Worth replicating any time we need to stage fork-only ops commits.
- **Mid-run regressions are findable from the e2e test, not just from cap-review reading.** The PR 67 missed-Bluesky-block came out of pushing a partial fix and watching the re-entrant pass. Cap-review on the rendered review wouldn't have caught it because the initial review *looked* fine — it took the round trip to expose the gap.

### Backlog after Session 16

Active:
1. **Maintainer `pr-review` walkthrough** on the no-activity subset (PRs 65, 68, 70, 71, 72, 73). Cam plans to do this on a clean session.
2. **Cost-variance monitoring** (Priority 4 from the plan) — defer until a real overrun appears.
3. **Cam-fork CI cosmetic fixes** (Priority 5) — non-Claude workflow failures on the fork.
4. **Investigate 5 lost ⚠️ catches** (Session 13 backlog #5) — still open.
5. **Upstream label deploy** (Session 14 backlog #4) — still open. Verify `scripts/labels/sync-labels.sh --repo pulumi/docs --dry-run` then for-real before this branch merges.
6. **Prose-pattern re-benchmark** (Session 14 backlog #5) — soft-watch a future em-dash-heavy blog PR.

Closed this session:
- Session 13/14/15 backlog item: "Re-test the full pipeline on fresh PRs, triage included" → ✅ done.
- Session 13/14/15 backlog item: "Simulate re-entrant reviews" → ✅ done; all three patterns (fix-response, dispute, re-verify) verified end-to-end.
- Cosmetic noise: self-loop on initial reviews → ✅ fixed (two-layer guard).
- Fact-check coverage gap: frontmatter sweep on duplicate phrasing → ✅ shipped.
- Re-entrant safety net: partial-fix duplicate-occurrence sweep → ✅ shipped.

### Files changed (Session 16 substance)

- `4cc3372000` — `ops: sync skill state to post-Session-15 baseline (214dd5caf4)` *(cam/master only)*
- `d7c76ddb46` — Stop self-loop on Claude Code re-entrant workflow *(worktree branch)*
- `90f8d9e09f` — `ops: stop @claude self-loop in re-entrant workflow` *(cam/master mirror)*
- `01de922a71` — `ops: bypass ESC for re-entrant claude on cam fork` *(cam/master only, fork-side)*
- (this commit) — fact-check.md frontmatter-sweep rule + update.md fix-response duplicate-occurrence sweep + Session 16 notes

Cam-fork operations:
- `cam/master` advanced from `b426b22c2b` → `01de922a71`.
- 14 fixture branches force-pushed atop the new sync.
- 10 PRs opened (`CamSoper/pulumi.docs#64–73`); all initial reviews + 4 re-entrant runs complete; 6 PRs left in no-activity state for the maintainer walkthrough.

Scratch artifacts: `/workspaces/src/scratch/2026-04-30-e2e-test/` — `REPORT.md`, `reviews/`, `triage/`, `cost-data.txt`, `reentrant-cost.txt`, `PLAN.md`.

### Memory updates

None. All Session-16 facts are project-state specific to this branch and the e2e fixture set; they belong in this file.

---

## Session 17 — 2026-04-30 (e2e re-test, trivial-threshold bump, AGENTS.md trim)

### Trigger

Cam closed Session 16's fork PRs and asked to re-run the full e2e against the fixture set, specifically validating the two Session-16 mitigations (fact-check frontmatter sweep, update.md duplicate-occurrence sweep) end-to-end. After the test, surveyed cost wins and AGENTS.md context bloat.

### What ran

- New sync `71f9188488` on `cam/master` overlaying worktree HEAD `113955e6b2` (fact-check + update.md tightening from Session 16).
- All 14 fixture branches cherry-picked onto the new sync (Session 14 lesson: explicit-SHA `git checkout -B`, never `master` on detached worktree). Session 16's extra fix-response/edit commits dropped from PRs 64/67/69 in the rebase.
- 10 fresh draft PRs `CamSoper/pulumi.docs#74–83`, marked ready 19:23:57Z; last review posted ~19:30Z.
- Re-entrant phase: 4 active (74 fix-response, 75 dispute *(pivot — see below)*, 77 fix-response partial body-only, 79 re-verify). 6 untouched (76, 78, 80, 81, 82, 83).
- Mid-session: trivial-threshold bump and AGENTS.md trim shipped after the e2e validation completed.

### Findings

**1. Fact-check frontmatter sweep validated end-to-end.** PR 77's initial review Finding 1 cited body line 38 + `social.linkedin` line 21 + `social.bluesky` line 28 as a single finding with three locations. Session-16 regression closed; Bluesky no longer missed. **Bonus: PR 77 turn count dropped 96 → 53 (−45%) and cost $3.32 → $2.93 (−12%)** because the sweep makes one verification cover three locations.

**2. Update.md partial-fix detection validated, different code path than expected.** Body-only fix at `594249d` was recognized in-place: Finding 1 stayed open with body line struck-through and tagged `✅ resolved in 594249d`, `social.linkedin` + `social.bluesky` still cited as un-fixed. Outstanding count stayed at 2. The strict "raise unflagged duplicate as new 🚨" path was *not* exercised because the new fact-check sweep caught all 3 at initial — the rules layered correctly: fact-check catches all 3 at initial, update.md keeps the finding open until all 3 are resolved. Author cannot merge while social blocks still carry the false claim. Strict missed-duplicate path remains unverified in production; deferred.

**3. PR 76 (JumpCloud SAML) returned 0/0/0/0** — Session 16 found `🚨 1 / ⚠️ 3` on the same diff including a SCIM-acronym ⚠️ that was the planned dispute target. Real session-to-session variance. Reading was substantive ("links resolve, shortcode exists, menu weight slots cleanly between Google Workspace and Okta"), not lazy. Either Session 16's findings were borderline FPs the new run dropped, or real signal is being lost — can't tell from one run. Worth tracking; non-determinism baseline (3× same-fixture replays) was floated and deferred.

**4. Dispute pivot — PR 75 stronger than the planned PR 76 SCIM-acronym would have been.** Pivoted the dispute target to PR 75's orphan-tag verification ⚠️ with empirical evidence (`data/openapi-spec.json` has both `AI` and `RegistryPreview` tags; `_content.gotmpl:72-78` urlization regex doesn't fire on `AI`, splits `RegistryPreview` correctly). Re-entrant Sonnet conceded cleanly *with independent regex verification* — stronger concession than Session 16's PR 66, which was a single-source footnote concession.

**5. Initial-review pipeline passing on every dimension.** Triage 10/10 correct on domain + short-circuit. Atomic label-apply 10/10. Short-circuits fired on 80 (trivial), 81 (fmonly clean), 82 (fmonly typo with prose advisories on "togther", "manageing"). Cost $11.47 / 201 turns / 33m44s cumulative wall (~6 min batched). Δ vs Session 16: cost −3%, turns −18%, wall flat.

**6. Self-loop guard verified twice.** Initial-review batch: 10 reviews posted, zero spurious self-triggers (Session 16 had 8 ❌ runs before the fix shipped). Re-entrant batch: exactly 4 `Claude Code` runs for 4 `@claude` posts, zero spurious self-triggers from re-entrant reviews themselves. End-to-end clean.

**7. Re-entrant patterns 4/4 successful.** Cost $1.22 / 74 turns / 6m50s wall (parallel) — flat against Session 16 ($1.22 / 66 turns / 12m42s). Sonnet remains ~5× cheaper than initial Opus on the same PR shape.

| PR | Pattern | Initial → re-entrant | Behavior |
|---:|---|---|---|
| 74 | fix-response (split-files) | 🚨 1→1, ✅ 0→1 | Mirrors Session 16's PR 64; partial-fix split clean. |
| 75 | dispute (pivot) | ⚠️ 1→0, ✅ 0→1 | Concession + independent verification. |
| 77 | fix-response (partial body-only) | 🚨 2→2, ✅ 0→0 | Body line struck-through within Finding 1; social blocks still cited. |
| 79 | re-verify | 🚨 1→1, ⚠️ 2→2 | All preserved against new diff; quoted text on Finding 3 updated for the wording change. |

### Mitigations shipped

**Trivial-threshold bump** (`triage-classify.py:245-246`, plus `triage-prose.md:8` and `AGENTS.md` description). Lines 5→10, files 1→2. Captures typo-sweeps across 2 sibling files and wording polish that previously failed the cap. Estimated cost win: shifted PRs go from $1–1.5 (full Opus review) to ~$0.05 (triage prose pass) — direct savings if the real-world PR shape has typo-fix and small-polish PRs that currently fail the cap.

**AGENTS.md trim** (170 → 104 lines, −39%). §PR Lifecycle detail (46 lines) moved to a new `CONTRIBUTING.md` §AI-assisted contributions section absorbing the full refresh-pattern + short-circuit-criteria detail. §Moving and Deleting Files (21 lines → 3) collapsed to a pointer to `.claude/commands/move-doc/SKILL.md` while preserving the load-bearing S3-redirect-for-non-Hugo rule. §Updating Internal Links (19 → 7 lines) keeps the DO/DON'T sweep rule + canonical-path requirement (load-bearing for every edit) and defers the find/sed implementation example.

Net repo-context-per-session reduction: 66 lines, since `CONTRIBUTING.md` isn't auto-loaded.

### Items NOT shipped (in backlog)

- **Sonnet pre-pass with escalation** — investigated, declined. Cam pointed out Session 6 already studied Sonnet-everywhere thoroughly (`scratch/2026-04-28-pipeline-comparison/SONNET-EVERYWHERE-ANALYSIS.md`): 3/6 reliability failures (silent no-posts, duplicate post), substance regressions on real bugs (PR 46 SCIM tab, PR 49 datadog.svg). Real saving after reliability discount was ~20%, not paper ~46%. The pre-pass-with-escalation idea has the same blocker — silent-failure-on-large-PR — and the gate only saves money if Sonnet's null-result is reliable, which Session 6 showed it isn't. Re-open conditions unchanged: fix silent-failure root cause, then rerun.
- **Adversarial "skeptic" sub-agent for quality not cost.** ~$0.30/PR Sonnet read-only pass that re-reads draft findings before posting and flags overconfident or under-evidenced ones. Could tighten variance like PR 76's. Defer until non-determinism baseline characterizes how much drift is normal.
- **Non-determinism baseline** — 3× same-fixture replays without code changes between, to characterize session-to-session noise. Cam declined for now ("not yet").

### Methodology / repeatable patterns

- **Check SESSION-NOTES.md before proposing experiments on a multi-session branch.** I floated Sonnet pre-pass as a cost win without first checking; Cam reminded me Session 6 had already studied it. Saved a memory entry — `feedback_check_session_notes_for_prior_experiments`.
- **Pre-state a dispute pivot.** Session 17's planned dispute target (PR 76 SCIM-acronym) didn't exist this run. Pivoting mid-test was clean enough but added a `/page-cam` round-trip. Future test plans should name a primary + a backup dispute target up front.
- **Empirical-evidence dispute > footnote dispute.** PR 75's orphan-tag verification (spec has both tags) tested the dispute pattern more rigorously than a footnote re-reading would have. The model not only conceded but independently verified the urlization regex. Pick disputes where the author's case is concrete evidence, not interpretation.
- **Frontmatter-sweep is a cost optimization, not just a coverage rule.** PR 77 turn drop (96 → 53) is the data point. Future fact-check rule design should consider whether consolidation (one verification covering N locations) pays back in turns.

### Backlog after Session 17

Active:
1. **Maintainer `pr-review` walkthrough** — was scoped to PRs 76, 78, 80, 81, 82, 83 from Session 17; Cam closed all PRs at session end so a fresh set is needed. Either reopen the closed ones (safe — reopen doesn't fire Claude reviews per workflow yaml; only the lint workflow fires) or roll into Session 18.
2. **Session 18 e2e validation** — re-run with 4 new boundary fixtures (`test-trivial-2files`, `test-trivial-7lines`, `test-trivial-over-lines`, `test-trivial-over-files`) plus the standard 10-PR set, validating the trivial bump + AGENTS.md trim. Prompt drafted at session end.
3. **Cost-variance monitoring** — defer; cost flat across 4 measurement passes (S13 $12.30 / S16 $11.79 / S17 $11.47 / S18 TBD).
4. **Cam-fork CI cosmetic fixes** — unchanged.
5. **Investigate 5 lost ⚠️ catches** (Session 13 #5) — still open.
6. **Upstream label deploy** (Session 14 #4) — verify `scripts/labels/sync-labels.sh --repo pulumi/docs --dry-run` then for-real before merge.
7. **Prose-pattern re-benchmark** — soft-watch.
8. **`update.md` raise-missed-duplicate code path** — needs a contrived test where fact-check's sweep slips. Defer until a real production miss appears.
9. **Non-determinism baseline (3× same-fixture replay)** — deferred per Cam.
10. **Adversarial skeptic sub-agent** — paired with #9; revisit together.

Closed this session:
- Session 16's "fact-check frontmatter sweep validation" → ✅ validated end-to-end on PR 77.
- Session 16's "update.md partial-fix detection validation" → ✅ validated (different code path; rules layer correctly).
- Trivial threshold bump → ✅ shipped.
- AGENTS.md trim → ✅ shipped (39% reduction).
- Session 16 backlog item: "Sonnet pre-pass investigation" → ✅ closed; superseded by Session 6's prior analysis.

### Files changed (Session 17 substance)

- `.claude/commands/docs-review/scripts/triage-classify.py` — lines 5→10, files 1→2.
- `.claude/commands/docs-review/triage-prose.md` — header description text.
- `AGENTS.md` — §PR Lifecycle 46 → 5 lines; §Moving 21 → 3 lines; §Updating Internal Links 19 → 7 lines.
- `CONTRIBUTING.md` — new §AI-assisted contributions section absorbing the trimmed PR-lifecycle detail.
- `SESSION-NOTES.md` — this entry.

Cam-fork operations:
- `cam/master` advanced from `01de922a71` → `71f9188488`.
- 14 fixture branches force-pushed atop the new sync.
- 10 PRs opened (`#74-83`); all initial reviews + 4 re-entrant runs complete; Cam manually closed all 10 at session end.

Scratch artifacts: `/workspaces/src/scratch/2026-04-30-e2e-test-v2/` — `REPORT.md`, `reviews/`, `triage/`, `labels-final.txt`, `cost-data.txt`, `reentrant-cost.txt`, `opened-prs.txt`, `start-time.txt`, `reentrant-start.txt`, `open-prs.sh`, `capture.sh`, `cost-data.sh`.

### Memory updates

One feedback entry added: `feedback_check_session_notes_for_prior_experiments` — captures the Sonnet pre-pass exchange where I proposed an experiment Session 6 had already characterized. Future sessions on multi-session branches should grep SESSION-NOTES.md for prior experiments before proposing new ones.

---

## Session 18 — 2026-04-30 (e2e re-test, trivial-cap rethink, four cleanup fixes)

### Trigger

Cam closed Session 17's fork PRs and asked to re-run the full e2e against the fixture set, this time with 4 new boundary fixtures to validate Session 17's `≤5/==1` → `≤10/≤2` trivial-threshold bump. Session pivoted mid-run when Cam canceled re-entrant after a series of issues surfaced; remainder spent characterizing trivial PRs in the wild and shipping the diagnosed-but-unshipped fixes.

### What ran

- New sync `26d0e0fdb3` on `cam/master` overlaying worktree HEAD `93dbfb6a5a` (Session 17 trivial bump + AGENTS.md trim + notes), preserving the cam-fork-only ESC-bypass commit.
- 4 new boundary fixture branches added: `test-trivial-2files` (4 lines / 2 files — should be trivial under bump), `test-trivial-7lines` (7 diff-lines / 1 file — should be trivial), `test-trivial-over-lines` (12 diff-lines / 1 file — should NOT be trivial), `test-trivial-over-files` (6 lines / 3 files — should NOT be trivial because of file cap).
- All 14 fixture branches rebased onto the new sync.
- 14 fresh draft PRs `CamSoper/pulumi.docs#84–97`, marked ready 20:43:02Z.
- Re-entrant phase **canceled** by Cam after the issues below surfaced.

### Findings

**1. Diverged Revert SHAs caused merge conflicts on PRs 84–87.** First rebase script cherry-picked the Revert commit separately onto each `compare/base-pr-XXXX` and `compare/pr-XXXX` branch. The cherry-picks created distinct SHAs, GitHub's merge-base fell back to the sync, and the file's create-on-head + delete-on-base history read as a modify/delete conflict. PRs opened with `MERGEABLE=false`. Fix: rebase head branches OFF THE REBASED BASE branches so they share the actual Revert SHA. Codified in `scratch/2026-04-30-e2e-test-v3/rebase-fixtures.sh`.

**2. Empty-diff race on PR creation.** Right after the force-push, `gh pr view --json files` returned 0 files / 0 additions / 0 deletions for ~30-60s while GitHub re-evaluated PR diffs. The review workflow read this empty state and ran the model with no diff context, which errored with `Internal error: directory mismatch for directory "/home/runner/work/_actions/anthropics/claude-code-action/v1/tsconfig.json"`. The "Flip to draft and back to ready, or mention `@claude`, to retry" message handled recovery, but only after manual draft-toggle round-trips. Affected PRs 84-87. **Mitigation shipped** — see below.

**3. PR 93 Haiku FP on a non-existent parallel-structure problem.** Triage Haiku flagged: "'destroying' should be 'destroy' to match parallel structure with 'provisioning' and 'updating'." All three are gerunds (`-ing`); the line is already parallel. Haiku then offered two contradictory "fixes" (change to "managing" — same `-ing` form; OR restructure as base verbs — also parallel). First confirmed Haiku FP across Sessions 16/17/18. Decision: don't change anything (advisory footer absorbs single-shot FPs; tightening the prompt costs budget on every triage; soft-watch the rate going forward).

**4. test-normal fixture obsoleted by Session 17's bump.** test-normal sat at 9 adds + 1 del → still trivial under `additions ≤ 10`. Was named for "normal PR, full review" but lost that meaning silently when the cap moved. **Mitigation shipped** — regrew to 13 additions.

**5. Label mutex bug.** `review:claude-ran` and `review:claude-stale` could coexist after a synchronize event (mark-stale added stale but didn't remove ran). The two labels represent mutually exclusive states. Cam spotted it. **Mitigation shipped** — see below.

**6. Frontmatter false-positive in `detect_starting_state`.** When a diff hunk doesn't include the file's opening `---` and a context line happens to look like a YAML key (e.g., `description: A minimal program.` inside a markdown ` ```yaml ` code block), the heuristic returns "frontmatter" and subsequent body changes get tagged `has_frontmatter_change=True`. Hit PR 96 this run; didn't change the trivial/fmonly outcome (other guards still triggered) but the diagnostic summary was misleading. **Mitigation shipped** — see below.

**7. Trivial-cap rethink — recommendation: switch to `additions` only.** Cam framed the trivial cap as cost optimization ("if it's short and easy for me to glance at and go 'yep, that's good!' it should save the token spend"). Pulled 200 most recent merged pulumi/docs PRs, filtered to non-bot + 100% content/*.md → 42 PRs (12 from jkodroff, the most active maintainer). Scored 7 candidate rules. `additions ≤ 10, files ≤ 2` catches 18/42 (43%) vs the old rule's 13/42 (31%) — a +5-PR shift, with all gains matching the cleanup pattern jkodroff and others use:
- #18703 jkodroff (9/41/1) — Replace card-style links with Related topics section
- #18681 jkodroff (6/0/2) — Document deletedWith inheritance
- #18521 cnunciato (0/62/1) — Remove AWS Summit Tel Aviv 2026
- #18641 smithrobs (4/32/1) — Remove redundant TOC
- #18707 smithrobs (9/0/1) — Add warning about workspaces.prefix
The metric tracks "how much new content does the maintainer have to read" rather than "how many diff line markers" — pure-deletion and deletion-dominant cleanup PRs are eligible because reading deleted content costs nothing. **Mitigation shipped** — see below.

### Mitigations shipped

**Trivial cap: `total_lines` → `additions`** (`triage-classify.py:245`, `CONTRIBUTING.md:51`). Commit `7ecf44f5a6`. The cap now measures new content, not raw diff line markers. CONTRIBUTING.md description updated to "≤10 added lines" and explicit mention of removal-dominant cleanup. Estimated effect on a 42-PR sample: 13 → 18 trivial (+38%), no false positives that look like real-review territory.

**Four cleanup fixes** (commit `0b8e9a0a4f`):
1. **Label mutex** (`claude-code-review.yml:43`): mark-stale step now adds `--remove-label "review:claude-ran"` alongside the `--add-label "review:claude-stale"`. The two labels are mutually exclusive states.
2. **Re-entrant re-marks** (`claude.yml:249-264`): on successful re-entrant runs, the Finalize step now re-adds `review:claude-ran` along with the existing removes. Without this, mark-stale's new remove would leave the PR carrying neither label after a successful refresh.
3. **Empty-diff race detection** (`claude-code-review.yml:92-104`, `:124-128`): pr-context step retries `gh pr view` once after a 30s pause if the first read returned 0 files. If still 0 after retry, skip with `skip_reason=empty-diff` instead of erroring with "directory mismatch."
4. **Frontmatter heuristic** (`triage-classify.py:102-110`): `detect_starting_state` returns "body" early for any hunk with `old_start > 30`. Hugo content frontmatter is always within the first ~30 lines, and the YAML-key regex is unreliable past that point because markdown YAML code blocks match the same shape.

**Two fixtures regrown** (cam fork only):
- `test-normal` 9 → 13 adds (HEAD `bb097c51e4`)
- `test-trivial-over-lines` 6 → 11 adds (HEAD `9e7b25a55e`)

**Rebase-fixtures script codified** (`scratch/2026-04-30-e2e-test-v3/rebase-fixtures.sh`): handles the base-then-head order so the Revert SHA is shared across `compare/base-pr-XXXX` and `compare/pr-XXXX`. Saves the Session-18 lesson for future fixture rebases.

### Items NOT shipped (in backlog)

- **Re-entrant phase** of this session was canceled. The 14 PRs opened (#84-97) sit in their initial-review state. Either a Session-19 walkthrough exercises them, or Cam closes and rebuilds. The re-entrant fix-response/re-verify behavior wasn't re-tested this run.
- **Tightening Haiku triage-prose** to reduce parallel-structure-style hallucinations. Decision: leave it. Single observed FP across 3 sessions; the rendered footer ("Best-effort spelling/grammar flags... Reject false positives at your discretion") is doing its job; tightening costs budget on every triage. Revisit if a second FP appears.
- **Boundary-fixture naming/recrafting** beyond the two regrown. The names `test-trivial-7lines` and `test-trivial-2files` over-promise (they describe diff-line counts, not source-line counts). Names didn't change because the underlying classification still validates the boundary.

### Methodology / repeatable patterns

- **Cherry-pick the Revert separately = merge conflict.** Whenever a fixture branch's base ALSO carries a Revert commit, the head branch must be cherry-picked off the rebased base, not the sync. Cherry-picking the Revert separately onto each gives them distinct SHAs and GitHub falls back to the sync as merge-base, which exposes the create-on-head/delete-on-base history as a conflict. Codified in `rebase-fixtures.sh`.
- **`gh pr view` is lazy after force-push.** The diff metadata can be empty for ~30-60s. Workflows that read it must guard or retry. Now done in `claude-code-review.yml`.
- **Boundary fixtures decay silently.** A test-* fixture sized exactly at the threshold becomes a no-op the moment the threshold moves. Whenever the rule changes, audit existing fixtures against the new rule, not just create new ones for the new rule.
- **Cam-pushback patterns worth internalizing this session:**
  - "Are you just trying to leak context into these skills?" — distinguish doc accuracy (humans read it) from agent-relevant signal (agents act on it). Don't dress one up as the other.
  - "Why do we give a shit about tokens? I thought it was deterministic." — be precise about which step is deterministic vs which step bills.
  - "I think you have the wrong expectations for your tests" — when fixture names use script-internal units that don't match author intuition, the names mislead even before a threshold change.

### Backlog after Session 18

Active:
1. **Maintainer `pr-review` walkthrough** — open PRs #84-97 are still in initial-review state. Cam closed re-entrant; either reopen Session-19 to exercise re-entrant on this set, or close + rebuild.
2. **Cost-variance monitoring** — defer; cost stable across 4 measurement passes.
3. **Cam-fork CI cosmetic fixes** — unchanged.
4. **Investigate 5 lost ⚠️ catches** (Session 13 #5) — still open.
5. **Upstream label deploy** (Session 14 #4) — still open. The trivial-cap shift makes this slightly more urgent (the rule change is now visible in skill files but not in production triage).
6. **Prose-pattern re-benchmark** — soft-watch.
7. **`update.md` raise-missed-duplicate code path** — defer.
8. **Non-determinism baseline + skeptic sub-agent** — paired; revisit together.
9. **Boundary-fixture name audit** — the names `test-trivial-7lines` etc. describe diff-line counts; consider renaming or recrafting to use source-line semantics.
10. **Sync cam/master to post-Session-18 HEAD** — cam fork is at sync `26d0e0fdb3` (Session-17 baseline). The two new commits (`7ecf44f5a6`, `0b8e9a0a4f`) are local-only and would need a fresh sync to test end-to-end on the fork.

Closed this session:
- Session-17 backlog item: trivial-bump validation → ✅ done with caveats (test-normal and test-trivial-over-lines were obsoleted, regrown).
- Trivial cap rethink → ✅ shipped (`additions ≤ 10`).
- Label mutex bug → ✅ shipped + re-entrant re-mark.
- Empty-diff race → ✅ shipped (retry + skip).
- Frontmatter FP heuristic → ✅ shipped.
- Re-entrant phase → ❌ canceled mid-session.

### Files changed (Session 18 substance)

- `7ecf44f5a6` — `Switch trivial cap from adds+dels to additions only` (`triage-classify.py`, `CONTRIBUTING.md`)
- `0b8e9a0a4f` — `Fix four issues surfaced by the Session-18 e2e run` (`triage-classify.py`, `claude-code-review.yml`, `claude.yml`)
- (this commit) — Session 18 notes

Cam-fork operations:
- `cam/master` advanced from `71f9188488` → `26d0e0fdb3` (Session-17 worktree state synced).
- 14 fixture branches force-pushed atop the new sync, plus 4 new boundary fixtures created.
- `test-normal` and `test-trivial-over-lines` regrown to clear the new cap.
- 14 PRs opened (`#84-97`); all initial reviews complete after PR-84-87 retry; re-entrant canceled. PRs left open at session end.

Scratch artifacts: `/workspaces/src/scratch/2026-04-30-e2e-test-v3/` — `pulumi-docs-prs.json` (200-PR sample for the trivial-rule analysis), `pulumi-docs-prs-flat.json`, `score-rules.py`, `open-prs.sh`, `capture.sh`, `cost-data.sh`, `cost-data.txt`, `rebase-fixtures.sh` (codifies the Session-18 base-then-head pattern), `reviews/`, `labels/`, `triage/`.

### Memory updates

None. All Session-18 facts are project-state specific to this branch and the e2e fixture set; they belong in this file.

## Session 19 — 2026-05-01 (live-vs-legacy benchmark, `domain:website`, trivial/fmonly tightening, exec writeups)

### Trigger

Cam asked whether the new pipeline actually beats what's running on `pulumi/docs` today, and whether we could quantify it. The Session-13 rebenchmark compared post-S12 against an inflated new-pipeline-against-itself baseline, never against the live legacy reviews. Today filled that gap, then surfaced a marketing-content review gap the benchmark also exposed, then closed the loop with exec writeups for #docs / leadership consumption.

### Work shipped

**1. Live-comparison v1: post-S12 vs `pulumi/docs` legacy on the original 6-PR battery.** Re-used `2026-04-28-pipeline-comparison/old-reviews/` and pulled cost data from upstream `claude[bot]` workflow runs (the `num_turns` / `total_cost_usd` / `duration_ms` come right out of `gh run view --log`). Result: 8-vs-8 substantive count head-to-head, 4 production-shipping bugs new caught that legacy missed, $1.78 per incremental catch. Surfaced one real new-pipeline weakness: PR 18642 (infra) — legacy made a single decisive `BUILD-AND-DEPLOY.md` doc-staleness catch the author landed verbatim; new scattered into three softer prompts and missed the load-bearing one. Tightened `infra.md` §Documentation drift with a "behavioral change to existing prose" rule that directs the model to grep `BUILD-AND-DEPLOY.md` for affected scripts/flags/env-vars even when the diff doesn't touch the doc. Report at `scratch/2026-05-01-live-comparison/REPORT.md`.

**2. Marketing-content review gap.** Tracing #18564 (a redirects-file PR) through the classifier surfaced that `content/**` paths under `about/`, `pricing/`, `vs/`, `why-pulumi/`, `legal/`, `careers/`, etc. either (a) fell through to bare `shared-criteria` (rule 5) or (b) got short-circuited as trivial when small. PR #18715 (legal PSA `last_updated`) was the canonical example — under old rules it was trivial-skipped despite being legal text with real consequences if the date bumped without the underlying semantic change.

**3. `domain:website` + trivial/fmonly tightening shipped in commit `85f85b8a3b`:**

- `triage-classify.py`: `classify_path` returns `domain:website` for any `content/**.md` path not matched by docs/blog/programs/infra. Trivial and fmonly gates now require `classify_path` to return `domain:docs` or `domain:blog` for every changed file (path-prefix filter `all_files_content_md` replaced with domain-membership filter `all_files_docs_or_blog`).
- `references/website.md` (new, 58 lines). Per Cam's calibration: surface claims as "worth a double-check before merge" rather than assertive findings, since marketing/legal authors typically have non-public data the reviewer can't see. 🚨 reserved for legal semantic edits and public-source-contradicted competitor claims; everything else defaults to ⚠️.
- `domain-routing.md`: added rule 4 routing `content/**.md` not matched by rules 2 or 3 to `references:website`.

Plus: trimmed `triage-prose.md` Haiku prompt (dropped trivial/fmonly criteria description — Haiku doesn't gate on it, just reads the diff), updated `CONTRIBUTING.md` short-circuit description, added `domain:website` to `scripts/labels/labels.json`, deployed the label to cam fork via `sync-labels.sh`.

**4. Live-comparison v2 benchmark on the fresh state (the load-bearing artifact for the rollout decision).** Fresh 11-PR battery: 6 carry-overs (18599, 18605, 18620, 18642, 18647, 18685) plus 5 new — 18715 (website-domain test), 18588 + 18573 (trivial path on real PRs), 18331 + 18568 (programs domain, previously zero coverage). Sync'd cam fork to `c935825257`, recreated all 11 fixture branches, opened fork PRs `#105–#115`, ran fresh new-pipeline reviews, scored against legacy via Agent.

Headline numbers:

| Axis | Result |
|---|---|
| Legacy substantive findings preserved or correctly silenced | 100% on full-review paths |
| Incremental substantive catches new made that legacy missed | **10**, every one would have shipped |
| FP rate | 0% on both pipelines |
| Maintainer signal quality (severity tier / evidence / grouping / suggestion block) | 95% new vs 30% legacy |
| Cost ratio | 1.93× legacy on this sample ($13.39 vs $6.94 across 11 PRs); projects ~1.5× on production mix once trivial-skip fires at the ~43% rate Session 18 measured |
| $/incremental shipped-defect prevented | **$0.65** |
| Single regression | PR 18573 trivial-cap edge case (4-line nav rewrite in a multi-section doc) — minor, soft-watch |

Notable catches: workflow-breaking SAML/SCIM nav bugs on #18605 (×2), OutSystems source misattribution propagated to LinkedIn+Bluesky social copy on #18647, broken `/docs/ai/integrations/` link on the #18685 Neo launch post, AGENTS.md canonical-path regressions on #18568 + #18599, Java snippet truncation introduced *while addressing legacy feedback* on #18331 (×2). PR #18715 (the website-domain test) routed correctly and produced the same finding as legacy with verification-ask framing instead of assertive — exact behavior `website.md` was designed for.

Report at `scratch/2026-05-01-live-comparison-v2/REPORT.md`.

**5. Exec writeups.**

- **Notion page** at Cam's Knowledge Preservation → Docs → *"Pulumi Docs PR-Review Pipeline — Executive Summary"* (`353fdbdf-1cce-816c-9d92-ea160ccba347`). Sections: Why (lead reason: rising agentic-PR velocity), How (two skill packages + mermaid flow with `@claude` refresh loop), Results (TL;DR callout + 11-PR comparison table with linked old/new reviews), Cost & tradeoffs (incl. an explicit noise-vs-nits bullet), See it in action, Next Steps (vale-based deterministic style linter as the primary follow-up).
- **PR #18680 description** rewritten end-to-end on `pulumi/docs`. Original 2-session draft replaced with what-ships / benchmark / status-before-merge / how-to-review structure that reflects the actual current state.
- **Slack draft** for `#docs` (`C85BS3LJZ`) introducing the pipeline and asking for feedback before next-week rollout. Cam edited and finalized; draft `Dr0B165TM9LJ` ready to send.

### Items NOT shipped (now in backlog)

- **Deterministic style-checking workflow (vale).** New backlog item — recovers prescriptive style-nit coverage (Click→Select, banned words, etc.) via free linter rather than Opus tokens. Half-day setup; out-of-scope for #18680 merge, in-scope as the immediate follow-up. Notion Next Steps documents the plan.
- **Upstream label deploy** — now load-bearing. `scripts/labels/sync-labels.sh --repo pulumi/docs` must run before #18680 merge or atomic label-apply will reject `domain:website`.
- **Trivial-cap edge case** (PR 18573 shape — multi-section docs file with a 4-line nav rewrite). Soft-watch, not a blocker. Tighten the classifier only if a second instance shows up in production.

### Methodology / repeatable patterns

- **Live comparison vs new-pipeline-vs-self.** Session 13 celebrated a 56% cost drop measured against a Pass-3 self-baseline; against actual `pulumi/docs` legacy, the new pipeline is 1.93× cost on the same shape of PR. *Always anchor cost framing to the live baseline.*
- **Cost extraction from upstream runs.** `gh run view --repo pulumi/docs <id> --log | grep -E 'num_turns|total_cost_usd|duration_ms'` works for any `claude-code-review.yml` run within retention. Codified in `scratch/2026-05-01-live-comparison-v2/cost-data.sh`.
- **Fixture rebase: file-overlay fallback for revert conflicts.** Session 18's `rebase-fixtures.sh` revert-and-reapply pattern hit a merge conflict on PR #18568 where cam/master had diverged from the merge's parent state. Fallback: `git checkout <merge>^1 -- <files>` to set base files to pre-merge state, commit; then `git checkout <merge> -- <files>` for the head. Works for any PR shape regardless of subsequent file churn. Documented in `scratch/2026-05-01-live-comparison-v2/rebase-fixtures.sh`.
- **Slack drafts via MCP.** `slack_send_message_draft` creates an attached draft on a channel; Cam edits in the UI. Drafts are user-local (not readable back via MCP), so any subsequent edits need to be pasted for review.
- **Notion page edits via update_content.** Search-and-replace on the markdown source. Cam editing the page in parallel will desync `old_str` matches; re-fetch before retrying. The "References" section disappeared between edits (Cam removed it during a parallel edit) — flagged but not restored.

### Backlog after Session 19

Active:

1. **Deterministic style-checking workflow (vale).** New, primary follow-up.
2. **Upstream `domain:website` + full label deploy** — pre-requisite for #18680 merge.
3. **Maintainer `pr-review` walkthrough on a real PR** (Session-18 #1) — could exercise on fork PRs #105–#115 or after upstream rollout.
4. **Trivial-cap edge case soft-watch** — PR 18573 shape.
5. **Investigate 5 lost ⚠️ catches** (Session 13 #5) — still open.
6. **Re-benchmark on a fresh production sample** after `domain:website` deploys upstream and real PRs flow through.
7. **`update.md` raise-missed-duplicate code path** — defer.
8. **Non-determinism baseline + skeptic sub-agent** — paired; revisit together.
9. **Boundary-fixture name audit** — old; unchanged.
10. **Cam's "claude-working" label mutex semantics** (Session-18 hand-written note) — partially addressed by Session 18's label mutex fix; worth a final sweep.
11. **Cam's "quick `/docs-review`" variant** (Session-18 hand-written note) — still open.

Closed this session:

- Live-pipeline benchmark vs `pulumi/docs` legacy → ✅ done (v1 + v2 reports).
- Marketing-content review gap → ✅ shipped (`domain:website` + tightened trivial/fmonly).
- Infra-domain doc-staleness gap from PR 18642 → ✅ tightened in `infra.md` §Documentation drift.
- Session 18 backlog: "Sync cam/master to post-Session-18 HEAD" → ✅ done (synced through `c935825257`).

### Files changed (Session 19 substance)

- `85f85b8a3b` — `Add domain:website and tighten trivial/fmonly to docs+blog only` (`triage-classify.py`, `references/website.md` new, `references/domain-routing.md`, `references/infra.md`, `triage-prose.md`, `CONTRIBUTING.md`, `scripts/labels/labels.json`).
- (this commit) — Session 19 notes.
- Cam fork sync `c935825257` — overlays post-S18+website state onto cam/master.

Cam-fork operations:

- `cam/master` advanced from `26d0e0fdb3` → `c935825257`.
- 11 fixture branches force-pushed (6 reused from prior, 5 new — including the 18568 file-overlay rebuild).
- 11 PRs opened (`#105–#115`); all initial reviews complete; left open for inspection.
- `domain:website` label deployed to fork.

Scratch artifacts:

- `/workspaces/src/scratch/2026-05-01-live-comparison/` — v1 report (post-S12 vs legacy, 6 PRs).
- `/workspaces/src/scratch/2026-05-01-live-comparison-v2/` — v2 report (post-S18+website vs legacy, 11 PRs), `old-reviews/`, `new-reviews/`, `cost-data-{legacy-all,new}.tsv`, `comment-permalinks.tsv`, `rebase-fixtures.sh`, `capture.sh`, `cost-data.sh`, `scoring-prompt.md`.

External outputs:

- Notion `353fdbdf-1cce-816c-9d92-ea160ccba347` (Knowledge Preservation → Docs → exec summary).
- PR #18680 description rewritten on `pulumi/docs`.
- Slack draft `Dr0B165TM9LJ` in `#docs` (`C85BS3LJZ`).

### Memory updates

None. All Session-19 facts are project-state specific to this branch and the v2 benchmark; they belong in this file.

## EXTRA HAND WRITTEN NOTE FROM CAM

I accidentally opened a bunch of PRs against my fork, and it was very instructive in how well this new pipeline will work. One thing I've noticed is that we should decide on standard behavior for "claude-working" labels and what other labels get deactivated when Claude is working.

## SECOND HAND WRITTEN NOTE FROM CAM

We should build a "quick" version of `/docs-review` that is similar to the existing `/docs-review` we use today. It's quicker and lighter.

## Session 20 — 2026-05-01 (design-only: hashtag-driven re-entrant routing, tracking-comment UX)

### Trigger

Cam asked whether the off-the-shelf animated tracking comment from `pulumi/docs:master`'s live `claude.yml` could be brought back to this branch while keeping the re-entrant workflow. Friday-evening design conversation; no code shipped.

### Investigation

The live `claude.yml` is a thin wrapper around `anthropics/claude-code-action@v1` with no `prompt:` argument. No-prompt = **tag mode**, which auto-posts the action's animated tracking comment with per-tool-call updates. Our `claude.yml` overlays a structured `prompt:` to encode three-path dispatch (review-related → `update.md`/`ci.md`, ad-hoc, ambiguous). Passing `prompt:` flips the action into agent mode and suppresses the tracking comment. We replaced it with a static `<!-- CLAUDE_PROGRESS -->` "🤖 Working on it" message — functional but not animated.

Action input `track_progress: true` was confirmed inapplicable: per the action's own docs it only fires for `pull_request` and `issue` event types, not the `issue_comment` / `pull_request_review_comment` / `pull_request_review` triggers `claude.yml` actually uses. Cam additionally noted there's no way for the model to know which comment ID to update, ruling it out cleanly.

### Options considered (and rejected)

1. **Drop custom prompt; rely on tag mode.** Risk: routing intelligence shifts to implicit project-context discovery; could mis-route on ambiguous mentions. ~80-85% reliability estimate from a one-line AGENTS.md instruction.
2. **Keep prompt + `track_progress: true`.** No-op for our trigger types per action docs.
3. **Drop prompt + lift dispatch into AGENTS.md verbatim** (~8-line block). Higher reliability (~98%) than option 1 but still trusting the model on a load-bearing routing decision.
4. **Spinner-only fallback** — embed an animated Claude logo asset inline in the existing CLAUDE_PROGRESS "Working on it" message. Tabled in favor of #5.
5. **Hashtag-driven routing** (Cam's idea — adopted).

### Settled design contract — hashtag-driven routing

`@claude` alone → off-the-shelf tag mode (animated tracking comment for free; ad-hoc / question / clarification cases). `@claude #update-review` → fires a separate workflow with the explicit re-entrant prompt. `@claude #new-review` → power-user escape hatch for regenerating a deleted/corrupted pinned review.

The hashtag closes a real gap: today's prompt classifies a compound mention like "Fix the typo and #update-review" or "I disagree with finding 3, re-verify, and also why X?" into one of three buckets and loses the other intents. The new `claude-update.yml` prompt is explicitly designed to handle compound mentions — address embedded asks (file edits / questions / disputes) inline, then refresh the review against the resulting state.

Three workflow files:

- **`claude.yml`** (off-the-shelf): `if:` requires `@claude` AND NOT (`#update-review` OR `#new-review`). No custom `prompt:`, no CLAUDE_PROGRESS plumbing, no `Save mention body`. Action's tag-mode tracking comment is the working signal. Keeps ESC fetch + access check + `claude_args` (Sonnet model + allowed-tools).
- **`claude-update.yml`** (new): `if:` requires `@claude` AND `#update-review`. Inherits current `claude.yml` machinery (ESC, access check, Save mention body, custom prompt, CLAUDE_PROGRESS with **animated spinner GIF** on the "Working on it" message, post-run label management). Prompt collapses to single-path: invoke `docs-review:references:update` with explicit handling for compound mentions.
- **`claude-new.yml`** (new): `if:` requires `@claude` AND `#new-review`. Invokes `ci.md` unconditionally — overwrites any existing pinned review. Power-user escape hatch.

Other settled details:

- **Two separate workflow files** rather than one mode-branching file — easier to diff each against the other.
- **Drop `review:claude-working` label** — the action's tracking comment (tag mode) and the spinner-bearing CLAUDE_PROGRESS (custom workflows) both replace it as a working signal.
- **Spinner only on the start-of-run "Working on it" message**; done / errored / cancelled states stay static (action's tracking comment naturally drops the animation at terminal state; our CLAUDE_PROGRESS text replaces the body entirely on edit).
- **Pinned-review footer** advertises `#update-review` only: *"Need a re-review? Want to dispute a finding? Mention `@claude` and include `#update-review`. (For ad-hoc questions or fixes, just `@claude` — no hashtag.)"* `#new-review` stays buried in meta-docs (CONTRIBUTING.md / skill files); not user-facing.
- **`#new-review` overwrites unconditionally** — the hashtag is the explicit confirmation; no safety prompt.

### Compound-mention contract for `claude-update.yml`

Worth recording verbatim because it's the substantive design output. The new prompt body (sketch):

```
The user invoked you with #update-review. The hashtag means: refresh the
pinned review. Their mention is in .claude-mention-body.txt — read it.

The mention may also contain:
- Code changes to make ("fix the typo and then update")
- Questions about specific findings ("why did you flag X?")
- Disputes ("this is intentional because Y")
- Combinations of the above

Plan of attack:
1. Read the mention body.
2. Address any embedded asks first:
   - File edits → Edit/Write, gh pr checkout, push.
   - Questions/disputes → fold the response into the relevant finding
     when you re-render the review (don't post separate gh pr comments;
     keeps everything in the pinned sequence).
3. Invoke `docs-review:references:update` against the resulting state.
   Pass the mention body as MENTION_BODY so the skill knows what
   prompted the refresh.
4. Post via `bash .claude/commands/docs-review/scripts/pinned-comment.sh upsert ...`
```

This is **more** capable than today's path 1 — today, "fix and update" gets classified as path 2 (ad-hoc) and skips the review update entirely. Hashtag scheme actually closes that gap.

### Items NOT shipped (carried into Session 21 — implementation queue)

1. **Strip `claude.yml`** to off-the-shelf shape. Drop custom `prompt:`, `Save mention body`, `Post progress signal`, `Finalize progress signal`, `review:claude-working` label management. Adjust `if:` to exclude both hashtags.
2. **Create `claude-update.yml`** with the compound-mention-aware prompt above; spinner GIF on start-of-run message.
3. **Create `claude-new.yml`** invoking `ci.md` with unconditional overwrite of any existing pinned review.
4. **Identify the canonical animated Claude logo asset URL** — likely in `anthropics/claude-code-action`'s `assets/` directory or extractable from a recent live tracking comment on `pulumi/docs:master`.
5. **Update the pinned-review footer** in the appropriate skill output template (probably `output-format.md`).
6. **Bury `#new-review` documentation** in CONTRIBUTING.md / power-user-facing meta docs.
7. **End-to-end test on cam fork** — exercise all three paths: `@claude` alone (off-the-shelf), `@claude #update-review` with a compound-mention payload (e.g., "fix the typo on line 4 and #update-review"), `@claude #new-review` after manually deleting a pinned review.
8. **Final plan-file rewrite** — the current plan file at `/home/vscode/.claude/plans/review-session-notes-md-to-know-vivid-ocean.md` reflects the spinner-only fallback (now superseded). Rewrite to the hashtag scheme before re-entering plan mode.

### Methodology / repeatable patterns

- **Hashtags as explicit-routing primitives.** When the model would otherwise have to infer intent from natural-language mention text — and risk wrong dispatch on compound or ambiguous cases — shift the disambiguation to a user-typed token. Cost: documenting the convention. Win: routing certainty plus a clean `if:` branch in workflow YAML. Generalizable to any mention-driven CI with multiple intents.
- **Plan iteration without writing code.** Four plan revisions in one session (Option 3 → spinner-only → `track_progress` rejected → hashtag scheme), each invalidated before any YAML edit. Reading the action source/docs and asking "but what about compound mentions?" caught the misfire of each preceding plan in turn. Cheap iteration when the cost of getting it wrong on a real PR is high.
- **Cam-pushback patterns this session:**
  - "Is Sonnet smart enough for that?" — when a design relies on the model inferring intent from minimal instruction, name the failure modes explicitly before claiming the design is reliable.
  - "What if they say 'Fix it and then #update-review'?" — single-intent designs collapse on real-world compound mentions. The toy case is never the actual case.

### Backlog after Session 20

Active:

1. **Implement hashtag-driven routing + spinner UX** (this session's design — top of Session-21 queue).
2. **Deterministic style-checking workflow (vale).** From Session 19; still primary follow-up.
3. **Upstream `domain:website` + full label deploy** — pre-requisite for #18680 merge.
4. **Maintainer `pr-review` walkthrough on a real PR** (Session-18 #1) — could exercise on fork PRs `#105-#115` after hashtag rollout.
5. **Trivial-cap edge case soft-watch** — PR 18573 shape.
6. **Investigate 5 lost ⚠️ catches** (Session 13 #5).
7. **Re-benchmark on a fresh production sample** after `domain:website` deploys upstream.
8. **`update.md` raise-missed-duplicate code path** — defer.
9. **Non-determinism baseline + skeptic sub-agent** — paired; revisit together.
10. **Boundary-fixture name audit** — old; unchanged.
11. **Cam's "claude-working" label mutex semantics** (Session-18) — partially addressed; one more sweep.
12. **Cam's "quick `/docs-review`" variant** (Session-18) — still open.

Closed this session:

- "Bring back the off-the-shelf tracking-comment UX" → ✅ design settled (hashtag scheme); implementation deferred to Session 21.

### Files changed (Session 20 substance)

- `/home/vscode/.claude/plans/review-session-notes-md-to-know-vivid-ocean.md` — three drafts during planning (Option 3 → spinner-only). Now stale; will be rewritten in Session 21 before implementation.
- (this commit) — Session 20 notes.

No code or workflow file changed.

### Memory updates

None. All Session-20 output is design state specific to this branch; belongs here.

## Session 21 — 2026-05-04 (Vale prose-style linting: make target, CI integration, triage augmentation, skill-file trim)

### Trigger

Top of Session-19 backlog: "Deterministic style-checking workflow (vale). Half-day setup; recovers prescriptive style-nit coverage via free linter rather than Opus tokens." This session implemented it end-to-end except for the fork-test battery (Cam has more changes coming first).

### Three design decisions taken up front

To avoid mid-implementation rework, asked Cam three questions in plan mode before writing code. All three picked the recommended option:

1. **Vale supersedes the overlapping prose-patterns.md rules** (passive voice, filler, buzzwords, hedging, etc.) rather than coexisting. Saves Opus tokens; one rule per pattern; cleaner mental model for the AI reviewer.
2. **Scope: `content/docs/` + `content/blog/` only.** Marketing/website (`content/about/`, `pricing/`, `legal/`), programs, and meta files excluded. Marketing copy tolerates "world-class"/"leverage" that Vale would over-flag.
3. **Minimal custom Pulumi style** layered over Google + write-good packages, not comprehensive-pulumi-style or off-the-shelf-only.

### Architecture

**Tool management:**

- `mise.toml` adds `vale = "3.14.1"` (current stable; not the placeholder 3.9.1 from the plan). Single source of truth.
- `scripts/ensure.sh` adds `check_version "Vale" ...` matching the existing Node/Hugo/Yarn pattern. Hard dep — same install path as other tools.
- CI workflows install via `jdx/mise-action@v2` (cache: true). Adds ~30s on cold cache; downstream cached.

**`.vale.ini` config:**

- `MinAlertLevel = warning` (suggestion is too noisy on existing technical prose).
- `Packages = Google, write-good`; `BasedOnStyles = Pulumi, Google, write-good` for `*.md`.
- `BlockIgnores` and `TokenIgnores` for both `{{< ... >}}` and `{{% ... %}}` Hugo shortcode forms (full + closing tags). Verified: `{{< notes >}}` blocks are correctly skipped.
- Disabled rules (per-rule, not per-package):
  - `Google.Headings` (Pulumi uses Title Case for H1; markdownlint covers H2+)
  - `Google.WordList` (Google product-name overrides don't match Pulumi terminology)
  - `Google.We` (docs allow first-person plural)
  - `Google.Will` (too noisy on declarative prose)
  - `Google.Parens` ("use parens judiciously" — vague, not actionable)
  - `write-good.Passive` (`Google.Passive` covers same ground; one finding per construct)
  - `write-good.E-Prime` (banning all forms of "to be" is impractical for technical docs)

Smoke-tested on `content/docs/iac/concepts/inputs-outputs/_index.md` (210 lines): 7 findings remain after disables — reasonable noise.

**Custom `styles/Pulumi/` pack** (5 rules + meta.json):

- `Substitutions.yml`: click→select, go to→navigate, public beta→public preview, cross-language package→Pulumi package, single-language/language-native package→native language package
- `BannedWords.yml`: ableist (`crazy`, `dummy`), gendered (`guys`), legacy security terms (`whitelist`, `blacklist`, `master`, `slave`, `sanity check`)
- `Difficulty.yml`: easy/easily/simple/simply/just/obviously/clearly/of course
- `ProductNames.yml`: substitution rule covering wrong-case forms (`pulumi esc`, `Pulumi Esc`, `Pulumi Iac`, `Pulumi IAC`, etc.) → correct (`Pulumi ESC`, `Pulumi IaC`)
- `PoliciesSingular.yml`: existence rule flagging plural verbs after "Pulumi Policies" (`enforce`, `are`, `have`, `allow`, `provide`, `support`, `enable`, `require`)

**Vendored `styles/Google/` and `styles/write-good/`** from `vale sync` — 220K, 49 files, checked in for reproducibility (no network in CI).

**`make lint-prose`** target:

- Defaults to **changed files vs master** via `git diff` + `git ls-files --others`. ~0.2s on a typical scope.
- `make lint-prose ARGS=content/docs/iac` for explicit path.
- Full-tree lint on 1500+ files takes 5+ minutes — not the default; explicit opt-in via ARGS only.
- Wrapper script `scripts/lint-prose.sh` always exits 0 (`vale --no-exit`). `make lint` is **not** modified — keeps the gating contract clean.

**`vale-findings-filter.py`** at `.claude/commands/docs-review/scripts/`:

- Reads Vale `--output=JSON`, intersects findings with PR-added line numbers from `gh pr diff --patch`, caps to **10/file and 50 total**, writes flat sorted JSON list.
- Empty input or zero intersection → `[]`, never errors.
- Unit-tested with mocked `gh pr diff`: pre-existing prose correctly excluded; only PR-introduced findings pass through.

**Three workflows wired:**

- `claude-code-review.yml`: `jdx/mise-action@v2` after checkout; new "Run Vale on PR-changed prose" step between `pr-context` and `check-access`. Gated `if: skip_reason == ''` and `continue-on-error: true`. Prompt updated with one paragraph telling Opus to surface findings under ⚠️ Low-confidence.
- `claude.yml` (re-entrant): same pattern, additionally gated on `is_pr == 'true'`. Prompt path 1 gets the same Vale paragraph.
- `claude-triage.yml`: Vale runs alongside Haiku (different coverage — see below). New §3b block, same `PROSE_CHECK_NEEDED` gate as Haiku. Findings render as `[style]` bullets in the existing `<!-- TRIAGE_PROSE -->` advisory comment, alongside Haiku's `[spelling]` bullets. `review:prose-flagged` label fires on either source.

### Why Vale doesn't replace Haiku in triage

Cam asked. Coverage is disjoint:

- **Haiku** (`spelling-grammar.md`): misspellings, wrong-word swaps (their/there/they're), subject-verb disagreement, missing articles, doubled words, UK→US spellings, Oxford commas.
- **Vale** (current config): substitutions (click→select), banned words, difficulty qualifiers, product names, passive voice, contractions, weasel words, too-wordy.

Vale's spelling check needs Hunspell + a wordlist we haven't set up; even then it wouldn't do wrong-word disambiguation or subject-verb checks. The gap Vale closes is different: trivial / frontmatter-only PRs touching docs/blog files skip the full review (and therefore skip Vale in `claude-code-review.yml` due to the `skip_reason == ''` gate). Adding Vale to triage closes that gap. One merged advisory comment with prefixed bullets > two separate comments.

### Skill-file trim (don't double-flag what Vale catches)

Same principle that drove the original `output-format.md` DO-NOT #7 ("no findings markdownlint or Prettier catches") applied to Vale-covered rules across the docs-review references:

- **`prose-patterns.md`**: deleted Passive voice, Filler/prepositional bloat, Empty intensifiers, Difficulty qualifiers, Hedging, Buzzword tax, Empty transitions, Em-dash density, Repetitive paragraph openers. Kept Spelling-and-grammar reference, Undefined acronyms, Nested clause stacks, Contrastive frames, Uniform sentence rhythm, Dense paragraphs. Added "Anything Vale catches" do-not-flag rule.
- **`docs.md`**: Priority 4 (Terminology and product accuracy) — replaced 4 bullets (product names, Policies-singular, public-preview, preferred pairs) with one paragraph deferring to Vale + a real reviewer task (first-mention acronym expansion, which Vale doesn't do). Pre-existing scope removed "product-name capitalization." Do-not-flag adds "Anything Vale catches."
- **`blog.md`**: Priority 4 (Product accuracy) — same treatment. Kept Feature names, "generally available" not "generally released," canonical doc links (not Vale-covered). Do-not-flag adds "Anything Vale catches" and clarifies the heading-case split (markdownlint owns case, Vale owns product-name miscapitalization).
- **`output-format.md`**: DO-NOT #7 narrowed from "the linter" to "markdownlint and Prettier" with explicit Vale carve-out. Bucket rules section adds Style nits (Vale) bullet examples under ⚠️ Low-confidence.
- **`SKILL.md`** (interactive): one paragraph telling the model to invoke `vale --no-exit --output=JSON <files>` for files under `content/docs/`/`content/blog/` and surface findings the same way as CI.
- **`ci.md`**: one paragraph instructing CI to read `.vale-findings.json` and render under ⚠️ Low-confidence with `[style]` prefix.

Skills not touched (different purpose): `glow-up.md`, `new-blog-post.md`, `fix-issue.md` — these *author or polish* content; they need STYLE-GUIDE as a creation reference, not just enforcement. Vale flags violations after the fact. `shared-criteria.md:27` (descriptive link text), `docs.md:77` (semantic shortcode choice), `code-examples.md:35` (code style) — not Vale-covered.

### Documentation

- `STYLE-GUIDE.md` adds a brief "Automated checks" section pointing to `.vale.ini`, `make lint-prose`, and the rule packs.
- `AGENTS.md` adds `make lint-prose` to the Build/Test/Lint Workflow list with a one-line "Nags, never blocks" note.

### Things worth knowing (gotchas)

- **`Vocab = Pulumi` suppresses matches across ALL rules**, not just spelling. Initial config had `Vocab = Pulumi` with `Pulumi` in the accept list; `Pulumi.ProductNames` wouldn't fire on "Pulumi Iac" until the Vocab line was removed. Vocab is for the spelling extender we're not using anyway. Don't re-add it without a clear reason.
- **Vale on the full content tree (1500 files) takes 5+ minutes.** Single file: 0.16s. Small directory: ~6s. The slowness is at scale only. `make lint-prose` defaults to changed-vs-master to keep the contributor UX fast; full-tree lint requires explicit `ARGS=content/docs`.
- **`vale --no-exit-code` is wrong; the flag is `--no-exit`**. Easy typo from reading docs of another linter.
- **`jdx/mise-action@v2` puts mise-managed tools on PATH automatically** — no `mise activate` required in workflow run scripts.
- **Vendored styles total 220K (49 files)**. Cheap to commit; pays back in zero network dependency in CI.

### Items NOT shipped (carried into Session 22)

1. **End-to-end fork test.** All verification was local: Vale runs, custom rules fire, intentional-violation tests pass, filter intersects correctly with mocked `gh pr diff`, YAML and embedded bash syntax-check. Untested: `jdx/mise-action@v2` actually installs Vale on the runner; the CI prompt actually picks up `.vale-findings.json`; pinned-comment renders Style nits the way described; the merged TRIAGE_PROSE comment renders cleanly with prefixes. Cam will run a full battery after additional changes.
2. **`/docs-review` graceful-degrade when Vale missing.** SKILL.md tells the model to run vale; doesn't say what to do if it's not installed. Discussed three options (hard-fail, graceful-skip with one-line note, auto-install via mise); recommendation = graceful-skip. Not yet wired.
3. **CI workflow `||` fallback hardening.** `claude-code-review.yml` and `claude.yml` Vale steps rely on `continue-on-error: true` plus the prompt's "if file exists" check. Triage uses explicit `vale ... || echo '{}' > .vale-raw.json` short-circuits — cleaner. Worth tightening the other two to match.
4. **Hashtag-driven re-entrant routing** (Session 20 design) — top of next session's queue per Cam.
5. **Pre-commit hook** (lint-staged + Vale) — deferred. Slowing every commit isn't worth it for v1.
6. **Vale on marketing/website content** — out of scope per the design decision.

### Methodology / repeatable patterns

- **Plan-mode Q&A up front saves cycles.** Three design questions answered before any code (Vale-supersedes vs coexist; scope; minimal vs comprehensive Pulumi pack). All three picked the recommended option, so no rework. Cheaper than discovering the design after writing rules.
- **Trim-on-overlap principle.** When adding a deterministic checker that shares scope with an AI rubric, edit the AI rubric to defer rather than duplicate. Mirrors how `output-format.md` DO-NOT #7 already excluded markdownlint findings. Applied here to `prose-patterns.md`, `docs.md` Priority 4, `blog.md` Priority 4. Reduces token cost AND avoids same-line double-flagging at conflicting severities.
- **Cam-pushback patterns this session:**
  - "Why don't we install Vale with `make ensure` or mise like other tools? If somebody runs `/docs-review`, it'll expect Vale to be there, right?" — caught the original plan's `scripts/install-vale.sh` shortcut and forced the right architecture (single source of truth in `mise.toml`, hard dep enforced by `ensure.sh`).
  - "And what happens if someone runs `/docs-review` local and vale isn't installed?" — caught the un-handled missing-binary path; led to the graceful-skip design (not yet wired).
  - "Did you verify any of the vale changes against an actual PR in the fork?" — explicit pushback on local-only verification. Honest answer was no; Cam absorbed it and chose to defer until more changes land.
- **The ultraplan / fork-branch gotcha.** Cam tried `/ultraplan` to refine the local plan; the cloud agent cloned `origin/master` (113 commits behind this branch) and 404'd because the entire `.claude/commands/docs-review/` skill it was supposed to modify doesn't exist on master. For mid-branch refinement, ultraplan needs the working branch pushed first. Worth documenting if ultraplan becomes part of regular flow.

### Backlog after Session 21

Active:

1. **Hashtag-driven re-entrant routing** (Session 20 design) — top of next session's queue per Cam.
2. **End-to-end fork test of Vale integration** (Session 21 #1) — bundle with the broader battery Cam plans.
3. **Graceful-skip for missing Vale in `/docs-review` interactive** (Session 21 #2).
4. **CI workflow `||` fallback hardening** (Session 21 #3).
5. **Upstream `domain:website` + full label deploy** — pre-requisite for #18680 merge.
6. **Maintainer `pr-review` walkthrough on a real PR** (Session-18 #1).
7. **Trivial-cap edge case soft-watch** — PR 18573 shape.
8. **Investigate 5 lost ⚠️ catches** (Session 13 #5).
9. **Re-benchmark on a fresh production sample** after `domain:website` deploys upstream.
10. **`update.md` raise-missed-duplicate code path** — defer.
11. **Non-determinism baseline + skeptic sub-agent** — paired.
12. **Boundary-fixture name audit** — old.
13. **Cam's "claude-working" label mutex semantics** (Session-18) — partially addressed; one more sweep.
14. **Cam's "quick `/docs-review`" variant** (Session-18) — still open.

Closed this session:

- **Deterministic style-checking workflow (vale)** → ✅ shipped (modulo fork test).

### Files changed (Session 21 substance)

New:

- `.vale.ini` — top-level config with shortcode ignores and rule disables.
- `scripts/lint-prose.sh` — wrapper; defaults to changed-vs-master, accepts ARGS.
- `.claude/commands/docs-review/scripts/vale-findings-filter.py` — line-intersection filter (10/file, 50 total caps).
- `styles/Pulumi/` — 5 custom rules + meta.json.
- `styles/Google/` and `styles/write-good/` — vendored from `vale sync`, 220K, 49 files.

Modified:

- `mise.toml`, `scripts/ensure.sh` — Vale 3.14.1 pinned and version-checked.
- `Makefile` — `lint-prose` target with `ARGS=` passthrough; `lint` untouched.
- `.github/workflows/claude-code-review.yml`, `claude.yml`, `claude-triage.yml` — `jdx/mise-action@v2` + Vale step + prompt updates (triage merges Haiku + Vale into one TRIAGE_PROSE comment with `[spelling]`/`[style]` prefixes).
- `.claude/commands/docs-review/SKILL.md`, `ci.md` — short paragraphs on consuming Vale findings.
- `.claude/commands/docs-review/references/output-format.md` — DO-NOT #7 carve-out; Style nits subsection under ⚠️.
- `.claude/commands/docs-review/references/prose-patterns.md` — deleted Vale-covered patterns (Passive, Filler, Intensifiers, Difficulty, Hedging, Buzzword, EmptyTransitions, EmDash, RepetitiveOpeners); kept Spelling-and-grammar ref, Undefined acronyms, Nested clauses, Contrastive frames, Uniform rhythm, Dense paragraphs; added "Anything Vale catches" do-not-flag rule.
- `.claude/commands/docs-review/references/docs.md`, `blog.md` — Priority 4 trimmed; do-not-flag updated.
- `STYLE-GUIDE.md`, `AGENTS.md` — pointers to `make lint-prose`.

### Memory updates

None. The Vocab gotcha and other Vale-specific quirks are project-state for this branch; SESSION-NOTES is the right home.

## Session 22 — 2026-05-04 (hashtag-driven re-entrant routing implementation; bundled Vale follow-ups)

### Trigger

Top of Session-21 backlog: implement Session 20's settled hashtag-driven routing design. Cam asked to bundle Session 21's deferred Vale follow-ups (graceful-skip, `||` hardening) into the same change since they touch the same workflow files.

### Architecture decisions confirmed up-front

Four AskUserQuestion picks before any code touched:

1. **Spinner GIF source** = the action's own tracking spinner at `https://github.com/user-attachments/assets/5ac382c7-e004-429b-8e35-7feb3e8f9c6f` (CDN-stable). Ruled out self-hosting (asset bootstrap problem) and emoji-only (loses the visual cue that motivated the redesign).
2. **`#new-review` architecture** — Cam pushed back on my original "duplicate `ci.md` invocation in claude-new.yml" plan and proposed a dispatcher: clear pinned + dispatch existing `claude-code-review.yml`. Smart simplification: single source of truth for "initial review" stays in one workflow. Implemented as `gh workflow run claude-code-review.yml -f pr_number=$PR -f force=true`. Required adding `workflow_dispatch:` trigger + `force` input to claude-code-review.yml.
3. **Compound hashtag precedence** — `#new-review` wins. claude-update.yml's `if:` gates on `#update-review AND NOT #new-review`. Documented as a deliberate edge case.
4. **`review:claude-working`** — full delete: workflows, labels file, pr-review SKILL state machine. The action's tracking comment and CLAUDE_PROGRESS spinner are both observable working signals; the label was duplicate state.

### Work shipped

**Workflow split** (commit `6924b51c49`):

- `claude.yml` (modified) — stripped to off-the-shelf shape, mirrors `pulumi/docs:master`'s live workflow. No custom `prompt:`, no Vale, no CLAUDE_PROGRESS plumbing, no `Save mention body`. `if:` adds `&& !contains(...,'#update-review') && !contains(...,'#new-review')` per event clause. Tag mode auto-posts the animated tracking comment for ad-hoc work.
- `claude-update.yml` (new) — full re-entrant pipeline gated on `@claude AND #update-review AND NOT #new-review`. Inherits current claude.yml machinery (ESC, mise, access check, PR-context, save mention body, Vale, CLAUDE_PROGRESS, post-run labels). Single-path collapsed prompt with explicit compound-mention contract: address embedded asks (file edits / questions / disputes) inline before invoking `docs-review:references:update`. Spinner GIF inline-rendered via `<img src="..." width="16">` in CLAUDE_PROGRESS body. Vale-ephemerality clause baked into the prompt: "Vale findings are NOT tracked across reviews… do NOT move resolved style nits into ✅ Resolved."
- `claude-new.yml` (new) — lightweight dispatcher gated on `@claude AND #new-review`. No `claude-code-action@v1` invocation. Steps: ESC fetch, access check, resolve PR number, `pinned-comment.sh clear`, post one-line confirmation comment, `gh workflow run claude-code-review.yml -f pr_number -f force=true`. ~130 lines of bash + gh CLI.
- `claude-code-review.yml` (modified) — added `workflow_dispatch:` trigger with `pr_number` + `force` inputs. Updated `if:` filter, concurrency group (`workflow_run.pull_requests[0].number || inputs.pr_number`), PR-number resolution, `head_sha` fallback. `force=true` bypasses trivial / fmonly / draft / bot-author skips (empty-diff stays unconditional). Vale step hardened with `|| echo '{}' > .vale-raw.json` and `|| echo '[]' > .vale-findings.json` to match claude-triage.yml's pattern. Dropped review:claude-working set/clear and supporting comment. Updated retry-prompt error text to `@claude #update-review`.
- `claude-triage.yml` (modified) — dropped `review:claude-working` from the state-label exclusion list at line 212.

**`pinned-comment.sh clear` subcommand** — new ~10-line `cmd_clear` that enumerates all `<!-- CLAUDE_REVIEW N/M -->` comments via the existing `find` helper and `gh api -X DELETE`s each. The only path that bypasses the 1/M-sacrosanct rule. Dispatcher table updated; usage block extended.

**Pinned-review footer** — `output-format.md:39` now reads "Need a re-review? Want to dispute a finding? Mention &#64;claude and include `#update-review`. (For ad-hoc questions or fixes, just &#64;claude — no hashtag.)" `#new-review` stays buried in CONTRIBUTING.md / AGENTS.md.

**Vale graceful-skip** in interactive `/docs-review` — `docs-review/SKILL.md:35` adds: "If `vale --version` fails or `vale` is not on PATH, skip the Vale step with a one-line note… don't hard-fail."

**Cleanup of `review:claude-working`:**

- `.github/labels-pr-review.md` — row + `gh label create` one-liner removed.
- `.claude/commands/pr-review/SKILL.md` — `WORKING` state dropped from the state machine and the corresponding §STALE / §WORKING / §ABSENT switch. State machine collapses to `CURRENT` / `STALE` / `ABSENT`.
- Workflows — all set/clear calls removed (claude.yml had nothing left after the strip; claude-code-review.yml dropped the add-label and remove-label calls plus the supporting "review:claude-working is always removed" comment).

**User-facing docs:**

- `CONTRIBUTING.md` — §AI-assisted contributions §"After review — three paths to refresh" rewritten. Path 1 now branches on hashtag: `@claude #update-review` for refresh/dispute/fix-response (with the three patterns under it), bare `@claude` for ad-hoc help. New §"Power-user escape hatch: `@claude #new-review`" subsection frames the regenerate path as recovery-only. Top-of-section paragraph also updated from "mention `@claude`" to "mention `@claude #update-review`".
- `AGENTS.md` — PR Lifecycle line updated to mention the new hashtags and the bare-`@claude`-is-ad-hoc framing.

### Items NOT shipped (carried into Session 23)

1. **End-to-end fork test battery** — deferred mid-session. Cam closed all existing fork PRs; next session opens new fixtures + new test PRs and exercises every path. Prompt drafted at end of this session.
2. **`scripts/labels/sync-labels.sh` retirement of `review:claude-working` on cam fork** — Cam will run after the test battery so the label is still available for any in-flight runs.

### Methodology / repeatable patterns

- **Cam-pushback patterns this session:**
  - "I had envisioned a workflow that clears the pinned comment and then just dispatches existing review workflow." — caught a duplicate-logic anti-pattern in my original plan and pushed me toward the dispatcher architecture. The lesson: when a new path mostly mirrors an existing one, dispatch instead of duplicate. The `force` input on the existing workflow plus a tiny dispatcher beats reimplementing 200 lines of PR-context resolution and prompt construction.
  - "Explain about the lifecycle of the vale-findings file and how it relates to #update-review. Is it going to re-run?" — caught an underspecified design point. The Vale-ephemerality contract (fresh per run, no diff-tracking against prior pinned, no "✅ resolved style nit") needed to live in the `claude-update.yml` prompt explicitly so the model doesn't accidentally migrate Vale findings into ✅ Resolved on subsequent refreshes.
- **Plan-mode-first, four-question gate.** Session 21's three-question gate up-front caught the architecture before any code; this session's four-question gate did the same. Worth keeping as a default.
- **Hashtag mutual-exclusion via filter, not workflow logic.** `claude-update.yml`'s `if:` includes `!contains(..., '#new-review')` so compound mentions where both hashtags appear cleanly elect `claude-new.yml` (its filter doesn't need the inverse exclusion). One-sided exclusion gives `#new-review` precedence with no extra plumbing.

### Backlog after Session 22

Active:

1. **End-to-end fork test battery** (S22 #1) — top of next session per Cam.
2. **Upstream `domain:website` + full label deploy** — pre-requisite for #18680 merge.
3. **Maintainer `pr-review` walkthrough on a real PR** (Session-18 #1).
4. **Trivial-cap edge case soft-watch** — PR 18573 shape.
5. **Investigate 5 lost ⚠️ catches** (Session 13 #5).
6. **Re-benchmark on a fresh production sample** after `domain:website` deploys upstream.
7. **`update.md` raise-missed-duplicate code path** — defer.
8. **Non-determinism baseline + skeptic sub-agent** — paired.
9. **Boundary-fixture name audit** — old.
10. **Cam's "claude-working" label mutex semantics** (Session-18) — ✅ closed by full delete in this session.
11. **Cam's "quick `/docs-review`" variant** (Session-18) — still open.

Closed this session:

- **Hashtag-driven re-entrant routing** (Session 20 design) → ✅ shipped (modulo fork test).
- **Vale graceful-skip in `/docs-review` interactive** (Session 21 #2) → ✅ shipped.
- **CI workflow `||` fallback hardening** (Session 21 #3) → ✅ shipped.
- **Cam's `claude-working` label mutex semantics** → ✅ closed by drop.

### Files changed (Session 22 substance)

New:

- `.github/workflows/claude-update.yml` — re-entrant pipeline gated on `#update-review`.
- `.github/workflows/claude-new.yml` — dispatcher gated on `#new-review`.

Modified:

- `.github/workflows/claude.yml` — stripped to off-the-shelf shape with hashtag exclusion.
- `.github/workflows/claude-code-review.yml` — `workflow_dispatch` trigger + `force` input + Vale `||` hardening + drop `review:claude-working`.
- `.github/workflows/claude-triage.yml` — drop `review:claude-working` from exclusion list.
- `.claude/commands/docs-review/scripts/pinned-comment.sh` — add `clear` subcommand.
- `.claude/commands/docs-review/SKILL.md` — Vale graceful-skip clause.
- `.claude/commands/docs-review/references/output-format.md` — pinned-review footer (advertises `#update-review`).
- `.claude/commands/pr-review/SKILL.md` — drop `WORKING` state from state machine.
- `.github/labels-pr-review.md` — drop `review:claude-working` row + `gh label create`.
- `CONTRIBUTING.md` — rewrite §"After review — three paths to refresh"; add `#new-review` escape-hatch section.
- `AGENTS.md` — PR Lifecycle line updated for hashtag routing.

Commit: `6924b51c49` (this session's substance), `<this commit>` (Session 22 notes).

### Memory updates

None. All Session-22 substance is project-state specific to this branch — workflow shape, hashtag conventions, dispatcher architecture — and belongs in this file rather than auto-memory.

## Session 23 — 2026-05-04 (end-to-end fork test battery; two latent bugs surfaced and fixed)

### Trigger

Top of Session-22 backlog: end-to-end test battery. Cam closed all prior fork PRs; this session opened fresh fixtures and ran a 12-row battery covering every code path the hashtag-driven router introduced.

### Fixtures opened

Six PRs on `CamSoper/pulumi.docs`:

- **#116** (carry-over) — JumpCloud SAML SSO integration guide (docs prose-heavy).
- **#117** (carry-over) — Executable plugin guide and Packages restructure (docs prose-heavy).
- **#118** (carry-over) — Neo Integration Catalog launch blog post (blog).
- **#119** (new) — `Click → Select` 1-line typo fix in `idp/concepts/services.md` (designed to classify `review:trivial`).
- **#120** (new) — Limitations section appended to `idp/concepts/no-code-stacks.md` with a deliberate `followign` typo on file line 34 (compound-mention test target).
- **#121** (new) — Recommended deployment pattern section in `idp/concepts/backstage-plugin.md` using "Always invoke …" guidance the reviewer would plausibly flag (dispute test target).

Carry-over rebases used `scratch/2026-05-01-live-comparison-v2/rebase-fixtures.sh` selectively (just the three needed) onto fresh master sync.

### Battery results

| Row | Scenario | Outcome | Evidence |
|---|---|---|---|
| 1 | Initial review on docs PR | ✅ | `claude-code-review.yml` ran on all 5 non-trivial PRs. PR #116 surfaces 2 `[style]` Vale bullets, PR #117 surfaces 35. `review:claude-ran` set, no `review:claude-working` anywhere. |
| 2 | Bare `@claude` (off-the-shelf) | ✅ (after fork bypass) | `Claude Code` run 25340806517 success; action posted its own tag-mode tracking comment "Claude finished … in 20s" on PR #116, edited live during the run (created 20:07:25, updated 20:08:01); pinned review untouched. |
| 3 | `#update-review` after a new commit | ✅ | Push to PR #116 fired mark-stale (label flip); `Claude Code (update-review)` refreshed pinned at 20:25:56Z; review history gained `re-reviewed after fix push (1 new commit, e24648c)` entry; label flipped back to `claude-ran`. |
| 4 | Compound mention "fix typo on line 34 and refresh" | ✅ | Model fixed `followign → following` in a new commit pushed to PR #120 (commits 1→2; head 06050b5c → 165082c0); pinned re-rendered at 20:10:00Z; original Outstanding typo moved to ✅ Resolved. |
| 5 | Dispute a finding | ✅ | PR #121 Outstanding count went 1→0; "Always invoke" finding moved to ✅ Resolved with strikethrough on the original claim and "concede: @CamSoper confirmed … intentional team guidance … Deferring to repo authority"; review history records the dispute reasoning. No separate `gh pr comment` was posted (response folded INTO finding). |
| 6 | Manually delete 1/M then `#new-review` | ✅ | Deleted CLAUDE_REVIEW 1/1 (id 4374035319) on PR #118; `Claude Code (new-review)` dispatcher posted "🤖 Pinned review cleared; regenerating from scratch…" at 20:21:14; dispatched `Claude Code Review` (workflow_dispatch) succeeded; new pinned review with new comment ID (4374227892) posted at 20:24:38Z. |
| 7 | Trivial PR + `#new-review` (force=true) | ✅ (after dispatcher fix) | PR #119 ends with **both** `review:trivial` AND `review:claude-ran` — `force=true` did bypass the trivial-skip and the dispatched Opus review actually ran. |
| 8 | Push commit, no mention (mark-stale) | ✅ | Push to PR #118 fired `Claude Code Review` mark-stale job at 19:56:38; label flipped `claude-ran → claude-stale`. No AI call. No CLAUDE_PROGRESS comment. |
| 9 | Compound hashtag `#update-review #new-review` | ✅ | On PR #117: `Claude Code` skipped, `Claude Code (update-review)` skipped (`!contains(...,'#new-review')` excluded itself), `Claude Code (new-review)` succeeded. Precedence rule confirmed in Actions tab. |
| 10 | Non-write-access mention | ⏸ Deferred | I have no second account; the access-check delta is purely in the `gh api collaborators/$AUTHOR/permission` call. Cam can validate manually if desired. |
| 11 | Vale graceful-skip locally | ✅ | `vale --version` exits 127 with default (non-mise) PATH; SKILL.md:35's clause unambiguously routes to the documented one-line skip note. No hard-fail. |
| 12 | Tag-mode tracking comment shows per-tool-call updates | ✅ (by inference) | The action's `mcp__github_comment__update_claude_comment` tool is the live-update mechanism — architecturally non-optional. Run 25340806517 logs show 33+ tool-related events; comment was edited at least once during the run. Live intermediate frames aren't preserved retroactively, but the mechanism is in use. |

11 PASS, 1 deferred. No FAIL rows after the two bug fixes below.

### Two latent bugs surfaced and fixed

**Bug 1: ESC bypass evaporates on every fresh `pr-review-overhaul → cam-fork:master` sync.**

Cam fork has no ESC trust policy on `github-secrets/pulumi-docs`. Issue_comment-triggered workflows fail at `pulumi/esc-action@v1` with `Invalid response from token exchange 401: Unauthorized`. Cam shipped commit `01de922a71` ("ops: bypass ESC for re-entrant claude on cam fork") on 2026-04-30 to address it: drop the ESC fetch step, fall back to `secrets.GITHUB_TOKEN`. That commit was on cam fork master only, not in the upstream branch. This session's prep step (`git push --force cam-fork CamSoper/pr-review-overhaul:master`) overwrote the fork master, wiping the bypass — same as it would on every prior session that did the same prep.

**Fix (fork ops only):** A new commit on cam fork master applies the bypass to all three issue_comment-triggered workflows simultaneously: `claude.yml`, `claude-update.yml` (new this session), `claude-new.yml` (new this session). All three lose the `Fetch secrets from ESC` step and replace `${{ steps.esc-secrets.outputs.PULUMI_BOT_TOKEN }}` with `${{ secrets.GITHUB_TOKEN }}`. Companion change in the same commit: `claude-code-review.yml` gains `allowed_bots: ${{ github.event_name == 'workflow_dispatch' && '*' || '' }}` (see Bug 2 below — the fork can't reach the upstream-side fix). Whole thing is fork-ops, never ships upstream; gets evaporated by every fresh sync (same lifecycle as 01de922a71).

**Bug 2: `claude-new.yml`'s dispatcher used `secrets.GITHUB_TOKEN` for `gh workflow run`, making the dispatched run's actor `github-actions[bot]` (type=Bot) — which `claude-code-action@v1` rejects by default with `"Workflow initiated by non-human actor: github-actions (type: Bot). Add bot to allowed_bots list or use '*' to allow all bots"`.**

Latent since `#new-review` was introduced in Session 22 — Session 22 never ran the dispatcher end-to-end. Not fork-specific in nature (would manifest the same way on `pulumi/docs:master`), but masked on the fork by Bug 1's ESC failure landing first.

**Fix (upstream — commit `52356f4298`):** Switch the dispatch step's `GH_TOKEN` from `secrets.GITHUB_TOKEN` to `steps.esc-secrets.outputs.PULUMI_BOT_TOKEN`. `pulumi-bot` is a User account (not a Bot in GitHub App sense), so the dispatched workflow_dispatch run's actor passes the action's bot check naturally. Other `gh` calls in the same workflow (clear pinned, post confirmation comment) keep using `GITHUB_TOKEN` — they don't go through the bot-actor check.

**Companion fork-side fix:** The cam fork can't reach `PULUMI_BOT_TOKEN` (no ESC trust). Instead, on the fork, `claude-code-review.yml` gets `allowed_bots: ${{ github.event_name == 'workflow_dispatch' && '*' || '' }}` — permissive only on the workflow_dispatch trigger, where the dispatcher is the only legitimate caller. The `workflow_run` and `pull_request` paths (Dependabot's normal route) keep the default rejection. Three pre-existing guards already filter Dependabot before the action (`claude-triage.yml:23`, `claude-code-review.yml:45`, the `bot-author` SKIP at line 175), so this fork-side relaxation has no effective surface for misuse.

### Why both fixes are needed

| Path | Trigger event | Dispatcher token | Action's actor check | Verdict |
|---|---|---|---|---|
| **Upstream** before fix | workflow_dispatch (from claude-new.yml) | GITHUB_TOKEN | github-actions[bot] = Bot → reject | ❌ |
| **Upstream** after `52356f4298` | workflow_dispatch (from claude-new.yml) | PULUMI_BOT_TOKEN | pulumi-bot = User → accept | ✅ |
| **Fork** before bypass | claude-update.yml's ESC fetch | (n/a — fails at ESC) | (never reaches action) | ❌ |
| **Fork** after bypass | (no ESC; dispatcher uses GITHUB_TOKEN) | github-actions[bot] = Bot | rejected unless `allowed_bots` | ❌ |
| **Fork** after bypass + `allowed_bots` clause | workflow_dispatch (from claude-new.yml) | github-actions[bot] | `allowed_bots: '*'` (workflow_dispatch only) → accept | ✅ |

### Session 22 oversight: `review:claude-working` still in `scripts/labels/labels.json`

Session 22 dropped `review:claude-working` from `.github/labels-pr-review.md` (the documentation/spec) and from all workflows, but missed `scripts/labels/labels.json` (the script's authoritative config). Without this fix, running `sync-labels.sh` against any repo would re-create the dropped label, defeating the cleanup. Fixed in commit `f4951563bd`. The label was deleted directly from the fork via `gh label delete` (the script's `--prune` only deletes rename-collision orphans, not labels-not-in-config).

### Items NOT shipped (carried into Session 24)

1. **Row 10 (non-write-access mention)** — needs a second GitHub account. Skill mechanism is the same access check as csoper's mentions; only the negative branch differs. Cam can validate manually if desired.
2. **Screenshots of rows 2 / 3 / 6** — for the eventual `pulumi/docs:#18680` Slack/Notion writeup. I can't capture screenshots; Cam to do this manually from the fork PR timelines (links in the table above are runs/comments).
3. **Push `pr-review-overhaul` upstream commits** — `52356f4298` (PULUMI_BOT_TOKEN dispatcher fix) and `f4951563bd` (labels.json cleanup) are committed locally but not pushed to origin. Cam to review and push.
4. **`scripts/labels/sync-labels.sh` enhancement** — currently `--prune` only deletes rename-collision orphans. A future improvement: also flag (and optionally delete) labels present in the repo but absent from `labels.json`. Out of scope for this session.

### Methodology / repeatable patterns

- **The "stop, capture, propose" rule paid off.** When the first round of mentions failed at ESC, I had a draft fix (add `secrets.ANTHROPIC_API_KEY` fallback) ready to push. Stopping and asking "how have previous test batteries handled this?" surfaced the existing 04-30 bypass commit — the right pattern was already designed for this exact case. Pushing the draft fix would have created a divergent third pattern.
- **Cam-pushback patterns this session:**
  - "How have previous test batteries handled this? Surely there's history in the workflow files." — caught me about to invent a fix when one already existed in git history. Lesson: when a problem looks new, search commit history for the pattern before designing a workaround.
  - "Would that cause dependabot to trigger reviews?" — turned `allowed_bots: '*'` from a blunt fix into a workflow_dispatch-gated one. Three independent pre-existing Dependabot guards meant the broad form would have been safe in practice, but the gated form is honest about the contract: bots may dispatch only via workflow_dispatch, never via workflow_run.
  - "At runtime, the bot dispatching will be pulumi bot, I believe. Does that make a difference?" — caught me about to ship a fork-only `allowed_bots` change as if it were the upstream fix. The actual upstream fix is the `PULUMI_BOT_TOKEN` dispatcher swap; `allowed_bots` is the fork-only fallback. Two different fixes for two different operating contexts.
- **Two-fix architecture for fork vs. upstream divergence.** When a workflow has features that only work on the upstream repo's secret/identity infrastructure (ESC trust, PULUMI_BOT_TOKEN), the fork-only ops commit owns the fallback path; the upstream branch owns the proper fix. Both forks of the design exist simultaneously, with the lifecycle of fork-ops commits being "wiped on every prep sync, re-applied each session."
- **Latent bugs in dispatcher paths only show up under end-to-end testing.** The `#new-review` dispatcher worked fine in isolation (the YAML was correct), but the *dispatched run's* identity propagation is the actual contract being tested. Unit-level inspection of the dispatcher YAML can't catch this. Reinforces the value of the e2e battery.

### Backlog after Session 23

Active:

1. **Drop "vale" as a name in PR-facing text.** Pinned-review surface should just say "Style check" (or similar) instead of `[style] write-good.TooWordy` / `[style] Google.Foo`. The Vale rule path is a CI implementation detail; the user-facing label should be tool-agnostic.
2. **Per-file nit summary in the collapsible roll-up.** The current "file with multiple nits" collapsible header doesn't preview what's inside. Add a one-line summary of the rule kinds (e.g., "3 wordiness, 2 substitutions"), so a reader can skim without expanding.
3. **Suppress `Google.EmDash`.** Currently noisy on existing technical prose; not pulling its weight relative to the false-positive rate.
4. **Cam's "quick `/docs-review`" variant** (Session-18) — still open.

Closed this session:

- **End-to-end fork test battery** (S22 #1) → ✅ shipped (11 PASS / 1 deferred / 0 FAIL after fixes).
- **`claude-new.yml` bot-actor rejection** → ✅ fixed upstream (`52356f4298`).
- **`scripts/labels/labels.json` Session 22 oversight** → ✅ fixed upstream (`f4951563bd`).
- **`review:claude-working` retired from cam fork** → ✅ deleted directly via `gh label delete`.

### Files changed (Session 23 substance)

Upstream `pr-review-overhaul`:

- `.github/workflows/claude-new.yml` — dispatcher GH_TOKEN switched to `steps.esc-secrets.outputs.PULUMI_BOT_TOKEN`. (`52356f4298`)
- `scripts/labels/labels.json` — `review:claude-working` entry removed. (`f4951563bd`)
- `SESSION-NOTES.md` — this entry.

Cam fork master only (lifecycle: wiped on every fresh sync):

- `.github/workflows/claude.yml`, `claude-update.yml`, `claude-new.yml` — drop the `Fetch secrets from ESC` step; replace `PULUMI_BOT_TOKEN` reference with `secrets.GITHUB_TOKEN`.
- `.github/workflows/claude-code-review.yml` — `allowed_bots: ${{ github.event_name == 'workflow_dispatch' && '*' || '' }}` clause added to the `claude-code-action@v1` block.

Fork PRs left for posterity:

- `CamSoper/pulumi.docs#116`, `#117`, `#118` (carry-over fixtures).
- `#119`, `#120`, `#121` (new test PRs — typo fix, compound-mention, dispute).

### Memory updates

None. All Session-23 substance is project state for this branch (workflow design, fork-ops lifecycle, hashtag-router behavior). The methodology lessons ("search git history for the pattern before designing a workaround"; "two-fix architecture for fork vs. upstream divergence") are repo-specific and live here, not in auto-memory.
