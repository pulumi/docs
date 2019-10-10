---

title: Identity

aliases: ["/docs/guides/crosswalk/kubernetes/aws/identity/"]
---

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

## Creating an IAM Role for Kubernetes Admins

Create an admin role in AWS that assumes the AWS account caller,
and attach EKS admin policies to the role. This role will be mapped into the
[`system:masters`][k8s-sys-masters] group in Kubernetes RBAC.

```typescript
import * as aws from "@pulumi/aws";

// Create the EKS cluster admins role.
const adminName = "admins";
const adminsIamRole = new aws.iam.Role(`${adminName}-eksClusterAdmin`, {
    assumeRolePolicy: aws.getCallerIdentity().then(id =>
        aws.iam.assumeRolePolicyForPrincipal({"AWS": `arn:aws:iam::${id.accountId}:root`}))
})
const adminsIamRolePolicy = new aws.iam.RolePolicy(`${adminName}-eksClusterAdminPolicy`, {
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

## Creating an IAM Role for Kubernetes Developers

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

## Creating IAM Roles for Kubernetes NodeGroups

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
const stdNodegroupIamRoleName = "standardNodeGroup";
const stdNodegroupIamRole = new aws.iam.Role(`${stdNodegroupIamRoleName}-eksClusterWorkerNode`, {
    assumeRolePolicy: aws.iam.assumeRolePolicyForPrincipal({"Service": "ec2.amazonaws.com"})
})
attachPoliciesToRole(stdNodegroupIamRoleName, stdNodegroupIamRole, nodegroupManagedPolicyArns);

// Create the performant node group worker role and attach the required policies.
const perfNodegroupIamRoleName = "performanceNodeGroup";
const perfNodegroupIamRole = new aws.iam.Role(`${perfNodegroupIamRoleName}-eksClusterWorkerNode`, {
    assumeRolePolicy: aws.iam.assumeRolePolicyForPrincipal({"Service": "ec2.amazonaws.com"})
})
attachPoliciesToRole(perfNodegroupIamRoleName, perfNodegroupIamRole, nodegroupManagedPolicyArns);

// Attach policies to a role.
function attachPoliciesToRole(name: string, role: aws.iam.Role, policyArns: string[]) {
    for (const policyArn of policyArns) {
        new aws.iam.RolePolicyAttachment(`${name}-${policyArn.split('/')[1]}`,
            { policyArn: policyArn, role: role },
        );
    }
}
```

[iam]: https://aws.amazon.com/iam/
[users]: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html
[groups]: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups.html
[roles]: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html
[policies]: https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html
[crosswalk-aws]: /docs/guides/crosswalk/aws
[iam-users]: /docs/guides/crosswalk/aws/iam/#iam-users
[iam-groups]: /docs/guides/crosswalk/aws/iam/#iam-groups
[iam-roles]: /docs/guides/crosswalk/aws/iam/#iam-roles
[iam-policies]: /docs/guides/crosswalk/aws/iam/#using-the-policydocument-interface
[gh-repo-stack]: https://github.com/metral/kubernetes-the-prod-way/tree/metral/crosswalk/aws/01-identity
[k8s-sys-masters]: https://kubernetes.io/docs/reference/access-authn-authz/rbac/#user-facing-roles
