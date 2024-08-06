---
title_tag: Pulumi Fundamentals | Pulumi Tutorials
title: "Pulumi Fundamentals"
layout: module
description:  Learn how to use Pulumi to build, configure, and deploy a real-world application.
meta_desc: Learn how to use Pulumi to build, configure, and deploy a real-life, modern application in this starter tutorial.
meta_image: meta.png
youll_learn:
    - Creating Pulumi projects
    - Configuring, provisioning, and destroying infrastructure
    - Managing Docker images, containers, and services with Pulumi
prereqs:
    - The [Pulumi CLI](/docs/install/)
    - A [Pulumi Cloud account](https://app.pulumi.com/signup) and [access token](/docs/pulumi-cloud/accounts#access-tokens)
    - Familiarity with JavaScript, TypeScript, or Python
    - A [Docker](https://docs.docker.com/get-docker/) service installed and running locally
collections:
    - pulumi-101
collections_weight: 1
weight: 1
aliases:
    - /learn/pulumi-fundamentals/
---

In this tutorial, you'll learn about cloud computing with Pulumi by building, configuring, and deploying a real-world, modern
application with Docker. You'll create a front-end interface, a back-end service, and a database to deploy a web application called the Pulumipus Boba Tea Shop. Along the way, you'll learn more about how Pulumi works.

For this tutorial, you'll use Docker to learn the basics of deploying with Pulumi. You'll create a Pulumi Project, build Docker images, and configure and provision containers with those images, all with Pulumi.

The sample app we'll be building, the Pulumipus Boba Tea Shop, is a progressive web application (PWA) built with MongoDB, ExpressJS, React, and Node.js (the MERN stack). It's a common stack used in e-commerce applications, adapted from [this repository](https://github.com/shubhambattoo/shopping-cart).
