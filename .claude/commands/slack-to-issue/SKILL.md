---
description: Fetch a Slack message and create a well-structured GitHub issue in pulumi/docs or pulumi/registry
---

# /slack-to-issue

Convert a Slack message or thread into a GitHub issue in the appropriate Pulumi docs repository.

## Usage

`/slack-to-issue <slack-url>`

**Required**: Full Slack message URL (from "Copy link" on any Slack message)

**Example**: `/slack-to-issue https://pulumi-community.slack.com/archives/C01234ABCDE/p1234567890123456`

---

## Process

**CRITICAL**: Complete all 6 steps in sequence. Display **[Step X/6]** before each step heading. Never skip a step.

---

### [Step 1/6] Check Prerequisites and Parse URL

**1. Verify Slack plugin:**

Use ToolSearch with query `"slack"` to discover available Slack tools.

- **Found** (any Slack tools returned): Plugin is available. Load the tools and continue.
- **Not found**: Display the setup instructions from `slack-to-issue:references:slack-setup` and **stop**. Do not continue to Step 2.

**2. Parse the Slack URL** from `{{arg}}`:

Extract these components from the URL path `...slack.com/archives/{CHANNEL_ID}/p{TIMESTAMP_RAW}`:

| Component | How to extract |
|---|---|
| **Channel ID** | Segment after `/archives/` (e.g., `C08ABC12345`) |
| **Message timestamp** | Remove the leading `p`, then insert a `.` before the last 6 digits (e.g., `p1234567890123456` → `1234567890.123456`) |
| **Thread timestamp** | Value of `thread_ts` query param, if present (already in decimal format) |

Display a summary:

```
Channel:           [CHANNEL_ID]
Message timestamp: [MESSAGE_TS]
Type:              [Thread reply | Channel message]
```

If the URL cannot be parsed as a Slack message link, display an error and ask the user to paste a valid URL from Slack's "Copy link" option.

---

### [Step 2/6] Fetch Slack Content

**For thread URLs** (URL contains `thread_ts` parameter):

Use the Slack tool for reading a thread, passing the channel ID and thread timestamp (the `thread_ts` parameter value).

**For channel message URLs** (no `thread_ts` parameter):

Use the Slack tool for reading a channel's recent messages, passing the channel ID, then locate the message matching the extracted timestamp.

Display the fetched content:

```
## Slack Content

Channel:  #[channel-name]
Date:     [formatted date]

[Message text]

[Thread replies, if any — show author and text for each]
```

If fetching fails (access denied, channel not found, message too old):

```
❌ Could not fetch message: [error]

Options:
- Paste the message text directly so we can continue
- Check that the Slack app has access to this channel
- See slack-to-issue:references:slack-setup for troubleshooting
```

Offer to accept manually pasted text to continue. If the user provides text, use it in place of the fetched content.

---

### [Step 3/6] Analyze Content

Read the fetched Slack content and extract:

- **Core problem**: What issue is the user describing?
- **Affected area**: Which docs page, feature, or topic is involved?
- **URLs mentioned**: Any `pulumi.com`, GitHub, or docs links in the conversation
- **Fix PRs**: Any GitHub PR links mentioned in the thread (e.g., `github.com/pulumi/*/pull/*`)
- **Code or error snippets**: Any stack traces, error messages, or code blocks

Use this analysis to infer the issue classification. Then ask:

```
AskUserQuestion:
  header: "Issue type"
  question: "What kind of issue does this Slack message describe?"
  options: (based on analysis; put the most likely first with "(Recommended)")
    - "Bug: Docs contain incorrect or outdated information"
    - "Gap: Information is missing or undocumented"
    - "Clarity: Content is confusing or hard to follow"
    - "Enhancement: Request for new or expanded content"
```

Then ask:

```
AskUserQuestion:
  header: "Affected area"
  question: "Which part of the docs is affected?"
  options: (derive the most likely from message context; put it first with "(Recommended)")
    - "[Detected area from message]"
    - "Pulumi IaC / Core SDK"
    - "Pulumi Cloud"
    - "Pulumi ESC"
    - "Registry / Package docs"
    - "Getting started / Tutorials"
    - "Other (I'll specify in the body)"
```

**Determine target repository** based on the confirmed affected area:

| Affected area | Target repo |
|---|---|
| Registry / Package docs, provider-specific documentation, individual provider or SDK API reference | `pulumi/registry` |
| All other areas (core SDK docs, getting started, concepts, CLI, cloud console, tutorials, etc.) | `pulumi/docs` |

If the affected area is ambiguous (e.g., the thread mentions both a provider issue and a core docs gap), ask:

```
AskUserQuestion:
  header: "Target repo"
  question: "Which repository should this issue be filed in?"
  options:
    - "pulumi/docs — core documentation site (Recommended)"
    - "pulumi/registry — provider and package documentation"
```

Store the confirmed issue type, affected area, target repo, and any fix PR links for use in Steps 4–6.

---

### [Step 4/6] Draft Issue

Generate a draft issue title and body using the guidelines in `slack-to-issue:references:issue-templates`.

**Title generation**:

- Format: `[Component]: [concise description]` (e.g., `Pulumi ESC: Missing example for environment variable interpolation`)
- Sentence case after the colon, imperative mood, under 80 characters
- Derive component from confirmed area (Step 3)

Ask for title confirmation:

```
AskUserQuestion:
  header: "Issue title"
  question: "Does this title accurately describe the issue?"
  options:
    - "[Generated title]" (Recommended)
    - "Edit the title"
    - "Generate a different title"
```

If the user chooses to edit: accept freeform input. If "Generate a different title": produce an alternative and ask again.

**Check for duplicate issues** using keywords from the confirmed title:

```bash
gh issue list --repo [TARGET_REPO] --state open --search "[keywords]" --limit 5
```

If matches are found, display them and ask:

```
AskUserQuestion:
  header: "Duplicates?"
  question: "Similar open issues were found. How would you like to proceed?"
  options:
    - "File new issue anyway (Recommended)"
    - "Cancel — I'll comment on an existing issue instead"
```

If the user cancels, display the matching issue URLs and exit without creating a new issue.

**If fix PRs were detected in the thread** (Step 3), include a note in the issue body:

```markdown
> **Note**: A fix may already be in progress: [PR URL]
```

Place this note at the end of the "Suggestions for a fix" section.

**Fetch the available labels** from the target repo:

```bash
gh label list --repo [TARGET_REPO] --limit 100 --json name,description
```

Use the results to offer relevant label options. Always exclude `needs-triage` from the list (it is applied automatically). Present the 3–4 most relevant labels based on the issue type and affected area, ordered by relevance. If no labels seem relevant beyond `needs-triage`, present the top options from the full list.

```
AskUserQuestion:
  header: "Labels"
  multiSelect: true
  question: "Which labels apply? (needs-triage is always included)"
  options: [derived from gh label list output — real label names only]
```

`needs-triage` is always applied and does not need to be selected.

---

### [Step 5/6] Preview and Confirm

Display the complete issue preview:

```
## Issue Preview

Repository:  [TARGET_REPO]
Title:       [title]
Labels:      needs-triage[, additional labels]

---

[Full issue body rendered as markdown]
```

Ask for final confirmation:

```
AskUserQuestion:
  header: "Confirm"
  question: "Ready to create this issue?"
  options:
    - "Yes, create the issue" (Recommended)
    - "Edit the title"
    - "Edit the body"
    - "Cancel"
```

Handle each response:

- **Edit title**: Prompt for new title, return to preview
- **Edit body**: Show the current body, ask for replacement text, return to preview
- **Cancel**: Display "Issue creation cancelled. No changes made." and exit

---

### [Step 6/6] Create Issue and Notify

**Create the issue:**

```bash
gh issue create \
  --repo [TARGET_REPO] \
  --title "{{CONFIRMED_TITLE}}" \
  --body "{{CONFIRMED_BODY}}" \
  --label "needs-triage"
```

Apply any additional labels selected in Step 4 using `--label` for each.

On success, display:

```
✅ Issue created: [ISSUE_URL]
```

**Offer Slack notification:**

```
AskUserQuestion:
  header: "Slack reply"
  question: "Post a reply in the Slack thread linking to the new issue?"
  options:
    - "Yes, post the reply" (Recommended)
    - "No thanks"
```

If yes, use the Slack tool for sending a message to reply in the original channel/thread:

```
Issue filed: [ISSUE_URL]
```

Display final confirmation:

```
✅ Done! Issue: [ISSUE_URL]
[✅ Slack reply posted | ⏭️ Slack reply skipped]
```

---

## Critical Rules

1. **Stop at Step 1 if Slack plugin is missing** — show setup instructions, do not continue
2. **Never create an issue without Step 5 confirmation** — always preview first
3. **`needs-triage` is always included** — it is the entry point for the triage workflow
4. **Target repo is `pulumi/docs` or `pulumi/registry`** — determined in Step 3 based on affected area
5. **Display `[Step X/6]`** before each step heading for progress tracking

---

## Error Recovery

If any step fails unexpectedly:

```
❌ Failed to [action]
Error: [error message]

Recovery options:
- Retry this step
- /slack-to-issue [url] (restart from Step 1)
- Create the issue manually: https://github.com/pulumi/docs/issues/new?template=0-docs-issue.md
```
