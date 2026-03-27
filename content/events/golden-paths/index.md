---
# Name of the event, <= 60 characters
title: "Golden Paths: Infrastructure Components and Templates"
meta_desc: Create reusable infrastructure components and templates that enable developer self-service while enforcing standards.
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
url_slug: golden-paths

# The event type (workshop, webinar, talk).
event_type: workshop

# URL for embedding a URL for ungated events.
youtube_url: 

# Sortable date. The datetime Hugo will use to sort the events in date order.
sortable_date: 2025-08-06T12:00:00-04:00

# Duration of the event.
duration: 60 minutes

# "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
location: virtual

# Description of the event.
description: |
    Golden paths are the foundation of successful Internal Developer Platforms—providing developers with pre-approved, production-ready infrastructure patterns they can self-serve. This hands-on workshop teaches you to build reusable Pulumi components and templates that encapsulate your organization's best practices. You'll learn to create composable building blocks that make the right thing the easy thing, reducing cognitive load for developers while maintaining operational excellence.
learn:
    - How to design and build reusable Pulumi components for common infrastructure patterns
    - Template creation strategies that balance flexibility with opinionated defaults
    - Component composition techniques for building complex infrastructure applications from simple building blocks.

# The event presenters
presenters:
    - name: Rob Smith
      role: Solutions Architect, Pulumi
      photo: /images/team/Rob-Smith.png
    - name: Engin Diri
      role: Senior Solutions Architect, Pulumi
      photo: /images/team/engin-diri.jpg

# case-sensitive
tags:
    level: Intermediate # Beginner, Intermediate, Advanced
    topics:  ["Platform Engineering", "Infrastructure as Code", "Components"]
    clouds: ["AWS"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 8bca877b-1398-442f-88ea-16ae11b77182
    salesforce_campaign_id: 701PQ00000ZYBbEYAX

--- 
