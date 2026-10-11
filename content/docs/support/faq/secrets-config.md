---
title_tag: "Pulumi ESC FAQs"
meta_desc: Frequently asked questions about Pulumi ESC, pricing and self-hosting.
title: Secrets & Configuration FAQ
h1: Secrets & Configuration FAQ
menu:
  support:
    parent: support-faq
    name: Secrets & Config FAQ
    weight: 2
    identifier: support-faq-secrets-config
aliases:
  - /docs/pulumi-cloud/esc/faq
  - /docs/esc/faq/
---

## Why did Pulumi launch ESC?

We launched Pulumi ESC in response to customer feedback about their difficulties in managing config and secrets, causing sprawl and duplications across stacks. Pulumi ESC brings the same Pulumi IaC-like software engineering approach to secrets and configuration, allowing [hierarchical](/docs/esc/concepts/) configurations that eliminate copy/paste. It can be used for all applications and infrastructure - with or without Pulumi IaC.

## What is the pricing of Pulumi ESC?

See our [pricing page](/pricing) for details.

## What counts as a secret towards pricing?

Secrets include [static secrets](/docs/esc/concepts/builtin-functions/fn-secret/), [dynamic login credentials](/docs/esc/providers/login/) and [dynamic secrets](/docs/esc/providers/secrets/).

In other words, when using Pulumi ESC's document editor, each definition of `fn::secret` and `fn::open::*` (except with the [pulumi-stacks provider](/docs/esc/providers/iac/pulumi-stacks/)) is counted as a secret.

Only the secrets from the latest environment revision are counted towards your bill.

## Can I self-host Pulumi ESC?

Yes. [Contact sales](/contact/?form=sales) for a demo or trial of self-hosted Pulumi ESC.

## Learn more

- [Pulumi IaC FAQ](/docs/support/faq/infrastructure/)
- [Pulumi Cloud FAQ](/docs/support/faq/pulumi-cloud/)
- [Pulumi Policies FAQ](/docs/support/faq/policies/)
