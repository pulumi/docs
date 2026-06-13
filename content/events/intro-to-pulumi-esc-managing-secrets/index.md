---
# Name of the event, <= 60 characters
title: Best Practices for Managing Secrets - An Introduction to ESC

meta_desc: Learn to tame secrets sprawl with Pulumi ESC — aggregate, manage, and securely access secrets and configuration from one place.
meta_image: /events/intro-to-pulumi-esc-managing-secrets/managing-secrets-esc-elisabeth.png

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
url_slug: intro-to-pulumi-esc-managing-secrets

# The event type (workshop, webinar, talk).
event_type: webinar

# URL for embedding a URL for ungated events.
youtube_url:

# Sortable date. The datetime Hugo will use to sort the events in date order.
sortable_date: 2026-08-05T09:00:00.000-07:00

# Duration of the event.
duration: 60 minutes

# "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
location: virtual

# Description of the event.
description: |
    Most teams end up with secrets scattered everywhere: environment variables, CI systems, cloud secret stores, `.env` files on someone's laptop. That sprawl is hard to audit, harder to rotate, and a security incident waiting to happen.

    This introductory session is about Pulumi ESC (Environments, Secrets, and Configuration), a configuration-as-code product that pulls secrets and configuration from many sources into hierarchical environments, so you can consume them safely across your infrastructure and dev workflows. No prior ESC experience needed. We start from the basics and build up. Bring your questions, we'll leave plenty of time for live Q&A.
learn:
    - What Pulumi ESC is, and how environments organize secrets and configuration
    - How to pull secrets from sources like AWS Secrets Manager, 1Password, and others into one consistent place
    - How to consume those secrets safely at runtime, in your IaC, CI/CD, and local dev

# The event presenters
presenters:
    - name: Elisabeth Lichtie
      role: Customer Success Architect, Pulumi
      photo: /images/team/elisabeth-lichtie.jpg
    - name: Adam Gordon Bell
      role: Community Engineer, Pulumi
      photo: /images/team/adam-gordon-bell.jpg

# case-sensitive
tags:
    level: Beginner # Beginner, Intermediate, Advanced
    topics: ["Pulumi ESC", "Secrets Management", "Security"]
    languages: []
    clouds: []

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: ccf592e3-c1da-4ba4-8639-0f42fb88e61d
    salesforce_campaign_id: 701PQ00000w5nqkYAA

---
