---
user-invocable: false
description: Issue body templates and field guidance for slack-to-issue
---

# Issue Templates

Use these templates and guidelines to generate well-structured issue bodies from Slack conversations.

---

## Standard Issue Body Template

```markdown
### Problem description

[1-3 sentence summary of the issue. State what the page currently says or doesn't say, and what the impact is on users trying to follow the docs.]

- [Issue type] on: [URL of the affected page]

[Relevant quote from Slack if it clarifies the problem — 1-2 short excerpts max]

### Suggestions for a fix

[Any specific suggestions from the Slack conversation. If none were given, write "No specific fix suggested." If the fix is obvious from the issue type, briefly state it.]

---

_Reported via Slack: [URL of the original message]_
```

---

## Field Guidance

### Problem description

**Do:**

- Lead with the user-visible symptom ("The docs say X, but the actual behavior is Y")
- Include the specific page URL as a bullet point in the problem description
- Quote brief, relevant excerpts from the Slack message when they clarify the problem
- Use the issue type to frame the opening sentence:
  - **Bug**: "The documentation incorrectly states..."
  - **Gap**: "The documentation does not cover..."
  - **Clarity**: "The documentation is unclear about..."
  - **Enhancement**: "Users have requested documentation for..."

**Don't:**

- Include full conversation transcripts
- Add speculation or analysis beyond what was in the Slack thread
- Include @mentions or Slack-specific formatting

### Suggestions for a fix

- If the user in Slack suggested a specific fix or linked to a fix, include it
- If the Slack conversation contains a correct answer (e.g., another team member answered correctly), note it: "The correct information is: [answer from thread]"
- If no suggestion exists, write: "No specific fix suggested."

### Slack source line

Always add the footer line. If you have the message URL, use:

```markdown
_Reported via Slack: [URL]_
```

---

## Example Issues

### Bug example

```markdown
### Problem description

The getting started guide for AWS incorrectly states that `pulumi up` requires
the `--yes` flag to deploy without confirmation. This flag was removed in Pulumi v3.x
and causes an error for anyone following the guide today.

- Documentation bug on: https://www.pulumi.com/docs/clouds/aws/get-started/

> "I keep getting 'flag not found: yes' when I follow the getting started guide"

### Suggestions for a fix

Remove the `--yes` flag from all examples in the getting started guide.

---

_Reported via Slack: https://pulumi-community.slack.com/archives/C01234ABCDE/p1234567890123456_
```

### Gap example

```markdown
### Problem description

The Pulumi ESC documentation does not explain how to use environment variable
interpolation across nested environments. Users must currently discover this
through trial and error or community support.

- Missing content on: https://www.pulumi.com/docs/esc/environments/

### Suggestions for a fix

Add an example showing how to reference a variable from a parent environment
using `${environments.parent.values.variableName}` syntax.

---

_Reported via Slack: https://pulumi-community.slack.com/archives/C01234ABCDE/p9876543210987654_
```

---

## Title Patterns by Issue Type

| Type | Pattern | Example |
| --- | --- | --- |
| Bug | `[Component]: [incorrect thing] is wrong/outdated` | `Pulumi ESC: rotate secrets example uses deprecated API` |
| Gap | `[Component]: Missing documentation for [feature]` | `Pulumi Cloud: Missing documentation for audit log filtering` |
| Clarity | `[Component]: [topic] is unclear or confusing` | `Getting started: Azure credentials setup is unclear` |
| Enhancement | `[Component]: Add documentation for [feature/scenario]` | `Registry: Add documentation for multi-language SDK examples` |

**Component names** (use these consistently):

- `Pulumi IaC` — core SDK, stacks, state, config
- `Pulumi Cloud` — Pulumi Cloud console, teams, policies
- `Pulumi ESC` — environments, secrets, config
- `Registry` — package registry, provider docs
- `Getting started` — onboarding, quickstarts
- `CLI` — command reference, CLI flags
- `Tutorials` — tutorials and guides section
- `pulumi.com` — marketing/website (not docs content)
