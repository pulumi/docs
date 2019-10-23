---
title: Identity
linktitle: Identity
---

{{< cloudchoose >}}

<div class="cloud-prologue-aws"></div>
<div class="mt">
{{% md %}}

AWS exposes an [Identity Access and Management (IAM)][iam] API which can be used to grant
permissions to both human and bot users. Using this API, [**IAM User**][users] accounts can be
slotted into [**IAM Groups**][groups] (e.g., the `networkAdmins` IAM Group), which can then be
allocated baseline permissions using [**IAM Policies**][policies].

AWS workloads (e.g., AWS Lambdas) can also be granted permissions temporarily, without the need for usernames and passwords, using [**IAM Roles**][roles].

In [Crosswalk for AWS][crosswalk-aws] we showcase how to define IAM:

  - [Users][iam-users]
  - [Groups][iam-groups]
  - [Roles][iam-roles]
  - [Policies][iam-policies]

The full code for this stack is on [GitHub][gh-repo-stack].

[iam]: https://aws.amazon.com/iam/
[users]: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html
[groups]: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups.html
[roles]: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html
[policies]: https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html
[crosswalk-aws]: {{< relref "/docs/guides/crosswalk/aws" >}}
[iam-users]: {{< relref "/docs/guides/crosswalk/aws/iam#iam-users" >}}
[iam-groups]: {{< relref "/docs/guides/crosswalk/aws/iam#iam-groups" >}}
[iam-roles]: {{< relref "/docs/guides/crosswalk/aws/iam#iam-roles" >}}
[iam-policies]: {{< relref "/docs/guides/crosswalk/aws/iam#using-the-policydocument-interface" >}}
[gh-repo-stack]: https://github.com/pulumi/kubernetes-the-prod-way/tree/crosswalk/aws/01-identity
{{% /md %}}
</div>

<div class="cloud-prologue-azure"></div>
<div class="mt">
{{% md %}}

TODO

The full code for this stack is on [GitHub][gh-repo-stack].

[gh-repo-stack]: https://github.com/pulumi/kubernetes-the-prod-way/tree/crosswalk/azure/01-identity
{{% /md %}}
</div>

<div class="cloud-prologue-gcp"></div>
<div class="mt">
{{% md %}}

TODO

The full code for this stack is on [GitHub][gh-repo-stack].

[gh-repo-stack]: https://github.com/pulumi/kubernetes-the-prod-way/tree/crosswalk/gcp/01-identity
{{% /md %}}
</div>

<div class="cloud-prologue-aws"></div>
<div class="mt">
{{% md %}}

## Overview

We'll review how to:

  * [Create an IAM Role for Admins](#create-an-iam-role-for-admins)
  * [Create an IAM Role for Developers](#create-an-iam-role-for-developers)
  * [Create IAM Roles for EKS Node Groups](#create-iam-roles-for-eks-node-groups)

{{% /md %}}
</div>

<div class="cloud-prologue-azure"></div>
<div class="mt">
{{% md %}}

## Overview

We'll review how to:

  * [Create an IAM Role for Admins](#create-an-iam-role-for-admins)
  * [Create an IAM Role for Developers](#create-an-iam-role-for-developers)
  * [Create IAM Roles for AKS Node Pools](#create-iam-roles-for-aks-node-pools)

{{% /md %}}
</div>

<div class="cloud-prologue-gcp"></div>
<div class="mt">
{{% md %}}

## Overview

We'll review how to:

  * [Create an IAM Role for Admins](#create-an-iam-role-for-admins)
  * [Create an IAM Role for Developers](#create-an-iam-role-for-developers)
  * [Create IAM Roles for GKE Node Pools](#create-iam-roles-for-gke-node-pools)

{{% /md %}}
</div>

## Create an IAM Role for Admins

<div class="cloud-prologue-aws"></div>
<div class="mt">
{{% md %}}

Create an admin role in AWS that assumes the AWS account caller,
and attach EKS admin policies to the role. This role will be mapped into the
[`system:masters`][k8s-sys-masters] group in Kubernetes RBAC.

```typescript
import * as aws from "@pulumi/aws";

// Create the EKS cluster admins role.
const adminsName = "admins";
const adminsIamRole = new aws.iam.Role(`${adminsName}-eksClusterAdmin`, {
    assumeRolePolicy: aws.getCallerIdentity().then(id =>
        aws.iam.assumeRolePolicyForPrincipal({"AWS": `arn:aws:iam::${id.accountId}:root`}))
})
const adminsIamRolePolicy = new aws.iam.RolePolicy(`${adminsName}-eksClusterAdminPolicy`, {
    role: adminsIamRole,
    policy: {
        Version: "2012-10-17",
        Statement: [
            { Effect: "Allow", Action: ["eks:*", "ec2:DescribeImages"], Resource: "*", },
            { Effect: "Allow", Action: "iam:PassRole", Resource: "*"},
        ],
    },
},
    { parent: adminsIamRole },
);
```
[k8s-sys-masters]: https://kubernetes.io/docs/reference/access-authn-authz/rbac#user-facing-roles
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

## Create an IAM Role for Developers

<div class="cloud-prologue-aws"></div>
<div class="mt">
{{% md %}}

Create a developer role in AWS that assumes the AWS account caller.
This role will be mapped into a limited developer role in Kubernetes RBAC.

```typescript
import * as aws from "@pulumi/aws";

// Create the EKS cluster developers role.
const devName = "devs";
const devsIamRole = new aws.iam.Role(`${devName}-eksClusterDeveloper`, {
    assumeRolePolicy: aws.getCallerIdentity().then(id =>
        aws.iam.assumeRolePolicyForPrincipal({"AWS": `arn:aws:iam::${id.accountId}:root`}))
})
```

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

<div class="cloud-prologue-aws"></div>
<div class="mt">
{{% md %}}
## Create IAM Roles for EKS Node Groups

Create a node group worker role in AWS that assumes the EC2 Service, and attach
required EKS cluster polices to the role. This role will be used by the node group in an
instance profile during cluster configuration and creation.

```typescript
// The managed policies EKS requires of nodegroups join a cluster.
const nodegroupManagedPolicyArns: string[] = [
    "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy",
    "arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy",
    "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly",
];

// Create the standard node group worker role and attach the required policies.
const stdName = "standardNodeGroup";
const stdNodegroupIamRole = new aws.iam.Role(`${stdName}-eksClusterWorkerNode`, {
    assumeRolePolicy: aws.iam.assumeRolePolicyForPrincipal({"Service": "ec2.amazonaws.com"})
})
attachPoliciesToRole(stdName, stdNodegroupIamRole, nodegroupManagedPolicyArns);

// Create the performant node group worker role and attach the required policies.
const perfName = "performanceNodeGroup";
const perfNodegroupIamRole = new aws.iam.Role(`${perfName}-eksClusterWorkerNode`, {
    assumeRolePolicy: aws.iam.assumeRolePolicyForPrincipal({"Service": "ec2.amazonaws.com"})
})
attachPoliciesToRole(perfName, perfNodegroupIamRole, nodegroupManagedPolicyArns);

// Attach policies to a role.
function attachPoliciesToRole(name: string, role: aws.iam.Role, policyArns: string[]) {
    for (const policyArn of policyArns) {
        new aws.iam.RolePolicyAttachment(`${name}-${policyArn.split('/')[1]}`,
            { policyArn: policyArn, role: role },
        );
    }
}
```

{{% /md %}}
</div>

<div class="cloud-prologue-azure"></div>
<div class="mt">
{{% md %}}
## Create IAM Roles for AKS Node Pools

TODO

```typescript
// TODO
```

{{% /md %}}
</div>

<div class="cloud-prologue-gcp"></div>
<div class="mt">
{{% md %}}
## Create IAM Roles for GKE Node Pools

TODO

```typescript
// TODO
```

{{% /md %}}
</div>
