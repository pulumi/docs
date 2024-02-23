---
# Name of the event, <= 60 characters
title: Get Started with Infrastructure as Code on Azure with Java
meta_desc: Learn the basics of Azure and Pulumi with a hands-on lab that will take you from deploying a simple static website to deploying a Spring Boot application.
meta_image: /images/get-started-azure-with-java.png

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
url_slug: getting-started-infrascructure-as-code-azure-java

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Get Started with Infrastructure as Code on Azure with Java

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: https://www.youtube.com/embed/tsdZpv63lhQ?rel=0

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2022-11-22T09:00:00-08:00

    # Duration of the webinar.
    duration: 1 hour

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        It’s now easier than ever for Java developers to deploy their apps to Microsoft Azure using Pulumi and Java. In this session, we’ll teach you the basics of Azure and Pulumi with hands-on labs that will take you from deploying a simple static website to deploying a Spring Boot application to the Azure App Service.

    learn:
        - Infrastructure as Code concepts for Java developers
        - Managing Azure resources with Pulumi
        - Deploying Spring Boot apps to the Azure App Service

    # The webinar presenters
    presenters:
        - name: Josh Kodroff
          role: Senior Solutions Architect, Pulumi
          photo: /images/team/josh-kodroff.jpg
        - name: Brian Benz
          role: Senior Cloud Advocate, Microsoft

    # case-sensitive
    tags:
        level: Beginner # Beginner, Intermediate, Advanced
        topics: ["Azure"]
        languages: ["Java"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 1331a411-ef77-43bd-8eae-4a1f9d5698fe
    salesforce_campaign_id: 
---
