---
title_tag: "Terraform vs. Pulumi"
meta_desc: Pulumi and Terraform have a few similarities, but they differ in many key ways. This page helps provide a rundown of these major differences.
title: Terraform
h1: Terraform vs. Pulumi
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Terraform
        parent: iac-concepts-compare
        weight: 1
        identifier: iac-concepts-compare-terraform
    concepts:
        identifier: vs-terraform
        parent: vs
        weight: 1
aliases:
- /docs/reference/vs/terraform/
- /docs/intro/vs/terraform/
- /docs/concepts/vs/terraform/
---

<style>
    main table {
        font-size: 0.94em;
    }

    main table th,
    main table td {
        width: 33.3%;
    }
</style>

<div class="rounded shadow-md" style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
    <iframe
        src="//www.youtube.com/embed/PqAP4BunQZU?rel=0"
        style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border:0;"
        allowfullscreen=""
        title="Pulumi + AWS: Universal Infrastructure as Code"
    ></iframe>
</div>

## Your Infrastructure, Your Programming Language, Your Way

Infrastructure as code shouldn't force you to learn yet another language. While Terraform requires learning HCL and is not open source (using the Business Source License), Pulumi takes an open-source, developer-first approach with Apache 2.0 licensing. With Pulumi, you can:

- **Use Existing Skills**: Write infrastructure code in Python, TypeScript, Java, .NET, or Go
- **Leverage Modern Tools**: Get full IDE support with code completion and error checking
- **Build with Confidence**: Access your language's entire ecosystem of libraries and tools
- **Work Your Way**: Choose between CLI, APIs, or embedding in your applications

## At a Glance

- 🔧 **Terraform**: Proprietary HCL language, Business Source License, community-supported providers
- 💻 **Pulumi**: Open source (Apache 2.0), mainstream languages, native cloud provider integration
- **Key Differences**:
  - Write infrastructure code in your team's preferred language
  - Full IDE support with code completion and type checking
  - Enhanced security with built-in secret encryption
  - Same-day support for new cloud features
  - Built-in testing frameworks
  - Advanced automation capabilities

## True Programming Language Freedom

Pulumi's deep integration with mainstream programming languages isn't just about syntax preferences – it's about unlocking the full power of modern development:

- **Python**: Leverage NumPy for calculations, Pandas for data processing
- **TypeScript/JavaScript**: Use npm packages, async/await for complex orchestration
- **Java**: Utilize enterprise-grade frameworks and tools
- **Go**: Access powerful concurrency features and standard library
- **.NET**: Integrate with existing enterprise .NET ecosystems
- **YAML**: Available for teams preferring simpler configurations

## Developer-First Features

Pulumi brings modern development practices to infrastructure:

### Advanced Development Experience

- Full IDE support with code completion and error detection
- Integrated testing framework (unit, property, and integration tests)
- Dynamic Providers for custom resource types
- Transformations for programmatic resource customization

### Cloud Native Power

- 100% Kubernetes API coverage with type checking
- Native Helm 2/3 support
- Built-in YAML-to-Pulumi conversion
- Kubernetes operator for GitOps workflows

### Enterprise-Ready

- Audit logs for tracking user activity
- Team collaboration features
- Robust secret management with encryption
- CrossGuard for policy enforcement in your preferred language

## Migration and Integration

Making the switch is easier than you think:

- **Migration Tools**: Built-in converters from Terraform HCL to Pulumi
- **Side-by-Side Usage**: Reference existing Terraform state
- **Expert Support**: Access to migration services and training
- **Enterprise Support**: Bundled Terraform workspace migrations
- **Success Stories**: Major companies like Atlassian have successfully migrated

Looking to get started with Pulumi? Visit [Pulumi's documentation](https://www.pulumi.com/docs/) to begin your journey with modern infrastructure as code.
