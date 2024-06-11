---
title: Pulumi Copilot
layout: copilot

meta_desc: Pulumi Copilot is a virtual teammate that automates management of any cloud

overview:
    title: Virtual Teammate that Automates Management of Any Cloud
    description: |
        Pulumi Copilot is a LLM-based assistant that automates any infrastructure management task. Copilot combines the power of large language models with semantic understanding of the cloud to unlock greater insights and controls over managing cloud infrastructure. Using the same GPT experience everyone knows, loves, and uses everyday, engineers can find anything in their cloud infrastructure and take action on any cloud resource. Pulumi Copilot lowers the barriers of managing the lifecycle of cloud infrastructure. 

get_started: Get Started with Copilot

benefits:
    title: How do I use Pulumi Copilot?
    description: |
        Pulumi Copilot is an interactive user interface in Pulumi Cloud, Pulumi documentation, and Pulumi CLI.
        
        Pulumi Copilot understands the entirety of over 160 clouds, including public clouds (AWS, Azure, Google Cloud), cloud native (Kubernetes, Helm), SaaS providers (Snowflake, Cloudflare, Datadog), and more. Pulumi Copilot directly interfaces with these cloud APIs and data models.
        
        Simply ask any question, and Copilot will provide relevant, contextual, and effective responses to queries across the entire platform.

        Pulumi Copilot is in beta, and some of the answers may be inaccurate. Please send us your feedback so we can continue to improve the experience by typing `/bug` into Copilot or filing an [issue](https://github.com/pulumi/pulumi/issues/new/choose) in GitHub.
    graphic:
        image: /images/product/copilot-demo.mp4
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
          No. We are using Azure’s OpenAI APIs for our text generation and are not using either a self-finetuned model or Azure’s finetuning product.  
          
          Learn more by reviewing [Azure’s OpenAI data privacy policy](https://learn.microsoft.com/en-us/legal/cognitive-services/openai/data-privacy#how-does-the-azure-openai-service-process-data)

      - header: Can I turn Pulumi Copilot off for my organization?
        content: |
          If your organization has compliance policies preventing you from using Large Language Models, you can turn Pulumi Copilot off in your organization by navigating to Organization Settings > Access Management > Pulumi Copilot.  

      - header: Can Copilot make changes or is it limited to read-only scenarios?
        content: |
          At this time Pulumi Copilot can only perform read operations, such as making GET requests on the user's behalf. If you ask Pulumi Copilot to perform an action, such as making a member an admin, it will confirm it is not able to. 

      - header: Does Copilot send my secrets to the Azure OpenAI API?
        content: |
          No, the only data sent to the Azure OpenAI API is the user prompt. We do not share any information with the model about your Pulumi state file, we make API calls on your behalf that may surface this information in the response. If you provide secrets in your prompt they will be sent to Azure, and similarly if you have unencrypted secrets in your state file, the model could see portions of it in an API response. 

      - header: Will Pulumi Copilot maintain a history of the organization’s conversations?
        content: |
          Yes, Pulumi Copilot will maintain a history of conversations for all users in an organization. Pulumi requires access to these conversations in order to ensure the best experience for customers. This allows Pulumi to manage support requests that may come up as well as evaluate the customer experience to identify areas for improvement in the future.

      - header: What are the models used for Pulumi Copilot?
        content: |
          Pulumi Copilot uses private, paid enterprise versions of Microsoft Azure OpenAI models. 

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
