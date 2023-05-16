---
title: Pulumi AI
meta_desc: Pulumi AI is an experimental feature that lets you use natural-language prompts to generate Pulumi infrastructure-as-code programs in your favorite language.
meta_image: /ai/meta.png
layout: ai
aliases:
    - pulumi-ai
welcome: |
    ## Welcome to Pulumi AI.

    What cloud infrastructure would you like to build?

    Try something like _I want a static website on AWS behind a CloudFront CDN_, or _I want an Ubuntu Linux server that I can access over SSH_.
---

Pulumi AI is an experimental feature that lets you use natural-language prompts to generate Pulumi infrastructure-as-code programs in any language. This page is a web-based version of the open-source [Pulumi AI project](https://github.com/pulumi/pulumi-ai).

Use the chat widget to describe the infrastructure you'd like to build, making adjustments conversationally as you go. When you're done, create a new Pulumi project and deploy:

1. [Install Pulumi](/docs/install/)

1. Create a new {{< pulumi-language >}} project:

    {{< pulumi-new >}}

1. Paste the code into {{< langfile >}}

1. Install any required {{< langhost >}} dependencies

1. Deploy with `pulumi up`

## Try the CLI {#cli}

When you're ready to go further, [try the Pulumi AI CLI](https://github.com/pulumi/pulumi-ai), which lets you build cloud infrastructure interactively in real time.
