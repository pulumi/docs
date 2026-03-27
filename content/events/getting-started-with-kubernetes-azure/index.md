---
# Name of the event, <= 60 characters
title: Getting Started with Kubernetes on Azure
meta_desc: Learn how Kubernetes runs on Azure using AKS. Create clusters, deploy containerized apps, and manage infrastructure with Pulumi.
meta_image: /events/getting-started-with-kubernetes-azure/intro-azure-aks-adam.png

# A featured event will display first in the list.
featured: false

# Events with unlisted as true will not be shown on the event list
unlisted: false

# Gated events will have a registration form and the user will need
# to fill out the form before viewing.
gated: true

# External events will link to an external page instead of an event
# landing/registration page. If the event is external you will need
# set the 'block_external_search_index' flag to true so Google does not index
# the event page created.
external: false
block_external_search_index: false

# The url slug for the event landing page. If this is an external
# event, use the external URL as the value here.
url_slug: getting-started-with-kubernetes-azure

# The event type (workshop, webinar, talk).
event_type: workshop

# URL for embedding a URL for ungated events.
youtube_url:

# Sortable date. The datetime Hugo will use to sort the events in date order.
sortable_date: 2026-06-10T09:00:00.000-07:00

# Duration of the event.
duration: 60 minutes

# "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
location: virtual

# Description of the event.
description: |
    This workshop introduces the fundamentals of running Kubernetes on Azure using Azure Kubernetes Service (AKS). You’ll learn how Kubernetes fits into the Azure platform and how clusters and containerized workloads are created and managed.

    Through guided exercises, you’ll create an AKS cluster and deploy a containerized application using Pulumi to define infrastructure in code. The focus is on practical workflows that help you understand Kubernetes on Azure before moving on to more advanced topics.
learn:
    - Create an Azure Kubernetes Service (AKS) cluster using Pulumi
    - How Pulumi manages Azure and Kubernetes resources together
    - Deploy and update containerized application to AKS using safe, repeatable workflows
    - How to preview, update, and tear down Kubernetes infrastructure safely

# The event presenters
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

---
