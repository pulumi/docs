---
title: GreenPark Sports
description: |
    Pulumi enabled GreenPark Sports to empower its developers with self-service cloud infrastructure, allowing them to quickly and easily deploy Kubernetes clusters and contribute infrastructure code.
meta_desc: |
    Pulumi enabled GreenPark Sports to empower its developers with self-service cloud infrastructure through a “developer-first” approach.

customer_name: GreenPark Sports
customer_logo: /logos/customers/greenpark-sports-wordmark.png
customer_url: https://greenparksports.com/

exec_summary: |
    GreenPark Sports creates digital experiences and games for the new generation of sports and esports fans. To increase velocity, its platform team wanted to make cloud infrastructure self-service by empowering the company’s developers to build and deploy Kubernetes applications. However, GreenPark’s legacy infrastructure tool used a domain-specific language (DSL) that impeded adoption by developers. The platform team migrated to Pulumi so that it could build, deploy, and manage infrastructure with general-purpose languages (Go, Python, TypeScript/JavaScript, C#), enabling developers to easily provision and use cloud infrastructure for developing cloud applications. This increased development velocity because more developers could deploy updates faster and more frequently. Since GreenPark adopted Pulumi, every developer now uses Infrastructure as Code to deploy changes, up from only 30% before Pulumi. Developers have also increased cloud deployments by 70%.

sections:
    - label: Exec Summary
      anchor: executive-summary
    - label: Designing for Democratization
      anchor: designing-for-democratization
    - label: Why Pulumi
      anchor: why-pulumi
    - label: Migrating Infrastructure to Pulumi
      anchor: migrating-infrastructure-to-pulumi
    - label: Putting “Developers First” with Cloud Infrastructure
      anchor: putting-developers-first-with-cloud-infrastructure
    - label: Benefits
      anchor: how-pulumi-benefits-greenpark-sports
---

## Democratizing Cloud Infrastructure to Power Sports Fandom

### About GreenPark Sports

GreenPark Sports is a social gaming developer for next generation sports and esports fans.  Its mission is to bring global sports fans together to connect, compete, celebrate, and collaborate in a uniquely social and immersive experience. First launched in January 2021, the free to play mobile app now includes early gameplay within multiple fan universes, including the League of Legends Championship Series (LCS), LaLiga, and the National Basketball Association (NBA). The app also includes a blockchain digital collectible experience starting with its first non-fungible tokens (NFTs) which dropped in fall of 2021.

### Designing for Democratization

Jacob Foard is Tech Lead for the platform team at GreenPark, which is responsible for enabling backend and mobile engineers with cloud infrastructure. With a background in infrastructure from his previous role, he knew that any bottlenecks in his team would slow developers down and reduce velocity. That experience taught him that his main challenge at GreenPark would be to eliminate these bottlenecks so that developers could build faster and more independently.

Jacob sought to adopt a “developer-first” approach where developers are empowered to build and deploy cloud infrastructure and applications themselves. The platform team would enable this approach while adding guardrails to prevent failures and enforce security and compliance rules. However, this would be a challenge with GreenPark’s cloud architecture, which used containers orchestrated by Kubernetes. Since Kubernetes can be daunting for developers to deploy and configure, it would be difficult for the team to self-service using existing tools and approaches.

Initially, Jacob’s team used Terraform to manage its infrastructure as code. They attempted to train developers to use it to provision infrastructure on their own, using building blocks the team had created. However, this approach wasn’t successful because Terraform’s domain-specific language (DSL) was a barrier to adoption, with less than one-third of engineers using the tool. The developers were used to writing in Go, while Terraform required developers to learn a new language, HCL, and lacked many of the features and ease-of-use of standard languages. If developers couldn’t work with infrastructure code themselves, then Jacob’s vision would fail. He needed a better way.

### Why Pulumi

Jacob needed a platform that would make building, deploying, and managing cloud infrastructure easy for developers, and it also needed to support Kubernetes, the cloud native ecosystem, and SaaS vendors. GreenPark runs on Google Cloud Platform (GCP) and uses Kubernetes and fully managed services to run the backend for its game platform. It also uses best-of-breed SaaS providers such as DataDog, CloudFlare, and Confluent.

<img class="block mx-auto md:max-w-4xl my-8" src="/images/case-studies/greenpark-sports-deploy-diagram.png">
<p class="text-sm italic text-center">GreenPark developers deploy environments that typically include a Kubernetes cluster, Confluent Kafka cluster, a MongoDB Atlas database, and Cloudflare.</p>

Jacob had already heard about Pulumi, but a strong recommendation from a former coworker convinced him to take a closer look. He learned that one significant advantage of Pulumi is that it supports general-purpose languages like Go, Python, TypeScript/JavaScript, and C# (.NET). This would enable GreenPark developers to use infrastructure as code with languages and tools they already use on a daily basis, such as Go, Visual Studio, and test frameworks.

Pulumi would also enable Jacob to build, share, and reuse infrastructure code with the full benefits of a software supply chain. His team would be able to build higher-level components that make it easier for developers to build production-quality cloud applications. The components would be wrapper functions and helper functions written in Go, which developers could use to build and deploy a fully-configured Kubernetes application.

When recounting how he first started evaluating Pulumi, Jacob said, “I took a look at Pulumi and that started a much happier time in my life.”

### Putting "Developers First" with Cloud Infrastructure

After deciding on Pulumi, Jacob and his team built a system based on a “developer-first” approach. The system made developers as independent as possible by allowing them to provision cloud infrastructure, with guardrails to maintain security.

#### Migrating Infrastructure to Pulumi

First, the platform team [migrated](/tf2pulumi/) its infrastructure from Terraform to Pulumi. This included Kubernetes resources, Google Cloud resources, GitHub repos, DataDog, CloudFlare, Confluent for Kafka, Consul, and Vault. This enabled them to build, deploy, and manage all of their cloud and SaaS resources from a single platform, using Go as their language of choice.

<img class="block mx-auto md:max-w-4xl my-8" src="/images/case-studies/greenpark-sports-monorepo-diagram.png">
<p class="text-sm italic text-center">GreenPark Sports uses a monorepo to manage its infrastructure code.</p>

#### Simplifying Kubernetes Deployments

Pulumi also simplified how they manage Kubernetes deployments. It gave them a strongly-typed way of modeling Kubernetes resources with standard languages (e.g., Go) instead of YAML. Using Pulumi’s [native support for Kubernetes](/kubernetes), they could access 100% of Kubernetes’ APIs. They could also build and manage Helm charts and Kubernetes custom resource definitions with Pulumi’s cloud native integrations.

#### Building Reusable Cloud Infrastructure

Next, Jacob’s team built a set of [reusable Pulumi components](/docs/intro/concepts/resources/#components) in Go which developers could use to build and deploy new services without having to think about infrastructure configurations. Components abstract away infrastructure complexity, making them easy to consume. For example, Jacob’s team built a component in 8 lines of code representing a service with around 100 resources configured with best practices. When using the component, developers only needed to input a name for the service, the environment they’re running in, and a few other settings.

#### Empowering Developers to Self-Service with Infrastructure

Finally, Jacob’s team established a workflow that allows developers to independently deploy infrastructure. It also ensures that changes comply with company standards and security. In this workflow, all changes are managed through GitHub pull requests (PRs). If someone wants to deploy something new or an update, they create a PR and the platform team reviews the request. Using the Pulumi Service console, platform team members can visualize what resources will be created or changed. They can also view logs of past changes. If the PR is approved and merged, then the changes are built, tested, and deployed with GreenPark’s CI/CD workflow, which uses Flux CD and Bazel.

As a result, GreenPark increased Infrastructure as Code adoption from less than one-third of engineers to 100%. Engineers now also deploy 70% more changes than before Pulumi. It’s also straightforward for the platform team to onboard new developers to infrastructure. Jacob says, “Before Pulumi, the barrier to entry for developers using the cloud was high. Now, a developer can just call a function, just as they normally would. Infrastructure is now familiar because everything is in Go instead of HCL. Everything just works.”

### How Pulumi Benefits GreenPark Sports

Pulumi enabled GreenPark Sports to empower its developers with self-service cloud infrastructure through a “developer-first” approach. The benefits were:

- Grew Infrastructure as Code adoption from <1/3 of engineers to 100%, which is defined as anyone who makes changes to GreenPark’s infrastructure codebase.
- Increased the number of infrastructure deployments initiated by developers by 70% since adopting Pulumi.
- The platform team empowered developers to build and deploy cloud infrastructure on a self-service basis while still enforcing security and compliance.
- Everyone can build, deploy, and manage cloud infrastructure, Kubernetes, and SaaS providers with general-purpose languages (Go, TypeScript/JavaScript, Python, C#) and existing development tools (e.g. IDEs, test frameworks, package managers).
- Simplified Kubernetes deployments because the platform team can manage Kubernetes resources, custom resources, and Helm charts from a single platform using general-purpose languages like Go.
