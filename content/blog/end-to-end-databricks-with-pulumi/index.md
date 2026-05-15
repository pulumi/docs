---
title: "Build a Governed Databricks Workspace with Pulumi"
date: 2026-06-04
draft: false
meta_desc: "Provision a governed Databricks workspace baseline with Pulumi, including cluster policies, notebooks, jobs, and promotion workflows."
feature_image: feature.png
meta_image: meta.png
authors:
    - pablo-seibelt
tags:
    - databricks
    - data-engineering
    - infrastructure-as-code
social:
    twitter: |
        Databricks workspaces drift fast when clusters, jobs, and permissions are configured by hand.

        Put the governed baseline in Pulumi instead.
    linkedin: |
        Databricks governance depends on repeatable workspace defaults: cluster policies, notebooks, and jobs.

        This guide shows how to manage that baseline with Pulumi and promote it across environments.
    bluesky: |
        Databricks clusters, notebooks, and jobs drift fast.

        Put workspace governance in Pulumi.
---

Platform teams responsible for [Databricks](https://www.databricks.com/) often find themselves manually configuring clusters and notebooks for every new data science team. This manual overhead leads to inconsistent cluster policies, runaway costs from oversized instances, and security gaps in workspace operations. Without a standardized way to provision workspace-local resources, data platforms become a fragmented collection of bespoke environments that are impossible to govern at scale.

As Databricks usage grows across the enterprise, the lack of a governed workspace baseline becomes a major operational risk. Inconsistent policies lead to unpredictable billing and audit failures. Standardizing your Databricks environment with Pulumi ensures that every workspace starts with the correct cost controls, cluster policies, notebooks, and automated jobs, allowing your data teams to move faster without compromising governance.

<!--more-->

## What you'll build

In this post, you will learn how to provision a governed Databricks workspace baseline using Pulumi. You will build:

1. **Cluster policies** to enforce instance types and cost controls.
1. **Workspace notebooks** to standardize workload locations.
1. **Secret scopes and permissions** to make access reviewable.
1. **Automated jobs** that run on policy-constrained compute.

By the end, you will have a reproducible workspace configuration that you can deploy to any new Databricks environment.

## The Databricks management boundary

When managing Databricks with Pulumi, understand the boundary between account-level and workspace-level resources.

1. **Account-level**: Creating cloud prerequisites such as VPCs, subnets, IAM roles, and Azure resource groups uses the cloud provider for your target platform. On AWS and GCP, Databricks workspace creation and account-level identity use the Databricks provider's account APIs; on Azure, the workspace itself is commonly managed with `azure-native`.
1. **Workspace-level**: Managing clusters, jobs, notebooks, permissions, and secret scopes within a specific workspace. This example uses the `@pulumi/databricks` provider against an Azure Databricks workspace URL, and the same workspace-resource pattern applies once your provider is configured for the target workspace.

For this tutorial, we'll assume you have an existing Databricks workspace and want to manage the resources within it.

## Configuring credentials with Pulumi ESC

Before writing code, we need to configure our credentials. [Pulumi ESC](/docs/esc/) (Environments, Secrets, and Configuration) manages these securely.

You can create an environment that maps Databricks credentials into Pulumi configuration for the Databricks provider:

```yaml
values:
  databricks:
    host: "https://adb-123456789.0.azuredatabricks.net"
    token:
      fn::secret: databricks-token
  pulumiConfig:
    databricks:host: ${databricks.host}
    databricks:token: ${databricks.token}
```

Once configured, import this environment into your Pulumi stack. The Databricks provider reads the `databricks:host` and `databricks:token` configuration values without requiring static secrets in stack config.

## Defining your data infrastructure

The following Pulumi program in TypeScript sets up separate cluster policies for interactive and job compute, a governed shared cluster, a secret scope, explicit permissions, a notebook, and a scheduled job that runs on policy-constrained compute.

```typescript
import * as databricks from "@pulumi/databricks";

const interactivePolicy = new databricks.ClusterPolicy("interactive-fair-use", {
    name: "Interactive Fair Use Policy",
    definition: JSON.stringify({
        "dbus_per_hour": {
            "type": "range",
            "maxValue": 10,
        },
        "autotermination_minutes": {
            "type": "fixed",
            "value": 20,
            "hidden": true,
        },
    }),
});

const jobPolicy = new databricks.ClusterPolicy("job-fair-use", {
    name: "Job Fair Use Policy",
    definition: JSON.stringify({
        "dbus_per_hour": {
            "type": "range",
            "maxValue": 10,
        },
    }),
});

const sharedCluster = new databricks.Cluster("shared-cluster", {
    clusterName: "Shared Engineering Cluster",
    sparkVersion: "17.3.x-scala2.13",
    nodeTypeId: "Standard_DS3_v2",
    autoterminationMinutes: 20,
    numWorkers: 2,
    policyId: interactivePolicy.id,
});

const clusterPermissions = new databricks.Permissions("shared-cluster-permissions", {
    clusterId: sharedCluster.id,
    accessControls: [{
        groupName: "data-engineers",
        permissionLevel: "CAN_RESTART",
    }, {
        groupName: "analysts",
        permissionLevel: "CAN_ATTACH_TO",
    }],
});

const secretScope = new databricks.SecretScope("etl-secrets", {
    name: "etl-secrets",
});

const secretScopeAcl = new databricks.SecretAcl("etl-secrets-readers", {
    scope: secretScope.name,
    principal: "data-engineers",
    permission: "READ",
});

const etlNotebook = new databricks.Notebook("etl-notebook", {
    path: "/Shared/ETL/NightlyProcess",
    language: "PYTHON",
    contentBase64: Buffer.from("print('Running ETL process...')").toString("base64"),
});

const job = new databricks.Job("nightly-etl", {
    name: "Nightly ETL Job",
    tasks: [{
        taskKey: "etl-task",
        newCluster: {
            numWorkers: 2,
            sparkVersion: "17.3.x-scala2.13",
            nodeTypeId: "Standard_DS3_v2",
            policyId: jobPolicy.id,
        },
        notebookTask: {
            notebookPath: etlNotebook.path,
        },
    }],
    schedule: {
        quartzCronExpression: "0 0 2 * * ?",
        timezoneId: "UTC",
    },
});
```

This baseline covers the resources a platform team needs to standardize first:

1. **Interactive cluster policy**: caps DBU consumption and enforces auto-termination for shared interactive compute.
1. **Job cluster policy**: caps DBU consumption for ephemeral job compute without applying interactive auto-termination settings.
1. **Shared cluster**: gives teams a governed interactive compute target.
1. **Secret scope and ACL**: makes ETL secret access reviewable.
1. **Cluster permissions**: assigns group-level access to the shared cluster.
1. **Notebook**: stores the workload artifact in the workspace.
1. **Job**: schedules the notebook on policy-constrained compute.

## Validation

After running `pulumi up`, you can validate your Databricks baseline:

1. **Databricks UI**: Navigate to the "Compute" section and verify that the interactive and job fair-use policies exist, with auto-termination fixed only on the interactive policy.
1. **Cluster check**: Confirm that the shared cluster references the interactive policy and uses the expected node type.
1. **Permission check**: Confirm that cluster and secret-scope permissions match the intended Databricks groups.
1. **Notebook check**: Confirm that `/Shared/ETL/NightlyProcess` exists in the workspace.
1. **Job check**: Go to the "Workflows" section and confirm that the "Nightly ETL Job" is scheduled and references the notebook.

Managing your Databricks workspace as code gives every team a governed, cost-aware baseline. Use Pulumi stacks to deploy the same cluster policies, permissions, secret scope, notebook, and job pattern to multiple workspaces with environment-specific configuration.

```bash
# Deploy to development
pulumi stack select dev
pulumi up

# Promote to production
pulumi stack select prod
pulumi up
```

This keeps production ETL jobs, cluster policies, secret scopes, and permission assignments aligned with development while still letting each stack bind to its own Databricks workspace and ESC environment.

## Conclusion

Next, connect this workspace baseline to your CI/CD pipeline and promote it through Pulumi stacks so Databricks jobs, cluster policies, and permissions move through the same review path as application code. Start with the [Databricks provider docs](/registry/packages/databricks/) and [Pulumi ESC](/docs/esc/) for credential handling.
