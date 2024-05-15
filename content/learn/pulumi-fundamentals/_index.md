---
title_tag: Pulumi Fundamentals | Learn Pulumi
title: "Pulumi Fundamentals"
layout: module
date: 2021-09-10T12:00:00-05:00
draft: false
description: |
    Learn how to use Pulumi to build, configure, and deploy a real-life, modern
    application.
meta_desc: Learn how to use Pulumi to build, configure, and deploy a real-life, modern application in this starter tutorial.
index: 0
meta_image: fundamentals.png
youll_learn:
    - Creating projects
    - Configuring and provisioning infrastructure
tags:
    - fundamentals
providers:
    - docker
---

For this tutorial, we're going to learn more about cloud computing by exploring
how to use Pulumi to build, configure, and deploy a real-life, modern
application using Docker. We will create a frontend, a backend, and a database
to deploy the Pulumipus Boba Tea Shop. Along the way, we'll learn more about how
Pulumi works.

## Time

How long this tutorial will take depends on your internet connection, reading
speed, and other factors. On average, this tutorial should take you about 25
minutes to complete.

## Prerequisites

You will need the following tools to complete this tutorial:

- A [Pulumi account and token](/docs/pulumi-cloud/accounts#access-tokens)
    - If you don't have an account, go to the [signup page](https://app.pulumi.com/signup).
- The [Pulumi CLI](/docs/cli/)
    - If you don't have the CLI, go to the [installation page](/docs/install/).
- [Docker](https://docs.docker.com/get-docker/)
- One of the following languages:
    - For the TypeScript/JavaScript version, Node.js 14 or later
    - For the Python version, Python 3.8 or later
    - For the Java version, Java 11 or later and Gradle 7.4 or later
    - For the YAML version, nothing specific!

As to skills, you should be able to  <!-- Grammar note: No colon on lists when the list completes the sentence like this :) -->

- use your local terminal.
- read and understand basic files from one of these languages:
    - TypeScript/JavaScript
    - Python
    - Java
    - YAML
- read and understand Dockerfiles or understand basic Docker concepts.

## Sample app

The sample app we're building, the Pulumipus Boba Tea Shop, is a progressive web
application (PWA) built with MongoDB, ExpressJS, React, and NodeJS (the MERN
stack). It's a fairly common implementation found in eCommerce applications. We
have adapted this application from
[this repository](https://github.com/shubhambattoo/shopping-cart). The app
consists of a frontend client, a backend REST server to manage transactions, and
a MongoDB instance for storing product data.

## About this pathway

This pathway discusses using Pulumi to create infrastructure, configure that
infrastructure, and push your infrastructure to production.

For this pathway, we will use Docker to let you learn the basics of Pulumi
without a cloud account. We will explore creating a Pulumi Project, building
Docker images, and configuring and provisioning containers.

Let's get started!
