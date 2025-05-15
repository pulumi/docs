---
title: "Announcing Pulumi IDP: Platform Engineering Accelerated"
date: 2025-05-06
draft: false
meta_desc: "Introducing Pulumi IDP: Build self-service infrastructure workflows with golden paths to boost dev productivity, unify components, and scale securely."
meta_image: meta.png

authors:
    - idp-team
    
tags:
    - idp
    - platform teams
    - internal developer platform
    - features
    - releases

social:
    twitter: "TODO"
    linkedin: "TODO"
---

Today, we’re excited to introduce Pulumi IDP (Internal Developer Platform), the latest evolution of the Pulumi Cloud Platform, designed to help organizations automate, secure, and manage everything they run in the cloud.

<!--more-->
{{< blog/cta-button "Get Started with Pulumi IDP" "/docs/idp/get-started/" >}}

For the past eight years, we’ve helped organizations simplify the deployment and management of their infrastructure. Pulumi launched at the height of DevOps, bringing general-purpose programming languages to infrastructure as code (IaC) at a time when application teams were often manually deploying their own infrastructure. Users were instantly hooked on the ability to leverage familiar programming paradigms to manage their infrastructure.

As we evolved, we introduced additional products to meet the needs of an expanding user base. We launched Pulumi Components to increase standardization and reuse across any programming language. We launched [Pulumi CrossGuard](https://www.pulumi.com/crossguard/) to codify policy as code and ensure compliance at scale. And last fall, we made [Pulumi ESC](https://www.pulumi.com/product/secrets-management/) and [Pulumi Insights](https://www.pulumi.com/product/pulumi-insights/) generally available to help tame secret sprawl and better manage all your cloud infrastructure.

At the same time that Pulumi was evolving, so too was the industry. DevOps ushered in a new way of shipping and maintaining software, but for many organizations, it brought about tool sprawl and Day 2 pain. These lessons learned, along with others, have led to the emergence of platform engineering and platform teams, which build tools and workflows that enable their internal users to provision infrastructure and deploy software.

## Platform Teams

The goal and promise of platform teams are to understand the needs of their users, creating scalable workflows to provision and maintain secure, compliant, and reliable infrastructure through Internal Developer Platforms without being blocked by other teams or having to maintain it themselves.

However, Platform teams have faced a harsh reality – offering flexible golden paths that account for security, compliance, and maintainability is inherently difficult. Most platform teams – especially in enterprises – must also build for multiple personas with varying consumption methods, from writing their own IaC code to point-and-click deployments.

Without establishing a foundation of standardized, reusable primitives that can be consumed in multiple ways, platform teams will stay trapped in a cycle of trying to build everything for everyone.

## Pulumi IDP

Pulumi IDP is a bottom-up framework that integrates with the entire Pulumi product suite, enabling platform teams to build and manage self-service workflows based on codified golden paths. We have launched a suite of new features and invested in existing ones to make the Day 0 through Day 2 experience of operating infrastructure seamless.

* Day 0: Establish a source of truth for standardized infrastructure building blocks that can be consumed in any workflow.
* Day 1: Provision infrastructure through flexible workflows based on standardized building blocks.
* Day 2: Establish context, gain insights, and perform operational tasks.

## Private Registry as the Source of Truth

The foundation of Pulumi IDP is the Pulumi Private Registry, the source of truth for private components, templates, providers, and policies.

Pulumi has long focused on enabling organizations to author reusable infrastructure building blocks. We recently introduced the [latest generation](/blog/pulumi-components/) of Pulumi components for encapsulating and reusing resources across programming languages. Reusable packages offer tremendous benefits, but significant pain points have also emerged:

* Discoverability: Once authored, teams often store packages in Git, but in most organizations, especially enterprises, they quickly become invisible. If no one can find packages, they won’t reuse them, and teams will write one-off solutions instead.

* Lifecycle Management: Organizations that are able to drive discovery and adoption encounter Day 2 issues, such as a lack of usage insights, performing updates, and more.

The Pulumi Private Registry was built to solve these issues and more. With a single `pulumi publish` command, platform engineers can ensure their standardized building blocks are discoverable from a central location. Their end-users can discover the packages available, explore README files, consume automatically generated API documentation, and learn about installing and using the package.

![Pulumi IDP Templates](registry-main.jpg)

Driving standardized component and template utilization through the registry also provides valuable usage insights for lifecycle management. Platform engineers can see where each package or template is used and at which version – critical for assessing the impact of changes and tracking version drift.

![Pulumi IDP Insights](registry-insights.jpg)

## Flexible Self-Service Workflows  

To ensure that users can consume packages and templates ergonomically, we’re introducing new flexible workflow tools to meet the needs of any persona.

Platform teams can exhaust themselves with designing, codifying, and publishing standardized patterns, but if they are not easily consumable, they won’t be used. Platform teams are often tasked with accommodating a spectrum of personas, ranging from users who want to scaffold infrastructure through components to non-technical users who want to point and click to deploy from a template. Each of their needs is valid, but the adage “designing for everyone means designing for no one” can quickly take effect.

With Pulumi IDP’s bottom-up approach, this isn’t an issue. The same standardized, secure, and compliant packages and templates published in a private registry are the same ones that power self-service workflows.

### No-Code

In no-code workflows, users can instantly create and deploy Pulumi programs without worrying about the underlying IaC code or stack configuration. The no-code workflow is built on Pulumi organization templates and stores stack config in Pulumi ESC, eliminating the need to write to a VCS like GitHub or GitLab. By storing config in Pulumi ESC, developers can also edit config on-demand and instantly redeploy.

### Low-Code

Users often need to compose their own Pulumi programs, but platform engineering teams want to ensure they use approved components. With the new Pulumi Private registry and the latest generation of Pulumi components, that’s never been easier.

Platform engineers can author and publish components in any language. Users can then discover the available components through the private registry, add them as dependencies in a Pulumi YAML program, and deploy the infrastructure.

### Full-Code

In some organizations, platform engineers want to offer application teams a starting point without dictating how they deploy infrastructure. Templates are now available from the Pulumi CLI to facilitate a local workflow. Application developers can scaffold infrastructure using the same templates available from the private registry directly from the convenience of their terminal.

For instances where a Pulumi program is written from scratch, the suite of Pulumi IaC languages is always nearby, with the ability to easily incorporate components to accelerate development.

## Organizational Context through Services

After you define and deploy infrastructure, you need to manage it, and that’s easier when it reflects your organization’s context. To make this possible, we’re introducing Pulumi Services.

Services enable teams to logically group stacks, environments, and resources, creating representations that are familiar within their organization. The service’s entities can live anywhere in Pulumi – across IaC and ESC projects or in different Insights Accounts.

![Pulumi Services](services-home.jpg)

Services also support properties – metadata that adds important context to a service, such as links to observability dashboards, Slack channels, and more.

![Pulumi Services - Details Page](services-details.jpg)

## A New Era for Platform Teams

Ready to accelerate your platform engineering journey? [Get started with Pulumi IDP today](/product/internal-developer-platforms/) and explore our comprehensive [documentation](/docs/idp/get-started/) to learn how to build self-service infrastructure workflows, establish golden paths, and boost developer productivity. Join the growing community of platform engineers who are transforming how their organizations deliver and manage cloud infrastructure at scale.
