---
title: "IDP Pattern: Container-based apps, centrally managed container infra"
linktitle: "Container-based apps, centrally managed container infra"
menu:
  idp:
    parent: idp-patterns
    weight: 50
meta_desc: Separate application deployment from infrastructure management using components for centrally managed container infrastructure
allow_long_title: true
h1: "IDP Pattern: Container-based apps, centrally managed container infra"
description: <p>Separate application deployment from infrastructure management using components for centrally managed container infrastructure.</p>
---

## Description

This pattern involves creating Pulumi components that abstract container infrastructure (like EKS clusters, ECS clusters, or container registries) which are managed centrally by platform teams, while application teams focus on deploying their containerized applications using these shared infrastructure components.

## When to use this pattern

- **Container-first architecture**: When your applications are designed to run in containers
- **Platform team separation**: When you have dedicated platform teams managing infrastructure
- **Shared infrastructure**: When multiple applications can share the same container runtime
- **Standardized deployment**: When you want consistent deployment patterns across teams

## When NOT to use this pattern

- **Legacy applications**: When applications aren't containerized or container-ready
- **Special infrastructure needs**: When applications require unique infrastructure configurations
- **Small organizations**: When you don't have dedicated platform teams

## How to use this pattern

Platform teams create reusable components that encapsulate container deployment to centrally managed infrastructure, while application teams simply specify their application requirements.

### Example

Platform team creates a container application component:

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

- [IDP Pattern: Components using other Components](/docs/idp/well-architected/patterns/components-using-other-components) - For building infrastructure component hierarchies
- [IDP Pattern: One ESC environment per service](/docs/idp/well-architected/patterns/one-esc-environment-per-service) - For service-specific configuration
- [IDP Pattern: Security Updates using Components](/docs/idp/well-architected/patterns/security-updates-using-components) - For maintaining secure infrastructure
