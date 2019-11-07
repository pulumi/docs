---
title: Try out the Cluster
menu:
  userguides:
    parent: crosswalk-kubernetes
    identifier: crosswalk-kubernetes-use-cluster
    weight: 3
---

{{< cloudchoose >}}

After the cluster is created with a Pulumi update, there will be
[outputs][pulumi-outputs] with fields like the cluster's `kubeconfig` file
contents, and its cluster name for reference.

## Overview

We'll explore how to:

  * [Access the Cluster](#access-the-cluster)
  * [Query the Cluster](#query-the-cluster)
  * [Deploy a Workload](#deploy-a-workload)
  * [Learn More](#learn-more)

### Access the Cluster

<div class="cloud-prologue-aws"></div>
<div class="mt">
{{% md %}}
In EKS, the account caller will be placed into the
`system:masters` Kubernetes RBAC group by default. The `kubeconfig`
generated will cater to this primary cluster creator use-case, and it must be
copied, and reconfigured to use with other IAM roles the caller assumes, as
demonstrated in [Configure Access Control][crosswalk-configure-access].

To access your new Kubernetes cluster using `kubectl`, we need to setup the
`kubeconfig` file.

```bash
$ pulumi stack output kubeconfig > kubeconfig.json
```

Or in JSON pretty-print.

```bash
$ pulumi stack output kubeconfig | jq '.' > kubeconfig.json
```

Export the environment variable for `kubectl` usage.

```bash
$ export KUBECONFIG=`pwd`/kubeconfig.json
```
[crosswalk-configure-access]: {{< relref "/docs/guides/crosswalk/kubernetes/configure-access-control" >}}
{{% /md %}}
</div>
<div class="cloud-prologue-azure"></div>
<div class="mt">
{{% md %}}
In AKS, the account caller will be placed into the
`system:masters` Kubernetes RBAC group by default. Two `kubeconfig` files will
be generated will that will cater to the admin and cluster user [use-cases][aks-cluster-roles].
To configure the cluster for use with IAM roles, check out
[Configure Access Control][crosswalk-configure-access].

To access your new Kubernetes cluster using `kubectl`, we need to setup the
`kubeconfig` file.

```bash
$ pulumi stack output kubeconfigAdmin > kubeconfig-admin.json
```

Or in JSON pretty-print.

```bash
$ pulumi stack output kubeconfigAdmin | jq '.' > kubeconfig-admin.json
```

Export the environment variable for `kubectl` usage.

```bash
$ export KUBECONFIG=`pwd`/kubeconfig-admin.json
```

[aks-cluster-roles]: https://docs.microsoft.com/en-us/azure/aks/control-kubeconfig-access#available-cluster-roles-permissions
[crosswalk-configure-access]: {{< relref "/docs/guides/crosswalk/kubernetes/configure-access-control" >}}
{{% /md %}}
</div>
<div class="cloud-prologue-gcp"></div>
<div class="mt">
{{% md %}}
In GCP, the account caller will be placed into the
`system:masters` Kubernetes RBAC group by default. The `kubeconfig`
generated will cater to this primary cluster creator use-case. `gcloud` auth
will leverage tokens to use with other users or ServiceAccounts as
demonstrated in [Configure Access Control][crosswalk-configure-access].

To access your new Kubernetes cluster using `kubectl`, we need to setup the
`kubeconfig` file.

```bash
$ pulumi stack output kubeconfig > kubeconfig.json
```

Or in JSON pretty-print.

```bash
$ pulumi stack output kubeconfig | jq '.' > kubeconfig.json
```

Export the environment variable for `kubectl` usage.

```bash
$ export KUBECONFIG=`pwd`/kubeconfig.json
```

[crosswalk-configure-access]: {{< relref "/docs/guides/crosswalk/kubernetes/configure-access-control" >}}
{{% /md %}}
</div>

### Query the Cluster

Get cluster information.

```bash
$ kubectl version
$ kubectl cluster-info
```

Get the nodes.

```bash
$ kubectl get nodes -o wide --show-labels
```

Get all pods in the cluster, and show output attributes.

```bash
$ kubectl get pods --all-namespaces -o wide --show-labels
```

### Deploy a Workload

{{< k8s-language nokx >}}

<div class="k8s-language-prologue-yaml"></div>
<div class="mt">
{{% md %}}
Imperatively deploy a NGINX Pod and public load-balanced service:

```bash
$ kubectl run --generator=run-pod/v1 nginx --image=nginx --port=80 --expose --service-overrides='{"spec":{"type":"LoadBalancer"}}'
```

After a few moments, visit the load balancer URL.

<div class="cloud-prologue-aws"></div>
<div class="mt">
{{% md %}}

```bash
$ if ING_LB=$((kubectl get svc nginx -o template --template='{{(index .status.loadBalancer.ingress 0).hostname}}') 2>&1) ; then echo "http://$ING_LB"; else echo "LB is not ready yet."; fi
```

{{% /md %}}
</div>

<div class="cloud-prologue-azure"></div>
<div class="mt">
{{% md %}}

```bash
$ if ING_LB=$((kubectl get svc nginx -o template --template='{{(index .status.loadBalancer.ingress 0).ip}}') 2>&1) ; then echo "http://$ING_LB"; else echo "LB is not ready yet."; fi
```

{{% /md %}}
</div>

<div class="cloud-prologue-gcp"></div>
<div class="mt">
{{% md %}}

```bash
$ if ING_LB=$((kubectl get svc nginx -o template --template='{{(index .status.loadBalancer.ingress 0).ip}}') 2>&1) ; then echo "http://$ING_LB"; else echo "LB is not ready yet."; fi
```

{{% /md %}}
</div>

Delete the pod and service.

```bash
$ kubectl delete pod/nginx svc/nginx
```
{{% /md %}}
</div>

<div class="k8s-language-prologue-typescript"></div>
<div class="mt">
{{% md %}}
Beclaratively deploy a NGINX Pod and public load-balanced service:

```ts
import * as k8s from "@pulumi/kubernetes";

// Expose a k8s provider instance of the cluster.
const provider = new k8s.Provider("provider", {kubeconfig: kubeconfig });

// Create a NGINX Pod
const nginx = new k8s.core.v1.Pod(name,
    {
        metadata: {labels: {app: "nginx"}},
        spec: {
            containers: [
                {
                    name: name,
                    image: "nginx:latest",
                    ports: [{ name: "http", containerPort: 80 }]
                }
            ],
        }
    }, {provider: provider}
);

// Create a LoadBalancer Service for the NGINX Deployment
const service = new k8s.core.v1.Service(name,
    {
        metadata: {labels: {app: "nginx"}},
        spec: {
            type: "LoadBalancer",
            ports: [{ port: 80, targetPort: "http" }],
            selector: {app: "nginx"},
        },
    }, {provider: provider}
);
```

<div class="cloud-prologue-aws"></div>
<div class="mt">
{{% md %}}
```ts
// Export the Service name and public LoadBalancer Endpoint
export const serviceName = service.metadata.apply(m => m.name);
export const serviceHostname = service.status.apply(s => s.loadBalancer.ingress[0].hostname)
```

After a few moments, visit the load balancer listed in the `serviceHostname`.

```bash
$ curl `pulumi stack output serviceHostname`
```

{{% /md %}}
</div>
<div class="cloud-prologue-azure"></div>
<div class="mt">
{{% md %}}
```ts
// Export the Service name and public LoadBalancer Endpoint
export const serviceName = service.metadata.apply(m => m.name);
export const serviceIp = service.status.apply(s => s.loadBalancer.ingress[0].ip)
```

After a few moments, visit the load balancer listed in the `serviceIp`.

```bash
$ curl `pulumi stack output serviceIp`
```

{{% /md %}}
</div>
<div class="cloud-prologue-gcp"></div>
<div class="mt">
{{% md %}}
```ts
// Export the Service name and public LoadBalancer Endpoint
export const serviceName = service.metadata.apply(m => m.name);
export const serviceHostname = service.status.apply(s => s.loadBalancer.ingress[0].ip)
```

After a few moments, visit the load balancer listed in the `serviceIp`.

```bash
$ curl `pulumi stack output serviceIp`
```

{{% /md %}}
</div>
To tear down NGINX, delete it's definition in the Pulumi program and run a Pulumi update.
{{% /md %}}
</div>

### Learn More

See the official [Kubernetes Basics][k8s-basics] tutorial for more details.

[pulumi-outputs]: https://www.pulumi.com/docs/intro/concepts/programming-model/#outputs
[k8s-basics]: https://kubernetes.io/docs/tutorials/kubernetes-basics/
