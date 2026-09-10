---
# Name of the event, <= 60 characters
title: "Extending Pulumi Neo: MCP Servers and Cloud CLIs"

meta_image: /events/extending-pulumi-neo-mcp-cloud-cli/meta.png
meta_image_square: /events/extending-pulumi-neo-mcp-cloud-cli/meta-square.png

meta_desc: Connect Pulumi Neo to Datadog, PagerDuty, Linear, and more via MCP, and to aws, gcloud, az, and kubectl — live workshop with real incident workflows.

# A featured event will display first in the list.
featured: false

# Events with unlisted as true will not be shown on the event list
unlisted: false

# Gated events will have a registration form and the user will need
# to fill out the form before viewing.
gated: true

# External events will link to an external page instead of an event
# landing/registration page.
external: false
block_external_search_index: false

# The url slug for the event landing page.
url_slug: extending-pulumi-neo-mcp-cloud-cli

# The event type (workshop, webinar, talk).
event_type: workshop

# URL for embedding a URL for ungated events.
youtube_url:

# Sortable date. The datetime Hugo will use to sort the events in date order.
# With sessions below, this is the earliest session's date.
sortable_date: 2026-09-08T09:00:00.000-07:00

# Duration of the event.
duration: 60 minutes

# The event runs twice, once per region. Each session gets its own tab on this
# page, its own card in the event list, and its own registration form.
sessions:
    - label: Americas
      sortable_date: 2026-09-08T09:00:00.000-07:00
      duration: 60 minutes
      form:
          riverside_event_id: 6a970364f31158d839105b35
          salesforce_campaign_id: 701PQ00000zDNF3YAO
      presenters:
          - name: Adam Gordon Bell
            role: Community Engineer, Pulumi
            photo: /images/team/adam-gordon-bell.jpg
    - label: EMEA
      sortable_date: 2026-09-30T10:00:00.000+02:00
      duration: 60 minutes
      form:
          hubspot_form_id: b67462e0-5973-4d0f-ad0a-a401a83cbcc1
          salesforce_campaign_id: 701PQ00000zDXj2YAG
      presenters:
          - name: Engin Diri
            role: Principal Solutions Architect, Pulumi
            photo: /images/team/engin-diri.jpg

# "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
location: virtual

# Description of the event.
description: |
    Infrastructure work lives between browser tabs: PagerDuty in one, Datadog in another, the AWS console in a third, your Pulumi state somewhere else entirely. Pulumi Neo already understands your infrastructure — your code, your stacks, your state. Its newest integrations extend that reach in two directions: into the third-party systems your team uses to plan and observe, and out to the cloud CLIs that actually drive your infrastructure.

    In this live workshop, we'll put the integrations to work on the problems they were built for: an alert that needs triage, a metric history that explains it, live cloud state that doesn't match what the code says, and a fix that should ship as a reviewed pull request rather than a console click. You'll see how Neo pulls context from the tools your team already uses — MCP integrations for Atlassian, Datadog, Honeycomb, Linear, PagerDuty, and Supabase — and reaches live cloud state through scoped CLI integrations for aws, gcloud, az, and kubectl, with each one configured, scoped, and controlled per task.

    We'll close with the newest additions to the integrations story: CLI integrations inside scheduled Neo Automations, so your recurring checks can reach live cloud state without a human in the loop, and Neo in your editor — Zed, JetBrains, VS Code, or Cursor — where it inherits the CLIs you're already authenticated to.
learn:
    - How MCP integrations bring tickets, traces, incidents, and runbooks into a Neo task.
    - How CLI integrations give Neo scoped, named access to live cloud state — staging without touching production.
    - How Pulumi ESC backs each CLI integration with credentials your org owns, instead of static API keys.
    - How per-task toggles and org-level settings keep the agent's reach under your control.
    - "What's new since launch — CLI integrations in scheduled Automations, and Neo in your editor via the Agent Client Protocol."

# No top-level presenters: each session above names its own lineup, and anything
# that needs "everyone at this event" derives the union from them.

# case-sensitive
tags:
    level: Intermediate # Beginner, Intermediate, Advanced
    topics: ["Pulumi Neo", "AI", "DevOps"]
    languages: []
    clouds: []
---
