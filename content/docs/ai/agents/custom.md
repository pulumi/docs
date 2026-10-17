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

Build a custom agent when you want to define its job and instructions yourself. For example, an agent can check infrastructure code for missing cost-allocation tags and propose a pull request with the required values.

## Create the agent

In the agent catalog, choose **Create your own from scratch**. Give the agent a name and description that help teammates decide when to use it. For the tagging example:

- **Name:** Cost-allocation tags
- **Description:** Find missing cost-allocation tags in infrastructure code and propose a pull request to add them

## Write its instructions

Write instructions that apply every time the agent runs. Describe its job, the information it should use, and the result it should produce. Put assignment-specific details, such as the repository or stack to check, in the task.

Enter the instructions in **System prompt**. For example:

```text
Check infrastructure code for resources missing the cost-allocation tags
required by our tagging guide at docs/tagging.md in the assigned repository.

Read the guide and the repository's contribution instructions before making
changes. Use the tag values documented for the project. If a required value
is missing or ambiguous, ask in the task instead of inventing one.

Add missing tags without changing existing tag values or unrelated code.
Open a pull request that lists the resources changed and the tags added.
Leave validation and deployment to the repository's existing pipeline.
Do not merge the pull request or deploy the changes.
```

Replace the example path and requirements with your team's own. The agent needs access to any repository or tool you reference; including a path or URL does not grant access.

Saved agent instructions replace your organization's AI preference instructions. Include any organization-wide requirements the agent must follow. Use roles and credentials to enforce access restrictions.

## Connect tools and assign access

Follow the shared setup steps to [connect tools](/docs/ai/agents/configure/#connect-the-tools-it-needs) and [assign access](/docs/ai/agents/configure/#set-its-access). For the tagging example, the agent needs a version control integration that can read the repository, push a branch, and open a pull request.

## Assign a task

[Save the agent](/docs/ai/agents/configure/#save-and-assign-a-task) and give it a specific assignment. Include the repository URL and stack name. For example:

> Check the staging stack in `<repository URL>` for missing cost-allocation tags. Propose a pull request using the tag requirements and values documented in docs/tagging.md.

Review the proposed changes and check results before merging. If the agent lacks information, add it to the task. Update the saved instructions when a correction should apply to future tasks, too.

Once the agent can complete the job, you can [add a schedule or event trigger](/docs/ai/agents/triggers/) to run it automatically.
