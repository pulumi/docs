---
title: "From CloudFormation to Pulumi Without a Rewrite"
date: 2026-05-21
meta_desc: "Migrate CloudFormation stacks to Pulumi with a retain-and-adopt strategy, import planning, generated code, and practical gotchas for production estates."
meta_image: meta.png
feature_image: feature.png
authors:
    - pablo-seibelt
tags:
    - migration
    - aws
    - pulumi-import
social:
    twitter: |
        Moving from CloudFormation to Pulumi does not have to mean rewriting everything.

        Use retain-and-adopt, import planning, and generated code to migrate safely.
    linkedin: |
        CloudFormation migrations work best when they are treated as adoption projects, not rewrites.

        This guide walks through discovery, retain-and-adopt, Pulumi import, generated code, and the gotchas that matter in production.
    bluesky: |
        CloudFormation to Pulumi works best as adoption, not rewrite.

        Plan imports, retain resources, generate code, then modernize safely.
---

Many teams start their infrastructure journey with AWS CloudFormation. It's a reliable service, but as infrastructure grows, the limitations of YAML and JSON templates become apparent. A common migration challenge is finding a clear path to move existing CloudFormation stacks into Pulumi without tearing everything down and starting over.

The good news is that you don't have to choose between a "big bang" migration and staying stuck in template hell. By using Pulumi's import capabilities and CloudFormation's retention policies, you can adopt existing resources into a modern programming environment while reducing downtime risk.

By the end, you will have a step-by-step strategy for migrating CloudFormation stacks to Pulumi while reducing downtime risk.

<!--more-->

## Why migrate from CloudFormation

CloudFormation is a powerful tool, but it often leads to "template sprawl" where large YAML files become difficult to test, refactor, or share across teams. Moving to Pulumi allows you to use familiar languages like TypeScript, Python, or Go. This shift enables:

1. **Real programming constructs**: Use loops, functions, and classes to reduce duplication.
1. **Strong typing**: Catch errors at development time rather than during a deployment.
1. **Better testing**: Use standard unit and integration testing frameworks.
1. **Faster iterations**: Pulumi's engine often provides faster feedback loops than waiting for CloudFormation stack updates.

## Step 1: Discovery and planning

Before you touch any code, you need to understand what you're migrating. You can use the AWS CLI to list your existing stacks and their resources.

```bash
# List all stacks in your account
aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE

# List resources for a specific stack
aws cloudformation list-stack-resources --stack-name my-production-vpc
```

Identify the core resources that form the foundation of your stack, such as VPCs, subnets, and security groups. These are usually the best candidates for the first phase of migration.

## Step 2: Generate Pulumi code with import

Pulumi's `import` command can do more than just bring a resource into state; it can also generate the corresponding code for you. This is a massive time-saver when migrating complex resources with many properties.

First, create a new Pulumi project:

```bash
mkdir migration-project && cd migration-project
pulumi new aws-typescript
```

Then, use the `--generate-code` flag to import a resource and create the TypeScript code automatically. For example, to import a VPC:

```bash
pulumi import aws:ec2/vpc:Vpc my-vpc vpc-0123456789abcdef0 --generate-code --out index.ts
```

Pulumi will query the AWS API, determine the current configuration of the VPC, and write the resource definition to your `index.ts` file.

## Step 3: The "retain and adopt" strategy

The most critical part of a CloudFormation migration is ensuring that deleting the old stack doesn't delete your actual infrastructure. Use a "Retain and Adopt" strategy to handle this safely.

### 1. Update the CloudFormation DeletionPolicy

In your CloudFormation template, set the `DeletionPolicy` to `Retain` for every resource you plan to migrate.

```yaml
Resources:
  MyVPC:
    Type: AWS::EC2::VPC
    DeletionPolicy: Retain
    Properties:
      CidrBlock: 10.0.0.0/16
```

Update the CloudFormation stack with this change. Now, if the stack is deleted, the VPC will remain active in your AWS account.

### 2. Import into Pulumi

Run the `pulumi import` commands for all resources in the stack. Ensure your Pulumi code matches the existing configuration exactly. You can run `pulumi preview` to verify that Pulumi sees no pending changes.

### 3. Validate CloudFormation detach safety

Before deleting the CloudFormation stack, review the stack template and resource list, verify that every logical resource that must survive has `DeletionPolicy: Retain`, and use a change set only for the preceding stack update that adds retention policies. Confirm no dependent stacks still consume this stack's exports through `Fn::ImportValue`. Migrate or replace those cross-stack references before the cutover.

### 4. Delete the CloudFormation stack

Once the resources are safely managed by Pulumi and detach safety checks pass, you can delete the CloudFormation stack. Because of the `Retain` policy, retained resources stay alive, while non-retained resources are still subject to normal CloudFormation deletion behavior.

### 5. Verify the imported code

After the import is complete, review the generated resource definition and keep protective options such as `protect: true` in place until you have a safe deletion plan.

```typescript
const vpc = new aws.ec2.Vpc("my-vpc", {
    cidrBlock: "10.0.0.0/16",
}, {
    protect: true,
});
```

## Side-by-side example: VPC and Subnet

Here is how a typical migration looks for a network stack. The Pulumi example shows the steady-state code after importing the existing VPC and subnet, not code to run before import.

**CloudFormation (Before):**

```yaml
Resources:
  PublicSubnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref MyVPC
      CidrBlock: 10.0.1.0/24
```

**Pulumi (After Import):**

```typescript
const vpc = new aws.ec2.Vpc("migrated-vpc", {
    cidrBlock: "10.0.0.0/16",
    enableDnsHostnames: true,
    enableDnsSupport: true,
}, { protect: true });

const subnet = new aws.ec2.Subnet("migrated-subnet", {
    vpcId: vpc.id,
    cidrBlock: "10.0.1.0/24",
}, { protect: true });
```

## Common gotchas

Watch for these migration details before you delete the CloudFormation stack:

1. **Drift**: If your CloudFormation stack has drifted from its template, `pulumi import` will capture the *actual* state of the resource, which might differ from what you expect.
1. **IAM Roles**: Circular dependencies between IAM roles and policies can be tricky. Sometimes it's easier to recreate IAM resources in Pulumi rather than importing them.
1. **Custom Resources**: CloudFormation Custom Resources don't have a direct 1:1 mapping in Pulumi. You'll likely need to replace these with Pulumi [Dynamic Resources](/docs/iac/concepts/providers/dynamic-providers/) or specific provider resources.

## Conclusion

Migrating from CloudFormation to Pulumi doesn't have to be a high-risk operation. By using the `pulumi import --generate-code` feature and CloudFormation's retention policies, you can move your infrastructure into a more flexible and powerful environment one stack at a time.

If you're ready to start your migration, check out our [CloudFormation migration guide](/docs/iac/guides/migration/migrating-to-pulumi/from-cloudformation/) and [`pulumi import`](/docs/iac/guides/migration/import/) guide for more examples and advanced configuration options.
