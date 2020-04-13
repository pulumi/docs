---
title: Policy as Code ("CrossGuard")
meta_desc: Pulumi's Policy as Code offering, CrossGuard, allows you to set guardrails for resources so
           best practices and security compliance are always followed.
menu:
    userguides:
        identifier: crossguard
        weight: 6
---

CrossGuard is Pulumi's new Policy as Code offering. CrossGuard empowers you to set guardrails to enforce compliance for resources so developers within an organization can provision their own infrastructure while sticking to best practices and security compliance. Using Policy as Code, you can write flexible business or security policies.

Using CrossGuard, organization administrators can apply these rules to particular stacks within their organization. When policies are executed as part of your Pulumi deployments, any violation will gate or block that update from proceeding.

## Languages

Policies can be written in TypeScript/JavaScript (Node.js) or Python and can be applied to Pulumi stacks written in any language.

|                                                        | Language                                                                | Status                                                            |
| ------------------------------------------------------ | ----------------------------------------------------------------------- | ----------------------------------------------------------------- |
| <img src="/logos/tech/logo-ts.png" class="h-10" />     | [TypeScript]({{< relref "/docs/reference/pkg/nodejs/pulumi/policy" >}}) | Stable                                                            |
| <img src="/logos/tech/logo-js.png" class="h-10" />     | [JavaScript]({{< relref "/docs/reference/pkg/nodejs/pulumi/policy" >}}) | Stable                                                            |
| <img src="/logos/tech/logo-python.png" class="h-10" /> | [Python]({{< relref "/docs/reference/pkg/python/pulumi_policy" >}})     | Preview                                                           |
| <img src="/logos/tech/dotnet.png" class="h-10" />      | .NET                                                                    | [Coming Soon](https://github.com/pulumi/pulumi-policy/issues/229) |
| <img src="/logos/tech/logo-golang.png" class="h-10" /> | Go                                                                      | [Coming Soon](https://github.com/pulumi/pulumi-policy/issues/230) |

## Getting Started

To get started with Pulumi CrossGuard, [download and install Pulumi]({{< relref "/docs/get-started/install" >}}). Afterwards,
try the [Getting Started tutorial]({{< relref "/docs/get-started/crossguard" >}}).

## Pulumi CrossGuard policies for AWS (AWSGuard)

In addition to being able to implement your own CrossGuard policies, we've also created a set of policies that codifies best practices for AWS that you can adopt and use in a Policy Pack. AWSGuard is a configurable library that you can use to enforce best practices for your own Pulumi stacks or organization. [Learn more and get started with AWSGuard]({{< relref "./awsguard" >}}).

## Configuring Policy Packs

Using configurable Policy Packs, you can write flexible policies that can be re-used across your organization. By default, some fields like enforcement level, are configurable. You may also specify configurable variables alongside each policy. [Learn more about configurable Policy Packs]({{< relref "./configuration" >}}).

## Examples

If you're looking for some example Policy Packs, take a look at these:

{{< chooser language "typescript,python" >}}

{{% choosable language typescript %}}

* [AWS](https://github.com/pulumi/examples/tree/master/policy-packs/aws-ts)
* [Azure](https://github.com/pulumi/examples/tree/master/policy-packs/azure-ts)
* [Google Cloud](https://github.com/pulumi/examples/tree/master/policy-packs/gcp-ts)
* [Kubernetes](https://github.com/pulumi/examples/tree/master/policy-packs/kubernetes-ts)

{{% /choosable %}}
{{% choosable language python %}}

* [AWS](https://github.com/pulumi/examples/tree/master/policy-packs/aws-python)
* [Azure](https://github.com/pulumi/examples/tree/master/policy-packs/azure-python)
* [Google Cloud](https://github.com/pulumi/examples/tree/master/policy-packs/gcp-python)
* [Kubernetes](https://github.com/pulumi/examples/tree/master/policy-packs/kubernetes-python)

{{% /choosable %}}

{{< /chooser >}}

## FAQs

Get the answers to some [Frequently Asked Questions]({{< relref "./faq" >}}) about CrossGuard.
