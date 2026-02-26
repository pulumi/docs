---
title: "Now GA: Up to 20x Faster Pulumi Operations for Everyone"
allow_long_title: true
date: 2026-02-27
draft: false
meta_desc: "A major performance enhancement is now on by default for all Pulumi Cloud organizations. Faster operations, less network traffic, no opt-in required."
meta_image: meta.png
authors:
    - thomas-gummerer
    - pat-gavlin
tags:
    - performance
    - pulumi-cloud
    - features
    - releases
social:
    twitter: |
        Now GA: Up to 20x Faster Pulumi Operations for Everyone

        - Up to [TODO: x] faster operations
        - p99 state updates under [TODO: x] seconds
        - [TODO: x]%+ reduction in network traffic
        - Zero config required — just upgrade your CLI

        Your deploys just got a whole lot faster. [link]
    linkedin: |
        Now GA: Up to 20x Faster Pulumi Operations for Everyone

        In January we introduced a new state management approach that sends incremental changes instead of full snapshots, cutting operation times by up to [TODO: x].

        Today, it's enabled by default for every Pulumi Cloud organization. No environment variables, no feature flags, no opt-in. Just faster deploys.

        ## The numbers

        Since the opt-in launch, we've processed thousands of state updates across many organizations. Here's what we're seeing in production:

        - p99 state update time: under [TODO: x] seconds
        - p50 state update time: under [TODO: x]ms
        - Network traffic reduction: [TODO: x]%+ for large stacks
        - Operation time reduction: up to [TODO: x] on parallelizable workloads

        ## What changed

        Previously, Pulumi serialized full state snapshots at every step. For large stacks, this was a bottleneck. The new approach sends incremental entries in parallel; Pulumi Cloud reconstructs the full snapshot server-side.

        ## What you need to do

        Nothing. If you're on Pulumi CLI v3.211.0 or later, you're already getting the faster experience. 

        Read more: [link]
---

In January, we [introduced a major performance enhancement for Pulumi Cloud](/blog/journaling/) through a fundamental change to how Pulumi manages state that speeds up operations by up to [TODO: x]. After a staged rollout across many organizations, **it is now enabled by default for every Pulumi Cloud organization**. No opt-in required.

<!--more-->

## What is new here?

Every time you run `pulumi up`, `pulumi destroy`, or `pulumi refresh`, Pulumi saves a snapshot of your infrastructure state at each step. This guarantees that if something fails mid-operation, Pulumi knows exactly what happened — but for large stacks, serializing and uploading the full snapshot at every step is a bottleneck.

The improvement sends incremental state updates to Pulumi Cloud in parallel; Pulumi Cloud reconstructs the full snapshot server-side. Same data integrity, dramatically less overhead. For the full technical deep-dive, see our [original blog post](/blog/journaling/).

## Production results

Since January, we've processed many state updates across many organizations:

| Metric | Value |
|--------|-------|
| p99 state update time | [TODO: x] |
| p50 state update time | [TODO: x] |
| Network traffic reduction | [TODO: x] |
| Operation time improvement | [TODO: x] |

The gains are most dramatic on stacks with high parallelism, but every stack benefits from reduced per-step overhead.

## How we rolled it out

We took a staged approach — shadow mode in CI, opt-in beta with a feature flag, then flag-for-all gated by `PULUMI_ENABLE_JOURNALING=true`. At each stage we monitored for snapshot mismatches. We found zero data integrity issues in production, and today we're flipping the default.

## What you need to do

**Nothing.** If you're on Pulumi CLI v3.211.0+ with Pulumi Cloud, it's already active.

If you encounter any issues, reach out on the [Pulumi Community Slack](https://slack.pulumi.com/) or through [Pulumi Support](https://support.pulumi.com/hc/en-us).
