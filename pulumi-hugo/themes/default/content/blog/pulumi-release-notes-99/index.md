---
title: "Pulumi Release Notes: Pulumi ESC, Deployments GA, MFA, AWS S3 Express One Zone Support, and more!"
allow_long_title: true
date: 2024-02-01T11:06:04-08:00
draft: false
meta_desc: The latest Pulumi updates include Pulumi ESC, Deployments GA, MFA, AWS S3 Express One Zone Support, and more 
meta_image: meta.png
authors:
    - arun-loganathan
    - justin-vanpatten
tags:
    - features
    - release-notes
---

We've had a busy last few months at Pulumi. From shipping a brand new product to Pulumi Cloud, to introducing several major features within Pulumi Cloud and updates to several Pulumi providers - we have them all. Check out [pulumi/pulumi repo](https://github.com/pulumi/pulumi/blob/master/CHANGELOG.md) changelog for CLI enhancements. As always, follow the [new features blogs](/blog/tag/features) to stay updated on the latest Pulumi Cloud features. Let's start with the major updates.

<!--more-->

- [AI](#ai)
  - [Deploy with Pulumi within Pulumi AI](#deploy-with-pulumi-within-pulumi-ai)
  - [Pulumi AI coverage and performance](#pulumi-ai-coverage-and-performance)
- [Pulumi Cloud](#pulumi-cloud)
  - [Pulumi ESC Preview](#pulumi-esc-preview)
  - [Developer Portal Gallery](#developer-portal-gallery)
  - [Deployments GA](#deployments-ga)
  - [Customer Managed Agents](#customer-managed-agents)
  - [MFA](#mfa)
  - [Pricing Calculator](#pricing-calculator)
  - [Historical Views](#historical-views)
- [Core](#core)
- [Providers and Packages](#providers-and-packages)
  - [AWS 6.0 to AWSX](#aws-60-to-awsx)
  - [Pulumi Google Cloud Classic 7.0](#pulumi-google-cloud-classic-70)
  - [AWS S3 Express One Zone Support](#aws-s3-express-one-zone-support)
  - [New Provider resources](#new-provider-resources)
  - [New Community Providers](#new-community-providers)
- [Wrap up](#wrap-up)

## AI

### Deploy with Pulumi within Pulumi AI

Pulumi AI's new feature enables [deploying cloud infrastructure using AI prompts](/blog/pulumi-ai-new). Users can rapidly generate and deploy templates through natural language inputs in 'pulumi new' CLI command and new project wizard, significantly streamlining the cloud setup process. Additionally, you now have the option to deploy the Pulumi AI generated Pulumi Programs from within [Pulumi AI]([/ai/](https://www.pulumi.com/ai)) and in the New Project Wizard in Pulumi Cloud console.

{{< video title="Pulumi new AI and deploy" src="../pulumi-ai-new/pulumi-new-ai.mp4" controls="false" autoplay="true" loop="true" >}}

### Pulumi AI coverage and performance

Pulumi AI can now write Pulumi programs for all 150 cloud providers in [Pulumi registry](https://www.pulumi.com/registry/) - up from 20 cloud providers. Pulumi AI has also been updated to OpenAI's GPT-4 Turbo for enhanced performance along with fine tuning of our prompts to improve our AI's ability to write code.

## Pulumi Cloud

### Pulumi ESC Preview

[Pulumi ESC](/docs/esc/) is our answer to the growing needs of our customers to manage secret sprawl and streamline config management. Pulumi ESC allows teams to store and aggregate secrets and configuration from various sources into a composable collection called an environment. You can dynamically generate [OIDC credentials](/docs/pulumi-cloud/oidc/aws/#pulumi-esc-1) from all three major cloud providers (AWS, Azure and GCP), and integrate with other [secrets managers](/docs/esc/get-started/retrieve-external-secrets/) like AWS Secrets Manager, Hashicorp Vault, Azure Vault and GCP Secret manager to pull secrets during runtime. Its hierarchical structure simplifies the composition and reuse of configurations, ensuring secure, auditable management and robust access control. [Get started](/docs/esc/get-started/) with Pulumi ESC

### Developer Portal Gallery 

We launched a new template gallery in the [New Project Wizard](/docs/pulumi-cloud/developer-portals/new-project-wizard), supercharging Platform teams to provision and distribute organization templates for their development teams to get up and running fast. Developers can generate Pulumi programs from these templates, commit and push code to GitHub and trigger deployment within the Pulumi Cloud console. The gallery supports three template types: Organization Templates for custom internal projects, Pulumi Templates authored by Pulumi to cover common architectural patterns and AI Generated Templates created through Pulumi AI. For more information, check out the full [blog post](/blog/developer-portal-gallery/).

{{< video title="Pulumi new AI and deploy" src="../developer-portal-gallery/gallery.mp4" controls="false" autoplay="true" loop="true" >}}

### Deployments GA

[Pulumi Deployments](/docs/pulumi-cloud/deployments) was made [generally available](/blog/deployments-ga) with new improvements such as support for [GitHub Enterprise](/docs/using-pulumi/continuous-delivery/github-app/#github-enterprise-server-support). Since launch, Pulumi Deployments has made infrastructure management at scale seamless for our customers, offering out of the box features such as [Review Stack](/docs/pulumi-cloud/deployments/review-stacks) and multiple deployment triggers.

### Customer Managed Agents

[Customer Managed agents](/blog/customer-managed-deployment-agents-launch/) for Pulumi Deployments enable customers with hard security and compliance requirements to take advantage of the powerful capabilities of Pulumi Deployments. By self-hosting the agents, you can host the agents anywhere within your infrastructure on any hardware and environment and meet compliance needs to keep the cloud provider credentials within your private network.

{{< video title="Pulumi new AI and deploy" src="../customer-managed-deployment-agents-launch/verify-setup.mp4" controls="false" autoplay="true" loop="true" >}}

### MFA

We now support [Multi-factor authentication](/blog/multi-factor-auth-mfa-in-pulumi-cloud/) to prevent unauthorized access, ensuring robust security. Organization administrators can now enable MFA for all members of the organization. At launch, MFA will only be available for Pulumi Cloud-backed users with support for time-based one-time passwords (TOTP).

### Pricing Calculator

[Pulumi cost calculator](/pricing/#calculator) for Team Edition enables you to quickly estimate the cost of using Pulumi Cloud. Simply input the number of resources in all your cloud accounts and the percentage of time they will be running to quickly get the total cost per month with a break down of estimated credits, free credits and cost per credit. You can also use the calculator to estimate the cost of using Pulumi Deployments.

![Screenshot of the pricing calculator](../pricing-calculator-blog/pricing_calc.png)

### Historical Views

Stack update page now contains the historical resources in the stack and the historical stack outputs. Simply click on details on each pulumi update to see the resource state and stack output at the time of the update. This history extends all the way back to the first update of the stack. See the [historical views](/blog/update-page-improvements/) blog post for more details.

![Historical views](../update-page-improvements/update-page.png)



## Core

Placeholder

## Providers and Packages

### AWS 6.0 to AWSX

We have launched [AWSx](https://www.pulumi.com/registry/packages/awsx/) 2.0, bringing all the benefits [AWS Classic 6.0](/blog/announcing-6-0-of-the-pulumi-aws-classic-provider/) to Pulumi Crosswalk for AWS (AWSx). The new versions offer several fixes and improvements, including support for the latest Terraform Plugin Framework, 56 new resources and 23 new functions for various AWS services.

[!AWS 6.0 vs 5.0 provider coverage](/blog/announcing-6-0-of-the-pulumi-aws-classic-provider/aws_api.png)

### Pulumi Google Cloud Classic 7.0

We have updated the [Pulumi Google Cloud Classic Provider](https://www.pulumi.com/registry/packages/gcp/) to reflect the latest developments from Google Cloud, including updates to existing resources and adding support for new resources, functions and input properties. One of the key update is the [fix](https://github.com/pulumi/pulumi-gcp/issues/722) for renaming of the Service Account resource for consistency and ease of use. We also made changes to align with [upstream changes](https://www.pulumi.com/blog/google-cloud-7-0/#:~:text=upstream%20documentation) to labels. Upgrading to this new version is straightforward. Check out our [blog post](/blog/google-cloud-7-0/) and [migration guide](https://www.pulumi.com/registry/packages/gcp/how-to-guides/7-0-migration/).

### AWS S3 Express One Zone Support

We [added support](/blog/amazon-s3-express-one-zone/) for [Amazon S3 Express One Zone](https://aws.amazon.com/s3/storage-classes/express-one-zone/), a new storage class offering up to 10X faster performance and reduced request costs by 50%. S3 Express One Zone is ideal for data-intensive applications such as AI/ML, HPC, etc. This update is part of our commitment to provide timely and effective support for the latest AWS offerings.

### New Provider resources

Placeholder

### New Community Providers

Placeholder

## Wrap up

That's a wrap on our latest Pulumi release notes! With each new feature and improvement, from AI advancements to enhanced cloud deployment tools, we're excited to see how you leverage these updates. Your [feedback](https://github.com/pulumi/pulumi-cloud-requests/issues/new/choose) is crucial in shaping our path forward. tay connected for more updates, and here's to building a more efficient cloud future together!
