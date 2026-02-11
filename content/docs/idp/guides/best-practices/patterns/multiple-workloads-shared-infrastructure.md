---
title: "IDP Pattern: Multiple workloads on shared infrastructure"
linktitle: "Multiple workloads on shared infrastructure"
menu:
  idp:
    parent: idp-patterns
    weight: 50
meta_desc: Separate application deployment from infrastructure management using components for centrally managed shared infrastructure
allow_long_title: true
h1: "IDP Pattern: Multiple workloads on shared infrastructure"
description: <p>Separate application deployment from infrastructure management using components for centrally managed shared infrastructure.</p>
aliases:
  - /docs/idp/guides/best-practices/patterns/container-based-apps-centrally-managed-infra
---

## Description

This pattern involves creating Pulumi components that abstract shared infrastructure which is managed centrally by platform teams, while application teams focus on deploying their workloads using these shared infrastructure components. Container infrastructure (like EKS clusters, ECS clusters, or container registries) is a common example, but this pattern applies to any shared infrastructure like databases, message queues, or compute clusters.

## When to use this pattern

- **Shared infrastructure benefits**: When multiple workloads can benefit from shared infrastructure (containers, databases, message queues, etc.)
- **Platform team separation**: When you have dedicated platform teams managing infrastructure
- **Resource efficiency**: When multiple applications can share the same underlying infrastructure
- **Standardized deployment**: When you want consistent deployment patterns across teams

## When NOT to use this pattern

- **Legacy applications**: When applications aren't containerized or container-ready
- **Special infrastructure needs**: When applications require unique configurations like specific GPU types, specialized networking, or custom security requirements
- **Single workload scenarios**: When you only have one application or service, regardless of organization size

## How to use this pattern

Platform teams create reusable components that encapsulate workload deployment to centrally managed shared infrastructure, while application teams simply specify their application requirements.

The platform team first provisions shared infrastructure (often using their own templates or components for standardization), then creates application-facing components that deploy workloads to this shared infrastructure.

### Example: Container workloads

This example shows the common case of container workloads. The platform team creates a container application component that deploys to their shared ECS cluster:

```typescript
// Platform-managed container application component
export class ContainerApp extends ComponentResource {
  constructor(name: string, args: ContainerAppArgs, opts?: ComponentResourceOptions) {
    super("acme:platform:ContainerApp", name, {}, opts);

    // Platform references existing ECR and ECS infrastructure
    const ecrRepo = aws.ecr.Repository.get("platform-ecr", args.ecrRepoId);
    const ecsCluster = aws.ecs.Cluster.get("platform-cluster", args.ecsClusterId);

    // Build and push container image to platform ECR
    const image = new awsx.ecr.Image(name, {
      repositoryUrl: ecrRepo.repositoryUrl,
      context: args.dockerContext,
    });

    // Deploy to platform ECS cluster
    this.service = new awsx.ecs.FargateService(name, {
      cluster: ecsCluster.arn,
      taskDefinitionArgs: {
        container: {
          image: image.imageUri,
          memory: args.memory || 512,
          cpu: args.cpu || 256,
          environment: args.environment,
        },
      },
    });
  }
}
```

Application teams use the component:

```typescript
// Application team usage
import { ContainerApp } from "@acme/platform-components";

const app = new ContainerApp("my-web-app", {
  ecrRepoId: "platform-web-repo",
  ecsClusterId: "platform-web-cluster",
  dockerContext: "./src",
  memory: 1024,
  cpu: 512,
  environment: [
    { name: "NODE_ENV", value: "production" },
    { name: "PORT", value: "3000" },
  ],
});
```

This allows application teams to deploy containers without managing ECR repositories or ECS clusters directly.

## Related patterns

- [IDP Pattern: Components using other Components](/docs/idp/guides/best-practices/patterns/components-using-other-components) - For building infrastructure component hierarchies
- [IDP Pattern: One ESC environment per service](/docs/idp/guides/best-practices/patterns/one-esc-environment-per-service) - For service-specific configuration
- [IDP Pattern: Security Updates using Components](/docs/idp/guides/best-practices/patterns/security-updates-using-components) - For maintaining secure infrastructure
