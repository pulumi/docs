---
# Name of the event, <= 60 characters (allow_long_title keeps the full title).
title: "Pulumi ESC, part 2: Short-lived credentials, rotation, and approvals"
allow_long_title: true
meta_desc: Part 2 of a two-part Pulumi ESC series. Vend short-lived cloud credentials, rotate secrets, and put approvals on the environments that matter.
meta_image: /events/pulumi-esc-part-2-credentials-rotation-approvals/meta.png
meta_image_square: /events/pulumi-esc-part-2-credentials-rotation-approvals/meta-square.png

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
sortable_date: 2027-02-02T09:00:00.000-08:00

# Duration of the event.
duration: 60 minutes

# "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
location: virtual

# Description of the event.
description: |
    A leaked credential usually means a long week: find every repo, pipeline, and laptop that holds a copy, change each one, and hope you didn't miss any. When credentials are issued from one place, that week becomes one change.

    In part 2 of our Pulumi ESC series, we go past storing secrets and into handing them out. We'll set up environments that vend short-lived cloud credentials on demand, rotate the secrets that can't be short-lived, and put approvals in front of changes to the environments that matter. Part 1 is useful background, but you can follow along if you already know ESC basics.

# The right hand side bullet points.
learn:
    - How ESC issues short-lived credentials through OIDC, so nothing long-lived sits in CI or on laptops
    - How to rotate secrets on a schedule, and what a rotation looks like to the systems using them
    - How approvals and functions keep one central source of truth that teams can still change safely

# The event presenters
presenters:
    - name: Elisabeth Lichtie
      role: Customer Success Architect, Pulumi
      photo: /images/team/elisabeth-lichtie.jpg

tags:
    level: Intermediate # Beginner, Intermediate, Advanced
    topics: ["Pulumi ESC", "Secrets Management"]
    languages: []
    clouds: []

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id:
    salesforce_campaign_id:
---
