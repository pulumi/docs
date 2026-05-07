---
# Name of the event, <= 60 characters
title: Getting started with DevOps AI Skills
meta_desc: Set up coding agents with the right hooks, LSP, and Pulumi skills so they produce clean Pulumi code.
meta_image:

# A featured event will display first in the list.
featured: false

# Events with unlisted as true will not be shown on the event list
unlisted: false

# Gated events will have a registration form and the user will need
# to fill out the form before viewing.
gated: true

# External events will link to an external page instead of an event
# landing/registration page. If the event is external you will need
# set the 'block_external_search_index' flag to true so Google does not index
# the event page created.
external: false
block_external_search_index: false

# The url slug for the event landing page. If this is an external
# event, use the external URL as the value here.
url_slug: getting-started-with-devops-ai-skills

# The event type (workshop, webinar, talk).
event_type: workshop

# URL for embedding a URL for ungated events.
youtube_url:

# Sortable date. The datetime Hugo will use to sort the events in date order.
sortable_date: 2026-07-02T09:00:00.000-07:00

# Duration of the event.
duration: 60 minutes

# "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
location: virtual

# Description of the event.
description: |
    Coding agents like Claude Code and opencode can write Pulumi for you, but the quality depends almost entirely on how you've configured them. In this workshop we set up both agents from scratch: settings, LSP integration, hooks, and the official Pulumi skills plus a few auxiliary ones, so by the end you have a rig that consistently produces idiomatic Pulumi code instead of plausible-looking guesses.

    From there we go straight into a live use case, putting the rig to work on a real Pulumi task so you can see the difference between a stock agent and a properly tuned one.

learn:
    - How to configure Claude Code and opencode with settings, LSP, and hooks tuned for Pulumi work.
    - How to install the official Pulumi skills and the auxiliary skills that fill in the gaps.
    - How to run a real task through the rig and see where it keeps the agent honest vs. where it still drifts.

# The event presenters
presenters:
    - name: Engin Diri
      role: Senior Solutions Architect, Pulumi
      photo: /images/team/engin-diri.jpg

# case-sensitive
tags:
    level: Intermediate # Beginner, Intermediate, Advanced
    topics: ["AI", "DevOps", "Developer Productivity"]
    languages: ["TypeScript", "Python"]
    clouds: []

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 10627c10-9d63-4437-8573-da3f28ad0698
    salesforce_campaign_id: 701PQ00000uMIkPYAW

---
