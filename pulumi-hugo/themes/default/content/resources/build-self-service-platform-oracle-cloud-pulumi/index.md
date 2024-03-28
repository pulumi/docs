---
# Name of the event, <= 60 characters
title: Build a Self-Service Platform for Oracle Cloud with Pulumi
meta_desc: Building a Self-Service Platform for Oracle Cloud Infrastructure (OCI) Services with Backstage and Pulumi
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
url_slug: build-self-service-platform-oracle-cloud-pulumi

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Build a Self-Service Platform for Oracle Cloud with Pulumi

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url:

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2024-04-25T08:00:00-07:00

    # Duration of the webinar.
    duration: 90 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
      This workshop is designed to accelerate the learning curve for platform engineers and DevOps teams on their journey with OCI, leveraging Infrastructure as Code (IaC). Participants will be guided through the steps to customize and deploy Backstage on an Oracle Container Instance and to design their first Backstage templates for major OCI services.

    learn:
        - A deeper understanding of OCI serverless services.
        - How to set up Backstage and deploy it on OCI using Pulumi IaC.
        - How to write your first Backstage templates to kickstart your self-service catalog.

    # The webinar presenters
    presenters:
      - name: Engin Diri
        role: Senior Community Engineer, Pulumi
        photo: /images/team/engin-diri.jpg
      - name: Eli Schilling
        role: Developer Advocate, Cloud Native and DevOps, Oracle
        photo: /images/people/eli-schilling.jpg

    # case-sensitive
    tags:
        level: Intermediate # Beginner, Intermediate, Advanced
        topics: ["Backstage", "Oracle Cloud", "Platform Engineering"]
        languages: ["YAML"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 52f0a5f7-9b22-4fa6-8834-f138df265f00
    salesforce_campaign_id: 701PQ000009SEXVYA4
---