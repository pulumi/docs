---
title_tag: Materialize | Case Studies
title: Materialize Streamlines Multi-Region Kubernetes Operations
layout: case-studies
description: |
    Materialize uses Pulumi to manage multi-region Kubernetes, leading to better developer self-service and deployment consistency. 
meta_desc: Learn how Pulumi supports Materialize in operating multi-cluster Kubernetes environments at scale. 

customer_name: Materialize
customer_logo: /logos/customers/materialize.svg
customer_url:

quote_block:
  quote: |
      "Pulumi lets us manage multi-cluster Kubernetes infrastructure efficiently, all in one stack. It has hugely benefited productivity and our service's reliability. Without Pulumi, we know that scaling and maintaining Materialize would be much harder for the team."
  quote_attrib: Paul Hemberger, Engineering Manager, Materialize
  headline_stat: 75% more productivity
  headline: for new engineers; faster release cycles and growth

exec_summary: |
    Materialize, a cloud operational data store provider, implemented Pulumi's Infrastructure as Code platform to manage their multi-region Amazon EKS Kubernetes clusters, addressing key challenges in configuration consistency and developer accessibility. The solution enables developers to use familiar programming languages like Python for infrastructure management, while providing a custom CLI for self-service deployments and automated workflows through GitHub Actions. The implementation dramatically improved operational efficiency by reducing developer onboarding time from one month to one week, ensuring standardized cluster configurations across regions, and maintaining robust security governance through centralized control and pre-deployment validation.

sections:
    - label: Exec Summary
      anchor: executive-summary
    - label: Challenges
      anchor: infrastructure-challenges
    - label: Automation with Pulumi
      anchor: automated-infratructure-management
    - label: Benefits of Using Pulumi
      anchor: benefits
    - label: Conclusion
      anchor: conclusion
---

## About Materialize

[Materialize](https://materialize.com) is a cloud operational data store that can be queried using SQL. It's designed to make trustworthy, transformed data available throughout an organization, while that data is still fresh. Loan providers, fraud prevention services, and logistics and manufacturing firms use Materialize to ensure they're acting on the freshest data available.

Materialize’s cloud team operates the database as a SaaS service. The team is responsible for provisioning, orchestrating, and managing the cloud resources that run Materialize. The key operational priorities are security, reliability, and performance, as customers demand low-latency queries that are always ready to run.

Materialize runs all its deployments in Kubernetes using Amazon EKS. A multi-cluster architecture enables regional operations, but this increases complexity. It's critical that consistent configuration is applied across different clusters and regions, along with clear visibility into what's running and where.

## Database-as-a-Service Infrastructure Challenges {#infrastructure-challenges}

Operating across multiple regions requires Materialize to maintain numerous EKS clusters, including data plane clusters that serve the database to users and control plane clusters that manage operations and observability. Ensuring consistent configuration across this distributed infrastructure is crucial, as even minor discrepancies between environments could lead to complex operational issues. This necessitated an automated system capable of efficiently deploying changes across the entire cluster fleet.

The company's infrastructure needs are further complicated by its organizational structure, where the core database development team operates independently from the infrastructure group. Database developers require the ability to test their changes in environments that accurately mirror production settings, but without requiring deep expertise in Kubernetes or cloud infrastructure. This demanded a solution that would simplify cluster deployment while maintaining proper security controls.

Infrastructure reliability is paramount given Materialize's responsibility for multiple clusters, regions, and customer database instances. The team requires confidence that infrastructure changes will deploy correctly without triggering a service outage. Additionally, the cloud team must maintain robust security and governance standards across all environments to prevent misconfigurations, ensure compliance, and maintain appropriate access controls.

## Automated Infrastructure Management with Pulumi {#automated-infratructure-management}

Materialize implemented Pulumi as its infrastructure management solution from day one, driven by previous challenges with traditional Infrastructure as Code tools. The team had found that tools like Terraform required developers to learn proprietary configuration languages and unfamiliar concepts, creating unnecessary friction, delays and complexity in their development process.

The organization now runs its infrastructure management through a GitHub Actions workflow, utilizing a centralized monorepo overseen by the cloud team. This pipeline automates the provisioning and management of Amazon EKS clusters through Pulumi, ensuring the Materialize database service deploys into properly configured environments. To support developer productivity, the cloud team maintains a custom CLI tool that enables developers to launch staging deployments of their code changes. This CLI integrates with the standard Pulumi workflow to deploy releases into isolated Kubernetes clusters, replicating production-like configurations in development environments.

Materialize maintains a strict "no ClickOps" policy, relying on Pulumi to manage every aspect of their infrastructure. The team has expanded beyond Pulumi's built-in Amazon EKS components by developing custom Pulumi Providers to manage additional infrastructure components. This comprehensive approach to infrastructure automation has streamlined development processes, reduced learning curves, and enabled the cloud team to provide reliable "staging as a service" capabilities to their database engineers.

## Benefits of Using Pulumi {#benefits}

Using Pulumi to manage Kubernetes infrastructure has unlocked far-reaching benefits for Materialize. The company has been able to standardize its cluster configuration so it's easy for developers to maintain and is reliable in production.

> "Pulumi lets us manage multi-cluster Kubernetes infrastructure efficiently, all in one stack. It's hugely benefited productivity and our service’s reliability,"  
> "Without Pulumi, we know that scaling and maintaining Materialize would be much harder for the team."  
> --- Paul Hemberger, Engineering Manager for Materialize's cloud team

The decision to use Python as their infrastructure programming language has proven particularly beneficial. Developers leverage familiar tools within the Python ecosystem, including formatters, linters, and code quality scanners—capabilities that would be unavailable with traditional domain-specific language solutions. This familiarity accelerates the onboarding process for new engineers, who can typically begin contributing meaningful work within their first week. By ramping up new developers more quickly, Materialize has also improved engineer productivity, agility and time to market for its new product releases.

Pulumi effectively addresses Materialize's multi-cluster Kubernetes requirements through centralized configuration management. This approach eliminates environment discrepancies and ensures consistency between staging and production deployments.

Materialize sees the code quality advantages of Pulumi as a key part of its appeal. Unlike other IaC tools, Pulumi IaC code is easily organized in a way that's "consistent with how everyone thinks about code." This has enabled the team to maintain consistent code quality standards for its Pulumi stack, even as the project's grown in scale. Developer productivity has also improved through the custom CLI tool that provides on-demand production-live development environments.

The solution has also strengthened Materialize's governance and reliability measures. By channeling all infrastructure changes through a controlled repository and requiring explicit approvals, Pulumi helps prevent unauthorized modifications. The platform's preview functionality allows teams to assess potential impacts before implementing changes, significantly reducing the risk of misconfigurations affecting production systems.

Materialize team members have also experimented with Pulumi AI. The feature lets developers use LLM-powered natural language prompts to generate Pulumi IaC code for new infrastructure resources. Although Materialize doesn't use it day-to-day, they found it's useful for quickly generating simpler components.

Materialize has found value in Pulumi's comprehensive support system, which includes responsive technical assistance, detailed documentation, and active community forums. This robust support infrastructure, combined with Pulumi's technical capabilities, has validated Materialize's choice for managing their Kubernetes infrastructure as code.

## Conclusion

Pulumi has become integral to Materialize's infrastructure strategy, enabling comprehensive management of their Amazon EKS Kubernetes cluster fleet. Pulumi guarantees consistent configuration, clear oversight of changes, and continual compliance. As a result, Materialize's cloud team can confidently operate its powerful streaming database solution at scale.

The adoption of standard programming languages for infrastructure management has significantly enhanced developer efficiency compared to traditional IaC solutions. New team members can immediately comprehend and contribute to infrastructure code, minimizing the learning curve typically associated with specialized configuration languages.

Overall, using Pulumi for Kubernetes IaC has substantially optimized Materialize’s operating efficiency. Pulumi simplifies infrastructure management and ensures all resources run reliably, improving the customer experience for Materialize's enterprise database users.

### Key Points

* Pulumi lets Materialize onboard new cloud team members 75% faster—within one week, instead of an estimated month without Pulumi.
* Pulumi supports Materialize in operating multi-cluster Kubernetes environments at scale. It ensures cluster configurations are reproducible and simplifies the rollout of changes across the entire Amazon EKS fleet.
* Using Pulumi makes it clear which clusters and resources are going to be affected by a change, making Kubernetes operations safer and more reliable.
* Materialize especially values the ability to write infrastructure code in familiar programming languages like Python, making its IaC more readable and easier to understand.
