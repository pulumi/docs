---
title: "Build an EKS Environment Factory with Pulumi and vCluster"
date: 2026-06-04
meta_desc: "Build EKS-hosted vCluster test environments with Pulumi, EKS Auto Mode, Helm, RBAC, quotas, and safe cleanup workflows."
meta_image: meta.png
feature_image: feature.png
authors:
    - pablo-seibelt
tags:
    - aws
    - kubernetes
    - platform-engineering
social:
    twitter: |
        Build an EKS environment factory with Pulumi and vCluster.

        Use EKS Auto Mode, Helm, RBAC, quotas, and previews to manage isolated test environments.
    linkedin: |
        Shared EKS clusters and vCluster can help platform teams provision isolated test environments faster.

        This post shows how to model that pattern with Pulumi, from the host cluster to tenant guardrails and cleanup.
    bluesky: |
        Build isolated EKS test environments with Pulumi and vCluster.

        Model the host cluster, vCluster tenants, guardrails, and cleanup as code.
---

AWS reports in an [AWS Architecture Blog case study](https://aws.amazon.com/blogs/architecture/deloitte-optimizes-eks-environment-provisioning-and-achieves-89-faster-testing-environments-using-amazon-eks-and-vcluster/) that Deloitte's move to a virtual cluster model on Amazon EKS resulted in 89% faster testing environment provisioning. By consolidating dozens of disparate clusters into a single host cluster with over 50 [vCluster](https://www.vcluster.com/) instances, the case study says Deloitte saved about 500 QA hours per year. This "Environment Factory" pattern allows platform teams to provide isolated, ephemeral Kubernetes environments on demand without the cost or lag of full cluster provisioning.

This post adapts that general architecture with Pulumi to orchestrate Amazon [EKS Auto Mode](https://docs.aws.amazon.com/eks/latest/userguide/automode.html) and vCluster.

<!--more-->

## The problem: environment sprawl and provisioning lag

Traditional development workflows often rely on one full EKS cluster per developer or feature branch. While this provides strong isolation, it introduces major pain points. Provisioning a full cluster can take 15 minutes or more, which slows down CI/CD pipelines. Managing dozens of clusters also leads to high costs and significant operational overhead.

Platform teams need a "soft multi-tenancy" model. This model should feel like a dedicated cluster to the developer but run on shared infrastructure to keep costs low and startup times fast.

## Architecture overview: the host and the tenants

The environment factory architecture consists of two main layers.

1. **Host cluster**: A single, reliable EKS cluster managed with EKS Auto Mode. This cluster provides the underlying compute, networking, and storage.
1. **Tenant environments**: Virtual clusters (vCluster) running as pods within host namespaces.

According to the [vCluster architecture](https://www.vcluster.com/docs/vcluster/introduction/architecture), the virtual control plane handles API requests while a syncer maps virtual resources to the host cluster. This separation allows tenants to manage their own CRDs, namespaces, and RBAC while platform teams use quotas, NetworkPolicies, pod security, IAM boundaries, and node isolation controls to protect the host and other tenants.

## Implementation: the EKS Auto Mode host

EKS Auto Mode simplifies the host cluster by automating infrastructure management. It handles node provisioning, scaling, and updates based on pod requirements.

The following snippet shows how to define an EKS cluster with Auto Mode enabled using Pulumi.

```typescript
import * as awsx from "@pulumi/awsx";
import * as eks from "@pulumi/eks";
import * as k8s from "@pulumi/kubernetes";
import { SubnetType } from "@pulumi/awsx/ec2";

const clusterName = "environment-factory";

const vpc = new awsx.ec2.Vpc("environment-factory", {
    enableDnsHostnames: true,
    cidrBlock: "10.0.0.0/16",
    subnetSpecs: [
        {
            type: SubnetType.Public,
            tags: {
                [`kubernetes.io/cluster/${clusterName}`]: "shared",
                "kubernetes.io/role/elb": "1",
            },
        },
        {
            type: SubnetType.Private,
            tags: {
                [`kubernetes.io/cluster/${clusterName}`]: "shared",
                "kubernetes.io/role/internal-elb": "1",
            },
        },
    ],
    subnetStrategy: "Auto",
});

// Create an EKS cluster with Auto Mode enabled.
const hostCluster = new eks.Cluster("host-cluster", {
    name: clusterName,
    authenticationMode: eks.AuthenticationMode.Api, // Use API authentication mode for EKS access entries.
    vpcId: vpc.vpcId,
    publicSubnetIds: vpc.publicSubnetIds,
    privateSubnetIds: vpc.privateSubnetIds,
    autoMode: {
        enabled: true,
    },
});

const hostProvider = new k8s.Provider("host-provider", {
    kubeconfig: hostCluster.kubeconfig,
});
```

## Implementation: the environment factory

Once the host cluster is ready, we can build the factory that stamps out tenant environments. Each tenant needs a dedicated namespace, resource quotas, and the vCluster itself.

### Tenant guardrails

Before installing vCluster, we set up a namespace and resource quotas to ensure one tenant cannot consume all host resources.

```typescript
import * as k8s from "@pulumi/kubernetes";

// Define a tenant namespace on the host cluster.
const tenantNamespace = new k8s.core.v1.Namespace("tenant-alpha", {
    metadata: { name: "tenant-alpha" },
}, { provider: hostProvider });

// Apply resource quotas to the tenant namespace.
const quota = new k8s.core.v1.ResourceQuota("tenant-quota", {
    metadata: { namespace: tenantNamespace.metadata.name },
    spec: {
        hard: {
            pods: "20",
            "requests.cpu": "4",
            "requests.memory": "8Gi",
            "limits.cpu": "8",
            "limits.memory": "16Gi",
        },
    },
}, { provider: hostProvider });

// Define a Role for the tenant within their namespace.
const tenantRole = new k8s.rbac.v1.Role("tenant-role", {
    metadata: { namespace: tenantNamespace.metadata.name },
    rules: [{
        apiGroups: [""],
        resources: ["pods", "services", "configmaps", "secrets"],
        verbs: ["get", "list", "watch", "create", "update", "patch", "delete"],
    }],
}, { provider: hostProvider });

// Bind the Role to a tenant user or group.
const tenantRoleBinding = new k8s.rbac.v1.RoleBinding("tenant-role-binding", {
    metadata: { namespace: tenantNamespace.metadata.name },
    subjects: [{
        kind: "User",
        // Replace "tenant-user" with the IAM-mapped user or group for this tenant.
        name: "tenant-user",
        apiGroup: "rbac.authorization.k8s.io",
    }],
    roleRef: {
        kind: "Role",
        name: tenantRole.metadata.name,
        apiGroup: "rbac.authorization.k8s.io",
    },
}, { provider: hostProvider });
```

For production use, map these Kubernetes identities to IAM principals using EKS Access Entries, with the legacy `aws-auth` ConfigMap still appearing in older clusters.

### Deploying vCluster with Helm

We use the [`kubernetes.helm.v3.Release`](/registry/packages/kubernetes/api-docs/helm/v3/release/) resource to install vCluster. This resource provides controlled [Helm](https://helm.sh/) lifecycle management for the vCluster release. The `values` block should be adjusted for each tenant profile to control resource synchronization and control plane behavior. Review the [vCluster release notes](https://github.com/loft-sh/vcluster/releases) when changing chart versions because values schema and generated secret names can change across releases.

```typescript
import * as k8s from "@pulumi/kubernetes";

// Install vCluster using the Helm Release resource.
const vcluster = new k8s.helm.v3.Release("vcluster-alpha", {
    name: "vcluster-alpha",
    chart: "vcluster",
    version: "0.20.0", // Tested with vCluster 0.20.x; review release notes before changing versions.
    repositoryOpts: {
        repo: "https://charts.loft.sh",
    },
    namespace: tenantNamespace.metadata.name,
    values: {
        // Explicit sync configuration; adjust per tenant profile.
        sync: {
            toHost: {
                pods: { enabled: true },
            },
        },
    },
}, { provider: hostProvider });
```

### Accessing the virtual cluster

The vCluster generates a kubeconfig that allows developers to interact with the virtual API server. We must treat this kubeconfig as a secret, and the endpoint in that kubeconfig must be reachable from the Pulumi runner before using it to create resources inside the virtual cluster.

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as k8s from "@pulumi/kubernetes";

// Retrieve the vCluster kubeconfig from the generated secret.
// The vCluster-generated secret can lag behind Helm release readiness on first creation,
// so teams may choose an explicit readiness check or rerun after the virtual control plane initializes.
const vclusterKubeconfig = k8s.core.v1.Secret.get("vcluster-secret",
    pulumi.interpolate`${tenantNamespace.metadata.name}/vc-vcluster-alpha`,
    {
        provider: hostProvider,
        dependsOn: [vcluster],
    }
).data.apply(data => Buffer.from(data["config"], "base64").toString());

// Export the kubeconfig as a secret.
export const tenantKubeconfig = pulumi.secret(vclusterKubeconfig);

// Create a provider for the virtual cluster using the secret kubeconfig.
const vclusterProvider = new k8s.Provider("vcluster-provider", {
    kubeconfig: tenantKubeconfig,
});
```

## Operational caveats

* **RBAC and permissions**: vCluster generates default RBAC rules that work for most scenarios. However, if your host cluster is heavily locked down, you may need to provide additional permissions to the vCluster service account.
* **Helm release previews**: When using [`kubernetes.helm.v3.Release`](/registry/packages/kubernetes/api-docs/helm/v3/release/), Pulumi previews may not show every detail of the rendered Kubernetes resources. It primarily tracks the state of the Helm release itself.
* **EKS Auto Mode node lifetime**: EKS Auto Mode uses immutable AMIs and has a 21-day node lifetime. Kubernetes reschedules vCluster pods and tenant workloads when nodes are replaced, so configure replicas, PodDisruptionBudgets, requests, and persistent storage for disruption tolerance.

## Conclusion: ephemeral environments at scale

By combining Pulumi with EKS Auto Mode and vCluster, you can build a scalable environment factory. This approach provides the isolation developers need while maintaining the speed and cost-efficiency required by platform teams.

The snippets provided here are adapted for illustration. In a production environment, you would likely wrap these resources into a Pulumi [ComponentResource](/docs/iac/concepts/resources/components/) to provide a clean, reusable API for your internal developers. When a feature branch is merged, deleting the Pulumi stack removes the resources managed by that stack, but validate namespace finalizers, persistent volume reclaim policies, and external cloud artifacts as part of cleanup.

For more on managing EKS with Pulumi, see the [EKS guide](/docs/clouds/aws/guides/eks/).
