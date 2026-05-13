---
title: "Crossplane to Pulumi: A Migration Map for Platform Teams"
date: 2026-05-19
draft: false
schema_type: auto
meta_desc: "Plan a Crossplane-to-Pulumi migration by mapping compositions, claims, providers, coexistence strategies, imports, and Kubernetes-native workflows."
meta_image: meta.png
feature_image: feature.png
authors:
    - pablo-seibelt
tags:
    - kubernetes
    - crossplane
    - migration
social:
    twitter: |
        Moving from Crossplane to Pulumi? Start with a map: compositions to components, claims to stack outputs, providers to packages, coexistence to import.

        Learn more in the post.
    linkedin: |
        Crossplane-to-Pulumi migrations go smoother when teams map concepts before moving code.

        This guide covers compositions, claims, providers, coexistence strategies, imports, and how to preserve Kubernetes-native workflows where they still fit.
    bluesky: |
        Crossplane to Pulumi starts with a concept map: compositions, claims, providers, coexistence, imports, and Kubernetes-native workflows.

        Learn more in the post.
---

Many platform teams start with [Crossplane](https://www.crossplane.io/) because they want to manage infrastructure using the Kubernetes API. It's a powerful idea: treat your cloud resources just like your pods and services. However, as infrastructure grows, the limitations of YAML-based compositions often lead teams to look for more flexible alternatives.

This guide provides a clear migration map from Crossplane concepts to Pulumi, including coexistence strategies and import paths for teams looking to modernize their Kubernetes-native infrastructure. In this post, you will build a migration strategy that maps Crossplane compositions to Pulumi component resources.

<!--more-->

This transition often starts when teams want to keep Kubernetes-native workflows but need more flexibility for complex infrastructure logic. While the Kubernetes Resource Model (KRM) is excellent for container orchestration, it can become a bottleneck for multi-cloud resources, reusable abstractions, and policy-driven platform workflows. Pulumi offers the same "infrastructure as data" benefits while providing the full power of general-purpose programming languages.

## Why teams move to Pulumi

The move from Crossplane to Pulumi is usually driven by a few key factors:

1. **Logic and abstraction**: Crossplane Compositions use Patch and Transform functions and composition functions to model reusable infrastructure APIs. Pulumi uses TypeScript, Python, Go, and other languages, making it easier to handle loops, conditionals, and complex data transformations.
2. **Tooling and ecosystem**: Pulumi integrates with existing IDEs, testing frameworks, and CI/CD pipelines without requiring custom Kubernetes controllers for every piece of logic.
3. **Debugging**: Troubleshooting a failing Crossplane claim often involves digging through multiple layers of Kubernetes events and status fields. Pulumi provides clear, actionable error messages and a local execution model that simplifies debugging.

## Mapping Crossplane concepts to Pulumi

If you're familiar with Crossplane, you'll find that Pulumi has direct equivalents for most of its core concepts.

| Crossplane concept | Pulumi equivalent | Description |
| :--- | :--- | :--- |
| Composite Resource (XR) | `ComponentResource` | A logical grouping of resources that defines a higher-level abstraction. |
| Composition | Component class implementation | The actual logic that defines how the abstraction is built. |
| Claim (XRC) | Stack or Component instance | The specific request for a set of resources with defined parameters. |
| ProviderConfig | Provider resource options | Configuration for how the provider authenticates and interacts with the cloud. |

## Side-by-side: Provisioning a database

Let's look at how you would define a managed database in both tools.

### Crossplane YAML

In Crossplane, you might define a `CompositeResourceDefinition` and a `Composition` to wrap an RDS instance.

```yaml
apiVersion: database.example.org/v1alpha1
kind: XPostgreSQLInstance
metadata:
  name: my-db
spec:
  parameters:
    storageGB: 20
```

### Pulumi TypeScript

In Pulumi, you use a `ComponentResource` to create the same abstraction.

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

export interface DatabaseArgs {
    storageGB: pulumi.Input<number>;
}

export class PostgreSQLInstance extends pulumi.ComponentResource {
    constructor(name: string, args: DatabaseArgs, opts?: pulumi.ComponentResourceOptions) {
        super("pkg:index:PostgreSQLInstance", name, args, opts);

        new aws.rds.Instance(name, {
            allocatedStorage: args.storageGB,
            engine: "postgres",
            instanceClass: "db.t3.micro",
                            }, { parent: this });
    }
}
```

## Coexistence and migration strategy

You don't have to migrate everything at once. A "big bang" migration is rarely the right choice for production infrastructure. Instead, consider a coexistence strategy.

1. **Leave Crossplane running**: Keep your existing Crossplane resources under management while you build out your Pulumi components.
2. **Reference existing resources**: Use Pulumi's `get` functions to reference resources managed by Crossplane. This allows you to build new infrastructure that depends on the old.
3. **Import by boundary**: Migrate resources one namespace or one claim boundary at a time. Use the [`pulumi import`](/docs/iac/guides/migration/import/) command to bring existing cloud resources under Pulumi management without downtime.

## Cutover checklist

When you're ready to move a resource from Crossplane to Pulumi, follow this checklist:

1. **Ownership**: Ensure the cloud resource's tags or ownership fields are updated to reflect that Pulumi is now the manager.
2. **State import**: Use `pulumi import` to generate the code and state for the existing resource.
3. **Policy check**: Run your Pulumi stack through [Pulumi Policies](/docs/insights/policy/) to ensure it meets compliance standards.
4. **Secrets**: Migrate any secrets from Kubernetes Secrets (used by Crossplane) to a dedicated secret manager or Pulumi's built-in secrets provider.
5. **Rollback plan**: Always have a plan to revert to Crossplane management if the initial Pulumi deployment fails.

Migrating from Crossplane to Pulumi allows your team to keep the benefits of infrastructure as code while gaining the flexibility and power of modern programming languages. Whether you're managing a few databases or a global multi-cloud estate, Next, pick one low-risk Crossplane composition, map its claim inputs to a Pulumi component, and use [Pulumi import](/docs/iac/adopting-pulumi/import/) to adopt existing resources without a rewrite.
