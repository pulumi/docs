---
title_tag: CLEAR | Case Studies
title: "CLEAR: A 90% Smaller Infrastructure Codebase with Pulumi"
description: |
    CLEAR migrated their infrastructure code from Terraform to a custom self-service internal developer platform built with the Pulumi Python SDK and Automation API, enabling service teams to dynamically provision their own infrastructure while targeting a 90% reduction in infrastructure code.
meta_desc: CLEAR replaced 150,000 lines of Terraform with a self-service Pulumi platform in Python and the Automation API, cutting infrastructure code by 90%.

customer_name: CLEAR
industry: security
customer_logo: /logos/customers/clear.png
customer_url: https://www.clearme.com/

quote_block:
  quote: |
      "For that 'batteries included' experience we wanted to provide, being able to have the full power of Python at our fingertips to handle all those sorts of specialized cases is really, really powerful."
  quote_attrib: James Forcier, Staff Software Engineer, CLEAR
  headline_stat: ~90%
  headline: projected reduction in lines of infrastructure code

exec_summary: |
    CLEAR is a secure identity verification company that has been serving airports for over 15 years, and additionally partners with a breadth of heavily regulated healthcare and government organizations where secure identity verification is critical to operational success.

    After identifying growing pains with their existing Terraform infrastructure, site reliability engineers used Pulumi's Python SDK and Automation API to build friendlier, lower-maintenance internal tools that enabled service teams to configure their own infrastructure faster. This migration to Pulumi is expected to reduce the size of CLEAR's infrastructure code by 90%, yielding a dramatic improvement in both maintainability and auditability.

sections:
    - label: Exec Summary
      anchor: executive-summary
    - label: Challenge
      anchor: customer-challenge-infrastructural-growing-pains
    - label: Solution
      anchor: solution-managing-infrastructure-directly-from-application-code
    - label: Results
      anchor: results
    - label: Looking Ahead
      anchor: looking-ahead-simplifying-regulatory-compliance-with-policy-as-code
---

## Customer challenge: infrastructural growing pains

James Forcier, Staff Software Engineer at CLEAR, noted that his team's biggest growing pains were caused by the sheer volume, sprawl, and fragmentation in their Terraform infrastructure. The lack of standardization within their Terraform and Terragrunt code became a bottleneck for both the production engineering team and the individual service teams they supported.

- **High maintenance cost**: The core Terraform and Terragrunt codebases alone comprised about 150,000 lines of HCL code, much of it defining service infrastructure that was not owned by core infrastructure engineers. Because this code was centralized in core repositories and spread across many modules, service teams had to continuously navigate other codebases to manage large volumes of non-standardized IaC code, diverting bandwidth from their day-to-day operations.
- **Manual configuration burden**: Every time developers needed to provision per-service resources, they had to coordinate configurations across different internal modules, and needed to gain expertise in how the rest of CLEAR's infrastructure worked. It became unnecessarily tedious for service teams to manually configure low-level AWS settings, such as security groups and RDS connections.
- **Difficulty communicating between modules with Terragrunt**: "A big problem we had before was that we used Terraform in conjunction with Terragrunt, and that's pretty heavily dependent on your on-disk structure," Forcier said. "We found that it was difficult for developers to understand how they needed to plug in outputs from different modules, or reference across different parts of the infrastructure. It was a challenge for us to maintain."

## Solution: managing infrastructure directly from application code

CLEAR sought a Terraform alternative that would allow service teams to provision infrastructure that was easy to use out of the box, without needing to think about low-level AWS configurations by default. They chose Pulumi because its unique capabilities enabled them to create custom self-serve infrastructure that was more user-friendly and configurable.

### Using Python to encapsulate infrastructure logic

Pulumi is the only multi-cloud IaC tool with the ability to use common general-purpose languages to define infrastructure, offering more workflow familiarity, high-level control flow, and complex logic management than IaC tools with proprietary DSLs. Forcier remarked that the advantages of Pulumi were clear: "Number one for us is the ability to use general-purpose programming languages. For that 'batteries included' experience we wanted to provide, being able to have the full power of Python at our fingertips to handle all those sorts of specialized cases is really, really powerful."

By using the [Pulumi Python SDK](/docs/iac/languages-sdks/python/) to consolidate their infrastructure logic, CLEAR was able to better encapsulate their code, creating a user-friendly and robust separation between low-level infrastructure details and the specific configurations set for each service repository.

### Building internal IaC tooling with the Pulumi Automation API

Another major motivation to migrate to Pulumi was its [Automation API](/docs/iac/concepts/automation-api/), which wraps infrastructure functionality that is normally only accessible as CLI commands. This makes it possible to dynamically manage and provision infrastructure directly from application code as if using any other SDK.

CLEAR used Pulumi's Automation API to help set up CI/CD workflows that dynamically provisioned per-service infrastructure as needed. "We moved from a lower-level Terraform and HCL-based interface to something built with Pulumi and the Automation API, to define this really custom, high-level, and much simpler YAML schema. We've identified really common business cases that our developers need out of the infrastructure, and made those into built-in defaults. They can just plug in a few standard GitHub Actions workflows and they have infrastructure right in their repo," Forcier said.

Instead of needing to become experts at navigating a monolithic infrastructure codebase, service developers can now configure infrastructure directly in their individual repositories by writing and editing simple YAML files.

### Standardizing IaC interfaces with the Automation API

CLEAR wanted a friendlier alternative to Terragrunt to enable developers to cross-reference other modules within the company.

They accomplished this by using the Automation API to let developers reference exports across different [stacks](/docs/iac/concepts/stacks/), or project instances. Pulumi [stack references](/docs/iac/concepts/stacks/#stackreferences) resolve dynamically across different environments, such as between `staging` and `prod`. This allows developers to use one consistent high-level interface to fetch exports from other programs without understanding their internal workings.

## Results

Switching to Pulumi has dramatically improved CLEAR's operational efficiency, simplifying infrastructure maintenance and service development. "Instead of having our centralized infrastructure repos with huge blobs of Terraform that developers have to maintain and care about, we have an internal developer platform and we move the configurations into the service repos themselves. It's a big win for our developers. They don't have to go hunting around in multiple places to find where their infrastructure is defined," Forcier remarked.

- **Code reduction and maintainability**: CLEAR used to maintain 150,000 lines of Terraform HCL. Their new Pulumi-based analogue is on track to be 90% smaller, making it faster to maintain, audit, and review infrastructure code. The migration to Python has also made infrastructure code significantly more manageable.
- **Streamlined CI/CD-ready infrastructure as code**: CLEAR used Pulumi to set up custom GitHub Actions workflows in service repositories, providing self-serve infrastructure to service teams that's pre-optimized for common business use cases by default.
- **Standardized IaC interface**: Engineers can now call a unified SDK using their language of choice to cross-reference exports from different instances, across different environments, rather than manually interfacing with large Terragrunt files to look up references.

Now that the biggest pain points have been successfully addressed, CLEAR is working on improving the rest of their core AWS infrastructure with Pulumi integrations.

## Looking ahead: simplifying regulatory compliance with policy as code

Since CLEAR operates in heavily regulated government spaces, its software needs to continue maintaining compliance with strict regulatory frameworks. "It would be a huge win for us to enforce our policy packs with the Automation API, to ensure that we can never create any non-compliant infrastructure. That's the big one that's on our radar next," Forcier said.

Pulumi maintains pre-built [policy packs](/docs/insights/policy/policy-packs/) for enforcing common security and compliance policies, including PCI DSS, HITRUST, ISO 27001, CIS, and NIST, across a broad range of cloud providers, including AWS, Azure, Google Cloud, and Kubernetes. Pulumi also supports custom policy packs, which can be written in TypeScript, Python, or OPA Rego to enforce organization-specific requirements.
