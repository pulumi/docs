---
# Name of the event, <= 60 characters
title: Streamlining AI/ML Workflows on GKE with Pulumi
meta_desc: Learn to harness the capabilities of GPUs and TPUs effortlessly, empowering data scientists to focus on model development rather than infrastructure management.
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
url_slug: streamlining-ai-ml-gke-pulumi

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Streamlining AI/ML Workflows on GKE with Pulumi

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url:

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2024-03-28T09:00:00.000-07:00

    # Duration of the webinar.
    duration: 90 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        One of the most popular ways to train and serve models is to do AI/ML on Kubernetes. However, data scientists typically don't do double duty as platform managers. Standing up a Kubernetes environment can be a challenge for data scientists but most data scientists know Python. We will demonstrate how with Pulumi you can deploy a machine learning platform on GKE and leverage the power of GPUs and TPUs

    learn:
        - How to deploy a machine learning platform on GKE using Pulumi, eliminating the challenges of Kubernetes management.
        - How to harness the computational power of GPUs and TPUs seamlessly within your AI/ML workflows.

    # The webinar presenters
    presenters:
        - name: Josh Kodroff
          role: Sr Solutions Architect, Pulumi
          photo: /images/team/josh-kodroff.jpg
        - name: Jason Smith
          role: Sr Cloud Customer Engineer, Google

    # case-sensitive
    tags:
        level: Intermediate # Beginner, Intermediate, Advanced
        topics: ["AI", "Kubernetes"]
        languages: ["Python"]

# The right hand side form section.
form:
    hubspot_form_id: 71503050-8ca0-4e76-bb92-5d35d08636a0
    salesforce_campaign_id: 701PQ000007ohFTYAY
---