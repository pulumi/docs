---
# Name of the event, <= 60 characters
title: "Build a multi-service app with Azure Container Apps"
meta_desc: Learn how to build and deploy a complete multi-service application to Azure Container Apps using Pulumi.
meta_image:

# A featured event will display first in the list.
featured: false

# Events with unlisted as true will not be shown on the event list
unlisted: false

# Gated events will have a registration form and the user will need
# to fill out the form before viewing.
gated: false

# External events will link to an external page instead of an event
# landing/registration page. If the event is external you will need
# set the 'block_external_search_index' flag to true so Google does not index
# the event page created.
external: false
block_external_search_index: false

# The url slug for the event landing page. If this is an external
# event, use the external URL as the value here.
url_slug: multi-service-application-with-azure-container-apps

# The event type (workshop, webinar, talk).
event_type: workshop

# URL for embedding a URL for ungated events.
youtube_url: https://www.youtube.com/embed/yTRPd39oN7A?si=KedQE5WTQbSnCxgq

# Sortable date. The datetime Hugo will use to sort the events in date order.
sortable_date: 2026-01-15T12:00:00-05:00

# Duration of the event.
duration: 60 minutes

# "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
location: virtual

# Description of the event.
description: |
    Learn how to build and deploy a complete multi-service application to Azure Container Apps using Pulumi. This hands-on workshop guides you through deploying a real-world two-tier architecture with a backend API and front-end web UI. Using Pulumi’s infrastructure as code approach, you’ll provision Azure Container Registry, Container Apps environments, and configure service-to-service communication, all as version-controlled, reproducible code.
learn:
    - Deploy a multi-service application to Azure Container Apps
    - Build and manage container images with Azure Container Registry
    - Implement secure service-to-service communication
    - Manage application configuration and environment variables
    - Create reproducible, version-controlled infrastructure with Pulumi

# The event presenters
presenters:
    - name: Adam Bell
      role: Community Engineer, Pulumi
      photo: /images/team/adam-gordon-bell.jpg

# case-sensitive
tags:
    level: Beginner # Beginner, Intermediate, Advanced
    topics:  ["Azure Container Apps"]
    languages: ["C#"]
    clouds: ["Azure"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 1aa7f3f2-8111-4df1-8421-db8133a1a6f7
    salesforce_campaign_id: 701PQ00000liIr0YAE

---
