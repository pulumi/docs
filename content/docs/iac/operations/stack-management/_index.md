---
title_tag: "Stack management | Pulumi Operations"
meta_desc: Manage Pulumi stacks day-to-day with targeted updates, update plans, safe state file editing, and self-managed state backends.
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

These pages cover the day-to-day operations of running Pulumi stacks: scoping updates to specific resources, previewing changes before they apply, safely editing state when recovery is needed, and configuring a self-managed state backend.

## Pages

**[Targeted updates](/docs/iac/operations/stack-management/targeted-updates/)** - Limit which resources Pulumi operates on with `--target`, `--exclude`, and `--target-replace`. Learn the trade-offs of partial operations and when to use them.

**[Running your program on refresh and destroy](/docs/iac/operations/stack-management/run-program/)** - Use `--run-program` to execute your Pulumi program before `refresh` or `destroy`. Required for dynamic credentials and useful for diff-clean provider upgrades.

**[Update plans](/docs/iac/operations/stack-management/update-plans/)** - Preview and review infrastructure changes before applying them. Update plans help you catch unintended modifications and coordinate changes across teams.

**[Detecting and reconciling drift](/docs/iac/operations/stack-management/drift/)** - Detect when your cloud resources diverge from your Pulumi program, then choose to remediate (re-apply code) or adopt (accept reality into the program).

**[Editing state files](/docs/iac/operations/stack-management/editing-state-files/)** - Safe techniques for modifying Pulumi state when normal operations can't recover. Use sparingly and always back up state first.

**[Restoring deleted stacks](/docs/iac/operations/stack-management/restoring-deleted-stacks/)** - Recover a recently deleted stack from the Pulumi Cloud console, including after an accidental `pulumi stack rm --force`.

**[Using a DIY backend](/docs/iac/operations/stack-management/using-a-diy-backend/)** - Configure a self-managed state backend with AWS S3, Azure Blob Storage, Google Cloud Storage, PostgreSQL, or the local filesystem.

**[Refactoring with aliases](/docs/iac/operations/stack-management/refactoring-with-aliases/)** - Use the `aliases` resource option to rename, re-parent, change the type, or move resources across stacks without destroying and recreating them.
