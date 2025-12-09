---
# Name of the event, <= 60 characters
title: "Build a multi-service app with Azure Container Apps"
meta_desc: Learn how to build and deploy a complete multi-service application to Azure Container Apps using Pulumi.
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
url_slug: multi-service-application-with-azure-container-apps

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Build a multi-service app with Azure Container Apps"
    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: 

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2026-01-15T12:00:00-05:00

    # Duration of the webinar.
    duration: 60 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        Learn how to build and deploy a complete multi-service application to Azure Container Apps using Pulumi. This hands-on workshop guides you through deploying a real-world two-tier architecture with a backend API and front-end web UI. Using Pulumi’s infrastructure as code approach, you’ll provision Azure Container Registry, Container Apps environments, and configure service-to-service communication, all as version-controlled, reproducible code.
    learn:
        - Deploy a multi-service application to Azure Container Apps
        - Build and manage container images with Azure Container Registry
        - Implement secure service-to-service communication
        - Manage application configuration and environment variables
        - Create reproducible, version-controlled infrastructure with Pulumi

    # The webinar presenters
    presenters:
        - name: Adam Bell
          role: Community Engineer, Pulumi
          photo: /images/team/adam-gordon-bell.jpg
    
    # case-sensitive
    tags:
        level: Beginner # Beginner, Intermediate, Advanced
        topics:  ["Azure Container Apps"]
        languages: ["Any"]
        clouds: ["Azure"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 1aa7f3f2-8111-4df1-8421-db8133a1a6f7
    salesforce_campaign_id: 701PQ00000liIr0YAE

event_data:
  name: "Build a multi-service app with Azure Container Apps"
  start_date: 2026-01-15T12:00:00-05:00
  end_date: 2026-01-15T13:00:00-05:00
  url: "https://www.pulumi.com/resources/multi-service-application-with-azure-container-apps/"
  description: |
    Learn how to build and deploy a complete multi-service application to Azure Container Apps using Pulumi. This hands-on workshop guides you through deploying a real-world two-tier architecture with a backend API and front-end web UI. Using Pulumi’s infrastructure as code approach, you’ll provision Azure Container Registry, Container Apps environments, and configure service-to-service communication, all as version-controlled, reproducible code.
---
