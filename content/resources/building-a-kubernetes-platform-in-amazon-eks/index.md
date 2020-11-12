---
# Name of the webinar.
title: "Building a Kubernetes Platform in Amazon EKS with Pulumi"
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
    title: "Cloud Engineering Concepts: Building a Kubernetes platform in Amazon EKS with Pulumi"
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
    title: "Cloud Engineering Concepts: Building a Kubernetes platform in Amazon EKS with Pulumi"
    # URL for embedding a URL for ungated webinars.
    youtube_url: ""
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2020-12-10T17:00:00-07:00
    # Duration of the webinar.
    duration: "2 hours"
    # Datetime of the webinar.
    datetime: ""
    # Description of the webinar.
    description: |
        In this workshop, we’ll examine how Pulumi interacts with Kubernetes, and show real-world examples of managing Amazon EKS clusters. We’ll focus on building a user-friendly Kubernetes platform, installing software that makes Kubernetes easy to use for application developers.

        Attendees will be guided through the process of provisioning an Amazon EKS cluster and installing platform friendly software such as cert-manager and external-dns.

        **Target Audience**

        Active Pulumi users, and users considering or actively building a Kubernetes platform
        **Prerequisites**

        Attendees should be familiar with Pulumi and have the Pulumi CLI installed on their machine.
        Attendees should have access to an AWS account, temporary AWS accounts will be provided to users on a first come, first served basis.

    # The webinar presenters
    presenters:
        - name: Lee Briggs
          role: Community Engineer, Pulumi
        - name: Yaniv Bossem
          role: Partner Solutions Architect, DevOps at Amazon Web Services (AWS)

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - How-to provision a production-ready Amazon EKS cluster with key features enabled using Pulumi
        - Provisioning the aws-load-balancer-controller to automate ingress creation
        - How to provision the external-dns add-on to automate DNS entry for Ingress resources
        - How to install cert-manager to automate the creation of TLS certificates for applications
        - Install an example application to show the end-to-end user experience for users.

# The right hand side form section.
form:
    # GoToWebinar webinar key. This key allows us to register people for webinars via the
    # HubSpot form.
    gotowebinar_key: ""

    # HubSpot form id.
    hubspot_form_id: "3ca277f5-deaa-40c1-8dcf-7ebc40f99f1a"
---
