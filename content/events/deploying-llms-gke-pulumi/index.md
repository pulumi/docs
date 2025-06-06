---
# Name of the event, <= 60 characters
title: Deploying LLMs on GKE with NVIDIA GPUs & Google Cloud
meta_desc: Deploy a Mixtral 8x7B LLM on GKE with NVIDIA GPUs using Pulumi and Python. Learn to build scalable, GPU-enabled AI workloads on Google Cloud.
meta_image: llms-google-cloud-nvidia-kubernetes.png

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
    title: Deploying LLMs on GKE with NVIDIA GPUs & Google Cloud

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: https://www.youtube.com/embed/HIjbgpTDCm4?si=DthqWSbcWG52onMY

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2024-07-31T09:00:00-07:00

    # Duration of the webinar.
    duration: 90 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        Join us for a hands-on workshop where we’ll walk through deploying a large language model (LLM) on Google Kubernetes Engine (GKE) using NVIDIA GPUs and Pulumi’s modern Infrastructure as Code platform.

        You’ll follow along as we deploy the open-weight Mixtral 8x7B model using Hugging Face’s Text Generation Inference and GKE’s powerful GPU-backed workloads. Learn how to provision GKE clusters with NVIDIA L4 GPUs, containerize AI models, and orchestrate everything with Pulumi and Python—all while leveraging Google Cloud's scalable infrastructure.

        Whether you're building your own AI workloads or curious about how to manage LLMs in production-ready environments, this workshop will give you practical, real-world experience from two cloud and DevOps experts—featuring guest speaker Jason Smith from Google Cloud.

    learn:
        - How to configure Google Cloud for scalable AI workloads
        - Deploying infrastructure with Pulumi in Python
        - Managing GPU-enabled Kubernetes clusters
        - Serving and testing LLMs on GKE with Hugging Face Inference

    # The webinar presenters
    presenters:
        - name: Engin Diri
          role: Sr. Solutions Architect, Pulumi
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
