---
user-invocable: false
description: Preview formats and confirmation flows for PR actions
---

# Action Preview Templates

**CRITICAL**: Always show what will happen before executing any action.

## Preview format

Every preview shows the chosen action, the merge toggle, any auto-applied changes, and the comment body that will be posted. Order:

```
## Preview

Action: <action>
[x] Auto-merge after approval (squash)   ← toggle, default depends on rules below

[If "Make changes and approve"]
Trivial fixes (will be applied):
  <N> trivial fixes: <breakdown>  [show diff]

Contradicted-claim fixes (will be applied):
  <file:line> — "<replacement text>"
  ...

Comment body that will be posted:
  <full comment>

Commands that will run:
  <list of gh commands>
```

When `AI_SUSPECT=true`, the trivial-fixes section is replaced with:

```
Trivial-fix auto-apply disabled (AI-suspect — manual review required)
```

## Auto-merge toggle defaults

The toggle's initial state is determined by these rules. The user can flip it during preview without re-navigating menus.

### Toggle defaults ON

Only when **all** of:

- Contributor is a **bot** (dependabot, pulumi-bot, renovate, copilot, github-actions)
- CI is green
- No remaining contradictions or unverifiable claims
- `AI_SUSPECT=false`

### Toggle defaults OFF

For all human-authored PRs, regardless of seniority, contributor type, or CI status. **Pulumi convention: authors merge their own PRs.** Auto-merging on a human's behalf is the exception, not the norm.

The toggle exists for the rare case where the user actually wants to merge on the author's behalf — typically external first-timers without merge rights, or stale PRs the author has abandoned.

### AI-suspect override

When `AI_SUSPECT=true`, the toggle defaults OFF unconditionally — even for bot PRs. This forces a conscious keystroke before merging anything that may contain AI-generated content.

## Standard Action Previews

| Action | Commands (with merge toggle ON) | Commands (with merge toggle OFF) |
|--------|----------------------------------|----------------------------------|
| **Approve** | `gh pr review {{arg}} --approve --body "{{COMMENT}}"`<br>`gh pr merge {{arg}} --auto --squash` | `gh pr review {{arg}} --approve --body "{{COMMENT}}"` |
| **Make changes and approve** | (See workflow below) followed by merge | (See workflow below), no merge |
| **Request changes** | `gh pr review {{arg}} --request-changes --body "{{COMMENT}}"` | (same — merge toggle hidden for this action) |
| **Close PR** | `gh pr comment {{arg}} --body "{{COMMENT}}"`<br>`gh pr close {{arg}}` | (same — merge toggle hidden for this action) |
| **Do nothing yet** | No changes will be made to PR #{{arg}}.<br>Run /pr-review {{arg}} again when ready. | (same) |

The merge toggle is shown only when the chosen action is `Approve` or `Make changes and approve`. For `Request changes`, `Close PR`, and `Do nothing yet`, it's hidden.

## Make Changes and Approve Preview

**Note**: Not available for bot PRs (excluded from bot menus).

**Flow**: Pull the candidate fixes from two sources, show the preview, confirm, then execute:

```
## Preview: Make Changes and Approve

Action: Make changes and approve
[x] Auto-merge after approval (squash)   ← OFF by default for human PRs

Trivial fixes (will be applied):
  12 trivial fixes: 4 trailing-ws · 3 EOF newlines · 5 heading-case  [show diff]

Contradicted-claim fixes (will be applied):
  content/docs/cli/logout.md:42 — "removes credentials for the current backend"
  content/blog/foo.md:88        — "available since v3.230.0 (not v3.220.0)"

Comment body that will be posted:
  [Template from message-templates.md]

I will:
1. Save current branch
2. Check out PR: gh pr checkout {{arg}}
3. Run auto-trivials.sh on changed files
4. Apply contradicted-claim suggested fixes via Edit
5. Show diff
6. Commit: "Apply review fixes\n\nCo-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>"
7. Push changes
8. Approve with comment above
9. [If toggle ON] gh pr merge {{arg}} --auto --squash
10. Return to original branch
```

Auto-trivials are skipped entirely when `AI_SUSPECT=true` (see `pr-review:references:trust-and-scrutiny`).

See SKILL.md Step 9 for complete workflow details.

## Confirmation Question

Use AskUserQuestion with these options:

**Question**: "Proceed with this action?"

**Options**:
1. **Yes, proceed** - Execute the action as previewed
2. **Toggle merge** - Flip the auto-merge toggle (no re-preview)
3. **Edit comment** - Modify the comment text before executing
4. **Cancel** - Exit without making any changes

## Response Handling

### Yes, proceed

- Continue to execution step
- Use exact content from preview, including current toggle state

### Toggle merge

- Flip the `Auto-merge after approval` toggle (ON ↔ OFF)
- Print a single-line confirmation: `Auto-merge toggle is now ON` (or `OFF`)
- Re-ask the confirmation question — **do not** re-display the full preview. The user just saw it; they only need the new toggle state and the menu.

### Edit comment

1. Use AskUserQuestion to ask user for revised comment text (open-ended)
2. Show updated preview with new text and current toggle state
3. Ask for confirmation again (repeat confirmation question)
4. Loop until user chooses "Yes, proceed" or "Cancel"

### Cancel

- Exit workflow immediately
- Display: "No action taken on PR #{{arg}}."
- Do not modify PR in any way

## Implementation Notes

- Always show the exact comment text and command list that will execute
- Always show the merge-toggle state explicitly so the user can verify before confirming
- For "Make changes and approve": show file-by-file changes and trivial-fix summary before commit
- Preview uses templates from `pr-review:references:message-templates` based on contributor type
- Confirmation loop allows toggle flips and comment edits without re-running entire workflow
- Never add a separate "Approve and merge" action — merge is always a toggle, never a menu choice
