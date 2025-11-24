---
title: "Change Management with the Pulumi Kubernetes Operator and Kargo"
h1: "Change Management with the Pulumi Kubernetes Operator and Kargo"
authors: 
  - "elisabeth-lichtie"
tags: ["kargo", "kubernetes", "pko", "change management", "gitops", "argocd", "verification"]
meta_desc: "Use Kargo with the Pulumi Kubernetes Operator to control how infrastructure changes are promoted across environments."
date: "2025-11-25"
meta_image: "kargo-change-mgmt.png"

summary: |
    The Pulumi Kubernetes Operator manages Pulumi stacks as Kubernetes resources, while Kargo provides controlled promotion of changes across environments. Used together, they let you manage infrastructure as code with Pulumi while systematically testing and promoting changes through dev, staging, and production environments.
---

The [Pulumi Kubernetes Operator](https://www.pulumi.com/docs/iac/guides/continuous-delivery/pulumi-kubernetes-operator/) enables you to manage Pulumi stacks as Kubernetes resources, but it doesn't provide much guidance on change management. [Kargo](https://kargo.io/) fills this gap by providing controlled, staged promotions with verification steps. Together, they let you keep your infrastructure defined in Pulumi while managing multi-environment rollouts in a systematic way.

<!--more-->

## What you can do with Argo CD, PKO, and Kargo

When you combine these tools, you gain several change management capabilities:

- **Control release timing**: Determine when updates to your Pulumi program are released to different environments, rather than deploying everywhere at once.
- **Visualize deployments**: See which environments are running which versions of your infrastructure code at a glance.
- **Automatic verification**: Automatically verify deployment success before promoting changes to the next environment.
- **Approval gates**: Set up discrete approval requirements before promotion, ensuring human review when needed.
- **Change tracking**: Maintain a clear audit trail of what changed, when, and how it moved through your environments.

## What is Kargo

Kargo is a [continuous promotion platform](https://docs.kargo.io/user-guide/core-concepts/) that manages how changes move through application lifecycle stages. While it's commonly used for application deployments, it also works for infrastructure code managed by PKO.

The key concepts you'll work with:

**Freight**: A packaged set of artifacts that move together through your pipeline. For PKO, this typically includes a Git commit reference to your Pulumi infrastructure code and any associated configuration.

**Stages**: Promotion targets that represent different lifecycle phases (like dev, staging, production). Each stage corresponds to a different PKO Stack resource managing that environment's infrastructure.

**Promotions**: The process of moving freight from one stage to the next. Kargo updates the Stack resources to point to the promoted freight.

**Warehouses**: Monitors that watch your Git repository for infrastructure code changes and package new commits as freight.

**Projects**: Organizational units that group related stages and warehouses, mapping to Kubernetes namespaces for access control.

When Kargo promotes freight to a stage, it updates the corresponding PKO Stack resource with the new Git reference. PKO then reconciles the stack, and your infrastructure changes are applied.

## Example architecture

To demonstrate how these tools work together, let's look at an example setup that manages infrastructure code through a controlled promotion pipeline:

![PKO and Kargo Architecture](PKO_Kargo_Architecture.png)

This architecture includes six main components working together:

1. **[Security Scanner repository](https://github.com/lichtie/security-scanner)**: Contains your Pulumi infrastructure code. Kargo watches this repository for new commits or releases.
1. **Kargo**: Controls the release pipeline. When it detects new code in the security scanner repository, it triggers an update to promote that code to the next stage.
1. **[Kargo manifests repository](https://github.com/lichtie/kargo-manifests)**: Stores the Kubernetes manifests that define PKO Stack resources. Kargo updates this repository with the new Git references when promoting freight.
1. **ArgoCD**: Watches the Kargo manifests repository and creates or updates Stack objects in Kubernetes when it detects changes.
1. **Pulumi Kubernetes Operator**: Watches Stack objects and deploys them to Pulumi, triggering stack updates or previews.
1. **Pulumi**: Performs the actual infrastructure deployments and previews based on PKO's instructions.

The workflow follows this pattern: Kargo detects new infrastructure code, updates the manifests repository with the new Git reference, ArgoCD syncs the Stack objects to Kubernetes, PKO triggers Pulumi to deploy the changes, and Kargo verifies the successful deployment. This creates a closed loop where infrastructure changes are systematically promoted and verified at each stage.
