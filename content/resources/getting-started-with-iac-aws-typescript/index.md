---
# Name of the event, <= 60 characters
title: Getting Started with Infrastructure as Code on AWS
meta_desc: In this workshop, you will learn the fundamentals of Infrastructure as Code through a series of guided exercises using the Pulumi Cloud Engineering platform.
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
url_slug: getting-started-with-iac-aws-typescript

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Getting Started with Infrastructure as Code on AWS

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url:

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2024-06-27T09:00:00.000-07:00

    # Duration of the webinar.
    duration: 90 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        Learn the fundamentals of Infrastructure as Code through a series of guided exercises using AWS and Pulumi’s platform, where you can use familiar programming languages to provision modern cloud infrastructure.

        This workshop is designed to help users who are completely new to Pulumi become familiar with the core concepts to be effective with the Pulumi Infrastructure as Code platform. We will guide you through the Pulumi platform with diagrams and a series of hands-on exercises to help you understand the building blocks available in Pulumi.

    learn:
        - The basics of the Pulumi Programming Model
        - How to provision, update, and destroy AWS resources
        - Build a simple serverless App with Lambda and s3 bucket

    # The webinar presenters
    presenters:
        - name: Diana Esteves
          role: Solutions Architect, Pulumi
          photo: /images/team/diana-esteves.jpg

    # case-sensitive
    tags:
        level: Beginner # Beginner, Intermediate, Advanced
        topics: []
        languages: ["TypeScript"]
        clouds: ["AWS"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: f1c53015-61ab-4d37-bc32-21869a3d7286
    salesforce_campaign_id: 701PQ00000DVVBJYA5
---
