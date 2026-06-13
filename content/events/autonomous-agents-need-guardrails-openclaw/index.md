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
    Roey Zalta gave OpenClaw its own Mac mini and let it run. Inside four days it had registered its own Apple ID, wired itself into his home cameras, and started counting his cats with GPT-4o vision — then wrote the LinkedIn post bragging about it. That's the fun half of autonomous agents.

    The other half: these things have shell access and can hit your cloud APIs on a loop, and the tech press spent early 2026 calling OpenClaw a security "dumpster fire." Dor Serero spends his days on that end — writing container-escape exploits and breaking Kubernetes boundaries — so when he says you can run one of these safely, it's worth hearing how.

    In this 60-minute panel, Dor and Roey from Microsoft join Adam Gordon Bell and Engin Diri from Pulumi to show what they actually run, where it bites, and the guardrails that keep an agent useful instead of dangerous. Roey brings the "it runs my life" demos; Dor brings the "here's how it gets you" teardown. Live with audience Q&A.
learn:
    - What people actually automate with OpenClaw — the useful, the weird, and the cat counter
    - The real failure modes when an agent has shell access and goals of its own
    - The guardrail stack: agent identity, isolation, policy gates, and IaC as the verifiable layer agents read and write
    - Where security (Microsoft) and infrastructure-as-code (Pulumi) meet on keeping agents in bounds

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
