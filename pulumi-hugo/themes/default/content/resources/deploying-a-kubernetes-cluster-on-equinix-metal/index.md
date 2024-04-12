---
# Name of the event, <= 60 characters
title: Deploying a Kubernetes Cluster on Equinix Metal
meta_desc: In this code-centric session, you will learn how to manage Equinix Metal resources using Pulumi and the new Equinix Pulumi provider.
meta_image: /images/resources/kubernetes-cluster-equinix-metal-oscar.png

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
url_slug: deploying-a-kubernetes-cluster-on-equinix-metal

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Deploying a Kubernetes Cluster on Equinix Metal

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: https://www.youtube.com/embed/a5iEQteKgHU?rel=0

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2023-09-13T09:00:00-04:00

    # Duration of the webinar.
    duration: 1 hour

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        In this code-centric session, you will learn how to manage Equinix Metal resources using Pulumi and the new Equinix Pulumi provider. We'll teach you the basics of how Pulumi works and demonstrate deploying a Kubernetes cluster and workload on Equinix Metal.

    learn:
        - How to provision a Kubernetes cluster on Equinix Metal
        - Defining and deploying Equinix resources using popular programming languages
        - How to use Pulumi and Equinix together

    # The webinar presenters
    presenters:
        - name: Josh Kodroff
          role: Senior Solutions Architect, Pulumi
          photo: /images/team/josh-kodroff.jpg
        - name: Oscar Cobles
          role: Integrations Engineer, Equinix

    # case-sensitive
    tags:
        level: Beginner # Beginner, Intermediate, Advanced
        topics: ["Kubernetes"]
        languages: []
        clouds: ["Equinix"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 97b4a73f-c4d4-440c-b24e-2c04fd34d62a
    salesforce_campaign_id: 701Du000000AXEtIAO
---
