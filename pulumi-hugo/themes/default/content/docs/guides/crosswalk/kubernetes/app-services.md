---
title_tag: Deploying Kubernetes App Services | Crosswalk
title: Deploying Kubernetes App Services
meta_desc: This page provides an overview of how to deploy Kubernetes App services to different
           cloud providers.
menu:
  userguides:
    parent: crosswalk-kubernetes
    identifier: crosswalk-kubernetes-app-svcs
    weight: 8
---

{{< chooser cloud "aws,azure,gcp" / >}}

App services are general services scoped at the Kubernetes application level.
These services tend to include datastores, and managers for ingress, DNS, and TLS.
They can be shared amongst several apps or be specific to workloads, and are
usually a mix of cloud provider and custom services.

{{% choosable cloud aws %}}

* [AWS app services stack on GitHub](https://github.com/pulumi/kubernetes-guides/tree/master/aws/05-app-services)

{{% /choosable %}}

{{% choosable cloud azure %}}

* [Azure app services stack on GitHub](https://github.com/pulumi/kubernetes-guides/tree/master/azure/05-app-services)

{{% /choosable %}}

{{% choosable cloud gcp %}}

* [GCP app services stack on GitHub](https://github.com/pulumi/kubernetes-guides/tree/master/gcp/05-app-services)

{{% /choosable %}}

* [General app services stack on GitHub](https://github.com/pulumi/kubernetes-guides/tree/master/general-app-services)

## Overview

We'll explore how to setup:

* [Datastores](#datastores)
* [General App Services](#general-app-services)

## Prerequisites

{{< chooser cloud "aws,azure,gcp" / >}}

{{% choosable cloud aws %}}

Authenticate as the `admins` role from the [Identity][aws-admin-identity-stack] stack.

```bash
$ aws sts assume-role --role-arn `pulumi stack output adminsIamRoleArn` --role-session-name k8s-admin
$ export KUBECONFIG=`pwd`/kubeconfig-admin.json
```

[aws-admin-identity-stack]: /docs/guides/crosswalk/kubernetes/identity#create-an-iam-role-for-admins/

{{% /choosable %}}

{{% choosable cloud azure %}}

Authenticate as the ServicePrincipal from the [Identity][azure-identity-stack] stack.

```bash
$ az login --service-principal --username $ARM_CLIENT_ID --password $ARM_CLIENT_SECRET --tenant $ARM_TENANT_ID
$ export KUBECONFIG=`pwd`/kubeconfig-admin.json
```

[azure-identity-stack]: /docs/guides/crosswalk/kubernetes/identity/
{{% /choosable %}}

{{% choosable cloud gcp %}}

Authenticate as the `admins` ServiceAccount from the [Identity][gcp-admin-identity-stack] stack.

```bash
$ gcloud auth activate-service-account --key-file k8s-admin-sa-key.json
$ export KUBECONFIG=`pwd`/kubeconfig.json
```

[gcp-admin-identity-stack]: /docs/guides/crosswalk/kubernetes/identity/#create-an-iam-role-for-admins

{{% /choosable %}}

## Datastores

Apps may want to persist data to databases or in-memory datastores. Often
times these services are provisioned directly with the cloud provider to simplify
running and managing their lifecycles.

{{% choosable cloud aws %}}

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
const provider = new k8s.Provider("eks-provider", {kubeconfig: config.kubeconfig.apply(JSON.stringify)});
const dbConn = new k8s.core.v1.Secret("postgres-db-conn",
    {
        data: {
            host: db.address.apply(addr => Buffer.from(addr).toString("base64")),
            port: db.port.apply(port => Buffer.of(port).toString("base64")),
            username: db.username.apply(user => Buffer.from(user).toString("base64")),
            password: postgresDbPassword.apply(pass => Buffer.from(pass).toString("base64")),
        },
    },
    {provider: provider},
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
const cacheConn = new k8s.core.v1.ConfigMap("redis-db-conn",
    {
        data: {
            host: cacheCluster.cacheNodes[0].address.apply(addr => Buffer.from(addr).toString("base64")),
        },
    },
    {provider: provider},
);
```

<!-- markdownlint-disable url -->
[k8s-secret]: https://kubernetes.io/docs/concepts/configuration/secret/
[k8s-cm]: https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/
[aws-ec]: https://aws.amazon.com/elasticache/
[aws-rds]: https://aws.amazon.com/rds/
<!-- markdownlint-enable url -->

{{% /choosable %}}

{{% choosable cloud azure %}}

### MongoDB

Create a MongoDB database instance in [Azure CosmosDB][azure-cosmosdb], and store its
connection information in a Kubernetes [Secret][k8s-secret] for apps to refer
to and consume.

```ts
import * as azure from "@pulumi/azure";
import * as k8s from "@pulumi/kubernetes";
import * as pulumi from "@pulumi/pulumi";

const name = pulumi.getProject();

// Define a separate resource group for app services.
const resourceGroup = new azure.core.ResourceGroup(name);

// Create a MongoDB-flavored instance of CosmosDB.
const cosmosdb = new azure.cosmosdb.Account("k8s-az-mongodb", {
    resourceGroupName: resourceGroup.name,
    kind: "MongoDB",
    consistencyPolicy: {
        consistencyLevel: "Session",
    },
    offerType: "Standard",
    geoLocations: [
        { location: resourceGroup.location, failoverPriority: 0 },
    ],
});

// A k8s provider instance of the cluster.
const provider = new k8s.Provider(`${name}-aks`, {
    kubeconfig: config.kubeconfig,
});

// Create secret from MongoDB connection string.
const mongoConnStrings = new k8s.core.v1.Secret(
    "mongo-secrets",
    {
        metadata: { name: "mongo-secrets", namespace: config.appsNamespaceName},
        data: mongoHelpers.parseConnString(cosmosdb.connectionStrings),
    },
    { provider },
);

```

<!-- markdownlint-disable url -->
[azure-cosmosdb]: https://azure.microsoft.com/en-us/services/cosmos-db/
[k8s-secret]: https://kubernetes.io/docs/concepts/configuration/secret/
<!-- markdownlint-enable url -->

{{% /choosable %}}

{{% choosable cloud gcp %}}

### Postgres Database

Create a Postgres database instance in [CloudSQL][gcp-cloudsql], and store its
connection information in a Kubernetes [Secret][k8s-secret] for apps to refer
to and consume.

```ts
import * as gcp from "@pulumi/gcp";
import * as k8s from "@pulumi/kubernetes";
import * as random from "@pulumi/random";

// Generate a strong password for the Postgres DB.
const postgresDbPassword = new random.RandomString(
    `${projectName}-db-password`,
    {
        length: 20,
        special: true,
    },
    { additionalSecretOutputs: ["result"] },
).result;

// Create a Postgres DB instance.
const db = new gcp.sql.DatabaseInstance("postgresdb", {
    project: config.project,
    region: "us-west1",
    databaseVersion: "POSTGRES_9_6",
    settings: { tier: "db-f1-micro" },
});

// Configure a new SQL user.
const user = new gcp.sql.User("default", {
    project: config.project,
    instance: db.name,
    password: postgresDbPassword,
});

// Create a new k8s provider.
const provider = new k8s.Provider("provider", {
    kubeconfig: config.kubeconfig,
});

// Create a Secret from the DB connection information.
const dbConn = new k8s.core.v1.Secret(
    "postgres-db-conn",
    {
        data: {
            host: db.privateIpAddress.apply(addr => Buffer.from(addr).toString("base64")),
            port: Buffer.from("5432").toString("base64"),
            username: user.name.apply(user => Buffer.from(user).toString("base64")),
            password: postgresDbPassword.apply(pass => Buffer.from(pass).toString("base64")),
        },
    },
    { provider: provider },
);
```

### Redis Datastore

Create a Redis datastore instance in [GCP Cloud MemoryStore][gcp-redis], and store its
connection information in a Kubernetes [ConfigMap][k8s-cm] for apps to refer
to and consume.

```ts
import * as gcp from "@pulumi/gcp";
import * as k8s from "@pulumi/kubernetes";

// Create a Redis instance.
const cache = new gcp.redis.Instance("redis", {
    tier: "STANDARD_HA",
    memorySizeGb: 1,
    redisVersion: "REDIS_3_2",
});

// Create a ConfigMap from the cache connection information.
const cacheConn = new k8s.core.v1.ConfigMap(
    "postgres-db-conn",
    {
        data: {
            host: cache.host.apply(addr => Buffer.from(addr).toString("base64")),
        },
    },
    { provider: provider },
);
```

<!-- markdownlint-disable url -->
[k8s-cm]: https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/
[k8s-secret]: https://kubernetes.io/docs/concepts/configuration/secret/
[gcp-redis]: https://cloud.google.com/memorystore/
[gcp-cloudsql]: https://cloud.google.com/sql/
<!-- markdownlint-enable url -->

{{% /choosable %}}

## General App Services

[General app services stack on GitHub](https://github.com/pulumi/kubernetes-guides/tree/master/general-app-services)

### NGINX Ingress Controller

The [NGINX Ingress Controller][nginx] is a custom Kubernetes [Controller][k8s-controller].
It manages [L7 network ingress][nginx-l7] / [north-south traffic][ns-traffic]
between external clients, and the servers in the cluster's apps.

<!-- markdownlint-disable url -->
[nginx]: https://github.com/kubernetes/ingress-nginx
[k8s-controller]: https://kubernetes.io/docs/concepts/architecture/controller/
[nginx-l7]: https://www.nginx.com/resources/glossary/layer-7-load-balancing/
[ns-traffic]: https://networkengineering.stackexchange.com/a/18877
<!-- markdownlint-enable url -->

#### Install NGINX

{{< chooser k8s-language "typescript,yaml" >}}

{{% choosable k8s-language yaml %}}

Deploy the [example YAML manifests][nginx-yaml] into the `ingress-nginx` namespace, and publicly expose it to the
Internet using a [load balanced Service][k8s-lb-svc].

> Note: NGINX requires a privileged PSP given its [use][nginx-priv-use] of `allowPrivilegeEscalation: true`.

```bash
$ kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/nginx-0.30.0/deploy/static/mandatory.yaml -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/nginx-0.30.0/deploy/static/provider/cloud-generic.yaml
```

Check that the NGINX deployment is running.

```bash
$ kubectl get pods -n ingress-nginx
NAME                                        READY   STATUS    RESTARTS   AGE
nginx-ingress-controller-7dcc95dfbf-k99k6   1/1     Running   0          21s
```

<!-- markdownlint-disable url -->
[nginx-priv-use]: https://github.com/kubernetes/ingress-nginx/blob/nginx-0.30.0/deploy/static/mandatory.yaml#L229
[nginx-yaml]: https://github.com/kubernetes/ingress-nginx/blob/master/docs/deploy/index.md#prerequisite-generic-deployment-command
[k8s-lb-svc]: https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer
<!-- markdownlint-enable url -->

{{% /choosable %}}

{{% choosable k8s-language typescript %}}

Deploy the [Helm chart][nginx-helm] into the `app-svcs` namespace created in [Configure
Cluster Defaults][crosswalk-k8s-defaults], and publicly expose it to the
Internet using a [load balanced Service][k8s-lb-svc].

> Note: NGINX requires a privileged PSP given its [use][nginx-priv-use] of `allowPrivilegeEscalation: true`.

```typescript
import * as k8s from "@pulumi/kubernetes";

// Deploy the NGINX ingress controller using the Helm chart.
const nginx = new k8s.helm.v3.Chart("nginx",
    {
        namespace: config.appSvcsNamespaceName,
        chart: "nginx-ingress",
        version: "1.24.4",
        fetchOpts: {repo: "https://charts.helm.sh/stable/"},
        values: {controller: {publishService: {enabled: true}}},
        transformations: [
            (obj: any) => {
                // Do transformations on the YAML to set the namespace
                if (obj.metadata) {
                    obj.metadata.namespace = config.appSvcsNamespaceName;
                }
            },
        ],
    },
    {providers: {kubernetes: provider}},
);
```

<!-- markdownlint-disable url -->
[nginx-priv-use]: https://github.com/helm/charts/blob/master/stable/nginx-ingress/values.yaml#L12
[k8s-lb-svc]: https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer
[nginx-helm]: https://github.com/helm/charts/tree/master/stable/nginx-ingress
[crosswalk-k8s-defaults]: /docs/guides/crosswalk/kubernetes/configure-defaults/#namespaces
<!-- markdownlint-enable url -->

{{% /choosable %}}

{{< /chooser >}}

#### Deploy a Workload

Deploy a [kuard][k8s-kuard] Pod, service, and ingress resources to
test the NGINX ingress controller.

Create the [ingress][k8s-ingress] resource for kuard that NGINX will manage by
keying off the `ingress.class` used.

NGINX will front the app through it's desired host and paths, and the apps are
will be accessible to the public internet as they share the public load balancer
endpoint provisioned for NGINX's service.

Traffic is then routed to the app by inspecting the host headers and paths
expected by NGINX onto the service that the kuard Pod runs.

{{< chooser k8s-language "typescript,yaml" >}}

{{% choosable k8s-language yaml %}}

```bash
$ kubectl run --generator=run-pod/v1 kuard --namespace=`pulumi stack output appsNamespaceName` --image=gcr.io/kuar-demo/kuard-amd64:blue --port=8080 --expose
```

```bash
$ cat > ingress.yaml << EOF
apiVersion: networking.k8s.io/v1beta1
kind: Ingress
metadata:
  name: kuard
  labels:
    app: kuard
  annotations:
    kubernetes.io/ingress.class: nginx
spec:
  rules:
  - host: apps.example.com
    http:
      paths:
        - path: "/"
          backend:
            serviceName: kuard
            servicePort: http
EOF
```

```bash
$ kubectl apply -f ingress.yaml --namespace=`pulumi stack output appsNamespaceName`
```

Check that the ingress is created, and after a few moments the `Address` will
be set to the NGINX LoadBalancer Service address.

```bash
$ kubectl describe ingress kuard --namespace=`pulumi stack output appsNamespaceName`
```

{{% /choosable %}}

{{% choosable k8s-language typescript %}}

```typescript
import * as k8s from "@pulumi/kubernetes";

// Create a kuard Deployment
const name = "kuard"
const labels = {app: name}
const deployment = new k8s.apps.v1.Deployment(name,
    {
        metadata: {
            namespace: config.appsNamespaceName,
            labels: {app: name},
        },
        spec: {
            replicas: 1,
            selector: { matchLabels: labels },
            template: {
                metadata: { labels: labels, },
                spec: {
                    containers: [
                        {
                            name: name,
                            image: "gcr.io/kuar-demo/kuard-amd64:blue",
                            resources: {requests: {cpu: "50m", memory: "20Mi"}},
                            ports: [{ name: "http", containerPort: 8080 }]
                        }
                    ],
                }
            }
        },
    },
    {provider: provider}
);

// Create a Service for the kuard Deployment
const service = new k8s.core.v1.Service(name,
    {
        metadata: {labels: labels, namespace: config.appsNamespaceName},
        spec: {ports: [{ port: 8080, targetPort: "http" }], selector: labels},
    },
    {provider: provider}
);

// Export the Service name and public LoadBalancer endpoint
export const serviceName = service.metadata.name;

// Create the kuard Ingress
const ingress = new k8s.extensions.v1beta1.Ingress(name,
    {
        metadata: {
            labels: labels,
            namespace: config.appsNamespaceName,
            annotations: {"kubernetes.io/ingress.class": "nginx"},
        },
        spec: {
            rules: [
                {
                    host: "apps.example.com",
                    http: {
                        paths: [
                            {
                                path: "/",
                                backend: {
                                    serviceName: serviceName,
                                    servicePort: "http",
                                }
                            },
                        ],
                    },
                }
            ]
        }
    },
    {provider: provider}
);
```

Check that the ingress is created, and after a few moments the `Address` will
be set to the NGINX LoadBalancer Service address.

```bash
$ kubectl describe ingress kuard-<POD_SUFFIX> --namespace=`pulumi stack output appsNamespaceName`
```

{{% /choosable %}}

{{< /chooser >}}

Use the NGINX LoadBalancer Service address to access kuard on its expected
hosts & paths. We simulate the headers using `curl`.

```bash
$ curl -Lv -H 'Host: apps.example.com' <INGRESS_ADDRESS>
```

#### Clean Up

{{< chooser k8s-language "typescript,yaml" >}}

{{% choosable k8s-language yaml %}}

Delete the pod, service, and ingress controller.

```bash
$ kubectl delete pod/kuard svc/kuard ingress/kuard
$ kubectl delete -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/nginx-0.30.0/deploy/static/mandatory.yaml -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/nginx-0.30.0/deploy/static/provider/cloud-generic.yaml
```

{{% /choosable %}}

{{% choosable k8s-language typescript %}}

Delete the nginx definition in the Pulumi program, and run a Pulumi update.

{{% /choosable %}}

{{< /chooser >}}

<!-- markdownlint-disable url -->
[k8s-kuard]: https://github.com/kubernetes-up-and-running/kuard
[k8s-ingress]: https://kubernetes.io/docs/concepts/services-networking/ingress/
<!-- markdownlint-enable url -->
