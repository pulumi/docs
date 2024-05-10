---
title_tag: Integrate with Kubernetes | Pulumi ESC
title: Kubernetes
h1: "Pulumi ESC: Integrate with Kubernetes"
meta_desc: This page provides an overview on how to use Pulumi ESC with Kubernetes.
weight: 2
menu:
  pulumiesc:
    parent: esc-other-integrations
    identifier: esc-other-integrations-kubernetes
---

## Overview

Pulumi ESC integrates with [Kubernetes](https://kubernetes.io/) to help developers connect to Kubernetes
clusters using centrally-managed configurations and credentials. This works with Kubernetes tools
such as `kubectl` and `helm`, and with Pulumi programs that use the
[Kubernetes provider for Pulumi](/registry/packages/kubernetes/).

## Prerequisites

To complete the steps in this tutorial, you will need to install the following prerequisites:

- the [Pulumi ESC CLI](/docs/esc-cli/)
- a Kubernetes cluster
- [kubectl](https://kubernetes.io/releases/download/#kubectl)

## Manage Kubernetes Configuration Files

ESC integrates with Kubernetes client tools by setting the `KUBECONFIG` environment variable to point to a
generated [Kubernetes configuration file](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/).

The kubeconfig content is determined by the ESC environment definition, and may include
information from a variety of sources, including stack outputs.

### Generate a kubeconfig file

The following environment defines a kubeconfig file to connect to a local cluster:

```yaml
values:
  files:
    KUBECONFIG: |
      apiVersion: v1
      kind: Config
      clusters:
      - cluster:
          server: https://127.0.0.1:6443
        name: docker-desktop
```

The Kubernetes configuration is picked up automatically by the `kubectl` command:

```bash
$ esc run <your-environment-name> -- kubectl get namespaces
```

This command opens the environment you just created, renders the kubeconfig as a temporary file, sets
the `KUBECONFIG` environment variable to refer to the file, and then runs a `kubectl` command.

### Use stack outputs to generate a kubeconfig file

Instead of hardcoding a kubeconfig, you also have the option of using ESC providers to dynamically import
cluster information. The [`pulumi-stacks`](/docs/esc/providers/pulumi-stacks/) provider is especially useful here, if the Kubernetes cluster
was provisioned by a Pulumi program. Such programs often export the cluster's kubeconfig as a stack output.
Check out the [Getting Started](/docs/clouds/kubernetes/) guide if you need help setting up a Kubernetes cluster.

The following environment defines a kubeconfig file based on a stack output:

```yaml
values:
  stacks:
    fn::open::pulumi-stacks:
      stacks:
        eks-cluster:
          stack: eks-cluster/demo
  kubeconfig: {'fn::toJSON': "${stacks.eks-cluster.kubeconfig}"}
  files:
    KUBECONFIG: ${kubeconfig}
```

This definition loads a Pulumi stack named `eks-cluster/demo`, parses the `kubeconfig` output as a JSON object,
and then defines a file named `KUBECONFIG` with the object.

## Use the kubeconfig in a Pulumi program

To use the kubeconfig in a Pulumi program, use the `pulumiConfig` section of your environment file to directly
configure the Pulumi Kubernetes provider.

The following environment configures the `kubernetes:kubeconfig` setting on the Kubernetes provider.

```yaml
values:
  stacks:
    fn::open::pulumi-stacks:
      stacks:
        eks-cluster:
          stack: eks-cluster/demo
  kubeconfig: {'fn::toJSON': "${stacks.eks-cluster.kubeconfig}"}
  pulumiConfig:
    kubernetes:kubeconfig: ${kubeconfig}
```

In practice, your environment should define both a kubeconfig file and a provider configuration.

Next, you will need to import your environment file into your Pulumi project. To do this,
open your `Pulumi.<your-stack-name>.yaml` file and update it to import your environment as shown below,
making sure to replace the value of `<your-environment-name>` with the name of your own environment:

```yaml
environment:
  - <your-environment-name>
```

## Authenticate to a Kubernetes Cluster

ESC enables you to connect to your Kubernetes cluster using credentials obtained from an ESC provider. For example,
to connect using AWS credentials returned by the [aws-login](/docs/esc/providers/aws-login/) provider.

Kubernetes tools typically execute an external command to obtain user credentials
(see [documentation](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#client-go-credential-plugins)).
These commands rely on environment variables and/or configuration files, and we'll use Pulumi ESC to set
them up.

### Configure AWS credentials

Taking an EKS cluster as an example, your environment can produce temporary AWS credentials using the `aws-login` provider.

```yaml
values:
  aws:
    creds:
      fn::open::aws-login:
        oidc:
          duration: 1h
          roleArn: arn:aws:iam::0123456789:role/cluster-admin
          sessionName: <your-environment-name>
  environmentVariables:
    AWS_ACCESS_KEY_ID: ${aws.creds.keyId}
    AWS_SECRET_ACCESS_KEY: ${aws.creds.secretAccessKey}
    AWS_SESSION_TOKEN: ${aws.creds.sessionToken}
```

This definition sets the `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_SESSION_TOKEN` environment variables
that are understood by the `aws-iam-authenticator` exec plugin, as described [here](https://github.com/kubernetes-sigs/aws-iam-authenticator?tab=readme-ov-file#specifying-credentials--using-aws-profiles).
This assumes that the kubeconfig is configured appropriately to use the authenticator.

### Import another environment

A good practice is to compose an environment by importing other environment(s). Consider encapsulating your cloud
credentials in a separate environment file, and reference the environment as necessary.

The following environment imports an environment named `aws-access` to incorporate credentials, and then prepares
a kubeconfig for `kubectl` and for the Pulumi Kubernetes provider.

```yaml
imports:
  - aws-access
values:
  stacks:
    fn::open::pulumi-stacks:
      stacks:
        eks-cluster:
          stack: eks-cluster/demo
  kubeconfig: {'fn::toJSON': "${stacks.eks-cluster.kubeconfig}"}
  pulumiConfig:
    kubernetes:kubeconfig: ${kubeconfig}
  files:
    KUBECONFIG: ${kubeconfig}
```

When this environment is opened, expect to see a combination
of environment variables and files.

{{< get-started-stepper >}}
