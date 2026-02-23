---
title: "Four Factors: Templates, Components, Environments, and Policies"
linktitle: "The Four Factors Framework"
meta_desc: A framework for building with Pulumi IDP using Templates, Components, Environments, and Policies
allow_long_title: true
menu:
  idp:
    parent: idp-best-practices
    weight: 5
aliases:
  - /docs/idp/best-practices/four-factors/
---

This guide introduces a framework for building with Pulumi IDP that leverages four key factors to create secure, scalable, and flexible developer workflows. By understanding and effectively combining these factors, platform teams can build robust internal developer platforms that enable developers to provision infrastructure efficiently while maintaining compliance and security.

## Templates

[Templates](/docs/idp/concepts/organization-templates/) are user-configurable scaffolding that creates new instances of infrastructure resources. They serve as the entry point for developers to quickly bootstrap new projects or components with pre-configured settings and best practices baked in.

Key characteristics:

- **User-configurable**: Developers can customize templates through simple parameters
- **Stack creation**: Each time a template is used it creates one or more new, independent [Pulumi stacks](/docs/iac/concepts/stacks/)
- **Standardized starting point**: Ensures consistent project structure and configuration
- **Low barrier to entry**: Enables developers to get started quickly without deep infrastructure knowledge

Templates abstract away the complexity of initial setup while providing flexibility for customization based on specific use cases.

## Components

[Components](/docs/iac/concepts/components/) are reusable building blocks that abstract and encapsulate business logic, set sensible defaults, limit inputs, and encode company standards. They represent the core infrastructure primitives that your organization uses repeatedly.

Key characteristics:

- **Business logic abstraction**: Hide complex infrastructure patterns behind simple interfaces
- **Sensible defaults**: Provide secure, compliant defaults out of the box
- **Limited inputs**: Reduce cognitive load by exposing only necessary configuration options
- **Company standards**: Encode organizational policies and best practices directly in code

Components enable platform teams to create opinionated infrastructure building blocks that developers can use confidently, knowing they follow organizational standards.

## Environments

[Environments](/docs/esc/environments/) provide credentials and configuration for your needs through composable, secure configuration management. They ensure that the right secrets and settings are available to the right workloads at the right time.

Key characteristics:

- **Least privilege**: Provide only the credentials and configuration needed for specific contexts
- **Composable**: Mix and match environment configurations based on deployment context
- **Secure**: Centrally manage and rotate secrets without exposing them in code
- **Context-aware**: Automatically apply the right configuration based on environment (staging, production, etc.)

Environments eliminate the need for developers to manage complex credential and configuration scenarios while maintaining security best practices.

## Policies

[Policies](/docs/insights/policy/) ensure continued compliance with company requirements through automated validation. They provide guardrails that prevent misconfigurations and enforce organizational standards across all infrastructure deployments.

Key characteristics:

- **Automated validation**: Continuously check infrastructure configurations against defined rules
- **Compliance assurance**: Prevent deployments that violate organizational policies
- **Consistent enforcement**: Apply the same rules across all environments and teams
- **Proactive prevention**: Catch issues before they reach production

Policies act as a safety net, ensuring that even as infrastructure scales and evolves, it remains compliant with organizational requirements.

## Bringing It All Together

The power of Pulumi IDP comes from combining these four factors into cohesive developer workflows. Here's how they work together in practice:

### Example: Deploying a Web Site

Consider a developer who needs to deploy a new web site hosted in a S3 bucket. Here's how the four factors collaborate:

- **Template**: The developer starts with a `web-site` template that scaffolds a new project with the necessary structure and dependencies.
- **Component**: The template uses a custom `TaggedBucket` component that automatically:
   - Creates an S3 bucket with secure defaults and user provided content
   - Applies required organizational tags (like `user:Stack`)
   - Configures appropriate access policies
- **Environment**: Based on the stack name, different ESC environments are automatically applied:
   - `staging` stack uses AWS credentials for `us-west-2` region
   - `production` stack uses AWS credentials for `us-east-1` region
- **Policy**: Pulumi Policies automatically validate the deployment:
   - Ensures the `user:Stack` tag is present on all resources
   - Ensures access policies meet organizational security standards
   - Blocks deployment if compliance requirements aren't met

### Developer Experience

From the developer's perspective, they only need to:

1. Create a new project from the web-site template
2. Answer a few configuration questions
3. Run `pulumi up`

Behind the scenes, the four factors work together to apply the correct environment configuration, use secure and compliant components, enforce organizational policies, and provide a consistent and reliable deployment experience.

### Benefits

This approach delivers several key benefits:

- **Reduced complexity**: Developers don't need to understand the intricacies of infrastructure configuration
- **Consistent compliance**: Policies ensure all deployments meet organizational standards
- **Secure by default**: Components and environments provide secure defaults and credential management
- **Scalable governance**: Platform teams can update templates, components, and policies centrally

By leveraging these four factors together, organizations can create internal developer platforms that balance developer productivity with operational requirements, security, and compliance.

## Learn More

To see how these four factors can be used together in some common use cases, check out our [patterns](/docs/idp/guides/best-practices/patterns) library.

### Additional Resources

- [Pulumi IDP Concepts](/docs/idp/concepts)
- [Private Registry](/docs/idp/concepts/private-registry)
- [No-code Stacks](/docs/idp/concepts/no-code-stacks)
