---
# Name of the event, <= 60 characters
title: "Start Building Azure Infrastructure with C#"
meta_desc: Learn how to build and manage Azure infrastructure using C# and Pulumi. A better alternative to ARM templates with full .NET support.
meta_image:

# A featured webinar will display first in the list.
featured: false

# Webinars with unlisted as true will not be shown on the webinar list
unlisted: false

# Gated webinars will have a registration form and the user will need
# to fill out the form before viewing.
gated: false

# The layout of the landing page.
type: webinars

# External webinars will link to an external page instead of a webinar
# landing/registration page. If the webinar is external you will need
# set the 'block_external_search_index' flag to true so Google does not index
# the webinar page created.
external: false
block_external_search_index: false

# The url slug for the webinar landing page. If this is an external
# webinar, use the external URL as the value here.
url_slug: intro-to-iac-azure

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Start Building Azure Infrastructure with C#"
    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: https://www.youtube.com/embed/FbrxKzhOsjs?si=ShpYzJbqgTiDYxra

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2025-09-24T09:00:00-07:00

    # Duration of the webinar.
    duration: 60 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        You know C# and you're working with Azure or planning to. But managing infrastructure with JSON-based ARM templates can be tedious, hard to scale, and disconnected from how you write application code.

        This hands-on workshop shows you how to build real-world Azure infrastructure using Pulumi and your existing .NET skills. You'll learn how to define, deploy, and manage Azure resources in C# using familiar programming tools and patterns.

        Pulumi brings the full power of C# to Infrastructure as Code. You'll move faster, reduce duplication, and build scalable, reliable infrastructure with less friction.

        If you're currently using ARM templates or just starting to explore Azure, this workshop will introduce a more flexible and developer-friendly way to manage your cloud infrastructure.
    learn:
        - How to get started with Pulumi and C# for Azure infrastructure
        - Key concepts of the Pulumi programming model for Infrastructure as Code
        - How to define, provision, and manage Azure resources using .NET
        - Why C# with Pulumi is a powerful alternative to JSON-based ARM templates
        - Examples of reusable and scalable infrastructure written entirely in C#

    # The webinar presenters
    presenters:
        - name: Adam Gordon Bell
          role: Community Engineer, Pulumi
          photo: /images/team/adam-gordon-bell.jpg

    # case-sensitive
    tags:
        level: Beginner # Beginner, Intermediate, Advanced
        topics:  ["IaC", "DevOps", "Automation"]
        languages: ["C#"]
        clouds: ["Azure"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 0fe7c9bd-333a-4ade-aa7c-2e21768df3a6
    salesforce_campaign_id: 701PQ00000eZOZuYAO

event_data:
  name: "Start Building Azure Infrastructure with C#"
  start_date: 2025-09-24T09:00:00-07:00
  end_date: 2025-09-24T10:00:00-07:00
  url: "https://www.pulumi.com/resources/intro-to-iac-azure/"
  description: |
    You know C# and you're working with Azure or planning to. But managing infrastructure with JSON-based ARM templates can be tedious, hard to scale, and disconnected from how you write application code.

    This hands-on workshop shows you how to build real-world Azure infrastructure using Pulumi and your existing .NET skills. You'll learn how to define, deploy, and manage Azure resources in C# using familiar programming tools and patterns.

    Pulumi brings the full power of C# to Infrastructure as Code. You'll move faster, reduce duplication, and build scalable, reliable infrastructure with less friction.

    If you're currently using ARM templates or just starting to explore Azure, this workshop will introduce a more flexible and developer-friendly way to manage your cloud infrastructure.
---
