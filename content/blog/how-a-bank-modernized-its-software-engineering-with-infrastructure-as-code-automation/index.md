---
title: "How a Bank Modernized Its Software Engineering With Infrastructure as Code Automation"
allow_long_title: true
# The date represents the post's publish date, and by default corresponds with
# the date and time this file was generated. Dates are used for display and
# ordering purposes only; they have no effect on whether or when a post is
# published. To influence the ordering of posts published on the same date, use
# the time portion of the date value; posts are sorted in descending order by
# date/time.
date: 2023-08-03

# The draft setting determines whether a post is published. Set it to true if
# you want to be able to merge the post without publishing it.
draft: false

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or
# social-media previews. This field is required or the build will fail the
# linter test. Max length is 160 characters.
meta_desc: Digital transformation in Financial Services. Learn how Washington Trust Bank modernized with infrastructure as code automation.

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
    - azure
    - fintech
    - case-studies
    - enterprise
    - crossguard
    - policy-as-code

# See the blogging docs at https://github.com/pulumi/pulumi-hugo/blob/master/BLOGGING.md
# for details, and please remove these comments before submitting for review.
---
{{% notes type="info" %}}
This blog post summarizes a presentation by Dennis Sauvé at [PulumiUP 2023](/pulumi-up/).
{{% /notes %}}

[Washington Trust Bank](https://www.watrust.com), the largest independently-owned full-service commercial bank in the Northwest, has served personal, private, commercial and wealth management clients throughout the region since 1902. It has assets exceeding $11 billion and currently has 42 branches and offices in Idaho, Oregon, and Washington. 

As an FDIC-governed financial institution, it is imperative for the bank to maintain secure, reliable, and compliant cloud resources to protect clients’ personal data. On the other hand, it also aimed to create more agile development teams as it modernized its software development and infrastructure. [Dennis Sauvé](https://github.com/dengsauve), the bank's first DevOps Engineer, recognized [Infrastructure as Code (IaC)](/what-is/what-is-infrastructure-as-code/) as the solution to these challenges. 

Embracing an Infrastructure as Code approach would allow them to automate building and deploying their cloud infrastructure, eliminate infrastructure provisioning as a bottleneck, and empower developers to self-service infrastructure and increase productivity.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Q63ZaX340M4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Background

The main challenge was managing Azure infrastructure in an efficient and secure way that kept pace with the bank's rapid growth. Previously, they ran on-premise infrastructure and deployed with BAT and Powershell scripts. Now, they had migrated to Azure and wanted to increase development speed through CI/CD for cloud infrastructure. 

In addition, cloud resources' security and reliability were paramount. They needed a way for the infrastructure and information security teams to work together to implement security best practices for infrastructure, including how to prevent insecure resources from being provisioned. 

The bank decided to adopt IaC to create reliable and rapid deployments while ensuring that its cloud infrastructure stayed compliant and secure.

## Why Washington Trust Bank Chose Pulumi

The bank evaluated several options, including [Terraform](/docs/concepts/vs/terraform/) and Azure Bicep. However, Pulumi stood out due to its versatility, support for multiple clouds and [native Azure support](/blog/introducing-azure-native-v2/), and the ability to write IaC in the bank's preferred language, TypeScript. The ease of using Pulumi with GitHub, its ability to be used in conjunction with Azure CLI, and its comprehensive [support for CI/CD](/docs/using-pulumi/continuous-delivery/) through GitHub Actions were also compelling factors.

Dennis praised Pulumi, saying, "_Pulumi was exactly the Swiss Army Knife versatility we were looking for. We've only uncovered more of what we love about Pulumi as our relationship has evolved._"

## Benefits of Using Pulumi

Pulumi helped Washington Trust Bank improve efficiency by maintaining its infrastructure in code, promoting the security of its infrastructure, and accelerating development speeds. It automated deployment of web services for its development teams, data management tools for its business insights team, and orchestrated its entire hub-and-spoke cloud architecture.

### Improved Development Speed with Reusable Infrastructure Packages and CI/CD

Pulumi's automation capabilities played a transformational role. By freeing the infrastructure team from handling manual deployments, it could focus on improving developer productivity. The team created reusable and repeatable [infrastructure components](/docs/concepts/resources/components/) built around strict IT security standards in the form of Frazure, an internal NPM package. 

Frazure allows the bank’s developers to easily provision out-of-the-box resources for cloud services and covers the necessary Azure resource groups, vnets, and other resources. The package encapsulates best practices, such as how resource groups and their virtual networks can be created, including subnet IP spaces, peerings to and from the hub virtual network, user-defined routes and more. 

To deploy, developers open a pull request which kicks off a [CI/CD pipeline in GitHub Actions](/docs/pulumi-cloud/deployments/ci-cd-integration-assistant/) and provisions testing environments and tests. Once the PR is reviewed and approved, the changes are automatically deployed to staging and live environments. This automated process enabled the bank to accelerate the building, testing, and deployment of new applications, translating into rapid value delivery to their customers.

### Safeguards for Infrastructure

Pulumi also gave the bank total confidence in being able to rapidly recover its cloud infrastructure in the case of a failure in Azure. The integration of Pulumi with GitHub Actions provided the team with a precise delta of changes to be made to the environment. Coupled with mandatory reviews from InfoSec and infrastructure, this significantly reduced the likelihood of deploying unapproved changes, thereby enhancing the reliability of their deployment processes.

###  Policy as Code Guardrails with Pulumi CrossGuard

[Pulumi CrossGuard](/docs/using-pulumi/crossguard/) adds an extra layer of security and control and is used in conjunction with Azure Policies, which are used for auditing purposes. CrossGuard prevents the deployment of undesired, insecure, or expensive resources during the preview and deployment stage, thus preventing developers from even reaching Azure to provision resources. Custom error messages give developers context on why their deployment was not allowed. 

[Pulumi Cloud Policy Packs](/docs/using-pulumi/crossguard/configuration/) allow them to group and deploy many policies simultaneously. The Policy Packs prevent specified resources from being deployed into staging and live environments. For example, one policy requires all SQL databases to use TLS 1.2 by default and another ensures all storage buckets have public access disabled by default. These capabilities helped bolster the security of the bank's cloud infrastructure.

## Financial services cloud modernization with Pulumi 

The DevOps and development teams at Washington Trust Bank rely on Pulumi as a key tool in their cloud modernization, while maintaining high security and quality standards. Pulumi played a vital role in streamlining their cloud infrastructure management, enabling their developers to be more productive, and improving the security and reliability of its cloud infrastructure.

[Sign up for a free account](https://app.pulumi.com/signup) to try deploying infrastructure on any cloud, or [register for an upcoming workshop](https://www.pulumi.com/resources/#upcoming) to learn more about how Pulumi can help you ship cloud infrastructure faster and more safely.

[Go to more case studies](/case-studies/)
