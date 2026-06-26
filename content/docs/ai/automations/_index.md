---
title: Automations
title_tag: Neo Automations
h1: Automations
meta_desc: Schedule Neo tasks to run on a recurring basis with auto-approval and read-only defaults; results delivered as pull requests for review.
menu:
    ai:
        name: Automations
        identifier: ai-automations
        parent: ai-home
        weight: 25
---

Automations turn any Neo task into recurring work. Define a prompt, set a cadence, and Neo runs the task at that interval. When a run produces changes, Neo opens a [pull request](/docs/ai/pull-requests/) that goes through your normal review process.

## What you can do with an automation

Provider freshness checks, encryption audits, backup audits, and activity digests are typical starting points: work that's important every time but identical enough that a prompt can capture it. When a run produces changes, Neo opens a pull request, so branch protection rules and required reviewers still gate what reaches your infrastructure. The autonomy level is configurable per automation for tighter oversight.

## Defaults that fit recurring work

Scheduled tasks default to two settings. Approval mode is [**auto**](/docs/ai/tasks/#task-modes), so the task proceeds without waiting for human confirmation at each step. Permission mode is [**read-only**](/docs/ai/tasks/#task-modes), so the task can read state and propose changes through pull requests, but it can't write directly to your infrastructure. Settings apply in this order:

1. The per-automation setting, if set
1. The org-level default
1. Auto approval and read-only permissions (the built-in fallback)

## Creating an automation

Open **Neo Tasks**, then the **Automations** tab, then **New automation**. You can start from a template (provider freshness check, encryption audit, backup audit, activity digest) or from a blank canvas. The form asks for a name, the prompt (which includes the same integration selector as an ad-hoc task), and the frequency (hourly, daily, weekdays, or weekly). Save the automation and it begins running at the next scheduled tick.

You can edit or delete an automation from the **Automations** tab. Deleting an automation also removes access to its previous runs.

## How automations interact with the rest of Neo

Automations inherit the rest of Neo's context model. [Custom Instructions](/docs/ai/settings/#custom-instructions) at the organization and project level apply to scheduled tasks just as they do to ad-hoc ones. [MCP integrations](/docs/ai/integrations/mcp/) use the credentials of whoever configured the integration (the OAuth identity for OAuth-based integrations, the API token or key for token-based ones). [CLI integrations](/docs/ai/integrations/cli/) use the credentials configured during setup.

## How permissions work

A scheduled task runs with the [RBAC permissions](/docs/administration/access-identity/rbac/) of the user who scheduled it, evaluated at execution time. If that user's permissions change between scheduling and execution, the new permissions apply.

## Limitations

Scheduled tasks are the only automation type available today.
