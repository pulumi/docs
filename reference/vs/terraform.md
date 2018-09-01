---
title: Pulumi vs. Terraform
redirect_from: /reference/terraform.html
---

Terraform is the closest comparison to Pulumi. In Terraform, you write programs in a custom
domain-specific-language (DSL) called Hashicorp Configuration Language (HCL), and the Terraform engine
takes care of provisioning and updating resources, very similar to Pulumi. Just like Pulumi, Terraform
supports many cloud providers. In fact, thanks to integration with Terraform, Pulumi is able to support a
superset of the cloud and service providers that Terraform currently offers.

The major differences between Terraform and Pulumi are as follows:

1. Terraform requires that you and your team learn a new custom language, the HCL DSL. In contrast, Pulumi lets you use
   languages you already know and love, like JavaScript, TypeScript, Python, and Go.

2. Because of the use of real languages, you get familiar constructs like for loops, functions, and classes. This
   significantly improves the ability to cut down on boilerplate and enforce best practices. Instead of creating
   a new ecosystem of modules and sharing, Pulumi lets you leverage existing package management tools and techniques.

3. Terraform, by default, requires that you manage concurrency and state manually, by way of its "state files." Pulumi,
   in contrast, uses the free app.pulumi.com service to eliminate these concerns. This makes getting started with
   Pulumi, and operationalizing it in a team setting, much easier. For advanced use cases, [it is possible to use
   Pulumi without the service](https://pulumi.io/reference/faq.html#can-i-use-pulumi-without-depending-on-pulumicom),
   which works a lot more like Terraform, but it is harder to do and opt-in. Pulumi errs on the side of ease-of-use.

4. Pulumi has deep support for cloud native technologies, like Kubernetes, and supports advanced deployment
   scenarios that cannot be expressed with Terraform. This includes Prometheus-based canaries, automatic Envoy
   sidecar injection, and more. Pulumi is a proud member of the Cloud Native Computing Foundation (CNCF).

Pulumi is [open source](https://github.com/pulumi/pulumi) and available on GitHub.

## Integration with Terraform

Pulumi is able to adapt [any Terraform Provider](https://github.com/terraform-providers) for use with Pulumi, enabling
management of any infrastructure supported by the Terraform Providers ecosystem using Pulumi programs.

Indeed, some of Pulumi's most interesting providers have been created this way, delivering access to robust,
tried-and-true infrastructure management.  The Terraform Providers ecosystem is mature and healthy, and enjoys
contributions from many cloud and infrastructure leaders across the industry, ourselves included.

Most Pulumi users don't need to know about this detail, however we are proud to be building on the work of others,
and contributing our own open source back to this vibrant ecosystem, and thought you should know.

In the event you'd like to add new providers, or understand how this integration works, please check out the
[Pulumi Terraform bridge repo](https://github.com/pulumi/pulumi-terraform).  This bridge is fully open source and
makes it easy to create new Pulumi providers out of existing Terraform Providers.
