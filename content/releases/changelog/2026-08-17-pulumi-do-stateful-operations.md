---
title: "Stateful, zero-setup resource operations with pulumi do"
date: 2026-08-17
meta_desc: pulumi do now runs stateful create, upsert, delete, and patch operations from any directory, with no project or stack setup required. GA in v3.258.0.
authors:
    - christian-nunciato
---

You can now use [`pulumi do`](/docs/iac/cli/direct-resource-operations/) to create, update, and delete real cloud resources directly from the command line — no program, project, or stack setup required. What started as a way to invoke a single function or resource operation is now **stateful**, supporting `create`, `upsert`, `delete`, and `patch`, and it works from **any directory**.

If you run it outside of a Pulumi project, `pulumi do` transparently falls back to a global project and `default` stack under `$PULUMI_HOME` and manages the stack for you, so a one-off just works:

```bash
# Create (or update) a resource — no pulumi new or pulumi stack init needed
pulumi do aws:s3/bucket:Bucket upsert my-bucket

# See what's in state so you can reference it
pulumi do show-resources

# Tear it down
pulumi do aws:s3/bucket:Bucket delete my-bucket
```

Everything still runs through the Pulumi engine, so state, providers, and secrets behave exactly as they do in a full program. That also makes `pulumi do` a natural, verb-oriented surface for agents driving Pulumi from a shell, where auto-naming keeps snippets stable across runs. And when a one-off grows into something worth keeping, `pulumi state promote` (new in [v3.260.0](https://github.com/pulumi/pulumi/releases/tag/v3.260.0)) turns those stateful snippets into Pulumi program code.

`pulumi do` is generally available as of [v3.258.0](https://github.com/pulumi/pulumi/releases/tag/v3.258.0). To learn more, read the [announcement post](/blog/pulumi-do-direct-resource-operations/) or the [Direct Resource Operations documentation](/docs/iac/cli/direct-resource-operations/).
