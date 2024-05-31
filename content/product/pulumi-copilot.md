---
title: Pulumi Copilot
layout: pulumi-copilot

meta_desc: Pulumi Deployments is an infrastructure lifecycle management service for automating the deployment and management of cloud infrastructure

overview:
    title: Infrastructure lifecycle management
    description: |
        Pulumi Deployments is an infrastructure lifecycle management service. It provides automation of deployment and operational workflows for cloud infrastructure. With Pulumi Deployments, you can orchestrate with ease the at-scale complexities of production infrastructure.

get_started: Get Started with Copilot

benefits:
    title: How will Pulumi Deployments benefit me?
    description: |
        Pulumi Deployments makes it easier for you and engineers on your team to manage the entire lifecycle of infrastructure from provisioning to tear down. You can choose from different workflows such as GitHub pull request triggered deployments, stacks with time based automatic deletions, scheduled automations, and more.

        You can also orchestrate custom workflows with [Automation API](/docs/using-pulumi/automation-api/) and offload the workflow execution to Pulumi Deployments instead of running the Automation API code locally yourself. Pulumi Deployments is a fully managed service with minimal setup and is available through [Pulumi Cloud](/product/pulumi-cloud/).

options:
    title: How can I use Pulumi Deployments today?
    description:
    items:
        - icon: git-merged
          icon_color: purple
          title: Git Push to Deploy
          description: Deploy infrastructure with each [push to a GitHub branch](/docs/pulumi-cloud/deployments/reference/#github-push-to-deploy), using pull requests to review changes in ephemeral [Review Stacks](/docs/pulumi-cloud/deployments/review-stacks/) before deploying them.
        - icon: upload-to-cloud
          icon_color: salmon
          title: Click to Deploy
          description: Deploy infrastructure with a click of a button from the Pulumi Cloud console. Run update, preview, refresh, and destroy commands.
        - icon: code-window
          icon_color: blue
          title: REST API
          description: Deploy infrastructure by calling the Pulumi Service REST API. You can also use the API to run [Remote Automation API](/docs/pulumi-cloud/deployments/reference/#rest-api) code.
        - icon: eye
          icon_color: fuchsia
          title: Review Stacks
          description: Automate the creation and deletion of dedicated cloud environments for every pull request, enabling cost-effective reviews.
        - icon: lightning
          icon_color: violet
          title: TTL Stacks
          description: Automatically cleanup infrastructure with self-destroying (automatic deletion) stacks.
        - icon: clock
          icon_color: yellow
          title: Scheduled Deployments
          description: Automate cloud operations (update, refresh, destroy) on defined schedules using cron expressions.

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


learn:
    title: Get Started
    items:
        - title: Try Pulumi Deployments today
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
