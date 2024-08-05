---
title_tag: Pulumi Fundamentals | Pulumi Tutorials
title: "Pulumi Fundamentals"
layout: module
description:  Learn how to use Pulumi to build, configure, and deploy a real-world application.
meta_desc: Learn how to use Pulumi to build, configure, and deploy a real-life, modern application in this starter tutorial.
meta_image: meta.png
youll_learn:
    - Creating projects
    - Configuring and provisioning infrastructure
prereqs:
    - A [Pulumi Cloud account](https://app.pulumi.com/signup) and [access token](/docs/pulumi-cloud/accounts#access-tokens)
    - The [Pulumi CLI](/docs/install/)
    - Familiarity with JavaScript, TypeScript, or Python
    - A [Docker](https://docs.docker.com/get-docker/) service installed and running
collections:
    - pulumi-101
collections_weight: 1
weight: 1
aliases:
    - /learn/pulumi-fundamentals/
---

In this tutorial, you'll learn about cloud computing with Pulumi by building, configuring, and deploying a real-world, modern
application with Docker. You'll create a front-end interface, a back-end service, and a database to deploy the Pulumipus Boba Tea Shop. Along the way, you'll learn more about how Pulumi works.

For this tutorial, we will use Docker to let you learn the basics of Pulumi
without a cloud account. We will explore creating a Pulumi Project, building
Docker images, and configuring and provisioning containers.

## What you'll build

The sample app we'll be building, the Pulumipus Boba Tea Shop, is a progressive web application (PWA) built with MongoDB, ExpressJS, React, and Node.js (the MERN stack). It's a common stack used in eCommerce applications. We have adapted this application from [this repository](https://github.com/shubhambattoo/shopping-cart). The app consists of a frontend client, a backend REST server to manage transactions, and a MongoDB instance for storing product data.

Let's get started!
