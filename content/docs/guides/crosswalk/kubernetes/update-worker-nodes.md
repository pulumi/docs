---
title_tag: Updating Kubernetes Worker Nodes | Crosswalk
title: Updating Kubernetes Worker Nodes
meta_desc: This page provides a guide on how to update Kubernetes Worker Nodes
           with Pulumi.
menu:
  userguides:
    parent: crosswalk-kubernetes
    identifier: crosswalk-kubernetes-update-workers
    weight: 10
---

{{< chooser cloud "aws,azure,gcp" / >}}

Updating the worker nodes is a multi-step process that includes proper management
of the nodes themselves, and the apps running on the them. Kubernetes is best
equipped to easily update [stateless][k8s-stateless] apps, but can also manage
stateful apps using [StatefulSets][k8s-stateful] with user and ops-driven
assistance.

Apps must comply to the [Pod termination lifecycle][k8s-term-lifecyce] to
properly terminate, and should leverage capabilities such as [Node selectors][k8s-node-selectors],
[affinity][k8s-affinity], and [probes][k8s-probes] to guarantee expected
scheduling, and readiness during updates.

{{% choosable cloud aws %}}

The full code for this stack is on [GitHub](https://github.com/pulumi/kubernetes-guides/tree/master/aws/03-cluster-configuration).

{{% /choosable %}}

{{% choosable cloud azure %}}

The full code for this stack is on [GitHub](https://github.com/pulumi/kubernetes-guides/tree/master/azure/03-cluster-configuration).

{{% /choosable %}}

{{% choosable cloud gcp %}}

The full code for this stack is on [GitHub](https://github.com/pulumi/kubernetes-guides/tree/master/gcp/03-cluster-configuration).

{{% /choosable %}}

## Overview

We'll examine how to:

- [Overview](#overview)
  - [Update an Existing Node Group](#update-an-existing-node-group)
  - [Migrate to a New Node Group](#migrate-to-a-new-node-group)

### Update an Existing Node Group

{{% choosable cloud aws %}}

Updating an existing node group can be trivial for basic property changes.

1. Verify that enough capacity is available in the cluster to handle workload
   spillover when the desired node group is scaled down.
1. Edit the `desiredCapacity` and `minSize` of the node group to scale down to
   a value of `0`.
1. Run an update with `pulumi up`.
1. Update the desired node group properties, such as the `instanceType` or `amiId`.
1. Scale the node group up to the desired value.
1. Run an update with `pulumi up`.

   > Note: [Don't drift][k8s-version-skew] far apart in minor Kubernetes versions between
   > the node group workers and the control plane.

See the [official AWS docs][aws-update-ng] for more details.

[k8s-version-skew]: https://kubernetes.io/docs/setup/release/version-skew-policy/#supported-version-skew
[aws-update-ng]: https://docs.aws.amazon.com/eks/latest/userguide/update-stack.html

{{% /choosable %}}

{{% choosable cloud azure %}}

Updating an existing node group can be trivial for basic property changes.

1. Verify that enough capacity is available in the cluster to handle workload
   spillover when the desired node group is scaled down.
1. Edit the node pool in VMSS portal to a value of `0`, as node pools cannot
   currently be scaled down to `0`, but it's [availability is planned][aks-scaledown].
1. Update the desired node group properties, such as the `vmSize` or
   `kubernetesVersion`.
1. Scale the node pool up to the desired value.
1. Run an update with `pulumi up`.

   > Note: [Don't drift][k8s-version-skew] far apart in minor Kubernetes versions between
   > the node group workers and the control plane.

See the official AKS [docs][aks-upgrade-docs] for more details.

[aks-scaledown]: https://github.com/Azure/AKS/issues/1050
[k8s-version-skew]: https://kubernetes.io/docs/setup/release/version-skew-policy/#supported-version-skew
[aks-upgrade-docs]: https://docs.microsoft.com/en-us/azure/aks/upgrade-cluster

{{% /choosable %}}

{{% choosable cloud gcp %}}

By default, GKE clusters and node pools have their versions upgraded automatically.

Manually updating an existing node group can be trivial for basic property changes.

1. Verify that enough capacity is available in the cluster to handle workload
   spillover when the desired node group is scaled down.
1. Edit the `initialNodeCount` of the node group to a value of `0`.
1. Run an update with `pulumi up`.
1. Update the desired node group properties, such as the `machineType` or
   `version`.
1. Scale the node pool up to the desired value.
1. Run an update with `pulumi up`.

   > Note: [Don't drift][k8s-version-skew] far apart in minor Kubernetes versions between
   > the node group workers and the control plane.

See the official GKE [docs][gke-upgrade-docs], and [cluster autoscaler docs][gke-autoscaler] for more details.

[k8s-version-skew]: https://kubernetes.io/docs/setup/release/version-skew-policy/#supported-version-skew
[gke-upgrade-docs]: https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster
[gke-autoscaler]: https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler

{{% /choosable %}}

### Migrate to a New Node Group

For an example of migrating node groups, see the general steps outlined in [Migrating Node Groups with Zero Downtime][migrate-ng-tutorial].

<!-- markdownlint-disable url -->
[migrate-ng-tutorial]: /registry/packages/kubernetes/how-to-guides/eks-migrate-nodegroups/
[k8s-stateless]: https://kubernetes.io/docs/tasks/run-application/run-stateless-application-deployment
[k8s-stateful]: https://kubernetes.io/docs/concepts/workloads/controllers/statefulset
[k8s-affinity]: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#inter-pod-affinity-and-anti-affinity-beta-feature
[k8s-probes]: https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-probes
[k8s-term-lifecyce]: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks
[k8s-node-selectors]: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#affinity-and-anti-affinity
<!-- markdownlint-enable url -->
