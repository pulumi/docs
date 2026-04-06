---
title: Tasks
title_tag: Tasks in Pulumi Neo
h1: Tasks in Pulumi Neo
meta_desc: Learn about tasks, the primary entity for interacting with Neo to perform infrastructure operations.
meta_image: /images/docs/meta-images/docs-meta.png
aliases:
- /docs/pulumi-cloud/neo/tasks/
- /docs/iac/neo/tasks/
- /docs/ai/neo/tasks/
menu:
    ai:
        name: Tasks
        parent: ai-home
        weight: 20
        identifier: ai-tasks
---

Tasks are Neo's primary unit of work. Each task is a conversation where you describe what you want to accomplish, and Neo handles the infrastructure changes.

## How tasks work

When you start a task, Neo outlines the steps it intends to take so you can see its approach before it begins. For example, if you ask Neo to update outdated Lambda functions, it might outline:

1. Identify all Lambda functions using Node.js
1. Determine the appropriate target runtime for each
1. Create code changes to update the runtime versions
1. Run a preview to validate all changes
1. Create a pull request with the updates

From there, Neo moves to execution, working through each step and seeking approvals based on the active [task mode](#task-modes).

## Plan Mode

For complex tasks, you can enable Plan Mode for thorough upfront discovery before Neo starts executing. Without Plan Mode, Neo outlines its approach and moves forward. With Plan Mode, Neo shifts into a dedicated research-and-planning phase where it investigates your environment in depth, synthesizes what it finds, and iterates with you before anything changes.

When Plan Mode is enabled, Neo:

1. **Investigates your environment** by examining existing infrastructure, reading relevant code, checking dependencies, and researching patterns, showing you what it finds in real time
1. **Synthesizes a grounded plan** explaining what it will do and why, referencing specific things it discovered like stack configurations and dependencies
1. **Iterates with you** through normal conversation so you can challenge assumptions, ask for alternatives, or request more detail
1. **Waits for your explicit approval** before any execution begins

To enable Plan Mode, select the plan button when starting a task.

### When to use Plan Mode

If your task is straightforward and you could describe the outcome in a sentence, skip Plan Mode and let Neo work directly. Use Plan Mode when the task is complex enough that upfront research changes the outcome:

- **Complex multi-stack operations** where understanding dependencies matters
- **Unfamiliar infrastructure** where discovery reduces churn
- **Autonomous execution** where plan approval is your key control point before Neo runs without step-by-step oversight

## Task modes

Task modes control how much autonomy Neo has during execution. At any time during a task, the operating mode can be set to:

- **Review mode** (default): Running `pulumi preview`, running `pulumi up`, and opening a PR all require approval.
- **Balanced mode**: Neo will only request approval before running `pulumi up`.
- **Auto mode**: Neo will not request any approvals.

Task modes are independent of Plan Mode. Task modes control what approvals Neo requires during execution, while Plan Mode controls what happens before execution. You can combine them: for example, use Plan Mode with Auto Mode to review the approach thoroughly up front, then let Neo execute without stopping.

## Approvals and previews

Depending on the task mode, Neo seeks approval before taking certain actions like running `pulumi up` or opening a PR.

At any time, you can ask Neo to run a [pulumi preview](/docs/iac/cli/commands/pulumi_preview/). If Neo proposes code changes as part of a task, it will also request to run a preview to validate the changes. [Learn more](/docs/ai/running-previews/) about Neo and previews.

## Pull requests

If a task results in code modifications, Neo will offer to open a [pull request](/docs/ai/pull-requests/) once you are satisfied with the implementation. PRs can also be modified after they have been opened.

## Context, sharing, and history

### Setting entity context

You can set the [stack](/docs/iac/concepts/stacks/) and [repository](/docs/iac/concepts/projects/) context when initiating a task. This helps Neo understand exactly where to focus its operations.

### Ownership and sharing

Each task belongs to the user who created it. By default, tasks are private, but you can share any task with others in your organization by generating a read-only link. Shared tasks let teammates see the full conversation, including Neo's reasoning, the actions it took, and the outcome.

Sharing preserves security boundaries:

- Viewers can see the conversation but cannot trigger any actions
- Links to stacks or resources within the shared task still enforce the viewer's existing [RBAC](/docs/pulumi-cloud/access-management/rbac/) permissions
- The original task owner retains full control

### Interruptions and resuming

Tasks continue running even if you close your browser or navigate away. Neo will keep working until it finishes the task or encounters a situation that needs your approval. When you return, it will show you any progress made while you were away.

### Task history

Neo tasks are saved and accessible through the Agent Tasks page in Pulumi Cloud. The entire task history is available at any time, though the task cache may be lost if the agent idles for an hour or more.
