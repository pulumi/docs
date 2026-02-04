---
# Name of the event, <= 60 characters
title: Getting Started with Kubernetes on Azure
meta_desc: Learn how Kubernetes runs on Azure using AKS. Create clusters, deploy containerized apps, and manage infrastructure with Pulumi.

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
url_slug: getting-started-with-kubernetes-azure

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Getting Started with Kubernetes on Azure

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url:

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2026-06-10T09:00:00.000-07:00

    # Duration of the webinar.
    duration: 60 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        This workshop introduces the fundamentals of running Kubernetes on Azure using Azure Kubernetes Service (AKS). You’ll learn how Kubernetes fits into the Azure platform and how clusters and containerized workloads are created and managed.

        Through guided exercises, you’ll create an AKS cluster and deploy a containerized application using Pulumi to define infrastructure in code. The focus is on practical workflows that help you understand Kubernetes on Azure before moving on to more advanced topics.
    learn:
        - Create an Azure Kubernetes Service (AKS) cluster using Pulumi
        - How Pulumi manages Azure and Kubernetes resources together
        - Deploy and update containerized application to AKS using safe, repeatable workflows
        - How to preview, update, and tear down Kubernetes infrastructure safely

    # The webinar presenters
    presenters:
        - name: Adam Gordon Bell
          role: Community Engineer, Pulumi
          photo: /images/team/adam-gordon-bell.jpg

    # case-sensitive
    tags:
        level: Beginner # Beginner, Intermediate, Advanced
        topics: ["Kubernetes", "Azure Kubernetes Service (AKS)", "Automation"]
        languages: []
        clouds: ["Azure"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 96796c7d-0213-4112-b895-d475253cafbf
    salesforce_campaign_id: 701PQ00000qES8CYAW

event_data:
  name: "Getting Started with Kubernetes on Azure"
  start_date: 2026-06-10T09:00:00.000-07:00
  end_date: 2026-06-10T10:00:00.000-07:00
  url: "https://www.pulumi.com/events/getting-started-with-kubernetes-azure/"
  description: |
    Learn how Kubernetes runs on Azure using AKS. Create clusters, deploy containerized apps, and manage infrastructure with Pulumi.
---
