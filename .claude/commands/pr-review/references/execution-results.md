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
| **Approve and merge** | ✅ PR #{{arg}} approved with auto-merge enabled!<br><br>PR will merge using squash when checks pass. Verify with: `gh pr view {{arg}} --json state,mergedAt,autoMergeRequest` | PR URL<br>Bot context (if bot): @username, Labels<br>If Dependabot dependency PR: "⚠️ Next merge to master triggers pulumi-test.io deployment" |
| **Make changes and approve** | ✅ Changes applied and PR #{{arg}} approved!<br><br>Changes committed: [SHA]<br>Files: [list] | PR URL/commits |
| **Request changes** | ✅ Changes requested on PR #{{arg}}<br><br>Review posted with request-changes flag. | PR URL |
| **Close PR** | ✅ PR #{{arg}} closed<br><br>Closing comment posted. | PR URL |
| **Do nothing yet** | No action taken. Run /pr-review {{arg}} again when ready. | - |

**Examples** to model:

- *Dependabot with merge*: `✅ PR #1234 approved with auto-merge enabled! PR will merge using squash when checks pass. Verify with: gh pr view 1234 --json state,mergedAt,autoMergeRequest | Bot: @dependabot[bot] | Labels: deps-security-patch | ⚠️ Next merge to master triggers pulumi-test.io deployment`
- *Make changes and approve*: `✅ Changes applied and PR #1234 approved! Changes committed: a1b2c3d | Files: content/docs/intro/index.md (typo fixes), content/docs/install/index.md (formatting) | View: [URL]`

## GitHub CLI Field Reference

For status verification, use these gh CLI fields:

- `state` - PR state (OPEN, CLOSED, MERGED)
- `mergedAt` - When PR was merged (null if not merged)
- `autoMergeRequest` - Auto-merge configuration (null if not enabled)

Example verification command:

```bash
gh pr view {{arg}} --json state,mergedAt,autoMergeRequest
```

