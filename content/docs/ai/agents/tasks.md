---
title: Work with tasks
title_tag: Work with tasks | Pulumi Agents
h1: Work with tasks
meta_desc: Continue agent tasks, collaborate with teammates, and respond through Pulumi Cloud or Slack.
aliases:
- /docs/ai/concepts/neo/tasks/
- /docs/pulumi-cloud/neo/tasks/
- /docs/iac/neo/tasks/
- /docs/ai/tasks/
- /docs/ai/neo/tasks/
menu:
    ai:
        name: Work with tasks
        parent: ai-agents
        identifier: ai-agents-tasks
        weight: 10
---

A task records your request, the agent’s progress, and the result, such as a diagnosis or a pull request. The agent keeps working when you close the browser.

<span id="setting-entity-context"></span>
<span id="integrations"></span>

For help starting a task and selecting a stack, see [Start your first task](/docs/ai/get-started/neo/#create-your-first-task).

<span id="choose-an-agent"></span>
<span id="start-a-task-in-pulumi-cloud"></span>
<span id="continue-a-task"></span>
<span id="how-tasks-work"></span>
<span id="context-sharing-and-history"></span>

## Return to a task {#task-history}

In Pulumi Cloud, open **Agents** and use **Search tasks** to find the task by name. Open it to see what the agent did and whether it needs a response. Reply there to answer a question, correct a detail, or ask the agent to revise its work.

<span id="review-the-result"></span>
<span id="approvals-and-previews"></span>
<span id="pull-requests"></span>
<span id="next-steps"></span>

If the agent opened a pull request, follow the link from the task to [review the proposed changes](/docs/ai/agents/review-changes/).

<span id="when-to-use-plan-mode"></span>

## Review a plan {#plan-mode}

To review the agent’s approach before it makes changes, enable **Plan mode** in the message box before you send your request. The agent posts its plan in the task and waits. Ask for revisions or approve the plan to let the agent proceed.

<span id="task-modes"></span>

After you approve the plan, the agent follows its usual [approval mode](/docs/ai/agents/permissions/#separate-approvals-from-access) for individual actions.

<span id="work-with-teammates"></span>
<span id="work-from-slack"></span>

## Work with teammates {#ownership-and-sharing}

For an agent your team creates, send a teammate the task URL. Teammates with [access to the task](/docs/ai/agents/permissions/#give-teammates-access) can read its history. Those with permission to contribute can reply in the same task. If the task started in Slack, teammates can reply in the original thread after [linking their Pulumi accounts](/docs/ai/integrations/slack/#setting-up-the-integration).

Neo tasks are private by default. To let others read one, select **Share**, choose **Anyone in** your organization, then select **Copy link** and **Done**. Organization members with the link can read the messages and results. They still need their own access to open linked stacks or resources. To turn off sharing, select **Shared**, choose **Private**, and select **Done**.

## Stop and resume a task {#interruptions-and-resuming}

Select **Cancel** beside the message box to stop the agent. To resume, send a new message in the same task with what you want it to do next.
