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

Many platform teams start with [Crossplane](https://www.crossplane.io/) because they want to manage infrastructure using the Kubernetes API. It's a powerful idea: treat your cloud resources like your pods and services. However, as infrastructure grows, YAML-based compositions can lead teams to look for more flexible alternatives.

This guide provides a clear migration map from Crossplane concepts to Pulumi, including coexistence strategies and import paths for teams looking to modernize their Kubernetes-native infrastructure. In this post, you will build a migration strategy that maps Crossplane compositions to Pulumi component resources.

<!--more-->

This transition starts when teams want to keep Kubernetes-native workflows but need more flexibility for complex infrastructure logic. While the Kubernetes Resource Model (KRM) works well for container orchestration, it can make some multi-cloud resources, reusable abstractions, and policy-driven platform workflows harder to model. Pulumi keeps declarative desired-state infrastructure management while adding general-purpose programming languages.

## Why teams move to Pulumi

The move from Crossplane to Pulumi is often driven by a few key factors:

1. **Logic and abstraction**: Crossplane Compositions historically used patch-and-transform expressions in YAML, with Composition Functions now allowing custom logic in Go, Python, or KCL. Pulumi expresses infrastructure logic directly in TypeScript, Python, Go, and other languages, making loops, conditionals, and complex data transformations easier to model.
1. **Tooling and ecosystem**: Pulumi integrates with existing IDEs, testing frameworks, and CI/CD pipelines without requiring custom Kubernetes controllers for every piece of logic.
1. **Debugging**: Troubleshooting a failing Crossplane request involves digging through multiple layers of Kubernetes events and status fields. Pulumi provides clear, actionable error messages and a local execution model that simplifies debugging.

## Mapping Crossplane concepts to Pulumi

If you're familiar with Crossplane, you'll find that Pulumi has direct equivalents for most of its core concepts.

| Crossplane concept | Pulumi equivalent | Description |
| :--- | :--- | :--- |
| Composite Resource (XR) | `ComponentResource` | A logical grouping of resources that defines a higher-level abstraction. |
| Composition | Component class implementation | The actual logic that defines how the abstraction is built. |
| Claim (XRC) or namespaced XR | Stack or Component instance | The specific request for a set of resources with defined parameters. Crossplane v1 commonly used claims; Crossplane v2 emphasizes namespaced composite resources. |
| ProviderConfig | Explicit `Provider` resource (e.g. `new aws.Provider(...)`) | Configuration for how the provider authenticates and interacts with the cloud. |

## Side-by-side: provisioning a database

Let's look at how you would define a managed database in both tools.

### Crossplane YAML

In Crossplane, the `CompositeResourceDefinition` and `Composition` define the abstraction, while a composite resource instance requests it. The simplified example below shows the request shape platform users might apply.

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

In Pulumi, you use a `ComponentResource` to create the same abstraction. Pass the database password as a Pulumi secret, for example from stack configuration or Pulumi ESC.

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

export interface DatabaseArgs {
    storageGB: pulumi.Input<number>;
    username: pulumi.Input<string>;
    password: pulumi.Input<string>;
}

export class PostgreSQLInstance extends pulumi.ComponentResource {
    constructor(name: string, args: DatabaseArgs, opts?: pulumi.ComponentResourceOptions) {
        super("pkg:index:PostgreSQLInstance", name, {}, opts);

        new aws.rds.Instance(name, {
            allocatedStorage: args.storageGB,
            engine: "postgres",
            instanceClass: "db.t3.micro",
            username: args.username,
            password: args.password,
            skipFinalSnapshot: true,
        }, { parent: this });
    }
}
```

## Coexistence and migration strategy

You don't have to migrate everything at once. A "big bang" migration is rarely the right choice for production infrastructure. Instead, consider a coexistence strategy.

1. **Leave Crossplane running**: Keep your existing Crossplane resources under management while you build out your Pulumi components.
1. **Reference existing resources**: Use Pulumi's `get` functions to reference resources managed by Crossplane. This allows you to build new infrastructure that depends on the old.
1. **Import by boundary**: Migrate resources one namespace or one request boundary at a time. Before importing a cloud resource into Pulumi, stop Crossplane from writing to the same object. Use provider-specific management policies or deletion policies so disabling Crossplane reconciliation does not delete the external resource, or switch to an observe-only pattern if your provider supports that. Then use the [`pulumi import`](/docs/iac/guides/migration/import/) command so only one control plane owns writes at a time.

## Cutover checklist

When you're ready to move a resource from Crossplane to Pulumi, follow this checklist:

1. **Ownership**: Ensure the cloud resource's tags or ownership fields are updated to reflect that Pulumi is now the manager.
1. **State import**: Use `pulumi import` to generate the code and state for the existing resource after Crossplane is no longer reconciling changes to that object.
1. **Policy check**: Run your Pulumi stack through [Pulumi Policies](/docs/insights/policy/) to ensure it meets compliance standards.
1. **Secrets**: Migrate any secrets from Kubernetes Secrets (used by Crossplane) to a dedicated secret manager or Pulumi's built-in secrets provider.
1. **Rollback plan**: Always have a plan to revert to Crossplane management if the initial Pulumi deployment fails, including how you will remove Pulumi ownership before resuming Crossplane reconciliation.

Migrating from Crossplane to Pulumi lets your team keep the benefits of infrastructure as code while gaining the flexibility of modern programming languages. Next, pick one low-risk Crossplane composition, map its request inputs to a Pulumi component, and use [Pulumi import](/docs/iac/guides/migration/import/) to adopt existing resources without a rewrite.

{{< blog/cta-button "Plan your Pulumi migration" "/docs/iac/guides/migration/" >}}
