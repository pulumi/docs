---
title: Automations
title_tag: Neo Automations
h1: Automations
meta_desc: Schedule Neo tasks to run on a recurring basis with auto-approval and read-only defaults; results delivered as pull requests for review.
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    ai:
        name: Automations
        identifier: ai-automations
        parent: ai-home
        weight: 25
---

Automations turn any Neo task into recurring work. Define a prompt, set a cadence, and Neo runs the task at that interval, producing a [pull request](/docs/ai/pull-requests/) each time that goes through your normal review process.

## What you can do with an automation

Drift detection, dependency updates, compliance scans, and cost reviews are typical starting points: work that's important every time but identical enough that a prompt can capture it. Because every run produces a pull request, branch protection rules and required reviewers still gate what reaches your infrastructure. The autonomy level is configurable per automation for tighter oversight.

## Defaults that fit recurring work

Scheduled tasks default to two settings. Approval mode is [**auto**](/docs/ai/tasks/#task-modes), so the task proceeds without waiting for human confirmation at each step. Permission mode is [**read-only**](/docs/ai/tasks/#task-modes), so the task can read state and propose changes through pull requests, but it can't write directly to your infrastructure. The per-automation setting takes precedence; the org-level default applies next; auto/read-only is the final fallback.

## Creating an automation

Open **Neo**, then the **Automations** tab, then **New automation**. You can start from a template (provider freshness check, encryption audit, backup audit, activity digest) or from a blank canvas. The form asks for a name, the prompt (which includes the same integration selector as an ad-hoc task), and the frequency (hourly, daily, weekdays, or weekly). Save the automation and it begins running at the next scheduled tick.

You can edit or delete an automation from the **Automations** tab.

## How automations interact with the rest of Neo

Automations inherit the rest of Neo's context model. [Custom Instructions](/docs/ai/settings/) at the organization and project level apply to scheduled tasks just as they do to ad-hoc ones. [MCP integrations](/docs/ai/integrations/mcp/) use the credentials of whoever configured the integration (the OAuth identity for OAuth-based integrations, the API token or key for token-based ones). [CLI integrations](/docs/ai/integrations/cli/) default to inheriting the organization's connected CLIs, overridable per automation.

## How permissions work

A scheduled task runs with the [RBAC permissions](/docs/pulumi-cloud/access-management/rbac/) of the user who scheduled it, evaluated at execution time. If that user's permissions change between scheduling and execution, the new permissions apply.

## Limitations

Scheduled tasks are the only automation type available today.
