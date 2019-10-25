---
title: Deploy App Services
menu:
  userguides:
    parent: crosswalk-kubernetes
    identifier: crosswalk-kubernetes-app-svcs
    weight: 8
---

{{< cloudchoose >}}

App services are general services scoped at the Kubernetes application level.
These services tend to include datastores, and managers for ingress, DNS, and TLS.
They can be shared amongst several apps or be specific to workloads, and are
usually a mix of cloud provider and custom services.

## Overview

We'll explore how to setup:

  * [Datstores](#datastores)
  * [General App Services](#general-app-services)

<div class="cloud-prologue-aws"></div>
<div class="mt">
{{% md %}}

The full code for the AWS app services stack is on [GitHub][gh-repo-stack].
[gh-repo-stack]: https://github.com/pulumi/kubernetes-the-prod-way/tree/crosswalk/aws/05-app-services

{{% /md %}}
</div>

<div class="cloud-prologue-azure"></div>
<div class="mt">
{{% md %}}

The full code for the Azure app services stack is on [GitHub][gh-repo-stack].
[gh-repo-stack]: https://github.com/pulumi/kubernetes-the-prod-way/tree/crosswalk/azure/05-app-services

{{% /md %}}
</div>

<div class="cloud-prologue-gcp"></div>
<div class="mt">
{{% md %}}

The full code for the GCP app services stack is on [GitHub][gh-repo-stack].
[gh-repo-stack]: https://github.com/pulumi/kubernetes-the-prod-way/tree/crosswalk/gcp/05-app-services

{{% /md %}}
</div>

The full code for the general app services is on [GitHub][gh-repo-stack].
[gh-repo-stack]: https://github.com/pulumi/kubernetes-the-prod-way/tree/crosswalk/general-app-services

## Datastores

Apps may want to persist data to databases or in-memory datastores. Often
times these services are provisioned directly with the cloud provider to simplify
running and managing their lifecycles.

<div class="cloud-prologue-aws"></div>
<div class="mt">
{{% md %}}

### Postgres Database

Create a Postgres database instance in [AWS RDS][aws-rds], and store its
connection information in a Kubernetes [Secret][k8s-secret] for apps to refer
to and consume.

```typescript
import * as aws from "@pulumi/aws";
import * as random from "@pulumi/random";
import * as k8s from "@pulumi/kubernetes";

// Generate a strong password for the Postgres DB.
const postgresDbPassword = new random.RandomString(`${projectName}-db-password`, {
	length: 20,
	special: true
}, {additionalSecretOutputs: ["result"]}).result;

// Create a Postgres DB instance of RDS.
const dbSubnets = new aws.rds.SubnetGroup(`${projectName}-subnets`, {
    subnetIds: privateSubnetIds
});
const db = new aws.rds.Instance("postgresdb", {
    engine: "postgres",
    instanceClass: "db.t2.micro",
    allocatedStorage: 20,
    dbSubnetGroupName: dbSubnets.id,
    vpcSecurityGroupIds: securityGroupIds,
    name: "testdb",
    username: "alice",
    password: postgresDbPassword,
    skipFinalSnapshot: true,
});

// Create a Secret from the DB connection information.
const eksProvider = new k8s.Provider("eks-provider", {kubeconfig: config.kubeconfig.apply(JSON.stringify)});
const dbConn = new k8s.core.v1.Secret("postgres-db-conn",
    {
        data: {
            host: db.address.apply(addr => Buffer.from(addr).toString("base64")),
            port: db.port.apply(port => Buffer.of(port).toString("base64")),
            username: db.username.apply(user => Buffer.from(user).toString("base64")),
            password: postgresDbPassword.apply(pass => Buffer.from(pass).toString("base64")),
        },
    },
    { provider: eksProvider },
);
```

### Redis Datastore

Create a Redis datastore instance in [AWS ElastiCache][aws-ec], and store its
connection information in a Kubernetes [ConfigMap][k8s-cm] for apps to refer
to and consume.

```typescript
import * as aws from "@pulumi/aws";
import * as k8s from "@pulumi/kubernetes";

// Create a Redis instance.
const cacheSubnets = new aws.elasticache.SubnetGroup(`${projectName}-cache-subnets`, {
    subnetIds: privateSubnetIds,
});
const cacheCluster = new aws.elasticache.Cluster("cachecluster", {
    engine: "redis",
    nodeType: "cache.t2.micro",
    numCacheNodes: 1,
    subnetGroupName: cacheSubnets.id,
    securityGroupIds: securityGroupIds,
});

// Create a ConfigMap from the cache connection information.
const cacheConn = new k8s.core.v1.ConfigMap("postgres-db-conn",
    {
        data: {
            host: cacheCluster.cacheNodes[0].address.apply(addr => Buffer.from(addr).toString("base64")),
        },
    },
    { provider: eksProvider },
);
```

[k8s-secret]: https://kubernetes.io/docs/concepts/configuration/secret/
[k8s-cm]: https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/
[aws-ec]: https://aws.amazon.com/elasticache/
[aws-rds]: https://aws.amazon.com/rds/
{{% /md %}}
</div>

<div class="cloud-prologue-azure"></div>
<div class="mt">
{{% md %}}

{{< k8s-language nokx >}}

<div class="k8s-language-prologue-yaml"></div>
<div class="mt">
{{% md %}}
AZURE YAML TODO
{{% /md %}}
</div>

<div class="k8s-language-prologue-typescript"></div>
<div class="mt">
{{% md %}}
AZURE pulumi-k8s TODO
{{% /md %}}
</div>

{{% /md %}}
</div>

<div class="cloud-prologue-gcp"></div>
<div class="mt">
{{% md %}}

{{< k8s-language nokx >}}

<div class="k8s-language-prologue-yaml"></div>
<div class="mt">
{{% md %}}
GCP YAML TODO
{{% /md %}}
</div>

<div class="k8s-language-prologue-typescript"></div>
<div class="mt">
{{% md %}}
GCP pulumi-k8s TODO
{{% /md %}}
</div>

{{% /md %}}
</div>

## General App Services

### Ingress Management

TODO

{{< k8s-language nokx >}}

<div class="k8s-language-prologue-yaml"></div>
<div class="mt">
{{% md %}}
YAML TODO
{{% /md %}}
</div>

<div class="k8s-language-prologue-typescript"></div>
<div class="mt">
{{% md %}}
pulumi-k8s TODO
{{% /md %}}
</div>

### Other Example

TODO

{{< k8s-language nokx >}}

<div class="k8s-language-prologue-yaml"></div>
<div class="mt">
{{% md %}}
YAML TODO
{{% /md %}}
</div>

<div class="k8s-language-prologue-typescript"></div>
<div class="mt">
{{% md %}}
pulumi-k8s TODO
{{% /md %}}
</div>
