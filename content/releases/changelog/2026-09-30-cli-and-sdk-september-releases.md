---
title: "CLI and SDK rollup: Richer deployment settings and more"
date: 2026-09-30
meta_desc: Our September CLI and SDK releases expand pulumi deployment settings edit, protect promoted state, sign the Windows binaries, and more.
authors:
    - christian-nunciato
---

We shipped a bunch of new features and improvements in the Pulumi CLI and SDK this month. A few highlights:

* A much more capable [`pulumi deployment settings edit`](/docs/iac/cli/commands/pulumi_deployment_settings_edit/) that can now configure git authentication, dependency caching, template sources, drift remediation, tag triggers, review stacks, and the version control integration ([v3.262](https://github.com/pulumi/pulumi/releases/tag/v3.262.0), [v3.263](https://github.com/pulumi/pulumi/releases/tag/v3.263.0), [v3.264](https://github.com/pulumi/pulumi/releases/tag/v3.264.0))
* [`pulumi state promote`](/docs/iac/cli/commands/pulumi_state_promote/) now protects the resources it retains, so a subsequent update can't delete them before the generated code lands in your program ([v3.263](https://github.com/pulumi/pulumi/releases/tag/v3.263.0))
* A `pulumi logout --all --delete-credentials-key` option to remove the key that encrypts your stored credentials from the OS credential store ([v3.265](https://github.com/pulumi/pulumi/releases/tag/v3.265.0))
* Authenticode-signed Windows CLI and language-host binaries ([v3.265](https://github.com/pulumi/pulumi/releases/tag/v3.265.0))
* Support for importing a `pulumi:index:Stash` resource ([v3.262](https://github.com/pulumi/pulumi/releases/tag/v3.262.0))
* Slightly faster startup across all commands ([v3.264](https://github.com/pulumi/pulumi/releases/tag/v3.264.0))

... plus a long list of PCL, program-generation, and SDK fixes, and the foundations for [component state migrations](/blog/component-state-migrations/) across the engine and the Go, Python, and Node.js SDKs. See the [Releases page on GitHub](https://github.com/pulumi/pulumi/releases) for details.
