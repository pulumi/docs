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
  support:
    parent: support-home
    identifier: support-troubleshooting
    weight: 2
aliases:
  - /docs/support/troubleshooting/infrastructure/
  - /docs/reference/troubleshooting/
  - /docs/troubleshooting/
  - /docs/troubleshooting/overview/
  - /docs/iac/support/
  - /docs/iac/troubleshooting/

sections:
- type: button-cards
  heading: Getting started
  cards:
  - emoji: ⚠️
    heading: Common Issues
    link: /docs/support/troubleshooting/common-issues/
    description: Guide to fixing specific problems that may arise in Pulumi programs.

  - emoji: 🔄
    heading: CI/CD Troubleshooting
    link: /docs/support/troubleshooting/ci-cd/
    description: Resolve continuous integration and deployment pipeline issues.

  - emoji: 📝
    heading: Editing State Files
    link: /docs/support/troubleshooting/editing-state-files/
    description: Safe techniques for modifying Pulumi state files when necessary.

- type: flat
  heading: Need more help?
  description_md: |
    - Join [Community Slack](https://slack.pulumi.com) for fast community support
    - Open [GitHub Issues](https://github.com/pulumi/pulumi/issues/new) to report bugs
    - [Contact us](/contact/) for paid support options

- type: flat
  heading: Have questions?
  description: <p>For questions or feedback, reach out on <a href="https://slack.pulumi.com" target="_blank">community Slack</a>, <a href="https://github.com/pulumi" target="_blank">GitHub</a>, or <a href="/support/">contact support</a>.</p>
---

<script>
// Redirect to the new update conflict page
// https://github.com/pulumi/pulumi/issues/20846
if (window.location.hash === "#conflict") {
  window.location = "/docs/support/troubleshooting/common-issues/update-conflicts/"
}
</script>