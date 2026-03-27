---
# Name of the event, <= 60 characters
title: "Automate Cloud Compliance with Policy as Code"
meta_desc: Learn how to automate cloud compliance and security guardrails using policy as code to ensure consistent infrastructure governance at scale.

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
url_slug: cloud-compliance-policy-as-code

# The event type (workshop, webinar, talk).
event_type: workshop

# URL for embedding a URL for ungated events.
youtube_url: 

# Sortable date. The datetime Hugo will use to sort the events in date order.
sortable_date: 2025-02-19T09:00:00-08:00

# Duration of the event.
duration: 90 minutes

# "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
location: virtual

# Description of the event.
description: |
   As organizations scale their cloud infrastructure, maintaining security and compliance becomes increasingly complex. This workshop explores how Policy as Code (PaC) transforms traditional manual compliance processes into automated, version-controlled, and programmatically enforced guardrails
   
   Participants will learn how to implement effective cloud governance strategies using modern PaC approaches, including writing custom policies, integrating them into CI/CD pipelines, and establishing automated enforcement mechanisms. Through practical demonstrations using Pulumi Policies, you'll discover how to bridge the gap between security requirements and infrastructure deployment while maintaining development velocity.
   
   Whether you're dealing with cost management, security compliance, or architectural standards, you'll leave with actionable insights to implement PaC in your organization.

learn:
    - How to transform compliance requirements into programmatic rules that can be version-controlled and automatically enforced
    - How to integrate policy enforcement into developer workflows and CI/CD pipelines to catch violations early in the development lifecycle and ensure your cloud environments stay in compliance
    - How to manage evolving security and compliance requirements against infrastructure at scale

# The event presenters
presenters:
    - name: James Connell
      role: Sr Solutions Architect, Pulumi
      photo: /images/team/James-Connell.jpg

# case-sensitive
tags:
    level: Intermediate # Beginner, Intermediate, Advanced
    topics: ["Platform Engineering"]
    languages: ["TypeScript"]
    clouds: ["AWS"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 37582977-ca15-467e-9238-900a45939faf
    salesforce_campaign_id: 701PQ00000ObegbYAB

---
