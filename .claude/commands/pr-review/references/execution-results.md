---
user-invocable: false
description: Result messages and status reporting after action execution
---

# Execution Results

Report results to user after executing confirmed action.

## Result Message Templates

| Action | Result Message | Additional Info |
|--------|---------------|-----------------|
| **Approve** | ✅ PR #{{arg}} approved successfully!<br><br>Approval comment posted. | PR URL |
| **Approve and merge** | ✅ PR #{{arg}} approved with auto-merge enabled!<br><br>PR will merge using squash when checks pass. Verify with: `gh pr view {{arg}} --json state,mergedAt,autoMergeRequest` | PR URL<br>Bot context (if bot): @username, Risk tier, Labels<br>If Dependabot HIGH/MEDIUM: "⚠️ Next merge to master triggers pulumi-test.io deployment" |
| **Make changes and approve** | ✅ Changes applied and PR #{{arg}} approved!<br><br>Changes committed: [SHA]<br>Files: [list] | PR URL/commits |
| **Request changes** | ✅ Changes requested on PR #{{arg}}<br><br>Review posted with request-changes flag. | PR URL |
| **Close PR** | ✅ PR #{{arg}} closed<br><br>Closing comment posted. | PR URL |
| **Do nothing yet** | No action taken. Run /pr-review {{arg}} again when ready. | - |

## Additional Context by Action Type

### Approve

Show PR URL and confirm comment posted.

### Approve and Merge

- Explain auto-merge behavior (merges when checks pass)
- Provide verification command
- **For bot PRs**: Include bot username, risk tier, relevant labels
- **For Dependabot HIGH/MEDIUM**: Warn about pulumi-test.io deployment trigger

**Example** (Dependabot HIGH): "✅ PR #1234 approved with auto-merge enabled! PR will merge using squash when checks pass. Verify with: gh pr view 1234 --json state,mergedAt,autoMergeRequest | Bot: @dependabot[bot] | Risk: HIGH | Labels: deps-security-patch | ⚠️ Next merge to master triggers pulumi-test.io deployment"

### Make Changes and Approve

Show commit SHA, list modified files with links.

**Example**: "✅ Changes applied and PR #1234 approved! Changes committed: a1b2c3d | Files: content/docs/intro/index.md (typo fixes), content/docs/install/index.md (formatting) | View: [URL]"

### Request Changes

Confirm request-changes flag set, show PR URL.

### Close PR

Confirm closed, show PR URL.

### Do Nothing Yet

Explain no changes made, remind how to re-run.

## Error Handling

If any command fails during execution:

```text
❌ Failed to [action] PR #{{arg}}

Error: [error message]

You can retry with:
- /pr-review {{arg}} (re-run full workflow)
- Or use gh CLI directly:
  [relevant recovery commands based on what failed]
```

## GitHub CLI Field Reference

For status verification, use these gh CLI fields:

- `state` - PR state (OPEN, CLOSED, MERGED)
- `mergedAt` - When PR was merged (null if not merged)
- `autoMergeRequest` - Auto-merge configuration (null if not enabled)

Example verification command:

```bash
gh pr view {{arg}} --json state,mergedAt,autoMergeRequest
```

## Implementation Notes

- Always show PR URL for easy access
- For bot PRs: Include bot context (username, risk, labels)
- For HIGH/MEDIUM Dependabot: Warn about deployment triggers
- Include verification commands where helpful
- Provide recovery commands on errors
- Keep messages concise but informative
