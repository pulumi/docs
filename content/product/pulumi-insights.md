---
title: Pulumi Insights
layout: pulumi-insights

meta_desc: Cloud security, compliance, and governance platform. Policy as code, asset management, and intelligence for your entire cloud estate.

aliases:
- /insights
- /crossguard
- /product/crossguard

overview:
    header: Pulumi Insights
    title: Cloud Security Posture Management (CSPM) that actually works
    body: |
      Pulumi Insights provides complete visibility, compliance, and control over your cloud infrastructure. Enforce policies before deployment, continuously scan for violations, auto-remediate issues, and maintain a real-time inventory of every resource across every cloud. Whether resources were created with Pulumi, Terraform, CloudFormation, or manually.
    items:
        - title: Policy as Code
          icon: shield
          icon_color: purple
          description: |
            Write policies in real programming languages. Enforce security and compliance rules automatically.

        - title: Asset Inventory
          icon: eye
          icon_color: yellow
          description: |
            Complete visibility into every cloud resource. Search, analyze, and track everything in one place.

        - title: Continuous Compliance
          icon: cycle
          icon_color: blue
          description: |
            Scan continuously for violations. Auto-remediate issues. Stay compliant 24/7.

workflow:
  description: |
      Making sense of millions of cloud resources across hundreds of clouds, regions, and accounts is hard. Pulumi Insights provides the tools to navigate all four phases of infrastructure management.
  items:
    - header: Discover
      body: Scan and sync all infrastructure to bring it under a single pane of glass.
    - header: Understand
      body: Find insights about your cloud to reach business objectives faster.
    - header: Manage
      body: Structure infrastructure into logical groups that map to business needs.
    - header: Improve
      body: Execute improvement plans for security, cost, and compliance.

features:
  - header: Resource Search
    subheader: Find anything in any cloud
    body: Query your entire cloud estate with SQL-like syntax or natural language. Search across AWS, Azure, GCP, Kubernetes, and 100+ providers. Find that needle in the haystack or run sophisticated queries to track down untagged or expensive resources.
    graphic: /images/product/insights-resource-search.png
  - header: Policy Violations
    subheader: Discover violations and enforce compliance
    body: Get a comprehensive view of all policy violations across your organization. Write policies in TypeScript, Python, or Go. Use 150+ pre-built policies for SOC 2, PCI DSS, HIPAA, CIS, and more. Block non-compliant deployments automatically.
    graphic: /images/product/insights-policy.png
  - header: AI Copilot
    subheader: Converse about your infrastructure
    body: Pulumi Copilot makes discovering cost savings, running compliance checks, and debugging deployments as easy as typing a question. Ask "What are my most expensive unused resources?" or "Do I have any public S3 buckets?" and get instant answers.
    graphic: /images/product/insights-copilot.png
  - header: Scan & Sync
    subheader: Gain visibility across all cloud resources
    body: Pulumi Insights scans and syncs your entire cloud infrastructure, including resources not managed by Pulumi IaC. Discover resources created by Terraform, CloudFormation, or manually through the console.
    graphic: /images/product/insights-scan-sync.png

ai:
    title: AI-Powered Intelligence
    subtitle: Automate infrastructure management with AI
    image: https://www.pulumi.com/uploads/pulumi-insights-copilot.gif
    description: |
        Pulumi Copilot provides deep understanding of your infrastructure. Gain visibility into team activity, discover cost savings, ensure compliance, and debug failures - all through natural language conversation.

customer_quotes:
  alkira:
    text: |
      "Pulumi Copilot and Insights make it really easy to find idle developer environments that need to be shut down, which reduces our cloud costs significantly."
    author: Santosh Dornal, Head of Software Test & DevOps
    logo: alkira

analytics:
    title: Analytics and Insights
    subtitle: Deep insights into infrastructure
    image: /images/product/pulumi-insights-analytics.png
    description: |
        Identify anomalies in resource usage. Export data to Snowflake, BigQuery, or Redshift. Query via REST API for custom dashboards. Built-in dashboards for cloud usage insights.

pricing:
    title: Pricing
    description: |
        Pulumi Insights is included for all resources managed by Pulumi Cloud. Advanced compliance packs and unlimited scanning available on Enterprise plans.

get_started:
    title: Get started with Pulumi Insights
    description: |
        Start with policy as code. Scale to complete cloud governance. Get visibility, compliance, and control over your entire cloud estate.
---