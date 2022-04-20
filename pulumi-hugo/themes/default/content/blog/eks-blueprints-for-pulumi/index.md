---
title: "EKS Blueprints for Pulumi"
date: 2022-04-20T18:00:00Z
draft: false
meta_desc: "Announcing Amazon EKS Blueprints for Pulumi: patterns and best practices for Kubernetes deployments."
meta_image: meta.png
authors: ["isaac-harris", "david-flanagan"]
tags: ["aws", "eks", "kubernetes"]
---

With the launch of [Amazon Elastic Kubernetes Service (EKS)](https://aws.amazon.com/blogs/aws/amazon-eks-now-generally-available/) in 2017, it is now [easier than ever]({{< relref "/blog/easily-create-and-manage-aws-eks-kubernetes-clusters-with-pulumi" >}}) to build, secure, operate and maintain Kubernetes clusters in the cloud. Notably, EKS removed the need to manage and configure underlying compute resources and scaling for clusters. Further, [EKS Anywhere](https://aws.amazon.com/eks/eks-anywhere/) brings many benefits to hybrid and on-premises deployments.

These developments have proved to be a huge leap forward in productivity for teams that manage cloud infrastructure, enabling them to focus their efforts on deploying applications to meet the needs of customers and stakeholders.

<!--more-->

As companies have matured in their use of Kubernetes, the day 0 through day 2 activities surrounding deployments have started to look similar regardless of where the workload is running. What has emerged is something we call a Shared Services Platform (SSP) – an internal company service that allows application developers to self-service infrastructure environments. SSPs are highly useful for platform teams when they want to share common infrastructure patterns and standardize/automate the provisioning of resources for their development teams.  This allows the platform team to be more responsive to development team requests for new environments.

Common activities for teams managing SSPs include:

- Setting up and managing multiple environments like DEV, TEST, STAGE, and PROD
- Simplifying platform administration with addons
- Onboarding Internal Teams via [GitOps]({{< relref "/blog/improving-gitops-with-pulumi-operator" >}})

Pulumi makes all of these activities easy to automate with built-in secrets management, reusable components, support for end-to-end infrastructure testing, and centralized policy enforcement. We also see new opportunities for simplification in all these activities. We’re excited to be part of the [Amazon EKS Blueprints program](
https://aws.amazon.com/blogs/containers/bootstrapping-clusters-with-eks-blueprints) to help Pulumi users deliver their platforms and applications faster than ever.

With today’s launch, we’re announcing a preview of a few of these scenarios that highlight the power of multi-language components that work across JavaScript/TypeScript, Python, .NET, and Golang in Pulumi. The goal is to get community feedback on these concepts and build more valuable components that meet the production needs of our users.

Here are some examples of how to simplify Kubernetes deployments using EKS Blueprint patterns built as Pulumi multi-language components:

## Setting up and managing multiple environments

Pulumi has a concept called [Stacks]({{< relref "/docs/intro/concepts/stack" >}}) that allows you to deploy the same Pulumi program multiple times, with minor variations to account for environmental differences. Leveraging this with our new Pulumi SSP SDK, you can deploy a cluster to multiple environments with very little code.
Here’s an example with one of Pulumi’s supported languages, Python.

```python
from pulumi_ssp import SharedServicesPlatform, ClusterArgsArgs

ssp = SharedServicesPlatform("python-platform", cluster_args=ClusterArgsArgs(kubernetes_version="1.21.0", region="us-east-1"))
```

That’s it! With a single line of code, you can deploy an EKS cluster in your region of choice and the version of Kubernetes you want. You’ll get the default EKS node group with this configuration, but what if you want more control? Let’s take a look at that with another supported language, TypeScript.

```typescript
import * as ssp from "@pulumi/ssp";

const sharedServicesPlatform = new ssp.SharedServicesPlatform("my-platform", {
  clusterArgs: {
    kubernetesVersion: "1.21.0",
    region: "us-east-1",
  },
});

sharedServicesPlatform.addManagedNodeGroup({
  name: "my-managed-group",
  desiredSize: 1,
  minSize: 1,
  kubernetesVersion: "1.21.0",
  maxSize: 2,
  instanceTypes: ["t3.medium"],
});
```

Our multi-language SDK provides some convenience functions that allow you to add NodeGroups and ManagedNodeGroups with just a few lines of configuration.

## Simplifying Platform Administration with Addons

Of course, a Kubernetes cluster with nothing on it isn’t going to give you the platform your organization needs to onboard teams and provide the level of redundancy and resiliency you need. So how can you add common Kubernetes deployments to handle observability, monitoring, and other “day 1 + day 2” tasks? Addons.

Our Pulumi SSP also provides a `clusterAddon` convenience function that allows you to deploy things with a single line.

A must-have for all Kubernetes clusters is the metrics-server and node-problem-detector, so let's add these. We’ll stick with TypeScript for this one.

```typescript
sharedServicesPlatform.clusterAddon({
  name: "metrics-server",
});

sharedServicesPlatform.clusterAddon({
  name: "node-problem-detector",
  version: "0.8.10"
});
```

Of course, you can easily leverage Pulumi’s integration with a variety of observability tools like [Datadog]({{< relref "/registry/packages/datadog" >}}) and [SumoLogic]({{< relref "/registry/packages/sumologic" >}}) as well.  We will be building more addons over the next few iterations, and we encourage you to reach out on our [Community Slack](https://slack.pulumi.com) and let us know what you’d like to see.

## Onboarding an Internal Team via GitOps

Lastly, Pulumi SSP allows platform teams to onboard teams to the platform, also with a convenience function call.

This time we’ll go wild and show what this looks like with CSharp.

```csharp
var ssp = new SharedServicesPlatform("csharp", new SharedServicesPlatformArgs
    {
      ClusterArgs = new Pulumi.Ssp.Inputs.ClusterArgsArgs
      {
        KubernetesVersion = "1.21.0",
        Region = "us-east-1",
      }
    });

    ssp.OnboardTeam(new SharedServicesPlatformOnboardTeamArgs
    {
      Name = "payments",
      Controller = "pulumi",
      Repository = "github.com/awesome-org/payments-team/infra"
    });
```

Onboarding a team to the platform is a wrapper for creating a namespace. Soon, this will add resource quotas and a GitOps delivery pipeline. We'll initially support ArgoCD and the Pulumi Operator, but support for FluxCD will be added shortly after.

## Conclusion

The EKS Blueprints program is helping to simplify the process of managing a shared services platform on Kubernetes by defining standard patterns that every engineering team will find useful.  We’d love to get your feedback on this approach and areas where you want to see more high-level components that simplify everyday infrastructure tasks. Check out these code examples and give us your feedback in our [EKS Blueprints repo](https://github.com/pulumi/eks-blueprint).
