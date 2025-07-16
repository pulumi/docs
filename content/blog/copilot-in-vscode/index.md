---
title: "Pulumi Copilot is Now Available in VS Code"

# The date represents the post's publish date, and by default corresponds with
# the date and time this file was generated. Dates are used for display and
# ordering purposes only; they have no effect on whether or when a post is
# published. To influence the ordering of posts published on the same date, use
# the time portion of the date value; posts are sorted in descending order by
# date/time.
date: 2025-02-03

# The draft setting determines whether a post is published. Set it to true if
# you want to be able to merge the post without publishing it.
draft: false

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or
# social-media previews. This field is required or the build will fail the
# linter test. Max length is 160 characters.
meta_desc: "Pulumi Copilot is now available in Visual Studio Code Copilot- offload tasks to Copilot right in your IDE by typing @pulumi in VS Code Copilot chat."

# The meta_image appears in social-media previews and on the blog home page. A
# placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: meta.png

# At least one author is required. The values in this list correspond with the
# `id` properties of the team member files at /data/team/team. Create a file for
# yourself if you don't already have one.
authors:
    - meagan-cojocar
    - eron-wright

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
    - releases
    - features

# The social copy used to promote this post on Twitter and Linkedin. These
# properties do not actually create the post and have no effect on the
# generated blog page. They are here strictly for reference.

social:
    twitter: "🎉 Pulumi Copilot is now available in Visual Studio Code! Offload tasks to Pulumi Copilot right in your IDE by typing @pulumi in Copilot Chat. Build, deploy, and manage cloud infrastructure more efficiently than ever."
    linkedin: "Exciting news! Pulumi Copilot is now available in Visual Studio Code Copilot, bringing AI-powered cloud infrastructure management directly to your IDE. Simply install the Pulumi extension and type @pulumi in Copilot Chat to access Pulumi's cloud intelligence and streamline your infrastructure workflows. 
    
    Learn how Pulumi Copilot is revolutionizing cloud development: [Link]"

---
Programming languages offer dozens of advantages for writing Infrastructure as Code (IaC). One of them is that Large Language Models are  effective at using general-purpose programming languages, thanks to the vast amount of high-quality training data available. Building on this advantage, we introduced Pulumi AI and Pulumi Copilot last year to enhance Infrastructure-as-Code development with generative AI capabilities. These tools have significantly streamlined infrastructure deployment for tens of thousands of developers.

Today, we are thrilled to announce that Pulumi Copilot is now available directly within [Visual Studio Code Copilot](https://marketplace.visualstudio.com/items?itemName=pulumi.pulumi-vscode-copilot). By simply typing @pulumi in Copilot Chat, developers can now access the power of Pulumi Copilot right within their IDE, saving them time on writing IaC and getting infrastructure deployed.

<!--more-->
## Video Walk Through

Hear Adam and Eron from Pulumi walk through this new feature in our PulumiTV introduction to the Visual Studio Code extension.

{{< youtube qdwIImlI-rA >}}

## What is Pulumi Copilot?

Pulumi Copilot is an AI-powered conversational assistant that seamlessly integrates with Pulumi Cloud, helping users:

* Explore and manage cloud infrastructure
* Gain insights into resources, policies, and deployments
* Troubleshoot errors and optimize configurations
* Author and deploy Pulumi IaC more effectively

Pulumi Copilot combines industry-leading AI models with Pulumi specific knowledge like the latest versions of providers, IaC best practices, and context from Pulumi Cloud on your environment.

### The Pulumi Copilot REST API

The [Pulumi Tools Visual Studio Code extension](https://marketplace.visualstudio.com/items?itemName=pulumi.pulumi-vscode-copilot) is powered by the recently announced [Pulumi Copilot REST API](/blog/pulumi-copilot-rest), which enables developers to integrate Pulumi Copilot's capabilities into their own tools and platforms. Just as we've built this extension to bring Pulumi Copilot directly into your development environment, you can use the same REST API to create your own innovative integrations, whether that's a custom CLI tool, a chat bot, or another IDE extension. The API's support for multi-turn conversations and contextual understanding makes it possible to build rich, interactive experiences like the one we're delivering today.

## How to Use Pulumi Copilot in Visual Studio Code

Using Pulumi Copilot in Visual Studio Code (VS Code) is as simple as 1-2-3:

1. Install the [Pulumi VS Code extension](https://marketplace.visualstudio.com/items?itemName=pulumi.pulumi-vscode-copilot-tools)
2. Open VS Code and navigate to Copilot Chat (icon to the right of the search bar)
3. Type `@pulumi` to activate Pulumi Copilot

You can then ask questions about your infrastructure, generate code, check deployment status, debug Pulumi errors, and more.

This seamless integration brings Pulumi's intelligence directly into the developer workflow.

Pulumi Copilot respects all role-based access control (RBAC) settings in Pulumi Cloud, ensuring that AI-generated responses are scoped only to authorized users within an organization.

## Key Use Cases

Let's explore four powerful ways to use Pulumi Copilot in VS Code:

### Infrastructure Code Generation

With Pulumi Copilot in VS Code, developers can generate Pulumi programs for new use cases, solving the blank page problem and getting you from 0 to 0.9.

Simply describe what you want to build and Pulumi Copilot will generate the infrastructure code for you. For example, ask "Create an AWS S3 bucket with versioning enabled and encrypted with a KMS key" and Copilot will generate the complete Pulumi program. Or ask Pulumi Copilot to extend an existing project such as adding a ManagedNodeGroup to your AWS EKS cluster.

### Terraform to Pulumi Migration

Migrating from Terraform to Pulumi? Just point Copilot at your Terraform files and ask it to convert them. For example:

1. Open your `main.tf` file in VS Code
2. Type `@pulumi convert this Terraform configuration to TypeScript`
3. Copilot will analyze your Terraform code and generate equivalent Pulumi code in `index.ts`

The conversion maintains your existing resource configurations while taking advantage of Pulumi's native programming language features.

### Resource Discovery

Pulumi Copilot can search across your entire infrastructure to find resource usage patterns. Ask questions like "Do we use AWS Lambda functions in any other stacks?" or "Show me all S3 buckets with public access enabled." Copilot will search your codebase and Pulumi Cloud to provide comprehensive answers about your infrastructure.

### Error Resolution

When you encounter errors in the terminal during Pulumi operations, Copilot can help explain and resolve them. Simply copy the error message and ask Copilot to explain it. For example:

```bash
Error: Error creating S3 Bucket (my-bucket): BucketAlreadyExists: The requested bucket name is not available
```

Copilot will explain the error in plain language, suggest potential solutions, provide code examples for fixing the issue, and reference similar issues from your organization's history.

## Getting Started

Pulumi Copilot is free to use for all organizations in Pulumi Cloud. Organization administrators can enable Pulumi Copilot by navigating to:
Settings > Access Management > Pulumi Copilot in the Pulumi Cloud console.

Try it now in VS Code and experience AI-driven cloud infrastructure management right in your IDE.

[👉 Start Using Pulumi Copilot](https://app.pulumi.com)
[👉 Start Using Pulumi Copilot in Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=pulumi.pulumi-vscode-copilot-tools)

We can't wait to see what you build with Pulumi Copilot! 🚀
