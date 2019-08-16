---
title: Bootstrapping Identity
---

Begin by cloning the [Kubernetes the Prod Way repository][ktpw]. The `identity` stack is implemented
for each of [AWS][aws], [Azure][azure], and [GCP][gcp].

This stack is the root from which we will bootstrap the rest of our infrastructure. This tutorial
defines the following:

* A service accounts for managed infrastructure CI/CD.
* A service accounts for Kubernetes application CI/CD

In the rest of the tutorial we will look at the code example that defines the identity
infrastructure, and then we will use Pulumi to provision it.

## Modeling Identity Infrastructure with Code

Infrastructure-as-code tools such as Pulumi allow you to model your infrastructure with _code_ that
describes a _desired state_ for your infrastructure. An engine of some kind will _execute_ this code
to bring this desired state to reality.

Pulumi projects the API of cloud providers (_e.g._, AWS) into TypeScript classes. Pulumi also has a
pluggable language layer, and currently supports Python 3 and Go as well.

If we look inside [`gcp/identity/index.ts`][identity], we can see what it looks like to model the
identity stack. Consider the service account that drives CI/CD for the `infrastructure` stack.
Defining this essentially involves four things:

1. Defining a GCP service account using `new gcp.serviceAccount.Account`.
1. Granting GKE and Cloud SQL admin permissions to that service account by defining a
   `gcp.projects.IAMBinding` that binds those permissions (currently this happens via a utility
   function, `util.bindToRole`).
1. Creating and exporting a client secret that we can use to set up CI/CD. (More on this later.)

Currently, the code looks like this:

```typescript
const infraCi = new gcp.serviceAccount.Account(infraCiId, {
    project: config.project,
    accountId: "infra-ci",
    displayName: "Infrastructure CI account"
});

const infraCiClusterAdminRole = util.bindToRole(`${infraCiId}ClusterAdmin`, infraCi, {
    project: config.project,
    role: "roles/container.clusterAdmin"
});

const infraCiCloudSqlAdminRole = util.bindToRole(`${infraCiId}CloudSqlAdmin`, infraCi, {
    project: config.project,
    role: "roles/cloudsql.admin"
});

const infraCiKey = util.createCiKey(`${infraCiId}Key`, infraCi);

// Export client secret so that CI/CD systems can authenticate as this service account.
export const infraCiClientSecret = util.clientSecret(infraCiKey);
```

## Prerequisites: Bootstrapping Identity

Once defined, we can use Pulumi to provision the identity layer. In order to do this, we must:

1. Create an admin account in the relevant cloud provider (AWS, Azure, or GCP)
1. Use that admin account to provision the initial set of identities, so that CI/CD and teams can
   provision and manage infrastructure.

Before you begin, you'll need to do this and then log in through the CLI:

* For AWS, run `aws configure` (see [docs][aws-cli])
* For Azure, run `az login` (see [docs][az-cli])
* For GCP, run `gcloud auth` (see [docs][gcp-cli])


## Provisioning

Once you've logged in through the CLI, `cd` into the `identity` directory of the cloud provider
you've chosen and install the Pulumi toolchain:

```sh
yarn install
```

In the previous step, you should have configured default values for various cloud-specific variables
(_e.g._, default zone, project name, and so on). Assuming you've done that, we can now run:

```sh
pulumi stack init <a-stack-name>
pulumi up
```

This will provision the service accounts for CI/CD and the roles for teams (if necessary). You
should see something like the following. This output is for GCP, but something similar will happen
for Azure and AWS.

<img src="/images/docs/k8s-the-prod-way/identity.png">

## Stack Outputs: Identity Credentials

Pulumi makes it easy for other stacks to consume the credentials generated in this stack using
_stack outputs_. These are values that can be referenced from other stacks. For example, in the case
of GCP, if we run `pulumi stack output` we see that we export two values:

1. `infraCiClientSecret`, the authentication credential that will be used by the infrastructure CI
1. `k8sAppDevCiClientSecret`, the authentication credential that will be used by the Kubernetes
   application CI.

Likewise, if we run `pulumi stack output k8sAppDevCiClientSecret`, this will output the Kubernetes
application CI credential.

## Next Steps

In the next lab, we will see how to consume these stack outputs to provision app infrastructure.


[ktpw]: https://github.com/pulumi/kubernetes-the-prod-way/

[aws]: https://github.com/pulumi/kubernetes-the-prod-way/tree/master/aws/identity
[azure]: https://github.com/pulumi/kubernetes-the-prod-way/tree/master/azure/identity
[gcp]: https://github.com/pulumi/kubernetes-the-prod-way/tree/master/gcp/identity

[aws-cli]: {{< relref "/docs/intro/clouds-and-languages/aws/setup.md" >}}
[az-cli]: {{< relref "/docs/intro/clouds-and-languages/azure/setup.md" >}}
[gcp-cli]: {{< relref "/docs/intro/clouds-and-languages/gcp/setup.md" >}}

[identity]: https://github.com/pulumi/kubernetes-the-prod-way/blob/master/gcp/identity/index.ts
