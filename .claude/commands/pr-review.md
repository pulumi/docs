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

### Step 6: Execute Chosen Action

Based on the user's choice AND contributor type, execute the appropriate action:

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

1. Ask user: "What changes should I make to the PR? (describe the specific edits needed)"
2. Save current branch: `git rev-parse --abbrev-ref HEAD`
3. Check out PR: `gh pr checkout {{arg}}`
4. Make the requested changes using Edit/Write tools
5. Commit: `git add . && git commit -m "Apply style and formatting fixes\n\nCo-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"`
6. Push: `git push`
7. Approve with appropriate tone:

   *External contributor*:

   ```bash
   gh pr review {{arg}} --approve --body "I've applied some minor style and formatting fixes. Thank you for your contribution! 🙏"
   ```

   *Internal contributor*:

   ```bash
   gh pr review {{arg}} --approve --body "Applied some style/formatting fixes. LGTM!"
   ```

8. Return: `git checkout <original-branch>`

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

---

## Important Notes

- **Communication tone**: Use warm, welcoming language with external contributors. Keep praise brief and specific (1 sentence max).
- **Encouragement**: Make contributors feel welcomed to the Pulumi community
- **Credit**: Use "make changes" option judiciously - only for minor fixes that don't reduce contributor's credit for the work
- **Branch safety**: Always track current branch and return to it after PR checkout
- **Error handling**: If any gh command fails, display the error and ask user how to proceed
