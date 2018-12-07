---
title: Bootstrapping Identity
---

Begin by cloning the [Kubernetes the Prod Way repository][ktpw]. The `identity` stack is implemented
for each of [AWS][aws], [Azure][azure], and [GCP][gcp].

This stack is the root from which we will bootstrap the rest of our infrastructure. In this
tutorial, we will:

* Provision service accounts for CI/CD
* Provision roles for users and teams

## Prerequisites: Bootstrapping Identity

In order to provision identities:

1. Someone must create an admin account in the relevant cloud provider (AWS, Azure, or GCP)
1. That admin account must provision the initial set of identities, so that CI/CD and teams can
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

<img src="/images/k8s-the-prod-way/identity.png">

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

[aws-cli]: https://pulumi.io/quickstart/aws/setup.html
[az-cli]: https://pulumi.io/quickstart/azure/setup.html
[gcp-cli]: https://pulumi.io/quickstart/gcp/setup.html
