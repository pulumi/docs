---
# Name of the event, <= 60 characters
title: Getting Started with Infrastructure as Code on GCP
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
url_slug: getting-started-with-iac-google-cloud-typescript

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Getting Started with Infrastructure as Code on GCP

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url:

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2024-06-26T09:00:00.000-07:00

    # Duration of the webinar.
    duration: 90 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        In this workshop, you will learn the fundamentals of infrastructure as code through guided exercises. You will be introduced to Pulumi, an infrastructure-as-code platform, where you can use familiar programming languages to provision modern cloud infrastructure.

        This workshop is designed to help new users become familiar with the core concepts needed to effectively deploy resources on Google Cloud. We will guide you through the Pulumi platform with diagrams and a series of labs to help accelerate your cloud projects.

    learn:
        - The basics of the Pulumi Programming Model
        - How to deploy resources on Google Cloud

    # The webinar presenters
    presenters:
        - name: Engin Diri
          role: Sr. Community Engineer, Pulumi
          photo: /images/team/engin-diri.jpg
        - name: Jason Smith
          role: Sr. Cloud Customer Engineer, Google
          photo: /images/team/jay-smith-google-jpeg.jpg
    # case-sensitive
    tags:
        level: Beginner # Beginner, Intermediate, Advanced
        topics: []
        languages: ["TypeScript"]
        clouds: ["Google Cloud"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 63a96e7b-76e8-4c57-9fcb-da2d8b05fa69
    salesforce_campaign_id: 701PQ00000CyiIcYAJ
---
