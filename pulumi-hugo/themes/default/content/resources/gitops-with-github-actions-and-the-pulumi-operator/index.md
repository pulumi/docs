---
# Name of the webinar.
title: "GitOps with GitHub Actions and the Pulumi Operator"
meta_desc: "In this workshop you will learn how to implement powerful Github Action workflows using Pulumi and the Pulumi Kubernetes Operator."

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
url_slug: "gitops-with-github-actions-and-the-pulumi-operator"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "GitOps with GitHub Actions and the Pulumi Operator"
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
    title: "GitOps with GitHub Actions and the Pulumi Operator"
    # URL for embedding a URL for ungated webinars.
    youtube_url: ""
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2022-06-21T09:00:00-07:00
    # Duration of the webinar.
    duration: "1 hour"
    # Datetime of the webinar.
    datetime: ""
    # Description of the webinar.
    description: |
        The Pulumi Kubernetes Operator enables Kubernetes users to create a Pulumi Stack as a first-class Kubernetes API resource, and use the StackController to drive updates. Combining GitHub Actions with the Pulumi Kubernetes Operator helps you to implement powerful GitOps workflows and automation for both your infrastructure and workloads.

    # The webinar presenters
    presenters:
        - name: David Flanagan
          role: Staff Developer Advocate, Pulumi
        - name: Rizel Scarlett
          role: Developer Advocate, Github

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - How to stand up a Kubernetes cluster the easy way with Pulumi
        - Configuring automation steps with GitHub Actions
        - Deploying a workload into your cluster using the Pulumi Kubernetes Operator

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: "72d36924-efc8-4e3b-a9ac-4cfe584da3a7"
---
