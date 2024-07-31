---
title_tag: Building with Pulumi | Learn Pulumi
title: "Building with Pulumi"
layout: module
date: 2021-09-20T08:30:13-05:00
draft: false
description: Learn how to use Pulumi for more complex configurations with multiple environments.
meta_desc: Learn how to create multiple Pulumi programs and work with them interdependently with this tutorial.
index: 1
meta_image: meta.png
youll_learn:
    - Using stacks for unique configurations of different environments
    - Sharing values from one Pulumi program or project to another
    - Working with secrets inside of Pulumi
aliases:
    - /learn/building-with-pulumi/
providers:
    - aws
---

This tutorial digs a little deeper into what it means to create multiple Pulumi programs and work with them interdependently. We will also cover how Pulumi uses secrets and how you can test your Pulumi programs.

## Time

How long this module will take depends on your internet connection, reading speed, and other factors. On average, this module should take you about 50 minutes to complete.

## Prerequisites

- Completion of the [Pulumi Fundamentals tutorial](/tutorials/pulumi-fundamentals/) and an existing `my-first-app` project
- A [Pulumi Cloud account](https://app.pulumi.com/signup) and [access token](/docs/pulumi-cloud/accounts#access-tokens)
- The [Pulumi CLI](/docs/install/)
- [Docker](https://docs.docker.com/get-docker/)
