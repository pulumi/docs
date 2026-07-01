---
title: "New: Previous CLI and SDK Version Docs on pulumi.com"
date: 2026-07-01
draft: false
meta_desc: "The Pulumi CLI command reference and SDK API docs now include a version selector, so you can browse the docs that match the release you're running."
meta_image: meta.png
feature_image: feature.png
authors:
    - cam-soper
tags:
    - pulumi-cli
    - features
    - announcements
category: product
schema_type: auto
social:
    twitter: |
        Pinned to an older Pulumi CLI or SDK release and reading docs for a newer one? The CLI command reference and SDK API docs now have a version selector.

        Pick your release from the dropdown and the docs match what you're running. Here's where to find it.
    linkedin: |
        Stuck on an older Pulumi CLI or SDK version and comparing your code against docs written for a newer release? That mismatch just got easy to avoid.

        The Pulumi CLI command reference and the SDK API docs now include a version selector. On the CLI reference it sits right next to the page title; on the SDK docs it's in the upper-right corner.

        Pick the release you're running, and the page loads the documentation generated for that exact version. Older snapshots are preserved, so the docs for the version in your project are always a dropdown away.

        Node.js, Python, .NET, and Java are covered, alongside the CLI.

        Here's how it works.
    bluesky: |
        We've closed the gap between the Pulumi version you're running and the docs you're reading.

        The CLI command reference and SDK API docs now have a version selector — pick your release and the docs match. Here's where to find it.
---

Pinned to an older Pulumi CLI or SDK version and finding that the docs describe a newer release? The [Pulumi CLI command reference](/docs/iac/cli/commands/) and the SDK API docs now include a version selector, so the documentation you're reading matches the version you're actually running.

<!--more-->

## How it works

When you open the [CLI command reference](/docs/iac/cli/commands/), you'll see a version dropdown right next to the page title. The SDK API docs carry the same dropdown in the upper-right corner. Choose a release, and the page loads the documentation generated for that exact version.

![Version selector next to the title on the Pulumi CLI command reference](cli-version-selector.png)

![Version selector in the upper-right corner of the Pulumi Node.js SDK API docs](sdk-version-selector.png)

## What's available

Alongside the latest release, we keep immutable snapshots of previous versions. The CLI command reference and the Node.js, Python, .NET, and Java SDK API docs are all covered, so the matching docs are always a dropdown away.

History reaches back to around v3.150.0 (early 2025); older CLI releases already prompt you to upgrade, so that makes a sensible floor. The Go SDK is versioned on [pkg.go.dev](https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3), so its documentation lives there rather than on the docs site.

## Get started

Head to the [CLI command reference](/docs/iac/cli/commands/) or the [SDK API docs](/docs/reference/) and try the version dropdown. If your projects pin specific releases, the docs that match are now a click away.

Have feedback? Let us know in the [Pulumi Community Slack](https://slack.pulumi.com) or by opening an issue on [GitHub](https://github.com/pulumi/docs).

{{< blog/cta-button "Browse the CLI command reference" "/docs/iac/cli/commands/" >}}
