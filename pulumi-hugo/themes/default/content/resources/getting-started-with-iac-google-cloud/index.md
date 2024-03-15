---
# Name of the event, <= 60 characters
title: Getting Started with Infrastructure as Code on Google Cloud
meta_desc: In this workshop, you will learn the core concepts needed to effectively deploy resources on Google Cloud with Pulumi.
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
url_slug: getting-started-with-iac-google-cloud

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Getting Started with Infrastructure as Code on Google Cloud

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url:

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2024-04-24T09:00:00.000-07:00

    # Duration of the webinar.
    duration: 1 hour

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
        - name: Diana Esteves
          role: Solutions Architect, Pulumi
          photo: /images/team/diana-esteves.jpg
        - name: Jayson Smith
          role: Sr. Cloud Customer Engineer, Google

    # case-sensitive
    tags:
        level: Beginner # Beginner, Intermediate, Advanced
        topics: ["Google Cloud"]
        languages: []

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 69fe7896-fa8e-4812-b76e-3436363ac4a2
    salesforce_campaign_id: 701PQ000008Z5OQYA0
---