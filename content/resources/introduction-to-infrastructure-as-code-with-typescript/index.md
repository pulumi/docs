---
# Name of the event, <= 60 characters
title: Intro to Infrastructure as Code with TypeScript
meta_desc: Learn the fundamentals of Infrastructure as Code (IaC) with Pulumi, using Docker, and TypeScript. Build and deploy a full stack app. Source code available.
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
url_slug: introduction-to-infrastructure-as-code-with-typescript

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Intro to Infrastructure as Code with TypeScript

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: https://www.youtube.com/embed/7ixwuUptuZ0?rel=0

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2022-12-08T18:00:00.000Z

    # Duration of the webinar.
    duration: 1 hour

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        In this workshop, you will learn the fundamentals of Infrastructure as Code through a series of guided exercises using Pulumi’s Cloud Engineering platform. You will be introduced to Pulumi, an infrastructure as code platform, where you can use familiar programming languages to provision modern cloud infrastructure.

        This workshop is designed to help users completely new to Pulumi to become familiar with the core concepts to be effective with the Pulumi Infrastructure as Code platform. We will guide you through the Pulumi platform with diagrams and a series of hands on exercises to help you understand the building blocks available in Pulumi.

        If you want to code along, you’ll need a [free Pulumi SaaS account](https://app.pulumi.com/signup/) and [the Pulumi CLI](https://www.pulumi.com/docs/install/)

    learn:
        - How to use TypeScript with Pulumi.
        - How to provision Docker containers with Pulumi.

    # The webinar presenters
    presenters:
        - name: Scott Lowe
          role: Sr. Technical Content Engineer, Pulumi
          photo: /images/team/scott-lowe.jpg

    # case-sensitive
    tags:
        level: Beginner # Beginner, Intermediate, Advanced
        topics: ["Docker"]
        languages: ["TypeScript"]

# The right hand side form section.
form:
  hubspot_form_id: 3a6aaf53-8479-4236-9376-58964fe6d5c6
  salesforce_campaign_id: 701Du0000009P9BIAU
---
