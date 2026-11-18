---
title: Review proposed changes
title_tag: Review proposed changes | Pulumi Agents
h1: Review proposed changes
meta_desc: Review an agent's proposed code, preview results, and pull request before deploying through your team's workflow.
menu:
    ai:
        name: Review proposed changes
        parent: ai-agents
        identifier: ai-agents-review
        weight: 30
---

Ask an agent to prepare a pull request when an assignment requires an infrastructure code change. Review and merge the pull request, then use your team's deployment workflow to apply it.

<span id="specify-the-change"></span>

For repository and credential setup, see [Integrations](/docs/ai/agents/integrations/) and [Permissions and approvals](/docs/ai/agents/permissions/).

## Check the code and preview

Read the proposed diff and confirm that it addresses the assignment without unrelated changes. Check the preview for resource creations, updates, deletions, and replacements. Review any policy results and test output alongside the code.

Some preview values, such as the IDs of new resources, can remain unknown until an update. If the preview fails or is unavailable, ask the agent to explain what it could not validate before deciding whether to proceed.

See [Run previews](/docs/ai/agents/previews/) for setup and approval controls, and [Prepare pull requests](/docs/ai/agents/pull-requests/) for the version control workflow.

## Request revisions

Reply in the task with the specific change you need. Identify the file, resource, or preview result that needs attention. Ask for another preview when a revision changes the infrastructure plan.

For shared agents, teammates need [permission to contribute](/docs/ai/agents/permissions/#give-teammates-access). A Neo task shared through a read-only link does not let viewers direct the agent; send feedback to the task owner.

## Merge and deploy

Run a final preview against the code you intend to merge. An earlier preview may no longer reflect changes to the code, configuration, or infrastructure, and does not guarantee that an update will succeed.

Use your repository's review and merge requirements. After merging, deploy through the workflow your team uses to validate and apply infrastructure changes. Approving an action in an agent task does not replace repository reviews or deployment approvals.
