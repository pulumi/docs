---
user-invocable: false
description: Preview formats and confirmation flows for PR actions
---

# Action Preview Templates

**CRITICAL**: Always show what will happen before executing any action.

## Standard Action Previews

| Action | Preview | Commands |
|--------|---------|----------|
| **Approve** | Comment: [Template from message-templates.md] | `gh pr review {{arg}} --approve --body "{{COMMENT}}"` |
| **Approve and merge** | Comment: [Template from message-templates.md] | `gh pr review {{arg}} --approve --body "{{COMMENT}}"`<br>`gh pr merge {{arg}} --auto --squash` |
| **Request changes** | Comment: [Template from message-templates.md]<br>Include issues with line numbers + suggestion blocks | `gh pr review {{arg}} --request-changes --body "{{COMMENT}}"` |
| **Close PR** | Comment: [Template from message-templates.md]<br>Include clear closing explanation | `gh pr comment {{arg}} --body "{{COMMENT}}"`<br>`gh pr close {{arg}}` |
| **Do nothing yet** | No changes will be made to PR #{{arg}}.<br>Run /pr-review {{arg}} again when ready. | - |

## Make Changes and Approve Preview

**Note**: Not available for bot PRs (excluded from bot menus)

**Flow**: Ask user for changes, then display preview:

```
## Preview: Changes and Approval

I will:
1. Save current branch
2. Check out PR: gh pr checkout {{arg}}
3. Make changes: [file: path - description]
4. Show diff before committing
5. Commit: "Apply style and formatting fixes\n\nCo-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
6. Push changes
7. Approve with comment: [Template]
8. Return to original branch
```

See SKILL.md Step 9 for complete workflow details.

## Confirmation Question

Use AskUserQuestion with these options:

**Question**: "Proceed with this action?"

**Options**:
1. **Yes, proceed** - Execute the action as previewed
2. **Edit comment** - Modify the comment text before executing
3. **Change action** - Go back to action selection menu
4. **Cancel** - Exit without making any changes

## Response Handling

### Yes, proceed

- Continue to execution step
- Use exact content from preview

### Edit comment

1. Ask user for revised comment text
2. Show updated preview with new text
3. Ask for confirmation again (repeat confirmation question)
4. Loop until user chooses "Yes, proceed" or "Cancel"

### Change action

- Return to action selection step (Step 7)
- Show menu again with all options
- Start preview process over with new selection

### Cancel

- Exit workflow immediately
- Display: "No action taken on PR #{{arg}}."
- Do not modify PR in any way

## Implementation Notes

- Always show exact comment text that will be posted
- Include all commands that will be executed
- For "Make changes and approve": Show file-by-file changes before commit
- Preview uses templates from message-templates.md based on contributor type
- Confirmation loop allows refinement without re-running entire workflow
- "Change action" preserves all context from review (doesn't require re-review)
