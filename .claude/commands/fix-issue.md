---
description: Analyze a GitHub issue and create a comprehensive plan to fix it
---

# Usage
# /fix-issue <issue-number>

You will analyze GitHub issue #{{arg}} and create a comprehensive plan to fix it.

## Step 1: Gather Issue Details

Use `gh issue view {{arg}}` to retrieve the full issue description, labels, comments, and any related context.

## Step 2: Understand the Codebase

Based on the issue details:
- Search for relevant files, functions, or patterns mentioned in the issue
- Understand the current implementation and identify the root cause
- Review related code sections to understand dependencies and impacts
- Check for similar issues or related functionality

## Step 3: Consult Repository Guidelines

Review and follow:
- `AGENTS.md` - Repository conventions and build/test workflow
- `STYLE-GUIDE.md` - Style and formatting requirements
- Related documentation to ensure any proposed changes align with existing patterns

## Step 4: Formulate a Comprehensive Plan

Create a detailed, step-by-step plan that includes:

1. **Analysis**: Clearly identify what's causing the issue or the gap in functionality
1. **Proposed Solution**: Describe the approach to fix the issue
1. **Files to Modify**: List specific files and line numbers that need changes
1. **Implementation Steps**: Break down the work into logical, sequential tasks
1. **Testing Strategy**: How to verify the fix works correctly
1. **Edge Cases**: Identify any edge cases or potential complications
1. **Verification Steps**: Commands to run (lint, build, test) to ensure the fix is complete

## Step 5: Present the Plan

Present the plan to the user using the `ExitPlanMode` tool. Include:
- Clear, concise steps
- Relevant file paths with line numbers
- Commands that will be run
- Any assumptions or decisions that may need user input

**Important**:
- Do NOT start implementing without user approval
- If the issue is ambiguous, ask clarifying questions before planning
- If multiple approaches are viable, present options and ask for the user's preference
- Be specific about what will change and why
- Ensure all changes comply with `STYLE-GUIDE.md` and `AGENTS.md`
