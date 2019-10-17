---
title: Update the Worker Nodes
menu:
  userguides:
    parent: crosswalk-kubernetes
    identifier: crosswalk-kubernetes-update-workers
    weight: 3
---

{{< cloudchoose >}}

TODO - Intro

## Overview

We'll examine how to:

  * [Update an Existing Node Group](#update-an-existing-node-group)
  * [Migrate to a New Node Group](#migrate-to-a-new-node-group)

### Update an Existing Node Group

<div class="cloud-prologue-aws"></div>
<div class="mt">
{{% md %}}

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

[k8s-version-skew]: https://kubernetes.io/docs/setup/release/version-skew-policy/#supported-version-skew
[aws-update-ng]: https://docs.aws.amazon.com/eks/latest/userguide/update-stack.html
{{% /md %}}
</div>

<div class="cloud-prologue-azure"></div>
<div class="mt">
{{% md %}}

TODO

```typescript
// TODO
```

{{% /md %}}
</div>

<div class="cloud-prologue-gcp"></div>
<div class="mt">
{{% md %}}

TODO

```typescript
// TODO
```

{{% /md %}}
</div>

### Migrate to a New Node Group

For a complete example of migrating node groups, please see [Migrating Node Groups with Zero Downtime][migrate-ng-tutorial].  

<div class="cloud-prologue-aws"></div>
<div class="mt">
{{% md %}}

See the [official AWS docs][aws-migrate-ng] for more details.

[aws-migrate-ng]: https://docs.aws.amazon.com/eks/latest/userguide/migrate-stack.html
{{% /md %}}
</div>

<div class="cloud-prologue-azure"></div>
<div class="mt">
{{% md %}}


{{% /md %}}
</div>

<div class="cloud-prologue-gcp"></div>
<div class="mt">
{{% md %}}


{{% /md %}}
</div>

[migrate-ng-tutorial]: {{< relref "/docs/tutorials/kubernetes/eks-migrate-nodegroups" >}}
