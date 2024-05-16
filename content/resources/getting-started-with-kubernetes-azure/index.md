---
# Name of the event, <= 60 characters
title: Getting Started with Kubernetes on Azure
meta_desc: In this workshop, you will learn how to deploy a Kubernetes cluster on Microsoft Azure and run containerized applications on the cluster.
meta_image:

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
url_slug: getting-started-with-kubernetes-azure

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Getting Started with Kubernetes on Azure

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: https://www.youtube.com/embed/qBoRBDZRkDk?rel=0

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2023-04-25T12:00:00.000Z

    # Duration of the webinar.
    duration: 90 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        In this workshop, you will learn how to deploy a Kubernetes cluster on Microsoft Azure and run containerized applications on the cluster. The workshop will include a brief introduction to Pulumi, an infrastructure-as-code platform, where you can use familiar programming languages to provision modern cloud infrastructure.
        
        This 200-level workshop is designed to help users who have basic familiarity with Pulumi effectively handle real-world use cases. We will guide you through the process with diagrams and a series of labs to help accelerate your cloud projects.

    # The webinar presenters
    presenters:
        - name: Josh Kodroff
          role: Senior Solutions Architect, Pulumi
          photo: /images/team/josh-kodroff.jpg
        - name: April Edwards
          role: Senior Enterprise Advocate, GitHub

    # case-sensitive
    tags:
        level: Intermediate # Beginner, Intermediate, Advanced
        topics: ["Kubernetes"]
        languages: []
        clouds: ["Azure"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 81a49dce-f5b7-4277-a9ca-98bbaa5df6cb
    salesforce_campaign_id: 701Du0000009z7QIAQ
---
