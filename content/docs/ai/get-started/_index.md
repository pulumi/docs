---
title: Getting started with Neo
title_tag: Getting started with Pulumi Neo
h1: Getting started with Pulumi Neo
meta_desc: Learn how to set up Pulumi Neo for your organization and run your first infrastructure task through conversational AI.
meta_image: /images/docs/meta-images/docs-meta.png
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

## Public Preview Access

Neo is in public preview and currently free to use. Users will receive ample warning before any pricing changes go into effect. Using Neo to optionally run [`pulumi preview`](/docs/iac/neo/running-previews/) consumes workflow minutes. Learn more about workflow minutes on our [pricing page](https://www.pulumi.com/pricing/#faq-pricing).

## Enabling and Disabling Neo

Neo is enabled by default. To disable Neo for your organization, navigate to the [Access Management page](/docs/pulumi-cloud/access-management/), under the Settings section. AI features can be enabled or disabled in the Pulumi Copilot section. If Copilot was previously disabled, it will need to be enabled to use Neo.

## GitHub App Installation

Installing the [Pulumi GitHub App](/docs/iac/using-pulumi/continuous-delivery/github-app/) significantly enhances Neo's capabilities, though it is not required. The Pulumi GitHub App:

- Allows Neo to read repository content for better context
- Enables pull request creation
- Streamlines the code change workflow

Neo can still provide code change suggestions without the GitHub App, but you'll need to apply the changes and open PRs manually.

To install the GitHub App, see the [GitHub integration guide](/docs/iac/using-pulumi/continuous-delivery/github-app/).

## Neo's Permission Model

Neo operates within the conversing user's [RBAC entitlements](/docs/pulumi-cloud/access-management/rbac/) and cannot perform actions that the user couldn't perform themselves. This means:

- There's no privilege escalation risk or special administrative access required
- Each user's Neo conversations are isolated from other users

## Quick Start Guide

### Enable Neo for Your Organization

Neo is automatically enabled for eligible organizations. To access Neo:

1. Navigate to [Pulumi Cloud](https://app.pulumi.com)
2. Click on **Agent Tasks** within the **Neo** section in the left navigation menu

> If Neo doesn't appear in your navigation, verify that AI features have not been disabled for your organization. AI controls are located on the [Access Management page](/docs/pulumi-cloud/access-management/), in the Pulumi Copilot section.

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

- GitHub Only - Neo only works with GitHub repositories. GitLab, Bitbucket, and other platforms are not supported yet.
- Code Changes Only - Neo can only modify infrastructure through code. It cannot perform API or UI actions like configure deployments, updating stack configurations, or managing environments in Pulumi Cloud.
- Cannot Create GitHub Repos - Neo cannot create new GitHub repositories or initialize new Git repos. It only works within existing repositories.
- Cannot Create New Projects - Neo cannot initialize new Pulumi projects. It can only work within existing projects that are already set up.
