---
title: CrossGuard

menu:
    userguides:
        parent: guides
        identifier: crossguard
---

{{% crossguard-preview %}}

CrossGuard is Pulumi's new Policy as Code offering. CrossGuard allows you to empower your developers to provision their own infrastructure while providing them with guardrails. Using Policy as Code, you can write flexible business or security policies.

Using CrossGuard, organization administrators can apply these rules to particular stacks within their organization. When policies are executed as part of your Pulumi deployments, any violation will gate or block that update from proceeding.

## Getting Started

To get started with Pulumi CrossGuard, [download and install Pulumi]({{< relref "/docs/get-started/install" >}}). Afterwards,
try the [Getting Started tutorial]({{< relref "/docs/get-started/policy-as-code" >}}).

## Examples

If you're looking for some example Policy Packs, take a look at these:

* [AWS](https://github.com/pulumi/examples/tree/master/policy-packs/aws)
* [Azure](https://github.com/pulumi/examples/tree/master/policy-packs/azure)
* [GCP](https://github.com/pulumi/examples/tree/master/policy-packs/gcp)
* [Kubernetes](https://github.com/pulumi/examples/tree/master/policy-packs/kubernetes)
