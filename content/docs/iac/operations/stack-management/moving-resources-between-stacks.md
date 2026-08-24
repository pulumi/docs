---
title_tag: "Moving resources between stacks | Pulumi Operations"
meta_desc: "Use the pulumi state move command to transfer resources from one stack to another without destroying and recreating the underlying cloud infrastructure."
title: Moving resources between stacks
h1: Moving resources between stacks
menu:
    iac:
        name: Moving resources between stacks
        parent: iac-operations-stack-management
        weight: 45
---

As a project grows, you may decide to split a monolithic stack into smaller ones, merge stacks together, or otherwise reorganize which stack owns which resources. The [`pulumi state move`](/docs/iac/cli/commands/pulumi_state_move/) command lets you transfer resources from a source stack to a destination stack by rewriting state directly, so Pulumi treats the resources as unchanged rather than deleting them from one stack and recreating them in another.

{{% notes type="info" %}}
`pulumi state move` only modifies the state files of the source and destination stacks. It does not change your program code. After moving resources you still need to add the corresponding resource declarations to the destination stack's program, as described in [Update the destination program](#update-the-destination-program) below.
{{% /notes %}}

For a complete worked example that provisions resources, moves them between two stacks in different projects, and updates the program code on both sides, see the [Move Resources Between Stacks](/learn/tutorials/move-resources-between-stacks/) tutorial. For the motivation behind splitting a monolithic stack in the first place, see [Organizing projects & stacks](/docs/iac/guides/basics/organizing-projects-stacks/).

## Identify the resources to move

Every resource has a unique [URN](/docs/iac/concepts/resources/names/#urns) that encodes its stack, project, type, and name. To list the URNs in a stack, select it and run:

```bash
$ pulumi stack select <STACK>
$ pulumi stack --show-urns
```

Copy the URN of each resource you want to move. You only need to specify the URNs of top-level resources — `pulumi state move` automatically includes their children.

## Move the resources

Run `pulumi state move` with the source stack, the destination stack, and one or more URNs:

```bash
$ pulumi state move \
    --source <SOURCE_STACK> \
    --dest <DEST_STACK> \
    <URN>...
```

A few notes on the arguments:

* If the resources are in the currently selected stack, you can omit `--source`.
* When the source and destination stacks belong to different projects, use the fully qualified stack name (`<org>/<project>/<stack>`) for both. Within the same project, the stack name alone is enough.
* URNs can contain characters your shell will otherwise interpret, so wrap each one in single quotes.

Before making any changes, the command lists every resource it plans to move — including child resources of anything you named directly — and flags any dependencies on resources that are staying behind:

```bash
$ pulumi state move \
    --source myorg/my-project/source \
    --dest myorg/my-project/dest \
    'urn:pulumi:source::my-project::aws:s3/bucket:Bucket::b'

Planning to move the following resources from myorg/my-project/source to myorg/my-project/dest:

  - urn:pulumi:source::my-project::aws:s3/bucket:Bucket::b
  - urn:pulumi:source::my-project::aws:s3/bucket:Bucket$aws:s3/bucketObject:BucketObject::index.html

Do you want to perform this move? yes
Successfully moved resources from myorg/my-project/source to myorg/my-project/dest
```

Review any dependency warnings carefully. If a moved resource depends on one that is staying in the source stack, that dependency won't be reflected on the destination side, and you'll need to wire it up again — typically with a [stack reference](/docs/iac/concepts/stacks/#stackreferences) — once the program code is updated.

## Update the destination program

`pulumi state move` changes state, not code. After the move, the destination stack's state describes resources that its program doesn't declare yet, and the source stack's program still declares resources that are no longer in its state. Update both:

* Add a matching resource declaration to the destination stack's program for each moved resource. Give the resource the same logical name it had in the source stack unless you also intend to rename it. Consult the CLI output or `pulumi stack --show-urns` on the destination stack to see the name each moved resource now has.
* Remove the corresponding resource declarations from the source stack's program, since the resources it described are no longer part of its state.
* If the destination program declares a moved resource under a different logical name, parent, or project than it had in the source, add an [alias](/docs/iac/operations/stack-management/refactoring-with-aliases/) so Pulumi recognizes the existing cloud resource instead of trying to replace it.

Once the program changes are in place, run `pulumi preview` on both stacks. A clean preview with no unexpected changes confirms the move succeeded and the program matches the new state.

## Learn more

* [Move Resources Between Stacks](/learn/tutorials/move-resources-between-stacks/) — a full tutorial covering this workflow end to end, including cross-project moves and resolving dependencies with stack references.
* [Refactoring with aliases](/docs/iac/operations/stack-management/refactoring-with-aliases/) — use the `aliases` resource option when a moved resource's identity changes in the destination program.
* [Organizing projects & stacks](/docs/iac/guides/basics/organizing-projects-stacks/) — the tradeoffs behind splitting a monolithic stack into layered or micro-stacks in the first place.
* [`pulumi state move` CLI reference](/docs/iac/cli/commands/pulumi_state_move/) — the full command reference, including flags.
