---
# Name of the event, <= 60 characters
title: Getting started with Kubernetes on AKS with Pulumi
meta_desc: Learn the fundamentals of building and deploying containerized workloads and get an introduction to Pulumi's IaC platform and deployment on Azure.
meta_image: /images/resources/kubernetes-aks-azure-engin.png
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
url_slug: getting-started-with-kubernetes-aks

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Getting started with Kubernetes on AKS with Pulumi

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url:

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2024-03-26T09:00:00.000-07:00

    # Duration of the webinar.
    duration: 90 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        Getting started with Kubernetes doesn't have to be complex! Pulumi's infrastructure-as-code (IaC) platform can help remove the complexity and enable even beginner developers to use any programming language to provision modern infrastructure. In this session, you will learn the fundamentals of building and deploying containerized workloads and get an introduction to Pulumi's IaC platform and deployment on Azure.

        We’ll guide you through setting up an Azure AKS cluster and deploying a containerized workload to the cluster. This workshop is designed to help new users become familiar with the core concepts needed to effectively deploy Kubernetes clusters and workloads on Azure. We will guide you through the Pulumi platform with diagrams and a series of examples to help accelerate your cloud projects.

    # The webinar presenters
    presenters:
        - name: Engin Diri
          role: Sr. Community Engineer, Pulumi
          photo: /images/team/engin-diri.jpg

    # case-sensitive
    tags:
        level: Beginner # Beginner, Intermediate, Advanced
        topics: ["Kubernetes"]
        languages: []
        clouds: ["Azure"]

# The right hand side form section.
form:
    hubspot_form_id: 54cb6dec-96e5-4849-bfdb-21f77a1a8209
    salesforce_campaign_id: 701PQ000007oxyYYAQ
---
