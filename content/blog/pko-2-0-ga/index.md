---
title: "Pulumi Kubernetes Operator 2.0 is Now Generally Available!"
date: 2025-02-20
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
- A new Workspace custom resource manages the Workspace pod lifecycle
- Stack operations are coordinated through a new Update custom resource
- The Stack custom resource API remains the primary interface, maintaining backward compatibility

This architecture delivers improved resource isolation, better secrets management, and flexible Workspace customization options. The pod-per-stack model ensures reliable resource allocation and clear operational boundaries for each deployment.

## What's New in GA?

The GA release introduces three powerful capabilities that give you more control over your deployments:

### Enhanced Logging Control

You can now set the log verbosity level of the Pulumi CLI for any given stack or Workspace. This feature offers granular control over logging output, making debugging and fine-tuning your deployment process more efficient.

### New Controller Events for Better Instrumentation

Additional controller events have been introduced to provide richer instrumentation and observability. These events offer improved insights into the operator's behavior, enabling more effective monitoring of your infrastructure.

### Workspace Reclaim Policy

Managing Workspace lifecycles is now even more flexible with the new `workspaceReclaimPolicy` field in the Stack specification. This enhancement allows you to define how workspace resources should be handled after stack deployment. The supported policies are:

- `Retain`: Keeps the Workspace and its resources after deployment (default)
- `Delete`: Automatically removes the Workspace once the stack is fully deployed

This gives you fine-grained control over resource cleanup and helps prevent workspace sprawl in your cluster.

## See It in Action

Here's an example that demonstrates how to deploy a Pulumi stack using the operator. This configuration creates a service account with appropriate permissions and defines a Stack resource that deploys a sample project from the Pulumi examples repository:

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as k8s from "@pulumi/kubernetes";
import * as pulumiservice from "@pulumi/pulumiservice";

// Create a Kubernetes ServiceAccount for the Pulumi Workspace pod
const sa = new k8s.core.v1.ServiceAccount("random-yaml", {});

// Grant system:auth-delegator to the ServiceAccount
const crb = new k8s.rbac.v1.ClusterRoleBinding("random-yaml:system:auth-delegator", {
    roleRef: {
        apiGroup: "rbac.authorization.k8s.io",
        kind: "ClusterRole",
        name: "system:auth-delegator",
    },
    subjects: [{
        kind: "ServiceAccount",
        name: sa.metadata.name,
        namespace: sa.metadata.namespace,
    }],
});

// Provision a Pulumi Cloud access token and store it in a Kubernetes Secret
const accessToken = new pulumiservice.AccessToken("random-yaml", {
    description: `For stack "${pulumi.runtime.getOrganization()}/${pulumi.runtime.getProject()}/${pulumi.runtime.getStack()}"`,
});
const apiSecret = new k8s.core.v1.Secret("random-yaml", {
    stringData: {
        "accessToken": accessToken.value,
    }
});

// Deploy the "random-yaml" program from the github.com/pulumi/examples repository.
const stack = new k8s.apiextensions.CustomResource("random-yaml", {
    apiVersion: 'pulumi.com/v1',
    kind: 'Stack',
    spec: {
        serviceAccountName: sa.metadata.name,
        projectRepo: "https://github.com/pulumi/examples",
        repoDir: "random-yaml/",
        branch: "master",
        shallow: true,
        stack: "pulumi-ts",
        refresh: true,
        destroyOnFinalize: true,
        envRefs: {
            PULUMI_ACCESS_TOKEN: {
                type: "Secret",
                secret: {
                    name: apiSecret.metadata.name,
                    key: "accessToken",
                },
            },
        },
        workspaceTemplate: {
            spec: {
                image: "pulumi/pulumi:3.147.0-nonroot",
            },
        },
    },
}, {dependsOn: [sa, crb, apiSecret]});
```

Here's an example of the enhanced event stream that shows the lifecycle of a stack deployment, from workspace creation to successful completion:

```
88s         Normal    SuccessfulCreate      statefulset/random-yaml-09aa1aad-workspace   create Pod random-yaml-09aa1aad-workspace-0 in StatefulSet random-yaml-09aa1aad-workspace successful
88s         Normal    StackUpdateDetected   stack/random-yaml-09aa1aad                   Initial stack update
0s          Normal    Pulled                pod/random-yaml-09aa1aad-workspace-0         Container image "pulumi/pulumi:3.147.0-nonroot" already present on machine
0s          Normal    Created               pod/random-yaml-09aa1aad-workspace-0         Created container pulumi
0s          Normal    Started               pod/random-yaml-09aa1aad-workspace-0         Started container pulumi
0s          Normal    Initialized           workspace/random-yaml-09aa1aad               Initialized workspace pod "random-yaml-09aa1aad-workspace-0"
0s          Normal    StackUpdateDetected   stack/random-yaml-09aa1aad                   Initial stack update
0s          Normal    UpdateSucceeded       update/random-yaml-09aa1aad-195200641a9      Updated stack "pulumi-ts"
0s          Normal    StackCreated          stack/random-yaml-09aa1aad                   Successfully updated stack
```

## Additional Resources

To help you get the most out of Pulumi Kubernetes Operator 2.0, we've prepared comprehensive documentation:

- [Migration Guide](https://github.com/pulumi/pulumi-kubernetes-operator/blob/v2.0.0/docs/migration.md): Step-by-step instructions for upgrading from v1.x to v2.0
- [Troubleshooting Guide](https://github.com/pulumi/pulumi-kubernetes-operator/blob/v2.0.0/docs/troubleshooting.md): Common issues and their solutions
- [Release Notes](https://github.com/pulumi/pulumi-kubernetes-operator/releases/tag/v2.0.0): Full details of what's new in version 2.0

## Start Using It Today

We are excited to see how you will use these new features to transform your cloud operations. Share your experiences, questions, and insights with us through our community forums or Slack channel.

[Get started with the Pulumi Kubernetes Operator in our documentation](/docs/iac/using-pulumi/continuous-delivery/pulumi-kubernetes-operator)

Happy deploying!
