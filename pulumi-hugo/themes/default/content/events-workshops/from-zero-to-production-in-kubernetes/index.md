---
# Name of the webinar.
title: "From Zero to Production in Kubernetes"
meta_desc: "Join Damian Curry & Elijah Zupancic and go from zero to production on Kubernetes by using Python to build abstractions that make getting to production easier."

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
url_slug: "from-zero-to-production-in-kubernetes"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "From Zero to Production in Kubernetes"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "From Zero to Production in Kubernetes"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/L-8uzn6AdHM"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2021-10-21T14:00:00-07:00
    # Duration of the webinar.
    duration: "1.5 hour"
    # Datetime of the webinar.
    datetime: "OCTOBER 21st, 2021"
    # Description of the webinar.
    description: |
        Setting up your production Kubernetes environment brings many benefits including scalability and portability for your applications. Before you reach production, It’s important to understand key Kubernetes concepts and architectures available to keep your clusters secure and scalable. Ingress controllers are vital parts of any Kubernetes platform and NGINX ingress controller provides the best in class traffic management solution for cloud native apps and containerized environments.

        It’s important to use repeatable mechanisms to handle your ingress objects and controller deployments. Adopting infrastructure as code provides a mechanism to easily deploy production-ready applications in a repeatable manner. In this livestream, we’ll explore how to leverage the power of Python with Pulumi, an infrastructure as code platform to define and manage your Kubernetes deployments and build powerful abstractions that make getting to production easier than ever before.

    # The webinar presenters
    presenters:
        - name: Damian Curry
          role: Business Development Technical Director, NGINX
        - name: Elijah Zupancic
          role: Solutions Architect, NGINX

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - How to stand up Kubernetes including Amazon VPC, Amazon EKS and other dependencies.
        - Setting up your ingress controller.
        - Deploying an app to your cluster.

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: e6b5082c-2ca8-43b7-96fb-6d19a331d554
aliases:
  - /resources/from-zero-to-production-in-kubernetes
---
