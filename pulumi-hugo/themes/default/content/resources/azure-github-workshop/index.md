---
# Name of the event, <= 60 characters
title: Getting Started with Azure IaC and Pulumi Deployments
meta_desc: Explore the new Azure Native v2 provider and learn how Pulumi Deployments make it easier to validate both infrastructure and app code before release.
meta_image: /images/resources/azure-deployments2.png

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
url_slug: azure-github-workshop

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Getting Started with Azure IaC and Pulumi Deployments

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: https://www.youtube.com/embed/iGNCBGWfOV0?rel=0

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2023-10-25T09:00:00.000-07:00

    # Duration of the webinar.
    duration: 1 hour

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        When managing cloud infrastructure, it’s important to establish a build-test-release process for your team. In this session, you will learn how to use Pulumi’s [Azure Native v2 provider](/blog/introducing-azure-native-v2/) and your favorite programming languages to stand up new projects on Azure quickly. Then, we’ll show you how Pulumi Deployments make it easier than ever to validate both infrastructure and app code before release.

    learn:
        - Infrastructure as Code on Azure
        - Serverless architectures
        - Setting up Pulumi Deployments

    # The webinar presenters
    presenters:
        - name: Josh Kodroff
          role: Sr. Solutions Architect, Pulumi
          photo: /images/team/josh-kodroff.jpg
        - name: Brian Benz
          role: Senior Cloud Advocate, Microsoft Azure

    # case-sensitive
    tags:
        level: Beginner # Beginner, Intermediate, Advanced
        topics: ["Azure", "Pulumi Deployments"]
        languages:

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 81828ab4-e433-4bfa-94a3-40b74ea2265c
    salesforce_campaign_id: 701Du000000Ab76IAC
---
