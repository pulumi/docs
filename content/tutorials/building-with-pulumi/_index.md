---
title_tag: Building with Pulumi | Pulumi Tutorials
title: Building with Pulumi
layout: module
description: Learn how to use Pulumi for more complex configurations with multiple environments.
meta_desc: Learn how to create multiple Pulumi programs and work with them interdependently with this tutorial.
meta_image: meta.png
youll_learn:
    - Using stacks for unique configurations of different environments
    - Sharing values from one Pulumi program or project to another
    - Working with secrets inside of Pulumi
prereqs:
    - Completion of the [Pulumi Fundamentals tutorial](/tutorials/pulumi-fundamentals/) and an existing `my-first-app` project
    - A [Pulumi Cloud account](https://app.pulumi.com/signup) and [access token](/docs/pulumi-cloud/accounts#access-tokens)
    - The [Pulumi CLI](/docs/install/)
    - A [Docker](https://docs.docker.com/get-docker/) service installed and running
collections:
    - pulumi-101
collections_weight: 2
weight: 2
aliases:
    - /learn/building-with-pulumi/
---

This tutorial digs a little deeper into what it means to create multiple Pulumi programs and work with them interdependently. We will also cover how Pulumi uses secrets and how you can test your Pulumi programs.
