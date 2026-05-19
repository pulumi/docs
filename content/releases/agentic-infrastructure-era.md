---
title: "Building for the agentic infrastructure era"
date: 2026-05-19
meta_desc: "The agentic infrastructure era is here. Pulumi is shipping the surfaces, integrations, and providers to run it in production."
meta_image: "/images/releases/may-2026/meta.png"

hero:
    overline: "May 2026 release"
    breadcrumb_label: "May 2026"
    heading: "Building for the agentic infrastructure era"
    description: "The agentic infrastructure era is here. We're shipping the surfaces, integrations, and providers to run it in production."
    feature_image_centered: "/images/releases/may-2026/release-hero-bottom-dark.svg"
    feature_image_split: "/images/releases/may-2026/release-hero-right-light.svg"
    feature_image_alt: "Agent surfaces — Claude Code, OpenCode, Codex, and Pulumi Neo — around the Pulumi mark"
    feature_image_max_width: 430

intro:
    quote: |
        "LLMs are now doing 20% of the infrastructure deployments, up from
        virtually zero a year ago. We expect this to grow to over 50% before
        the end of this year."
    attribution: |
        Joe Duffy on why infrastructure as code is the natural substrate for
        AI agents, and what Pulumi is shipping today to make agentic
        infrastructure real.
    link: "/blog/the-agentic-infrastructure-era/"

toc_heading: "What we're shipping"

sections:
    - anchor: meeting-agents
      label: "Meeting agents where they work"
      heading: "Meeting agents where they work"
      description: |
          Real code is the right substrate for agentic infrastructure, but
          agents want to start small and level up. We've designed the Pulumi
          CLI as a progression — from first command to full infrastructure
          as code, with no walls in between.
      cards:
          - variant: text
            icon: terminal-window
            title: "One-command execution"
            description: "A new NPM package enables `npx pulumi <anything>`-style commands so agents can run any Pulumi command anywhere."

          - variant: image-top
            image: "/images/releases/may-2026/release-pulumi-do.svg"
            image_alt: "pulumi do — extruded type illustration"
            icon: rows-plus-bottom
            title: "Imperative infrastructure operations"
            description: "The new `pulumi do` command enables direct create, read, update, delete, list, and API operations with a single command."

          - variant: text
            icon: user-circle-plus
            title: "Agent accounts"
            description: "Now agents can use free, ephemeral Pulumi Cloud accounts straight from Claude Code, Codex, OpenCode, Copilot, Cursor, and others."

          - variant: image-left
            image: "/images/releases/may-2026/release-cloud-cli.svg"
            image_alt: "Pulumi Cloud surfaces — stack, env, org, deployment — reachable from the CLI"
            icon: cloud-check
            title: "Pulumi Cloud in the CLI"
            description: "Over 30 new commands for Pulumi Cloud operations — you can think of this as the equivalent of the `gh` CLI, which agents really like."

    - anchor: neo-everywhere
      label: "Neo, everywhere you work"
      heading: "Neo, everywhere you work"
      description: |
          What comes after the CLI is asynchronous work and real autonomy.
          Neo, Pulumi's infrastructure agent, now ships with the surfaces,
          integrations, and cadences teams need to run agentic
          infrastructure in production.
      cards:
          - variant: image-right
            image: "/images/releases/may-2026/release-neo-cli.svg"
            image_alt: "Neo running inside a terminal"
            icon: terminal-window
            title: "Neo in the CLI"
            description: "The new `pulumi neo` command lets you run the same agent that is already in Pulumi Cloud, allowing you to do agentic infrastructure wherever you prefer."

          - variant: image-top
            image: "/images/releases/may-2026/release-neo-github-slack.svg"
            image_alt: "Neo integrated with GitHub and Slack"
            icon: chats
            title: "Neo GitHub and Slack apps"
            description: "Now you can @-mention Neo from GitHub pull requests, and/or straight from Slack, to kick off agentic infrastructure workflows wherever it is most convenient."

          - variant: text
            icon: plugs
            title: "Neo integration catalog"
            description: "A new integration catalog lets you configure connectors to other systems that bring valuable infrastructure management context, including Atlassian, Datadog, Honeycomb, Linear, PagerDuty, and Supabase."

          - variant: text
            icon: calendar-check
            title: "Scheduled tasks and readonly sessions"
            description: "Now you can automate recurring infrastructure tasks, including confining Neo to readonly operations for extra safety."

    - anchor: ai-frontier
      label: "Partnering with the frontier of AI infra"
      heading: "Partnering with the frontier of AI infrastructure"
      description: |
          We're investing in deep partnerships with the companies building
          the frontier of AI infrastructure, and are shipping two new
          partner providers in close collaboration with the teams behind
          them.
      cards:
          - variant: text
            icon: cpu
            title: "CoreWeave provider"
            description: "This new provider brings the full power of the CoreWeave platform, the leader in GPU infrastructure, to help teams provision AI workloads with ease. This includes support for all of the CoreWeave services including CoreWeave Kubernetes Service (CKS)."
            link: "/registry/packages/coreweave/"

          - variant: text
            icon: circuitry
            title: "NVIDIA AI Cluster Runtime (AICR) provider"
            description: "This new provider delivers fully functional NVIDIA software stacks atop the underlying cloud provider's GPU infrastructure. This packages out of the box components like NVIDIA GPU Operator, Kubeflow, NIM Operator, and dozens more otherwise tricky-to-configure cluster components."

    - anchor: agentic-intelligence
      label: "Educating and measuring agentic infra intelligence"
      heading: "Educating and measuring agentic infra intelligence"
      cards:
          - variant: text
            icon: book-open
            title: "Agent-friendly docs"
            description: "We now serve our docs website in markdown to agents and did a pass over our documentation and CLI text to ensure it's maximally useful to agents."

          - variant: image-top
            image: "/images/releases/may-2026/release-new-skills.svg"
            image_alt: "Stacked cards representing the new Neo skills"
            icon: head-circuit
            title: "New skills"
            description: "A refreshed set of skills, plus a new uber-skill that walks agents through the full progression — from agent accounts to `pulumi do` to full IaC to Neo and Pulumi Cloud governance. Handy for humans too."
            link: "/docs/ai/skills/"

          - variant: text
            icon: brackets-curly
            title: "Agent-friendly CLI ergonomics"
            description: "We have added `--json` and structured errors across the CLI to help agents parse and react to outputs appropriately."
            link: "/blog/better-cli-interactions-for-agents-and-humans/"

          - variant: image-left
            image: "/images/releases/may-2026/release-infra-bench.svg"
            image_alt: "Stylized bar chart representing the InfraBench evaluation"
            icon: chart-line
            title: "InfraBench"
            description: "A new benchmark for measuring how agents perform on representative infrastructure tasks — the infrastructure equivalent of SWE-bench. We're keeping the suite internal for now, but will publish our progress as we improve agent performance over time."

blog_section:
    title: "More from the blog"
    posts:
        - /blog/the-agentic-infrastructure-era
        - /blog/better-cli-interactions-for-agents-and-humans
        - /blog/10-more-things-you-can-do-with-neo
---
