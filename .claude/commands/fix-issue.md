---
description: Analyze a documentation issue and create an implementation plan (investigates problem and plans solution)
---

# Usage

`/fix-issue <issue-number>`

**Use this when:** You need to address a GitHub issue and want help investigating the problem and creating a step-by-step implementation plan.

Analyzes GitHub issue #{{arg}} and creates a comprehensive plan to address it, acting as a technical content engineer focused on improving documentation quality.

---

## Process

### 1. Gather issue details

Use `gh issue view {{arg}}` to retrieve the complete issue information:

- Read the full issue description to understand the problem
- Review labels to identify issue type (bug, enhancement, clarification, etc.)
- Read all comments and discussion to understand user pain points
- Note any related issues or PRs mentioned
- Identify the affected product area or documentation section

### 2. Research current documentation

Use semantic search and file tools to thoroughly investigate:

- Locate the specific documentation files mentioned or affected
- Read the current content to understand what's written today
- Identify what's missing, incorrect, outdated, or unclear
- Review related documentation pages for consistency and cross-references
- Search for similar patterns elsewhere in the docs that might have the same issue
- Check if code examples exist and whether they're tested

### 3. Review guidelines

Before proposing changes, verify compliance with:

- `AGENTS.md` — Repository conventions, build/test workflow, file movement rules, SEO requirements
- `STYLE-GUIDE.md` — Writing style, heading capitalization, code formatting, terminology
- Existing documentation patterns in the same section to maintain consistency
- Google Developer Documentation Style Guide for topics not covered in STYLE-GUIDE.md

### 4. Create implementation plan

Develop a detailed plan with these components:

1. **Analysis** — Clearly explain:
   - What the current documentation says (or doesn't say)
   - Why it's problematic for users
   - What impact this has on the user experience
   - The root cause of the issue

2. **Solution** — Describe the specific changes:
   - New content to write (with outline of key points)
   - Sections to restructure (with proposed new organization)
   - Text to clarify (with examples of better wording)
   - Outdated content to remove
   - Code examples to add or fix

3. **Files to modify** — List exact file paths and locations:
   - Full paths from repository root (e.g., `content/docs/clouds/aws/get-started.md`)
   - Specific section headings where changes occur
   - Line numbers if known

4. **Implementation steps** — Break work into logical, ordered tasks:
   - Update section headings and structure
   - Rewrite or add explanatory content
   - Add, update, or fix code examples in `/static/programs`
   - Add cross-references and internal links
   - Update or create diagrams/images (if needed - Be wary of images due to maintenance overhead)
   - Add aliases if moving files (critical for SEO)
   - Update related documentation for consistency

5. **Verification** — Define how to validate the fix:
   - Run `make lint` to check for errors
   - Run `make serve` to preview rendering at <http://localhost:1313>
   - Test any code examples using program tests
   - Verify all links work (internal and external)
   - Confirm technical accuracy with subject matter experts if needed
   - Check readability and clarity from user perspective

6. **Considerations** — Note special requirements or impacts:
   - Version-specific changes needed across multiple doc versions
   - Related docs that need updates for consistency
   - Breaking changes or deprecations to communicate
   - SEO implications (aliases, redirects) if moving or deleting content
   - Localization impacts if docs are translated
   - Whether this reveals a larger documentation gap to address separately

### 5. Present for approval

**IMPORTANT: Do NOT implement without user approval.**

Present the complete plan to the user including:

- Clear, numbered steps in logical order
- Exact file paths with section headings or line numbers
- Specific commands that will be run (e.g., `make lint`, `make serve`)
- Any assumptions made or decisions that need user input
- Estimated scope (minor fix vs. major restructuring)

If the issue is ambiguous, ask clarifying questions before creating the plan. If multiple valid approaches exist, present options with pros/cons and ask for the user's preference.
