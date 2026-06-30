---
title: Getting started with Neo
title_tag: Getting started with Pulumi Neo
h1: Getting started with Pulumi Neo
meta_desc: Learn how to set up Pulumi Neo for your organization and run your first infrastructure task through conversational AI.
aliases:
- /docs/pulumi-cloud/neo/get-started/
- /docs/iac/neo/get-started/
- /docs/ai/neo/get-started/
menu:
    ai:
        name: Get Started
        parent: ai-home
        weight: 10
        identifier: ai-get-started
---

## Enabling and Disabling Neo

Neo is enabled by default. To disable Neo for your organization, navigate to **Settings > Neo Settings > General** in the Pulumi Cloud console.

## VCS integration

Connecting a [version control integration](/docs/integrations/version-control/) significantly enhances Neo's capabilities, though it is not required. Pulumi supports [GitHub](/docs/integrations/version-control/github-app/), [Azure DevOps](/docs/integrations/version-control/azure-devops-integration/), and [GitLab](/docs/integrations/version-control/gitlab/). A VCS integration:

- Allows Neo to read repository content for better context
- Enables pull request creation
- Streamlines the code change workflow

Neo can still provide code change suggestions without a VCS integration, but you'll need to apply the changes and open PRs manually.

To set up a VCS integration, see the [version control docs](/docs/integrations/version-control/).

## Neo's permission model

Neo operates within the conversing user's [RBAC entitlements](/docs/pulumi-cloud/access-management/rbac/) and cannot perform actions that the user couldn't perform themselves. This means:

- There's no privilege escalation risk or special administrative access required
- Each user's Neo conversations are isolated from other users

### Read-only mode

When you create a Neo task, you can choose between two permission levels:

| Option | What Neo can do |
| :--- | :--- |
| **Use my permissions** | Full access (default behavior) |
| **Read-only** | Read, preview, and create PRs. No infrastructure mutations. |

Read-only mode takes your existing permissions and removes the ability to make changes. Neo never gets more access than you have, only less. If you can view a stack but not a particular environment, Neo in read-only mode also cannot see that environment.

In read-only mode, Neo can still read your infrastructure state, run previews, write and refactor code, create branches, and open pull requests. The only difference is that Neo cannot trigger deployments or other write operations in Pulumi Cloud directly.

## Quick Start Guide

### Enable Neo for Your Organization

Neo is automatically enabled for eligible organizations. To access Neo:

1. Navigate to [Pulumi Cloud](https://app.pulumi.com/signin)
2. Click on **Agent Tasks** within the **Neo** section in the left navigation menu

> If Neo doesn't appear in your navigation, verify that AI features have not been disabled for your organization. AI controls are located in **Settings > Neo Settings > General**.

### Create Your First Task

Each conversation with Neo is called a "task" - a contained unit of work where Neo helps you accomplish a specific infrastructure goal.

Let's run a simple infrastructure [task](/docs/ai/tasks/) to see Neo in action

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
   - Request approval before opening a [pull request](/docs/ai/pull-requests/)
   - Create a [PR](/docs/ai/pull-requests/) with clear documentation of the changes

## Considerations and Limitations

- Code Changes Only - Neo can only modify infrastructure through code. It cannot perform API or UI actions like configure deployments, updating stack configurations, or managing environments in Pulumi Cloud.
- Cannot Create Repos - Neo cannot create new repositories or initialize new Git repos. It only works within existing repositories.
- Cannot Create New Projects - Neo cannot initialize new Pulumi projects. It can only work within existing projects that are already set up.
