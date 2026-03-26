---
# Name of the event, <= 60 characters
title: Build a Self-Service Platform for Oracle Cloud with Pulumi
meta_desc: Building a Self-Service Platform for Oracle Cloud Infrastructure (OCI) Services with Backstage and Pulumi
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
url_slug: build-self-service-platform-oracle-cloud-pulumi

# The event type (workshop, webinar, talk).
event_type: workshop

# URL for embedding a URL for ungated events.
youtube_url:

# Sortable date. The datetime Hugo will use to sort the events in date order.
sortable_date: 2024-04-25T08:00:00-07:00

# Duration of the event.
duration: 90 minutes

# "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
location: virtual

# Description of the event.
description: |
  This workshop is designed to accelerate the learning curve for platform engineers and DevOps teams on their journey with OCI, leveraging Infrastructure as Code (IaC). Participants will be guided through the steps to customize and deploy Backstage on an Oracle Container Instance and to design their first Backstage templates for major OCI services.

learn:
    - A deeper understanding of OCI serverless services.
    - How to set up Backstage and deploy it on OCI using Pulumi IaC.
    - How to write your first Backstage templates to kickstart your self-service catalog.

# The event presenters
presenters:
  - name: Engin Diri
    role: Senior Community Engineer, Pulumi
    photo: /images/team/engin-diri.jpg
  - name: Eli Schilling
    role: Developer Advocate, Cloud Native and DevOps, Oracle
    photo: /images/people/eli-schilling.jpg

# case-sensitive
tags:
    level: Intermediate # Beginner, Intermediate, Advanced
    topics: ["Backstage", "Platform Engineering"]
    languages: ["YAML"]
    clouds: ["Oracle"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 52f0a5f7-9b22-4fa6-8834-f138df265f00
    salesforce_campaign_id: 701PQ000009SEXVYA4
---