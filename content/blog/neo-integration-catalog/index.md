---
title: "Neo's Integration Catalog: Give Your Agent Access to the Tools It Needs"
allow_long_title: true
date: 2026-04-24
draft: false
meta_desc: "Connect Neo to Atlassian, Datadog, Honeycomb, Linear, PagerDuty, and Supabase so your infrastructure agent has the context it needs to help."
meta_image: meta.png
feature_image: feature.png
authors:
    - neo-team
tags:
    - ai
    - ai-agents
    - features
    - pulumi-neo

social:
    twitter: |
        A latency spike shows up in Datadog. You pull up Honeycomb, copy findings into Linear, then check what Pulumi changed. Four tools before you have an answer.

        Neo can now do all of that from one task. Here's what the Integration Catalog looks like.
    linkedin: |
        A latency spike shows up in Datadog. You open four tabs: Honeycomb for traces, Linear to file a ticket, PagerDuty to check on-call, Pulumi to see what changed. That's most of the job before you've even diagnosed anything.

        We kept asking whether an agent could handle that whole sequence as a single task. The tricky part wasn't the API connections — it was figuring out the access model for a whole engineering team.

        Here's what we built and what the first batch of integrations looks like.
    bluesky: |
        A latency spike shows up in Datadog. Traces in Honeycomb, tickets in Linear, on-call in PagerDuty — four tabs before you can even diagnose anything.

        We spent a long time on whether one task could cover all of those. The hard part wasn't the APIs. Here's what we figured out.
---

Infrastructure work doesn't happen in one tool. Something pages. The signal sits in a metrics dashboard. The follow-up lives in a ticket, and the runbook is in a doc somewhere. Jumping between them is most of the job: copying context, pasting graphs into chat, re-typing the same summary for the ticket.

Today we're launching the **Integration Catalog** for [Pulumi Neo](/blog/pulumi-neo/): one place to connect Neo to the tools your team already uses, so your agent has the context it needs to help.

<!--more-->

## Six integrations in the launch catalog

Neo ships with six integrations at launch, each exposed to the agent through the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/):

- **Atlassian** — Jira issues, Confluence pages, project context
- **Datadog** — metrics, logs, monitors
- **Honeycomb** — traces and observability queries
- **Linear** — issue tracking and project workflows
- **PagerDuty** — incidents, on-call schedules, escalations
- **Supabase** — database management and edge functions

Each integration is a vendor-hosted MCP server. Neo calls the integration through a structured tool protocol and only sees the tools the vendor chooses to expose.

## Neo in action: one task, many systems

A latency spike showed up in Datadog yesterday afternoon, and you want to know whether your deploy caused it.

> **You:** Neo, our `payments` stack saw elevated p95 starting around 3pm yesterday. Did our deploy cause it? Check Datadog and Honeycomb.

Neo lines up the Pulumi update history for the `payments` stack against the latency and error-rate metrics in Datadog around the same window, then surfaces the top slow traces in Honeycomb to confirm the suspect change.

> **You:** Open a Linear ticket on the `platform` team with the findings and link the offending update.

Neo opens the Linear issue with the summary, the Pulumi update URL, and a pointer to the Datadog dashboard, all without you leaving the chat or copy-pasting context between tabs.

## How the Integration Catalog works

**Admins configure credentials once.** In your org's Neo settings, open the Integration Catalog, pick an integration, and paste in an API token or service-account key.

**Your team gets the capability immediately.** No per-user setup, no extra OAuth flow for each developer, no asking platform to share a token in 1Password.

**Neo uses integrations transparently.** When a task runs, the service decrypts the configured credentials and hands them to the agent runtime as MCP server auth. If an integration is misconfigured or its credentials have been rotated, Neo skips that integration and continues with the rest. The session doesn't fail.

## What's coming next: CLI, OAuth, and access controls

This is the first cut. Here's what we're working on:

- **CLI integrations** — `kubectl` first, then `aws`, `gcloud`, and `az`, for the long tail of tools that don't yet have an MCP server.
- **OAuth integrations** — for providers whose hosted MCP servers only speak OAuth (Notion, Sentry, Vercel), and for orgs that want per-user credentials.
- **Per-integration access controls** — team-scoped policies so admins can say "only the platform team can let Neo touch PagerDuty."

## Try it out

The Integration Catalog is available now for Neo-enabled organizations. Open your org's Neo settings, head to the Integrations tab, and connect the first tool you reach for when something breaks.

As always, we'd love to hear what's missing. File a feature request in [pulumi-cloud-requests](https://github.com/pulumi/pulumi-cloud-requests/issues/new/choose) with the integration you want next. We're prioritizing based on what teams actually use.

Happy building.
