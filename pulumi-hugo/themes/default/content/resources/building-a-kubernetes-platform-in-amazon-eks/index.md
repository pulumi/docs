---
# Name of the event, <= 60 characters
title: Building a Kubernetes Platform in AWS EKS with Pulumi
meta_desc: In this workshop, you will examine how Pulumi interacts with Kubernetes, and build real-world examples of managing Amazon EKS clusters.
meta_image: /images/resources/kubernetes-platform-amazon-eks-josh-carlos.png

# A featured webinar will display first in the list.
featured: false

# Webinars with unlisted as true will not be shown on the webinar list
unlisted: true

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
url_slug: building-a-kubernetes-platform-in-amazon-eks

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Building a Kubernetes Platform in AWS EKS with Pulumi

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    #youtube_url:

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2024-03-25T09:00:00-07:00

    # Duration of the webinar.
    duration: 90 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        In this workshop, we’ll examine how Pulumi interacts with Kubernetes, and show real-world examples of managing Amazon EKS clusters. We’ll focus on building a user-friendly Kubernetes platform, installing software that makes Kubernetes easy to use for application developers.

        Attendees will be guided through the process of provisioning an Amazon EKS cluster and installing platform friendly software such as cert-manager and external-dns.

    learn:
        - How-to provision a production-ready Amazon EKS cluster with key features enabled using Pulumi
        - Provisioning the aws-load-balancer-controller to automate ingress creation
        - Install an example application to show the end-to-end user experience for users.

    # The webinar presenters
    presenters:
      - name: Josh Kodroff
        role: Sr. Solutions Architect, Pulumi
        photo: /images/team/josh-kodroff.jpg
      - name: Carlos Santana
        role: Cloud Solutions Architect, AWS

    # case-sensitive
    tags:
        level: Intermediate # Beginner, Intermediate, Advanced
        topics: ["Kubernetes", "EKS"]
        languages: []

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: ca697654-48d5-4809-ade2-757fa53679b4
    salesforce_campaign_id: 701PQ0000068BVtYAM
---
