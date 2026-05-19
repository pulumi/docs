---
title_tag: "Stack management | Pulumi Operations"
meta_desc: Manage Pulumi stacks day-to-day with targeted updates, update plans, and safe state file editing techniques.
title: Stack management
h1: Stack management
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Stack Management
        parent: iac-operations
        weight: 10
        identifier: iac-operations-stack-management
---

These pages cover the day-to-day operations of running Pulumi stacks: scoping updates to specific resources, previewing changes before they apply, and safely editing state when recovery is needed.

## Pages

**[Targeted updates](/docs/iac/operations/stack-management/targeted-updates/)** - Limit which resources Pulumi operates on with `--target`, `--exclude`, and `--target-replace`. Learn the trade-offs of partial operations and when to use them.

**[Update plans](/docs/iac/operations/stack-management/update-plans/)** - Preview and review infrastructure changes before applying them. Update plans help you catch unintended modifications and coordinate changes across teams.

**[Editing state files](/docs/iac/operations/stack-management/editing-state-files/)** - Safe techniques for modifying Pulumi state when normal operations can't recover. Use sparingly and always back up state first.
