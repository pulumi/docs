---
# Name of the event, <= 60 characters
title: "Neo in a Docker Sandbox: Using Pulumi’s Coding Agent for All Things Infra Safely and Securely"
allow_long_title: true
meta_desc: Join Docker and Pulumi to run Neo, Pulumi’s infrastructure coding agent, inside a Docker Sandbox and turn plain-English requests into real cloud infrastructure.
meta_image: /events/neo-in-a-docker-sandbox-eu/meta.png
meta_image_square: /events/neo-in-a-docker-sandbox-eu/meta-square.png

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
url_slug: neo-in-a-docker-sandbox-eu

# The event type (workshop, webinar, talk).
event_type: workshop

# URL for embedding a URL for ungated events.
youtube_url:

# Sortable date. The datetime Hugo will use to sort the events in date order.
sortable_date: 2026-09-17T10:00:00.000+02:00

# Duration of the event.
duration: 60 minutes

# "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
location: virtual

# Description of the event.
description: |
    Coding agents changed how software gets written, but almost nobody lets one near their infrastructure. The reason is simple: an agent that breaks your laptop is annoying, while an agent that breaks production comes with a postmortem. This joint session from Docker and Pulumi is about letting the agent in anyway, safely.

    Pulumi Neo is a coding agent for all things infra. It sits in your terminal like any other agent; the difference is that the code it writes runs your cloud. You’ll put Neo in a Docker Sandbox, so whatever it installs or breaks stays inside its own sealed workspace. In the workshop, you’ll watch a plain-English request turn into running infrastructure in a real cloud account.

learn:
    - What changes when a coding agent’s target is your cloud instead of your codebase.
    - What’s inside a Docker Sandbox, and how to set up the perfect one for your projects.
    - How Docker Sandboxes give Neo a sealed workspace where it can work without supervision.
    - How Pulumi ESC replaces static API keys with short-lived credentials for AWS, Azure, or Google Cloud.

# The event presenters
presenters:
    - name: Engin Diri
      role: Principal Solutions Architect, Pulumi
      photo: /images/team/engin-diri.jpg
    - name: Adam Gordon Bell
      role: Community Engineer, Pulumi
      photo: /images/team/adam-gordon-bell.jpg
    - name: Mike Coleman
      role: Staff Solutions Architect, Docker
      photo: /images/team/mike-coleman.jpg

# case-sensitive
tags:
    level: Beginner # Beginner, Intermediate, Advanced
    topics: ["AI", "Docker", "DevOps"]
    languages: []
    clouds: []

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id:
    salesforce_campaign_id:

---
