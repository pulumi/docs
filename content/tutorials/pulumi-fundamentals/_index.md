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
meta_image: meta.png
youll_learn:
    - Creating projects
    - Configuring and provisioning infrastructure
tags:
    - fundamentals
providers:
    - docker
aliases:
    - /learn/pulumi-fundamentals/
---

In this tutorial, you'll learn about cloud computing with Pulumi by building, configuring, and deploying a real-world, modern
application with Docker. You'll create a front-end interface, a back-end service, and a database to deploy the Pulumipus Boba Tea Shop. Along the way, you'll learn more about how Pulumi works.

For this tutorial, we will use Docker to let you learn the basics of Pulumi
without a cloud account. We will explore creating a Pulumi Project, building
Docker images, and configuring and provisioning containers.

## Prerequisites

To complete this tutorial, you'll need:

- A [Pulumi Cloud account](https://app.pulumi.com/signup) and [access token](/docs/pulumi-cloud/accounts#access-tokens)
- The [Pulumi CLI](/docs/install/)
- [Docker](https://docs.docker.com/get-docker/)
- One of the following supported language runtimes, depending on your language choice:
    - Node.js
    - Python
    - Java
    - YAML

You should also be able to:

- Use your local terminal
- Read and understand Dockerfiles and basic Docker concepts.

## What you'll build

The sample app we'll be building, the Pulumipus Boba Tea Shop, is a progressive web application (PWA) built with MongoDB, ExpressJS, React, and Node.js (the MERN stack). It's a common stack used in eCommerce applications. We have adapted this application from [this repository](https://github.com/shubhambattoo/shopping-cart). The app consists of a frontend client, a backend REST server to manage transactions, and a MongoDB instance for storing product data.

Let's get started!
