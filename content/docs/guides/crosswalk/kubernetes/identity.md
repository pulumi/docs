---
title: Identity
linktitle: Identity
---

{{< cloudchoose >}}

<div class="cloud-prologue-aws"></div>
<div class="mt">
{{% md %}}

AWS exposes an [Identity Access and Management (IAM)][iam] API which can be used to grant
permissions to both human and bot users. Using this API, [IAM User][users] accounts can be
slotted into [IAM Groups][groups] (e.g., the `networkAdmins` IAM Group), which can then be
allocated baseline permissions using [IAM Policies][policies].

AWS workloads (e.g., AWS Lambdas) can also be granted permissions temporarily, without the need for usernames and passwords, using [IAM Roles][roles].

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

Azure exposes an [Active Directory][azure-iam] API which can be used to grant
permissions to both human and bot users. Using this API, [IAM User][azure-users] accounts can be
slotted into [IAM Groups][azure-groups] (e.g., the `networkAdmins` IAM Group), which can then be
allocated baseline permissions using [IAM Permissions][azure-permissions].

Azure services can also be granted permissions temporarily, without the need for usernames and passwords, using [Applications and ServicePrincipals][azure-sp].

The full code for this stack is on [GitHub][gh-repo-stack].

[azure-iam]: https://azure.microsoft.com/en-us/services/active-directory/
[azure-users]: https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/directory-overview-user-model
[azure-groups]: https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/directory-overview-user-model
[azure-roles]: https://docs.microsoft.com/en-us/azure/role-based-access-control/rbac-and-directory-admin-roles?context=azure/active-directory/users-groups-roles/context/ugr-context
[azure-permissions]: https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/users-default-permissions?context=azure/active-directory/users-groups-roles/context/ugr-context
[azure-sp]: https://docs.microsoft.com/en-us/azure/active-directory/develop/app-objects-and-service-principals
[gh-repo-stack]: https://github.com/pulumi/kubernetes-the-prod-way/tree/crosswalk/azure/01-identity
{{% /md %}}
</div>

<div class="cloud-prologue-gcp"></div>
<div class="mt">
{{% md %}}

GCP exposes an [Identity Access and Management (IAM)][gcp-iam] API which can be used to grant
permissions to both human and bot users. Using this API, [IAM Members][gcp-iam] can be
slotted into end users, [IAM Groups][gcp-iam] (e.g., the `networkAdmins` IAM Group),
and GSuite accounts, and can then be allocated [IAM Roles][gcp-roles] with baseline permissions using [IAM Policies][gcp-policies].

GCP services can also be granted permissions temporarily, without the need for usernames and passwords, using [ServiceAccounts][gcp-sa].

The full code for this stack is on [GitHub][gh-repo-stack].

[gcp-iam]: https://cloud.google.com/iam/docs/overview
[gcp-policies]: https://cloud.google.com/iam/docs/reference/rest/v1/Policy
[gcp-roles]: https://cloud.google.com/iam/docs/understanding-roles
[gcp-members]: https://cloud.google.com/iam/docs/overview
[gcp-sa]: https://cloud.google.com/iam/docs/service-accounts
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

  * [Create an IAM Server Application and ServicePrincipal](#create-an-iam-server-application-and-serviceprincipal)
  * [Create an IAM Client Application and ServicePrincipal](#create-an-iam-server-application-and-serviceprincipal)
  * [Create an IAM Group for Developers](#create-an-iam-group-for-developers)

{{% /md %}}
</div>

<div class="cloud-prologue-gcp"></div>
<div class="mt">
{{% md %}}

## Overview

We'll review how to:

  * [Create an IAM Role and ServiceAccount for Admins](#create-an-iam-role-and-serviceaccount-for-admins)
  * [Create an IAM Role for Managing CloudSQL Databases](#create-an-iam-role-for-managing-cloudsql-databases)
  * [Create an IAM Role and ServiceAccount for Developers](#create-an-iam-role-and-serviceaccount-for-developers)

{{% /md %}}
</div>

<div class="cloud-prologue-aws"></div>
<div class="mt">
{{% md %}}

## Create an IAM Role for Admins

Create an admin role in AWS and attach EKS admin policies to the role.
This role will be mapped into the [`system:masters`][k8s-sys-masters] group in Kubernetes RBAC.

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

Azure AD integration with AKS requires that two Azure AD application objects be
created: a server component to provide authentication, and a client component
used by the CLI for authentication that works with the server component.

See the official [docs][azure-ad-aks] for more details.

## Create an IAM Server Application and ServicePrincipal

```typescript
import * as azuread from "@pulumi/azuread";

// Create the server application in Azure AD.
const applicationServer = new azuread.Application(`${name}-app-server`, {
    replyUrls: ["http://k8s_server"],
    type: "webapp/api",
    groupMembershipClaims: "All",
    requiredResourceAccesses: [
        // Windows Azure Active Directory API
        {
            resourceAppId: "00000002-0000-0000-c000-000000000000",
            resourceAccesses: [{
                // DELEGATED PERMISSIONS: "Sign in and read user profile"
                id: "311a71cc-e848-46a1-bdf8-97ff7156d8e6",
                type: "Scope",
            }],
        },
        // MicrosoftGraph API
        {
            resourceAppId: "00000003-0000-0000-c000-000000000000",
            resourceAccesses: [
                // APPLICATION PERMISSIONS: "Read directory data"
                {
                    id: "7ab1d382-f21e-4acd-a863-ba3e13f7da61",
                    type: "Role",
                },
                // DELEGATED PERMISSIONS: "Sign in and read user profile"
                {
                    id: "e1fe6dd8-ba31-4d61-89e7-88639da4683d",
                    type: "Scope",
                },
                // DELEGATED PERMISSIONS: "Read directory data"
                {
                    id: "06da0dbc-49e2-44d2-8312-53f166ab848a",
                    type: "Scope",
                },
            ],
        },
    ],
});

// Create the server application Service Principal.
const principalServer = new azuread.ServicePrincipal(`${name}-sp-server`, {
    applicationId: applicationServer.applicationId,
});

// Export outputs.
export const resourceGroupName = resourceGroup.name;
export const adServerAppId = applicationServer.applicationId;
export const adServerAppSecret = spPasswordServer.value;
```

## Create an IAM Client Application and ServicePrincipal

```typescript
import * as azuread from "@pulumi/azuread";

// Create the client application in Azure AD.
const applicationClient = new azuread.Application(`${name}-app-client`, {
    replyUrls: ["http://k8s_server"],
    type: "native",
    requiredResourceAccesses: [
        // Windows Azure Active Directory API
        {
            resourceAppId: "00000002-0000-0000-c000-000000000000",
            resourceAccesses: [{
                // DELEGATED PERMISSIONS: "Sign in and read user profile"
                id: "311a71cc-e848-46a1-bdf8-97ff7156d8e6",
                type: "Scope",
            }],
        },
        // AKS ad application server
        {
            resourceAppId: applicationServer.applicationId,
            resourceAccesses: [{
                // Server app Oauth2 permissions id
                id: applicationServer.oauth2Permissions[0].id,
                type: "Scope",
            }],
        },
    ],
});

// Create the client application Service Principal.
const principalClient = new azuread.ServicePrincipal(`${name}-sp-client`, {
    applicationId: applicationClient.applicationId,
});

// Export outputs.
export const adClientAppId = applicationClient.applicationId;
export const adClientAppSecret = spPasswordClient.value;
export const adGroupDevs = devs.name;
```

[azure-ad-aks]: https://docs.microsoft.com/en-us/azure/aks/azure-ad-integration
{{% /md %}}
</div>

<div class="cloud-prologue-gcp"></div>
<div class="mt">
{{% md %}}

## Create an IAM Role and ServiceAccount for Admins

Create an admin role in GCP and attach admin policies to the role.
This role will be bound to the admin service account.

```typescript
import * as gcp from "@pulumi/gcp";

// Create a new service account.
const infraCi = new gcp.serviceAccount.Account("infraCi", {
    project: config.project,
    accountId: "infra-ci",
    displayName: "Infrastructure CI account",
});

// Create a key from the service account.
const infraCiKey = util.createCiKey(`${infraCiId}Key`, infraCi);

// Export client secret to authenticate as this service account.
export const infraCiClientSecret = util.clientSecret(infraCiKey);

// Assign the service account GKE cluster admin privileges to add/delete clusters.
const infraCiClusterAdminRole = util.bindToRole(`${infraCiId}ClusterAdmin`, infraCi, {
    project: config.project,
    role: "roles/container.clusterAdmin",
});

// Helper to bind the service account to a given role.
export function bindToRole(
    name: string,
    sa: gcp.serviceAccount.Account,
    args: { project: pulumi.Input<string>; role: pulumi.Input<string> },
): gcp.projects.IAMBinding {
    return new gcp.projects.IAMBinding(name, {
        project: args.project,
        role: args.role,
        members: [sa.email.apply(email => `serviceAccount:${email}`)],
    });
}

// Helper to create new service account key.
export function createCiKey(name: string, sa: gcp.serviceAccount.Account): gcp.serviceAccount.Key {
    return new gcp.serviceAccount.Key(name, { serviceAccountId: sa.name });
}

// Helper to export service account for authentication use.
export function clientSecret(key: gcp.serviceAccount.Key): pulumi.Output<string> {
    return key.privateKey.apply(key => JSON.parse(Buffer.from(key, "base64").toString("ascii")));
}
```

Authenticate as the admin service account by exporting the key, and signing
into gcloud with it.

```bash
$ pulumi stack output infraCiClientSecret > infra-ci-client-secret.json
$ gcloud auth activate-service-account --key-file infra-ci-client-secret.json
```

## Create an IAM Role for Managing CloudSQL Databases

```typescript
import * as gcp from "@pulumi/gcp";

// (Optional): Assign the service account CloudSQL admin privileges to add/delete datastores.
const infraCiCloudSqlAdminRole = bindToRole(`${infraCiId}CloudSqlAdmin`, infraCi, {
    project: config.project,
    role: "roles/cloudsql.admin",
});
```

[k8s-sys-masters]: https://kubernetes.io/docs/reference/access-authn-authz/rbac#user-facing-roles
{{% /md %}}
</div>

<div class="cloud-prologue-aws"></div>
<div class="mt">
{{% md %}}

## Create an IAM Role for Developers

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

## Create an IAM Group for Developers

```typescript
import * as azuread from "@pulumi/azuread";

// Create the AD group for Developers.
const devs = new azuread.Group("devs", {
    name: "pulumi:devs",
});

// Export outputs.
export const adGroupDevs = devs.name;
```

{{% /md %}}
</div>

<div class="cloud-prologue-gcp"></div>
<div class="mt">
{{% md %}}

## Create an IAM Role and ServiceAccount for Developers

Create a developer role in GCP that will be mapped into a limited developer
role in Kubernetes RBAC.

```typescript
import * as gcp from "@pulumi/gcp";

// Create a new service account.
const k8sAppDevCi = new gcp.serviceAccount.Account(k8sAppDevCiId, {
    project: config.project,
    accountId: "k8s-app-dev-ci",
    displayName: "Infrastructure CI account",
});

// Assign the service account GKE cluster developer privileges to work with clusters.
const k8sAppDevRole = util.bindToRole(k8sAppDevCiId, k8sAppDevCi, {
    project: config.project,
    role: "roles/container.developer",
});

// Create a key from the service account.
const k8sAppDevCiKey = util.createCiKey(`${k8sAppDevCiId}Key`, k8sAppDevCi);

// Export client secret so that CI/CD systems can authenticate as this service account.
export const k8sAppDevCiClientSecret = util.clientSecret(k8sAppDevCiKey);
```

Authenticate as the dev service account by exporting the key, and signing
into gcloud with it.

```bash
$ pulumi stack output infraCiClientSecret > k8s-app-dev-ci-key.json
$ gcloud auth activate-service-account --key-file k8s-app-dev-ci-key.json
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
