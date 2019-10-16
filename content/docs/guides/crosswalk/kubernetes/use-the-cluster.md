---
title: Use the Cluster
menu:
  userguides:
    parent: crosswalk-kubernetes
    identifier: crosswalk-kubernetes-use-cluster
    weight: 4
---

After running `pulumi up` the cluster will be created and there will exist
[Pulumi outputs][pulumi-outputs] with fields like the cluster's `kubeconfig`
and it's cluster name for reference and usage.

In EKS, the AWS account caller will be placed into the
`system:masters` Kubernetes RBAC group by default. The `kubeconfig`
generated will cater to this primary cluster creator use-case, and it must be
copied, and reconfigured to use with other IAM roles the caller assumes, as
demonstrated below in [Use Kubernetes RBAC](#use-kubernetes-rbac).

### Access the Cluster

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
$ kubectl get nodes
$ kubectl get nodes -o wide --show-labels -l beta.kubernetes.io/instance-type=t2.medium
$ kubectl get nodes -o wide --show-labels -l beta.kubernetes.io/instance-type=t3.2xlarge
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

```bash
$ if ING_LB=$((kubectl get svc nginx -o template --template='{{(index .status.loadBalancer.ingress 0).hostname}}') 2>&1) ; then echo "http://$ING_LB"; else echo "LB is not ready yet."; fi
```

Delete the pod and service.

```bash
$ kubectl delete pod/nginx svc/nginx
```

[pulumi-outputs]: https://www.pulumi.com/docs/intro/concepts/programming-model/#outputs
