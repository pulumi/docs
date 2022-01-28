---
title: "Pulumi Fundamentals"
layout: module
date: 2021-09-10T12:00:00-05:00
draft: false
description: |
    Learn how to use Pulumi to build, configure, and deploy a real-life, modern
    application.
meta_desc: |
    Learn how to use Pulumi to build, configure, and deploy a real-life, modern
    application.
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

- A [Pulumi account and token]({{< relref "/docs/intro/pulumi-service/accounts#access-tokens" >}})
  - If you don't have an account, go to the
    [signup page](https://app.pulumi.com/signup).
- [Docker](https://docs.docker.com/get-docker/)
- Python 3.8 or later

As to skills, you should be able to  <!-- Grammar note: No colon on lists when the list completes the sentence like this :) -->

- use your local terminal.
- read and understand basic Python code.
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
