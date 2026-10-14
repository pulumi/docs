---
# Event title, <= 60 characters.
title: "Who Spent All the Tokens? Per-Team AI Cost Control as Code"

meta_image: /events/per-team-ai-cost-control/meta.png
meta_image_square: /events/per-team-ai-cost-control/meta-square.png

meta_desc: Track Amazon Bedrock token spend per team with Pulumi: tagged inference profiles, token metrics, policy guardrails, alarms, and budgets, all as code.

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
    One agent task can fire off hundreds of model calls. When several teams share one Amazon Bedrock account, the bill shows up as one line item, and nobody can tell you which team burned the tokens, let alone rein it in.

    In this live workshop, we'll build per-team AI cost control as code with Pulumi. Each team gets its own Bedrock application inference profile, tagged with a team and a cost center, and an IAM role that can call only that profile. Bedrock invocation logging feeds CloudWatch, where metric filters turn every request into per-team input and output token counts. Pulumi Policies block untagged profiles and wildcard invoke grants before they deploy. When one team's output tokens spike, a CloudWatch alarm fires. Credentials come from Pulumi ESC over OIDC, so there are no static access keys.

    Adding a team is one line of config. The code is open source, so you can clone it after the session and run it in your own AWS account.
learn:
    - How to give each team its own Amazon Bedrock inference profile and an IAM role that can invoke only that profile.
    - How to turn Bedrock invocation logs into per-team token metrics with CloudWatch metric filters.
    - How Pulumi Policies block untagged profiles and wildcard invoke permissions before they deploy.
    - How to alert on token spikes with a CloudWatch alarm and track spend per team with AWS Budgets.
    - How Pulumi ESC supplies short-lived AWS credentials over OIDC instead of static access keys.

# Speakers.
presenters:
    - name: Adam Gordon Bell
      role: Community Engineer, Pulumi
      photo: /images/team/adam-gordon-bell.jpg

# Used for filtering on the event list page.
tags:
    level: Intermediate # Beginner | Intermediate | Advanced
    topics: ["AI", "Policy as Code", "Pulumi ESC"]
    languages: ["TypeScript"]
    clouds: ["AWS"]

# Registration form (only rendered when gated: true).
# TODO: HubSpot form ID and Salesforce campaign ID pending.
form:
    hubspot_form_id: ""
    salesforce_campaign_id: ""
---
