---
# Name of the event, <= 60 characters
title: Getting Started with Kubernetes on Google Cloud
meta_desc: In this workshop, you will learn how to deploy a Kubernetes cluster on Google Cloud and run containerized applications on the cluster.
meta_image: /images/resources/intro-k8s-google-cloud-jay.png

# A featured event will display first in the list.
featured: false

# Events with unlisted as true will not be shown on the event list
unlisted: false

# Gated events will have a registration form and the user will need
# to fill out the form before viewing.
gated: false

# External events will link to an external page instead of an event
# landing/registration page. If the event is external you will need
# set the 'block_external_search_index' flag to true so Google does not index
# the event page created.
external: false
block_external_search_index: false

# The url slug for the event landing page. If this is an external
# event, use the external URL as the value here.
url_slug: kubernetes-on-google-cloud

# The event type (workshop, webinar, talk).
event_type: workshop

# URL for embedding a URL for ungated events.
youtube_url: https://www.youtube.com/embed/eQMDlXB_Zvc?rel=0

# Sortable date. The datetime Hugo will use to sort the events in date order.
sortable_date: 2023-10-05T12:00:00-04:00

# Duration of the event.
duration: 90 minutes

# "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
location: virtual

# Description of the event.
description: |
    In this workshop, you will learn how to deploy a Kubernetes cluster on Google Cloud and run containerized applications on the cluster. The workshop will include a brief introduction to Pulumi, an infrastructure-as-code platform, where you can use familiar programming languages to provision modern cloud infrastructure.
    
    This 200-level workshop is designed to help users who have basic familiarity with Pulumi effectively handle real-world use cases. We will guide you through the process with diagrams and a series of labs to help accelerate your cloud projects.

learn:
    - How to use real programming languages to manage cloud resources in a declarative fashion.
    - How to manage Google Cloud and Kubernetes resources with Pulumi.
    - How Pulumi's provider ecosystem allows you to orchestrate all the resources your cloud-native workloads need with a single tool.

# The event presenters
presenters:
    - name: Josh Kodroff
      role: Sr Solutions Architect, Pulumi
      photo: /images/team/josh-kodroff.jpg
    - name: Jason Smith
      role: Customer Engineer, Google Cloud

# case-sensitive
tags:
    level: Intermediate # Beginner, Intermediate, Advanced
    topics: ["Kubernetes"]
    languages: []
    clouds: ["Google Cloud"]

# The right hand side form section.
form:
  hubspot_form_id: 73602700-1d98-4bfe-921e-826cca5805a1
  salesforce_campaign_id: 701Du000000AupjIAC
---
