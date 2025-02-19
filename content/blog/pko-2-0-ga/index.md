---
title: "Announcing GA: Pulumi Kubernetes Operator 2.0 is Here!"
date: 2025-02-19
draft: false
meta_desc: "Today, we're announcing the GA of Pulumi Kubernetes Operator 2.0! Discover the new features and improvements that make managing Kubernetes easier than ever."
meta_image: "meta.png"
authors:
  - eron-wright
  - meagan-cojocar

tags:
  - kubernetes
  - operator
  - releases
  - features

social:
    twitter: "The GA release of Pulumi Kubernetes Operator 2.0 is here! Enhanced logging control, improved observability, and smarter workspace management make infrastructure automation easier than ever. Get started today!"
    linkedin: "Announcing Pulumi Kubernetes Operator 2.0 GA: Now with enhanced logging control, richer controller events, and flexible workspace management. Experience enterprise-grade infrastructure automation with improved observability and resource management in your Kubernetes clusters."

---

Today marks an exciting milestone as we announce the General Availability (GA) release of the Pulumi Kubernetes Operator 2.0! This release builds upon the foundation we [laid during the beta phase](/blog/pulumi-kubernetes-operator-2-0/), delivering a production-ready solution that transforms how teams manage their cloud infrastructure.
<!--more-->

[Learn more about the Pulumi Kubernetes Operator in our documentation](/docs/iac/using-pulumi/continuous-delivery/pulumi-kubernetes-operator)

## What Is the Pulumi Kubernetes Operator?

The Pulumi Kubernetes Operator brings infrastructure automation directly to your Kubernetes cluster. By treating your infrastructure as native Kubernetes resources, it enables teams to manage their entire cloud environment—from databases to DNS records—using familiar Kubernetes workflows and tools.

Imagine having a dedicated infrastructure automation engine running within your cluster, continuously ensuring your cloud resources stay in sync with your desired state. That's exactly what the Pulumi Kubernetes Operator delivers, complete with the observability and control you need for production environments.

## The Evolution to 2.0

Pulumi Kubernetes Operator 2.0 introduces a completely new architecture for running Pulumi programs. The key changes include:

- Each Stack now runs in its own dedicated Workspace pod, rather than within the Operator pod
- A new Workspace Custom Resource manages the workspace pod lifecycle
- Stack operations are coordinated through a new Update custom resource
- The Stack Custom Resource API remains the primary interface, maintaining backward compatibility

This architecture delivers improved resource isolation, better secrets management, and flexible workspace customization options. The pod-per-stack model ensures reliable resource allocation and clear operational boundaries for each deployment.

## What's New in GA?

The GA release introduces three powerful capabilities that give you more control over your deployments:

### Enhanced Logging Control

You can now set the log verbosity level of the Pulumi CLI for any given stack or workspace. This feature offers granular control over logging output, making debugging and fine-tuning your deployment process more efficient.

### New Controller Events for Better Instrumentation

Additional controller events have been introduced to provide richer instrumentation and observability. These events offer improved insights into the operator's behavior, enabling more effective monitoring of your infrastructure.

### Workspace Reclaim Policy

Managing workspace lifecycles is now even more flexible with the new `WorkspaceReclaimPolicy` field in the Stack specification. This enhancement allows you to define policies for reclaiming workspaces, ensuring optimal resource management and cleanup.

## See It in Action

Here's a practical example of deploying an NGINX stack using the operator. This code creates a Stack resource that pulls a Pulumi program directly from a Git repository:

<!-- TODO, potential example, we can do any Eron thinks is best -->

## Start Using It Today

We are excited to see how you will use these new features to transform your cloud operations. Share your experiences, questions, and insights with us through our community forums or Slack channel.

[Get started with the Pulumi Kubernetes Operator in our documentation](/docs/iac/using-pulumi/continuous-delivery/pulumi-kubernetes-operator)

Happy deploying!
