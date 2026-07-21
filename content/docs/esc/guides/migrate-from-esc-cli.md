---
title_tag: Migrate from the ESC CLI to pulumi env
title: Migrate from the ESC CLI
h1: Migrate from the ESC CLI to pulumi env
meta_desc: The standalone esc CLI retired as of v0.26.0. Learn how to map every esc command to its pulumi env equivalent in the Pulumi CLI.
menu:
  esc:
    parent: esc-guides
    identifier: esc-guides-migrate-from-esc-cli
    weight: 20
aliases:
  - /docs/esc-cli/
---

The standalone Pulumi ESC CLI (`esc`) retired. [v0.26.0](https://github.com/pulumi/esc/releases/tag/v0.26.0) is its final release, the [`pulumi/esc`](https://github.com/pulumi/esc) repository is archived, and the code now lives in [`pulumi/pulumi`](https://github.com/pulumi/pulumi).

Every ESC command is available in the [Pulumi CLI](/docs/install/) under the [`pulumi env`](/docs/iac/cli/commands/pulumi_env/) sub-command, and has been since ESC's first release. If you are already using the Pulumi CLI, nothing changes for you. If you have the standalone `esc` binary installed, this guide shows you how to switch.

## What changed

The standalone binary no longer receives updates. New ESC features ship in the Pulumi CLI only, so a workflow pinned to `esc` will drift further behind with each release.

Nothing changes on the service side. Your environments, values, versions, and access controls are unaffected — this is a change to how you invoke ESC from your terminal, not to ESC itself.

## Command mapping

The mapping is mechanical:

| Standalone ESC CLI | Pulumi CLI |
|---|---|
| `esc env <command>` | `pulumi env <command>` |
| `esc env ls` | [`pulumi env ls`](/docs/iac/cli/commands/pulumi_env_list/) |
| `esc env open <env>` | [`pulumi env open <env>`](/docs/iac/cli/commands/pulumi_env_open/) |
| `esc env run <env> -- <cmd>` | [`pulumi env run <env> -- <cmd>`](/docs/iac/cli/commands/pulumi_env_run/) |
| `esc open <env>` | [`pulumi env open <env>`](/docs/iac/cli/commands/pulumi_env_open/) |
| `esc run <env> -- <cmd>` | [`pulumi env run <env> -- <cmd>`](/docs/iac/cli/commands/pulumi_env_run/) |
| `esc login` | [`pulumi login`](/docs/iac/cli/commands/pulumi_login/) |
| `esc logout` | [`pulumi logout`](/docs/iac/cli/commands/pulumi_logout/) |
| `esc version` | [`pulumi version`](/docs/iac/cli/commands/pulumi_version/) |

Two details are worth calling out:

- `esc open` and `esc run` were top-level shortcuts for `esc env open` and `esc env run`. Both forms map to the same `pulumi env` command, so `esc open` and `esc env open` both become `pulumi env open`.
- `login`, `logout`, and `version` are Pulumi CLI commands, not `pulumi env` commands. `esc login` becomes `pulumi login`, not `pulumi env login`.

Everything else — like `edit` or `get` — keeps its name under `pulumi env`. See the [`pulumi env` reference](/docs/iac/cli/commands/pulumi_env/) for the full surface.

## Migrate your setup

1. [Install the Pulumi CLI](/docs/install/) if you don't already have it, or upgrade an existing install to pick up the latest ESC features.
1. Confirm ESC is available:

    ```bash
    pulumi env ls
    ```

    You should see the environments you had access to through `esc`.

1. Update your scripts, CI pipelines, and documentation using the mapping above.
1. Remove the standalone binary once nothing references it. If you installed it with Homebrew, run `brew uninstall pulumi/tap/esc`. If you installed it with the `get.pulumi.com/esc` script, delete the `esc` binary from `~/.pulumi/bin`.

## Authentication

You do not need to log in again. The ESC CLI used the Pulumi CLI's credential store, so an existing `pulumi login` session already covers `pulumi env`.

`PULUMI_ACCESS_TOKEN` works the same way in both, which means CI pipelines that set it need no credential changes — only the command names change.

## Next steps

- [Running commands with `pulumi env run`](/docs/esc/guides/running-commands/) — inject secrets and configuration into any command or script.
- [`pulumi env` command reference](/docs/iac/cli/commands/pulumi_env/) — every sub-command, flag, and example.
- [Use ESC with Pulumi IaC](/docs/esc/guides/pulumi-iac/) — how ESC environments feed your stack configuration.
