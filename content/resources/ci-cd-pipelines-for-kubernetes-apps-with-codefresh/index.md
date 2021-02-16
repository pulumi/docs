---
# Name of the webinar.
title: "CI/CD Pipelines for Kubernetes Apps with Pulumi & Codefresh"
meta_desc: "In this video we will cover how to set up automated CI/CD pipelines for Kubernetes applications using Pulumi and Codefresh."

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
url_slug: "ci-cd-pipelines-for-kubernetes-apps-with-codefresh"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "CI/CD Pipelines for Kubernetes Apps with Pulumi & Codefresh"
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
    title: "CI/CD Pipelines for Kubernetes Apps with Pulumi & Codefresh"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/c7TUy-0N5OA"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2021-01-21T09:00:00-08:00
    # Duration of the webinar.
    duration: "1 hour"
    # Datetime of the webinar.
    datetime: "January 21st, 2021"
    # Description of the webinar.
    description: |
        Leading cloud engineering organizations are automating infrastructure deployments using Pulumi’s infrastructure as code platform and Codefresh makes it easy to manage infrastructure code as part of your continuous delivery process.

    # The webinar presenters
    presenters:
        - name: Anais Urlichs
          role: Developer Evangelist, Codefresh
        - name: Mitch Gerdisch
          role: Senior Sales Engineer, Pulumi
        - name: Kostis Kapelonis
          role: Developer Advocate, Codefresh
        - name: Praneet Loke
          role: Software Engineer, Pulumi

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - The basics of CI/CD using Codefresh.
        - How to declare cloud resources using Pulumi and your favorite programming languages.
        - How to define a simple pipeline for Kubernetes deployments.
        - Practical tests to ensure infrastructure reliability as part of your pipeline.

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: "3cf3d5a6-7649-44db-835b-4bb242a4b3d7"
---
