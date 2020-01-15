---
title: "Towards Pulumi 2.0"
date: 2020-01-16
meta_desc: "This provides an overview of features for the Pulumi 2.0 release"
meta_image: meta.png
authors:
 - sophia-parafina
tags:
 - Pulumi
 - workflow portability
 - Terraform
 - policy as code
---

After releasing Pulumi 1.0, we previewed new features that make deploying infrastructure and modern applications faster, easier, and more secure. As Pulumi 2.0 approaches General Availability, we’re taking all those features and focusing on three themes: workflow portability, policy as code, and developer experience.

Why these three? Workflow portability is core to Pulumi, as we like to say, “Create, deploy and manage infrastructure, on any cloud, in any language.” Deploying and managing your infrastructure go hand-in-hand. That’s why we released Policy as Code or PaC. You can manage resources, security, compliance, and costs with PaC. Finally, Pulumi provides tools to improve the developer experience for both developers and operators. These tools can shorten the development cycle allowing for experimentation and provide observability during tests. Pulumi brings modern software development practices to infrastructure deployments.

<!--more-->

## Workflow Portability

The first area is workflow portability. In a [Screaming in the Cloud](https://www.lastweekinaws.com/podcast/screaming-in-the-cloud/episode-67-infrastructure-as-code-with-terraform-and-mitchell-hashimoto/) interview, [Mitchel Hashimoto](https://twitter.com/mitchellh) of Hashicorp defines workflow portability as:

> “What is more important to me is workflow portability, which is sort of the process by which you get infrastructure, deploy applications, secure them, network them.”

Pulumi enables workflow portability by providing SDKs for AWS, Azure, and GCP. However, many organizations have existing resources or configuration code in Terraform’s HCL language that they would like to reuse. Using [`tf2pulumi`](https://github.com/pulumi/tf2pulumi), you can convert HCL into Pulumi stacks that are ready for deployment. We can take reuse one step further and import existing resources by finding the resource id from either the Terraform state file or the could provider’s console. The example below show how to import an existing Azure `ResourceGroup`.

```ts
const mainResourceGroup = new azure.core.ResourceGroup("main", {
 location: "West US 2",
 name: `${prefix}-resources`,
}, { import: "/subscriptions/0282681f-7a9e-424b-80b2-96babd57a8a1/resourceGroups/tfvmex-resources" });
```

You can watch the full life cycle of resource reuse in this video.

{{< youtube kX_3Wdft0Ms >}}

## Policy as Code

Policies are the guardrails of infrastructure. They control access, set limits, and manage how infrastructure operates. In many systems, policies are created by clicking on a GUI, making it difficult to replicate or version. Pulumi implements policy by writing it as code in a Typescript, which ensures that you can write policies using software development practices such as automated testing, deployment, and version control.

[Gareth Rushgrove](http://twitter.com/garethr) said in a QCon [presentation](https://www.infoq.com/presentations/policy-as-code/):

> “My policy kit doesn’t need to just be about bits on disk and packages, and files, and my SSH config, and my firewall rules, and my network rules. It can be about my cloud instances and how they’re actually configured and set up at the API level. Ultimately, there’s an API somewhere, and I have a bunch of resources, and I want to set some policies about them.”

Pulumi released the CrossGuard preview last fall. CrossGuard lets you verify, enforce, and apply custom policies on resources in your infrastructure. You can run policies against any Pulumi stack, which means that you can apply policies written in Typescript to stacks written in any language supported by Pulumi such as Python. Policy Packs are bundles of policies, and when you run `pulumi up`, every resource in the stack is evaluated through the Policy Pack. CrossGuard ensures that you can enforce best prac1tices for cost, compliance, security, and team practices for a single project or across your organization.

The CrossGuard preview provides the following key features:

 1. [Policy SDK](https://github.com/pulumi/pulumi-policy) for coding custom policies using TypeScript or Javascript
 2. [Running a Policy Pack locally](https://www.pulumi.com/docs/get-started/crossguard/authoring-a-policy-pack/#testing-the-policy-pack-locally) to speed up development and testing of policies
 3. [AWSGuard](https://github.com/pulumi/pulumi-policy-aws) for enforcing AWS best practices security, reliability, and cost
 4. [Apply a Policy Pack](https://www.pulumi.com/docs/get-started/crossguard/enforcing-a-policy-pack/) across an organization

If you’re interested in trying out CrossGuard, check out our blog post [Enforcing Different Kinds of Policies for Cloud Resources](https://www.pulumi.com/blog/enforcing-different-kinds-of-policies-for-cloud-resources/). Since the preview release, we have been incorporating user feedback and refining CrossGuard. Watch the introductory demo for CrossGuard and look for new features and policy packs in Pulumi 2.0.

{{< youtube -xJT_lON254 >}}

## Developer Experience

Building an application takes time, and it’s especially true with modern applications built on cloud resources. In Microsoft development circles, the inner loop is the process of writing, building, and debugging code iteratively. In modern application development, you want the loop to execute as quickly as possible, where the time it takes to execute a change is proportional to the size of that change. For example, a small change shouldn’t require the redeployment of a resource. A fast inner loop minimizes the time to collect high-quality descriptive feedback that aids in debugging. Finally, the inner loop should only run the operations necessary to test the change and defer operations not associated with the change.

Pulumi introduced two new experimental features to speed up inner loop development and make you more productive. The first feature is Pulumi Watch, a mode for developing cloud infrastructure that lets developers focus on application code and infrastructure instead of deployments. Watch does the following:

- Watches the workspace (defined in the Pulumi.yaml file) for changes
- Triggers an update to the stack whenever there is a change
- Streams output containing summaries of key update events as well as logs from any resources under management into a combined CLI output

In Watch mode, every time you save a change, it automatically deploys infrastructure changes. Switching between your editor and a terminal to use a CLI or trigger a build on a CI/CD is unnecessary. You can rapidly iterate through new ideas on your cloud infrastructure. Not all cloud infrastructure is amenable to fast iterations but severless, and Kubernetes deployments are ideal environments for using Watch.

The second experimental feature we introduced was [Pulumi Query for Kubernetes](https://github.com/pulumi/pulumi-query-kubernetes). Pulumi Query lets you query for live Kubernetes resources. You can write queries for discovering resources, the type of resources running, and characteristics of resources such as versions of MySQL or Pods that are publically exposed to the internet.

Query has two modes, batch and streaming. Batch queries generate a fixed report when they run to completion and return lists of resources specified in the query. Streaming queries watch resources in Kubernetes and can act when events occur. For example, a streaming query can post a notification on Slack when a volume runs out of disk space.

We will be incorporating these experimental features in the 2.0 release to improve the development experience through accelerating inner loop development and providing powerful primitives for introspection and observability.

## The Road Ahead

These are the major themes for the Pulumi 2.0 release. We’re building on our earlier work and incorporating the feedback and suggestions from the community and our customers. These features are available in preview, and we encourage you to try them provide feedback either through issues in [Github](https://github.com/pulumi) or on the [Pulumi Community Slack](https://slack.pulumi.com/).
