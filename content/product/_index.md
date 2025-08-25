---
title: Platform Overview
meta_desc: The complete infrastructure as code platform. Write in any language, deploy to any cloud, with enterprise-grade security and collaboration.
layout: pulumi-cloud

aliases:
    - /product/pulumi-cloud/
    - /product/pulumi-service/
    - /product/cloud/
    - /cloud/

overview:
    title: The Complete Infrastructure Platform
    description: |
        **Pulumi IaC** is our open source engine that lets you write infrastructure as code in any programming language. It's free forever and works with any state backend. **Pulumi Cloud** is the easiest way to use Pulumi in a team, providing managed state storage, secrets encryption, team collaboration, and enterprise features. Free for individuals.

case_studies:
    title: Teams Succeeding with Pulumi
    items:
        - name: BMW
          link: /case-studies/bmw/
          logo: bmw
          description: |
            11,000+ developers building cloud platforms across hybrid environments.

        - name: Snowflake
          link: /case-studies/snowflake/
          logo: snowflake
          description: |
            3x faster deployments with multi-cloud Kubernetes platform.

        - name: Atlassian
          link: /case-studies/atlassian/
          logo: atlassian
          description: |
            Developers reduced their time spent on maintenance by 50%.

        - name: Lemonade
          link: /case-studies/lemonade/
          logo: lemonade
          description: |
            Standardized infrastructure architectures with reusable components.

        - name: Starburst
          link: /blog/how-starburst-data-creates-infrastructure-automation-magic-with-code/
          logo: starburst
          description: |
            Increased velocity with deployments up to 3x faster.

        - name: Elkjop Nordic
          link: /case-studies/elkjop-nordic/
          logo: elkjop-nordic
          description: |
            Increased developer agility through platform engineering.

products:
    - header: Platform Capabilities
      content:
        - header: Infrastructure as Code
          tabid: iac-select
          subheader: Open source foundation
          link: /product/infrastructure-as-code/
          image: /images/product/console-resource-graph.svg
          details:
            - title: Write in real programming languages
              description: |
                Use TypeScript, Python, Go, C#, Java, or YAML to define infrastructure. Get full IDE support with autocomplete, type checking, and testing. Deploy to AWS, Azure, Google Cloud, Kubernetes, and thousands of providers.

              more_info: |
                The Pulumi IaC engine is 100% open source and free forever. Use loops, conditionals, functions, and classes - no more copy-paste.

                Test your infrastructure with unit tests. Preview changes before deploying. Catch errors at compile time, not runtime.

            - title: Use with any state backend
              description: |
                Self-manage state with S3, Azure Blob, Google Cloud Storage, or local files. Or use Pulumi Cloud for managed state with encryption, versioning, and locking.

              more_info: |
                Pulumi Cloud makes collaboration easy with automatic state management, concurrent deployments, and full history of all changes.

        - header: Pulumi ESC
          tabid: esc-select
          subheader: Secrets and configuration management
          link: /product/secrets-management/
          image: /images/product/esc-screenshot-2.png
          details:
            - title: Stop hardcoding secrets
              description: |
                Centralize all secrets and configuration in one secure place. Pull from any secrets store including HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, and more.

              more_info: |
                No more .env files with plaintext secrets. Access configuration via CLI, API, SDKs, or Kubernetes operator.

                Every environment supports versioning, RBAC, and full audit logs. Use short-lived credentials and dynamic secrets.

            - title: Works with any tool
              description: |
                Use Pulumi ESC with or without Pulumi IaC. Integrate with any application, CI/CD pipeline, or infrastructure tool.

              more_info: |
                Available via TypeScript, Python, Go SDKs. Kubernetes operator for native integration. REST API for custom integrations.

        - header: Pulumi Insights
          tabid: insights-select
          subheader: Cloud governance and intelligence
          link: /product/pulumi-insights/
          image: /images/product/resource-search-diagram.svg
          details:
            - title: Complete visibility and control
              description: |
                See everything running in your cloud. Search across all resources. Enforce policies. Auto-remediate violations. Track compliance.

              more_info: |
                Discovers all resources, even those not managed by Pulumi. Write policies in code with CrossGuard. 150+ pre-built policies for SOC 2, PCI DSS, HIPAA, and more.

            - title: AI-powered insights
              description: |
                Pulumi Copilot helps you understand infrastructure, debug failures, find cost savings, and identify security issues - all through natural language.

              more_info: |
                Ask questions like "What are my most expensive unused resources?" or "Do I have any public S3 buckets?" Get instant answers with actionable recommendations.

open_source:
    title: Open Source with Enterprise-Grade Platform
    image: /images/product/service-open-source-diagram.svg
    description: |
        Pulumi IaC is open source and free forever. Pulumi Cloud adds team collaboration, security, and scale. Think of it like Git (open source) vs GitHub (managed service) - you can use Git alone, but GitHub makes collaboration much easier.

security:
    title: Enterprise Security
    image: /images/product/soc-aicpa.svg
    description: |
        SOC 2 Type II compliant. All data encrypted at rest and in transit. SAML SSO, SCIM provisioning, and RBAC. Complete audit logs of all actions.

deployment:
    title: Deployment Options
    items:
        - title: SaaS
          icon: rocketship
          icon_color: purple
          description: Fully managed service with no maintenance required.

        - title: Self-Hosted
          icon: program
          icon_color: yellow
          description: Run Pulumi Cloud in your own environment.

pricing:
    title: Pricing
    description: |
        Free for individuals. Team plans start at $1 per resource per month. Volume discounts available for large teams and enterprises.

get_started:
    title: Get Started Today
    description: |
        Deploy infrastructure in minutes with the open source CLI or sign up for Pulumi Cloud for team collaboration.
---