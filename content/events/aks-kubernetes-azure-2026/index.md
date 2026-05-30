---
# Name of the event, <= 60 characters
title: "Getting Started with Kubernetes on Azure"
meta_desc: Learn the fundamentals of running Kubernetes on Azure using AKS and Pulumi infrastructure-as-code tools.

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
external: true
block_external_search_index: true

# The url slug for the event landing page. If this is an external
# event, use the external URL as the value here.
url_slug: https://luma.com/4eia7arb

# The event type (workshop, webinar, talk).
event_type: workshop

# URL for embedding a URL for ungated events.
youtube_url:

# Sortable date. The datetime Hugo will use to sort the events in date order.
sortable_date: 2026-06-10T09:00:00-07:00

# Duration of the event.
duration: 1 hour

# "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
location: Virtual

# Description of the event.
description: |
    This introductory workshop covers the fundamentals of running Kubernetes on Azure using Azure Kubernetes Service (AKS). Participants will learn how Kubernetes fits into the Azure platform and how clusters and containerized workloads are created and managed through hands-on exercises. Attendees will gain understanding of establishing an AKS cluster via Pulumi, how Pulumi coordinates Azure and Kubernetes resources, deploying containerized applications to AKS with secure, repeatable processes, and managing infrastructure safely through preview, update, and teardown workflows.

# The event presenters
presenters:
    - name: Adam Gordon Bell
      role: Speaker

# case-sensitive
tags:
    level: Beginner # Beginner, Intermediate, Advanced
    topics: ["Kubernetes", "Infrastructure as Code", "Cloud Platforms"]
    languages: []
    clouds: ["Azure"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id:
    salesforce_campaign_id:

---
