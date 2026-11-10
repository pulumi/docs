---
title: Delivery
linktitle: Delivery
docs_home: true
notitle: true
norightnav: true
menu:
  delivery:
    identifier: delivery-home
    weight: 1
meta_desc: Pulumi Delivery lets you write your release pipeline as a Pulumi program and promote each release through stages, stacks, jobs, and approval gates.
h1: Pulumi Delivery
description: <p>Write your release pipeline as a Pulumi program. Pulumi Cloud runs each release through your stages in order, updating stacks, running jobs, and waiting at the gates you define.</p>

link_buttons:
  primary:
    label: Get started
    link: /docs/delivery/get-started/
  secondary:
    label: Concepts
    link: /docs/delivery/concepts/

sections:
- type: button-cards
  heading: Learn Delivery
  cards:
  - icon: lightbulb
    heading: Concepts
    description: Pipeline programs, runs, stages, steps, sources, and releases, and how they fit together.
    link: /docs/delivery/concepts/
  - icon: arrows-clockwise
    heading: Sources and triggers
    description: Decide which repositories make up a release and which changes start a run.
    link: /docs/delivery/concepts/sources-and-triggers/
  - icon: lock-key
    heading: Stages and gates
    description: Order promotion between environments and hold a release for approval or a manual check.
    link: /docs/delivery/concepts/stages-and-gates/
  - icon: package
    heading: Steps
    description: Update stacks, run commands, and publish artifacts inside a stage.
    link: /docs/delivery/concepts/steps/

- type: button-cards
  heading: Build and operate pipelines
  cards:
  - icon: key
    heading: Cloud credentials
    description: Give each stage the cloud credentials it needs through Pulumi ESC.
    link: /docs/delivery/guides/cloud-credentials/
  - icon: code-window
    heading: Pipeline patterns
    description: Per-environment helpers, smoke tests, stacks that deploy together, and monorepos.
    link: /docs/delivery/guides/pipeline-patterns/
  - icon: wrench
    heading: Runs and stages
    description: Retry, cancel, roll back, redeploy, promote, and pause.
    link: /docs/delivery/operations/runs-and-stages/
  - icon: question
    heading: Troubleshooting
    description: Find out why a run is stuck or failed, and how to get it moving again.
    link: /docs/delivery/operations/troubleshooting/

- type: flat
  heading: Have questions?
  description: <p>Pulumi Delivery is in public preview. For questions or feedback, reach out on <a href="https://slack.pulumi.com" target="_blank">community Slack</a> or <a href="/support/">contact support</a>.</p>
---
