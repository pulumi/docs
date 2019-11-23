---
title: "KubeCon NA 2019: Are you about to break Prod? Acceptance Testing with Ephemeral Environments"
date: 2019-11-26
draft: true
meta_desc: "In this post, we recap and add more details to our KubeCon talk on setting up ephemeral environments. We will highlight how to acceptance test your application and infrastructure using ephemeral environments."
meta_image: meta.png
authors: ["erin-krengel"]
tags: ["testing", "ephemeral environments", "KubeCon", "kubernetes"]
---

Last week, my colleague Sean and I had the opportunity to present "Are you about to break prod? Acceptance Testing with Ephemeral Environments" at KubeCon NA 2019. In this talk, we covered what is an ephemeral environment, what is required to create one, and then we walked the audience through a concrete example of how to create one. Given our limited time, we had to move quickly through a ton of information. Today, I will recap our presentation and add a few more details we weren't able to cover.

<!--more-->

As software engineers, our job is to deliver business value. To do this, we need to be delivering software both quickly and reliably.

[DORA](), the DevOps Research Association, puts out an annual report evaluating the effectiveness of IT organization’s development and deployment processes. Their annual report consistently shows that top performers are deploying more frequently and getting code into production quicker, yet have lower rates of failure and quicker recovery times. The DORA report tell us that automated testing allows developers to confidently rely on their test suite for catching issues before they end up in production and confidentially know that a green test suite indicates the code is ready for deployment.

Today we will use Pulumi and GitLabCI to build a pipeline that validates both our application, infrastructure and deployment process.

## Ephemeral Environments

What is an ephemeral environment? It is a short-lived environment that mimics our production environment. To maintain agility, we typically define the boundaries of this environment to only encompass the first-level dependencies of the particular microservice we are deploying. This means, we will not spin up every single microservice or piece of infrastructure thats running in production. Yet we may need to spin up some extra pieces infrastructure to be able to properly test our microservice. For example, we may need to create a subscription to pull from a PubSub topic your microservice writes to.

## Why do we care

Infrastructure is often a key part of our application's behavior. Our architecture and requirements are constantly evolving. How can we incorporate these into our testing suite to give us a high degree of confidence?

Ephemeral environments allow us to integrate our infrastructure and deployment process into our testing suite. They ensure our testing environment is always in-sync with production and therefore allows us to iterate quickly and meet new requirements.

Ephemeral environments also encourage us to lean on automated tests over manual tests. If we use ephemeral environments as a replacement for a testing environment, there is not enough time to go in and run a manual check.

## Creating an Ephemeral Environment

To create an ephemeral environments, we will need a tool that allows us to do the following:

1. Infrastructure as Code - This allows us to create a consistently reproducible environment. Using an IaC tool means we can use the same code to define our infrastructure in both our ephemeral environment and production, giving us a high degree of confidence that production is accurately being mimicked. Today, we will use Pulumi to provision our Kubernetes and GCP resources.

1. Unique name for our ephemeral environment -  We use GitLab's pipeline ID and set our environment name to be `test-$CI_PIPELINE_ID`. Having a unique name for our ephemeral environment, allows us to run multiple tests (and therefore multiple pipelines) at once.

1. Configurable infrastructure - We will prepend our environment name to all the resources we create. This will allow us to easily distinguish our test resources and make sure resources don't conflict if we're running multiple tests at once. This also means if something goes wrong and we have lingering resources, we can use regex and a cron job to clean up these extra resources.

1. Configurable application & tests - Making both our application and tests configurable ensures they are always using the correct resources for their environment. This will allow us to deploy the exact same immutable image of our application to run our acceptance tests against as we will deploy to production.

1. Conditionally provision test infrastructure - There some extra pieces of infrastructure needed to acceptance test our application. We need to be able to conditionally provision these extra pieces as well as our test itself during an acceptance test.

1. Clean up resources - We need to be able to cleanly tear down all the resources we created for our ephemeral environment. We will use the `pulumi destroy` command to do this.

## Our Demo Application

To demonstrate the effectiveness of integrating acceptance testing with ephemeral environments into your deployment process, we created a simple demo application. The service is written in Go and accepts a message on the `/message` endpoint, then places it in a storage bucket and sends a notification about the new object on a PubSub topic.

## Our Pipeline

When developing a new service, it’s important that we establish a solid deployment strategy upfront. We want to make sure we're building in quality from day one. As we develop the service, we can add acceptance tests for each and every feature we add while the context and requirements are still fresh in our minds. This ensures we have thorough coverage of our app's functionality.

We used GitLab to set up our pipeline, which consists of four stages.

1. Test and Build - This runs our unit tests and builds both our application and acceptance test images. The application image is an immutable image that is used for both running our acceptance tests and deploying to production.
1. Acceptance Test - This is what spins up our ephemeral environments and runs our acceptance tests. This acts a quality gate catching issues prior to production.
1. Prod Pulumi Preview - This is what preview changes to our production infrastructure. We can incorporate this into our Merge Request review process, allowing us to validate our infrastructure changes are as we expect. Some teams may choose to start with this stage as manual gate and then switch to an automatic stage once they've built up confidence.
1. Prod Pulumi Up - This is what is actually performing our production deployment and only gets run on master.

## Recap

This is a great approach bc...
You need to make tradeoffs...
If you're interested in watching the presentation here it is:

{{< youtube "jAQhDZiRzBQ?rel=0" >}}
