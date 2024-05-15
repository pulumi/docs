---
# Name of the event, <= 60 characters
title: Get started with CI/CD for AWS using Pulumi & GitHub Actions
meta_desc: In this workshop, you will learn the fundamentals of an infrastructure CI/CD pipeline through guided exercises using Pulumi.
meta_image: "/images/resources/cicd-aws-github-actions-diana.png"


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
url_slug: cicd-for-aws-with-pulumi-and-github-actions

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Get started with CI/CD for AWS using Pulumi & GitHub Actions

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url:

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2024-03-29T09:00:00-07:00

    # Duration of the webinar.
    duration: 90 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        This workshop introduces new users to DevOps best practices. You will become familiar with the core concepts needed to deploy cloud resources continuously. Walk through configuring Pulumi GitHub Actions to deploy AWS resources programmatically and accelerate your cloud projects with the skeleton code provided.

    learn:
        - The basics of the Pulumi programming model
        - The key components of a continuous pipeline
        - How to build your own infrastructure CI/CD pipeline
        - Configuring the Pulumi GitHub Actions to deploy AWS resources

    # The webinar presenters
    presenters:
        - name: Diana Esteves
          role: Technical Content Engineer, Pulumi
          photo: /images/team/diana-esteves.jpg
        - name: Marina Novikova
          role: Sr. Solutions Architect, AWS
          photo: /images/team/marina-novikova.jpg

    # case-sensitive
    tags:
        level: Beginner # Beginner, Intermediate, Advanced
        topics: ["GitHub Actions", "DevOps", "CI/CD"]
        languages: []
        clouds: ["AWS"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 33107308-f24a-47f2-bb6d-c26850491d0d
    salesforce_campaign_id: 701PQ0000074nvmYAA
---
