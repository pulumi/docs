---
# Name of the event, <= 60 characters
title: Advanced Kubernetes Platforms on Google Cloud with Pulumi
meta_desc: In this workshop, we’ll explore how to deliver and scale a Kubernetes platform on Google Cloud.
meta_image: /images/resources/advanced-kubernetes-on-google-cloud-engin.png

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
url_slug: kubernetes-platforms-on-google-cloud

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Advanced Kubernetes Platforms on Google Cloud with Pulumi

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: https://www.youtube.com/embed/tchzFVFZmSY?rel=0

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2023-09-11T10:00:00.000-04:00

    # Duration of the webinar.
    duration: 90 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        Platform engineering teams often need to help development teams stand up core platforms, build release automation, deploy applications, and scale resources to match customer demand. A best practice in these scenarios is to break up these services into multiple stacks to enable updates to infrastructure and processes that won’t disrupt production.

        In this session, experts from Pulumi and Google Cloud will show you how to stand up networking and cluster components GKE Autopilot, configure CI/CD pipelines and run an application that leverages multiple Google Cloud resources. We’ll also show you how to scale your infrastructure across multiple regions.

    learn:
        - Google Cloud project and service creation
        - Managing Networks on Google Cloud
        - Setting up your development environment
        - Configuring GKE Autopilot for multiple regions
        - Setting up Cloud Build pipelines and more.

    # The webinar presenters
    presenters:
        - name: Tim Hiatt
          role: Technical Solutions Consultant, Google Cloud
        - name: Engin Diri
          role: Customer Experience Architect, Pulumi
          photo: /images/team/engin-diri.jpg

    # case-sensitive
    tags:
        level: Intermediate # Beginner, Intermediate, Advanced
        topics: ["Google Cloud", "Kubernetes"]
        languages: []

# The right hand side form section.
form:
  hubspot_form_id: 5f859a0d-bf36-4969-82f5-a4dd818b62ef
  salesforce_campaign_id: 701Du000000AupeIAC
---
