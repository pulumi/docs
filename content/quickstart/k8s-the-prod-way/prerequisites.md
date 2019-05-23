---
title: Prerequisites
---

This tutorial leverages [Pulumi][pulumi] and [Node.js][nodejs] to provision and configure
infrastructure on AWS, Azure, or GCP. Pulumi is a platform for building and deploying cloud
infrastructure and applications in your favorite language on any cloud. This particular tutorial is
written in [TypeScript][ts], a strict superset of JavaScript that allows users to add optional type
hints to variables. (Pulumi also supports Python and nothing in principle prevents using that
instead.)

## Pulumi CLI

To begin, you should [install the Pulumi CLI][pulumi-cli]. By default, the Pulumi CLI uses the
Pulumi service to coordinate concurrent updates, so you should also [create an account][pulumi].

It is possible to avoid a dependency on the service by using the [local backend][local-backend].
But, for the purposes of this tutorial, it is much more convenient to use the service, and the
entire tutorial can be completed using only the free tier.

## Yarn CLI

If this is your first time writing a Node.js application, you'll need to install either Yarn or npm,
which are package managers for Node.js applications. You can install it by following [the official
instructions][yarn].

## Cloud Provider CLI

This tutorial provides code samples for AWS, Azure and GCP. You will need to create an account for
one of those providers, and then install the official CLI. For details, consult our installation
guides:

* [AWS][aws-setup]
* [Azure][azure-setup]
* [GCP][gcp-setup]

## `kubectl`, the Kubernetes CLI

Pulumi will help to provision cloud resources, including those running on Kubernetes. To interact
with the cluster, it will be useful to install `kubectl`, the official Kubernetes CLI. See official
instructions [here][kubectl].


[pulumi]: https://www.pulumi.com/
[nodejs]: https://nodejs.org/en/
[pulumi-cli]: https://pulumi.io/quickstart/install.html
[local-backend]: https://pulumi.io/reference/state.html
[ts]: https://www.typescriptlang.org/
[yarn]: https://yarnpkg.com/en/docs/install

[aws-setup]: https://pulumi.io/quickstart/aws/setup.html
[azure-setup]: https://pulumi.io/quickstart/azure/setup.html
[gcp-setup]: https://pulumi.io/quickstart/gcp/setup.html

[kubectl]: https://kubernetes.io/docs/tasks/tools/install-kubectl/
