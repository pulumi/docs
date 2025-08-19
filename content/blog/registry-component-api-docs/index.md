---
title: "Streamline Platform Engineering with Automatic API Documentation and Registry-Backed Templates"

date: 2025-08-21T00:00:05-06:00

draft: false

meta_desc: "Auto-generate API docs for infrastructure components and publish templates directly to your private registry. No manual documentation or GitHub required."

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
    - infrastructure-templates
    - platform-engineering


# The social copy used to promote this post on Twitter and Linkedin. These
# properties do not actually create the post and have no effect on the
# generated blog page. They are here strictly for reference.

# Here are some examples of posts we have made in the past for inspiration:
# https://www.linkedin.com/feed/update/urn:li:activity:7171191945841561601
# https://www.linkedin.com/feed/update/urn:li:activity:7169021002394296320
# https://www.linkedin.com/feed/update/urn:li:activity:7155606616455737345
# https://twitter.com/PulumiCorp/status/1763265391042654623
# https://twitter.com/PulumiCorp/status/1762900472489185492
# https://twitter.com/PulumiCorp/status/1755637618631405655

social:
    twitter: |
        Your infrastructure components now document themselves.
        Publish to your Pulumi private registry → get instant multi-language API docs.
        Plus: templates now live directly in your registry. No GitHub setup needed.
        Platform teams, this one's for you ↓ 
        [link]

    linkedin: |
        🚀 New in Pulumi: Automatic API Documentation & Registry-Backed Templates
        Platform teams, we heard you. Managing infrastructure documentation and template distribution shouldn't slow you down.
        Today's release brings two powerful capabilities to your private registry:
        ✨ Automatic API Documentation
        Every component you publish now gets comprehensive, multi-language API docs—automatically generated, always in sync. Your Python components show TypeScript developers TypeScript examples. No manual documentation needed.
        📦 Registry-Backed Templates
        Publish templates directly to your private registry with semantic versioning. No more GitHub repositories just for template distribution. One CLI command and your golden paths are available to every team.
        Together, these features transform your private registry into a complete infrastructure sharing platform. From discovery to deployment, your teams get the resources they need without the friction.
        See what's possible when infrastructure sharing just works → [link]
        #PlatformEngineering #DevOps #InfrastructureAsCode #IaC #CloudNative

# See the blogging docs at https://github.com/pulumi/docs/blob/master/BLOGGING.md
# for details, and please remove these comments before submitting for review.
---

Building and maintaining reusable infrastructure has always been about more than just writing good code—it's about making that code discoverable, understandable, and easy to adopt across your organization. Today, we're excited to announce two new features that remove significant friction from sharing and consuming infrastructure components and templates: automatic API documentation generation and registry-backed templates.

<!--more-->

## The Challenge of Sharing Infrastructure at Scale

Platform teams invest significant effort in creating reusable infrastructure components and templates. But creating the infrastructure is only half the battle. The real challenge comes in making these resources discoverable and usable by development teams across the organization.

Until now, teams faced two key pain points:

**Documentation Drift**: When platform teams publish components to their private registry, developers still had to figure out how to use them. Without proper API documentation, developers resort to reading source code or pinging the platform team on Slack—neither of which scales. Even when documentation exists, keeping it synchronized with the actual component implementation becomes yet another maintenance burden.

**Template Distribution Complexity**: Sharing Pulumi templates required pushing them to GitHub and configuring the Pulumi GitHub app to discover them. This added unnecessary complexity to what should be a simple process.

## Automatic API Documentation: From Code to Comprehensive Docs

Starting today, whenever you publish a component to your Pulumi private registry—whether it's a brand new component or an updated version—Pulumi automatically generates comprehensive API documentation for all of the component's resources.

### How It Works

When you run pulumi package publish for your component, we analyze your component's structure, inputs, outputs, and resources to generate rich, interactive API documentation. This documentation is immediately available in your private registry, formatted consistently across all Pulumi-supported languages.

### Multi-Language Support Out of the Box

One of Pulumi's core strengths is our multi-language components—write once in your preferred language, and teams can consume the component in Python, TypeScript, Go, C#, Java, or YAML. The automatic documentation generation embraces this philosophy.

When you publish a component written in Python, developers using TypeScript can view the TypeScript-specific documentation. The same component shows Go developers idiomatic Go code. This language-specific documentation removes the last barrier to cross-team component adoption.

### Improving Discoverability and Adoption

With automatic API documentation, your private registry transforms from a simple package repository into a comprehensive infrastructure catalog. Developers can:

* Browse available components and immediately understand their purpose and usage
* See all available configuration options with type information
* Understand the resources that will be created without diving into implementation details

This dramatically reduces the time from component discovery to successful deployment, accelerating your organization's infrastructure velocity.

## Registry-backed Templates: Simple Publishing and Versioning

Templates are one of the most effective ways for platform teams to provide golden paths—pre-configured, best-practice infrastructure patterns that developers can deploy with minimal configuration. However, the previous workflow for sharing templates created unnecessary friction. Today, that changes.

You can now publish templates directly to your private registry using the Pulumi CLI, without any GitHub integration required:

```bash
pulumi template publish ./path-to-template --name my-template --version 1.0.0
```

That's it. No GitHub repository setup, no app configuration, no webhook management. Your template is immediately available in your private registry, ready for teams to discover and use.

### Seamless Integration Across Pulumi

Registry-backed templates are now first-class citizens throughout the Pulumi experience. They appear alongside other templates in the New Project Wizard, whether you're using Pulumi Deployments or CLI deployment workflows. Teams can discover and use them through the familiar Pulumi UI or directly from the command line.

### Self-Contained Templates

When you publish a template to the registry, Pulumi stores the complete template content—not just a reference to a git repository. This means there are no external dependencies on GitHub, and templates remain available even if the source repository is deleted or moved.

## Getting Started

Both features are available today for all Pulumi Cloud customers with access to private registries. To start using them:

### Automatic API Documentation

Simply publish or update any component in your private registry. Documentation generation happens automatically—no configuration required.

### Registry-Backed Templates

Update to the latest Pulumi CLI and use the pulumi package publish command with your template:

```bash
pulumi template publish ./path-to-template --name my-template --version 1.0.0
Publishing template my-org/my-template@1.0.0...
Successfully published template my-org/my-template@1.0.0
```

#### Using Registry Templates

With the latest CLI, you can create new projects from registry-backed templates using flexible URL formats:

```bash
pulumi new my-template
```

`my-template` is short for a registry URL. If you have a template in the registry called `my-template`, these are equivalent:

```bash
my-template
my-org/my-template
private/my-org/my-template
registry://templates/private/my-org/my-template
```

Versions can be used by appending `latest` or a concrete version `1.0.0` to the template used. If a version isn't passed, `latest` is assumed.

## Looking Ahead

These features represent our continued investment in making Pulumi the most productive platform for infrastructure teams. By removing friction from the component and template lifecycle, we're enabling platform teams to focus on what matters most: building robust, secure, and scalable infrastructure patterns that accelerate their entire organization.

We're excited to see how teams use these features to build more effective infrastructure development platforms. As always, we'd love to hear your feedback and learn about your use cases.

Ready to streamline your infrastructure development workflow? Get started with [Pulumi Cloud](https://app.pulumi.com/signup) or check out our [documentation](/docs/idp/get-started/private-registry/) to learn more.
