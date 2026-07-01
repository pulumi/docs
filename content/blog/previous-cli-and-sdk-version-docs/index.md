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
        Pinned to an older Pulumi CLI or SDK release and reading docs that describe a newer one?

        That mismatch just went away. No more cross-checking which docs match your release. Here's what changed.
    linkedin: |
        If you've ever pinned a Pulumi CLI or SDK to an older release, you know the small friction: the documentation on the site describes the latest version, not the one you're actually running.

        So you cross-reference against a changelog, guessing which flags and APIs still apply to the version in your project.

        We just removed that step for the CLI command reference and the SDK API docs, across Node.js, Python, .NET, and Java.

        The fix itself is small, but it makes the reference trustworthy again for teams that don't upgrade on day one.

        Here's what changed.
    bluesky: |
        For a while, running an older Pulumi release meant the docs on the site described a newer one. We closed that gap.

        You no longer have to guess which parts of the reference still apply to your version. Here's what we shipped.
---

Pinned to an older Pulumi CLI or SDK version and finding that the docs describe a newer release? The [Pulumi CLI command reference](/docs/iac/cli/commands/) and the SDK API docs now include a version selector, so the documentation you're reading matches the version you're actually running.

<!--more-->

## How it works

When you open the [CLI command reference](/docs/iac/cli/commands/), you'll see a version dropdown near the top of the page, below the title. The SDK API docs carry the same dropdown in the upper-right corner. Choose a release, and the page loads the documentation generated for that exact version.

![Version selector near the top of the Pulumi CLI command reference](cli-version-selector.png)

![Version selector in the upper-right corner of the Pulumi Node.js SDK API docs](sdk-version-selector.png)

## What's available

Alongside the latest release, we keep immutable snapshots of previous versions. The CLI command reference and the Node.js, Python, .NET, and Java SDK API docs are all covered, so the matching docs are always a dropdown away.

History reaches back to around v3.150.0 (early 2025); older CLI releases already prompt you to upgrade, so that makes a sensible floor. The Go SDK is versioned on [pkg.go.dev](https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3), so its documentation lives there rather than on the docs site.

## Get started

Head to the [CLI command reference](/docs/iac/cli/commands/) or the [SDK API docs](/docs/reference/) and try the version dropdown. If your projects pin specific releases, select your version and read the docs that match.

Have feedback? Let us know in the [Pulumi Community Slack](https://slack.pulumi.com) or by opening an issue on [GitHub](https://github.com/pulumi/docs).

{{< blog/cta-button "Browse the CLI command reference" "/docs/iac/cli/commands/" >}}
