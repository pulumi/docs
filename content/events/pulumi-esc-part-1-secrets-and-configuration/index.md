---
# Name of the event, <= 60 characters.
title: "Pulumi ESC, part 1: One place for secrets and configuration"
meta_desc: Part 1 of a two-part Pulumi ESC series. Start from zero and pull secrets and configuration from many sources into one place.
meta_image: /events/pulumi-esc-part-1-secrets-and-configuration/meta.png
meta_image_square: /events/pulumi-esc-part-1-secrets-and-configuration/meta-square.png

# A featured event will display first in the list.
featured: false

# Events with unlisted as true will not be shown on the event list
unlisted: false

# Gated events will have a registration form and the user will need
# to fill out the form before viewing.
gated: true

# The event type (workshop, webinar, talk).
event_type: workshop

# URL for embedding a URL for ungated events.
youtube_url:

# Sortable date. The datetime Hugo will use to sort the events in date order.
sortable_date: 2027-01-26T09:00:00.000-08:00

# Duration of the event.
duration: 60 minutes

# "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
location: virtual

# Description of the event.
description: |
    Most teams end up with secrets scattered everywhere: environment variables, CI systems, cloud secret stores, `.env` files on someone's laptop. Nobody can say where a given key lives, or what breaks when it changes.

    This is part 1 of a two-part series on Pulumi ESC (Environments, Secrets, and Configuration). We start from zero: what an environment is, how environments compose, and how to pull secrets and configuration from the places they already live into one consistent source. No prior ESC experience needed. Part 2, the following week, builds on this with short-lived credentials, rotation, and approvals.

# The right hand side bullet points.
learn:
    - What Pulumi ESC is, and how environments organize and inherit secrets and configuration
    - How to pull secrets from sources like AWS Secrets Manager and 1Password into one place
    - "How to use them at runtime: in your IaC, in CI/CD, and in local dev"

# The event presenters
presenters:
    - name: Elisabeth Lichtie
      role: Customer Success Architect, Pulumi
      photo: /images/team/elisabeth-lichtie.jpg

tags:
    level: Beginner # Beginner, Intermediate, Advanced
    topics: ["Pulumi ESC", "Secrets Management"]
    languages: []
    clouds: []

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id:
    salesforce_campaign_id:
---
