---
# Name of the event, <= 60 characters
title: "Migrating IaC from Terraform to TypeScript"
meta_desc: Learn how to leverage TypeScript's flexibility and ecosystem to simplify your infrastructure code and streamline cloud operations.
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
url_slug: migrating-iac-terraform-to-typescript

# The event type (workshop, webinar, talk).
event_type: workshop

# URL for embedding a URL for ungated events.
youtube_url: 

# Sortable date. The datetime Hugo will use to sort the events in date order.
sortable_date: 2025-01-29T09:00:00-08:00

# Duration of the event.
duration: 90 minutes

# "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
location: virtual

# Description of the event.
description: |
   Teams managing cloud infrastructure sometimes want the flexibility of a general-purpose language for complex workflows and long-term maintainability. This workshop demonstrates how transitioning to a general-purpose programming language can transform your infrastructure management, making common tasks more intuitive and maintainable.
   
   You'll discover how TypeScript's rich ecosystem of libraries and familiar syntax can simplify everything from dynamic resource creation to complex configuration management. Through practical examples, we'll explore strategies for gradually migrating existing infrastructure code while maintaining operational stability.
   
   Whether you're dealing with repetitive boilerplate, struggling with complex state management, or seeking more flexibility in your infrastructure automation, you'll learn how to leverage TypeScript's capabilities to build more elegant and powerful infrastructure solutions that scale with your organization's needs.

learn:
    - How a general-purpose language like TypeScript can simplify common infrastructure tasks for teams that prefer one
    - How to introduce Pulumi IaC and either coexist with or convert your existing Terraform code
    - How Pulumi's advanced features can help enable even greater capabilities for your organization to keep teams moving fast, securely

# The event presenters
presenters:
    - name: Josh Kodroff 
      role: Principal Solutions Architect, Pulumi
      photo: /images/team/josh-kodroff.jpg

# case-sensitive
tags:
    level: Intermediate # Beginner, Intermediate, Advanced
    topics: ["Platform Engineering"]
    languages: ["TypeScript"]
    clouds: ["AWS"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 53f23815-4b41-45ce-a926-1dc69e5a50b5
    salesforce_campaign_id: 701PQ00000Obc8XYAR

---
