---
description: Review and approve/merge pull requests as a maintainer (full workflow with approve, request changes, merge, close actions)
---

# Pull Request Review Command

**Use this when:** You're reviewing someone's pull request as a maintainer and need to approve, request changes, merge, or close it.

Performs comprehensive review with style and accuracy checks, then provides an interactive workflow for approval actions. Automatically detects external contributors and adapts communication tone (warm/welcoming for external, professional for internal).

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

### Step 3: Present Test Deployment and Review Guidance

**CRITICAL**: This step must be completed and presented to the user IMMEDIATELY after Step 2 and BEFORE starting Step 4. Do not delay this output.

#### Part A: Fetch Test Deployment URL

1. Get all pulumi-bot comments from the PR and extract the most recent one:

   ```bash
   gh api repos/pulumi/docs/issues/{{arg}}/comments \
     --jq '.[] | select(.user.login == "pulumi-bot") | {created_at, body}' | tail -1
   ```

2. Extract the deployment base URL from the `body` field:
   - Look for the pattern: `http://www-testing-pulumi-docs-origin-pr-{PR_NUMBER}-{COMMIT_HASH}.s3-website.us-west-2.amazonaws.com`
   - Store this as the base deployment URL

3. Handle edge cases:
   - **No pulumi-bot comment yet**: Display "⏳ Test deployment is not ready yet (no pulumi-bot comment found). The deployment typically appears within a few minutes after pushing commits. You can review the code now and check the deployment later."
   - **Multiple comments exist**: Use the most recent based on `created_at` timestamp
   - **Comment exists but no URL**: Treat same as no comment case

#### Part B: Analyze Changes and Generate Targeted Review Guidance

**IMPORTANT**: The guidance must be based on the **actual substance of changes in the diff**, not generic style guide rules.

1. **Analyze the diff** from Step 2 (`gh pr diff {{arg}}`) to identify:
   - New sections or headings added (lines with `+ ##`, `+ ###`, etc.)
   - New code examples or code blocks (lines with `+` followed by `````)
   - New images or assets (lines containing `+ ![` or `+ <img`)
   - Modified links or references (lines with `+ [` or `+ <a href`)
   - Configuration changes (frontmatter, YAML)
   - Table additions/modifications
   - New callouts, warnings, or notes
   - Content restructuring (moved sections, reordered content)
   - Terminology changes (consistent patterns of replacements)

2. **Generate change-specific guidance** based on what actually changed:

   ✅ **Good**: "Verify the new TypeScript code example on the Components page runs correctly"
   ✅ **Good**: "Check that the reorganized sections flow logically from basic to advanced concepts"
   ❌ **Avoid**: "Check formatting, broken links, code examples rendering, headings"
   ❌ **Avoid**: "Verify images display correctly, have reasonable file size, and have alt text"

3. **Construct direct URLs** for each changed documentation page:

   **URL mapping pattern**: Remove `content/` prefix, remove `.md`/`_index.md` suffix, add trailing `/`, prepend base deployment URL

   **Examples**:
   - `content/docs/iac/concepts/components/_index.md` → `[base-url]/docs/iac/concepts/components/`
   - `content/blog/my-post.md` → `[base-url]/blog/my-post/`

   **CRITICAL**: Each changed page MUST have its own direct, clickable link. Do NOT just show the base URL.

4. **Group guidance by page/file** with 2-4 specific items per page based on what changed

#### Part C: Display the Review Guidance

**TIMING**: Display this output IMMEDIATELY after Step 2 completes, BEFORE starting the comprehensive AI review in Step 4. This allows users to review the deployment while the AI performs its analysis.

**Format** (adapt based on whether deployment URL is available):

**If deployment URL is available:**

```markdown
## 🔍 Test Deployment Review

**Deployment URL**: [base-url]

### Review the Following Changes

**[Page/File Name]** - [Direct link to this specific page]
- [ ] [Specific change-based item from diff analysis]
- [ ] [Specific change-based item from diff analysis]
- [ ] [Specific change-based item from diff analysis]

**[Another Page/File Name]** - [Direct link to this specific page]
- [ ] [Specific change-based item from diff analysis]
- [ ] [Specific change-based item from diff analysis]

[... continue for all pages with substantive changes ...]

---

*Please review these specific changes in the deployment before proceeding.*
```

**If deployment URL is NOT available:**

```markdown
## 🔍 Test Deployment Review

⏳ Test deployment is not ready yet (no pulumi-bot comment found)

The deployment typically appears within a few minutes after pushing commits.
You can proceed with the code review now and check the deployment later.

### When the deployment is ready, review:

**[Page/File Name]**
- [ ] [Specific change-based item from diff analysis]
- [ ] [Specific change-based item from diff analysis]

**[Another Page/File Name]**
- [ ] [Specific change-based item from diff analysis]
- [ ] [Specific change-based item from diff analysis]

[... continue for all pages with substantive changes ...]

---

*The deployment URL will be available at: http://www-testing-pulumi-docs-origin-pr-{{arg}}-[commit-hash].s3-website.us-west-2.amazonaws.com*
```

#### Part D: Handle Edge Cases

- **Large file lists**: If more than 10 files changed, prioritize documentation pages (`.md` files under `content/`) and show "... and N more files" for others
- **Purely mechanical changes**: If changes are only typo fixes or whitespace (no new content, no structural changes), note: "Changes appear to be mechanical fixes (typos, formatting). Suggest quick scan rather than detailed review."
- **Infrastructure/non-visual changes**: For non-content files (`.yaml`, `.json`, build scripts), explain what behavior to verify rather than visual appearance
- **Blog posts**: For blog posts, focus on readability, images, and code examples rather than cross-references
- **Mixed content types**: Group by content type (docs pages, blog posts, examples, infrastructure)

### Step 4: Perform Comprehensive Review

Review the PR changes using the **Review Criteria** section from `docs-review.md`.

This includes all standard checks: style guide enforcement, spelling/grammar, link validation, code examples, file standards, SEO, special cases (file moves, redirects, infrastructure changes), and role-specific guidelines for documentation vs blog/marketing content.

### Step 5: Present Review Findings

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

   This summary helps users understand scope when choosing an action in Step 6.

### Step 6: Present Action Choices

Use AskUserQuestion to present these 6 options (messaging tone adapts: warm/welcoming for external contributors, professional for internal):

1. **Approve** (Recommended)
   - Approve PR with feedback
   - Use: When PR is ready to merge

2. **Approve and merge**
   - Approve and merge immediately (squash)
   - Use: When PR is ready for immediate merge

3. **Make changes and approve**
   - Make minor edits, then approve
   - Use: For small fixes (typos, formatting) that preserve contributor's credit

4. **Request changes**
   - Post review feedback with request-changes flag
   - Use: When author should address issues

5. **Close PR**
   - Close with explanation
   - Use: When PR doesn't fit or is no longer needed

6. **Do nothing yet**
   - Exit without action
   - Use: Need more time or team discussion

### Step 7: Preview Planned Actions and Get Confirmation

**CRITICAL**: Always show the user what will happen before executing any action.

Generate a preview based on the user's choice from Step 6:

#### For "Approve"

```text
## Preview: Approval Comment

Comment: See "Approve" template in Message Templates section (adapts to contributor type)

GitHub command: gh pr review {{arg}} --approve --body "{{COMMENT}}"
```

#### For "Approve and merge"

```text
## Preview: Approval and Merge

Comment: See "Approve and merge" template in Message Templates section (adapts to contributor type)

GitHub commands:
1. gh pr review {{arg}} --approve --body "{{COMMENT}}"
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
7. Approve with comment from "Make changes and approve" template (adapts to contributor type)
8. Return to original branch
```

#### For "Request changes"

```text
## Preview: Request Changes Comment

Comment format: See "Request changes" template in Message Templates section (adapts to contributor type)

Include specific issues with line numbers from Step 4 findings and suggestion code blocks.

GitHub command: gh pr review {{arg}} --request-changes --body "{{COMMENT}}"
```

#### For "Close PR"

```text
## Preview: Close PR

Comment format: See "Close PR" template in Message Templates section (adapts to contributor type)

Include clear explanation of why closing.

GitHub commands:
1. gh pr comment {{arg}} --body "{{COMMENT}}"
2. gh pr close {{arg}}
```

#### For "Do nothing yet"

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

- **"Yes, proceed"**: Continue to Step 8 (execution)
- **"Edit comment"**:
  - Ask user: "Please provide the revised comment text:"
  - Generate updated preview with new comment
  - Request confirmation again with same options
  - Repeat until user confirms or cancels
- **"Change action"**: Return to Step 6 (action selection) and let user choose again
- **"Cancel"**: Display "No action taken on PR #{{arg}}." and exit

### Message Templates

Use these templates when executing actions. Select the appropriate template based on contributor type (determined in Step 1):

**Approve**:

- External: "Thank you for this contribution! [Brief specific praise, 1 sentence max, or omit if nothing stands out]. Welcome to the community! 🎉"
- Internal: "LGTM! [Any specific positive feedback or minor suggestions]"

**Approve and merge**:

- External: "Thank you for this contribution! [Brief specific praise, 1 sentence max]. Merging now. 🎉"
- Internal: "LGTM! Merging now."

**Make changes and approve**:

- External: "I've applied some minor style and formatting fixes. Thank you for your contribution! 🙏"
- Internal: "Applied some style/formatting fixes. LGTM!"

**Request changes**:

- External: Format with:
  - Brief opening: "Thank you for this contribution!"
  - Brief acknowledgment of good aspects if applicable (1 sentence max)
  - Specific issues with line numbers
  - Suggestion code blocks for fixes
  - Simple closing: "Feel free to mention @claude if you need help with these changes"
- Internal: Format with:
  - Professional opening
  - Specific issues with line numbers
  - Suggestion code blocks for fixes
  - Clear action items

**Close PR**:

- External: Format with:
  - Brief thank you: "Thank you for taking the time to contribute!"
  - Clear, kind explanation of why closing
  - Brief acknowledgment of valuable aspects if applicable
  - Suggest alternatives if appropriate
  - Simple closing: "We appreciate your interest in Pulumi!"
- Internal: Clear explanation of why closing

### Step 8: Execute Confirmed Action

**Using the confirmed/edited content from Step 7**, execute the action based on the user's choice and contributor type:

**For "Approve"**:

Use "Approve" template from Message Templates section based on contributor type.

```bash
gh pr review {{arg}} --approve --body "{{COMMENT}}"
```

**For "Approve and merge"**:

Use "Approve and merge" template from Message Templates section based on contributor type.

```bash
gh pr review {{arg}} --approve --body "{{COMMENT}}"
gh pr merge {{arg}} --auto --squash
```

**For "Make changes and approve"**:

1. Save current branch: `git rev-parse --abbrev-ref HEAD`
2. Check out PR: `gh pr checkout {{arg}}`
3. Make the requested changes (from Step 7) using Edit/Write tools
4. Show the diff: `git diff`
5. Display the diff in the conversation
6. Ask user: "Proceed with commit and approval? (Yes/No)"
   - If No: Ask "Would you like to make additional changes or cancel? (Additional changes/Cancel)"
     - Additional changes: Return to making edits, show diff again, repeat confirmation
     - Cancel: Return to original branch and exit without committing
   - If Yes: Continue to next step
7. Commit: `git add . && git commit -m "Apply style and formatting fixes\n\nCo-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"`
8. Push: `git push`
9. Approve (use "Make changes and approve" template from Message Templates section):

   ```bash
   gh pr review {{arg}} --approve --body "{{COMMENT}}"
   ```

10. Return: `git checkout <original-branch>`

**For "Request changes"**:

Use "Request changes" template from Message Templates section based on contributor type.

```bash
gh pr review {{arg}} --request-changes --body "{{COMMENT}}"
```

**For "Close PR"**:

Use "Close PR" template from Message Templates section based on contributor type.

```bash
gh pr comment {{arg}} --body "{{COMMENT}}"
gh pr close {{arg}}
```

**For "Do nothing yet"**:

No confirmation needed - exit directly with message: "No action taken. You can run this command again when ready."

### Step 9: Report Execution Results

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

- **Preview accuracy**: Previews show the planned action with exact comment text. The actual execution in Step 8 uses the confirmed (or edited) content from Step 7.
- **Preview-to-execution consistency**: What users see in the preview is exactly what gets posted to GitHub. Always use the confirmed comment text from Step 7 when executing in Step 8.
- **Edit flexibility**: The "Edit comment" option allows users to refine tone, add context, or adjust wording before posting. After editing, show the updated preview and confirm again.
- **Communication tone**: Use warm, welcoming language with external contributors. Keep praise brief and specific (1 sentence max).
- **Encouragement**: Make contributors feel welcomed to the Pulumi community
- **Credit**: Use "make changes" option judiciously - only for minor fixes that don't reduce contributor's credit for the work
- **Branch safety**: Always track current branch and return to it after PR checkout, especially if errors occur
- **Error handling**: See error recovery template in Step 9
- **Token efficiency**: Generate preview text once in Step 7 and reuse it in Step 8. For large diffs (>100 lines), show summary with option to expand full diff.
- **Large diffs**: When showing diffs in "Make changes and approve", if the diff exceeds 100 lines, show a summary (files changed, lines added/removed) and ask if user wants to see the full diff
- **Contributor type caching**: Store the contributor type (internal/external) result from Step 1 and reuse it throughout Steps 6-9. Don't re-query the GitHub API if the user changes actions during preview.
