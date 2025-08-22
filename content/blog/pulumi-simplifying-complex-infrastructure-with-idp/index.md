---
title: "Using IDP to Simplify Complex Infrastructure"
h1: "Using IDP Templates to Simplify the Deployment of Complex Infrastructure: An Example with Pulumi's EKS Self-hosted Installer"
authors: 
  - "elisabeth-lichtie"
tags: ["idp", "pulumi", "eks", "aws", "infrastructure-as-code", "platform-engineering"]
meta_desc: "How to use Pulumi’s Internal Developer Platform (IDP) to encapsulate complex infrastructure logic behind simple, reusable YAML templates."
date: "2025-08-23"
meta_image: "Self-Hosted with IDP.png"

summary: |
  This approach to using Pulumi Internal Developer Platform (IDP) gives developers the flexibility they need in language and logic while presenting end users with a simple, abstracted YAML template. This post details Pulumi’s complex self-hosted EKS installer redesigned as a modular system built with IDP components and templates. Leveraging IDP this way preserves developer flexibility behind the scenes, while templates are easily delivered and deployed through the Pulumi UI or CLI—providing platform users with a clean, repeatable, and simplified deployment experience.
---

This approach to using Pulumi Internal Developer Platform (IDP) gives developers the flexibility they need in language and logic while presenting end users with a simple, abstracted YAML template. This post details Pulumi’s complex self-hosted EKS installer redesigned as a modular system built with IDP components and templates. Leveraging IDP this way preserves developer flexibility behind the scenes, while templates are easily delivered and deployed through the Pulumi UI or CLI—providing platform users with a clean, repeatable, and simplified deployment experience.

## The Approach

{{% notes type="info" %}}
See the full repositories for the [components](https://github.com) and [templates](https://github.com) for more details
{{% /notes %}}

Our example refactors Pulumi's [self-hosted EKS installer](https://github.com/pulumi/pulumi-self-hosted-installers/tree/master/eks-hosted) to provide a simple end-user template while abstracting away the complex infrastructure and logic into components. By creating componentized templates, we can enable flexible consumption patterns.

This approach enables each team to work at their optimal level of abstraction for appropriate flexibility and clarity at each level:

**Developers** create components with complete flexibility, choosing their preferred programming language and implementing whatever business logic and resources they need. In this example, features like ESC, Insights, Policies, and the Pulumi Cloud Service are components that can be abstracted to expose key configuration parameters in a clean interface.

**Platform teams** combine developer-created components with foundational infrastructure into cohesive templates. They define the underlying infrastructure — IAM roles, network topology, EKS clusters, and databases — choosing the right abstraction level for their end users. In this example, the EKS cluster, VPC, and database components are fully componentized for simplicity, but you can choose to define these in the template directly or import them as a stack reference depending on the technical sophistication and customizability needs of the end user.

**End users** consume simple YAML templates that hide underlying complexity. Instead of managing dozens of configuration files and understanding intricate dependencies, they see a clear interface with clear documentation: "I'm deploying these five features and the network infrastructure to run them." In this example, users might configure domain names, resource sizing, and feature toggles while the template handles EKS setup, networking configuration, and service deployment automatically.

This layered pattern simplifies complex infrastructure deployment into a form-based experience while preserving the flexibility platform teams need to maintain, secure, and evolve their infrastructure. In this example, what was once a complex multi-step EKS installation becomes a simple template deployment with clear parameters and automated infrastructure provisioning.

## Motivation and Use Cases

### Providing self-hosted applications to third parties

The primary motivation for this approach is delivering complete applications to third parties for self-hosting in their own environments. This is particularly valuable for enterprise software vendors, SaaS companies offering private cloud deployments, or organizations providing complex applications to customers who require on-premises installations.

In our EKS installer example, this means providing customers with a complete Pulumi Cloud deployment they can run in their own AWS accounts. Rather than requiring customers to understand EKS configuration, networking topologies, database setup, and service orchestration, they receive a simple template that handles all complexity behind the scenes.

This approach supports multiple deployment patterns. In our EKS installer example, we use **self-service deployment**: customers add the components to their own IDP and deploy using their existing Pulumi workflows, maximizing autonomy while preserving organizational standards.

However, if you're providing infrastructure to your own customers, you may choose alternative patterns:

**User-managed deployment**: Customers deploy in a provider-managed account using their own cloud credentials. This requires providing GitHub and Pulumi tokens with the template while allowing providers to maintain visibility through access grants.

**Provider-managed deployment**: The provider deploys infrastructure for customers using ESC environments with pre-configured credentials through the Pulumi UI, maintaining full management and visibility throughout the deployment lifecycle.

### Internal infrastructure provisioning

Platform teams can use this pattern to standardize infrastructure provisioning for internal development teams. Instead of each team recreating common patterns like application hosting, databases, or monitoring stacks, platform teams create templates that encapsulate organizational best practices, security requirements, and compliance standards.

Development teams consume these templates through the Pulumi UI, choosing from code-based, low-code, or no-code deployment options based on their technical expertise and project requirements.

### Internal developer tooling

Organizations can componentize internal tools and services—CI/CD pipelines, monitoring systems, security tools, or development environments—into reusable templates. This ensures consistent deployments while allowing teams to focus on application logic rather than infrastructure setup.

### Component marketplace

This approach enables organizations to build internal component marketplaces where different teams contribute specialized infrastructure components. Database teams might provide optimized database components, security teams contribute compliant networking components, and application teams build service deployment components. Platform teams can then compose these components into templates tailored for specific use cases.

### Multi-environment deployments

Templates can abstract environment-specific complexity, allowing the same application definition to deploy across development, staging, and production environments with appropriate configurations, scaling parameters, and security policies automatically applied based on the target environment.

## The Value

### For developers

Developers gain complete flexibility in their component creation, choosing their preferred programming language and implementing whatever business logic and resources they need. This approach lessens the burden on platform teams by allowing developers to work in languages they're most comfortable with, while secure components and guardrails enable developer autonomy without sacrificing security. AI agents automate away routine tasks and accelerate developer efficiency, letting developers focus on solving business problems rather than wrestling with infrastructure complexity.

### For platform teams

Platform teams can maintain visibility into deployed infrastructure while keeping the design and content more confidential through abstracted views. They determine what parts of the infrastructure are customizable versus necessary for security and functionality, creating templates that balance flexibility with organizational standards. This approach enables easy ingestion of updates to recommended infrastructure when new template versions are released, and makes it possible to set up team token generation for full self-service deployments.

### For consumers

End users benefit from multiple levels of insight into what's being deployed—abstracted, detailed, and visual—using YAML templates, AI, and previews to understand their infrastructure without managing complexity. They stay more secure by using their own access to deploy infrastructure, while the abstracted interface simplifies what was once a complex multi-step process into a form-based experience. More resources managed through this approach means per-resource costs decrease, making infrastructure deployment both simpler and more cost-effective.

## Integrations and Considerations

### Maintaining Visibility

### Security - RBAC and Team Segmentation

### Using ESC

### Using Policies
