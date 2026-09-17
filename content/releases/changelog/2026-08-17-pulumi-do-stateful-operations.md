---
title: "Stateful, zero-setup resource operations with pulumi do"
date: 2026-08-17
meta_desc: pulumi do now runs stateful create, upsert, delete, and patch operations from any directory, with no project or stack setup required. GA in v3.258.0.
authors:
    - christian-nunciato
---

You can now use [`pulumi do`](/docs/iac/cli/direct-resource-operations/) to create, read, update, and delete cloud resources directly from the command line — no program, project, or stack required — and pull them into new or existing Pulumi projects when you're ready. Resources created with `pulumi do` are tracked and managed transparently for you, so commands like these just work:

```bash
# Create a new resource
pulumi do aws:s3:Bucket create my-bucket

# Update the resource in place
pulumi do aws:s3:Bucket patch my-bucket

# Delete it
pulumi do aws:s3:Bucket delete my-bucket
```

When the time comes to pull these resources into a proper Pulumi project of your own, you can promote them using the new [`pulumi state promote`](/docs/iac/cli/commands/pulumi_state_promote/) command:

```bash
pulumi state promote my-bucket
```

All of this makes `pulumi do` a unified, consistent API across the whole cloud that agents can use to manage resources easily and directly, without you having to give up the benefits of a solid IaC foundation.

`pulumi do` is generally available as of [v3.258.0](https://github.com/pulumi/pulumi/releases/tag/v3.258.0). To learn more, read the [announcement post](/blog/pulumi-do-direct-resource-operations/) or the [`pulumi do` documentation](/docs/iac/cli/direct-resource-operations/).
