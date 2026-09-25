---
title: "Change your components, keep your infrastructure"
date: 2026-09-24
draft: true
meta_desc: "Use Pulumi component state migrations to move a VPC from classic AWSX to modern AWSX and plain AWS resources while keeping the same infrastructure."
feature_image:
authors:
    - julien-poissonnier
tags:
    - aws
    - typescript
    - infrastructure-as-code
category: product
resource_links:
    - type: documentation
      url: /docs/iac/guides/building-extending/components/state-migrations/
      text: Component state migrations
    - type: github
      url: https://github.com/pulumi/examples/tree/master/aws-ts-awsx-vpc-state-migration
      text: AWSX VPC migration example
---

[Components](/docs/iac/concepts/components/) let you turn a group of resources into a reusable building block. You can define a network, a database, or an application service once and share it across projects and teams. People using the component work with its inputs and outputs without needing to understand every resource inside it.

Suppose you built your network with the legacy AWSX VPC component. It manages the VPC, subnets, route tables, and gateways behind a few lines of code. Now you want to upgrade to the modern AWSX component. Later, your needs change again: you want more control over the resources than the component gives you. At each step, the network is already running. You want to change the code that manages it without rebuilding the network itself.

Pulumi's new component state migrations let you ship the upgrade path with the component itself. A migration translates the saved state of a component and its children before Pulumi works out which resources need to change. Component authors can change the internal design and include the migration in the same release.

<!--more-->

{{% notes type="info" %}}
The state migrations API is experimental and may change.

Share feedback in the [component state migrations discussion](https://github.com/pulumi/pulumi/discussions/24799).
{{% /notes %}}

## Start with legacy AWSX (v1)

The [AWSX VPC example](https://github.com/pulumi/examples/tree/master/aws-ts-awsx-vpc-state-migration) follows a network as your needs change over time. You start with v1, upgrade to v2, and later move to v3. Each version builds on the infrastructure already running.

You start with the legacy `awsx.classic.ec2.Vpc` component. This first version creates a VPC with one isolated subnet, a route table and its association, and an internet gateway. A security group sits outside the component and refers to the VPC.

Without a migration that connects the old state to the new code, an upgrade could replace the VPC instead of keeping it. That change would reach beyond the component: the security group refers to the VPC's ID, so a new VPC would mean [replacing the security group too](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroup.html#cfn-ec2-securitygroup-vpcid).

Now imagine a production database using that network and security group. The example does not create a database, but in a real application, changes to its network can cause downtime or require more resource replacements. If the database itself has to be recreated, its replacement does not automatically contain the old data. Without a backup or a data migration, deleting the old database could mean losing that data. You do not want a component upgrade to turn into a database recovery job.

After running this network for a while, you decide to upgrade to the modern `awsx.ec2.Vpc` component. The second version makes that change while keeping your existing network.

Further down the road, suppose the modern component no longer fits your needs. You want to define and configure each resource yourself. The third version removes AWSX and declares the resources directly with `@pulumi/aws`. Pulumi still manages them, but your code now controls each resource instead of relying on the component to create it.

Across all three versions, the AWS resource IDs stay the same. The security group continues to use the same VPC. What changes is how Pulumi records those resources and their relationships.

These trees show the resources Pulumi tracks in each version. The security group is outside the VPC tree and is omitted here. The `awsx:` entries are component records; the `aws:` entries represent the AWS resources that stay in place.

```text
v1: awsx:x:ec2:Vpc "vpc"
    ├── aws:ec2/vpc:Vpc "vpc"
    ├── awsx:x:ec2:Subnet "vpc-isolated-0"
    │   ├── aws:ec2/subnet:Subnet "vpc-isolated-0"
    │   ├── aws:ec2/routeTable:RouteTable "vpc-isolated-0"
    │   └── aws:ec2/routeTableAssociation:RouteTableAssociation "vpc-isolated-0"
    └── awsx:x:ec2:InternetGateway "vpc"
        └── aws:ec2/internetGateway:InternetGateway "vpc"

v2: awsx:ec2:Vpc "vpc"
    └── aws:ec2/vpc:Vpc "vpc"
        ├── aws:ec2/subnet:Subnet "vpc-isolated-1"
        │   └── aws:ec2/routeTable:RouteTable "vpc-isolated-1"
        │       └── aws:ec2/routeTableAssociation:RouteTableAssociation "vpc-isolated-1"
        └── aws:ec2/internetGateway:InternetGateway "vpc"

v3: aws:ec2/vpc:Vpc "vpc"
    ├── aws:ec2/subnet:Subnet "vpc-isolated-1"
    │   └── aws:ec2/routeTable:RouteTable "vpc-isolated-1"
    │       └── aws:ec2/routeTableAssociation:RouteTableAssociation "vpc-isolated-1"
    └── aws:ec2/internetGateway:InternetGateway "vpc"
```

## Why a change in code needs a change in state

Pulumi's state records both the physical resources and the components that group them. Each record has a Pulumi name, called a URN. Managed resources also have an ID from the cloud provider, such as an AWS VPC ID.

Legacy and modern AWSX organize their resources differently. The legacy component wraps the subnet and internet gateway in separate components. Modern AWSX removes those wrappers and puts the managed resources under different parents. In this example, the Pulumi name of the subnet also changes from `vpc-isolated-0` to `vpc-isolated-1`.

[Aliases](/docs/iac/concepts/resources/options/aliases/) handle changes to a resource's name, type, or parent when its saved state remains compatible. This upgrade also needs to remove component wrappers and transfer references to the resources that take their place. A state migration describes that whole change together.

## Later, upgrade to modern AWSX (v1 to v2)

To move your existing network to modern AWSX, you register the new VPC component with an alias for the legacy component type and a migration callback through the `stateMigrations` option. This excerpt from the example shows the registration; `availabilityZone` and `vpcTags` hold the same settings used in the first version, and `migrateClassicVpc` comes from the example's [migration file](https://github.com/pulumi/examples/blob/master/aws-ts-awsx-vpc-state-migration/v2/migration.ts).

```typescript
{{% example-program-snippet path="awsx-vpc-state-migration-blog" language="typescript" file="modern-vpc.ts.txt" %}}
```

The alias lets Pulumi find the old component. The callback then receives its saved state, followed by the state of its children. It copies those records, changes their names and parents to match modern AWSX, and returns two things:

- `newState`: the complete set of records that should replace the old component and its children.
- `successors`: a map from each old URN that disappears to the URN that takes its place.

```typescript
{{% example-program-snippet path="awsx-vpc-state-migration-blog" language="typescript" file="migration-sketch.ts.txt" %}}
```

[Full migration code](https://github.com/pulumi/examples/blob/master/aws-ts-awsx-vpc-state-migration/v2/migration.ts)

The first checks make the callback safe to run again: if the state already uses modern AWSX or plain AWS resources, there is nothing to do. An unexpected component type raises an error instead of guessing how to migrate it.

The `rename` helper copies the saved record and changes its URN, type, and parent. It preserves the AWS resource ID and the other saved fields. Here, it moves the subnet under the managed VPC.

The two subnet entries in `successors` let the Pulumi engine know that the old component wrapper and the managed subnet point to the same new subnet record. Pulumi uses these mappings to update dependencies and resource references elsewhere in the stack. For example, the security group lives outside the VPC component, but its reference to the VPC still needs to be valid after the migration. The VPC successor mapping keeps that reference connected to the migrated VPC record, which retains the same AWS VPC ID.

## Later still, manage each resource directly (v2 to v3)

You have been running v2 for a while when a new requirement calls for a subnet or routing layout that the modern component does not support. You decide to manage those choices in your own code. The third version declares the VPC, subnet, route table, association, and internet gateway directly with `@pulumi/aws`. This migration changes who defines those resources in your program; you can then adjust their configuration in a separate update.

The [second migration](https://github.com/pulumi/examples/blob/master/aws-ts-awsx-vpc-state-migration/v3/migration.ts) removes the AWSX VPC component record and moves the managed VPC into its place. Both the old component and its VPC child map to the new VPC record. The VPC keeps its AWS ID, and the other resources remain beneath it.

The VPC registration keeps aliases for both previous component types and both migration callbacks:

```typescript
{{% example-program-snippet path="awsx-vpc-state-migration-blog" language="typescript" file="plain-vpc.ts.txt" %}}
```

Pulumi runs the callbacks in order, passing each result to the next callback. A stack still using legacy AWSX can upgrade directly to the plain AWS version. A stack already using modern AWSX skips the first migration. Once both migrations have run, both callbacks return no result on later updates.

Keeping earlier migrations with the component means its users can skip versions without having to edit stack state by hand.

## Check the upgrade before applying it

A migration changes saved state. Afterward, Pulumi compares the new program with that state and calls the provider for any remaining changes. Keeping resource IDs does not mean every upgrade has an empty preview: this example can still show in-place updates for provider defaults and tags.

To try the example, start with `v1` and follow its README. Use the same stack, backend, project name, AWS region, and availability zone for each version.

Before each upgrade, run `pulumi preview`. The existing VPC, subnet, route table, association, internet gateway, and security group should have no creates, deletes, or replacements. Review any in-place changes before running `pulumi up`. Preview evaluates the migration without saving it, and the update saves the migrated state.

## Ship the migration with your component

If you maintain a component, register the migration inside its implementation and ship both together. Users do not need to write the migration, attach the callback, or edit their stack state. When they upgrade the component and run Pulumi, it runs the migration as part of the normal preview and update.

For an internal change that keeps the same component inputs and outputs, users can keep their existing component calls. They do not need to know which resources moved or how the saved state changed. They still review the preview, as with any upgrade, but the component handles the migration details.

That makes the upgrade path part of the reusable building block. You write and test it once, and each team using the component gets it with the new version.

The [component state migrations guide](/docs/iac/guides/building-extending/components/state-migrations/) covers the callback contract. The [VPC example](https://github.com/pulumi/examples/tree/master/aws-ts-awsx-vpc-state-migration) contains all three programs and the migration code shown here.
