---
title: "An Update on Pulumi 2.0"
authors: ["joe-duffy"]
tags: ["Pulumi-News"]
date: "2020-03-04"
meta_desc: "."
meta_image: "pulumi-1-0.png"
---

It's been a few months since we announced the Pulumi 2.0 roadmap and we've been hard at work ever since. This includes significant rounding out of the .NET and Go SDKs, getting Policy as Code ready for prime-time, and many generally useful features and foundational improvements. As we get closer to the launch date, I wanted to take a moment to highlight some of these new capabilities. And please don't hold back on the feedback &mdash; we want to make sure 2.0 is the best that it can be!

<!--more-->

## .NET

We've made good progress on our .NET SDK. This includes tidying up the API surface area to feel more .NET-like, adding C# getting started guides for [AWS](https://www.pulumi.com/docs/get-started/aws?language=csharp), [Azure](https://www.pulumi.com/docs/get-started/azure?language=csharp), [GCP](https://www.pulumi.com/docs/get-started/aws?language=csharp), and [Kubernetes](https://www.pulumi.com/docs/get-started/aws?language=csharp), and adding more examples. We've closed the gap on all Pulumi features missing from the initial release, including [aliases]({{< relref "/docs/intro/concepts/programming-model#aliases" >}}), [transformations]({{< relref "/docs/intro/concepts/programming-model#transformations" >}}), [StackReference]({{< relref "/docs/intro/concepts/organizing-stacks-projects#inter-stack-dependencies" >}}), and .NET versions of the [Kubernetes](https://github.com/pulumi/pulumi-kubernetes), [Docker](https://github.com/pulumi/pulumi-docker), and [Terraform remote state](https://github.com/pulumi/pulumi-terraform) packages.

For .NET, we're just about done for 2.0. The remaining areas to improve include making the API documentation available in C# (we are getting close &mdash; more on that in the "still to come" section), migrating to .NET Core 3.1, and enabling you to more easily test your infrastructure.

## Go

We've entirely overhauled our Go SDK to be more idiomatic and easier to use. We previously used `map[string]interface{}` types in many places where you actually wanted to pass a real typed data structure; now you get strong typing for all Go APIs. . This can be seen by looking at some of the diffs in our examples, like this one.

Although we've had GoDoc support for some time now, we just recently began linking to them from our documentation website. We also added Go versions of our getting started guides. We have more improvements on the way.

There are a few upcoming features still remaining to flesh out. The biggest one is retiring Dep in favor of Go modules in our SDK, examples, and templates. We are also adding support for aliases, transformations, and improved API projections, such as supporting union types. Finally, we'll be adding Go support for our Kubernetes, Docker, and Terraform remote state packages.

## Policy as Code

CrossGuard, our Policy as Code framework, is now ready to take for a serious test drive. This new feature enables you to write policies in real code and enforce them during updates. Policies can check for anything, however the most common checks tend to involve security, compliance, cost management, and general and team best practices. You can write your own policy packages or use off-the-shelf policy packs like our own AWSGuard package.

CrossGuard is open source and the functionality is behind the new pulumi policy command, as well as the new --policy-pack flag for the preview and up commands. You can use this on any edition of Pulumi, without restriction, including the offline backends.

If you choose to use CrossGuard with the Enterprise Edition of Pulumi, however, you'll see some additional functionality. This includes server-side enforcement of policies and organizational policies, including policy packs which let you group many policies together.

We recently added the ability to tag policy packs with a semantic version so that you can easily manage and apply packs using user-friendly versions instead of auto-generated numbers.

All of the essential capabilities are now available and we don't expect any major breaking changes between now and the 2.0 launch. The remaining areas of focus are:

* First, letting you author policy packs in Python. It's already the case that your policies can apply to stacks written in any language, no matter the language of the policy pack itself, but today policy packs can only be written in Node.js; before GA, Python will be supported, and Go and .NET will follow afterward.
* Next, we are working on configurable policy packs so that you can selectively enable or disable specific rules, and/or set configuration variables on them that influence their behavior, on a per stack or policy group basis.
* Finally, we will be further fleshing out our reference policy packs, AWSGuard, AzureGuard, GCPGuard, and KubernetesGuard, so that you both have configurable rules available out-of-the-box, in addition to a starting point for creating your own packs.

Try CrossGaurd today using its easy Getting Started guide or check out some fun ideas on ways you might use it with the following blog post. 

## Other Goodies

Although we've seen significant improvements along these three main areas, there are too many features to name/

Pulumi Enterprise Edition now has full audit logs.

Stack grouping and sorting.

Stack export for the CLI and in the service.

Infrastructure mocking and testing.

## Goodies Still to Come

We continue to make progress on our multi-language library sharing capabilities. These will enable us to bring your favorite packages like EKS and AWSX to new languages, including Python, C#, and Go, in addition to letting you write your own. This has entailed some gnarly engineering work but will give us EKS in Python to start. We'll also be speaking at GopherCon this year about how it all works under the hood as part of our multi-language runtime.

Our API docs are getting a major overhaul! This includes a more resource-oriented view which will make it much easier to navigate and find what you're looking for, including code samples. This will also bring all languages on equal footing in terms of how documentation is presented and coverage of code samples.

Our tf2pulumi tool, which converts any Terraform HCL to Pulumi code, is currently getting a fresh coat of paint. This includes HCL2 support and Python code-generation.

We've made progress improving performance and have a lot more in the works. The changes already made include reducing overall network bandwidth used by an average update by 100x in some common cases. The work happening now will improve startup time by being smarter about how we configure providers to avoid roundtrips with, for instance, AWS. The net result is that you'll see fewer delays during updates and multiple seconds shaved off of startup time.

## Next Steps

Most of the remaining work is on our end but we're feeling great about the 2.0 release overall.
