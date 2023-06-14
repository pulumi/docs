---
title_tag: "Pulumi Deployments vs Traditional CI/CD Systems"
meta_desc: How does Pulumi deployments compare to traditional CI/CD systems?
title: "Vs. Traditional CI/CD"
h1: "Pulumi Deployments vs. traditional CI/CD"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  pulumicloud:
    parent: deployments
    weight: 7
aliases:
  - /docs/intro/deployments/versus/
---

Pulumi Deployments is a cloud automation platform. It can serve as a CI/CD system, but it has the flexibility to do much more. How does it compare to something like GitHub Actions, GitLab CI, or Terraform Enterprise?

Pulumi Deployments is purpose-built for infrastructure. It provides both a "platform in a box" that let's your team get up and running quickly with features like [Review Stacks](/docs/pulumi-cloud/deployments/review-stacks), in addition to a powerful API that you can build on top of to power custom infrastructure workflows. Pulumi Deployments has the flexibility to handle more than just source control events - something that CI/CD systems typically focus on exclusively. Other systems assume that the primary mechanism for a workflow run is a git commit. That assumption may be true in the domain of application development, but it falls apart when working in the domain of cloud infrastructure automation.

Pulumi Deployments provides a fully featured, git commit-driven deployment workflow for the simple case. But when deploying infrastructure, a single program often maps to dozens, hundreds, or even thousands of environments. SaaS companies often spin up dedicated infrastructure in response to a customer signing up for a particular SKU. Platform teams often enable self-service of Kubernetes clusters through internal tools and portals. High-scale, globally distributed systems often deploy the same component dozens of times into multiple regions. In all of these systems, you are not pushing a single commit through your three traditional dev/staging/production environments. You are writing complex orchestration at scale.

The Deployments Platform offers a combination of Deployment Settings that describe all necessary dependencies, and Deployment Triggers that run deployments via Automation API, the REST API, and more. Stacks can be programmatically created and configured via the Settings REST API, and updated via Triggers. This unlocks platform scenarios that aren’t possible with tools that only offer `git push` workflows.

## Using Deployments with your Existing CI/CD System

Many teams are at the stage where CI/CD is more than enough. They are happy with GitHub Actions, and wonder why they might consider migrating from GitHub Actions to Deployments. You don’t have to make that choice, as the two are better together. Teams often configure Pulumi Deployments on their stacks, and then trigger deployments via the REST API from within a GitHub Actions workflow. This gives you access to Deployments Platform tools such as Click to Deploy from the Pulumi Cloud UI, while keeping the familiarity of your existing CI/CD workflow. As Pulumi adds more built-in capabilities to the Deployments Platform like [Drift Detection](https://github.com/pulumi/service-requests/issues/173), [TTL stacks](https://github.com/pulumi/service-requests/issues/149), and [Ephemeral Environments](https://github.com/pulumi/service-requests/issues/206), you’ll automatically accrue the productivity benefits.

![Pulumi Deployments Platform Architecture](../deployments.png)
