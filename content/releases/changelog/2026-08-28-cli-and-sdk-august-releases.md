---
title: "CLI and SDK rollup: pulumi new, pulumi do, and more"
date: 2026-08-28
meta_desc: Our August CLI and SDK releases add a redesigned interactive pulumi new, encrypted credential storage, full-stack Go policies, and more.
authors:
    - christian-nunciato
---

We shipped a bunch of new features and improvements in the Pulumi CLI and SDK this month. A few highlights:

* A redesigned interactive [`pulumi new`](/docs/iac/cli/commands/pulumi_new/) that asks for a cloud provider and language instead of listing every template, then confirms your project, stack, and config defaults in a single step ([v3.258](https://github.com/pulumi/pulumi/releases/tag/v3.258.0), [v3.259](https://github.com/pulumi/pulumi/releases/tag/v3.259.0))
* Opt-in encryption of stored credentials with a key protected by your operating system, selected with `PULUMI_CREDENTIAL_STORE` ([v3.258](https://github.com/pulumi/pulumi/releases/tag/v3.258.0))
* A new [`pulumi state get`](/docs/iac/cli/commands/pulumi_state_get/) command to inspect an individual resource in your state ([v3.257](https://github.com/pulumi/pulumi/releases/tag/v3.257.0))
* A new [`pulumi state promote`](/docs/iac/cli/commands/pulumi_state_promote/) command that turns the stateful snippets created by [`pulumi do`](/releases/changelog/pulumi-do-stateful-operations/) into Pulumi program code ([v3.260](https://github.com/pulumi/pulumi/releases/tag/v3.260.0))
* An `--ignore-protect` flag for `pulumi up`, `pulumi preview`, and `pulumi destroy` that deletes protected resources without unprotecting them in state first ([v3.256](https://github.com/pulumi/pulumi/releases/tag/v3.256.0))
* Full-stack validation for Go policy packs via `policyx.NewStackValidationPolicy` ([v3.258](https://github.com/pulumi/pulumi/releases/tag/v3.258.0))
* A `PULUMI_DEFAULT_ORGANIZATION` environment variable to set your default organization ([v3.259](https://github.com/pulumi/pulumi/releases/tag/v3.259.0))
* Support for Go 1.27 ([v3.260](https://github.com/pulumi/pulumi/releases/tag/v3.260.0))

We also retired the AI mode of `pulumi new` in favor of [`pulumi neo`](/docs/ai/) ([v3.256](https://github.com/pulumi/pulumi/releases/tag/v3.256.0)), and made a whole slew of improvements to [`pulumi do`](/releases/changelog/pulumi-do-stateful-operations/) itself.

See the [Releases page on GitHub](https://github.com/pulumi/pulumi/releases) and the [`pulumi do` docs](/docs/iac/cli/direct-resource-operations/) for details.
