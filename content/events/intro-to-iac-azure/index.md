---
# Name of the event, <= 60 characters
title: "Learn Azure Infrastructure with C#"
meta_desc: Learn how to build and manage Azure infrastructure using C# and Pulumi. A better alternative to ARM templates with full .NET support.
meta_image:

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
external: false
block_external_search_index: false

# The url slug for the event landing page. If this is an external
# event, use the external URL as the value here.
url_slug: intro-to-iac-azure

# The event type (workshop, webinar, talk).
event_type: workshop

# URL for embedding a URL for ungated events.
youtube_url: https://www.youtube.com/embed/FbrxKzhOsjs?si=ShpYzJbqgTiDYxra

# Sortable date. The datetime Hugo will use to sort the events in date order.
sortable_date: 2025-09-24T09:00:00-07:00

# Duration of the event.
duration: 60 minutes

# "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
location: virtual

# Description of the event.
description: |
    Want to learn Azure using C#? If you know .NET, you can do more than build apps, you can also build and manage your Azure infrastructure with the same language and tools.

    This hands-on workshop shows you how to define, deploy, and manage Azure resources in C#. Instead of writing JSON-based ARM templates, you’ll use real C# code to provision Azure services, automate deployments, and scale your cloud environments.

    With Pulumi, you bring the full power of C# to Azure Infrastructure as Code. That means fewer manual steps, less duplication, and a smoother path from application code to cloud infrastructure.

    Whether you’re just getting started with Azure or looking for a better alternative to ARM templates, you’ll discover a modern, developer-friendly way to build on the Microsoft cloud.
learn:
    - How to get started with Azure infrastructure in C#
    - Key concepts of Azure Infrastructure as Code with Pulumi
    - How to define, provision, and manage Azure resources using .NET
    - Why C# with Pulumi is a powerful alternative to JSON-based ARM templates
    - Examples of reusable, scalable Azure infrastructure written entirely in C#

# The event presenters
presenters:
    - name: Adam Gordon Bell
      role: Community Engineer, Pulumi
      photo: /images/team/adam-gordon-bell.jpg

# case-sensitive
tags:
    level: Beginner # Beginner, Intermediate, Advanced
    topics:  ["Infrastructure as Code", "DevOps", "Automation"]
    languages: ["C#"]
    clouds: ["Azure"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 0fe7c9bd-333a-4ade-aa7c-2e21768df3a6
    salesforce_campaign_id: 701PQ00000eZOZuYAO

---
