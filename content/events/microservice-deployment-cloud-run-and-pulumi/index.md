---
# Name of the event, <= 60 characters
title: Efficient Microservice Deployment on Cloud Run with Pulumi
meta_desc: Join the workshop 'Efficient Microservice Deployment on Google Cloud Run' to learn how to build and deploy microservices with minimal code changes.
meta_image: /images/resources/microservice-deployment-cloud-run-kat-xiang.png

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
url_slug: microservice-deployment-cloud-run-and-pulumi

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Efficient Microservice Deployment on Cloud Run with Pulumi

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url:

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2024-02-28T09:00:00.000-08:00

    # Duration of the webinar.
    duration: 90 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        Discover how to build and deploy microservices with minimal code changes using Cloud Run. Learn to secure internal services with serverless VPC connectors, leverage Redis in Memorystore, and deploy infrastructure using Pulumi. Ideal for developers seeking efficient, scalable solutions on Google Cloud.

    learn:
        - How to secure internal services
        - Defining resources in Google Cloud with Pulumi
        - Running and scaling your application on Cloud Run

    # The webinar presenters
    presenters:
        - name: Kat Morgan
          role: Senior Developer Advocate, Pulumi
          photo: /images/team/kat-morgan.jpg
        - name: Xiang Shen
          role: Solutions Architect, Google Cloud
          photo: /images/people/xiang-shen.jpg

    # case-sensitive
    tags:
        level: Intermediate # Beginner, Intermediate, Advanced
        topics: []
        languages: []
        clouds: ["Google Cloud"]

# The right hand side form section.
form:
  hubspot_form_id: c3944d6f-4de2-48b4-a597-01c83aecc57a
  salesforce_campaign_id: 701Du000000BuctIAC
---
