---
title: "CLI and SDK rollup: Automation API commands, resourceExists, and more"
date: 2026-10-28
meta_desc: Our October CLI and SDK releases expand the Automation API, add a resourceExists check, retire pulumi watch, and more.
authors:
    - christian-nunciato
---

We shipped a bunch of new features and improvements in the Pulumi CLI and SDK this month. A few highlights:

* A big expansion of the generated [Automation API](/docs/guides/automation-api/) for Node.js, Python, and Go, adding `version`, `whoami`, `install`, `state`, `env`, `up`, and `logs` commands ([v3.268](https://github.com/pulumi/pulumi/releases/tag/v3.268.0), [v3.271](https://github.com/pulumi/pulumi/releases/tag/v3.271.0), [v3.273](https://github.com/pulumi/pulumi/releases/tag/v3.273.0))
* A new `resourceExists` built-in — and generated `exists` methods — that check whether a resource with a given ID exists without adopting it into your stack ([v3.273](https://github.com/pulumi/pulumi/releases/tag/v3.273.0))
* Version 2 of the `--policy-pack-config` format, which nests policy configuration under `policies` and adds an `exceptions` field, plus a `--show-policy-exceptions` flag for `pulumi up` and `pulumi preview` ([v3.271](https://github.com/pulumi/pulumi/releases/tag/v3.271.0), [v3.272](https://github.com/pulumi/pulumi/releases/tag/v3.272.0))
* New [`pulumi env change-request`](/docs/iac/cli/commands/pulumi_env_change-request/) commands for reviewing, approving, and applying ESC change requests from the CLI ([v3.272](https://github.com/pulumi/pulumi/releases/tag/v3.272.0))
* Fixes to `pulumi org audit-log` so it honors `--user` and `--event-type`, moves to the V2 audit log API, and adds `--end-time` ([v3.271](https://github.com/pulumi/pulumi/releases/tag/v3.271.0))

We also retired the deprecated `pulumi watch` command and the bare `pulumi logs` command in favor of its subcommands ([v3.273](https://github.com/pulumi/pulumi/releases/tag/v3.273.0)).

See the [Releases page on GitHub](https://github.com/pulumi/pulumi/releases) for the full list.
