---
# Name of the event, <= 60 characters
title: Introduction to Infrastructure as Code on Azure
meta_desc: Learn how to use Pulumi to manage Azure resources in TypeScript
meta_image:

# A featured webinar will display first in the list.
featured: false

# Webinars with unlisted as true will not be shown on the webinar list
unlisted: false

# Gated webinars will have a registration form and the user will need
# to fill out the form before viewing.
gated: true

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
    title: Introduction to Infrastructure as Code on Azure

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url:

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2024-06-05T09:00:00.000-07:00

    # Duration of the webinar.
    duration: 60 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        In this workshop, you'll learn how to use Pulumi to help you manage infrastructure in Azure using general purpose programming languages. This workshop is designed to help users who are completely new to Pulumi become familiar with the core concepts to be effective with the Pulumi Infrastructure as Code platform.

        We'll take you through building several sample architectures on Azure through a series of hands-on exercises to get you started. The workshop exercises will be run in TypeScript, but practitioners of other Pulumi languages will likely find the material useful.

    learn:
        - The basics of the Pulumi Programming Model
        - How to manage Azure resources with Pulumi's Azure Native provider in TypeScript
        - An overview of Pulumi's features that help platform teams enable their organization to deliver faster

    # The webinar presenters
    presenters:
        - name: Josh Kodroff
          role: Sr. Solutions Architect, Pulumi
          photo: /images/team/josh-kodroff.jpg
    # case-sensitive
    tags:
        level: Beginner # Beginner, Intermediate, Advanced
        topics: []
        languages: ["TypeScript"]
        clouds: ["Azure"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 70ec73e2-d4cb-44b8-a5bb-32caab3c737d
    salesforce_campaign_id: 701PQ00000CADujYAH
---