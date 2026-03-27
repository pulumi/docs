---
# Name of the event, <= 60 characters
title: Enabling Platform Workflows with Temporal
meta_desc: Unlock Temporal Cloud's full potential with Pulumi. Learn to automate resource management, enhance developer workflows, and build platform engineering solutions
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
url_slug: enabling-platform-workflows-with-temporal

# The event type (workshop, webinar, talk).
event_type: workshop

# URL for embedding a URL for ungated events.
youtube_url: 

# Sortable date. The datetime Hugo will use to sort the events in date order.
sortable_date: 2025-06-24T12:00:00-04:00

# Duration of the event.
duration: 60 minutes

# "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
location: virtual

# Description of the event.
description: |
    Platform Engineering teams are responsible for giving developers clear, repeatable playbooks for orchestrating resilient, scalable applications. When using Temporal Cloud, managing Namespaces, Task Queues, and Worker configurations effectively is crucial to ensuring reliability and performance.
    
    In this workshop, we’ll explore how Pulumi empowers teams to define, provision, and manage Temporal Cloud resources using modern Infrastructure as Code (IaC) practices. You'll learn how to automate resource lifecycles, enforce policies, and integrate Temporal Cloud into platform engineering workflows—ensuring developers have a seamless and self-service experience.

learn:
    - "IaC for Temporal Cloud: Automate the provisioning and lifecycle management of Temporal Namespaces, Task Queues, and Workers using Pulumi."
    - "Consistency & Compliance: Enforce governance, security, and best practices for Temporal Cloud resources across multiple environments."
    - "Hands-on Automation: Trigger a complex deployment cycle with Pulumi Deployments and create approval steps"

# The event presenters
presenters:
    - name: Yosef Ejigu
      role: Solutions Engineer, Pulumi, Pulumi
      photo: /images/team/yosef-ejigu.jpg
    - name: Cornelia Davis
      role: Developer Advocate, Temporal
      photo: /images/people/cornelia-davis.jpg

# case-sensitive
tags:
    level: Intermediate # Beginner, Intermediate, Advanced
    topics:  ["Temporal", "Platform Engineering"]
    languages: ["TypeScript"]
    clouds: ["AWS"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 45641519-d8a1-4507-8e59-da1847c4b743
    salesforce_campaign_id: 701PQ00000VDHioYAH

---
