---
title: Task API (preview)
title_tag: Task API (preview) | Pulumi Agents
h1: Task API (preview)
meta_desc: Create agent tasks, send follow-up messages, and retrieve task events through the preview task API.
menu:
    ai:
        name: Task API (preview)
        parent: ai-reference
        identifier: ai-agents-reference
        weight: 10
---

Use the [preview task API](/docs/reference/cloud-rest-api/neo/#post-apipreviewagentsorgnametasks) to create tasks, send follow-up messages, and retrieve task events.

## Run a task with an organization-created agent

{{< pulumi-cloud "pulumi-agents" />}}

The task-creation schema includes `agentDefinitionId` for selecting an agent. Access to this preview field must be enabled for your organization.
