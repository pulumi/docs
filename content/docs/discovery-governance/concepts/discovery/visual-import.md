---
title: Visual Import
title_tag: Visual Import | Discovery & governance
h1: Visual Import
meta_desc: Learn how Visual Import turns resources found by Discovery into Pulumi IaC code, and how the resources it imports become managed by Pulumi.
menu:
  discovery-governance:
    name: Visual Import
    parent: dg-concepts-discovery
    weight: 20
pulumi_cloud_feature: insights-discovery
---

Visual Import generates Pulumi IaC code for cloud resources that [Discovery](/docs/discovery-governance/concepts/discovery/) has found but Pulumi doesn't manage yet. You choose resources in the Pulumi Cloud console instead of looking up each resource's type and ID yourself, and Visual Import writes a Pulumi program that adopts them. Once you run that program, the resources are managed by Pulumi like any resource you created with Pulumi IaC.

## How Visual Import works

Visual Import builds on the inventory that Discovery keeps for your [cloud accounts](/docs/discovery-governance/concepts/discovery/cloud-accounts/):

1. **You select unmanaged resources.** Visual Import lists only resources that Discovery has found and that no Pulumi stack manages.
1. **Visual Import adds related resources.** Discovery records the relationships between resources, so Visual Import can suggest the resources your selection depends on and the resources that depend on it. Importing related resources together keeps a service's infrastructure in one program.
1. **Visual Import generates code.** It writes a program in the language you choose: TypeScript, Python, Go, C#, Java, or YAML. You can have [Pulumi Neo](/docs/ai/neo/) refine the generated code, for example to use more meaningful names or to reference related resources instead of hard-coding their IDs.
1. **You run the program.** You add the code to a new or existing stack and run `pulumi up`.

## How resources become managed

Each resource in the generated code sets the [`import` resource option](/docs/iac/concepts/resources/options/import/) to the ID of the existing cloud resource. When you run `pulumi up`, Pulumi adopts each resource into the stack's state instead of creating a new one, so nothing in your cloud account is replaced. After that, the resources are ordinary stack resources: a change to the program updates them, and Discovery shows them as managed by Pulumi.

Because Pulumi reads the existing resources during the import, the Pulumi CLI needs credentials for the cloud account that contains them.

## Visual Import and other ways to import

Visual Import is one of several ways to bring existing resources under Pulumi management:

- **Visual Import** suits resources that Discovery has already found, when you want to pick them from an inventory and see their relationships.
- **The [`pulumi import`](/docs/iac/guides/migration/import/) command** imports resources from the CLI when you already know their types and IDs, and can import many resources at once from a file.
- **[Discovered stacks](/docs/discovery-governance/concepts/discovery/discovered-stacks/)** model CloudFormation and ARM deployments as stacks, with a path to [migrate them](/docs/discovery-governance/guides/migrate-discovered-stack/) to Pulumi IaC as a unit.

## Next steps

- [Import resources with Visual Import](/docs/discovery-governance/guides/visual-import/): a walkthrough of the workflow in the Pulumi Cloud console.
