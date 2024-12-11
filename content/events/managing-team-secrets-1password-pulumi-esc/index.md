---
# Name of the event, <= 60 characters
title: Managing team secrets with 1Password & Pulumi ESC
meta_desc: Learn Pulumi ESC + 1Password for secure, automated secret management in multi-cloud setups. Store & fetch secrets easily in our workshop
meta_image: "/images/resources/1password-pulumi-esc-platform-engineering.png"

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
url_slug: managing-team-secrets-1password-pulumi-esc

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Managing team secrets with 1Password & Pulumi ESC

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: https://www.youtube.com/embed/8AgmP01_qnw?rel=0

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2024-04-23T09:00:00.000-07:00

    # Duration of the webinar.
    duration: 90 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        Platform engineering teams need to be able to fetch secrets at runtime, especially when managing multi-cloud and multi-service deployments with Pulumi. In this workshop, we’ll show you how Pulumi ESC works with 1Password to ensure secrets are securely made available to approved team members and deployments.


    learn:
        - How to store secrets in 1Password
        - Configuring Pulumi ESC to work with 1Password and controlling access for approved team members
        - Retrieving secrets automatically at runtime from your Infrastructure as Code deployments.

    # The webinar presenters
    presenters:
        - name: Simon Barendse
          role: Team Lead, Engineering - Programmatic Interfaces @ 1Password
          photo: /images/people/simon-barendse.jpg
        - name: Diana Esteves
          role: Solutions Architect, Pulumi
          photo: /images/team/diana-esteves.jpg

    # case-sensitive
    tags:
        level: Intermediate # Beginner, Intermediate, Advanced
        topics: ["Secrets Management", "Platform Engineering"]
        languages: ["Golang"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: d9cca680-de60-4cef-9e45-84e9bbef1d3f
    salesforce_campaign_id: 701PQ000009KHXRYA4
---
