---
title: Lykke
description: |
    Lykke worked closely with Pulumi to bring new applications to market and deploy infrastructure capabilities that help their developer team be more productive.
meta_desc: |
    Lykke worked closely with Pulumi to bring new applications to market and deploy infrastructure capabilities that help their developer team be more productive.

customer_name: Lykke
customer_logo: /logos/customers/lykke_logo.svg
customer_url: https://lykke.com/

exec_summary: |
    [Lykke](https://lykke.com/) is a Swiss fintech company bridging the gap between traditional finance and Blockchain. Lykke operates a commission-free exchange for digital assets and cryptocurrencies. Lykke developers rely on scalable blockchain infrastructure and leverage Pulumi to define reusable components and services and create abstractions needed to support its ecosystem of products.  Using Pulumi, Lykke has been able to rapidly lower the time-to-market for its services and deliver innovative new capabilities for the fast-growing cryptocurrency market, shipping its new product to production customers in a matter of months. Pulumi also helped Lykke adopt cloud-native architectures faster and migrate to managed services, which helped reduce costs by at least 20%.

sections:
    - label: Exec Summary
      anchor: executive-summary
    - label: About Lykke
      anchor: about-lykke
    - label: Challenges Faced
      anchor: challenges-faced
    - label: Results
      anchor: results
    - label: Next Steps
      anchor: next-steps
---

## About Lykke

Founded in 2013, Lykke received its initial funding in 2015 to bridge the gap between traditional finance and blockchain. The company builds on decades of research by its founder Richard Olsen, a pioneer in the field of high-frequency finance. Its vision is to provide a global marketplace where financial instruments can be traded and settled peer-to-peer with second-by-second interest payments. This open-source marketplace utilizes blockchain technology pioneered by Bitcoin to offer immediate settlement and direct ownership without transaction fees.

## Challenges Faced

Lykke originally built a monolithic stack with a wide variety of components. The engineering team wanted to adopt a serverless architecture and in April 2019, they decided to build a completely new infrastructure to support new applications - all without a dedicated ops team. To add to the complexity, the group needed to accurately model key parts of their infrastructure and create abstractions that would simplify scaling and make it accessible to both-back end and front-end engineers. This greenfield project was an exciting opportunity to select best-in-class solutions that worked well with their chosen cloud provider, AWS, and were compatible with their preferred engineering tools and frameworks -- React Native, .NET Core, and serverless architecture.

## Solution: Pulumi Modern Infrastructure-as-Code and Cloud Best Practices

Lykke engineering head Damian Hickey had been aware of Pulumi since the company launched in 2017 and decided to deploy the new infrastructure using [Pulumi's collection of libraries]({{< relref "/crosswalk/aws" >}}) that model AWS infrastructure patterns using well-architected best practices. This allowed him to design and manage infrastructure within his development team, rather than building a dedicated ops team. Pulumi's libraries also provided Lykke with built-in Well Architected patterns and best practices - helping the team move new applications into production faster.

With Pulumi, Damian’s team quickly set up their infrastructure without having to learn a new, proprietary programming language. In addition to creating their own abstractions, models, and best-practice files, Lykke was also able to take advantage of pre-built templates and libraries available right out of the box.

Lykke is now running multiple accounts with many core services each - all defined and managed with Pulumi. Pulumi allows the team to dynamically spin up instances through a single pull request within the stack and manage across multiple environments as needed.

## Results

One of the biggest considerations for the team was cost management. Pulumi helped Lykke adopt cloud-native architectures faster and migrate to managed services like Amazon Elastic Kubernetes Service (EKS) . This helped the Lykke team to run their services more efficiently, reducing costs by at least 20% and making their services more scalable.

Pulumi also helped the team to configure services like Amazon VPC using only a dozen lines of code - something that required 10x more configuration with other IaC tools. The code review process also became faster, with infrastructure changes taking hours, rather than days to deliver.

Within a month of adopting Pulumi, Lykke deployed core supporting infrastructure for a new product. By improving overall productivity for their development team, Lykke was able to deliver the new product to production customers in a matter of months. Lykke is also adopting a comprehensive approach to infrastructure policy using Pulumi’s [Policy as Code]({{< relref "/crossguard" >}}) framework. This ensures that internal security, compliance and cost management policies are automatically enforced through policy-as-code.

## Next steps

Lykke continues to work closely with Pulumi to bring new applications and services to market and deploy new infrastructure capabilities that help their developer team be more productive.

As their next step, the team is reviewing current workloads to optimize existing resources and spin down unused instances that can drive up operating costs. These unaccounted-for resources can easily overwhelm developer budgets and reduce Lykke’s ability to scale their business as they continue to expand their products and attract new customers.

Lykke’s engineering team also plans to adopt unit testing for existing and future infrastructure deployments, as well as explore additional security policies to set up approval and compliance checking for new IAM roles.

## About Pulumi

Pulumi’s cloud engineering platform brings infrastructure, developer, and security teams together through a unified software engineering process that tames cloud complexity and accelerates innovation. Using the Pulumi platform, teams can build, deploy, and manage modern cloud applications faster and with more confidence, using any language, any architecture and any cloud. Pulumi lets teams build Modern Infrastructure as Code using popular programming languages (Python, JavaScript, TypeScript, Go, .NET/C#). It enables deploying infrastructure and applications together through a unified delivery process. Finally, teams can manage cloud applications with Policy as Code, better visibility, and controls.

Check out the following articles to get started:

- [AWS Identity and Access Management with Pulumi]({{< relref "/docs/guides/crosswalk/aws/iam" >}})
- [AWS Lambda with Pulumi]({{< relref "/docs/guides/crosswalk/aws/lambda" >}})
- [Get Started with Pulumi Policy as Code]({{< relref "/docs/guides/crossguard/get-started" >}})
- [Get Started with Kubernetes with Pulumi]({{< relref "/docs/guides/crosswalk/kubernetes" >}})
