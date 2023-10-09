---
title: "How Starburst Data Creates Infrastructure Automation Magic With Code"
allow_long_title: true

# The date represents the post's publish date, and by default corresponds with
# the date and time this file was generated. Dates are used for display and
# ordering purposes only; they have no effect on whether or when a post is
# published. To influence the ordering of posts published on the same date, use
# the time portion of the date value; posts are sorted in descending order by
# date/time.
date: 2023-08-23

# The draft setting determines whether a post is published. Set it to true if
# you want to be able to merge the post without publishing it.
draft: false

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or
# social-media previews. This field is required or the build will fail the
# linter test. Max length is 160 characters.
meta_desc: Learn how Starburst Data built infrastructure automation into its data lake platform to ship more frequent updates to its customers with zero downtime.

# The meta_image appears in social-media previews and on the blog home page. A
# placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: meta.png

# At least one author is required. The values in this list correspond with the
# `id` properties of the team member files at /data/team/team. Create a file for
# yourself if you don't already have one.
authors:
    - george-huang

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
    - case-studies
    - kubernetes
    - cloud-native
    - automation-api
    - community
    - pulumi-events

# See the blogging docs at https://github.com/pulumi/pulumi-hugo/blob/master/BLOGGING.md
# for details, and please remove these comments before submitting for review.
---
{{% notes type="info" %}}
This blog post summarizes a presentation by Matt Stephenson at [PulumiUP 2023](/pulumi-up/).
{{% /notes %}}

[Matt Stephenson](https://github.com/mattstep) is Senior Principal Software Engineer for [Starburst Data](https://www.starburst.io) and a [Puluminary](/community/puluminaries/) member. He’s deeply involved in the [Infrastructure as Code (IaC)](/what-is/what-is-infrastructure-as-code/) space, having contributed to Ansible, been a core contributor to Apache jclouds, and has written many Terraform plugins. He leads infrastructure architecture at Starburst and originally introduced Pulumi to the company. Starburst provides a data lake analytics platform that’s powered by Trino - an open-source distributed SQL query engine designed for running fast analytic queries across large datasets in multiple data sources. At Starburst, Matt helped revamp and improve how the company manages its multi-cloud and cloud native infrastructure.

{{< youtube "t-oSFZuNqXQ?rel=0" >}}
Watch Matt Stephenson's full presentation with demos. 8:03 demo of CI/CD. 15:33 demo of infrastructure automation.

## Technical and Business Problems to Solve
Starburst operates a managed Trino service that runs on Kubernetes clusters on multiple clouds. Their Kubernetes clusters needed frequent manual scaling based on workloads. Furthermore, upgrading Trino versions running on the clusters ran the risk of potential service disruptions for customers. The company had been using tools like [Terraform](/docs/concepts/vs/terraform/) for IaC, Argo CD for deploying Helm charts, Maven, Docker containers, and a Slack bot for infrastructure and deployments. Their CI/CD workflow was difficult to maintain because they needed to create wrappers for their previous IaC tooling, making it less approachable in CI/CD environments. The pipeline was tenuously bound together using GitHub Actions and a Slack bot, requiring specialized GHA runners, leading to a messy architecture.

## Why Starburst Chose Pulumi
Recognizing opportunities for improvement, Matt brought in Pulumi and its [Automation API](/automation). This unified Starburst's software development and infrastructure management practices, especially when deploying and managing Trino clusters on [Kubernetes](/kubernetes). The top two reasons Matt chose Pulumi were:
* **Support for programming languages:** Pulumi supports the main languages used by Starburst’s developers, Java and TypeScript. This enables all engineers to write infrastructure code and promotes a cohesive application and infrastructure codebase.
* **Pulumi Automation API:** Automation API is a programmatic interface for the Pulumi CLI and Pulumi IaC engine, which enables Starburst engineers to build [infrastructure automation](https://github.com/pulumi/automation-api-examples) into their applications and CI/CD processes, and orchestrate complex provisioning workflows.

## Benefits of Using Pulumi
Adopting Pulumi and its Automation API provided several benefits that made Starburst’s engineers more efficient and productive, ultimately leading to faster and more reliable releases for Starburst’s customers. Matt summed up the benefits of Pulumi for Starburst’s engineers: "When I think about building an airplane, I think about precision and having the right tools for the job." Pulumi, for Starburst, epitomized this precision and efficiency.

**Increased deployment speeds by 3x for new customer releases:** Starburst engineers used the Pulumi Automation API to triple the deployment speed of multi-cloud Kubernetes clusters with blue-green deployments that complete within minutes. They did this by orchestrating blue-green updates across their data plane running on the clusters, ensuring zero customer downtime. They built intricate integrations between Pulumi and internal APIs that enabled them to seamlessly transition customers to new clusters. Now they can update their customers’ runtimes, including VPCs and Kubernetes clusters, twice a week.

**Unified cluster and infrastructure management:** Rather than juggling multiple tools for managing Kubernetes and infrastructure, Starburst engineers use a single tool to manage over 50 [Kubernetes clusters](https://www.pulumi.com/templates/kubernetes/) and [deploy Helm charts](https://www.pulumi.com/templates/kubernetes-application/helm-chart/) into the clusters, spanning multiple regions. They also use Pulumi to manage SaaS platforms like Cloudflare, Confluent, and DataDog.

**Consistent deployment lifecycles:** Using Pulumi’s [integration with GitHub Actions](/docs/using-pulumi/continuous-delivery/github-actions/), Starburst engineers built a streamlined CI/CD process where infrastructure and application code builds within the same pipelines with automated test environments. They accomplished this using Pulumi Automation API to abstract the underlying runtime environments, circumventing the need for additional layers and wrappers.

![Infrastructure automation code](https://www.pulumi.com/uploads/content/blog/how-starburst-data-creates-infrastructure-automation-magic-with-code/starburst-code.png)

## Try Pulumi for Infrastructure as Code Automation

[Sign up for a free account](https://app.pulumi.com/signup) to try deploying infrastructure on any cloud with [Pulumi Deployments](/docs/pulumi-cloud/deployments/), or [register for an upcoming workshop](https://www.pulumi.com/resources/#upcoming) to learn more about how Pulumi can help you ship cloud infrastructure faster and more safely.

[Go to more case studies &rarr;](/case-studies/)
