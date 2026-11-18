---
title: Start your first task
title_tag: Start your first task | Pulumi Agents
h1: Start your first task
meta_desc: Ask Neo to review stack encryption settings, check its findings, and request a pull request if changes are needed.
aliases:
- /docs/pulumi-cloud/neo/get-started/
- /docs/iac/neo/get-started/
- /docs/ai/neo/get-started/
menu:
    ai:
        name: Start your first task
        parent: ai-start
        weight: 20
        identifier: ai-get-started-neo
---

Neo is the built-in agent in Pulumi Agents. In this walkthrough, you ask Neo to check a stack's storage encryption settings. Sending the request starts a task where Neo reports its findings and you can ask questions as needed. If a change is needed, you can continue the task by asking Neo to prepare a pull request.

<span id="enabling-and-disabling-neo"></span>
<span id="enable-neo-for-your-organization"></span>
<span id="vcs-integration"></span>

## Before you begin

You need a [Pulumi Cloud account](https://app.pulumi.com/signin) and access to a stack that manages storage resources, such as buckets or disks. Pulumi Agents must be [enabled for your organization](/docs/ai/concepts/neo/settings/#neo-access).

Neo can review the resource configuration recorded in Pulumi Cloud using only the stack you select.

<span id="quick-start-guide"></span>
<span id="create-your-first-task"></span>

## Start a task

1. Open **Agents** in Pulumi Cloud.
1. Select **Neo** in the agent selector.
1. Select **Add context**, then **Stack**, and choose the stack to review.
1. Open **Task options**, select **Permissions**, and choose **Read-only**.
1. If your organization has connected CLI or MCP integrations, deselect them in the task composer for this review.
1. Enter the following request, then select **Send message**:

    ```text
    Review this stack's storage resources. Report whether encryption is
    enabled and show the resource configuration that supports each answer.
    If you cannot verify a setting, say what information is missing.
    Do not make changes.
    ```

<span id="neos-permission-model"></span>
<span id="read-only-mode"></span>

Read-only mode blocks writes to Pulumi Cloud. Connected tools use their own credentials. See [Permissions and approvals](/docs/ai/agents/permissions/) before adding that access.

<span id="considerations-and-limitations"></span>

## Review the findings

Check the storage resources and encryption settings Neo cites. If they meet your requirements, the review is complete. If the stack configuration leaves a setting unresolved, check that resource in your cloud provider before deciding whether to change it.

## Request a code change

If the findings show that a change is needed, [connect your repository](/docs/ai/agents/integrations/#repositories), and check the [preview prerequisites](/docs/ai/agents/previews/#prerequisites). Give Neo the repository URL and describe the change:

```text
Prepare a pull request to enable encryption for the resource we just
reviewed. Use this repository: <repository URL>.
Include the preview results and explain any checks you could not complete.
Do not apply the change.
```

[Review the code and preview](/docs/ai/agents/review-changes/) before merging. Use your team's deployment workflow to apply the change.

## Continue working

See [task controls](/docs/ai/agents/tasks/) to return to a saved task, share its findings, or stop work in progress.
