---
title_tag: Kubernetes Identity & Access Management | Crosswalk
title: Kubernetes Identity & Access Management
meta_desc: An overview of cloud identity and access management providers when using Kubernetes.
no_on_this_page: true
linktitle: Identity
---

{{< chooser cloud "aws,azure,gcp" / >}}

{{% choosable cloud aws %}}

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

<!-- markdownlint-disable url -->
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
[gh-repo-stack]: https://github.com/pulumi/kubernetes-guides/tree/master/aws/01-identity
<!-- markdownlint-enable url -->

{{% /choosable %}}

{{% choosable cloud azure %}}

Azure exposes an [Active Directory][azure-iam] API which can be used to grant
permissions to both human and bot users. Using this API, [IAM User][azure-users] accounts can be
slotted into [IAM Groups][azure-groups] (e.g., the `networkAdmins` IAM Group), which can then be
allocated baseline permissions using [IAM Permissions][azure-permissions].

Azure services can also be granted permissions temporarily, without the need for usernames and passwords, using [Applications and ServicePrincipals][azure-sp].

The full code for this stack is on [GitHub][gh-repo-stack].

<!-- markdownlint-disable url -->
[azure-iam]: https://azure.microsoft.com/en-us/services/active-directory/
[azure-users]: https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/directory-overview-user-model
[azure-groups]: https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/directory-overview-user-model
[azure-roles]: https://docs.microsoft.com/en-us/azure/role-based-access-control/rbac-and-directory-admin-roles?context=azure/active-directory/users-groups-roles/context/ugr-context
[azure-permissions]: https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/users-default-permissions?context=azure/active-directory/users-groups-roles/context/ugr-context
[azure-sp]: https://docs.microsoft.com/en-us/azure/active-directory/develop/app-objects-and-service-principals
[gh-repo-stack]: https://github.com/pulumi/kubernetes-guides/tree/master/azure/01-identity
<!-- markdownlint-enable url -->

{{% /choosable %}}

{{% choosable cloud gcp %}}

GCP exposes an [Identity Access and Management (IAM)][gcp-iam] API which can be used to grant
permissions to both human and bot users. Using this API, [IAM Members][gcp-iam] can be
slotted into end users, [IAM Groups][gcp-iam] (e.g., the `networkAdmins` IAM Group),
and GSuite accounts, and can then be allocated [IAM Roles][gcp-roles] with baseline permissions using [IAM Policies][gcp-policies].

GCP services can also be granted permissions temporarily, without the need for usernames and passwords, using [ServiceAccounts][gcp-sa].

The full code for this stack is on [GitHub][gh-repo-stack].

<!-- markdownlint-disable url -->
[gcp-iam]: https://cloud.google.com/iam/docs/overview
[gcp-policies]: https://cloud.google.com/iam/docs/reference/rest/v1/Policy
[gcp-roles]: https://cloud.google.com/iam/docs/understanding-roles
[gcp-members]: https://cloud.google.com/iam/docs/overview
[gcp-sa]: https://cloud.google.com/iam/docs/service-accounts
[gh-repo-stack]: https://github.com/pulumi/kubernetes-guides/tree/master/gcp/01-identity
<!-- markdownlint-enable url -->

{{% /choosable %}}

{{% choosable cloud aws %}}

## Overview

We'll review how to:

- [Create an IAM Role for Admins](#create-an-iam-role-for-admins)
- [Create an IAM Role for Developers](#create-an-iam-role-for-developers)
- [Create IAM Roles for EKS Node Groups](#create-iam-roles-for-eks-node-groups)

{{% /choosable %}}

{{% choosable cloud azure %}}

## Overview

We'll review how to:

- [Create an IAM Server Application and ServicePrincipal](#create-an-iam-server-application-and-serviceprincipal)
- [Create an IAM Client Application and ServicePrincipal](#create-an-iam-server-application-and-serviceprincipal)
- [Create an IAM Group for Developers](#create-an-iam-group-for-developers)

{{% /choosable %}}

{{% choosable cloud gcp %}}

## Overview

We'll review how to:

- [Create an IAM Role and ServiceAccount for Admins](#create-an-iam-role-and-serviceaccount-for-admins)
- [Create an IAM Role for Managing CloudSQL Databases](#create-an-iam-role-for-managing-cloudsql-databases)
- [Create an IAM Role and ServiceAccount for Developers](#create-an-iam-role-and-serviceaccount-for-developers)

{{% /choosable %}}

{{% choosable cloud aws %}}

## Create an IAM Role for Admins

Create an admin role in AWS that assumes the AWS account caller, and attach EKS admin policies to the role.
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

Authenticate as the admin role.

```bash
$ aws sts assume-role --role-arn `pulumi stack output adminsIamRoleArn` --role-session-name k8s-admin
```

[k8s-sys-masters]: https://kubernetes.io/docs/reference/access-authn-authz/rbac#user-facing-roles

{{% /choosable %}}

{{% choosable cloud azure %}}

Azure AD integration with AKS requires that two Azure AD application objects be
created: a server component to provide authentication, and a client component
used by the CLI for authentication that works with the server component. We
will create both in the sections below.

> Note: The Server and Client Application registrations will be created with the desired accesses, but an administrator
**will need** to grant the Server Application consent before they can be used in proceeding stacks.

See the official [docs][azure-ad-aks] for more details.

### Prerequisites

To facilitate working with Azure, it is recommended that you create a new
ServicePrincipal with the proper permissions needed to create all of the
resources in each stack.

```bash
$ az ad sp create-for-rbac --name MyServicePrincipal
$ az login --service-principal --username $ARM_CLIENT_ID --password $ARM_CLIENT_SECRET --tenant $ARM_TENANT_ID
```

Ensure the ServicePrincipal has the following permissions for the legacy, and current Graph APIs:

#### **Azure Active Directory Graph (Legacy)**

| Permission Name  | Type |
|---|---|
|Application.ReadWrite.All | Application |
|Directory.ReadWrite.All | Application  |
|Group.ReadWrite.All | Delegated  |
|User.Read.All  | Delegated  |

#### **Microsoft Graph**

| Permission Name  | Type |
|---|---|
|Application.ReadWrite.All | Application |
|Directory.ReadWrite.All | Application  |
|Group.ReadWrite.All | Delegated  |
|User.Read  | Delegated  |

## Create an IAM Server Application and ServicePrincipal

Create an Azure server Application and ServicePrincipal, and attach it AD
permissions.

> Note: The Application registration will be created with the desired accesses, but an administrator
**will need** to grant consent before they can be used in proceeding stacks.

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
export const adServerAppId = applicationServer.applicationId;
```

## Create an IAM Client Application and ServicePrincipal

Create an Azure client Application and ServicePrincipal, and attach it AD
permissions.

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
```

[azure-ad-aks]: https://docs.microsoft.com/en-us/azure/aks/azure-ad-integration

{{% /choosable %}}

{{% choosable cloud gcp %}}

See the official [docs][gke-rbac] for more details.

[gke-rbac]: https://cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control

### Prerequisites

To facilitate working with GCP, it is recommended that you create a new
ServiceAccount with the proper permissions needed to create all of the
resources in each stack. We'll set this ServiceAccount to be bound to [GCP roles][gcp-roles]
the with permissions of `role/editor` and `roles/container.clusterAdmin`.

Create the ServiceAccount and its secret key to use for auth. Then bind it to
the `roles/editor` role, and authenticate as the ServiceAccount to use with the stacks.

```bash
$ gcloud iam service-accounts create my-service-account --description MyServiceAccount --display-name MyServiceAccount
$ gcloud iam service-accounts keys create ~/key.json --iam-account my-service-account@pulumi-development.iam.gserviceaccount.com
$ gcloud projects add-iam-policy-binding pulumi-development --member serviceAccount:my-service-account@pulumi-development.iam.gserviceaccount.com --role roles/editor
$ gcloud projects add-iam-policy-binding pulumi-development --member serviceAccount:my-service-account@pulumi-development.iam.gserviceaccount.com --role roles/container.clusterAdmin
$ gcloud auth activate-service-account --key-file ~/key.json
```

[gcp-roles]: https://cloud.google.com/iam/docs/understanding-roles

## Create an IAM Role and ServiceAccount for Admins

Create an admin role in GCP and attach admin policies to the role.
This role will be bound to the admin service account.

```typescript
import * as gcp from "@pulumi/gcp";

// Create the GKE cluster admins ServiceAccount.
const adminsName = "admins";
const adminsIamServiceAccount = new gcp.serviceAccount.Account(adminsName, {
    project: config.project,
    accountId: `k8s-${adminsName}`,
    displayName: "Kubernetes Admins",
});

// Bind the admin ServiceAccount to be a GKE cluster admin.
util.bindToRole(`${adminsName}-k8s`, adminsIamServiceAccount, {
    project: config.project,
    roles: ["roles/container.clusterAdmin", "roles/container.developer"],
});

// Bind the admin ServiceAccount to be a CloudSQL admin.
util.bindToRole(`${adminsName}-cloudsql`, adminsIamServiceAccount, {
    project: config.project,
    roles: ["roles/cloudsql.admin"],
});

// Export the admins ServiceAccount key.
const adminsIamServiceAccountKey = util.createServiceAccountKey(`${adminsName}Key`, adminsIamServiceAccount);

// Export the admins ServiceAccount client secret to authenticate as this service account.
export const adminsIamServiceAccountSecret = util.clientSecret(adminsIamServiceAccountKey);

// Helper to bind the service account to a given role.
export function bindToRole(
    name: string,
    sa: gcp.serviceAccount.Account,
    args: { project: pulumi.Input<string>; roles: string[]})
{
    args.roles.forEach((role, index) => {
        new gcp.projects.IAMBinding(`${name}-${index}`, {
            project: args.project,
            role: role,
            members: [sa.email.apply(email => `serviceAccount:${email}`)],
        });
    })
}

// Helper to create new service account key.
export function createServiceAccountKey(name: string, sa: gcp.serviceAccount.Account): gcp.serviceAccount.Key {
    return new gcp.serviceAccount.Key(name, { serviceAccountId: sa.name });
}

// Helper to export service account for authentication use.
export function clientSecret(key: gcp.serviceAccount.Key): pulumi.Output<any> {
    return key.privateKey.apply(key => JSON.parse(Buffer.from(key, "base64").toString("ascii")));
}
```

Authenticate as the admin ServiceAccount by exporting the key, and signing
into gcloud with it.

```bash
$ pulumi stack output adminsIamServiceAccountSecret > k8s-admin-sa-key.json
$ gcloud auth activate-service-account --key-file k8s-admin-sa-key.json
```

## Create an IAM Role for Managing CloudSQL Databases

```typescript
import * as gcp from "@pulumi/gcp";

// Bind the admin ServiceAccount to be a CloudSQL admin.
util.bindToRole(`${adminsName}CloudSqlAdmin`, adminsIamServiceAccount, {
    project: config.project,
    roles: ["roles/cloudsql.admin"],
});
```

[k8s-sys-masters]: https://kubernetes.io/docs/reference/access-authn-authz/rbac#user-facing-roles

{{% /choosable %}}

{{% choosable cloud aws %}}

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

Authenticate as the devs role.

```bash
$ aws sts assume-role --role-arn `pulumi stack output devsIamRoleArn` --role-session-name k8s-devs
```

{{% /choosable %}}

{{% choosable cloud azure %}}

## Create an IAM Group for Admins

Create an admins group in Azure. This group will be mapped into the `system:masters`group in Kubernetes RBAC.

```typescript
import * as azure from "@pulumi/azure";
import * as azuread from "@pulumi/azuread";

const clientConfig = azure.core.getClientConfig();
const currentPrincipal = clientConfig.objectId;

const admins = new azuread.Group("admins", {
    name: "pulumi:admins",
    members: [
        currentPrincipal,
    ],
});
```

## Create an IAM Group for Developers

Create a developer group in Azure. This group will be mapped into a limited
developer role in Kubernetes RBAC.

Add a new user in AD, or get an existing user to add to the new AD group.

> Note: On deletion of this Pulumi stack you **cannot** use the
> ServicePrincipal to delete the Group, as [ActiveDirectory][so-ad-no-apps] does not allow
> Application registrations to delete AD Groups. Instead, you must authenticate as a
> user, and ensure that the user has `admin` rights in AD to be able to
> delete the group.

[so-ad-no-apps]: https://stackoverflow.com/questions/46604721/azure-ad-delete-user-group-unauthorized

```typescript
import * as azuread from "@pulumi/azuread";

/* Create a new user in AD.
const dev = new azuread.User("k8s-dev", {
    userPrincipalName: "k8sdev@example.com",
    displayName: "Kubernetes Dev",
    password: "Qjker21!G",
});
*/

// Get an existing AD user.
const dev = azuread.getUser({
    userPrincipalName: "alice@example.com",
});

// Create the AD group for Developers.
const devs = new azuread.Group("devs", {
    displayName: "pulumi:devs",
    // Assign a new or existing user to the group.
    members: dev.then(d => [d.objectId]),
});

// Export outputs.
export const adGroupDevs = devs.displayName;
```

{{% /choosable %}}

{{% choosable cloud gcp %}}

## Create an IAM Role and ServiceAccount for Developers

Create a developer role in GCP that will be mapped into a limited developer
role in Kubernetes RBAC.

```typescript
import * as gcp from "@pulumi/gcp";

// Create the GKE cluster developers ServiceAccount.
const devsName = "devs";
const devsIamServiceAccount = new gcp.serviceAccount.Account(devsName, {
    project: config.project,
    accountId: `k8s-${devsName}`,
    displayName: "Kubernetes Developers",
});

// Bind the devs ServiceAccount to be a GKE cluster developer.
util.bindToRole(`${devsName}-k8s`, devsIamServiceAccount, {
    project: config.project,
    roles: ["roles/container.developer"],
});

// Export the devs ServiceAccount key.
const devsIamServiceAccountKey = util.createServiceAccountKey(`${devsName}Key`, devsIamServiceAccount);

// Export the devs ServiceAccount client secret to authenticate as this service account.
export const devsIamServiceAccountClientSecret = util.clientSecret(devsIamServiceAccountKey);
```

Authenticate as the dev ServiceAccount by exporting the key, and signing
into gcloud with it.

```bash
$ pulumi stack output devsIamServiceAccountSecret > k8s-devs-sa-key.json
$ gcloud auth activate-service-account --key-file k8s-devs-sa-key.json
```

{{% /choosable %}}

{{% choosable cloud aws %}}

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

{{% /choosable %}}
