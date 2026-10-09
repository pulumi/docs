---
# Event title, <= 60 characters.
title: "Give your coding agent an (Elastic) memory"
meta_desc: "Give your coding agent persistent, searchable memory in Elasticsearch, deployed to Elastic Cloud with one Pulumi command."

# Social cards rendered by /event-meta-image (Pulumi + Elastic logos).
meta_image: /events/give-your-coding-agent-an-elastic-memory/meta.png
meta_image_square: /events/give-your-coding-agent-an-elastic-memory/meta-square.png

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
sortable_date: 2026-10-22T09:00:00.000-07:00

# Human-readable duration.
duration: 60 minutes

# "virtual" or a city/state (e.g., "Seattle, WA").
location: virtual

# Markdown description.
description: |
    If you work with a coding agent every day, you know the routine. Each new session starts blank: the agent re-reads files it read yesterday, asks about decisions you settled last week, and redoes debugging you already finished. Its only memory is the context window, and that empties every time you close your laptop.

    Claude Code ships a built-in fix: markdown notes the agent writes for itself and reads back at the next session start. It helps, but the notes live on one machine, there is no real search, and anything past the first page of the index gets dropped.

    In this hands-on workshop, we'll take that idea further with agent-memory, an open source project that keeps decisions, tasks, and session history in Elasticsearch, so they're searchable and shared across machines. You'll stand up the whole memory backend on Elastic Cloud with one Pulumi command, wire it into your coding agent, then kill the agent mid-task and see how much a fresh one remembers when its memory is a search engine instead of a text file.

    You'll leave with a repo you can review and share, so every teammate gets an identical memory backend instead of their own snowflake. No promises about becoming a 1000x AI engineer, but your agent will stop asking you the same question twice.

# What attendees will learn (rendered as a checklist).
learn:
    - Why built-in markdown memory breaks down across sessions, machines, and teams.
    - How agent-memory stores and searches agent context in Elasticsearch.
    - How to deploy the memory backend to Elastic Cloud with Pulumi as reviewable code.
    - How to plug it into your coding agent and recover a killed session.

# Speakers.
presenters:
    - name: Engin Diri
      role: Principal Solutions Architect, Pulumi
      photo: /images/team/engin-diri.jpg

# Used for filtering on the event list page.
tags:
    level: Intermediate # Beginner | Intermediate | Advanced
    topics: ["AI"]
    languages: ["HCL"]
    clouds: []

# Registration form (only rendered when gated: true).
form:
    # TODO: wire in from MA-1045 (https://linear.app/pulumi/issue/MA-1045) once marketing creates the form and campaign.
    hubspot_form_id: ""
    salesforce_campaign_id: ""
---
