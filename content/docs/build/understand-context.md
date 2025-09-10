---
title: Understand Pulumi Context
h1: Understand Pulumi Context
capability: build
menu:
    build:
        name: Understand Pulumi Context
        identifier: build-understand-context
        parent: build-core-concepts
        weight: 70
meta_desc: Understand Pulumi in context of other tools like Terraform, CloudFormation, and AWS CDK. Learn migration strategies and when to use Pulumi.
meta_image: /images/docs/meta-images/docs-meta.png
---

Understand how Pulumi compares to other infrastructure tools and when to use Pulumi for your infrastructure needs. Learn about migration strategies and tool comparisons.

## vs. Terraform & OpenTofu

Compare Pulumi with Terraform and understand the key differences:

- [Pulumi vs. Terraform](/docs/iac/concepts/vs/terraform/) - Comprehensive comparison
- [Pulumi vs. OpenTofu](/docs/iac/concepts/vs/terraform/opentofu/) - OpenTofu-specific differences
- [Terraform terminology in Pulumi](/docs/iac/concepts/vs/terraform/terminology/) - Mapping concepts

## vs. CloudFormation & ARM Templates

Understand how Pulumi differs from cloud-native template languages:

- [Pulumi vs. CloudFormation](/docs/iac/concepts/vs/cloud-templates/cloudformation/) - AWS comparison
- [Cloud templates overview](/docs/iac/concepts/vs/cloud-templates/) - General cloud templates comparison

## vs. AWS CDK

Compare Pulumi with AWS CDK and other cloud development kits:

- [Pulumi vs. AWS CDK](/docs/iac/concepts/vs/cloud-template-transpilers/aws-cdk/) - CDK-specific comparison
- [Cloud template transpilers](/docs/iac/concepts/vs/cloud-template-transpilers/) - CDK and similar tools

## Migration Strategy

Learn when and how to adopt Pulumi from other tools:

- [Adopting Pulumi](/docs/iac/adopting-pulumi/) - Migration strategy overview
- [Import existing resources](/docs/iac/adopting-pulumi/import/) - When and why to import existing infrastructure
- [Migration tools](/docs/pulumi-cli/) - Technical migration utilities and tools

## Key Pulumi Advantages

Understanding why developers choose Pulumi:

- **Use familiar languages**: TypeScript, Python, Go, C#, Java, YAML
- **Full programming language features**: Loops, conditionals, functions, classes
- **Rich ecosystem**: Package managers, IDEs, testing frameworks
- **Multi-cloud by default**: Same tools and languages across all clouds
- **Infrastructure as software**: Not just configuration, but real software engineering practices

## When to Choose Pulumi

Pulumi is particularly well-suited for:

- **Complex infrastructure**: When you need loops, conditionals, or advanced logic
- **Multi-cloud deployments**: Managing infrastructure across multiple cloud providers
- **Developer-focused teams**: When infrastructure teams want to use familiar programming languages
- **Component reuse**: Building and sharing reusable infrastructure components
- **Integration with application code**: When infrastructure and application development are tightly coupled

## Getting Started

Ready to try Pulumi? Start here:

- [Install Pulumi](/docs/iac/download-install/) - Get up and running
- [Your first stack](/docs/iac/get-started/) - Deploy your first infrastructure
- [Choose your language](/docs/iac/languages-sdks/) - Pick your preferred programming language
