---
title: "Benefits of Policy as Code"
date: 2020-05-27
meta_desc: "An organization can benefit from Policy as Code through cost control, compliance, and best practices."
meta_image: pac-benefits.png
authors:
    - sophia-parafina
tags:
    - policy-as-code
---

Writing policies in a high-level programming language can automate the process. When policies are written with code, you can apply software development practices such as testing, automated deployment, and version control. Cloud providers typically offer a GUI to create policies,  but creating policies is not easily repeatable, nor can you version policies. Moreover, policies must be tested against a live system, which means using an existing system or configuring and deploying an ephemeral version.

While the benefits of writing policies as code are evident for developers and operators, the organizational benefits are even more significant. Organizations can realize cost savings, improved compliance, efficient deployments, fine-grained control over infrastructure, and better use of cloud provider native resources. Let’s take a look at these benefits in-depth.

<!--more-->

## Controlling Costs

A sizeable monthly cloud bill due to unused resources left running or using over-sized instances for small tasks is an industry cliché. One way to control costs is to set policies based on pricing. With pricing data online, we can calculate the cost of a resource ahead of time and create a policy that limits the amount spent to deploy it. In a [previous article]({{< relref "/blog/manage-infrastructure-with-pac#controlling-cost-on-aws" >}})), we provided an example policy that finds all the resources in a deployment and calculates the total monthly cost. The policy sets the monthly cost permitted and sends a warning if the deployment exceeds it.

But what about unused or abandoned resources? We can use a cloud provider’s resources to implement a watchdog function with a policy that cleans up unused resources. In this [article]({{< relref "/blog/controlling-aws-costs-with-lambda-and-pulumi" >}}), we show how to use a serverless function to find unused resources daily and shut them down. We implemented this system at Pulumi and [reduced our operating costs by 64%]({{< relref "/blog/controlling-aws-costs-with-lambda-and-pulumi#in-conclusion" >}}).

## Compliance

Policy as Code is a way to enforce infrastructure policies that prevent inadvertent access to resources such as databases and storage or to enforce cost policies.

We can use cloud provider native tools and practices in combination with policy to control costs. Using AWS as an example, [Joe Duffy](https://twitter.com/funcofjoe) wrote an article on using tags for cost tracking, automation, and organization. If you are not familiar with tags, they are a simple key/value pair applied to a resource. Tags let you manage, search, and filter resources.

The [article]({{< relref "/blog/automatically-enforcing-aws-resource-tagging-policies" >}}) showed how you could use your favorite programming language to tag a resource to enable cost tracking by project, stack, and cost center. Joe then demonstrated how to use policy as code to [enforce tagging of resources]({{< relref "/automatically-enforcing-aws-resource-tagging-policies#defining-our-tags-enforcer-policy" >}}) when they are created.  The article also shows how to [automatically tag resources]({{< relref "/blog/automatically-enforcing-aws-resource-tagging-policies#automatically-applying-tags" >}}) and enables resources to pass the tagging policy.

## Validate Before or During Deployment

One of the shortcomings of using a cloud provider GUI to create policies is that they can only be tested on deployed resources. One solution is to implement an [ephemeral environment](https://about.gitlab.com/blog/2020/01/27/kubecon-na-2019-are-you-about-to-break-prod/) for testing, but this incurs resource costs as wells as time spent deploying. A feature of Pulumi’s deployment engine is that it constructs a preview of the resource graph. When it creates the preview, it also tests if resources are compliant with the included policies. The policies are run before a resource is registered, and inputs (configuration parameters) are validated. Out-of-compliance resources are blocked from being created or modified by the policy.

There are cases where it is necessary to deploy a resource to test policy; for example, a resource property is required to provision another resource. For these instances, the Pulumi engine supports testing either the entire stack or selected resources. This is analogous to integration testing vs. unit testing. You can [run policies against a stack]({{< relref "/blog/enforcing-different-kinds-of-policies-for-cloud-resources#stack-validation" >}}) as a whole, i.e., when all resources are registered and do not block out of compliance resources from being created.

In either case, your infrastructure is validated before it’s deployed, saving both time and money.

## Best Practices as Policies

All cloud providers offer a set of best practices for deploying resources. Best practices can be implemented as policies, but instead of managing them as individual policies, wouldn’t it be more efficient to organized similar policies as a bundle? This is the idea behind [Policy Packs]({{< relref "/docs/guides/crossguard/core-concepts#policy-pack" >}}). They provide a way to group similar policies based on how you manage your infrastructure. For example, you may have several policies for storage based on how they are tagged. Policy packs don’t restrict which policies you combine; you can have Kubernetes policies bundled with container registry policies. You create Policy Packs according to the requirements and needs of your organization.

You can apply a Policy Pack to a single stack of resources or across multiple stacks. A group of stacks that use the same Policy Pack is a [Policy Group]({{< relref "/docs/guides/crossguard/core-concepts#policy-group" >}}). Note that a stack can belong to multiple Policy Groups. A typical application of Policy Groups is to set policies for environments; for example, you might have a more permissive Policy Group for your development and staging environments and more restrictive one for production.

Policy as code enables you to deploy best practices as policies. Moreover, you can organize policies in bundles or Policy Packs based on your organizational requirements. This provides repeatable and fine-grained control over the resources you deploy. You can apply Policy Packs on individual resource stacks or across multiple stacks as Policy Groups, giving you granular control over how and which resources are deployed.

## Working with Cloud Native Resources

Cloud providers have methods for managing access to resources such as IAM (Identity Access and Management) policies and ACL (Access Control Lists). This is one type of policy, but it doesn’t cover the full range of actions available for managing your infrastructure. Pulumi uses cloud provider APIs to build and maintain infrastructure. The Pulumi engine works with cloud provider resources in conjunction with Policy as Code.

In a [previous]({{< relref "/blog/aws-iam-access-analyzer-and-crossguard" >}}) article, we demonstrated how to use the IAM Access Analyzer in conjunction with Policy as Code.  IAM Access Analyzer validates all resources per-region with a single analyzer. It creates a record for each problem identified and shows which policy is responsible for granting wider access to resources than would be best practice. Policy as Code applies policy packs to stacks of resources anytime infrastructure is deployed.

The IAM Access Analyzer works on deployed resources, so in the example, we have to deploy the infrastructure first before running the analyzer using a Pulumi program. When the scan of a resource is complete, it returns the detailed results that we can pass to the policy for validation. In this way, we can use cloud provider native tools in conjunction with Policy as Code to manage and protect our infrastructure.

## Conclusion

We often talk about Policy as Code in terms of repeatability, versioning, and testing, which benefits developers and operators directly. The benefits extend beyond DevOps and into the success of an organization. Policy as Code provides the following organizational benefits:

- means for automated cost control,
- compliance to avoid downtime by securing resources,
- validating infrastructure before creating resources (another cost-saving measure),
- encoding best practices for resource stacks,
- and working with cloud provider native resources to provide best of breed security and granular control.

Learn more about using programming languages for [Policy as Code with our docs]({{< relref "/docs/guides/crossguard" >}}).
