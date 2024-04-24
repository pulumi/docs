---
title: "New Pulumi Deployments Free Tier for Everyone: Automate Your Infrastructure Workflows"
allow_long_title: True
date: 2024-04-24T07:00:01-08:00
draft: false
meta_desc: Pulumi enhances its Deployments feature to offer free minutes, making it easier for customers to test and adopt cloud infrastructure management solutions.
meta_image: deployments-free-tier.png
authors:
    - meagan-cojocar
tags:
    - features
    - infrastructure-lifecycle-management
---

At Pulumi, we are committed to empowering developers and infrastructure teams with the tools they need to efficiently manage cloud resources at scale. As part of our ongoing efforts to enhance user experience and ease of use, we are excited to share some significant updates to Pulumi Deployments pricing, making it easier for _all_ customers to experiment with and adopt the easiest way to go from code to cloud. 

Starting today, all paid Pulumi Cloud organizations get 3,000 minutes per month of Pulumi Deployments included with their Pulumi Cloud subscription.

Paired with the launch of [Drift Detection and Remediation](/blog/drift-detection), [Time-to-Live Stacks](/blog/ttl) and [Scheduled Deployments](/blog/scheduled-deployments) - it has never been easier to kick the tires on the latest and greatest tools for [infrastructure lifecycle management](/blog/infrastructure-lifecycle-management).

## Introduction to Pulumi Deployments

[Pulumi Deployments](/docs/pulumi-cloud/deployments) is a fully managed platform designed to empower teams to efficiently manage and scale their cloud infrastructure. Whether you are just getting started in the cloud and want the easiest path to set up secure CI/CD, or are a platform engineer building a self-service platform to support thousands of engineers, Pulumi Deployments provides you with the building blocks that enable you to scale your cloud footprint without scaling your headcount. It offers a fully managed, secure, and elastic compute environment for running infrastructure deployments. It simplifies configuration by centralizing the management of source code, cloud credentials, and other necessities at the stack level. Additionally, the platform supports a variety of deployment triggers such as [REST API](/docs/pulumi-cloud/deployments/api), [Git Push to Deploy](/docs/pulumi-cloud/deployments/reference/#github-push-to-deploy), and [Click to Deploy](/docs/pulumi-cloud/deployments/reference/#click-to-deploy), allowing users to customize and automate their cloud operations beyond the capabilities of traditional CI/CD systems. When a stack is managed with Pulumi Deployments, richer Pulumi Cloud functionality is supported, such as [Review Stacks](/docs/pulumi-cloud/deployments/review-stacks) and Click to Deploy templates in the New Project Wizard.

## Exciting New Features

### Drift Detection

Stay on top of your infrastructure's health with our new [Drift Detection](/docs/pulumi-cloud/deployments/drift-detection) feature. Drift Detection helps you monitor and rectify discrepancies between your desired infrastructure state and the actual state, ensuring consistency and compliance.

### TTL Stacks

Manage resources effectively with [Time to Live (TTL) Stacks](/docs/pulumi-cloud/deployments/ttl-stacks). This feature automatically deallocates resources after a set period, perfect for temporary or experimental deployments, reducing costs and manual cleanup efforts.

### Scheduled Deployments

Optimize your deployment strategy with [Scheduled Deployments](/docs/pulumi-cloud/deployments/scheduled-deployments). This feature allows you to plan and execute deployments at specific times, making it easier to manage updates during off-peak hours, minimizing impact on your services.

## Pulumi Deployments for Everyone

To help ensure all Pulumi Cloud users can get started with Pulumi Deployments, we are introducing an updated allocation model for deployment minutes. Now, all customer tiers—Team, Enterprise, and Business Critical—will receive 3,000 free deployment minutes each month. This change allows our users to test and leverage Pulumi Deployments without upfront commitments or the need to engage in lengthy procurement processes. The table below shows the Pulumi Deployments dimensions (both pricing and limits) by tier, more details can be found on our [pricing page](https://www.pulumi.com/pricing/).

| Dimension               | Individual | Team        | Enterprise  | Business Critical |
|-------------------------|------------|-------------|-------------|-------------------|
| Minutes Included        | 500/month  | 3000/month  | 3000/month  | 3000/month        |
| Cost per minute         |            | $0.01 | Starts at $0.01 | Starts at $0.01   |
| Concurrency Limit       | 1          | 5           | 25          | 150               |
| Self-hosted Deployment Runners | Available  | Available   | Available   | Included         |

## Looking Forward

As a core part of Pulumi Cloud, Pulumi Deployments is now easier to adopt in your organization. We expect to release even more rich features built on Pulumi Deployments, offloading the time consuming work to Pulumi Cloud with turn-key features to solve your existing pain points.

We can't wait to hear any feedback on this new set of features and Pulumi Deployments as a whole!
