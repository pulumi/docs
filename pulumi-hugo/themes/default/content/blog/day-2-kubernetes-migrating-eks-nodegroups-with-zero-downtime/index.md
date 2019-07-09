---
title: "Day 2 Kubernetes - Migrating EKS Node Groups with Zero Downtime"
authors: ["mike-metral"]
tags: ["Kubernetes","EKS", "Migrations", "Node Groups"]
date: "2019-07-22"

meta_image: "eks-migrate-nodegroups.png"
---

Managed Kubernetes offerings greatly reduce the overhead required in
administering Kubernetes. However, the cluster is only one of the
components under management, as app lifecycles are self-driven tasks
that vary by workloads.

In Kubernetes, node groups are a useful mechanism of creating pools of resources that can enforce
scheduling requirements. They also provide a utility for shifting
workloads around during cluster management and updates.

In this post, we'll see how to use Pulumi for Day 2 Kubernetes administration.
We'll spin up a new EKS cluster with two node groups and a given workload.
Then we'll add one more node group with an updated configuration, and migrate the workload
over to it with zero downtime using code and `kubectl`.

<!--more-->

[View the full tutorial and code.][eks-nodegroup-tutorial]

<p align="center"><img src="eks-migrate-nodegroups.svg" width="650"/></p>

## Create an EKS cluster and Deploy the Workload

The inital update we'll perform will configure and launch an EKS cluster using
`v1.13` of Kubernetes, along with the cluster's infrastructure dependencies
(VPC and IAM) using [Crosswalk for AWS][crosswalk-aws]. We'll also
create and attach the following node groups to the cluster:

* A standard `t2.medium` worker node group using the recent `v1.13.7` worker [AMI][eks-amis]. For use by general purpose workloads such as the [`EchoServer`][echoserver], a simple app that echo's client request headers.
* A 2xlarge `t3.2xlarge` worker node group using an older `v1.12.7` worker [AMI][eks-amis]. For use use by larger, intensive workloads such as the [NGINX Ingress Controller][ingress-nginx].

With the cluster successfully created and the node groups available, Pulumi
will deploy the workload: the [`EchoServer`][echoserver], and the [NGINX Ingress Controller][ingress-nginx] that will manage it's ingress.
The `echoserver` will land on the Standard node group, and NGINX is set
to specifically target the `2xlarge` node group.

Once the workload is deployed, we can validate it is up and running by accessing
the `echoserver` behind the NGINX endpoint using `curl`:

<img style="max-width:none; height: 350px; width: 850px;" src="k8s-cluster-workload.gif"/>

> **Note**: You can open the <a href="./k8s-cluster-workload.gif" target="_blank">GIF</a> for a maximized view.

## The Great Migration

After initial deployment, we decide to update the node group used by NGINX.

We'll move NGINX from the `2xlarge` node group over to a new, `4xlarge` worker
node group that differs in: an updated AMI, instance type, and desired instance count.

As we migrate NGINX over to the `4xlarge` and decommission the `2xlarge` node
group in the next steps, we'll also actively load test the endpoint of the
`echoserver` to ensure that we are not losing requests through out the migration.

### Step 1: Create the new `4xlarge` Node Group

Create the new, `4xlarge` node group by defining it and running an update.

<p align="center"><img src="ng-4xlarge.svg" width="650"/></p>

### Step 2: Migrate NGINX to the `4xlarge` Node Group

With the `4xlarge` node group created, we'll migrate the NGINX service away
from the `2xlarge` node group over to the `4xlarge` node group by changing
its node selector scheduling terms.

This change updates the NGINX Deployment spec to require the use of
`c5.4xlarge` nodes during scheduling, and forces a rolling update over to the
`4xlarge` node group.

NGINX is able to successfully migrate across node groups because it is
configured with HA settings, [spread-type scheduling predicates][tutorial-ha-refs],
and can gracefully terminate within the Kubernetes [Pod lifecycle][pod-lifecycle].

<p align="center"><img src="target-ng-4xlarge.svg" width="650"/></p>

### Step 3: Decomission the `2xlarge` Node Group

Once migration of NGINX has completed onto the `4xlarge` node group, we can
commence the decommissioning of the original `2xlarge` node group no
longer in use from Kubernetes and AWS.

Decommissioning the node group means that we'll:

  * Drain the Kubernetes nodes.
  * Delete the Kubernetes nodes from the APIServer.
  * Scale down the Auto Scaling Group to `0`.
  * Delete the node group.

Setup `kubectl` by using the `kubeconfig` from the stack output.

```bash
$ pulumi stack output kubeconfig > kubeconfig.json
$ export KUBECONFIG=$PWD/kubeconfig.json
```

To drain the `2xlarge` node group, we'll use `kubectl drain`:

```bash
for node in $(kubectl get nodes -l beta.kubernetes.io/instance-type=t3.2xlarge -o=name); do
    kubectl drain --force --ignore-daemonsets --delete-local-data --grace-period=10 "$node";
done
```

After draining has completed, to delete the nodes from the APIServer use `kubectl delete node`:

```bash
for node in $(kubectl get nodes -l beta.kubernetes.io/instance-type=t3.2xlarge -o=name); do
    kubectl delete "$node";
done
```

Scale down the node group Auto Scaling Group completely by setting
the `desiredCapacity: 0` and running an update:

<p align="center"><img src="scale-down-ng-2xlarge.svg" width="650"/></p>

Once the Auto Scaling Group has scaled down, we can delete the node group from
AWS and the Pulumi program:

<p align="center"><img src="remove-ng-2xlarge.svg" width="650"/></p>

## Summary

In this post we stood up an EKS cluster with a couple of node groups, and an
`echoserver` and NGINX workload. We then created a new, updated node group and
migrated NGINX over to it.

We acheived this node group migration with zero downtime to our apps during
load testing and decommissioning of the original node group.

<img style="max-width:none; height: 350px; width: 850px;" src="eks-migration.gif"/>

> **Note**: You can open the <a href="./eks-migration.gif" target="_blank">GIF</a> for a maximized view.

## Learn More

If you'd like to learn about Pulumi and how to manage your
infrastructure and Kubernetes through code, [click here to get started today]({{< ref "/docs/quickstart" >}}). Pulumi is open source and free to
use.

For a follow-up example on how to further use Pulumi to create Kubernetes
clusters, or deploy workloads to a cluster, check out the rest of the
[Kubernetes tutorials]({{< relref "/docs/reference/tutorials/kubernetes" >}}).

As always, you can check out our code on
[GitHub](https://github.com/pulumi), follow us on
[Twitter](https://twitter.com/pulumicorp), subscribe to our [YouTube
channel](https://www.youtube.com/channel/UC2Dhyn4Ev52YSbcpfnfP0Mw), or
join our [Community Slack](https://slack.pulumi.io/) channel if you have
any questions, need support, or just want to say hello.

If you'd like to chat with our team, or get hands-on assistance with
migrating your existing configuration code (including ksonnet programs)
to Pulumi, please don't hesitate to [drop us a line]({{< ref "/contact" >}}).

[eks-amis]: https://docs.aws.amazon.com/eks/latest/userguide/eks-optimized-ami.html
[ingress-nginx]: https://github.com/kubernetes/ingress-nginx
[echoserver]: https://github.com/kubernetes-retired/contrib/blob/master/ingress/echoheaders/echo-app.yaml
[pod-lifecycle]: https://kubernetes.io/docs/concepts/workloads/pods/pod/#termination-of-pods
[eks-nodegroup-tutorial]: {{< relref "/docs/reference/tutorials/kubernetes/tutorial-eks-migrate-nodegroups" >}}
[crosswalk-aws]: {{< relref "/docs/reference/crosswalk/aws" >}}.
[tutorial-ha-refs]: {{< relref "/docs/reference/tutorials/kubernetes/tutorial-eks-migrate-nodegroups#kubernetes-workloads-high-availability-ha-rolling-updates" >}}
