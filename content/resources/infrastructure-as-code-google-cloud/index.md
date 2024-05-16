---
# Name of the event, <= 60 characters
title: Getting Started with Infrastructure as Code on Google Cloud
meta_desc: This workshop is designed to help new users become familiar with the core concepts needed to effectively deploy resources on Google Cloud using Pulumi.
meta_image: /images/resources/getting-started-iac-google-josh-jay.png

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
url_slug: infrastructure-as-code-google-cloud

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Getting Started with Infrastructure as Code on Google Cloud

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: https://www.youtube.com/embed/4RZWY1n2GPY?rel=0

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2024-01-31T09:00:00-08:00

    # Duration of the webinar.
    duration: 90 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        In this workshop, you will learn the fundamentals of infrastructure as code through guided exercises. You will be introduced to Pulumi, an infrastructure-as-code platform, where you can use familiar programming languages to provision modern cloud infrastructure. This workshop is designed to help new users become familiar with the core concepts needed to effectively deploy resources on Google Cloud. We will guide you through the Pulumi platform with diagrams and a series of labs to help accelerate your cloud projects.

    learn:

    # The webinar presenters
    presenters:
        - name: Josh Kodroff
          role: Sr. Solutions Architect, Pulumi
          photo: /images/team/josh-kodroff.jpg
        - name: Jayson Smith
          role: Sr. Cloud Customer Engineer, Google

    # case-sensitive
    tags:
        level: Beginner # Beginner, Intermediate, Advanced
        topics: []
        languages: []
        clouds: ["Google Cloud"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: ea5da134-9b0e-4a34-83f8-e2074f498f21
    salesforce_campaign_id: 701Du000000Bu2kIAC
---
