---
title: Migrating to Pulumi
meta_desc: Focus on building momentum with early wins while establishing practices that will scale with your organization.
weight: 4
menu:
    cloud:
        name: Migrating to Pulumi
        parent: pulumi-onboarding-guide
        identifier: migrating-to-pulumi
---
Successfully migrating to Pulumi requires strategic decisions about your migration approach. Focus on building momentum with early wins while establishing practices that will scale with your organization.

## Migrating existing infrastructure

If you have existing cloud infrastructure to bring into Pulumi IaC, you have several strategies available.

### Choose your migration approach

**Start fresh:** Simply throw away existing infrastructure and begin anew. This ensures you can adopt all best practices from the outset without technical debt. This option isn't always practical for business-critical services.

**Import existing infrastructure:** Pulumi has tools to import any cloud infrastructure regardless of how it was created — even manually through cloud consoles. The [Visual Import](https://www.pulumi.com/docs/insights/import/) feature is the recommended approach for importing resources. However, Pulumi also offers tailored migration tools for Terraform, AWS CloudFormation/CDK, Azure ARM, and Kubernetes YAML. These tools generate Pulumi IaC code in your chosen language and actively place existing resource management under Pulumi IaC, swapping out management without disrupting resources for zero downtime.

**Coexist and migrate incrementally:** Pulumi supports coexisting with existing ecosystems. You can deploy Helm charts as-is or consume Terraform workspace outputs. This enables incremental migration over time when the value is right.

**Get professional help:** Pulumi offers professional services to help with migration.

{{% notes type="info" %}}

Learn more at the [Pulumi Migration Hub](https://www.pulumi.com/docs/iac/adopting-pulumi/migrating-to-pulumi/) or [detailed migration tooling documentation](https://www.pulumi.com/docs/iac/adopting-pulumi/).

{{%/notes%}}

## Drive and measure migration success

Successfully migrating to Pulumi requires treating it like a product launch with clear success metrics and strategic execution.

### Start with a beachhead win

**Goal:** Get your first 1-3 workloads into production as soon as possible (typically 3-6 months for most organizations).

This "beachhead" win accomplishes three things:

- Keeps you grounded in reality without going dark too long
- Lays groundwork for onboarding more workloads while improving your platform
- Provides tangible accomplishments to showcase to management and broader teams

These workloads should be automated with CI/CD pipelines and use as many best practices as possible, even though you'll be early in figuring out components and templates.

### Stay focused on impact

**Take a "workload-first" strategy:** Rather than creating dozens of abstractly-useful components, inform specific component requirements from real-world applications emerging from your beachhead win.

**Resist the redesign temptation:** Don't conflate redesigning projects with new cloud architectures and platform migration. This adds risk. Get workloads onto Pulumi first, then refactor and redesign in place.

### Treat your platform like a product

An internal cloud platform is a product requiring superb developer experiences. While self-service is the primary goal, it's a journey. Start by:

- Getting your platform well-architected
- Documenting components and templates. You can use [Pulumi Cloud IDP](https://www.pulumi.com/product/internal-developer-platforms/) to provide user visibility and access to your templates and components.
- Instituting an internal open source strategy for collaboration
- Building comprehensive platform capabilities over time

### Don't defer security

Use this moment of change to build security into your platform from day one. Implement Pulumi IaC's Policy as Code features and short-lived cloud credentials with [Pulumi ESC and OIDC](https://www.pulumi.com/docs/esc/integrations/dynamic-login-credentials/). Teams that build up technical debt in this area face costly implications later.

### Measure your success

Establish clear success metrics from the outset:

**Common improvement metrics:**

- Time from checking in code until it ships to production
- DORA metrics (deployment frequency and related measurements)
- Time for developers to get new cloud environments

Pulumi customers commonly see 5-10X improvements in these areas, with environment setup times reducing from months to minutes through self-service techniques.
{{< get-started-stepper >}}
