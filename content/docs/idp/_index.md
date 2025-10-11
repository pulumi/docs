---
title: Internal Developer Platform
linktitle: Internal Developer Platform
docs_home: true
notitle: true
norightnav: true
menu:
  idp:
    identifier: idp-home
    weight: 1


meta_desc: Build self-service infrastructure workflows with reusable components, templates, and golden paths—from Day 0 to Day 2.
meta_image: /images/docs/meta-images/docs-meta.png
h1: Internal Developer Platform
description: Build self-service infrastructure workflows with reusable components, templates, and golden paths—from Day 0 to Day 2.

link_buttons:
  primary:
    label: Get Started
    link: /docs/idp/get-started/

sections:
- type: flat
  heading: Overview
  description_md: |
    Pulumi IDP provides infrastructure building blocks that platform teams publish and developers consume. Platform teams author templates and components that codify organizational standards, then publish them to a private registry. Developers scaffold infrastructure from templates, compose components in code, or deploy directly from the console.

    The platform supports Day 0 through Day 2 operations: establishing golden paths, provisioning infrastructure, and maintaining deployed resources.

- type: button-cards
  heading: Getting started
  cards:
  - emoji: 🚀
    heading: Get Started
    link: /docs/idp/get-started/
    description: Learn the IDP approach and how platform teams provide self-service infrastructure workflows.

  - emoji: 📦
    heading: Private Registry
    link: /docs/idp/get-started/private-registry/
    description: Centralized registry for your organization's templates, components, and infrastructure building blocks.

  - emoji: 🎯
    heading: Templates
    link: /docs/idp/developer-portals/templates/
    description: Scaffold new projects from organization templates that encode standards and best practices.

  - emoji: ⚙️
    heading: Workflows
    link: /docs/idp/get-started/workflows/
    description: Provision infrastructure through code, low-code YAML templates, or no-code deployment from the console.

  - emoji: 🏗️
    heading: Services
    link: /docs/idp/get-started/services/
    description: Logical groupings of stacks, environments, and resources that model your infrastructure.

  - emoji: 🔗
    heading: Developer Portals
    link: /docs/idp/developer-portals/
    description: Integrate with Backstage, use the New Project Wizard, or build custom portals.

  - emoji: 🤖
    heading: Publishing from GitHub Actions
    link: /docs/idp/get-started/publishing-from-github-actions/
    description: Automate component testing and publishing to your private registry with GitHub Actions workflows.

- type: flat
  heading: Have questions?
  description: <p>For questions or feedback, reach out on <a href="https://slack.pulumi.com" target="_blank">community Slack</a>, <a href="https://github.com/pulumi" target="_blank">GitHub</a>, or <a href="/support/">contact support</a>.</p>

---
