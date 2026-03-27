---
# Name of the event, <= 60 characters
title: "Self-Service & AI Agents for Developer Productivity"
meta_desc:  Learn how to build self-service developer platforms using Pulumi's AI agent, templates, and automation for Kubernetes and DigitalOcean deployments.
meta_image:

# A featured event will display first in the list.
featured: false

# Events with unlisted as true will not be shown on the event list
unlisted: false

# Gated events will have a registration form and the user will need
# to fill out the form before viewing.
gated: false

# External events will link to an external page instead of an event
# landing/registration page. If the event is external you will need
# set the 'block_external_search_index' flag to true so Google does not index
# the event page created.
external: false
block_external_search_index: false

# The url slug for the event landing page. If this is an external
# event, use the external URL as the value here.
url_slug: self-service-enabling-developer-productivity

# The event type (workshop, webinar, talk).
event_type: workshop

# URL for embedding a URL for ungated events.
youtube_url: https://www.youtube.com/embed/gK1N88I0GQ8?si=T17pPuYgupJUL2ON

# Sortable date. The datetime Hugo will use to sort the events in date order.
sortable_date: 2025-11-06T12:00:00-05:00

# Duration of the event.
duration: 60 minutes

# "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
location: virtual

# Description of the event.
description: |
    This hands-on workshop with Pulumi Cloud shows how AI agents and self-service platforms help teams automate infrastructure creation and standardize deployments.

    You’ll work with Pulumi Neo, our AI agent for infrastructure and platform engineering, to build a self-service developer platform using templates, guided deployments, and reusable infrastructure patterns. Throughout the session, you’ll create templates, deploy real workloads, and build Kubernetes components, seeing how intelligent agents simplify provisioning, configuration, and GitOps workflows while preserving governance and consistency.
    
learn:
    - How to build and publish Pulumi templates that power self-service infrastructure provisioning
    - How to deploy a monitored DigitalOcean cluster through an AI-assisted, wizard-style workflow
    - How to create reusable Kubernetes components, like Argo CD, with Pulumi TypeScript and ESC environments
    - How intelligent agents enforce best practices and scale developer autonomy safely

# The event presenters
presenters:
    - name: Engin Diri
      role: Senior Solutions Architect, Pulumi
      photo: /images/team/engin-diri.jpg
    - name: Adam Bell
      role: Community Engineer, Pulumi
      photo: /images/team/adam-gordon-bell.jpg

# case-sensitive
tags:
    level: Beginner # Beginner, Intermediate, Advanced
    topics:  ["Platform Engineering", "Argo CD", "Kubernetes", "Pulumi Neo", "AI"]
    languages: []
    clouds: ["AWS", "DigitalOcean"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 01bea8e9-71fa-430d-953f-2077d3958d15
    salesforce_campaign_id: 701PQ00000edwmiYAA

---
