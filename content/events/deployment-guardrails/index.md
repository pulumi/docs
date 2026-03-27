---
# Name of the event, <= 60 characters
title: "Deployment Guardrails with Policy as Code"
meta_desc: Implement automated governance through policy as code that enables self-service while maintaining security and compliance.
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
url_slug: deployment-guardrails

# The event type (workshop, webinar, talk).
event_type: workshop

# URL for embedding a URL for ungated events.
youtube_url: 

# Sortable date. The datetime Hugo will use to sort the events in date order.
sortable_date: 2025-08-13T12:00:00-04:00

# Duration of the event.
duration: 60 minutes

# "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
location: virtual

# Description of the event.
description: |
    Effective Internal Developer Platforms provide guardrails, not gates—enabling developer autonomy while automatically enforcing security, compliance, and operational standards. This workshop demonstrates how to implement comprehensive policy as code using Pulumi Policies. You'll learn to create policies that prevent misconfigurations, enforce tagging standards, and ensure compliance requirements are met automatically, turning your IDP into a secure-by-default platform.
learn:
    - How to implement security and compliance policies that run automatically in CI/CD
    - Strategies for creating policies that guide rather than block developer productivity
    - Real-world policy examples for common governance requirements (tagging, security groups, encryption)

# The event presenters
presenters:
    - name: Adam Bell
      role: Community Engineer, Pulumi
      photo: /images/team/adam-gordon-bell.jpg
    - name: Josh Kodroff
      role: Principal Solutions Architect, Pulumi
      photo: /images/team/josh-kodroff.jpg

# case-sensitive
tags:
    level: Intermediate # Beginner, Intermediate, Advanced
    topics:  ["Security", "Policy as Code", "Governance"]
    languages: ["TypeScript"]
    clouds: ["AWS"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 541113c9-3795-4537-ab07-5485e85362a3
    salesforce_campaign_id: 701PQ00000ZYMhuYAH

--- 