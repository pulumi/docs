---
title_tag: "Pulumi ESC FAQs"
meta_desc: Frequently asked questions about Pulumi ESC, pricing and roadmap.
title: FAQ
h1: Pulumi ESC FAQs
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  esc:
    parent: esc-home
    weight: 11
    identifier: faq
aliases:
  - /docs/pulumi-cloud/esc/faq
search:
  keywords:
    - ESC
    - secrets
    - customer feedback
    - configuration management
---

## Why did Pulumi launch ESC?

We launched Pulumi ESC in response to customer feedback about their difficulties in managing config and secrets, causing sprawl and duplications across stacks. Pulumi ESC brings the same Pulumi IaC-like software engineering approach to secrets and configuration, allowing [hierarchical](/docs/esc/#configuration-as-code) configurations that eliminate copy/paste. It can be used for all applications and infrastructure - with or without Pulumi IaC.

## What is the pricing of Pulumi ESC?

See our [pricing page](https://www.pulumi.com/pricing/) for details.

## What counts as a secret towards pricing?

Secrets include [static secrets](/docs/esc/get-started/store-and-retrieve-secrets/), [dynamic login credentials](/docs/esc/integrations/dynamic-login-credentials/) and [dynamic secrets](/docs/esc/integrations/dynamic-secrets/).

In other words, when using Pulumi ESC's document editor, each definition of `fn::secret` and `fn::open::*` (except with the [pulumi-stacks provider](/docs/esc/integrations/infrastructure/pulumi-iac/pulumi-stacks/)) is counted as a secret.

Only the secrets from the latest environment revision are counted towards your bill.

## What is the roadmap for Pulumi ESC?

Check out our [public roadmap](https://github.com/orgs/pulumi/projects/44/) page.

If you are interested in a particular feature, we encourage you to create a [feature request](https://github.com/pulumi/esc/issues/new/choose) or upvote an [existing request](https://github.com/pulumi/esc/issues).

## Can I self-host Pulumi ESC?

Yes. [Contact sales](/contact/?form=sales) for a demo or trial of self-hosted Pulumi ESC.

## More FAQ

- [Pulumi IaC FAQ](/docs/iac/support/faq/)
- [Pulumi Cloud FAQ](/docs/pulumi-cloud/faq/)
- [Pulumi Cloud Deployments FAQ](/docs/pulumi-cloud/deployments/faq/)
- [Pulumi Cloud SCIM FAQ](/docs/pulumi-cloud/access-management/scim/faq/)
- [Kubernetes guides FAQ](/docs/clouds/kubernetes/guides/faq/)
- [Pulumi CrossGuard FAQ](/docs/using-pulumi/crossguard/faq/)
