---
# Name of the event, <= 60 characters
title: "Automating Deployments with IaC & GitHub Actions"
meta_desc: Level up your Infrastructure as Code practices with secure, automated deployment pipelines and enterprise-grade security controls.

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
url_slug: automating-deployments-iac-github-actions

# The event type (workshop, webinar, talk).
event_type: workshop

# URL for embedding a URL for ungated events.
youtube_url: 

# Sortable date. The datetime Hugo will use to sort the events in date order.
sortable_date: 2025-02-05T09:00:00-08:00

# Duration of the event.
duration: 90 minutes

# "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
location: virtual

# Description of the event.
description: |
   For organizations already using Infrastructure as Code (IaC), the next crucial step is establishing reliable, secure deployment pipelines. This workshop bridges the gap between basic IaC adoption and production-grade infrastructure automation.
   
   You'll learn how to transform manual or partially automated infrastructure processes into fully automated, secure delivery pipelines. Through hands-on demos using Pulumi and GitHub Actions, you will learn how to implement enterprise-grade practices including repeatable deployments of infrastructure pipelines, automated drift detection, and secure credential handling. Discover how to overcome common challenges in infrastructure automation while building deployment workflows that enhance security, improve reliability, and reduce operational overhead.
   
   This workshop is ideal for teams looking to mature their IaC practices and establish repeatable, secure infrastructure delivery processes.

learn:
    - Best practices for automating infrastructure delivery with IaC
    - How to create technically sound, secure IaC pipelines that reduce secret sprawl and improve your organization's security posture
    - How to enable drift detection for your infrastructure to ensure that your cloud resources stay auto

# The event presenters
presenters:
    - name: Rob Smith 
      role: Solutions Architect, Pulumi
      photo: /images/team/Rob-Smith.png

# case-sensitive
tags:
    level: Intermediate # Beginner, Intermediate, Advanced
    topics: ["Platform Engineering"]
    languages: ["TypeScript"]
    clouds: ["AWS"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: a44783df-451c-4d8a-9785-005304e4c7a5
    salesforce_campaign_id: 701PQ00000ObSHGYA3

---
