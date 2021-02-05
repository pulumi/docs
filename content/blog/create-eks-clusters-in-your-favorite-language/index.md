---
title: "Create Amazon EKS clusters in your favorite language"
date: 2021-02-04
draft: false
meta_desc: The pulumi-eks package is now available in Python, Go, .NET, and TypeScript.
meta_image: multi-lang.png
authors:
    - levi-blackstone
tags:
    - aws
    - eks
    - .net
    - python
    - go
    - typescript
---

Pulumi's infrastructure as code tooling combines the programming languages and tools you already know with the full power of cloud
infrastructure. But until now, some Pulumi components for cloud infrastructure, like our popular [EKS package] for Amazon's Elastic
Kubernetes Service, were only available in a subset of the languages supported by Pulumi.

Now, you can use the [EKS package]–previously only available for TypeScript–in all four Pulumi languages: TypeScript, Python, .NET,
and Go. Regardless of the language you choose, you can [manage EKS clusters] with Pulumi, starting with the [v0.22.0 release]. Check
out our Modern Infrastructure Wednesday video to see it in action:

{{< youtube "gxLyAr0lUg0?rel=0" >}}

<!--more-->

### Making components available in every language

Pulumi's EKS package is made up of Pulumi components. A component is a collection of Pulumi [resources] that provides an easy way to
package best practices for using cloud resources, even if those best pratices span individual resources or even entire cloud providers.
Until now though, components could only be used in Pulumi programs written in the same language as the component.

To change that, we're creating "[multi-language components]". With multi-language components, anyone will be able to author a component
in one language and automatically compile it to all other languages supported by Pulumi. This means anyone in the worldwide Pulumi
community will be able to take advantage of any component, even if it's written in a different language. Right now, unless a component
author is willing to write code in all four Pulumi languages, their component is only able to reach Pulumi users using the same
language SDK.

In addition to expanding the library of publicly available components, this work will also enable organizations to write
Pulumi components in the right programming language, or languages, for each team and each product. Infrastructure or platform teams will
be able to write components in Go and share them with a webapp team using TypeScript, write components in .NET and share them with a
machine learning team using Python, and any other combination that suits their business.

The next step in the story is a seamless authoring experience that enables component creators to write, build, and publish multi-language
components. That will be in public preview soon, and we're excited for you to try it out. If you'd like, subscribe to the
[multi-language components] issue for updates.

### Next steps

If you haven't yet, try out the new pulumi-eks package with [this walkthrough].

<!-- markdownlint-disable url -->
[EKS package]: {{< relref "/docs/reference/pkg/eks" >}}
[v0.22.0 release]: https://github.com/pulumi/pulumi-eks/releases/tag/v0.22.0
[manage EKS clusters]: {{< relref "/blog/easily-create-and-manage-aws-eks-kubernetes-clusters-with-pulumi" >}}
[multi-language components]: https://github.com/pulumi/pulumi/issues/2430
[this walkthrough]:  https://www.pulumi.com/blog/easily-create-and-manage-aws-eks-kubernetes-clusters-with-pulumi/
[resources]: https://www.pulumi.com/docs/intro/concepts/resources/
<!-- markdownlint-enable url -->
