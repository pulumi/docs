---
title: Getting started with Neo
title_tag: Getting started with Pulumi Neo
h1: Getting started with Pulumi Neo
meta_desc: Learn how to set up Pulumi Neo for your organization and run your first infrastructure task through conversational AI.
aliases:
- /docs/pulumi-cloud/neo/get-started/
- /docs/iac/neo/get-started/
- /docs/ai/get-started/
menu:
    ai:
        name: Get started with Neo
        parent: ai-neo
        weight: 10
        identifier: ai-get-started
---

## Enabling and Disabling Neo

Neo is enabled by default. To disable Neo for your organization, navigate to **Settings > Neo Settings > General** in the Pulumi Cloud console.

## VCS integration

A [version control integration](/docs/integrations/version-control/) is optional. With one connected, Neo can read your code and open pull requests. Pulumi supports [GitHub](/docs/integrations/version-control/github-app/), [Azure DevOps](/docs/integrations/version-control/azure-devops-integration/), [GitLab](/docs/integrations/version-control/gitlab/), [Bitbucket](/docs/integrations/version-control/bitbucket/), and [Custom VCS](/docs/integrations/version-control/custom-vcs/). A VCS integration:

- Allows Neo to read repository content for better context
- Enables pull request creation
- Streamlines the code change workflow

Neo can still provide code change suggestions without a VCS integration, but you'll need to apply the changes and open PRs manually.

To set up a VCS integration, see the [version control docs](/docs/integrations/version-control/).

## Neo's permission model

Neo operates within the conversing user's [RBAC entitlements](/docs/administration/concepts/rbac/) and cannot perform actions that the user couldn't perform themselves — there's no privilege escalation, and tasks are private to the user who created them unless they [share one](/docs/ai/neo/tasks/#ownership-and-sharing). For the full picture of which identity Neo acts as on each surface, how permission and approval modes constrain it, and how to scope its access, see [Neo's permissions model](/docs/ai/neo/permissions/).

### Read-only mode

When you create a task, you can run Neo with your full permissions ("Use my permissions", the default) or in read-only mode. Read-only mode takes your existing permissions and removes the ability to trigger writes in Pulumi Cloud: Neo can still read state, run previews, write and refactor code, and open pull requests, but it can't trigger deployments or other Pulumi Cloud write operations directly. Neo never gets more access than you have, only less.

Read-only is scoped to Pulumi Cloud. It does not, on its own, prevent Neo from opening [ESC](/docs/esc/) environments you can open or reaching the cloud accounts those environments unlock — see [ESC, secrets, and downstream cloud access](/docs/ai/neo/permissions/#esc-secrets-and-downstream-cloud-access).

## Quick Start Guide

### Enable Neo for Your Organization

Neo is included on every current Pulumi plan and is on by default, so there is nothing to turn on. (Organizations still on the legacy Starter, Pro, or per-stack plans need to move to a current plan first — see [pricing](/pricing/).) To access Neo:

1. Navigate to [Pulumi Cloud](https://app.pulumi.com/signin)
2. Click on **Agent Tasks** within the **Neo** section in the left navigation menu

> If Neo doesn't appear in your navigation, verify that AI features have not been disabled for your organization. AI controls are located in **Settings > Neo Settings > General**.

### Create Your First Task

Each conversation with Neo is called a "task" - a contained unit of work where Neo helps you accomplish a specific infrastructure goal.

Let's run a simple infrastructure [task](/docs/ai/neo/tasks/) to see Neo in action

1. Start with a read-only analysis task by prompting Neo:

    `Which of my resources are not using their latest major version?`

2. Neo will:
   - Acknowledge your request
   - Search through your infrastructure
   - Present findings in a clear format

3. As a follow-up, ask Neo what you should address first:

    `Which version issue should I address first?`

4. Neo will respond with a plan to address the most important outdated version it found. Go ahead and ask it to propose a change for the highest priority finding:

    `Can you propose the necessary code change to address the highest priority item?`

5. Depending on the scale of the issue, Neo may propose a plan for addressing it; or, Neo may get to work right away to create a PR. Neo will then:

   - Ask for confirmation before making changes
   - Generate the necessary code modifications
   - Request approval before opening a [pull request](/docs/ai/neo/pull-requests/)
   - Create a [PR](/docs/ai/neo/pull-requests/) with clear documentation of the changes

## Considerations and Limitations

- Changes go through code, deployments, and APIs - Where your Pulumi Cloud configuration (deployment settings, stack configuration, environment definitions) is managed in IaC, Neo changes it through code and pull requests. Where it isn't, Neo can edit it directly through the Pulumi Cloud APIs. Neo can also run deployments (`pulumi up`) and, where it has access, cloud CLI operations, so its effects reach beyond code. See [Neo's permissions model](/docs/ai/neo/permissions/) for the full picture.
- Creating repositories requires individual access - Neo creates repositories as your own connected version control account, not as the shared Pulumi app, so you must [grant individual access](/docs/integrations/version-control/github-app/#individual-user-setup) to your provider first. Custom VCS servers do not support repository creation at all.
- Cannot Create New Projects - Neo cannot initialize new Pulumi projects. It can only work within existing projects that are already set up.
