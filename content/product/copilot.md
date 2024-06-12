---
title: Pulumi Copilot
layout: copilot

meta_desc: Pulumi Copilot is an AI-powered assistant for general cloud infrastructure management

overview:
    title: Intelligent Cloud Management
    description: |
        Pulumi Copilot is an AI-powered assistant that automates any infrastructure management task. Copilot combines the power of large language models with semantic understanding of the cloud to unlock greater insights and controls over managing cloud infrastructure. Using the same GPT experience everyone knows, loves, and uses everyday, engineers can find anything in their cloud infrastructure and take action on any cloud resource. Pulumi Copilot lowers the barriers of managing the lifecycle of cloud infrastructure. 

get_started: Get Started with Copilot

benefits:
    title: How do I use Pulumi Copilot?
    description: |
        Pulumi Copilot is an interactive user interface in the Pulumi Cloud console and the Pulumi CLI.
        
        Pulumi Copilot understands the entirety of over 160 clouds, including public clouds (AWS, Azure, Google Cloud), cloud native (Kubernetes, Helm), SaaS providers (Snowflake, Cloudflare, Datadog), and more. Pulumi Copilot directly interfaces with these cloud APIs and data models.
        
        Simply ask any question, and Copilot will provide relevant, contextual, and effective responses to queries across the entire platform.

        Pulumi Copilot is available in public beta, and is free while in beta. Organization admins can turn on Copilot in their organization **Settings > Access Management > Pulumi Copilot** within the Pulumi Cloud console.
        
        Some of the answers in Pulumi Copilot may be inaccurate. Please send us your feedback so we can continue to improve the experience by typing `/bug` into Copilot.
    graphic:
        image: https://www.pulumi.com/uploads/copilot-demo.mp4
        alt: Pulumi Copilot Demo

options:
    title: What are the use cases of Pulumi Copilot?
    description:
    items:
        - icon: upload-to-cloud
          icon_color: purple
          title: Generate infrastructure code
          description: You can generate a Pulumi program and deploy it as a template in seconds with a few simple text prompts.
          example: "Example:  Create a new project to deploy a serverless application on AWS"
          link: "https://app.pulumi.com/pulumi/?askCopilot=Create a new project to deploy a serverless application on AWS"
        - icon: eye
          icon_color: salmon
          title: Discover cost savings
          description: Copilot can access infrastructure stack and resource data, so you can analyze your infrastructure on cost, compliance, cloud usage.
          example: "Example:  What are my least used, most expensive resources?"
          link: "https://app.pulumi.com/pulumi/?askCopilot=What are my least used, most expensive resources?"
        - icon: shield
          icon_color: blue
          title: Run compliance checks
          description: You can analyze infrastructure for security and compliance concerns.
          example: "Example:  We are going through an internal security audit. Can you tell me any infrastructure that is not following AWS Well-Architected standards?"
          link: "https://app.pulumi.com/pulumi/?askCopilot=We are going through an internal security audit. Can you tell me any infrastructure that is not following AWS Well-Architected standards?"
        - icon: code-window
          icon_color: fuchsia
          title: Debug failed stack updates
          description: Copilot can access update and deployment logs of your stacks, so you can easily get answers about what caused failures.
          example: "Example:  Why did my deployment yesterday fail?"
          link: "https://app.pulumi.com/pulumi/?askCopilot=Why did my deployment yesterday fail?"

faq:
    items:
      - header: Will my data be used to train Pulumi Copilot?
        content: |
          No, Pulumi Copilot is not using either a self-fine tuned model or a fine tuning product, therefore today data is not being used to train Pulumi Copilot.

      - header: Can I turn Pulumi Copilot off for my organization?
        content: |
          Pulumi Copilot is off by default at public beta launch. Organization admins can turn it on by navigating to organization Settings > Access Management > Pulumi Copilot. You can make it available for all members, just admins or no one in your organization. It can be turned off at any point.  

      - header: Can Copilot make changes or is it limited to read-only scenarios?
        content: |
          At this time Pulumi Copilot can only perform read operations, such as making GET requests on the user's behalf. If you ask Pulumi Copilot to perform an action, such as making a member an admin, it will confirm it is not able to. 

      - header: What data does Pulumi Copilot send to Azure OpenAI API?
        content: |
          Pulumi Copilot transmits data to Pulumi’s Azure tenant to generate responses, including both contextual data and data about the user’s actions. The transmitted data is encrypted both in transit and at rest; Pulumi Copilot-related data is encrypted in transit using transport layer security (TLS). Furthermore, Pulumi Copilot does not have the ability to decrypt secrets, so no secret data is exposed to either users or the Pulumi’s Azure tenant by Pulumi Copilot.

      - header: What data is Pulumi Copilot storing?
        content: |
          Pulumi Copilot stores conversation data, similar to all other product metrics logging in Pulumi Cloud, including the response from Azure’s OpenAI API in order to debug issues and measure model quality. This data is treated sensitively and used only for operational purposes.

      - header: What model does Pulumi Copilot use?
        content: |
          Pulumi Copilot currently uses OpenAI GPT-4o, hosted in Azure OpenAI Service in a Pulumi owned and managed Azure subscription. Over time the expectation is that Copilot will use a combination of models to improve the user experience and answer quality.

learn:
    title: Get Started
    items:
        - title: Try Pulumi Copilot today
          description: Automate any infrastructure management task by creating a free Pulumi account.
          buttons:
            - link: https://app.pulumi.com/
              type: primary
              action: Try Copilot
        - title: Documentation
          description: Review our documentation to learn more about Pulumi Copilot.
          buttons:
            - link: /docs/pulumi-cloud/copilot
              type: secondary
              action: Pulumi Copilot Docs

aliases:
    - /copilot
---
