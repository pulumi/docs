---
# Name of the event, <= 60 characters
title: Autonomous Agents Need Guardrails with OpenClaw
meta_desc: A live panel on the security and infrastructure guardrails autonomous agents need before they touch production cloud.

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
    Autonomous agents are already taking real actions on real cloud infrastructure — provisioning clusters, applying configs, repairing drift. The pattern is familiar: a memory file, a heartbeat check, a loop that runs until the system "looks right." But nobody has agreed on what guardrails belong around that loop, who owns blast radius, or what the verifiable-state layer should look like — and that gap is where outages and security incidents live.

    In this 60-minute panel, Adam Gordon Bell (Pulumi) sits down with Dor Serero and Roey Zalta (Microsoft) to work through what breaks when agents touch production infrastructure and the security and infrastructure-as-code patterns that keep them productive instead of dangerous. Live with audience Q&A.
learn:
    - How autonomous agents go wrong when they touch infrastructure — real failure modes and war stories from OpenClaw
    - The guardrail stack — agent identity and policy gates, verifiable state, heartbeat and convergence checks, reversibility, and human-in-the-loop checkpoints
    - How the security (Microsoft) and infrastructure-as-code (Pulumi) lenses combine when agents and platforms read and write the same verifiable artifact

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
