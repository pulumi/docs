---
title_tag: Aptos Labs | Case Studies
title: "Aptos Labs Transforms Development Process"
description: |
    Aptos Labs used Pulumi to transform development, increasing velocity by up to 10X while improving security, compliance, and cost control.
meta_desc: Aptos Labs used Pulumi to transform development, increasing velocity by up to 10X while improving security, compliance, and cost control.

customer_name: Aptos Labs
customer_logo: /logos/customers/aptos.png
customer_url: https://aptoslabs.com/

exec_summary: |
   Aptos Labs, the creator of the Aptos blockchain, partnered with Pulumi in 2022 to transform their development process and replace Terraform. By adopting Pulumi's cloud engineering platform, Aptos Labs increased development velocity by up to 10X, improved security, compliance, and cost control, and empowered developers to use their preferred programming languages. Pulumi's professional services team migrated Aptos Labs' existing Terraform code, configured the Aptos landing zones for AWS and Google Cloud, and set up Kubernetes clusters and serverless functions. Aptos Labs is now positioned for greater efficiency and scalability, with plans to further modularize projects using Pulumi to reduce complexity, increase code reuse, and enhance flexibility across different cloud environments.

sections:
    - label: Exec Summary
      anchor: executive-summary
    - label: Migration
      anchor: migrations
    - label: Benefits
      anchor: benefits
    - label: Next Steps
      anchor: next-steps

aliases:
    - /case-studies/aptos-labs
---

## About Aptos Labs

Aptos Labs, co-founded by Mo Shaikh and Avery Ching, is dedicated to creating better network tooling and seamless usability to bring the benefits of decentralization to the masses. Having now raised over $400M, Aptos Labs is backed by top-flight investors, including a16z, Jump Crypto, Binance Labs, Dragonfly, PayPal Ventures, Andreessen Horowitz and Franklin Templeton Investments. Learn more at: https://aptoslabs.com/

## Migrating Away from Terraform {#migration}

> **By making the switch from Terraform, Aptos Labs increased the pace of development by as much as 10X**

Pulumi's partnership with Aptos Labs began in 2022 with a small initial deployment in an otherwise Terraform-enabled environment. With Pulumi, the Aptos Labs infrastructure team was able to support a rapidly growing team of engineers and projects as they delivered critical services to their retail customers around the globe.

Encouraged by their success, the Aptos Labs team elected to replace their existing IaC tool, Terraform, with the Pulumi cloud platform to gain greater efficiency across their development team. Aptos Labs' challenge was completing the migration while seamlessly supporting the Aptos network, a next-generation Layer 1 blockchain. Pulumi's professional services experts stepped in to accelerate the migration of Aptos Labs’ Terraform code to Pulumi.

In addition to helping Aptos Labs achieve significant developer velocity gains, switching to the Pulumi's cloud platform meant Aptos Labs was able to spend more time on value-generating product development.

> “Terraform was slowing down our growing team of software engineers,” says Christian Theilemann, Staff Software Engineer at Aptos Labs. “Switching to Pulumi for our IaC needs helped us massively accelerate development velocity by increasing the level of automation and making infrastructure maintainable by every software engineer, not just the infrastructure team.”

The migration to Pulumi accelerated development at Aptos Labs and refocused their engineering team on writing and shipping differentiated code while spending less time on maintenance and duplicate efforts. Pulumi has made it easier for internal and external engineers to engage with infrastructure as code in the language of their choice, further accelerating development.

## Benefits of the Pulumi Platform {#benefits}

As part of migrating to Pulumi, the professional services team converted 13 modules at Aptos Labs across dev, test, and production environments for multiple cloud providers. The team used Pulumi to configure all aspects of the Aptos Labs landing zone for AWS and Google Cloud accounts including IAM roles, VPCs, DNS, secrets management, container registries, compute, and storage accounts. They also used Pulumi for advanced Kubernetes management including setting up Google Kubernetes Engine (GKE) clusters and configuring networking and observability for each cluster.

The team configured multi-cloud serverless capabilities such as Google Cloud Functions and Google Cloud Run.

In addition to documenting the migration, the Pulumi team provided import automation and patterns to streamline the transition from Terraform to Pulumi. This approach significantly reduced the need to recreate critical resources and accelerated the import process.

The developers at Aptos Labs reported higher satisfaction with the Pulumi platform than alternative approaches. They also shared that Pulumi helped enforce policies and best practices across their security and cost attribution centers without adding friction.

**Making the switch to Pulumi helped advance Aptos Labs' infrastructure journey in the following ways:**

1. Teams are shipping code faster: Aptos Labs engineers can now prioritize building business value over managing cloud resources using domain-specific code, thanks to Pulumi's streamlined approach.
2. Developers are enabled in their language of choice: The move to Pulumi allows the developers to use their preferred programming languages, promoting better software engineering practices like encapsulation and DRY (don’t repeat yourself) principles.
3. Improved development practices and collaboration: Integrating infrastructure management with standard software development techniques enhances code quality and collaboration.

## Removal of Terraform Dependency

With the successful migration from Terraform to Pulumi, Aptos Labs gained access to a more robust and flexible toolset. As a result, Aptos Labs is well-positioned to achieve a more efficient, scalable, and modern infrastructure management approach. Aptos Labs has also allowed engineers to reduce the cognitive burden of understanding a domain-specific language and work in the languages used for critical business functions. With Pulumi, Aptos Labs can now build usable and shareable software abstractions that encapsulate best practices for cloud infrastructure.

## What's Next for Aptos Labs? {#next-steps}

Aptos Labs and Pulumi plan to build on this success to advance improvements in their infrastructure management even further. These efforts will continue to optimize the structure and management of projects at Aptos Labs to achieve greater efficiency, scalability, and consistency.

### Modularization of Projects

Aptos Labs' projects are structured to combine multiple concerns within a single stack. This approach results in managing network, cluster, and application-specific resources together, leading to complexities, redundancies, and excess costs.

For example, by separating Network, Cluster, and Application Resources into distinct, independent projects, Aptos Labs can streamline management and enhance clarity. Further, Aptos Labs can leverage Pulumi components and transformations to create a modular, cloud-agnostic infrastructure by adopting cloud-agnostic modularization. This approach enables the development of infrastructure code that is both reusable and adaptable to different cloud environments. Aptos Labs can efficiently manage cloud-specific resources and configurations by maintaining a core set of common code and employing feature flags. This strategy ensures minimal changes are required when adapting the infrastructure to different cloud providers, enhancing maintainability and scalability.
