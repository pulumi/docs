---
# Name of the event, <= 60 characters
title: "Extending Pulumi Neo: MCP Servers and Cloud CLIs (EU)"

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
url_slug: extending-pulumi-neo-mcp-cloud-cli-eu

# The event type (workshop, webinar, talk).
event_type: workshop

# URL for embedding a URL for ungated events.
youtube_url:

# Sortable date. The datetime Hugo will use to sort the events in date order.
sortable_date: 2026-09-30T10:00:00.000+02:00

# Duration of the event.
duration: 60 minutes

# "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
location: virtual

# Description of the event.
description: |
    Infrastructure work lives between browser tabs: PagerDuty in one, Datadog in another, the AWS console in a third, your Pulumi state somewhere else entirely. Pulumi Neo already understands your infrastructure — your code, your stacks, your state. Its newest integrations extend that reach in two directions: into the third-party systems your team uses to plan and observe, and out to the cloud CLIs that actually drive your infrastructure.

    In this live workshop, Engin works a realistic incident end to end inside a single Neo conversation: an alert fires, Neo pulls the incident from PagerDuty, checks the metrics history, queries live cloud state through a scoped CLI integration, and opens a reviewed pull request with the fix. Along the way you'll see how MCP integrations (Atlassian, Datadog, Honeycomb, Linear, PagerDuty, Supabase) and CLI integrations (aws, gcloud, az, kubectl) are configured, scoped, and controlled per task.
learn:
    - How MCP integrations bring tickets, traces, incidents, and runbooks into a Neo task.
    - How CLI integrations give Neo scoped, named access to live cloud state — staging without touching production.
    - How Pulumi ESC backs each CLI integration with credentials your org owns, instead of static API keys.
    - How per-task toggles and org-level settings keep the agent's reach under your control.

# The event presenters
presenters:
    - name: Engin Diri
      role: Principal Solutions Architect, Pulumi
      photo: /images/team/engin-diri.jpg

# case-sensitive
tags:
    level: Intermediate # Beginner, Intermediate, Advanced
    topics: ["Pulumi Neo", "AI", "DevOps"]
    languages: []
    clouds: []

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id:
    salesforce_campaign_id:
---
