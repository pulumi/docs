---
title_tag: "Pulumi Deployments: FAQ & Pricing"
meta_desc: Frequently asked questions including pricing, general availability, and roadmap.
title: FAQ
h1: Pulumi Deployments FAQ
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  pulumicloud:
    parent: deployments
    weight: 6
aliases:
  - /docs/intro/deployments/faq/
---

## Roadmap

We track open feature requests for Deployments in the [Pulumi Cloud requests repo](https://github.com/pulumi/pulumi-cloud-requests). Here are a few that have been requested by customers that are on our roadmap:

- [Built-in drift detection](https://github.com/pulumi/service-requests/issues/173)
- [Built-in temporary infrastructure and TTL stacks](https://github.com/pulumi/service-requests/issues/149)
- [User-hosted deployment runners](https://github.com/pulumi/service-requests/issues/207)
- [Add `git push` support for other VCS providers such as Bitbucket](https://github.com/pulumi/service-requests/issues/162)

## Security and Isolation

Deployments run on single-use virtual machines and compute and storage are never shared across runs. We designed our architecture to maximize isolation. In addition, security features like OIDC allow you to fine tune credential scope, lifetime, and expiration policies at a per-deployment level. Self-hosted deployment runners are on our roadmap.

## More FAQ

- [Kubernetes guides FAQ](/docs/clouds/kubernetes/guides/faq/)
- [Policy as code FAQ](/docs/using-pulumi/crossguard/faq/)
- [Pulumi CLI & Pulumi Cloud FAQ](/docs/support/faq/)
- [Pulumi Cloud SCIM FAQ](/docs/pulumi-cloud/access-management/scim/faq/)
