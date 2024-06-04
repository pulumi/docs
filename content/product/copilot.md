---
title: Pulumi Copilot
layout: copilot

meta_desc: Pulumi Copilot is a virtual teammate that automates management of any cloud

overview:
    title: Virtual Teammate that Automates Management of Any Cloud
    description: |
        Pulumi Copilot is a LLM-based assistant that automates any infrastructure management task. Copilot combines the power of large language models with semantic understanding of the cloud to unlock greater insights and controls over managing cloud infrastructure. Using the same GPT experience everyone knows, loves, and uses everyday, engineers can find anything in their cloud infrastructure and take action on any cloud resource. Pulumi Copilot lowers the barriers of managing the lifecycle of cloud infrastructure. 

get_started: Get Started with Copilot

# TODO: replace graphic and alt text
benefits:
    title: Where do I use Pulumi Copilot?
    description: |
        Pulumi Copilot is an interactive user interface in Pulumi Cloud, Pulumi documentation, and Pulumi CLI.
        
        Pulumi Copilot understands the entirety of over 160 clouds, including public clouds (AWS, Azure, Google Cloud), cloud native (Kubernetes, Helm), SaaS providers (Snowflake, Cloudflare, Datadog), and more. Pulumi Copilot directly interfaces with these cloud APIs and data models.
        
        Simply ask any question, and Copilot will provide relevant, contextual, and effective responses to queries across the entire platform.
    graphic:
        image: /images/product/pulumi-deployments-graphic.png
        alt: Pulumi Deployments Architecture Screenshot

# TODO: fix examples and descriptions (fragment on compliance checks)
options:
    title: How do I use Pulumi Copilot?
    description:
    items:
        - icon: upload-to-cloud
          icon_color: purple
          title: Generate infrastructure code
          description: You can generate a Pulumi program and deploy it as a template in seconds with a few simple text prompts.
          example: "Example: Create a severless application"
        - icon: eye
          icon_color: salmon
          title: Answer questions about existing infrastructure
          description: Copilot can access infrastructure stack and resource data, so you can You can analyze your infrastructure on cost, compliance, cloud usage
          example: "Example: TBD"
        - icon: shield
          icon_color: blue
          title: Run compliance checks
          description: You can analyze and update infrastructure for
          example: "Example: TBD"
        - icon: code-window
          icon_color: fuchsia
          title: Debug failed stack updates
          description: Copilot can access update and deployment logs of your stacks, so you can easily get answers about what caused failure.
          example: "Example: TBD"

# TODO: fill this out for Copilot or remove entirely
faq:
    items:
      - header: What is Pulumi Deployments?
        content: |
          Pulumi Deployments is an infrastructure lifecycle management service. It provides automation of deployment and operational workflows for cloud infrastructure. With Pulumi Deployments, you can orchestrate with ease the at-scale complexities of production infrastructure.

      - header: Is there a free tier for Pulumi Deployments?
        content: |
          Individual Edition has 500 deploy minutes/month. Team, Enterprise, and Business Critical Editions all have 3,000 included deploy minutes/month.

      - header: How does drift detection work?
        content: |
          Drift detection and remediation operate continuously, on a schedule of your choosing, comparing the state of your resources with the expected configurations defined in your Pulumi setups. Any discrepancies triggered by modifications, deletions, or additions of resources are promptly reported and, if configured, can be automatically remediated. Alerts can be configured to be sent via webhooks, Slack, or Microsoft Teams, with detailed information about the drift's nature and scope provided directly within the alerts.

      - header: Can you use drift detection without Pulumi Deployments?
        content: |
          Yes, you can configure your existing CI/CD system to run `pulumi refresh --preview-only` regularly, and the results will still be displayed as part of the Drift tab in Pulumi Cloud and you can receive notifications when drift is detected.

      - header: What granularity can you define schedules for Scheduled Deployments?
        content: |
          You can define schedules for any stack at the granularity of cron expressions.

# TODO: updates to these CTAs
learn:
    title: Get Started
    items:
        - title: Try Pulumi Copilot today
          description: Deploy infrastructure on any cloud by creating a free Pulumi account.
          buttons:
            - link: https://app.pulumi.com/signup
              type: primary
              action: Sign up for Pulumi Cloud
        - title: Documentation
          description: Review our documentation to learn more about Pulumi Deployments.
          buttons:
            - link: /docs/pulumi-cloud/deployments
              type: secondary
              action: Pulumi Deployments Docs
            - link: /docs/reference/deployments-rest-api
              type: secondary
              action: REST API Docs

aliases:
    - /copilot
---
