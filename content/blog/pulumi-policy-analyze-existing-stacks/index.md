---
title: "Introducing `pulumi policy analyze` for existing stacks"
date: 2026-03-28
draft: false
meta_desc: "Use the new `pulumi policy analyze` command to run local policy packs against existing stack state, with workflows for developers and AI agents."
authors:
    - fraser-waters
tags:
    - policy-as-code
    - features
    - iac
    - ai
social:
    twitter: "New in Pulumi CLI: `pulumi policy analyze` runs policy packs against existing stack state, making policy testing faster for developers and automation workflows."
    linkedin: "Pulumi now includes `pulumi policy analyze`, a new command for running local policy packs against existing stack state without running your Pulumi program. It is useful for policy authoring, regression testing, and automation workflows, including agent-driven checks."
---

We just merged a new Pulumi CLI command: [`pulumi policy analyze`](https://github.com/pulumi/pulumi/pull/22250).

This command analyzes an existing stack snapshot against one or more local policy packs, without running your Pulumi program and without making provider calls.

<!--more-->

## Why this command matters

Policy authoring and policy updates usually involve an iteration loop:

1. Make a policy change.
1. Run a policy check.
1. Inspect violations or remediations.
1. Repeat until the policy behavior matches intent.

Before this command, that loop often depended on `pulumi preview` or `pulumi up`, which can be heavier than you need when your goal is validating policy logic against known state.

With `pulumi policy analyze`, you can evaluate your current stack state directly and quickly.

## Basic usage

At minimum, provide a policy pack path and optionally a stack:

```bash
pulumi policy analyze \
  --policy-pack ./policy-pack \
  --stack dev
```

You can also pass a config file for each policy pack:

```bash
pulumi policy analyze \
  --policy-pack ./policy-pack \
  --policy-pack-config ./policy-config.dev.json \
  --stack dev
```

If any mandatory policy violations are found, the command exits non-zero.

If remediation policies fire, those changes are reported in output, but stack state is not modified.

## Testing new policy packs as a developer

For policy pack development, this command is useful as a tight local feedback loop:

1. Pick a representative stack (`dev`, `staging`, or a fixture stack).
1. Run `pulumi policy analyze` against that stack after each policy change.
1. Use the output to verify mandatory, advisory, and remediation behavior.
1. Repeat before publishing the policy pack or attaching it to broader policy groups.

Two output modes are especially useful:

1. `--diff` for a concise, human-readable view while iterating locally.
1. `--json` for structured output that can be consumed in scripts and CI.

## Using it in AI and agent workflows

This command is also a good primitive for AI-assisted policy workflows.

Because `pulumi policy analyze` can emit JSON and a clear process exit code, agents can use it for deterministic policy evaluation steps:

1. Propose or edit policy rules.
1. Run `pulumi policy analyze --json` against target stacks.
1. Parse violations and remediation signals.
1. Suggest policy fixes, config adjustments, or targeted infrastructure changes.
1. Re-run analysis until mandatory violations are resolved.

A few practical reasons this works well for agents:

1. It does not require executing the Pulumi program for each check.
1. It does not make provider calls, reducing side effects and runtime variance.
1. It gives machine-readable output and a fail/success contract for automation.

In short, this command helps both humans and agents treat policy validation as a fast, repeatable, test-like step.

## Try it out

If you are authoring or tuning policy packs, start by running this command against a known stack in your environment. It is a quick way to validate policy behavior before rollout.

For implementation details, see the merged PR: [pulumi/pulumi#22250](https://github.com/pulumi/pulumi/pull/22250).
