---
title: Building for agentic infrastructure
date: 2026-05-19
meta_desc: As agents take on more of the work of cloud infrastructure, they need tools that meet them where they are. Here's a closer look at what we've just shipped.
meta_image: /images/releases/may-2026/meta.png
label: May 2026 release
short_description: As agents take on more of the work of infrastructure, they need tools that meet them where they are.
feature_image: /images/releases/may-2026/release-hero-right-light.svg
feature_image_alt: Agent surfaces — Claude Code, OpenCode, Codex, and Pulumi Neo — around the Pulumi mark

hero:
  breadcrumb_label: May 2026
  heading: Building for agentic infrastructure
  description: |
    As agents take on more of the work of infrastructure, they need tools that meet them where they are.
    This month, we've got new commands, providers, integrations, and more that help humans and agents do
    infrastructure better.
  hero_image: /images/releases/may-2026/release-hero-bottom-dark.svg
  hero_image_alt: Agent surfaces — Claude Code, OpenCode, Codex, and Pulumi Neo — around the Pulumi mark
  hero_image_max_width: 430

intro:
  quote: |
    "LLMs are now doing over 20% of infrastructure deployments, up from
    virtually zero a year ago. We expect this to grow to over 50% this year."
  attribution: |
    — Joe Duffy, co-founder and CEO, on the increasing pace at which teams are adopting AI-driven infrastructure
  link: /blog/the-agentic-infrastructure-era/
  link_label: Read the blog post

toc_heading: What's New in This Release

sections:
  - anchor: meeting-agents
    label: Meeting agents where they are
    heading: Meeting agents where they are
    description: |
      What do coding agents love more than code? Well-designed CLIs. So we poured some love into the Pulumi CLI to
      make it even more usable for humans and agents alike.
    cards:
      - variant: text
        icon: terminal-window
        title: One-command execution
        description: |
          A new Node.js package enables `npx pulumi <anything>`-style commands so that agents can discover
          and run Pulumi commands more easily.

      - variant: image-top
        image: /images/releases/may-2026/release-pulumi-do.svg
        image_alt: pulumi do — extruded type illustration
        icon: rows-plus-bottom
        title: Imperative infrastructure operations
        description: |
          The new `pulumi do` command enables direct operations like create, read, update, delete, and list
          across all Pulumi-supported clouds and services.
        link: /blog/pulumi-do-direct-resource-operations/

      - variant: text
        icon: user-circle-plus
        title: Agent accounts
        description: |
          Ephemeral Pulumi Cloud accounts allow agents like Claude Code and Codex to spin up Pulumi-managed
          infrastructure without requiring a human in the loop.
        link: /docs/administration/organizations-teams/agent-accounts/

      - variant: image-left
        image: /images/releases/may-2026/release-cloud-cli.svg
        image_alt: Pulumi Cloud surfaces — stack, env, org, deployment — reachable from the CLI
        icon: cloud-check
        title: Pulumi Cloud in the CLI
        description: |
          Dozens of new commands for Pulumi operations previously only available in the browser. Think of it
          like the `gh` CLI (which agents love) for Pulumi Cloud.
        link: /blog/better-cli-interactions-for-agents-and-humans/

  - anchor: neo-everywhere
    label: Neo everywhere you work
    heading: Neo everywhere you work
    description: |
      With this release, Neo, our infrastructure agent, moves out of the Pulumi Cloud console and into
      more of the places where the work of managing infrastructure happens.
    cards:
      - variant: image-right
        image: /images/releases/may-2026/release-neo-cli.svg
        image_alt: Neo running inside a terminal
        icon: terminal-window
        title: Neo in the CLI
        description: |
          The new `pulumi neo` command brings Neo out of Pulumi Cloud and into your terminal, so you can do
          agentic infrastructure anywhere you can run Pulumi.
        link: /blog/pulumi-neo-cli/

      - variant: image-top
        image: /images/releases/may-2026/release-neo-github-slack.svg
        image_alt: Neo integrated with GitHub and Slack
        icon: chats
        title: Neo GitHub and Slack apps
        description: |
          Now you can @-mention Neo in GitHub issues and pull requests, and in your team's Slack workspace, to
          kick off full-context infra tasks wherever you are.
        link: /blog/neo-github-slack/

      - variant: text
        icon: plugs
        title: Neo integration catalog
        description: |
          A new integration catalog lets you configure connectors for a growing library of complementary
          services including Atlassian, Datadog, Honeycomb, Linear, PagerDuty, and Supabase.
        link: /blog/neo-integrations/

      - variant: text
        icon: calendar-check
        title: Scheduled tasks and read-only sessions
        description: |
          Use Neo to automate recurring infrastructure tasks like keeping providers updated, identifying
          non-compliant resources, and summarizing infrastructure changes from week to week.
        link: /blog/neo-automations/

  - anchor: ai-frontier
    label: Partnering with the frontier of AI infrastructure
    heading: Partnering with the frontier of AI infrastructure
    description: |
      Working closely with companies building the frontier of AI infrastructure, we're releasing two new
      partner providers in close collaboration with the teams behind them.
    cards:
      - variant: text
        icon: cpu
        title: CoreWeave provider
        description: |
          This new provider brings the full power of the CoreWeave platform, the leader in GPU infrastructure,
          to help teams provision AI workloads. Includes support for all CoreWeave services, including
          CoreWeave Kubernetes Service (CKS).
        link: /registry/packages/coreweave/

      - variant: text
        icon: circuitry
        title: NVIDIA AI Cluster Runtime (AICR) provider
        description: |
          This new provider delivers fully functional NVIDIA software stacks atop the underlying cloud
          provider's GPU infrastructure. Includes out-of-the-box components like NVIDIA GPU Operator,
          Kubeflow, NIM Operator, and dozens more.
        link: https://github.com/pulumi-labs/pulumi-nvidia-aicr

  - anchor: agentic-intelligence
    label: Educating and measuring agentic infra intelligence
    heading: Educating and measuring agentic infra intelligence
    cards:
      - variant: text
        icon: book-open
        title: Agent-friendly docs
        description: |
          We now serve all of our documentation, including the complete Pulumi Registry, in easily consumable,
          agent-friendly Markdown.
        link: /blog/better-cli-interactions-for-agents-and-humans/#agent-friendly-markdown-docs-for-providers-and-components

      - variant: image-top
        image: /images/releases/may-2026/release-new-skills.svg
        image_alt: Stacked cards representing the new Neo skills
        icon: head-circuit
        title: New agent skills
        description: |
          We've reviewed and refreshed all of our existing agent skills, and added a new über-skill designed
          to help agents decide how best to use Pulumi in different scenarios. It's handy for humans too.
        link: /docs/ai/skills/

      - variant: text
        icon: brackets-curly
        title: Agent-friendly CLI ergonomics
        description: |
          We've made command names, help text, examples, output formats, and exit codes more consistent across
          the board to help agents navigate and use Pulumi even more efficiently.
        link: /blog/better-cli-interactions-for-agents-and-humans/

      - variant: image-left
        image: /images/releases/may-2026/release-infra-bench.svg
        image_alt: Stylized bar chart representing the InfraBench evaluation
        icon: chart-line
        title: InfraBench
        description: |
          A new benchmark for measuring how well agents perform on a wide array of representative
          infrastructure tasks — like the infrastructure equivalent of SWE-bench.

blog_section:
  title: From the blog
  posts:
    - /blog/the-agentic-infrastructure-era
    - /blog/better-cli-interactions-for-agents-and-humans
    - /blog/10-more-things-you-can-do-with-neo
    - /blog/pulumi-neo-cli
    - /blog/neo-integrations
    - /blog/neo-github-slack
    - /blog/neo-automations
    - /blog/pulumi-do-direct-resource-operations
---
