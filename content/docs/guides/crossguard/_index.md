---
title: Policy as Code ("CrossGuard")
menu:
    userguides:
        identifier: crossguard
        weight: 4
---

{{% crossguard-preview %}}

CrossGuard is Pulumi's new Policy as Code offering. CrossGuard empowers you to set guardrails to enforce compliance for resources so developers within an organization can provision their own infrastructure while sticking to best practices and security compliance. Using Policy as Code, you can write flexible business or security policies.

Using CrossGuard, organization administrators can apply these rules to particular stacks within their organization. When policies are executed as part of your Pulumi deployments, any violation will gate or block that update from proceeding.

## Getting Started

To get started with Pulumi CrossGuard, [download and install Pulumi]({{< relref "/docs/get-started/install" >}}). Afterwards,
try the [Getting Started tutorial]({{< relref "/docs/get-started/crossguard" >}}).

## Pulumi CrossGuard policies for AWS (AWSGuard)

In addition to being able to implement your own CrossGuard policies, we've also created a set of policies that codifies best practices for AWS that you can adopt and use in a Policy Pack. AWSGuard is a configurable library that you can use to enforce best practices for your own Pulumi stacks or organization. [Learn more and get started with AWSGuard]({{< relref "./awsguard" >}}).

## Examples

If you're looking for some example Policy Packs, take a look at these:

* [AWS](https://github.com/pulumi/examples/tree/master/policy-packs/aws)
* [Azure](https://github.com/pulumi/examples/tree/master/policy-packs/azure)
* [GCP](https://github.com/pulumi/examples/tree/master/policy-packs/gcp)
* [Kubernetes](https://github.com/pulumi/examples/tree/master/policy-packs/kubernetes)

## FAQs

Get the answers to some [Frequently Asked Questions]({{< relref "./faq" >}}) about CrossGuard.
