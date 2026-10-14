---
# Event title, <= 60 characters.
title: "Who Spent All the Tokens? Per-Team AI Cost Control as Code"

meta_image: /events/per-team-ai-cost-control/meta.png
meta_image_square: /events/per-team-ai-cost-control/meta-square.png

meta_desc: See which team is spending your Amazon Bedrock tokens, and put guardrails around it, with Pulumi infrastructure as code.

# A featured event displays first in the list.
featured: false

# Hide from the event list.
unlisted: false

# Show a registration form. Requires form.hubspot_form_id.
gated: true

# The event type (workshop, webinar, talk).
event_type: workshop

# YouTube embed URL. When set, the event appears in "On-demand recordings".
# When empty, it appears in "Upcoming events".
youtube_url:

# ISO 8601 datetime used for sorting and display.
sortable_date: 2026-11-04T09:00:00.000-08:00

# Human-readable duration.
duration: 60 minutes

# "virtual" or a city/state (e.g., "Seattle, WA").
location: virtual

# Markdown description.
description: |
    One agent task can fire off hundreds of model calls. When several teams share one Amazon Bedrock account and nothing is set up to split usage, the bill shows up as one line item, and it's hard to tell which team burned the tokens.

    In this live workshop, we'll build per-team AI cost tracking on Amazon Bedrock as code with Pulumi. Each team gets its own inference profile and a role scoped to it, so usage can be measured team by team. We'll turn Bedrock's logs into per-team token counts and use Pulumi Policies to catch mistakes before they deploy.

    The code is open source, so you can take it home and run it in your own AWS account.
learn:
    - How to give each team its own Amazon Bedrock inference profile with access scoped to it.
    - How to measure token usage per team from Bedrock's logs.
    - How Pulumi Policies catch cost and access mistakes before they deploy.

# Speakers.
presenters:
    - name: Adam Gordon Bell
      role: Community Engineer, Pulumi
      photo: /images/team/adam-gordon-bell.jpg
    - name: Engin Diri
      role: Principal Solutions Architect, Pulumi
      photo: /images/team/engin-diri.jpg

# Used for filtering on the event list page.
tags:
    level: Intermediate # Beginner | Intermediate | Advanced
    topics: ["AI", "Policy as Code"]
    languages: ["TypeScript"]
    clouds: ["AWS"]

# Registration form (only rendered when gated: true).
# TODO: HubSpot form ID and Salesforce campaign ID pending.
form:
    hubspot_form_id: ""
    salesforce_campaign_id: ""
---
