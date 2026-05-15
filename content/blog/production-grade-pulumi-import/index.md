---
title: "Pulumi Import for Real Production Estates"
date: 2026-07-07
meta_desc: "Use Pulumi import beyond demos with bulk import files, provider edge cases, state-only imports, and reviewable adoption workflows."
authors:
    - pablo-seibelt
tags:
    - pulumi-import
    - day-2
    - tutorial
meta_image: meta.png
feature_image: feature.png
social:
    twitter: |
        Pulumi import gets interesting at production scale: bulk files, state-only imports, third-party providers, and long-running adoption workflows.

        Learn more in the post.
    linkedin: |
        Production imports are rarely one-resource demos.

        This guide covers Pulumi import patterns for real estates: bulk import files, state-only imports, third-party providers, long-running operations, and reviewable adoption workflows.
    bluesky: |
        Pulumi import at production scale means bulk files, state-only imports, third-party providers, and careful adoption workflows.

        Learn more in the post.
---

Adopting existing infrastructure into Infrastructure as Code (IaC) is a common challenge for growing teams. The demand is clear from sustained community interest in import workflows and custom provider support. While the basic [`pulumi import`](/docs/iac/guides/migration/import/) command is great for a single S3 bucket, production environments often require importing many resources across multiple providers.

To move beyond simple demos, you need to understand the different import modes, how to handle bulk operations, and how to manage long-running adoptions without breaking your production stacks.

This post covers production-grade import strategies, including bulk import files, state-only imports, and common pitfalls when working with custom providers. By the end, you will have a playbook for mass infrastructure adoption using Pulumi's advanced import features.

<!--more-->

## The three modes of import

Pulumi provides three distinct ways to bring resources under management. Choosing the right one depends on whether you already have the code written or if you want Pulumi to generate it for you.

### 1. CLI import (state and code)

The standard [`pulumi import`](/docs/iac/cli/commands/pulumi_import/) command is the most common starting point. It performs two actions: it adds the resource to your stack state and prints the corresponding TypeScript, Python, Go, C#, Java, or YAML code to your terminal.

```bash
pulumi import aws:ec2/vpc:Vpc my-vpc vpc-0123456789abcdef0
```

By default, this command protects the resource from accidental deletion. You must copy the generated code into your program before your next `pulumi up` to ensure the state and code remain in sync.

### 2. Code-based import (code-only)

If you prefer to write your own resource definitions or if you are importing resources that already follow a specific pattern, you can use the `import` resource option.

```typescript
const vpc = new aws.ec2.Vpc("my-vpc", {
    cidrBlock: "10.0.0.0/16",
}, {
    import: "vpc-0123456789abcdef0",
});
```

This is a "code-only" approach because the CLI doesn't imperatively modify your state. Instead, the import happens during the next `pulumi up`. Once the resource is imported, you should remove the `import` option from your code to keep future updates focused on normal resource management.

### 3. State-only import

Sometimes you already have the code perfectly written, perhaps by copying it from another project or using a template, and you just want to link it to an existing resource without seeing the generated code again. You can use the `--generate-code=false` flag for this.

```bash
pulumi import aws:ec2/vpc:Vpc my-vpc vpc-0123456789abcdef0 --generate-code=false
```

This updates the state file directly, assuming your code already matches the resource configuration. After import, the resource is managed like any other Pulumi resource, so keep protection in place until the team intentionally owns delete behavior and consider `retainOnDelete` for resources that must survive stack destruction.

## Bulk imports with import files

Importing resources one by one is tedious and error-prone. For large-scale adoptions, Pulumi supports bulk imports using a JSON file.

### Scaffolding the import file

The easiest way to create a bulk import file is to let Pulumi do the hard work. If you write your desired resource definitions in your program first, you can run a preview to generate a template.

```bash
pulumi preview --import-file bulk-import.json
```

Pulumi will identify all resources in your program that don't yet exist in the state and create a JSON file with the correct types and names. You only need to fill in the `id` fields for each resource.

### Executing the bulk import

Once your `bulk-import.json` is ready, run the import command pointing to the file:

```bash
pulumi import --file bulk-import.json
```

This command will process all resources in the file in a single operation, significantly speeding up the adoption process.

## Custom and third-party providers

Not every resource belongs to the standard AWS, Azure, or Google Cloud providers. When importing resources from custom or third-party providers, you may need to specify the provider explicitly.

If you have multiple instances of a provider (e.g., different AWS regions), pass the provider name and URN to the import command in `name=urn` form:

```bash
pulumi import aws:ec2/vpc:Vpc my-vpc vpc-0123456789abcdef0 --provider "awsProvider=urn:pulumi:stack::project::pulumi:providers:aws::my-provider-name::12345678-1234-1234-1234-123456789abc"
```

In a bulk import file, define provider names in `nameTable`, then reference those names from each resource:

```json
{
    "nameTable": {
        "awsProvider": "urn:pulumi:stack::project::pulumi:providers:aws::my-provider-name::12345678-1234-1234-1234-123456789abc"
    },
    "resources": [
        {
            "type": "aws:ec2/vpc:Vpc",
            "name": "my-vpc",
            "id": "vpc-0123456789abcdef0",
            "provider": "awsProvider"
        }
    ]
}
```

## Strategies for large adoptions

When importing a large resource estate, a single massive import can be risky. Here are strategies to ensure a smooth transition.

### Chunking the work

Break your adoption into logical chunks. Start with foundational resources like VPCs and subnets, then move to security groups, and finally to application-level resources like databases and load balancers. This makes it easier to verify each step and recover if something goes wrong.

### Checkpoint recovery

Bulk import recovery is a checkpoint-management workflow, not an idempotent retry. If an import file fails partway through, inspect the stack state and the failed operation output, remove resources that were already imported from the import file, then rerun `pulumi import --file` with only the remaining resources. This keeps the next import focused on resources that are not already registered in the stack.

### Validating with a no-op preview

After any import, your goal is to reach a "no-op" state where `pulumi preview` shows zero changes.

1. Run `pulumi preview` after the import.
1. If Pulumi shows "updates" to your resources, it means your code doesn't perfectly match the cloud configuration.
1. Adjust your code properties until the preview shows no changes.
1. Only then should you consider the import complete.

## Conclusion

Production-grade imports require more than the basic CLI command. Start with one low-risk stack, run a no-op preview after every import batch, and only then expand the pattern to larger parts of your estate.
