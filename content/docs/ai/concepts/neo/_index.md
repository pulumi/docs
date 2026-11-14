---
title: Pulumi Neo
title_tag: Pulumi Neo | Pulumi Agents
h1: Pulumi Neo
meta_desc: Neo is the pre-built personal agent in Pulumi Agents. Investigate infrastructure and make changes from Pulumi Cloud, your terminal, or your editor.
aliases:
- /docs/pulumi-cloud/neo/
- /docs/iac/neo/
- /docs/neo/
- /docs/ai/neo/
menu:
    ai:
        name: Neo
        parent: ai-agents
        identifier: ai-neo-concept
        weight: 20
---

Neo is the pre-built personal agent each user gets with Pulumi Agents. It works with your Pulumi Cloud permissions to investigate infrastructure, preview changes, and update Pulumi code.

## Neo and agents you configure

Neo is ready to use without creating an agent or assigning it a role. Start a task with the work you want it to do.

To create an agent for your team, [configure a pre-built agent](/docs/ai/agents/configure/) or [build a custom agent](/docs/ai/agents/custom/). You save its instructions, select its integrations, and assign a Pulumi Cloud role that determines its access.

## Tasks and access

A [task](/docs/ai/concepts/neo/tasks/) contains your request, the conversation, and Neo's work. You can provide context, answer questions, and ask Neo to revise its approach as the task progresses.

Your Pulumi Cloud permissions determine which stacks and ESC environments Neo can access. Credentials for connected tools determine its access to those tools. Approval settings control when Neo asks before taking an action; approval does not grant additional access. See [Neo permissions](/docs/ai/concepts/neo/permissions/).

## Use Neo

[Start your first task](/docs/ai/get-started/neo/) in Pulumi Cloud, or use Neo from your [terminal](/docs/ai/concepts/neo/neo-in-the-cli/) or [editor](/docs/ai/concepts/neo/neo-in-your-editor/).

- [Work through a task](/docs/ai/concepts/neo/tasks/) and review actions that need approval.
- [Prepare pull requests](/docs/ai/concepts/neo/pull-requests/) and [run previews](/docs/ai/concepts/neo/previews/).
- [Review code](/docs/ai/concepts/neo/code-reviews/) and [schedule recurring work](/docs/ai/concepts/neo/automations/).
- [Configure Neo](/docs/ai/concepts/neo/settings/) and [connect tools](/docs/ai/agents/integrations/).
