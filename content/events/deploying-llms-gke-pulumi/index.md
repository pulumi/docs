---
# Name of the event, <= 60 characters
title: Deploying LLMs on GKE with Pulumi
meta_desc: This workshop is for devs, DevOps engineers, and AI practitioners, providing tools and knowledge to integrate machine learning with cloud-native infrastructure.
meta_image:

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
url_slug: deploying-llms-gke-pulumi

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Deploying LLMs on GKE with Pulumi

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: 

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2024-07-31T09:00:00-07:00

    # Duration of the webinar.
    duration: 90 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        This hands-on workshop guides participants through deploying a Mixtral 8X7B large language model on Google Kubernetes Engine (GKE) using Pulumi for infrastructure as code. Attendees will learn to leverage NVIDIA L4 GPUs on GKE to serve advanced AI models efficiently. The session covers setting up the Google Cloud environment, deploying a Pulumi-based GKE cluster, and containerizing the model using Hugging Face’s text generation inference.

    learn:
        - Configuring GCP for AI workloads
        - Using Pulumi with Python for infrastructure deployment
        - Managing GPU-enabled Kubernetes clusters
        - Serving and testing large language models on GKE

    # The webinar presenters
    presenters:
        - name: Engin Diri
          role: Customer Experience Architect, Pulumi
          photo: /images/team/engin-diri.jpg
        - name: Jason Smith
          role: Sr. Cloud Customer Engineer, Google
          photo: /images/team/jay-smith-google-jpeg.jpg

    # case-sensitive
    tags:
        level: Intermediate # Beginner, Intermediate, Advanced
        topics: ["Kubernetes", "AI"]
        languages: ["Python"]
        clouds: ["Google Cloud"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 7b52eed2-52b9-43da-87bd-b2c601bb48d2
    salesforce_campaign_id: 701PQ00000GVJA2YAP
---
