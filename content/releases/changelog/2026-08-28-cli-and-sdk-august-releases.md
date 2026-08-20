---
title: "CLI and SDK rollup: interactive pulumi new and more"
date: 2026-08-28
meta_desc: Our August CLI and SDK releases add a redesigned interactive pulumi new, encrypted credential storage, full-stack Go policies, and more.
authors:
    - christian-nunciato
---

We shipped a batch of new features and improvements in the Pulumi CLI and SDK this month. A few highlights:

* A redesigned interactive [`pulumi new`](/docs/iac/cli/commands/pulumi_new/) that asks for a cloud provider and language instead of listing every template, then confirms your project, stack, and config defaults in a single step ([v3.258](https://github.com/pulumi/pulumi/releases/tag/v3.258.0), [v3.259](https://github.com/pulumi/pulumi/releases/tag/v3.259.0))
* Opt-in encryption of stored credentials with a key protected by your operating system, selected with `PULUMI_CREDENTIAL_STORE` ([v3.258](https://github.com/pulumi/pulumi/releases/tag/v3.258.0))
* A new [`pulumi state get`](/docs/iac/cli/commands/pulumi_state_get/) command to inspect an individual resource in your state ([v3.257](https://github.com/pulumi/pulumi/releases/tag/v3.257.0))
* A new `pulumi state promote` command that turns the stateful snippets created by [`pulumi do`](/releases/changelog/pulumi-do-stateful-operations/) into Pulumi program code ([v3.260](https://github.com/pulumi/pulumi/releases/tag/v3.260.0))
* An `--ignore-protect` flag for [`pulumi up`](/docs/iac/cli/commands/pulumi_up/), `pulumi preview`, and `pulumi destroy` that deletes protected resources without unprotecting them in state first ([v3.256](https://github.com/pulumi/pulumi/releases/tag/v3.256.0))
* Full-stack policy validation for Go policy packs via `policyx.NewStackValidationPolicy` ([v3.258](https://github.com/pulumi/pulumi/releases/tag/v3.258.0))
* A `PULUMI_DEFAULT_ORGANIZATION` environment variable to set your default organization ([v3.259](https://github.com/pulumi/pulumi/releases/tag/v3.259.0))
* Support for Go 1.27 ([v3.260](https://github.com/pulumi/pulumi/releases/tag/v3.260.0))

We also retired the AI mode of `pulumi new` in favor of [`pulumi neo`](/docs/ai/) ([v3.256](https://github.com/pulumi/pulumi/releases/tag/v3.256.0)), and made a raft of improvements to [`pulumi do`](/releases/changelog/pulumi-do-stateful-operations/).

... and lots more. See the [Releases page on GitHub](https://github.com/pulumi/pulumi/releases) for details.
