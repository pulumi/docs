---
title_tag: "Pulumi Deployments vs Traditional CI/CD Systems"
meta_desc: Learn how Pulumi Deployments differs from traditional CI/CD systems and why it's uniquely suited for infrastructure as code.
title: "Vs. Traditional CI/CD"
h1: "Pulumi Deployments vs. Traditional CI/CD"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  cloud:
    name: Vs. Traditional CI/CD
    parent: pulumi-cloud-deployments
    weight: 10
    identifier: pulumi-cloud-deployments-versus
aliases:
  - /docs/intro/deployments/versus/
---

Pulumi Deployments is purpose-built for infrastructure automation, complementing and enhancing traditional CI/CD systems like GitHub Actions or GitLab CI rather than replacing them. While simply calling the Pulumi CLI directly in these traditional systems is an option, Pulumi Deployments provides specialized infrastructure-focused functionality that works alongside your existing CI/CD pipelines, addressing the unique needs of infrastructure management that general-purpose CI/CD tools weren't designed to handle.

## Key Differences

### Stack-centric vs. Repository-centric

**Traditional CI/CD:** Typically organized around repositories and branches. Workflows and configuration are usually tied to a specific repo structure or branch strategy.

**Pulumi Deployments:** Organized around Pulumi stacks, which represent environments or deployment targets. Deployment Settings are configured per-stack, not per-repo or per-branch, giving you more flexibility in how you structure your infrastructure deployments.

### Multi-stack Orchestration

**Traditional CI/CD:** Designed primarily for linear application deployments, where a single build artifact moves through environments sequentially.

**Pulumi Deployments:** Built to handle complex multi-stack orchestration patterns common in infrastructure deployments:

- Create complex dependencies between stacks
- Handle parallel deployments across multiple environments
- Deploy a shared infrastructure stack followed by multiple application-specific stacks

### Infrastructure State Management

**Traditional CI/CD:** Generally stateless, focused on building and deploying code that manages its own state elsewhere.

**Pulumi Deployments:** Deeply integrated with Pulumi's state management system, understanding the nuances of infrastructure state:

- Automatically manages state files with proper locking
- Provides built-in drift detection and remediation, scheduled deployments, time to live duration on stacks, review stacks (ephemeral environments)
- Offers operations like refresh, import, and destroy that are infrastructure-specific

### Specialized Operations

**Traditional CI/CD:** Focuses on general-purpose build, test, and deploy operations.

**Pulumi Deployments:** Provides specialized infrastructure operations:

- Preview changes before applying them
- Detect and remediate configuration drift
- Generate comprehensive change reports

### Event-driven Architecture

**Traditional CI/CD:** Primarily responds to source control events like pushes or pull requests.

**Pulumi Deployments:** Has the flexibility to handle more than just source control events:

- Deploy via a REST API
- Trigger deployments based on time schedules
- Coordinate deployments between dependent stacks
- Enable user-initiated deployments through the UI

## Using Deployments with Your Existing CI/CD System

You don't have to choose between Pulumi Deployments and your existing CI/CD system - they work well together. Many teams configure Pulumi Deployments on their stacks and then trigger deployments via their existing CI/CD workflows.

This approach gives you:

- Access to specialized infrastructure operations and the Pulumi Cloud UI
- Consistent infrastructure state management
- The familiarity of your existing CI/CD workflow
- Advanced capabilities like drift detection and management of dependent stacks

As Pulumi adds more capabilities to the Deployments Platform like enhanced drift detection, TTL stacks, and ephemeral environments, you'll automatically benefit from these features while maintaining your existing workflows.
