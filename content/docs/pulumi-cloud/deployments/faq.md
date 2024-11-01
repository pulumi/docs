---
title_tag: "Pulumi Deployments: FAQ & Pricing"
meta_desc: Frequently asked questions including pricing, general availability, and roadmap.
title: FAQ
h1: Pulumi Deployments FAQ
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  cloud:
    name: FAQ
    parent: pulumi-cloud-deployments
    weight: 9
    identifier: pulumi-cloud-deployments-faq
  pulumicloud:
    parent: deployments
    weight: 6
aliases:
  - /docs/intro/deployments/faq/
---

## Security and Isolation

Deployments run on single-use virtual machines and compute and storage are never shared across runs. We designed our architecture to maximize isolation. In addition, security features like OIDC allow you to fine tune credential scope, lifetime, and expiration policies at a per-deployment level. It is also possible to use [self-hosted runners](/docs/pulumi-cloud/deployments/customer-managed-agents/) if you require additional isolation.

## Common recipes

See [Using Deployments](/docs/pulumi-cloud/deployments/reference/) for common recipes and best practices.

## More FAQ

- [Pulumi IaC FAQ](/docs/iac/support/faq/)
- [Pulumi ESC FAQ](/docs/esc/faq/)
- [Pulumi Cloud FAQ](/docs/pulumi-cloud/faq/)
- [Pulumi Cloud SCIM FAQ](/docs/pulumi-cloud/access-management/scim/faq/)
- [Pulumi CrossGuard FAQ](/docs/using-pulumi/crossguard/faq/)
- [Kubernetes guides FAQ](/docs/clouds/kubernetes/guides/faq/)
