---
title: Troubleshooting
title_tag: Pulumi Troubleshooting Guide
linktitle: Troubleshooting
docs_home: true
notitle: true
norightnav: true
meta_desc: Comprehensive troubleshooting guides for common issues with Pulumi infrastructure, deployments, and configuration.
h1: Troubleshooting Guide
description: <p>Resources for diagnosing and resolving issues with Pulumi programs and deployments.</p>
menu:
  iac:
    parent: iac-operations
    identifier: iac-operations-troubleshooting
    name: Troubleshooting
    weight: 30
aliases:
  - /docs/support/troubleshooting/
  - /docs/support/troubleshooting/infrastructure/
  - /docs/support/troubleshooting/common-issues/
  - /docs/reference/troubleshooting/
  - /docs/troubleshooting/
  - /docs/troubleshooting/overview/
  - /docs/iac/support/
  - /docs/iac/troubleshooting/

sections:
- type: button-cards
  heading: Common issues
  cards:
  - icon: warning
    heading: Update Conflicts
    link: /docs/iac/operations/troubleshooting/update-conflicts/
    description: 'Resolve "409 conflict: Another update is currently in progress" errors.'

  - icon: warning
    heading: Server Errors
    link: /docs/iac/operations/troubleshooting/server-errors/
    description: Handle 500 internal server errors from Pulumi Cloud.

  - icon: warning
    heading: Post-step Errors
    link: /docs/iac/operations/troubleshooting/post-step-errors/
    description: Troubleshoot post-step event failures and engine bugs.

  - icon: warning
    heading: Connection Issues
    link: /docs/iac/operations/troubleshooting/connection-issues/
    description: Fix network connectivity and proxy problems.

  - icon: warning
    heading: DIY Backend Access Errors
    link: /docs/iac/operations/stack-management/using-a-diy-backend/#error-reading-pulumimetayaml
    description: Resolve `read ".pulumi/meta.yaml"` errors when the CLI can't access a self-managed state backend.

  - icon: warning
    heading: Destroy Failures
    link: /docs/iac/operations/troubleshooting/destroy-failures/
    description: Handle scenarios when `pulumi destroy` fails.

  - icon: warning
    heading: Interrupted Updates
    link: /docs/iac/operations/troubleshooting/interrupted-updates/
    description: Recover from interrupted deployments.

  - icon: warning
    heading: macOS Architecture Mismatch
    link: /docs/iac/operations/troubleshooting/architecture-mismatch/
    description: Fix crashes or hangs on Apple Silicon caused by x86_64 binaries running under Rosetta 2.

- type: button-cards
  heading: Related
  cards:
  - icon: arrows-clockwise
    heading: CI/CD Troubleshooting
    link: /docs/iac/operations/continuous-delivery/troubleshooting/
    description: Resolve continuous integration and deployment pipeline issues.

  - icon: note-pencil
    heading: Editing State Files
    link: /docs/iac/operations/stack-management/editing-state-files/
    description: Safe techniques for modifying Pulumi state files when necessary.

  - icon: target
    heading: Targeted Updates
    link: /docs/iac/operations/stack-management/targeted-updates/
    description: Limit operations to specific resources with `--target` and `--exclude` when a stuck or misbehaving resource is blocking a wider update.

  - icon: chart-bar
    heading: Logging
    link: /docs/iac/operations/debugging/logging/
    description: CLI verbose logging and program logging for debugging and diagnostics.

  - icon: wrench
    heading: Using Dev Builds
    link: /docs/iac/operations/debugging/using-dev-builds/
    description: Install pre-release builds to access bug fixes that haven't shipped in a stable release yet.

- type: flat
  heading: Need more help?
  description_md: |
    - Join [Community Slack](https://slack.pulumi.com) for fast community support
    - See our [guide for filing GitHub issues](/docs/support/filing-issues/) to report bugs in the right repository
    - [Contact us](/contact/) for paid support options

- type: flat
  heading: Have questions?
  description: <p>For questions or feedback, reach out on <a href="https://slack.pulumi.com" target="_blank">community Slack</a>, <a href="https://github.com/pulumi" target="_blank">GitHub</a>, or <a href="/support/">contact support</a>.</p>
---

<script>
// Redirect to the new update conflict page
// https://github.com/pulumi/pulumi/issues/20846
if (window.location.hash === "#conflict") {
  window.location = "/docs/iac/operations/troubleshooting/update-conflicts/"
}

// Redirect to the new verbose logging page
// https://github.com/pulumi/docs/issues/16985
if (window.location.hash === "#verbose-logging") {
  window.location = "/docs/iac/operations/debugging/logging/#cli-verbose-logging"
}
</script>
