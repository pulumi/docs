---
user-invocable: false
description: How to wait for a pinned pre-merge review to land — event subscription, bounded polling, and when to hand back.
---

# Watching for the review

The pre-merge review is a GitHub Actions job, not something you can block on. `claude-code-review.yml` gives the job a 40-minute ceiling and the model step 18 minutes; in practice a review posts in **5-15 minutes** from the ready-for-review transition. Anything past ~40 minutes without a pinned comment is a failure, not a slow run.

## First: is a review even coming?

Don't watch a PR that will never post one.

| Situation | Signal | What to say |
|---|---|---|
| PR is a draft | `isDraft: true` | "Review fires when this goes ready-for-review — want me to mark it ready?" |
| Trivial short-circuit | `review:trivial` | No pinned comment is coming. If `review:prose-flagged` is also set, triage posted an advisory comment — walk that instead. |
| Frontmatter-only | `review:frontmatter-only` | Same as above. |
| Oversized | `review:oversized` | Triage posted a `<!-- TRIAGE_OVERSIZED -->` advisory suggesting a split. Offer to split the hand-written source into its own PR — that PR gets a real review. |
| Bot-authored PR | author is `pulumi-bot` / `dependabot[bot]` | Review skips bot PRs. |
| `review:error` | Workflow failed before publishing | Watching won't help. Read the Actions log; `@claude #new-review` reruns from scratch. |

## Preferred: subscribe to PR events

When the session has PR activity subscription available (Claude Code on the web and other remote sessions expose `subscribe_pr_activity`), use it:

- Subscribe once with the repo and PR number, then **end the turn**. Review completion, CI results, and comments arrive as wake events; the session resumes on its own.
- Do not also poll. A subscription plus a polling loop wakes twice per event and burns the session for nothing.
- On the wake event: re-fetch the pinned comment, then go to the skill's Step 3. The event tells you *that* something happened, never *what the review says*.
- Unsubscribe when the PR merges or closes, or when the user says to stop.

## Fallback: bounded polling

In a local CLI session there is no event stream. Poll on a **bounded** loop, and tell the user the shape of it before starting ("checking every 2 minutes for up to 30").

```bash
for i in $(seq 1 15); do
  LABELS=$(gh pr view "$PR" --json labels --jq '[.labels[].name] | join(",")')
  case "$LABELS" in
    *review:outstanding-issues*|*review:no-blockers*) echo "review posted"; break ;;
    *review:error*) echo "review errored"; break ;;
  esac
  sleep 120
done
```

Rules for the fallback:

- **Cap it.** 30 minutes of polling, then stop and report — never an unbounded loop.
- **Stay quiet while waiting.** One line at the start, one when it lands. No per-iteration narration.
- **Offer the alternative first.** Polling occupies the session; many users would rather do something else and run `/address-review <PR>` later. Ask, and make "ping me later" a real option rather than a formality.
- **Watch the run, not just the label,** when the user wants detail: `gh run watch` on the `Pre-merge Review (main)` workflow run for the head SHA.

## While waiting

Waiting time is not dead time. Useful things to offer:

- Run `/docs-review` locally on the same branch — same criteria, no GitHub round-trip. Findings you fix now can land in the same fix-push later.
- Pre-read the diff for the things the review reliably flags: missing aliases on moved files, internal links to pages that don't exist, frontmatter `meta_desc` length, heading case.

Don't start speculative edits while waiting unless the user asks. A push during the review run makes the review stale the moment it posts.

## When it doesn't land

Past the 40-minute ceiling with no pinned comment and no `review:error`:

1. Check the workflow run for the head SHA — a cancelled or timed-out job leaves no comment.
1. Check whether the PR is still marked ready (a draft transition mid-run kills it).
1. Re-trigger with `@claude #new-review`, which bypasses the skip paths, or transition draft → ready.

Report what happened rather than waiting again. Two silent 40-minute waits is worse than one clear "the review job timed out; want me to retrigger it?"
