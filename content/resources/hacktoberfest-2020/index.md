---
meta_desc: Join Pulumi for Hacktoberfest and help us build open source
  integrations, automation and libraries.
title: Hacktoberfest 2020
subtitle: Help us build new open source capabilities for Pulumi
unlisted: true

aliases:
  - /events/hacktoberfest-2020

event:
  eventbrite_url: ""
  registration_url: https://organize.mlh.io/participants/events/4954-pulumi-hacktoberfest
  calendly_url: ""
  eventbrite_id: ""
  start_date: 2020-10-22
  time: 9:00 AM - 11:00 AM
  cost: $0
  end_date: 2020-10-23
  location: VIRTUAL
  type:
    - Hackathon
  description: Join the Pulumi team and members of the community as we hack new
    integrations, automation, and infrastructure libraries!
type: events
url_slug: hacktoberfest-2020
block_external_search_index: false
---
## About Hacktoberfest

Hacktoberfest® is open to everyone in our global community. Whether you’re a developer, student learning to code, event host, or company of any size, you can help drive growth of open source and make positive contributions to an ever-growing community. All backgrounds and skill levels are encouraged to complete the challenge.

This year, Pulumi is participating in Hacktoberfest with three areas where the community at large can collaborate to build new open source capabilities.

### Policy as Code

[Pulumi CrossGuard](https://www.pulumi.com/docs/guides/crossguard/) allows you to create policies for logic that you may want to enforce on your cloud resources as code. Policies are written as validation functions that are evaluated against all resources in your Pulumi stack. An example of this in practice is [AWSGuard](https://github.com/pulumi/pulumi-policy-aws), a library that codifies best practices for AWS.

Here are some helpful links to get you started with Policy as Code:

* [Crossguard Core Concepts](https://www.pulumi.com/docs/guides/crossguard/core-concepts/) - An in-depth guide to the core concepts for Policy as Code.
* [Example Policy Packs](https://github.com/pulumi/examples/tree/master/policy-packs) - Example policies for common cloud providers.
* [Configurable Policy Packs](https://www.pulumi.com/docs/guides/crossguard/configuration/) - A guide to authoring flexible Policy Packs that can be configured and reused.

### Automation API

The recently unveiled [Automation API](https://www.pulumi.com/blog/automation-api/) provides a robust programmatic layer on top of Pulumi's declarative Infrastructure as Software. By exposing Pulumi programs and stacks as strongly-typed composable building blocks, it means that Pulumi can now be fully embedded inside your software projects.

We've already seen the Automation API being used in incredibly creative ways, and we'd love to see what you dream up with it.

Here are some helpful links to get you started with the Automation API:

* [Go Documentation](https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/x/auto) - Go documentation for the Automation API.
* [TypeScript/JavaScript Documentation](https://www.pulumi.com/docs/reference/pkg/nodejs/pulumi/pulumi/x/automation/) - Typescript documentation for the Automation API.
* [Automation API examples](https://github.com/pulumi/automation-api-examples) - Examples of different Automation API use cases.

### Reusable Infrastructure Libraries

One of Pulumi's superpowers is that it allows you to easily create new abstractions and infrastructure building blocks in the form of [component resources]({{< relref "/docs/intro/concepts/resources#components" >}}). A component is a logical container for physical cloud resources and controls how resources are grouped in the CLI. In fact, some of our own libraries like [awsx](https://github.com/pulumi/pulumi-awsx) and [kx](https://github.com/pulumi/pulumi-kubernetesx) do just that by creating higher-level components (i.e. component resources) on top of the [pulumi-aws](https://github.com/pulumi/pulumi-aws) and [pulumi-kubernetes](https://github.com/pulumi/pulumi-kubernetes) providers respectively.

Here are some helpful links to get you started on authoring your own component resources:

* [Creating and Reusing Cloud Components using Package Managers](https://www.pulumi.com/docs/tutorials/aws/s3-folder-component/) - A step-by-step guide to building and publishing a `StaticWebsite` component.
* [AWS Lambda Warmer as Pulumi Component](https://mikhail.io/2018/08/aws-lambda-warmer-as-pulumi-component/) - An abstraction of a common pattern to avoid cold starts in AWS Lambda.
* Docker Image Component in [Typescript](https://github.com/pulumi/pulumi-docker/blob/master/sdk/nodejs/image.ts), [Python](https://github.com/pulumi/pulumi-docker/blob/master/sdk/python/pulumi_docker/image.py), [C#](https://github.com/pulumi/pulumi-docker/blob/master/sdk/dotnet/Image.cs) and [Go](https://github.com/pulumi/pulumi-docker/blob/master/sdk/go/docker/image.go) - An example in each supported language, so you can use what works best for you.
* [Pulumi Programming Model]({{< relref "/docs/intro/concepts/resources#components" >}}) - Documentation to understand the underlying concepts in a Pulumi program.

## How to get started

1. **[Register](https://hacktoberfest.digitalocean.com)** on the Hacktoberfest site for access to get credit for your open source contributions.
2. **[Join the Pulumi Community Slack](https://slack.pulumi.com)** and head over to the #Hacktoberfest channel.
3. **Recruit a team to work on your idea** - we'll pin a form on the #Hacktoberfest channel for you to register your team.
4. **Start hacking** - The Pulumi team will share tutorials on this page to help you get started during the hackathon.

## Schedule

**10/21/2020** - 9:00 AM PDT - Tutorial content shared on our #Hacktoberfest Slack channel

**10/22/2020** - 9:00 AM PDT - Kickoff and team formation

**10/23/2020** - 10:00 AM PDT - Team demos
