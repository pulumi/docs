---
title: "Pulumi 2.0 Roadmap"
authors: ["joe-duffy"]
tags: ["Pulumi-News"]
meta_desc: "Today we've published Pulumi's 2.0 roadmap, the next major phase in Pulumi's journey. This release will support great productivity, deeper support for enterprise workloads, and a whole lot more. Let us know what you think."
date: "2019-12-02"

meta_image: "pulumi-1-0.png"
---

Today we've published [Pulumi's 2.0 roadmap](https://github.com/pulumi/pulumi/issues/3591). 2.0 is the next major phase in Pulumi's journey, and will include better productivity through languages, libraries, and tools, in addition to advanced features for teams in production. And, though we are excited to share our own thoughts, more than anything else, we'd love to hear your feedback to help make sure it's right.

Since [releasing Pulumi 1.0 in September](/blog/pulumi-1-0), we have heard loud and clear that you appreciate the commitment to compatibility, as well as the completeness and stability of the platform, and we have been hard at work making sure we honor those promises.

As we look to 2.0, we are aiming to help you be more successful with modern cloud architectures, by implementing features that we've heard are missing or could be better, as well as doing better at the fundamentals. Although this is a "2.0" release, we do not plan any major breaking changes, so that we can continue honoring our promise to provide a stable platform to you.

## Two Themes for 2.0

The two themes we have chosen for Pulumi 2.0 are:

* **Best in class productivity.** Pulumi's foundation of general-purpose languages has already enabled great productivity gains thanks to ecosystems of tools, sharing and reuse, and familiarity. But we have ideas for more. This includes more languages, features that bring deployments closer to the inner development loop like watch mode, more libraries of off-the-shelf patterns and practices, and the ability to test your infrastructure more easily.

* **Belts and suspenders for teams and enterprises.** As we work with more teams and enterprises to deliver demanding many-cloud workloads to public, private, and hybrid clouds &mdash; increasingly involving Kubernetes, and often spanning developers and operations teams &mdash; we have heard about many features that would maximize Pulumi's effectiveness and utility. This includes advanced security and compliance capabilities, more organization-wide controls and policies, and more flexible self- and on-premises hosting of the Pulumi service.

Several major 2.0 features are available to try out today and we'd love to hear what you think. [The 2.0 roadmap is on GitHub](https://github.com/pulumi/pulumi/issues/3591) so that you can easily comment or follow along as we make progress.

## Trying Out 2.0 Preview Features

A number of new features are already available in "preview"; the preview tag simply means we expect possibly-significant changes to them between now and the 2.0 release.

> Many features require you to set the `PULUMI_EXPERIMENTAL` environment variable to `true` before you can use them.
> This can be done by running `export PULUMI_EXPERIMENTAL=true` in your macOS or Linux shell, or by running
> `$env:PULUMI_EXPERIMENTAL = "true"` in your Windows PowerShell console.

### Better Language Support

Support for Go and .NET Core (C#/F#/VB) languages is currently marked preview because there is known work before we're comfortable calling them "done." This includes improving the programming models to be more idiomatic for their respective ecosystems &mdash; such as stronger typing in Go instead of `interface{}` and `StackReference` support in .NET &mdash; as well as improving the documentation, availability of samples, templates, and tutorials, written in those languages.

Expect to see a steady stream of improvements between now and 2.0 being finished; to follow along, see these work items on GitHub: [Go](https://github.com/pulumi/pulumi/issues/1614) and [.NET](https://github.com/pulumi/pulumi/issues/3470).

### Policy as Code ("CrossGuard")

Today we have released preview support for a new policy as code offering that we call CrossGuard. Just as you can write your infrastructure as code in your favorite language, so too can you now write your policies. These policies run whenever you do a Pulumi deployment, enabling CrossGuard to restrict deployments that violate security, compliance, cost, or stylistic requirements.

You can write custom policies, or use off-the-shelf policies authored by the community, including our preview [AWS pack](https://github.com/pulumi/pulumi-policy-aws) and [Open Policy Agent (OPA) integration](https://github.com/pulumi/pulumi-policy-opa). Just as you can share your own infrastructure creations using your language's package manager, you can share your policies too.

CrossGuard is 100% open source, enabled by `pulumi up`'s new `--policy-pack` flag, and advanced organization-wide controls are available in the Team and Enterprise Editions. To learn more, [read the CrossGuard user guide](/docs/guides/crossguard); or, to dive straight in, try out [the getting started tutorial](/docs/get-started/crossguard).

### Testing

[We've blogged previously about how to test your infrastructure](/blog/unit-testing-infrastructure-in-nodejs-and-mocha/). However, we hear all the time about new scenarios and ways in which Pulumi could do a better job here, including removing many of the rough edges currently hit when testing Pulumi code.

Pulumi 2.0 will support a spectrum of testing scenarios, including unit testing, integration testing, and post-deployment runtime validation. The addition of CrossGuard also means you can validate your infrastructure configuration integrated into your existing CI/CD processes. As part of the 2.0 release, we will be publishing comprehensive guides and tutorials for testing your infrastructure.

### Watch Mode

We recently added the ability to deploy changes to your applications and infrastructure continuously, straight from your IDE. This brings infrastructure as code to your core inner development loop in a major way and is guaranteed to change the way you think about the essential differences between the way you approach engineering modern cloud applications versus the requisite infrastructure.

To give watch mode a try, simply run `pulumi watch`. Or, to see a demo of watch mode in action, check out this video:

{{< youtube X96EMLi8uJY >}}

### Self-Host and On-Premises

Although we've worked hard to make the Pulumi service easy and affordable to use by default, we understand that some customers can't depend on a multi-tenanted SaaS website for their infrastructure deployments. For these customers, Pulumi already offers [custom state hosting](/docs/intro/concepts/state/) in AWS S3, Azure Blob Storage, GCP Cloud Storage, or even as a manually managed JSON file. However, by hosting the state this way, you lose out on what makes the Pulumi service so great: identity, teams, RBAC, policies, webhooks, and more.

Today we are releasing preview support for the self-hosted Pulumi service. This gives you the full capabilities of the Pulumi Enterprise SaaS, while also giving you the flexibility to run it anywhere. Self-hosted Pulumi Enterprise can run on-premises behind your firewall on a VM or in Kubernetes, in your AWS, Azure, or GCP account &mdash; virtually anywhere that can run VMs or containers. For more information, see the [tutorial about how to configure self-hosted Pulumi Enterprise](/docs/guides/self-hosted), or [contact us for pricing information and a demo](/contact).

### A Lot More ...

This is just a sampling of what's already ready to try out. Expect a lot more, including many features and stability improvements that are driven by ongoing customers and community feedback.

## From Modern Infrastructure to Modern Architecture

Pulumi 1.0 gave us a solid foundation of modern infrastructure as code. As we see the things you are building with Pulumi, we understand that challenges don't stop at infrastructure provisioning. Pulumi is also about the applications themselves, as modern cloud architectures demand infrastructure and applications to coexist in harmony and unique ways that Pulumi enables.

In addition to many great features, Pulumi 2.0 will also further advance the [Pulumi Crosswalk family of offerings](/docs/guides/crosswalk) to bring more of these modern application architecture patterns to your fingertips. This includes support for additional languages beyond JavaScript and TypeScript, improved documentation, interactive tutorials, and more extensive libraries of patterns and practices.

## Two Asks

Although a lot of 2.0 is already underway, we are still planning out the concrete roadmap and there is a lot of room for feedback. We have two asks for you:

* Please give the preview features a try, and let us know what you think.
* Please let us know what is missing from our list.

Please give us feedback by [commenting on the GitHub tracking issue](https://github.com/pulumi/pulumi/issues/3591) or [in the Community Slack](https://slack.pulumi.com).

## Next Steps

1.0 was a major milestone for us and 2.0 is going to be better. 2.0 will make modern cloud architectures even more approachable and productive to create, while also deepening support for modern teams and workloads running in production, often across many-clouds.

We want to thank you for your continued support and feedback &mdash; it's what makes Pulumi tick!
