---
# Name of the event, <= 60 characters
title: Enabling Platform Workflows with Pulumi and Docker
meta_desc: Learn how Pulumi and Docker Build Cloud can enable teams to deliver containerized workloads faster than ever.
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
url_slug: enabling-platform-workflows-with-pulumi-and-docker

# The event type (workshop, webinar, talk).
event_type: workshop

# URL for embedding a URL for ungated events.
youtube_url: 

# Sortable date. The datetime Hugo will use to sort the events in date order.
sortable_date: 2025-05-21T12:00:00-04:00

# Duration of the event.
duration: 60 minutes

# "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
location: virtual

# Description of the event.
description: |
    Modern workloads require frequent container builds and deployments, but traditional build processes can be slow and resource-intensive, creating bottlenecks in your delivery pipeline. Docker Build Cloud offers distributed, cached builds that can dramatically reduce build times, while Pulumi provides the orchestration layer to automate your entire deployment workflow using familiar programming languages.

    In this hands-on workshop, you'll learn how to integrate Docker Build Cloud with Pulumi to create a streamlined container build and deployment pipeline. We'll demonstrate how to leverage Docker Build Cloud's distributed architecture and layer caching to accelerate builds, while using Pulumi to automate the end-to-end process from foundational infrastructure to container build to production deployment.

learn:
    - How to configure Docker Build Cloud and integrate it with your existing container build pipeline.
    - Techniques for optimizing container builds with intelligent caching and distributed processing.
    - Best practices for automating container deployments using Pulumi's infrastructure as code.

# The event presenters
presenters:
    - name: Josh Kodroff
      role: Principal Customer Success Architect, Pulumi
      photo: /images/team/josh-kodroff.jpg
    - name: Nelson Espinal
      role: Global Solutions Engineer - Strategic Alliances, Docker

# case-sensitive
tags:
    level: Intermediate # Beginner, Intermediate, Advanced
    topics:  ["Docker", "Containers", "Platform Engineering"]
    languages: ["TypeScript"]
    clouds: ["AWS"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: f1a54d48-f0d7-4bda-ab85-61781d55dfb2
    salesforce_campaign_id: 701PQ00000VDMc0YAH

---
