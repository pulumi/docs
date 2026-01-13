---
title: "Zero-downtime migration with Neo"

date: 2026-01-21

draft: false

meta_desc: Neo automates migrations from CDK, Terraform, and ARM to Pulumi with zero downtime and verified safety.

meta_image: meta.png

authors:
    - neo-team

tags:
    - neo
    - aws
    - cdk
    - terraform
    - azure
    - arm
    - migration
    - ai

schema_type: auto

---

The barrier to migrating to Pulumi has always been the infrastructure you already have. Your existing resources can't be disrupted, and manually importing them into a new tool is risky and time-consuming. Today, we're excited to share how Neo removes this barrier entirely with automated, zero-downtime migration to Pulumi from AWS CDK, Terraform, and Azure ARM templates.

<!--more-->

## Why IaC migrations are hard

The promise of Infrastructure as Code is that your code perfectly describes your running infrastructure. But switching IaC tools breaks this promise in dangerous ways.

When you rewrite your infrastructure code in a new tool, you have two choices, both problematic. You can destroy and recreate all your resources to match the new code, accepting downtime and risk. Or you can try to import existing resources, which requires perfect knowledge of how every resource maps between the old and new systems. Many teams get stuck here, wanting Pulumi's modern platform but unable to safely make the switch.

## Neo's insight: State knowledge enables perfect imports

The key to safe migration isn't just converting code - it's understanding the complete relationship between your existing IaC tool's state and your actual cloud resources. Each IaC tool maintains this relationship differently: CDK through CloudFormation stacks, Terraform through state files, and ARM through Azure deployments. But they all have complete knowledge of what they manage.

Neo leverages this existing state knowledge to orchestrate perfect imports. Instead of asking you to manually find resource IDs and construct import commands, Neo reads your current tool's state, discovers every resource's physical identity, and maps them to Pulumi's import system. This isn't just automation - it's using the source tool's own knowledge against the migration problem.

In practice, this means Neo can bridge the gap between how tools name resources and where they actually live. A Lambda function that CDK knows as `OrderHandler9I0J1K2L` actually exists in AWS as `my-app-OrderHandler-9I0J1K2L`, while a Terraform resource at address `aws_instance.web[2]` maps to EC2 instance `i-0abc123def456`. Neo understands these mappings and handles the complex cases like composite IDs (`FunctionName|StatementId`), resource references, and dependency chains that must be imported in order.

Because Neo uses the source tool's own state knowledge, your infrastructure doesn't change at all during migration. Not a single resource is modified, recreated, or even touched. We're simply transferring ownership from one IaC tool to another.

This approach delivers three critical guarantees:

1. **Zero downtime**: Resources are never deleted or recreated
2. **Zero risk**: Since nothing changes, you can abandon the migration at any point without consequence
3. **Zero surprises**: Preview confirms no infrastructure changes before you commit

## Migration in action: Three tools, one approach

Neo adapts its migration strategy to each tool's unique characteristics while maintaining the same zero-downtime guarantee. Let's explore how Neo handles migrations from each major IaC tool.

## AWS CDK to Pulumi

For teams using AWS CDK, Neo leverages the CloudFormation layer that underpins CDK deployments. CDK's architecture actually makes migration straightforward: since CDK synthesizes to CloudFormation templates, Neo can read the deployed stacks directly to understand every resource and its configuration.

The challenge with CDK migrations isn't the CloudFormation layer - it's the cryptic resource naming. CDK generates logical IDs like `OrdersTableA7B2C3D4` that map to physical resources with completely different names. These mappings are buried in CloudFormation metadata, and getting them wrong means either orphaning resources or accidentally creating duplicates. Neo navigates this complexity by reading CloudFormation's own stack outputs and resource metadata, discovering the exact physical ID for every logical resource.

CDK also introduces complexity through its construct hierarchy. A single high-level construct might expand into dozens of CloudFormation resources, each with dependencies and references to others. Neo preserves these relationships during migration, ensuring that IAM roles still reference the right Lambda functions, API Gateway deployments still point to the correct stages, and security groups maintain their exact rules. The migration completes with your infrastructure unchanged and Pulumi's preview confirming zero modifications.

## Terraform to Pulumi

Terraform's state file architecture makes it both easier and harder to migrate than other tools. The good news is that Terraform's state file contains complete information about every resource, including its provider, type, and physical ID. The challenge is that Terraform's state format has evolved over years, with different versions storing information differently, and the mapping between Terraform resource addresses and their actual cloud identities can be complex.

Neo handles this complexity by first converting Terraform's state into Pulumi state, establishing the connection to your real cloud resources. Then, using both the Terraform configuration files and this converted state, Neo generates a Pulumi program that matches your existing infrastructure. When Terraform manages resources with `count` or `for_each`, creating indexed instances like `aws_instance.web[2]`, Neo ensures these map correctly to both the cloud resources and the generated Pulumi code. Your third web server remains exactly that after migration, properly indexed and connected.

## Azure ARM to Pulumi

ARM templates present unique migration challenges. Unlike CDK and Terraform, which maintain clear separation between code and state, ARM templates blur this line. The template is both the definition and, through deployment history, part of the state tracking. ARM's template expression language, with its concat functions and resource ID constructors, makes it difficult to determine what resources actually exist until deployment time.

Neo orchestrates ARM migrations through intelligent AI-driven conversion. When an ARM template uses functions like `concat(parameters('appName'), '-plan')`, the conversion process evaluates these expressions using the actual parameter values to generate the correct resource names. Azure resource IDs follow predictable patterns - subscription IDs, resource groups, providers, and resource names - and Neo ensures these are correctly mapped to Pulumi's import system using inline import IDs directly in the generated code.

The biggest challenge with ARM migrations is handling the implicit dependencies and resource provider quirks. An App Service might implicitly create a service plan, a SQL database requires a server that might be defined in a linked template, and child resources like application settings need separate imports. Neo understands these Azure-specific patterns and generates the appropriate Pulumi code with imports for every resource. The migration completes with a zero-diff preview, confirming your exact Azure configuration is preserved while giving you a more maintainable, type-safe way to manage it going forward.

## The architecture powering it all

While each tool requires specific handling, Neo's core architecture remains consistent:

### Universal orchestration layer

Neo acts as the intelligent migration coordinator, regardless of source tool:

- **Credential verification**: Ensures proper cloud credentials are configured in Pulumi ESC
- **Resource inventory**: Builds a complete catalog of existing resources
- **Conversion orchestration**: Manages the code transformation
- **Import coordination**: Executes resource imports in the correct order
- **Audit trail generation**: Creates comprehensive migration reports

### Unified import engine

The import engine works consistently across all tools:

- Maps source resource IDs to Pulumi import formats
- Handles complex and composite resource identifiers
- Provides fallback strategies for edge cases
- Ensures idempotent operations

### Human oversight

While Neo automates the heavy lifting, we maintain human checkpoints:

- Review generated code before import
- Verify preview shows zero changes
- Approve the resulting pull request

## Start your migration today

Ready to migrate to Pulumi? Here's how to get started with Neo, regardless of your current tool:

### From AWS CDK

```text
Ask Neo: "Help me migrate my CDK application to Pulumi"
```

Prerequisites:

- CDK application that synthesizes cleanly
- AWS credentials configured in Pulumi ESC

### From Terraform

```text
Ask Neo: "Migrate my Terraform configuration to Pulumi"
```

Prerequisites:

- Access to Terraform configuration files
- Current Terraform state file
- Cloud credentials in Pulumi ESC

### From Azure ARM

```text
Ask Neo: "Convert my ARM templates to Pulumi"
```

Prerequisites:

- ARM template files (JSON)
- Azure subscription access
- Azure credentials in Pulumi ESC

## What this means for your team

Migration friction no longer locks you into your current IaC tool. If you want Pulumi's programming model, policy engine, and multi-cloud support, Neo gets you there without disrupting your infrastructure.

Ready to migrate? Join us in the [Pulumi Community Slack](https://slack.pulumi.com/) or reach out to your account team for a guided migration session.
