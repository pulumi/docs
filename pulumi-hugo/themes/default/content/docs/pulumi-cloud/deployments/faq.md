---
title_tag: "Pulumi Deployments: FAQ & Pricing"
meta_desc: Frequently asked questions including pricing, general availability, and roadmap.
title: FAQ
h1: Pulumi Deployments FAQ
menu:
  pulumicloud:
    parent: deployments
    weight: 6
aliases:
  - /docs/intro/deployments/faq/
---

## General Availability

Pulumi Deployments is currently in preview and is expected to reach general availability (GA) by the end of 2023. We view the platform as stable, and production-ready with users including Pulumi itself relying on deployments in production environments every day. Pulumi does not make breaking changes, even to preview APIs. At GA we will cut a new version of the Deployments REST API, and continue to maintain the preview version for one year or until we’ve assisted all users in migrating. The most significant change that will come with GA is the addition of a pricing model, the details of which are discussed further in this document.

## Pricing

Pulumi Deployments is free during the preview, with plans to add a pricing model when the platform becomes generally available. We will charge based on the number of deployment minutes that you consume, similar to the billing model of GitHub Actions. Custom contract pricing in advance of GA is available for Enterprise customers.  [Contact us for a quote](https://pulumi.com/contact/?form=sales).

## Roadmap

We track open feature requests for Deployments in the [service-requests repo](https://github.com/pulumi/service-requests). Here are a few that have been requested by customers that are on our roadmap:

- [Built-in drift detection](https://github.com/pulumi/service-requests/issues/173)
- [Ephemeral stack support](https://github.com/pulumi/service-requests/issues/206)
- [Built-in temporary infrastructure and TTL stacks](https://github.com/pulumi/service-requests/issues/149)
- [User-hosted deployment runners](https://github.com/pulumi/service-requests/issues/207)
- [Add `git push` support for other VCS providers such as Bitbucket](https://github.com/pulumi/service-requests/issues/162)
- [Integrating Deployment statuses with Slack](https://github.com/pulumi/service-requests/issues/168)

## Security and Isolation

Deployments run on single-use virtual machines and compute and storage are never shared across runs. We designed our architecture to maximize isolation. In addition, security features like OIDC allow you to fine tune credential scope, lifetime, and expiration policies at a per-deployment level. Self-hosted deployment runners are on our roadmap.

## More FAQ

- [Kubernetes guides FAQ](/docs/clouds/kubernetes/guides/faq/)
- [Policy as code FAQ](/docs/using-pulumi/crossguard/faq/)
- [Pulumi CLI & Pulumi Cloud FAQ](/docs/support/faq/)
- [Pulumi Cloud SCIM FAQ](/docs/pulumi-cloud/access-management/scim/faq/)
