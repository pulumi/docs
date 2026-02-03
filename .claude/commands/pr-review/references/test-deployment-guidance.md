---
user-invocable: false
description: Test deployment URL fetching and review guidance generation
---

# Test Deployment Guidance

**CRITICAL**: This step must be completed and presented to the user IMMEDIATELY after gathering the PR diff and BEFORE starting the comprehensive review. Do not delay this output.

## Part A: Fetch Test Deployment URL

1. Get most recent pulumi-bot comment:
   ```bash
   gh api repos/pulumi/docs/issues/{{arg}}/comments --jq '.[] | select(.user.login == "pulumi-bot") | {created_at, body}' | tail -1
   ```

2. Extract deployment URL pattern:
   ```
   http://www-testing-pulumi-docs-origin-pr-{PR}-{HASH}.s3-website.us-west-2.amazonaws.com
   ```

3. **No comment/URL**: Display "⏳ Deployment not ready. Typically appears in minutes. Review code now, check deployment later."

## Part B: Analyze Changes and Generate Targeted Review Guidance

**IMPORTANT**: Base guidance on **actual diff substance**, not generic rules.

1. **Analyze the diff** to identify:
   - Content (headings `+ ##`, code blocks `+ `````, images `+ ![`, links `+ [`)
   - Config (frontmatter, YAML)
   - Assets (tables, callouts)
   - Structure (moved sections)
   - Terminology (replacements)

2. **Generate specific guidance**:
   - ✅ "Verify new TypeScript example on Components page runs"
   - ✅ "Check reorganized sections flow logically"
   - ❌ Avoid generic: "Check formatting, links, code rendering"

3. **Construct direct URLs**: Remove `content/` prefix, remove `.md`/`_index.md` suffix, add trailing `/`, prepend base URL.
   - Example: `content/docs/iac/concepts/components/_index.md` → `[base]/docs/iac/concepts/components/`
   - **CRITICAL**: Each page needs direct link, not just base URL.

## Part C: Display the Review Guidance

**TIMING**: Display this output IMMEDIATELY after gathering the diff, BEFORE starting the comprehensive AI review. This allows users to review the deployment while the AI performs its analysis.

**Group guidance by page/file** with 2-4 specific items per page based on what changed.

### Format: With Deployment URL

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

### Format: Without Deployment URL

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

## Part D: Handle Edge Cases

- **>10 files**: Prioritize `.md` files under `content/`, show "... and N more"
- **Mechanical changes**: Typos/whitespace only → "Mechanical fixes. Suggest quick scan."
- **Infrastructure/non-visual**: `.yaml`/`.json`/scripts → Explain behavior verification
- **Blog posts**: Focus on readability, images, code (not cross-refs)
- **Mixed types**: Group by docs/blog/examples/infrastructure
