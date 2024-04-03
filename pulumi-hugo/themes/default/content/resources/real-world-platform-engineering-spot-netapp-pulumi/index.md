---
# Name of the event, <= 60 characters
title: Microsoft AKS Engineering at Scale with Spot and Pulumi
meta_desc: Explore real-world examples of how organizations can leverage the power of Pulumi and Spot to optimize their AKS workloads.
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
url_slug: real-world-platform-engineering-spot-netapp-pulumi

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Microsoft AKS Engineering at Scale with Spot and Pulumi

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url:

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2024-04-10T09:00:00.000-07:00

    # Duration of the webinar.
    duration: 90 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        As the rush to the cloud continues, businesses need to run at the speed of innovation. This means a well-defined and efficient platform engineering approach becomes essential while balancing your cloud infrastructure’s security, compliance, and scalability.

        In this webinar, presented by Spot by NetApp and Pulumi, we will explore real-world examples of how organizations can leverage the power of Pulumi and Spot to optimize their AKS workloads at launch and why continuous optimization of your AKS infrastructure is a critical part of any successful platform engineering program. Our experts will discuss best practices for managing AKS at scale and how you can simultaneously increase time-to-market and developer productivity.

    learn:
        - What Spot is and how to use it in Azure.
        - How Spot ensures security and compliance while scaling.
        - How Pulumi and Spot facilitates AKS usage at enterprise scale.

    # The webinar presenters
    presenters:
        - name: Engin Diri
          role: Sr. Community Engineer, Pulumi
          photo: /images/team/engin-diri.jpg
        - name: Shon Harris
          role: Developer Relations Lead, NetApp
          photo: /images/people/shon-harris.jpg

    # case-sensitive
    tags:
        level: Beginner # Beginner, Intermediate, Advanced
        topics: ["Azure", "AKS", "Platform Engineering", "Spot by NetApp"]
        languages: []

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 99bdfd5c-c36c-4be7-b45a-75b1cf490c45
    salesforce_campaign_id: 701PQ000008YkQlYAK
---
