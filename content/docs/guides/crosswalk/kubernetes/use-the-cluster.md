---
title: Use the Cluster
menu:
  userguides:
    parent: crosswalk-kubernetes
    identifier: crosswalk-kubernetes-use-cluster
    weight: 4
---

{{< cloudchoose >}}

After running `pulumi up` the cluster will be created and there will be
[Pulumi outputs][pulumi-outputs] with fields like the cluster's `kubeconfig`
and its cluster name for reference and usage.

<div class="cloud-prologue-aws"></div>
<div class="mt">
{{% md %}}

## Overview

We'll examine how to:

  * [Access the Cluster](#access-the-cluster)
  * [Query the Cluster](#query-the-cluster)
  * [Deploy a Workload](#deploy-a-workload)

[crosswalk-configure-access]: {{< relref "/docs/guides/crosswalk/kubernetes/configure-access-control" >}}
{{% /md %}}
</div>

<div class="cloud-prologue-azure"></div>
<div class="mt">
{{% md %}}

TODO

{{% /md %}}
</div>

<div class="cloud-prologue-gcp"></div>
<div class="mt">
{{% md %}}

TODO

{{% /md %}}
</div>

### Access the Cluster

In EKS, the AWS account caller will be placed into the
`system:masters` Kubernetes RBAC group by default. The `kubeconfig`
generated will be specific to this primary cluster creator use-case. It must be
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

### Query the Cluster

Get cluster information.

```bash
$ kubectl version
$ kubectl cluster-info
```

Get nodes.

```bash
$ kubectl get nodes -o wide --show-labels
```

Get all pods.

```bash
$ kubectl get pods --all-namespaces -o wide --show-labels
```

### Deploy a Workload

Imperatively deploy a NGINX Pod and public load-balanced service:

```bash
$ kubectl run --generator=run-pod/v1 nginx --image=nginx --port=80 --expose --service-overrides='{"spec":{"type":"LoadBalancer"}}'
```

After it is deployed, visit the load balancer URL.

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

[pulumi-outputs]: https://www.pulumi.com/docs/intro/concepts/programming-model/#outputs
