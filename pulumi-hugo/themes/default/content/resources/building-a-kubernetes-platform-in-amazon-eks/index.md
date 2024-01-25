---
# Name of the webinar.
title: "Building a Kubernetes Platform in AWS EKS with Pulumi"
meta_desc: "In this workshop, you will examine how Pulumi interacts with Kubernetes, and build real-world examples of managing Amazon EKS clusters."

# A featured webinar will display first in the list.
featured: false

# If the video is pre-recorded or live.
pre_recorded: false

# If the video is part of the PulumiTV series. Setting this value to true will list the video in the "PulumiTV" section.
pulumi_tv: false

# The preview image will be shown on the list page.
preview_image: ""

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
url_slug: "building-a-kubernetes-platform-in-amazon-eks"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Building a Kubernetes Platform in AWS EKS with Pulumi"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Webinar pages support multiple session via the 'multiple' property.
# multiple:
#   - datetime: 2020-02-05T10:00:00-07:00
#     hubspot_form_id: ""
#     gotowebinar_key: ""

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Building a Kubernetes Platform in AWS EKS with Pulumi"
    # URL for embedding a URL for ungated webinars.
    youtube_url: # "https://www.youtube.com/embed/emUSsZDcu6E"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2024-04-03T09:00:00-07:00
    # Duration of the webinar.
    duration: "90 minutes"
    # Datetime of the webinar.
    datetime: ""
    # Description of the webinar.
    description: |
        In this workshop, we’ll examine how Pulumi interacts with Kubernetes, and show real-world examples of managing Amazon EKS clusters. We’ll focus on building a user-friendly Kubernetes platform, installing software that makes Kubernetes easy to use for application developers.

        Attendees will be guided through the process of provisioning an Amazon EKS cluster and installing platform friendly software such as cert-manager and external-dns.

    # The webinar presenters
    presenters:
        - name: Josh Kodroff
          role: Sr. Solutions Architect, Pulumi
        - name: Carlos Santana
          role: Cloud Solutions Architect, AWS

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - How-to provision a production-ready Amazon EKS cluster with key features enabled using Pulumi
        - Provisioning the aws-load-balancer-controller to automate ingress creation
        - Install an example application to show the end-to-end user experience for users.
form:
    hubspot_form_id: ca697654-48d5-4809-ade2-757fa53679b4
    salesforce_campaign_id: 701PQ0000068BVtYAM
---
