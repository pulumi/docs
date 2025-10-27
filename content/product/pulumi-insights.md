---
title: Cloud Asset and Compliance Management – Pulumi Insights
layout: pulumi-insights

heading: Insights & Governance
subheading: |
    Complete visibility and control for your cloud

meta_desc: Join us on November 5 to see how Neo helps you get clean and stay clean - automatically. Watch it in action. Live demo + Q&A.
meta_image: /images/product/insights-neo-launch-meta.png

aliases:
- /insights
- /product/pulumi-insights
- /product/crossguard
- /crossguard

preview:
  header:  Pulumi Neo just got smarter about infrastructure policy automation
  description: Join us on November 5 at 10:00 AM PT / 18:00 (UTC +0) for Pulumi Policies: Get Clean and Stay Clean Automatically. Watch it in action. Live demo + Q&A.  
  hubspotID: 4031229e-1370-4118-9379-ee2be1fd64fd
  videoID: mwcrOTEf1EQ?si=Fx77RxM-uCjJLN-6

overview:
    header: Complete visibility and control for your cloud
    title: See everything. Control everything. Ship with confidence.
    body: |
      Get complete visibility into your cloud infrastructure - whether created with Pulumi IaC, Terraform, CloudFormation, or the console. Enforce policies as code, ensure compliance, and catch issues before they reach production. 
    items:
        - title: Policy as Code
          icon: shield
          icon_color: purple
          description: |
            Write policies in TypeScript or Python. Hundreds of built-in policies. Block bad configurations before they ship. Auto-remediate existing violations.

        - title: Cloud Resource Search
          icon: eye
          icon_color: yellow
          description: |
            Search across all your clouds using structured queries or natural language. Find resources, track dependencies, identify security risks and compliance violations.

        - title: Complete Cloud Visibility
          icon: global
          icon_color: blue
          description: |
            See every resource across AWS, Azure, GCP, and thousands of providers. Track relationships, monitor drift, identify unused resources. 

workflow:
  description: |
      From discovery to governance, get the visibility and control you need to manage cloud infrastructure at scale.
  items:
    - header: Discover
      body: Automatically scan and catalog all cloud resources across AWS, Azure, GCP, and thousands of providers - regardless of how they were created.
    - header: Govern
      body: Enforce policies as code across your entire infrastructure. Prevent violations at deployment time, ensure compliance, maintain security standards.
    - header: Analyze
      body: Search and query your infrastructure. Understand relationships, track dependencies, identify security and compliance issues.
    - header: Act
      body: Fix policy violations, remediate security issues, clean up unused resources. Take action based on real data, not guesswork.

features:
  - header: Resource Search
    subheader: Find anything in any cloud
    body: Search your infrastructure across thousands of cloud providers using structured queries or natural language. Find specific resources across multiple clouds and environments. Track down untagged resources, identify security group violations, or locate idle infrastructure across your entire organization.
    graphic: /images/product/insights-resource-search.png
  - header: Policy as Code
    subheader: Enterprise governance using real programming languages
    body: Write policies in TypeScript or Python - the same languages you use for infrastructure. Choose from hundreds of built-in policies or create custom rules. Block non-compliant resources during `pulumi up`. Auto-remediate existing violations. Meet SOC 2, HIPAA, and PCI-DSS requirements.
    graphic: /images/product/insights-policy.png
  - header: Natural Language Search
    subheader: Ask questions about your infrastructure
    body: Search using plain English queries. "Which EC2 instances are publicly accessible?" "What changed in production last week?" "Show me resources without required tags." Get answers across all your clouds instantly.
    graphic: /images/product/insights-copilot.png
  - header: Cloud Discovery
    subheader: See everything, regardless of how it was created
    body: Automatically discover and catalog resources created outside of Pulumi - whether from Terraform, CloudFormation, or manual console operations. Get complete visibility across your entire cloud estate. Apply policies and insights to all resources, not just Pulumi-managed ones.
    graphic: /images/product/insights-scan-sync.png

governance:
    title: Enterprise-Grade Governance
    subtitle: Policy enforcement that doesn't slow you down
    image: https://www.pulumi.com/uploads/pulumi-insights-copilot.gif
    description: |
        Shift security and compliance left with policy as code. Define guardrails in TypeScript or Python, enforce them at deployment time, and automatically remediate violations. Integrate with your existing compliance frameworks and get detailed audit trails for every policy decision. 

customer_quotes:
  alkira:
    text: |
      “I’m making developers at Alkira significantly more productive while also making my job easier using Pulumi’s IaC platform and features like Pulumi Insights and Deployments. I can get developers using IaC immediately with Pulumi Deployments and its GitHub integration, while Pulumi Insights makes it really easy to find idle developer environments that need to be shut down, which reduces our cloud costs.”
    author: Santosh Dornal, Head of Software Test & DevOps
    logo: alkira

analytics:
    title: Analytics & Intelligence
    subtitle: Data-driven infrastructure decisions
    image: /images/product/pulumi-insights-analytics.png
    description: |
        Transform infrastructure data into actionable intelligence. Track costs, identify trends, detect anomalies, and measure compliance. Export to Snowflake, BigQuery, or any data warehouse. Build custom dashboards, automate reports, and integrate with your existing BI tools. Make informed decisions backed by comprehensive cloud analytics.

pricing:
    title: Pricing
    description: |
         Insights & Governance capabilities are included with Pulumi Cloud. Get visibility and control over all your cloud resources, whether managed by Pulumi or not.

learn:
    title: Take control of your cloud
    items:
        - title: Start with complete visibility
          description: |
            Get instant visibility into all your cloud resources. Add governance policies and optimize with AI-powered insights.
          buttons:
            - link: /docs/insights/get-started/
              type: primary
              action: Start Free
            - link: /contact/?form=request-a-demo
              type: secondary
              action: Book a Demo
        - title: Learn more
          description: |
            Discover how to implement policies, track compliance, and optimize costs across your entire cloud infrastructure.
          buttons:
            - link: /docs/pulumi-cloud/insights/
              type: primary
              action: Read the Docs
            - link: /docs/insights/policy/policy-as-code/
              type: secondary
              action: Policy Guide
---
