---
# Name of the event, <= 60 characters
title: Automate Image Builds using Pulumi and Docker Build Cloud
meta_desc: Join our workshop to master automating your Docker build process using Pulumi Docker Build provider and Docker Build Cloud with TypeScript.
meta_image:

# A featured event will display first in the list.
featured: false

# Events with unlisted as true will not be shown on the event list
unlisted: false

# Gated events will have a registration form and the user will need
# to fill out the form before viewing.
gated: true

# External events will link to an external page instead of an event
# landing/registration page. If the event is external you will need
# set the 'block_external_search_index' flag to true so Google does not index
# the event page created.
external: false
block_external_search_index: false

# The url slug for the event landing page. If this is an external
# event, use the external URL as the value here.
url_slug: automating-docker-image-builds-using-pulumi

# The event type (workshop, webinar, talk).
event_type: workshop

# URL for embedding a URL for ungated events.
youtube_url:

# Sortable date. The datetime Hugo will use to sort the events in date order.
sortable_date: 2024-06-25T09:00:00.000-07:00

# Duration of the event.
duration: 90 minutes

# "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
location: virtual

# Description of the event.
description: |
    In this workshop, you will learn how to automate your Docker build process by leveraging the Pulumi Docker Build provider and Docker Build Cloud. You will use TypeScript to define your infrastructure as code (IaC), including the configuration of Docker builds. Additionally, you will set up a Docker Build Cloud to use external caching to reduce the time required for builds significantly.

learn:
    - How to create and configure a Docker Build Cloud (DBC) builder
    - How to create a Pulumi program in TypeScript to define IaC
    - How to build NGINX Dockerfile in Pulumi and DBC

# The event presenters
presenters:
    - name: Michael Irwin
      role: Senior Manager, Developer Relations, Docker
      photo: /images/people/michael-irwin.jpg

# case-sensitive
tags:
    level: Intermediate # Beginner, Intermediate, Advanced
    topics: ["Docker"]
    languages: ["TypeScript"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 64754c08-8bf2-427d-8ded-eac9214c64af
    salesforce_campaign_id: 701PQ00000CsD30YAF
---