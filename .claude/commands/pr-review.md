---
description: Comprehensive Pulumi Docs PR review with approve/request changes/close workflow
---

# Pull Request Review Command

Perform comprehensive Pulumi Docs review of any pull request with style and accuracy checks, then streamline the approval workflow with automated actions. Automatically detects external contributors and uses warm, welcoming communication.

---

## Usage

`/pr-review <PR_NUMBER>`

Reviews any pull request and presents action choices for approval, changes, or closure.

**Required**: PR number

**Works with**: All PRs (internal and external)

**Special handling**: Automatically detects external contributors and uses warmer, more appreciative tone

---

## Process

### Step 1: Verify PR and Detect Contributor Type

1. Verify the PR exists: `gh pr view {{arg}}`
2. Get PR author: `gh pr view {{arg}} --json author --jq '.author.login'`
3. Check if author is pulumi org member:

   ```bash
   curl -s -o /dev/null -w "%{http_code}" \
     -H "Authorization: token $GITHUB_TOKEN" \
     -H "Accept: application/vnd.github+json" \
     "https://api.github.com/orgs/pulumi/members/$AUTHOR"
   ```

4. Store contributor type for later use:
   - If HTTP 204: Internal contributor (pulumi org member)
   - If HTTP 404: External contributor (non-org member)
5. Display: "📝 Reviewing PR #{{arg}} from @username (external/internal contributor)"

### Step 2: Gather PR Information

1. Get full PR details: `gh pr view {{arg}} --json title,body,files,additions,deletions`
2. Get the diff: `gh pr diff {{arg}}`
3. Note the PR title, description, and files changed

### Step 3: Perform Comprehensive Review

Review the PR changes using the **Review Criteria** section from `docs-review.md`.

This includes all standard checks: style guide enforcement, spelling/grammar, link validation, code examples, file standards, SEO, special cases (file moves, redirects, infrastructure changes), and role-specific guidelines for documentation vs blog/marketing content.

### Step 4: Present Review Findings

Present the review in the conversation:

1. Start with a summary of what was reviewed (files, scope)
2. List findings by category (critical issues, style improvements, suggestions)
3. Include specific line numbers for each issue
4. Use suggestion code blocks for recommended changes
5. Highlight positive aspects of the contribution
6. Keep feedback constructive and encouraging
7. Display a change summary for context:

   **Changes:** [X] file(s) changed (+[additions]/-[deletions] lines)

   Extract counts from the `gh pr view {{arg}} --json files,additions,deletions` command already run in Step 2.
   - Files count: Length of `files` array
   - Additions: `additions` field
   - Deletions: `deletions` field

   Use singular "file" when count is 1, plural "files" otherwise.

   **Example outputs**:
   - "**Changes:** 1 file changed (+3/-1 lines)" - Small, focused change
   - "**Changes:** 15 files changed (+543/-234 lines)" - Substantial change

   This summary helps users understand scope when choosing an action in Step 5.

### Step 5: Present Action Choices

Use AskUserQuestion to present these 6 options (labels and descriptions adapt based on contributor type):

**For External Contributors**:

1. **Approve** (Recommended)
   - Approve PR with warm, personalized thank you comment
   - Use: When PR is ready to merge

2. **Approve and merge**
   - Approve with heartfelt thanks and merge immediately
   - Use: When PR is excellent and ready for immediate merge

3. **Make changes and approve**
   - Make minor edits, then approve with appreciation
   - Use: For small fixes (typos, formatting) that preserve contributor's credit

4. **Request changes**
   - Post encouraging, constructive feedback with request-changes flag
   - Use: When contributor should make the changes themselves

5. **Close with thanks**
   - Post grateful explanation and close
   - Use: When PR doesn't fit but you appreciate their effort

6. **Do nothing yet**
   - Exit without action
   - Use: Need more time or team discussion

**For Internal Contributors**:

1. **Approve** (Recommended)
   - Approve PR with constructive feedback
   - Use: When PR is ready to merge

2. **Approve and merge**
   - Approve and merge immediately (squash)
   - Use: When PR is ready for immediate merge

3. **Make changes and approve**
   - Make edits, then approve
   - Use: For minor fixes before approval

4. **Request changes**
   - Post review feedback with request-changes flag
   - Use: When author should address issues

5. **Close PR**
   - Close with explanation
   - Use: When PR is no longer needed or doesn't fit

6. **Do nothing yet**
   - Exit without action
   - Use: Need more time or discussion

### Step 6: Preview Planned Actions and Get Confirmation

**CRITICAL**: Always show the user what will happen before executing any action.

Generate a preview based on the user's choice from Step 5:

#### For "Approve"

Display the exact comment that will be posted:

```text
## Preview: Approval Comment

The following comment will be posted when approving PR #{{arg}}:

---
[Exact comment text based on contributor type:
 - External: "Thank you for this contribution! [Brief specific praise if applicable]. Welcome to the community! 🎉"
 - Internal: "LGTM! [Any specific positive feedback or minor suggestions]"]
---

GitHub command: gh pr review {{arg}} --approve --body "[comment]"
```

#### For "Approve and merge"

Display the exact comment and merge action:

```text
## Preview: Approval and Merge

The following comment will be posted when approving PR #{{arg}}:

---
[Exact comment text based on contributor type:
 - External: "Thank you for this contribution! [Brief specific praise]. Merging now. 🎉"
 - Internal: "LGTM! Merging now."]
---

GitHub commands:
1. gh pr review {{arg}} --approve --body "[comment]"
2. gh pr merge {{arg}} --auto --squash
```

#### For "Make changes and approve"

First, ask the user: "What changes should I make to the PR? (describe the specific edits needed)"

Then, analyze which files will be affected and display:

```text
## Preview: Changes and Approval

I will:
1. Save current branch
2. Check out PR branch: gh pr checkout {{arg}}
3. Make these changes:
   - File: [path] - [description of edits]
   - File: [path] - [description of edits]
4. Show you the diff before committing
5. Commit: "Apply style and formatting fixes"
6. Push changes
7. Approve with this comment:

---
[Exact comment text based on contributor type:
 - External: "I've applied some minor style and formatting fixes. Thank you for your contribution! 🙏"
 - Internal: "Applied some style/formatting fixes. LGTM!"]
---

8. Return to original branch
```

#### For "Request changes"

Display the full formatted comment:

```text
## Preview: Request Changes Comment

The following review will be posted with request-changes flag on PR #{{arg}}:

---
[Full formatted comment based on contributor type:

External contributor:
- Opening: "Thank you for this contribution!"
- Brief acknowledgment of good aspects (1 sentence max, if applicable)
- Specific issues with line numbers from Step 4 findings
- Suggestion code blocks for fixes
- Closing: "Feel free to mention @claude if you need help with these changes"

Internal contributor:
- Professional opening
- Specific issues with line numbers from Step 4 findings
- Suggestion code blocks for fixes
- Clear action items]
---

GitHub command: gh pr review {{arg}} --request-changes --body "[comment]"
```

#### For "Close with thanks" / "Close PR"

Display the full closing comment:

```text
## Preview: Close PR

The following comment will be posted before closing PR #{{arg}}:

---
[Full formatted comment based on contributor type:

External contributor ("Close with thanks"):
- "Thank you for taking the time to contribute!"
- Clear, kind explanation of why closing
- Brief acknowledgment of valuable aspects (if applicable)
- Suggest alternatives if appropriate
- Closing: "We appreciate your interest in Pulumi!"

Internal contributor ("Close PR"):
- Clear explanation of why closing]
---

GitHub commands:
1. gh pr comment {{arg}} --body "[comment]"
2. gh pr close {{arg}}
```

#### For "Do nothing yet"

Display:

```text
## Preview: No Action

No changes will be made to PR #{{arg}}.

You can run /pr-review {{arg}} again when ready to take action.
```

#### Request Confirmation

Use AskUserQuestion with these options:

**Question**: "Proceed with this action?"

**Options**:

1. **Yes, proceed** - Execute the action as previewed
2. **Edit comment** - Modify the comment text before posting
3. **Change action** - Go back and choose a different action
4. **Cancel** - Exit without taking any action

**Handle responses**:

- **"Yes, proceed"**: Continue to Step 7 (execution)
- **"Edit comment"**:
  - Ask user: "Please provide the revised comment text:"
  - Generate updated preview with new comment
  - Request confirmation again with same options
  - Repeat until user confirms or cancels
- **"Change action"**: Return to Step 5 (action selection) and let user choose again
- **"Cancel"**: Display "No action taken on PR #{{arg}}." and exit

### Step 7: Execute Confirmed Action

**Using the confirmed/edited content from Step 6**, execute the action based on the user's choice and contributor type:

**For "Approve"**:

*External contributor*:

```bash
gh pr review {{arg}} --approve --body "Thank you for this contribution! [Brief specific praise, 1 sentence max, or omit if nothing stands out]. Welcome to the community! 🎉"
```

*Internal contributor*:

```bash
gh pr review {{arg}} --approve --body "LGTM! [Any specific positive feedback or minor suggestions]"
```

**For "Approve and merge"**:

*External contributor*:

```bash
gh pr review {{arg}} --approve --body "Thank you for this contribution! [Brief specific praise, 1 sentence max]. Merging now. 🎉"
gh pr merge {{arg}} --auto --squash
```

*Internal contributor*:

```bash
gh pr review {{arg}} --approve --body "LGTM! Merging now."
gh pr merge {{arg}} --auto --squash
```

**For "Make changes and approve"**:

1. Save current branch: `git rev-parse --abbrev-ref HEAD`
2. Check out PR: `gh pr checkout {{arg}}`
3. Make the requested changes (from Step 6) using Edit/Write tools
4. Show the diff: `git diff`
5. Display the diff in the conversation
6. Ask user: "Proceed with commit and approval? (Yes/No)"
   - If No: Ask "Would you like to make additional changes or cancel? (Additional changes/Cancel)"
     - Additional changes: Return to making edits, show diff again, repeat confirmation
     - Cancel: Return to original branch and exit without committing
   - If Yes: Continue to next step
7. Commit: `git add . && git commit -m "Apply style and formatting fixes\n\nCo-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"`
8. Push: `git push`
9. Approve with appropriate tone (using confirmed comment from Step 6):

   *External contributor*:

   ```bash
   gh pr review {{arg}} --approve --body "I've applied some minor style and formatting fixes. Thank you for your contribution! 🙏"
   ```

   *Internal contributor*:

   ```bash
   gh pr review {{arg}} --approve --body "Applied some style/formatting fixes. LGTM!"
   ```

10. Return: `git checkout <original-branch>`

**For "Request changes"**:

*External contributor*:

```bash
gh pr review {{arg}} --request-changes --body "[Format with:
- Brief opening: 'Thank you for this contribution!'
- Brief acknowledgment of good aspects if applicable (1 sentence max)
- Specific issues with line numbers
- Suggestion code blocks for fixes
- Simple closing: 'Feel free to mention @claude if you need help with these changes']"
```

*Internal contributor*:

```bash
gh pr review {{arg}} --request-changes --body "[Format with:
- Professional opening
- Specific issues with line numbers
- Suggestion code blocks for fixes
- Clear action items]"
```

**For "Close PR"**:

*External contributor*:

```bash
gh pr comment {{arg}} --body "[Format with:
- Brief thank you: 'Thank you for taking the time to contribute!'
- Clear, kind explanation of why closing
- Brief acknowledgment of valuable aspects if applicable
- Suggest alternatives if appropriate
- Simple closing: 'We appreciate your interest in Pulumi!']"
gh pr close {{arg}}
```

*Internal contributor*:

```bash
gh pr comment {{arg}} --body "[Clear explanation of why closing]"
gh pr close {{arg}}
```

**For "Do nothing yet"**:

- Display: "No action taken. You can run this command again when ready."
- Exit

### Step 8: Report Execution Results

After execution completes, provide clear confirmation of what happened:

**For successful approval (action: "Approve")**:

```text
✅ PR #{{arg}} approved successfully!

Approval comment posted to the PR.
The PR author has been notified.

View the PR at: [PR URL from gh pr view]
```

**For successful approval and merge (action: "Approve and merge")**:

```text
✅ PR #{{arg}} approved and merged successfully!

Approval comment posted and PR merged using squash merge.
The PR author has been notified.

View the merged PR at: [PR URL from gh pr view]
```

**For successful changes and approval (action: "Make changes and approve")**:

```text
✅ Changes applied and PR #{{arg}} approved successfully!

Changes committed: [commit SHA from git log -1 --format=%h]
Files modified:
- [list files from git diff --name-only HEAD~1]

Approval comment posted to the PR.

View changes at: [PR URL from gh pr view]/commits
```

**For successful change request (action: "Request changes")**:

```text
✅ Changes requested on PR #{{arg}}

Review posted with request-changes flag.
The PR author has been notified and will receive your feedback.

View the review at: [PR URL from gh pr view]
```

**For successful PR closure (action: "Close with thanks" / "Close PR")**:

```text
✅ PR #{{arg}} closed successfully

Closing comment posted explaining the decision.
The PR author has been notified.

View the closed PR at: [PR URL from gh pr view]
```

**For "Do nothing yet" exit**:

```text
No action taken on PR #{{arg}}.

You can run /pr-review {{arg}} again when ready to take action.
```

**For errors**:

```text
❌ Error executing action

Command failed: [command that failed]
Error output: [error message from gh or git]

No changes were made to PR #{{arg}}.

Recovery options:
1. Run /pr-review {{arg}} to try again
2. Check your permissions with: gh auth status
3. Verify PR status with: gh pr view {{arg}}
4. Perform the action manually via GitHub web interface
```

If you checked out a PR branch and an error occurred, return to the original branch before displaying the error:

```bash
git checkout <original-branch>
```

---

## Important Notes

- **Preview accuracy**: Previews show the planned action with exact comment text. The actual execution in Step 7 uses the confirmed (or edited) content from Step 6.
- **Preview-to-execution consistency**: What users see in the preview is exactly what gets posted to GitHub. Always use the confirmed comment text from Step 6 when executing in Step 7.
- **Edit flexibility**: The "Edit comment" option allows users to refine tone, add context, or adjust wording before posting. After editing, show the updated preview and confirm again.
- **Communication tone**: Use warm, welcoming language with external contributors. Keep praise brief and specific (1 sentence max).
- **Encouragement**: Make contributors feel welcomed to the Pulumi community
- **Credit**: Use "make changes" option judiciously - only for minor fixes that don't reduce contributor's credit for the work
- **Branch safety**: Always track current branch and return to it after PR checkout, especially if errors occur
- **Error handling**: If any gh or git command fails, return to original branch (if applicable), display the error with recovery options, and ensure no partial state (e.g., don't post comment if merge fails)
- **Token efficiency**: Generate preview text once in Step 6 and reuse it in Step 7. For large diffs (>100 lines), show summary with option to expand full diff.
- **Large diffs**: When showing diffs in "Make changes and approve", if the diff exceeds 100 lines, show a summary (files changed, lines added/removed) and ask if user wants to see the full diff
- **Contributor type caching**: Store the contributor type (internal/external) result from Step 1 and reuse it throughout Steps 5-8. Don't re-query the GitHub API if the user changes actions during preview.
