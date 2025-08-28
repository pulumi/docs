---
title: "Introducing Automatic API Docs in Private Registry"

date: 2025-08-27T00:00:05-06:00

draft: false

meta_desc: "Auto-generate API docs for infrastructure components in Pulumi Private Registry."

# The meta_image appears in social-media previews and on the blog home page. A
# placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: meta.png

authors:
    - idp-team

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
    - idp
    - private-registry
    - infrastructure-components
    - platform-engineering

social:
    twitter: |
        Your infrastructure components now document themselves.
        Publish to your Pulumi private registry → get instant multi-language API docs.
        Platform teams, this one's for you ↓ 
        [link]

    linkedin: |
        🚀 New in Pulumi: Automatic API Documentation for Pulumi components
        Platform teams, we heard you. Managing infrastructure documentation shouldn't slow you down.
        Today's release brings two powerful capabilities to your private registry:
        ✨ Automatic API Documentation
        Every component you publish now gets comprehensive, multi-language API docs, automatically generated and always in sync. Your Python components show TypeScript developers TypeScript examples. No manual documentation needed.
        From discovery to deployment, your teams get the resources they need without the friction.
        See what's possible when infrastructure sharing just works → [link]
        #PlatformEngineering #DevOps #InfrastructureAsCode #IaC

---

Building and maintaining reusable infrastructure has always been about more than just writing good code. It's about making that code discoverable, understandable, and easy to adopt across your organization. Today, we're excited to announce a new feature that removes significant friction from sharing and consuming [infrastructure components](/docs/concepts/resources/components/): automatic multi-language API documentation in [Pulumi Private Registry](/docs/idp/get-started/private-registry/).

<!--more-->

## The Challenge of Sharing Infrastructure at Scale

[Platform teams](/product/internal-developer-platforms/) invest significant effort in creating [reusable infrastructure components](/docs/idp/best-practices/patterns/). But creating the infrastructure is only half the battle. The real challenge comes in making these resources discoverable and usable by development teams across the organization.

Until now, platform teams publishing components faced a discovery challenge. While developers get excellent IDE support with autocomplete once they're coding, teams first need to know what components exist, understand their capabilities, and evaluate which one fits their needs. Without browsable API documentation in the registry, developers couldn't easily discover available components or compare versions. Security and compliance teams lacked visibility into what infrastructure patterns were being shared. And platform teams had no central place to showcase their catalog of approved, battle-tested components that encode organizational best practices.

## From Code to Comprehensive Docs

Starting today, whenever you publish a component to your Pulumi private registry, whether it's a brand new component or an updated version, Pulumi automatically generates comprehensive API documentation for all of the component's resources.

### How It Works

When you run `pulumi package publish` for your component, we analyze your component's structure, inputs, outputs, and resources to generate rich, interactive API documentation. This documentation is immediately available in your private registry, formatted consistently across all Pulumi-supported languages.

### Multi-Language Support Out of the Box

One of Pulumi's core strengths is our [multi-language components](/blog/pulumi-components/): write once in your preferred language, and teams can consume the component in [Python, TypeScript, Go, C#, Java, or YAML](/docs/languages-sdks/). The automatic documentation generation embraces this philosophy.

When you [publish a component](/docs/idp/get-started/publishing-from-github-actions/) written in Python, developers using TypeScript can view the TypeScript-specific documentation. The same component shows Go developers idiomatic Go code. This language-specific documentation removes the last barrier to [cross-team component adoption](/docs/idp/best-practices/patterns/components-using-other-components/).

![Multi-language component support](multi-lang-apis.jpg)

### Improving Discoverability and Adoption

With automatic API documentation, your [private registry](/blog/announcing-pulumi-private-registry/) transforms from a simple package repository into a comprehensive catalog. Developers can:

* Browse available components and immediately understand their purpose and usage
* See all available configuration options with type information
* Understand the resources that will be created without diving into implementation details

This dramatically reduces the time from component discovery to successful deployment, accelerating your organization's [infrastructure velocity](/blog/platform-engineering-pillars-2/).

## Getting Started

Automatic API docs are available today for all [Pulumi Cloud](/product/pulumi-cloud/) customers with access to private registry. To start generating docs, simply [publish your component](/docs/idp/get-started/private-registry/#publishing-components). Documentation generation happens automatically with no configuration required, and docs will automatically appear for existing components.

## Looking Ahead

Automatic API docs represent our continued investment in making Pulumi the most productive platform for infrastructure teams. By removing friction from the component lifecycle, we're enabling platform teams to focus on what matters most: building robust, secure, and scalable [infrastructure patterns](/docs/idp/best-practices/patterns/) that accelerate their entire organization.

We're excited to see how teams use them to build more effective [internal developer platforms](/blog/announcing-pulumi-idp/). As always, we'd love to hear your feedback and learn about your use cases on our [Pulumi Cloud requests repository](https://github.com/pulumi/pulumi-cloud-requests).

Ready to streamline your infrastructure development workflow? Get started with [Pulumi Cloud](https://app.pulumi.com/signup) or check out our [IDP documentation](/docs/idp/get-started/) to learn more about [building with components](/docs/idp/best-practices/four-factors/) and [workflows](/docs/idp/get-started/workflows/).
