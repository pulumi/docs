---
# Name of the webinar.
title: "Deploy Kubernetes and the Kitchen Sink with NGINX and Pulumi"
meta_desc: "In this Live Cast, Elijah Zupancic (NGINX) and Lee Briggs (Pulumi) will introduce a push-button Kubernetes deployment on AWS EKS using Pulumi."

# A featured webinar will display first in the list.
featured: false

# If the video is pre-recorded or live.
pre_recorded: true

# If the video is part of the PulumiTV series. Setting this value to true will list the video in the "PulumiTV" section.
pulumi_tv: false

# The preview image will be shown on the list page.
preview_image: ""

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
url_slug: "nginx-deploy-kubernetes-and-the-kitchen-sink"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Deploy Kubernetes and the Kitchen Sink with NGINX and Pulumi"
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
    title: "Deploy Kubernetes and the Kitchen Sink with NGINX and Pulumi"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/BIbJM9n5XeE"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2021-10-08T11:00:00-07:00
    # Duration of the webinar.
    duration: "1 hour"
    # Datetime of the webinar.
    datetime: ""
    # Description of the webinar.
    description: |
        In this Live Cast, Elijah Zupancic (NGINX) and Lee Briggs (Pulumi) will introduce a push-button Kubernetes deployment on AWS EKS using Pulumi for infrastructure definition. We will delve into some advanced topics such as chaining multiple Pulumi projects together, creating Kubernetes infrastructure as code, building / deploying NGINX Kubernetes Ingress Controller, and application deployments. All topics covered will have corresponding open-source examples that can be borrowed from freely.

        This Live Cast should give you what you need to get started with a production ready Kubernetes cluster with NGINX and Pulumi.

    # The webinar presenters
    presenters:
        - name: Lee Briggs
          role: Software Engineer, Pulumi
        - name: Elijah Zupancic
          role: Solution Architect, NGINX

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - Kubernetes Infrastructure as code
        - Push-button Kubernetes deployments
        - Application deployments

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: "ab9fb33f-1859-4386-ac28-69438606b9fb"
---
