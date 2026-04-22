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
