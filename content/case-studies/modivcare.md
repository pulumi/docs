---
title_tag: Modivcare | Case Studies
title: "Modivcare: Self-Service and Governance Create a Competitive Advantage"
allow_long_title: true
description: |
    Modivcare used Pulumi to transform fragmented acquisition-built infrastructure into a unified platform without service disruption, achieving up to 25% cost reductions and enabling developer self-service.
meta_desc: See how Modivcare used Pulumi to unify fragmented AWS infrastructure across acquisitions, reducing costs by up to 25%.

customer_name: Modivcare
customer_logo: /images/case-studies/modivcare.png
customer_url: https://www.modivcare.com/

quote_block:
  quote: |
      "Pulumi ESC has been fundamentally game-changing in how we want to bring that apart, not just in solving that disconnected set of Terragrunt files, but also in normalizing a lot of those Terragrunt files."
  quote_attrib: Zachary Cook, Senior Manager, DevOps at Modivcare
  headline_stat: 25% Cost Savings
  headline: By eliminating redundant resources

exec_summary: |
    [Modivcare](https://www.modivcare.com/) is a technology-enabled healthcare services company that provides a suite of integrated supportive care solutions for public and private payors and their members. Built through strategic acquisitions, Modivcare consolidated multiple healthcare service organizations, each bringing different operational practices and infrastructure approaches. Using Pulumi Insights, Pulumi ESC, and a developer portal integration, Modivcare transformed from disconnected infrastructure implementations into a unified platform supporting their healthcare mission—all without disrupting critical healthcare services.

sections:
    - label: Exec Summary
      anchor: executive-summary
    - label: The Challenge
      anchor: the-challenge
    - label: Gaining Visibility
      anchor: gaining-visibility
    - label: Results
      anchor: results
    - label: Conclusion
      anchor: conclusion
---

## About Modivcare

Modivcare's value-based solutions address the social determinants of health by connecting members to essential care services. By doing so, Modivcare helps health plans manage risks, reduce costs, and improve health outcomes. Beyond non-emergency medical transportation, they provide meal delivery services, daily care coordination, and various supportive care solutions—including the ubiquitous Higi health screening kiosks available at many retail locations.

Built through strategic acquisitions, Modivcare consolidated multiple healthcare service organizations, each bringing different operational practices and infrastructure approaches. This growth model enabled rapid expansion but created significant technical challenges that needed resolution to achieve operational efficiency at scale.

## The Challenge: When Growth Becomes a Technical Burden

By 2023, Modivcare's acquisition strategy had created a perfect storm of infrastructure complexity. Each acquired company arrived with different AWS approaches: mature Terraform and Terragrunt setups, AWS CDK or CloudFormation implementations, or no infrastructure automation at all—just manually provisioned resources and PowerShell scripts.

"We had an organization, we had a top-down design, but when there was an acquisition, if they were in AWS, that account got added to the organization after the fact," explained Zachary Cook, Senior Manager, DevOps at ModivCare.

The newly formed platform engineering team had to onboard legacy AWS accounts, invisible resources, and teams with vastly different cloud maturity levels. Traditional consolidation would require disruptive migrations that could impact healthcare services—unacceptable for a company serving vulnerable populations.

{{< youtube "1um_8QTVqXg" >}}

## Gaining Visibility Into the Unknown

Rather than forcing immediate migrations, Modivcare's platform team started with visibility. They deployed Pulumi Insights across their fragmented AWS environment to understand what infrastructure they actually had.

Pulumi Insights revealed exactly which resources were managed through infrastructure as code versus manually provisioned. For the first time, teams could see their complete AWS footprint and identify at-risk infrastructure. Equally important, Pulumi's comprehensive provider ecosystem and import capabilities meant teams could continue using their preferred programming languages and existing tools while bringing resources under proper management without disruption.

"We could start to see quickly with Insights what portion of resources are managed versus what portion of resources are expressed as an infrastructure as code process."

This visibility became the foundation for everything that followed. Teams that had been operating blind could now make informed decisions about their infrastructure.

## Meeting Teams Where They Are

With visibility established, the platform team tackled standardization without disruption using Pulumi ESC (Environments, Secrets, and Configuration).

For newly acquired companies, they created targeted ESC environments addressing specific needs without touching existing workloads. When a new acquisition needed subdomain management, they created an ESC environment providing only Route 53 access for that task.

"We'll have an ESC environment that's specifically for this one account, it's a new acquisition, we don't necessarily want to disrupt everything, but we do want to maybe maintain some infrastructure as code role for doing things like adding a subdomain."

This approach created a breakthrough: teams began adopting infrastructure as code organically, starting with fast time-to-value use cases rather than being forced into wholesale migrations.

## Unifying Configuration Across Disconnected Systems

Pulumi ESC solved unexpected problems. Teams with mature Terragrunt implementations had been maintaining dozens of disconnected configuration variable files across repositories. Every change required manual updates across multiple files—a maintenance nightmare.

Pulumi ESC normalized these configurations, providing centralized management while coexisting with legacy tools. Teams could continue using AWS Secrets Manager or Parameter Store, but configuration became consistent organization-wide.

The result was transformative: what had been a complex web of disconnected configurations became a unified, manageable system that reduced operational overhead while improving reliability.

## Building Developer Self-Service at Scale

About a year after forming their platform engineering team, Modivcare built a developer portal using Backstage, integrated with GitLab CI/CD and Pulumi.

The integration was elegantly simple: Backstage's scaffolder created repositories and pipelines, GitLab runners executed workflows, and Pulumi provisioned AWS resources. Developers gained a single interface to discover solutions and provision infrastructure without becoming infrastructure experts.

The impact on productivity was dramatic: infrastructure provisioning went from days-long bottlenecks involving multiple teams to self-service capabilities that developers could use in minutes.

## Results

Modivcare's journey delivered concrete business results:

**Operational Excellence**: Infrastructure standardization across multiple AWS accounts without service disruption. This non-disruptive approach typically reduces project delays by 70% while maintaining healthcare service reliability.

**Developer Productivity**: Self-service infrastructure eliminated development bottlenecks. Dozens of reusable modules enabled developers to focus on healthcare solutions rather than infrastructure complexity.

**Strategic Capability**: Established repeatable patterns for integrating acquisitions. Rather than creating complexity, new acquisitions now follow proven integration approaches.

**Cost and Governance**: Visibility and standardization achieved up to 25% infrastructure cost reductions through elimination of redundant resources and improved governance.

**Cross-Account Simplification**: Managing their complex, acquisition-built AWS organization became dramatically simpler through Pulumi ESC's normalized configuration.

## Learning From Real Usage Patterns

Within their first year, the platform team created dozens of infrastructure modules ranging from simple utilities to comprehensive "golden path" solutions. They tracked usage through Backstage to understand how developers actually used these tools.

The results surprised them: simple tools like repository creation with basic documentation were used far more than comprehensive architectures.

"Interestingly, a new repo with basic rules in place or a basic example of a decent readme, that tool is used more than a lot of those fully blown golden path examples."

This taught them a valuable lesson: iteration and simplicity often delivered more value than comprehensive solutions, fundamentally changing their approach to platform development.

## Conclusion

Modivcare transformed from disconnected infrastructure implementations into a unified platform supporting their healthcare mission. Their platform engineering approach became a competitive advantage, enabling faster acquisition integration and more reliable service delivery.

"By integrating Pulumi Policy as Code with Insights Account Scanning and our developer portal, we're achieving the holy grail for Platform Engineering: instant visibility and governance over legacy infrastructure that isn't yet defined in IaC, while also accelerating our path to production for new cloud-native projects," said Cook.

For healthcare organizations or any company growing through acquisitions, Modivcare demonstrates that infrastructure standardization doesn't require disruption. The right approach achieves operational excellence while maintaining service reliability that people depend on.

### Key Lessons: What Made the Difference

- **Start with visibility, not migration**: Understanding existing infrastructure drove informed decisions. Pulumi Insights provided the foundation for strategic planning.
- **Meet teams where they are**: Incremental adoption through targeted use cases built trust and demonstrated value before requesting bigger commitments.
- **Listen to actual usage patterns**: Data-driven understanding of developer needs led to more effective solutions than assumptions.
