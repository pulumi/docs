---
# Name of the event, <= 60 characters
title: "Advanced Topics for Building an IDP"
meta_desc: Learn how to build modern IDPs using Pulumi while leveraging existing IaC investments and knowledge.
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
url_slug: advanced-topics-idp

# The event type (workshop, webinar, talk).
event_type: workshop

# URL for embedding a URL for ungated events.
youtube_url: 

# Sortable date. The datetime Hugo will use to sort the events in date order.
sortable_date: 2025-09-17T12:00:00-04:00

# Duration of the event.
duration: 60 minutes

# "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
location: virtual

# Description of the event.
description: |
    Many organizations have significant investments in legacy IaC platforms like Terraform but want to modernize their approach to include Internal Developer Platforms. This workshop shows how to build next-generation IDPs with Pulumi while leveraging existing Terraform infrastructure and team knowledge. You'll learn interoperability patterns, and how Pulumi creates a clear path from static infrastructure as code to dynamic, self-service platforms.
learn:
    - How to coexist with Terraform while delivering modern IDP infrastructure
    - How to modernize your IDP components incrementally - without throwing out known-good IaC.

# The event presenters
presenters:
    - name: Engin Diri
      role: Senior Solutions Architect, Pulumi
      photo: /images/team/engin-diri.jpg

# case-sensitive
tags:
    level: Intermediate # Beginner, Intermediate, Advanced
    topics:  ["Terraform", "Migration", "Platform Engineering"]
    clouds: ["AWS", "Azure", "Google Cloud"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 80baf260-52f7-481b-a085-5b8575eac389
    salesforce_campaign_id: 701PQ00000ZY23IYAT

--- 