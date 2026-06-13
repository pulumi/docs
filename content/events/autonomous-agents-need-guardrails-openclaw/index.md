---
# Name of the event, <= 60 characters
title: "OpenClaw Needs Guardrails: Securing Agentic Infrastructure"
meta_desc: A live panel on securing OpenClaw and autonomous agents before they touch production cloud — the guardrails, identity, and verifiable state they need.
meta_image: /events/autonomous-agents-need-guardrails-openclaw/openclaw-agents-guardrails.png

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
url_slug: autonomous-agents-need-guardrails-openclaw

# The event type (workshop, webinar, talk).
event_type: webinar

# URL for embedding a URL for ungated events.
youtube_url:

# Sortable date. The datetime Hugo will use to sort the events in date order.
sortable_date: 2026-07-14T11:00:00.000-04:00

# Duration of the event.
duration: 60 minutes

# "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
location: virtual

# Description of the event.
description: |
    Autonomous agents are already taking real actions on real cloud infrastructure: provisioning clusters, repairing drift. The pattern is familiar: a memory file, a heartbeat check, a cycle that keeps going until the system "looks right." Nobody's quite agreed on what guardrails belong around that loop, who owns blast radius, or what the verifiable-state layer should look like.

    In this 60-minute panel, Dor Serero (Principal Architect) and Roey Zalta (Data & AI Solutions Engineer) from Microsoft sit down with Adam Gordon Bell and Engin Diri from Pulumi. Live with audience Q&A. Bring your hardest questions about letting agents into production.
learn:
    - What goes wrong when agents touch infrastructure: war stories from OpenClaw, autonomous-paper-clipping moments, real outages
    - The guardrail stack: memory files, heartbeat checks, policy gates, blast-radius bounds, and IaC as the verifiable layer agents read and write
    - What Microsoft sees on the security side: agent identity, audit, governance
    - What Pulumi sees on the IaC side: how agents and platforms share the same artifact
    - What engineering leaders should do this quarter

# The event presenters
presenters:
    - name: Adam Gordon Bell
      role: Community Engineer, Pulumi
      photo: /images/team/adam-gordon-bell.jpg
    - name: Engin Diri
      role: Senior Solutions Architect, Pulumi
      photo: /images/team/engin-diri.jpg
    - name: Dor Serero
      role: Principal Architect, Microsoft
    - name: Roey Zalta
      role: Data & AI Solutions Engineer, Microsoft

# case-sensitive
tags:
    level: Intermediate # Beginner, Intermediate, Advanced
    topics: ["AI", "Security"]
    languages: []
    clouds: []

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: d0c8fa60-4dbc-4cc9-a8f3-1d32b836e8be
    salesforce_campaign_id: 701PQ00000w5qz6YAA

---
