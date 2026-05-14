---
title: "Pulumi Neo Slash Commands for Real Platform Workflows"
date: 2026-07-14
meta_desc: "Use Pulumi Neo slash commands and operating modes for practical platform workflows such as base image refreshes, drift cleanup, and reviewed automation."
meta_image: meta.png
feature_image: feature.png
authors:
    - pablo-seibelt
tags:
    - neo
    - platform-engineering
    - cookbook
social:
    twitter: |
        Slash commands are useful when they encode real platform workflows.

        See Pulumi Neo patterns for image refreshes, drift cleanup, and reviewed automation.
    linkedin: |
        Pulumi Neo slash commands work best when they turn repeated platform workflows into reviewed, auditable actions.

        This cookbook covers practical commands for base image refreshes, drift cleanup, and operating modes that keep humans in control.
    bluesky: |
        Pulumi Neo slash commands can encode real platform workflows: base image refreshes, drift cleanup, reviewed automation.

        Learn more in the post.
---

Platform engineering teams often find themselves caught between two worlds: the need for high-velocity infrastructure changes and the reality of manual SRE toil. Tasks like upgrading runtimes, refreshing AMIs for security compliance, and cleaning up drift are essential but repetitive. [Pulumi Neo](/product/neo/) closes this gap by turning these workflows into interactive, AI-assisted experiences.

By combining slash commands with operating modes, you can encode your team's best practices into shortcuts the team can run with predictable guardrails. By the end, you will have a set of Neo slash commands for common SRE tasks like runtime upgrades and drift cleanup.

<!--more-->

## Closing the SRE-toil gap

Slash commands in Neo are more than just shortcuts. They are pre-configured prompts that capture the context, constraints, and expected outcomes of a specific task. When paired with operating modes, they allow you to delegate the heavy lifting to Neo while maintaining the exact level of oversight your organization requires.

## Upgrade runtimes

**Slash command**: `/upgrade-runtime`

Upgrading Lambda runtimes or container base images across a stack fleet is a classic example of toil.

**Intent**: Identify and upgrade outdated runtimes to the latest supported versions.

**Slash command body**:
> "Scan all stacks in the current project for AWS Lambda resources using Node.js 16 or 18. Draft a change to upgrade them to Node.js 20, ensuring that any associated environment variables or layers remain compatible. Prepare a reviewed workflow for the update."

**Expected output**: Neo identifies the affected resources, modifies the Pulumi code, and presents a preview of the changes for approval.

## Refresh base images

**Slash command**: `/refresh-base-image`

Security vulnerabilities often require immediate base-image refreshes across compute platforms. This recipe standardizes the response pattern so teams can update AMIs, container images, or VM images without hardcoding a one-time image ID into the slash command.

**Intent**: Identify resources using an outdated approved image family and move them to the current approved image for that environment.

**Slash command body**:
> "Find compute resources using the previous approved base image for the current environment. Resolve the latest approved image from our ESC environment value `baseImages.current`, draft the code changes, and include rollout notes for instances, Auto Scaling Groups, and container workloads. Prepare a reviewed workflow."

**Expected output**: Neo prepares reusable code changes and a deployment plan that respects your availability constraints.

## Clean up drift

**Slash command**: `/cleanup-drift`

Infrastructure drift is inevitable, but managing it shouldn't be a full-time job.

**Intent**: Detect resources that have diverged from their defined state and bring them back into alignment.

**Slash command body**:
> "Run a refresh on the current stack to detect drift. For any resources where the live state differs from the Pulumi state, draft a plan to remediate the drift. If the change was intentional, suggest the code updates to match the live state."

**Expected output**: A detailed report of drifted resources and a guided workflow to either revert the changes or update the code.

## Rotate stack secrets

**Slash command**: `/rotate-stack-secrets`

Managing secret rotation across multiple environments is high-stakes and error-prone.

For stack secrets stored in [Pulumi Cloud](/product/pulumi-cloud/), Neo can help trace references and prepare the reviewed update.

**Intent**: Rotate specific stack secrets and update the associated resources.

**Slash command body**:
> "Identify all resources using the 'dbPassword' stack config key. Generate a new random password, update the secret in Pulumi Cloud, and draft the necessary changes to update the resources using it. Prepare a reviewed workflow."

**Expected output**: Neo helps draft the rotation plan and reviewed code changes to update the infrastructure.

## Bump provider dependencies

**Slash command**: `/bump-dependencies`

Keeping your Pulumi programs up to date with the latest provider versions ensures you have access to new features and security fixes.

**Intent**: Update Pulumi provider packages and resolve any breaking changes.

**Slash command body**:
> "Check for updates to the 'pulumi-aws' and 'pulumi-kubernetes' packages. Update them to the latest minor versions in the package.json or requirements.txt. Run a preview to ensure no breaking changes were introduced."

**Expected output**: Updated dependency files and a clean preview confirming compatibility.

## Rename stacks

**Slash command**: `/rename-stack`

Refactoring stack names or moving resources between stacks can be complex due to state dependencies.

**Intent**: Safely rename a stack while preserving state and updating dependents.

**Slash command body**:
> "I need to rename the 'staging-old' stack to 'staging-new'. Draft a plan that uses pulumi stack rename, updates any StackReference callers in dependent projects, and calls out backend-specific checks before the reviewed workflow runs."

**Expected output**: A step-by-step rename plan that preserves state in place, updates dependencies, and avoids an unnecessary import cycle.

## Operating modes and safety

The power of these recipes comes from how you run them. Neo's operating modes and permissions settings provide a safety net for platform teams:

1. **Review mode**: Neo requests approval for previews, updates, and pull requests. This is the default mode and the safest fit for production workflows.
1. **Balanced mode**: Neo can perform routine work but requests approval before `pulumi up`.
1. **Auto mode**: Neo runs without approval prompts, which is best reserved for tightly scoped non-production workflows.
1. **Read-only permissions**: Read-only access is a permissions setting, not an operating mode. Use it for exploration workflows where Neo should analyze infrastructure and draft changes without mutating live environments. See [Neo read-only mode](/blog/neo-read-only-mode/) for details.

By combining these modes with custom slash commands, you give platform teams a faster way to draft, review, and apply infrastructure changes under your standards and controls.
