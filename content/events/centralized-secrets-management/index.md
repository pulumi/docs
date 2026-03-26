---
# Name of the event, <= 60 characters
title: "Implementing Centralized Secrets Management for Your Team"
meta_desc: Learn how to implement a secure, scalable secrets management strategy that streamlines development while maintaining enterprise-grade security controls.

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
url_slug: centralized-secrets-management

# The event type (workshop, webinar, talk).
event_type: workshop

# URL for embedding a URL for ungated events.
youtube_url: 

# Sortable date. The datetime Hugo will use to sort the events in date order.
sortable_date: 2025-03-12T09:00:00-07:00

# Duration of the event.
duration: 90 minutes

# "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
location: virtual

# Description of the event.
description: |
   In modern cloud-native environments, managing secrets across multiple teams, applications, and environments has become increasingly complex. This workshop explores best practices for implementing centralized secrets management that balances security requirements with developer productivity. You'll learn how to establish a unified approach to handling configuration values, static secrets, and dynamic credentials while maintaining proper access controls and audit capabilities.
   
   Through practical demonstrations using Pulumi ESC, we'll explore how to consolidate secrets from various sources, implement role-based access controls, and seamlessly integrate with existing CI/CD pipelines. This workshop is designed for organizations looking to mature their infrastructure as code practices by establishing a robust secrets management strategy that scales with their team.

learn:
    - Design and implement a centralized secrets management architecture that reduces operational overhead while enhancing security posture
    - Master techniques for managing different types of secrets (static, dynamic, and configuration) across multiple environments and applications
    - Establish effective access controls and audit procedures that align with security best practices while maintaining developer velocity

# The event presenters
presenters:
    - name: Josh Kodroff 
      role: Principal Solutions Architect, Pulumi
      photo: /images/team/josh-kodroff.jpg

# case-sensitive
tags:
    level: Intermediate # Beginner, Intermediate, Advanced
    topics: ["Platform Engineering", "Pulumi ESC"]
    languages: ["TypeScript"]
    clouds: ["AWS"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 9e1cd3e2-bf83-4b19-a5d1-4a0520e54226
    salesforce_campaign_id: 701PQ00000Oba3XYAR

---
