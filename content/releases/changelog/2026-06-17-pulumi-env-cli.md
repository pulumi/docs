---
title: Retiring the standalone ESC CLI
date: 2026-06-17
aliases:
    - /releases/changelog/pulumi-env-cli/
meta_desc: The standalone Pulumi ESC CLI is being retired in favor of pulumi env.
authors:
    - christian-nunciato
---

When we introduced Pulumi ESC, we shipped it as both a [standalone CLI tool](https://github.com/pulumi/esc) (`esc`) as well as a subcommand of the Pulumi CLI (`pulumi env`). Both offered the same functionality, but since the majority of ESC users also use Pulumi IaC, we've chosen to retire the standalone CLI in favor of a unified [`pulumi env`](/docs/iac/cli/commands/pulumi_env/).

The final release of the standalone `esc` binary will be next month (July, 2026), at which time the [GitHub repository](https://github.com/pulumi/esc) will be archived.

To learn more about Pulumi ESC and `pulumi env`, visit the [Pulumi ESC documentation](/docs/esc/).
