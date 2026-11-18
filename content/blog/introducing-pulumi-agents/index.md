---
title: "Introducing Pulumi Agents"

date: 2026-11-18T04:00:00-08:00

draft: false

meta_desc: "Introducing Pulumi Agents: AI agents you can create and customize to carry out infrastructure tasks and ongoing responsibilities for your team."

feature_image: feature.png

authors:
    - pulumi-ai

tags:
    - product-launches

category: product
schema_type: auto

social:
    twitter: |
        Ask an agent to build an isolated staging environment and it inspects your stacks, writes the infrastructure code, and opens a pull request with its reasoning attached.

        That's Pulumi Agents. Here's how they work.
    linkedin: |
        Tell an agent to spin up a staging environment for a service, isolated from production, and it gets to work: reading your Pulumi stacks and infrastructure code, checking the Context API for dependencies, and pulling in your deployment docs.

        What comes back is a pull request: the proposed change, the reasoning behind it, and the checks it ran. If requirements are unclear, it asks before anything ships.

        That's one assignment. Agents can also stick around for ongoing work: a drift agent that responds when live infrastructure diverges from code, an incident agent that investigates when an alert fires, a scheduled cost review that proposes changes on its own timeline. Each one keeps its instructions, integrations, and context across every task.

        We call this Pulumi Agents, and it's live today. Here's how to set one up.
    bluesky: |
        When Pulumi detects drift between recorded state and live infrastructure, an agent can investigate it, propose a pull request to keep an intentional change, or explain how to reverse one that shouldn't have happened.

        This is Pulumi Agents, live today. Here's how one works.
---

It's hard to overstate how much AI agents have changed the way we make software. When it comes to managing your cloud infrastructure, though, we're still very much in the early days. This is why we're excited to announce **Pulumi Agents**, your agentic infrastructure team.

Pulumi Agents are digital teammates that assist with incident investigation, program and resource planning, or proactive infrastructure maintenance.

The user experience with Pulumi Agents will feel familiar to anyone who has used agents before: you define the goal or tasks an agent performs, the constraints it must respect, and its permissions. Pulumi then runs the agent in the cloud, where it works with your existing infrastructure and connected tools to prepare findings and pull requests for your team to review.

## Delegate infrastructure work

To carry out a task, agents combine infrastructure code, recorded resource state, and update history with data from connected systems. They can retrieve the runbooks and engineering standards your team keeps in Confluence, Notion, or GitHub, through connections authorized to read them. During an incident, an agent can consult those runbooks, query logs and metrics, and use Pulumi's [Context API](https://www.pulumi.com/docs/discovery-governance/concepts/context-api/) to examine dependencies between resources and stacks as it prepares a diagnosis or proposed fix.

Authorized teammates can collaborate with the agent on the same task through Pulumi Cloud or Slack. The agent can ask for information or a decision, and teammates can ask it to explain a finding or revise its proposal.

Tasks can start on request, in response to events, or on a schedule. Pulumi includes trigger setup for Datadog monitor alerts, Honeycomb triggers, and PagerDuty incidents, plus generic webhooks for other systems. Pulumi events, such as detected drift or failed updates, can also start tasks, and schedules can kick off recurring work such as dependency reviews.

## Define each agent's responsibility and access

You can define agents in code, keeping their instructions, integrations, and roles in source control. Your team can then review changes to an agent's responsibility and access before they're applied.

Each agent has its own identity and Pulumi Cloud role, independent of the user who creates it. That role scopes access to stacks and Pulumi ESC environments, while credentials for connected systems govern access to those systems separately.

Pulumi Cloud's [role-based access control](https://www.pulumi.com/docs/ai/agents/permissions/) distinguishes permission to create or edit an agent from permission to participate in its tasks. Every request a teammate makes in a task must be allowed by both that person's permissions and the agent's role.

## Use agents in Pulumi Delivery pipelines

Pulumi Delivery lets you add agents as steps in your deployment pipelines. For example, a release pipeline can ask an agent to assess proposed changes against your team's risk criteria.

The agent returns its assessment in a format you define, such as a risk level with an explanation. A pipeline rule can then require human approval for high-risk changes before deployment.

## Get started

You can create a Pulumi agent with the coding agent you already use. Install the [Pulumi CLI](https://www.pulumi.com/docs/install/) and add the [Pulumi skills](https://github.com/pulumi/agent-skills#installation), then ask your coding agent to create and configure a Pulumi agent for your team. You can also use the Pulumi Cloud console to customize a prebuilt agent or create your own.

The [agent configuration guide](https://www.pulumi.com/docs/ai/agents/configure/) explains how to configure an agent and connect the systems it needs. The [events and schedules guide](https://www.pulumi.com/docs/ai/agents/triggers/) covers connecting incoming work and setting up recurring schedules.
