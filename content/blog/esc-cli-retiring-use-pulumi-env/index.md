---
title: "The Standalone ESC CLI Is Retiring: Use pulumi env"
date: 2026-07-22
draft: false
meta_desc: "The standalone esc CLI is archived as of v0.26.0. Every ESC command is available in the Pulumi CLI under pulumi env: one binary to install and upgrade."
feature_image: feature.png
authors:
    - pablo-terradillos
    - boris-schlosser
tags:
    - esc
    - features
category: product
schema_type: auto

# Social media copy — auto-posted to X, LinkedIn, and Bluesky when merged to master.
# Character limits: X ~280, Bluesky 300, LinkedIn 3000. Leave blank to skip a platform.
social:
    twitter: |
        The standalone esc CLI is retired. v0.26.0 is the final release and the repo is archived.

        Most commands move over by swapping esc for pulumi env. Three of them don't. Here's what moves where.
    linkedin: |
        Pulumi ESC shipped with its own CLI. Every one of its commands has also been available inside the Pulumi CLI, under pulumi env.

        Keeping both around stopped making sense. One binary to install, one login to manage, one place to look things up — that matters whether the operator is a person or an agent.

        So esc v0.26.0 is the final standalone release. The repository is archived and the code now lives in pulumi/pulumi.

        If you already use the Pulumi CLI, nothing changes for you. If you use esc, the switch is mostly mechanical, with a handful of commands that don't follow the pattern.

        We wrote up the migration, command by command.
    bluesky: |
        esc v0.26.0 is the last standalone ESC CLI release. The repo is archived, and every command now lives under pulumi env in the Pulumi CLI.

        Swapping esc for pulumi env covers most of them. The ones it doesn't cover are the ones worth knowing. We documented all of them.
---

[Pulumi ESC](/docs/esc/) CLI v0.26.0 is the latest standalone release. We encourage users to use the [Pulumi CLI](/docs/iac/cli/) instead.

The [ESC repository](https://github.com/pulumi/esc) has been archived and the code now lives under [pulumi](https://github.com/pulumi/pulumi).

<!--more-->

We have decided to stop delivering ESC as a standalone CLI. The `pulumi env` commands were never a reimplementation — the Pulumi CLI has built them from the ESC CLI's own code since ESC's first release, which is why the same command surface has always been available under [`pulumi env`](/docs/iac/cli/commands/pulumi_env/).

## Why are we making this change

Pulumi ESC is the best way to store and manage configuration and secrets in your Pulumi programs and while you can certainly use ESC to store secrets and configurations for your applications or to manage your AI agents' credentials, it's still a core feature of [Pulumi Cloud](/docs/iac/guides/basics/pulumi-cloud-vs-oss/), and we want to make sure we deliver a consistent experience across our entire suite.

In addition to consistency, ESC and the Pulumi CLI share a lot of capabilities to interface to Pulumi Cloud and we want to make it easier and simpler for our customers: it's now easier to understand which Pulumi organization you are working with, which user is logged in, etc.

### Playing nicer with humans and AI agents

A single CLI means one binary to install, one login to manage, and one place to look things up. That matters whether the operator is a person or an agent.

AI agents love code, and they love CLIs. By unifying the Pulumi CLI and ESC we offer a single place to look up operations around your Pulumi programs. Agents can now reason better about where to store configuration and secrets, without being confused by multiple CLI options that interface against the same service.

### Faster improvements

With a shared CLI, any improvement to account management is automatically delivered to both: Pulumi and ESC users. At the same time, both benefit from ESC improvements and new features from day 1.

ESC is a core component of our platform; a separate interface no longer makes sense.

## Do I need to update?

If you are using the ESC CLI, you should switch as soon as possible, as the standalone binary will not get the latest features. Don't worry — the mapping is mechanical, and the [migration guide](/docs/esc/guides/migrate-from-esc-cli/) covers it command by command:

- `esc env <command>` becomes `pulumi env <command>`. For example, `esc env ls` becomes `pulumi env ls`.
- The `esc open` and `esc run` shortcuts become `pulumi env open` and `pulumi env run`.
- `esc login`, `esc logout`, and `esc version` become `pulumi login`, `pulumi logout`, and `pulumi version`.

If you are already using the Pulumi CLI, you have nothing to worry about; this has no effect since ESC commands were already available under the `pulumi env` sub-command.

Ready to switch? [Install the Pulumi CLI](/docs/install/) if you don't have it yet, then run `pulumi env ls` to see your environments. Every command is documented in the [`pulumi env` reference](/docs/iac/cli/commands/pulumi_env/).
