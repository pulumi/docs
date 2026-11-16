---
title: Build a custom agent
title_tag: Build a custom agent | Pulumi Agents
h1: Build a custom agent
pulumi_cloud_feature: pulumi-agents
meta_desc: Define a custom agent's job, write reusable instructions, and connect the tools it needs to work.
menu:
    ai:
        name: Build a custom agent
        parent: ai-agents-create-manage
        identifier: ai-agents-custom
        weight: 25
---

Build a custom agent when you want to define its job and instructions yourself. For example, a checkout investigation agent can use application logs, recent deployments, and cloud configuration to diagnose failures and prepare fixes for review.

## Create the agent

In the agent catalog, choose **Create your own from scratch**. Give the agent a name and description that help teammates decide when to use it. For the checkout investigation example:

- **Name:** Checkout investigation
- **Description:** Investigate checkout failures using our incident runbook and prepare fixes for review

## Write its instructions

Write instructions that apply every time the agent runs. Describe its job, the information it should use, and the result it should produce. Put assignment-specific details, such as the repository or stack to check, in the task.

Enter the instructions in **System prompt**. For example:

```text
Investigate checkout failures using the incident runbook at
runbooks/checkout.md in the checkout repository.

Compare application errors during the reported incident with recent
deployments and cloud configuration changes. Follow the runbook's diagnostic
steps and link to the logs, changes, and resources that support your findings.
Distinguish confirmed causes from hypotheses. Ask for missing information
when you cannot determine the cause.

If the evidence supports a code fix, read the repository's contribution
instructions and open a pull request explaining the cause and proposed fix.
Do not merge the pull request or deploy the changes.
```

Replace the example path and requirements with your team's own. The agent needs access to any repository or tool you reference; including a path or URL does not grant access.

Saved agent instructions replace your organization's AI preference instructions. Include any organization-wide requirements the agent must follow. Use roles and credentials to enforce access restrictions.

## Connect tools and assign access

Follow the shared setup steps to [connect tools](/docs/ai/agents/configure/#connect-the-tools-it-needs) and [assign access](/docs/ai/agents/configure/#set-its-access). For this example, give the agent access to checkout logs, relevant cloud resources, and the repository containing its code and runbook. The version control integration must allow it to push branches and open pull requests.

## Assign a task

[Save the agent](/docs/ai/agents/configure/#save-and-assign-a-task) and give it a specific assignment. Include the affected environment, incident time window, and links to relevant alerts. For example:

> Investigate the increase in checkout errors in production between 14:00 and 14:30 UTC on October 20, 2026. Use the alert at `<alert URL>` and the checkout repository at `<repository URL>`. Explain the cause and prepare a fix for review if the evidence supports one.

Review the findings and any proposed pull request. Check validation results before merging. If the agent lacks information, add it to the task. Update the saved instructions when a correction should apply to future tasks, too.

Once the agent can complete the job, you can [add a schedule or event trigger](/docs/ai/agents/triggers/) to run it automatically.
