---
title_tag: "Pulumi Neo"
meta_desc: Pulumi Neo is an agentic AI that enables conversational infrastructure management through natural language interactions.
title: Pulumi Neo
h1: Pulumi Neo
meta_image: /images/docs/meta-images/docs-meta.png
aliases:
- /docs/iac/neo/
- /docs/neo/
menu:
    cloud:
        name: Neo
        parent: cloud-home
        weight: 5
        identifier: cloud-neo
---

## Overview

Neo is a purpose-built infrastructure automation agent that can carry out platform engineering tasks on your behalf. Neo enables platform engineers to make natural language requests, which Neo autonomously plans and executes. Rather than writing code or running CLI commands for routine tasks, you can simply tell Neo what you need:

- "Find all Lambda functions running deprecated runtimes and upgrade them"
- "Fix the S3 buckets that violate our security policies"
- "Analyze what resources depend on our production database"

Beyond maintenance and analysis, Neo can create new infrastructure resources, remove unused components, and refactor code into reusable modules. Neo works across multiple stacks in a single task when needed, like updating connection strings everywhere at once or applying security policies across your entire infrastructure.

Neo understands your intent, creates an execution plan, and handles the implementation through existing [GitHub workflows](/docs/iac/using-pulumi/continuous-delivery/github-actions/) and [Pulumi operations](/docs/iac/cli/).

### Key benefits

#### Accelerate Delivery

Automate multi-step workflows and routine maintenance to respond faster to development team needs and infrastructure requirements.

#### Reduce Context Switching

Platform teams manage infrastructure across multiple repositories, clouds, and tools. Neo understands this complexity and can work across your entire infrastructure landscape, eliminating the need to context-switch between different systems.

#### Focus on Strategic Work

Neo handles routine infrastructure tasks that consume platform engineering time. Policy violations, runtime upgrades, and dependency analysis can be delegated to Neo, freeing your team to focus on architecture, optimization, and innovation.

#### Maintain Control and Compliance

Every change Neo makes goes through [pull requests](/docs/pulumi-cloud/neo/pull-requests/), ensuring human review and your existing CI/CD pipeline validations. Neo operates within the [RBAC boundaries](/docs/pulumi-cloud/access-management/rbac/) of the user making the request and automatically enforces your [Pulumi policies](/docs/iac/crossguard/).

## How Neo Fits into Pulumi

Neo complements and enhances your existing Pulumi workflows

- **Pulumi IaC**: Neo generates and modifies Pulumi infrastructure code, working with your existing [programs](/docs/iac/concepts/projects/) and [stacks](/docs/iac/concepts/stacks/)
- **Pulumi ESC**: Neo uses [ESC](/docs/esc/) for secure credential management, enabling it to run previews and validate changes
- **Pulumi Policies**: Neo automatically respects and enforces your [policy packs](/docs/iac/crossguard/), preventing non-compliant changes
- **Pulumi Cloud**: Neo leverages [Pulumi Cloud's](/docs/pulumi-cloud/) infrastructure graph to understand dependencies and impacts

## Tasks

[Tasks](/docs/pulumi-cloud/neo/tasks/) are how Neo plans and executes multi-step operations while maintaining safety through comprehensive controls.

Safety is maintained through [policy controls](/docs/iac/crossguard/) that define guardrails for Neo's operations, ensuring all changes align with your organization's standards and compliance requirements.

## Human-in-the-loop workflows

Neo ensures that critical decisions require human approval and all infrastructure changes go through your existing review processes. This approach provides:

- **Pull request-based changes**: All infrastructure modifications are proposed through PRs, maintaining your standard code review workflow
- **Approval gates**: Intensive operations, such as running [Pulumi preview](/docs/pulumi-cloud/neo/running-previews/), pause for explicit human authorization before proceeding
- **Audit trails**: Complete visibility into what Neo planned, executed, and why

This design gives you the benefits of automation while preserving the control and oversight essential for production infrastructure management.
