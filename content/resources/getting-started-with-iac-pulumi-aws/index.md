---
# Name of the event, <= 60 characters
title: Getting Started with Infrastructure as Code on AWS
meta_desc: This workshop is designed to help new users become familiar with the core concepts needed to effectively deploy resources on AWS using Pulumi.
meta_image: /images/resources/getting-started-aws-kat.png

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
url_slug: getting-started-with-iac-pulumi-aws

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Getting Started with Infrastructure as Code on AWS

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: https://www.youtube.com/embed/ZeU7dmxCjuM?rel=0

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2023-11-14T09:00:00.000-08:00

    # Duration of the webinar.
    duration: 90 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        In this workshop, you will learn the fundamentals of infrastructure as code through guided exercises. You will be introduced to Pulumi, an infrastructure-as-code platform, where you can use familiar programming languages to provision modern cloud infrastructure.
    
        This workshop is designed to help new users become familiar with the core concepts needed to effectively deploy resources on AWS. We will guide you through the Pulumi platform with diagrams and a series of labs to help accelerate your cloud projects.

    learn:
        - The basics of the Pulumi Programming Model
        - How to provision, update, and destroy AWS resources
        - All the new features of aws-classic v6 and AWSX

    # The webinar presenters
    presenters:
        - name: Josh Kodroff
          role: Sr. Solutions Architect, Pulumi
          photo: /images/team/josh-kodroff.jpg

    # case-sensitive
    tags:
        level: Beginner # Beginner, Intermediate, Advanced
        topics: []
        languages: []
        clouds: ["AWS"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 9f553ea2-c429-473e-9fbe-7ffca0ac0dff
    salesforce_campaign_id: 701Du000000BVBlIAO
---
