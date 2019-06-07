---
title: Provisioning Shared, Managed Infrastructure
aliases: ["infrastructure.html"]
---

This lab assumes you have successfully completed [lab 1]({{< relref "identity.md" >}}), the results of which are
to have successfully bootstrapped the identity platform for CI/CD and teams.

In this tutorial, we will use this identity to:

* Create a shared, managed Kubernetes cluster

Inside the [Kubernetes the Prod Way repository][ktpw], the `infrastructure` stack is implemented for
each of [AWS][aws], [Azure][azure], and [GCP][gcp].

## Modeling Shared, Managed Infrastructure with Code

When we provisioned the identity stack, we saw a basic example of using the Pulumi TypeScript SDK to
provision the identity stack on top of GCP.

This example uses the same SDK to define a set of shared, managed infrastructure (_e.g._, for
compute, networking, and storage). Typically this would be managed through a GCP service account
running with the role permissions defined in the identity stack; we'll hook this up later.

For now, looking inside [`gcp/infrastructure/index.ts`][infra], we can see how in our GCP
infrastructure stack, we define the GKE cluster we will deploy applications on:

```typescript
const cluster = new gcp.container.Cluster(name, {
    project: config.project,
    zone: config.zone,
    initialNodeCount: config.nodeCount || defaultClusterOptions.nodeCount,
    nodeVersion: defaultClusterOptions.nodeVersion,
    minMasterVersion: defaultClusterOptions.minMasterVersion,
    masterAuth: {
        username: defaultClusterOptions.masterUsername,
        password: defaultClusterOptions.masterPassword
    },
    network: network.name,
    subnetwork: subnet.name,
    nodeConfig: {
        machineType: config.nodeMachineType || defaultClusterOptions.nodeMachineType,
        oauthScopes: [
            "https://www.googleapis.com/auth/compute",
            "https://www.googleapis.com/auth/devstorage.read_only",
            "https://www.googleapis.com/auth/logging.write",
            "https://www.googleapis.com/auth/monitoring"
        ]
    }
});

export const kubeconfig = createKubeconfig(cluster);
```

The GKE cluster is defined using a GCP `Network` and a `Subnet` -- we've elided those for
simplicity.

But, we can also see that we're exporting the YAML text of a `kubeconfig` file, which will be used
by the application stack to authenticate against the cluster. We will see how this works later.

## Prerequisites: Logging into cloud provider with CLI

In the first lab, we need to set up credentials using the CLI, so that Pulumi can authenticate
against the cloud provider of your choice. Make sure you're still logged in before continuing.

## Provisioning

Begin by `cd`'ing into the `infrastructure` directory of the cloud provider of your choice. From
there, install the Pulumi toolchain:

```sh
yarn install
```

The infrastructure stack comes with a script that will allow you to authenticate using the CI/CD
service account we defined in lab 1. We will use this to provision this cluster -- later we will use
this in CI/CD.

Assuming you have successfully finished lab 1, you'll need to specify the name of the identity stack
you've created. This was the argument you passed to `pulumi stack init`.

```sh
./scripts/login-to-ci-service-account.sh <identity-stack-name>
```

This script obtains the client secret from the identity stack, and then uses `gcloud` to
authenticate with it.

```sh
pulumi stack output infraCiClientSecret -s "$1" > infra-ci-client-secret.json
gcloud auth activate-service-account --key-file infra-ci-client-secret.json
rm infra-ci-client-secret.json
```

From here, we can provision the infrastructure stack. We need to specify the name of the identity
stack so that this stack can configure itself to use the same project, zone, _etc_., as the identity
stack.

```sh
pulumi stack init
pulumi config set identityStackName <identity-stack-name>
pulumi up
```

On success, this should look something like the following. This example is for GCP, but similar
output will be displayed for AWS and Azure.

<img src="/images/k8s-the-prod-way/infrastructure.png">

## Stack Outputs: Kubernetes Credentials

Much like lab 1, this stack produces output values that can be referenced in other stacks. If we run
`pulumi stack output`, we see one export value:

* `kubeconfig`, the kubeconfig file the app stack will use to authenticate against the Kubernetes
  cluster we just provisioned.

## Next Steps

In the next lab, we will see how to provision a Kubernetes application using the credentials
generated here and in lab 1.


[ktpw]: https://github.com/pulumi/kubernetes-the-prod-way/

[aws]: https://github.com/pulumi/kubernetes-the-prod-way/tree/master/aws/infrastructure
[azure]: https://github.com/pulumi/kubernetes-the-prod-way/tree/master/azure/infrastructure
[gcp]: https://github.com/pulumi/kubernetes-the-prod-way/tree/master/gcp/infrastructure


[infra]: https://github.com/pulumi/kubernetes-the-prod-way/blob/master/gcp/infrastructure/index.ts
