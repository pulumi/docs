---
title_tag: Building with Pulumi | Pulumi Tutorials
title: Building with Pulumi
layout: module
description: Learn how to use Pulumi for more complex configurations with multiple environments.
meta_desc: Learn how to create multiple Pulumi programs and work with them interdependently with this tutorial.
meta_image: meta.png
weight: 2
summary: |
    This tutorial digs a little deeper into what it means to create multiple Pulumi programs and work with them interdependently. We will also cover how Pulumi uses secrets and how you can test your Pulumi programs.
youll_learn:
    - Using multiple stacks to configure environments independently
    - What stack outputs are and how to use them
    - How to manage sensitive data like database passwords with encrypted secrets
    - How to consume the outputs of another Pulumi stack with stack references
prereqs:
    - Completion of the [Pulumi Fundamentals tutorial](/tutorials/pulumi-fundamentals/) and an existing `my-first-app` project
    - The [Pulumi CLI](/docs/install/)
    - A [Pulumi Cloud account](https://app.pulumi.com/signup) and [access token](/docs/pulumi-cloud/accounts#access-tokens)
    - Familiarity with JavaScript, TypeScript, or Python
    - A [Docker](https://docs.docker.com/get-docker/) service installed and running locally
collections:
    - learn-pulumi
collections_weight: 2
aliases:
    - /learn/building-with-pulumi/
---
