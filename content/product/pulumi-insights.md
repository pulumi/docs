---
title: Pulumi Insights
layout: pulumi-insights

meta_desc: Pulumi Insights is Intelligent Cloud Management. Gain security, compliance, and cost insights into your cloud, and automatically remediate issues.

aliases:
- /insights

overview:
    header: Intelligent Cloud Management
    title: A central hub to securely manage all of your environments, secrets, and configurations
    body: |
      - **Stop secret sprawl.** Pull and sync secrets and configuration with any secrets store – HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, GCP Secret Manager, 1Password, and more – and consume in any application, tool, or CI/CD platform.  
      - **Trust (and prove) your secrets are secure.** Adopt dynamic, short-lived secrets on demand as a best practice. Lock down every environment with RBAC, versioning, and a full audit log of all changes.  
      - **Ditch `.env` files.** No more copying-and-pasting secrets or storing them in plaintext on dev computers. Developers can easily access secrets via CLI, API, Kubernetes operator, the Pulumi Cloud UI, and SDKs.
      - **Use with or without Pulumi IaC.** Use Pulumi ESC independently, or use with Pulumi IaC to support storing secrets in config in a more secure way than using plaintext.
    description: |
        Pulumi Insights is an asset and compliance management service that gives search, compliance remediation, resource visualizations, and AI insights over any infrastructure, including resources not provisioned by Pulumi IaC such as AWS CloudFormation, Microsoft ARM, HashiCorp Terraform, or even manually.
    items:
        - title: Security
          icon: shield
          icon_color: purple
          description: |
            Analyze and dig into your organization’s cloud usage and trends.

        - title: Compliance
          icon: gavel
          icon_color: yellow
          description: |
            Reduce lead time from ideation to delivery through Pulumi AI and Pulumi Copilot.

        - title: Efficiency
          icon: cycle
          icon_color: blue
          description: |
            Analyze and update infrastructure to optimize costs, enhance security, and ensure compliance. 

workflow:
  - header: Discover
    body: Lorem ipsum odor amet, consectetuer adipiscing elit. Malesuada quis pellentesque vehicula, fermentum nostra a.
  - header: Understand
    body: Lorem ipsum odor amet, consectetuer adipiscing elit. Mattis venenatis viverra orci sapien, fermentum massa.
  - header: Manage
    body: Lorem ipsum odor amet, consectetuer adipiscing elit. Per felis mollis vitae bibendum torquent fringilla urna.
  - header: Import
    body: Lorem ipsum odor amet, consectetuer adipiscing elit. Massa euismod fermentum aliquet primis auctor hendrerit velit.

features:
  - header: Resource Search
    subheader: Find anything in any cloud
    body: Ask any questions about your infrastructure across more than 100 clouds, using either structured search queries or natural language prompts. Search helps you find that needle in the haystack – locating a single resource across many clouds and environments – as well as running sophisticated queries such as tracking down untagged or expensive resources across the whole organization.
    graphic: https://www.pulumi.com/uploads/pulumi-insights-search.gif
  - header: Policy Violations
    subheader: Lorem ipsum odor amet
    body: Lorem ipsum odor amet, consectetuer adipiscing elit. Fames scelerisque sagittis ipsum felis neque. Sociosqu nisl pulvinar eget enim vestibulum litora platea. In lobortis nisi phasellus purus primis laoreet mollis torquent sed.
    graphic: https://www.pulumi.com/uploads/pulumi-insights-search.gif
  - header: AI copilot
    subheader: Automate infrastructure with the power of AI
    body: Automate infrastructure management tasks through AI. You can tap into the Pulumi Copilot's deep understanding of your user and organization context to gain visibility into your team's activity, discover cost saving opportunities, get compliant, and debug cloud failures. 
    graphic: https://www.pulumi.com/uploads/pulumi-insights-copilot.gif

ai:
    title: AI
    subtitle: Automate infrastructure with the power of AI
    image: https://www.pulumi.com/uploads/pulumi-insights-copilot.gif
    description: |
        Automate infrastructure management tasks through AI. You can tap into the Pulumi Copilot's deep understanding of your user and organization context to gain visibility into your team's activity, discover cost saving opportunities, get compliant, and debug cloud failures. 

customer_quotes:
  alkira:
    text: |
      “I’m making developers at Alkira significantly more productive while also making my job easier using Pulumi’s IaC platform and features like Pulumi Insights and Deployments. I can get developers using IaC immediately with Pulumi Deployments and its GitHub integration, while Pulumi Insights makes it really easy to find idle developer environments that need to be shut down, which reduces our cloud costs.”
    author: Santosh Dornal, Head of Software Test & DevOps
    logo: alkira

analytics:
    title: Analytics
    subtitle: Gain deeper insights into infrastructure as code
    image: /images/product/pulumi-insights-analytics.png
    description: |
        Identify anomalies or trends in resource usage and dig into cost, security, and [compliance](/compliance/) concerns. You can programmatically query a REST API to add automation around search results or to integrate with internal platforms and dashboards. You can export data to other data warehouses including Snowflake, Amazon Redshift, Google BigQuery and Azure Synapse. You also have built-in dashboards that give you key insights about cloud usage.

pricing:
    title: Pricing
    description: |
         Pulumi Insights is included for all resources managed by Pulumi Cloud. 

get_started:
    title: Get started today
    description: |
        Gain a deep understanding of your cloud usage, discover potential cost savings opportunities, and enforce compliance and security policies across your entire cloud.
---
