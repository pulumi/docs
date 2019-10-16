---
title: Update the Worker Nodes
menu:
  userguides:
    parent: crosswalk-kubernetes
    identifier: crosswalk-kubernetes-update-workers
    weight: 3
---

TODO - Intro

### Update an Existing Node Group

Updating an existing node group can be trivial for basic changes.

1. Verify that enough capacity is available in the cluster to handle workload
   spillover when the desired node group is scaled down.
1. Edit the `desiredCapacity` and `minSize` of the node group to scale down to
   a value of `0`.
1. Run an update with `pulumi up`.
1. Update the desired node group properties, such as the `instanceType` or `amiId`.
1. Run an update with `pulumi up`.

   > Note: [Don't drift][k8s-version-skew] far apart in minor Kubernetes versions between
   > the node group workers and the control plane.

See the [official AWS docs][aws-update-ng] for more details.

### Migrate to a New Node Group

For a complete example of migrating node groups, please see [Migrating Node Groups with Zero Downtime][migrate-ng-tutorial].  

See the [official AWS docs][aws-migrate-ng] for more details.

[k8s-version-skew]: https://kubernetes.io/docs/setup/release/version-skew-policy/#supported-version-skew
[migrate-ng-tutorial]: {{< relref "/docs/tutorials/kubernetes/eks-migrate-nodegroups" >}}
[aws-update-ng]: https://docs.aws.amazon.com/eks/latest/userguide/update-stack.html
[aws-migrate-ng]: https://docs.aws.amazon.com/eks/latest/userguide/migrate-stack.html
