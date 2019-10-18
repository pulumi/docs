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

In EKS, the AWS account caller will be placed into the
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

### Learn More

See the official [Kubernetes Basics][k8s-basics] tutorial for more details.

[pulumi-outputs]: https://www.pulumi.com/docs/intro/concepts/programming-model/#outputs
[crosswalk-configure-access]: {{< relref "/docs/guides/crosswalk/kubernetes/configure-access-control" >}}
[k8s-basics]: https://kubernetes.io/docs/tutorials/kubernetes-basics/
