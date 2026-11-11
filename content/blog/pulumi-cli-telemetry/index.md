---
title: "Adding telemetry to the Pulumi CLI"
date: 2026-11-13
draft: false
meta_desc: "Starting with v3.276.0, the Pulumi CLI collects anonymous usage telemetry. Here's what we collect, why, and how to opt out."
# Leave blank — add a real hero image later with /blog-feature-image or a
# designer-supplied one (1884x1256). Never commit a placeholder. Required
# before publishing unless the post is `category: general` or `draft: true`.
feature_image:
authors:
    - tatiana-cooke
tags:
    - pulumi-cli
    - announcements
# Required: exactly one category (a scalar) from the closed set in
# data/blog_categories.yaml. Use "general" for posts that don't clearly fit a
# specific kind. Validated by `make lint`.
category: product
schema_type: auto

# Social media copy — auto-posted to X, LinkedIn, and Bluesky when merged to master.
# Character limits: X ~280, Bluesky 300, LinkedIn 3000. Leave blank to skip a platform.
social:
    twitter:
    linkedin:
    bluesky:
---

We want to give our users the best possible experience as they build with our IaC platform. In the past year, we've been excited to hear about new usage patterns and even more ambitious projects our users want to take on by leveraging AI in combination with our SDKs and CLI. In order to understand where we may have gaps, we're going to be introducing thoughtful telemetry to the CLI. Users will have the option to opt out if they prefer not to share this telemetry.

Starting with Pulumi CLI v3.276.0, the Pulumi CLI will collect anonymous usage data. This post explains more about why we're collecting this data, what data we'll collect, and how to turn it off with one command or environment variable.

<!--more-->

## Why we're doing this

Our users depend on our SDKs and CLI to provide informative errors, help them triage and understand infrastructure changes, and to manage operationally critical infrastructure. We continue to see usage of our platform via coding agents grow. Over the past six months the CLI and SDKs have picked up significant new features, a broad swath of new commands, and we're making foundational investments in our user-facing diagnostics. Knowing whether a CLI invocation originated with a human at a terminal, automation in a CI system, or an agentic coding harness lets us see how we can improve those paths for the specific usage.

We're focused on understanding questions that directly impact this experience, including:

- Which commands fail most often, and do the diagnostics we report aid in rapid recovery?
- Has a recent release change impacted user outcomes?
- As more users adopt coding agents, does our platform provide the helpful information to agents?

Our underlying goal is to ensure we're better able to quickly discover and respond to friction points. You should see bigger improvements each time we update the CLI as a result.

## What we will collect

Our telemetry is limited to a fixed set of events with enumerated values. We've focused these designs on capturing telemetry that helps us drive experience improvements. With this update we'll start capturing:

- Which command ran, which version of the CLI was used, which flags were set, and which `PULUMI_*` environment variables were present (names only, never their values). This helps us understand version- and command-specific issues.
- Whether the command succeeded, and if it failed, the exit code and error class. This helps us dig in on where we can iterate on our diagnostic experience.
- Which kind of context it ran in: an interactive terminal, a CI system, or a detected coding agent. This helps us identify different usage patterns over time that may inform the design of our CLIs and SDKs.
- Which backend the command targeted, such as Pulumi Cloud, a local file, or an object store. This helps us make sure we're delighting both our Pulumi Cloud and DIY backend users.

Every event carries two random identifiers: one for your installation, stored in `$PULUMI_HOME/telemetry.json`, and one for the individual command invocation. These let us tell "one person hit this error ten times" apart from "ten people hit it once". They aren't tied to your account, and we don't fingerprint your machine. Deleting `$PULUMI_HOME/telemetry.json` gives you a fresh installation ID.

## What we don't collect

The telemetry pipeline never collects arbitrary data from its environment. Instead, the pipeline only submits values that conform to a published schema that consists of a set of booleans, numbers, and enumerations. This approach helps ensure that the CLI cannot send:

- Stack, project, or organization names.
- Resource names, types, or configuration.
- Full error messages, which can include paths and other identifying details.
- Your account identity or anything from your source code.

We chose this constraint deliberately. Sanitizing free-form text after the fact is error-prone, so we didn't build a way to send free-form text at all.

## When and how this change will roll out

Telemetry will ship in Pulumi CLI v3.276.0 and will apply to any installation that is used with the Pulumi Cloud or a DIY Backend. Self-hosted Pulumi Cloud installations and the EU region aren't included in this release.

The first time a CLI with telemetry runs on your machine, it prints a notice telling you that telemetry is on and how to disable it. For existing installations, this happens the first time you run a command after upgrading.

To keep the CLI fast and responsive for interactive use, events are written to a local log and sent in batches in the background. In CI and other non-interactive scenarios, the CLI waits for the send to finish so nothing is lost when the job exits.

## How to opt out

You can disable telemetry using the following commands.

Disable it permanently for an installation:

```bash
pulumi telemetry disable
```

This writes `"telemetry": "disabled"` to `$PULUMI_HOME/telemetry.json`. Run `pulumi telemetry` at any time to check the current state, and `pulumi telemetry enable` to turn it back on.

Disable it through the environment, which is handy for CI images and shared dev containers:

```bash
export PULUMI_TELEMETRY=0
```

Or use the cross-tool convention from [donottrack.sh](https://donottrack.sh/):

```bash
export DO_NOT_TRACK=1
```

If more than one is set, `DO_NOT_TRACK` wins, then `PULUMI_TELEMETRY`, then the setting in `telemetry.json`.

## Questions or feedback

<!-- TODO: Link "CLI telemetry documentation" to the docs page once it exists. -->
The full details live in the CLI telemetry documentation. If you have questions, please open an issue on [pulumi/pulumi](https://github.com/pulumi/pulumi/issues) or find us in the [Pulumi Community Slack](https://slack.pulumi.com/).

Build on!

-The Pulumi Team
