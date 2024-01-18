---
title_tag: "Pulumi ESC FAQs"
meta_desc: Frequently asked questions about Pulumi ESC preview, GA, pricing and roadmap.
title: FAQ
h1: Pulumi ESC FAQs
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  pulumiesc:
    weight: 6
    identifier: faq
---

## Is it safe to use Pulumi ESC for my production stacks?

Yes, Pulumi ESC is served using the same [highly secure](/security/pulumi-cloud-security-whitepaper.pdf) and highly available infrastructure as the rest of Pulumi Cloud. The service is currently in preview as we are rapidly iterating and improving the feature set. It is unlikely that we will make any breaking changes. Should we introduce a new API, we are dedicated to ensuring optimal compatibility to prevent any interruptions to your infrastructure.

## Why did Pulumi launch ESC?

We launched Pulumi ESC in response to customer feedback about their difficulties in managing config and secrets causing sprawl and duplications across stacks. Pulumi ESC is a natural extension of Pulumi IaC by allowing [hierarchical](/docs/pulumi-cloud/esc/#configuration-as-code) configurations that can be used across stacks.

## When will Pulumi ESC be generally available?

Pulumi ESC will be generally available in 2024.

## What will be the pricing of Pulumi ESC?

During the preview, the product is free to use. When the product is made generally available, it will have a pricing model that is competitive with the market.

**What is the roadmap for Pulumi ESC?**
<br>
We have a lot of [features](https://github.com/pulumi/esc/issues) planned for ESC. Here are a few highlights:

- [Webhooks](https://github.com/pulumi/esc/issues/188)
- [Syncing config/secrets to external systems](https://github.com/pulumi/esc/issues/58)
- [Version controlled environments](https://github.com/pulumi/esc/issues/63)
- [Table UI authoring experience](https://github.com/pulumi/esc/issues/62)

We encourage you to create a [feature request](https://github.com/pulumi/esc/issues/new/choose) or upvote [existing open requests](https://github.com/pulumi/esc/issues).

## Can a Self-hosted Pulumi customer use this?

Pulumi ESC is currently not supported for self-hosted customers. [Contact sales](/contact/?form=sales) if you'd like to participate in our self-hosted beta for ESC when it is available.
