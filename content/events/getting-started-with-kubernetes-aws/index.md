---
# Name of the event, <= 60 characters
title: Getting Started with Kubernetes on AWS using Pulumi
meta_desc: In this workshop, you will learn the fundamentals of setting up EKS clusters on AWS through guided exercises using Pulumi.
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
url_slug: getting-started-with-kubernetes-aws

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Getting Started with Kubernetes on AWS using Pulumi

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: 

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2024-09-11T09:00:00.000-07:00

    # Duration of the webinar.
    duration: 90 minutes
    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        In this session, you will learn the fundamentals of building and deploying containerized workloads and get an introduction to Pulumi’s IaC platform and deployment on AWS.

        We’ll guide you through setting up an Amazon EKS cluster on AWS and deploying a containerized workload to the cluster.

        This workshop is designed to help new users become familiar with the core concepts needed to effectively deploy Kubernetes clusters and workloads on AWS. We will guide you through the Pulumi platform with diagrams and a series of examples to help accelerate your cloud projects.

    learn:
        - The basics of writing Pulumi programs to manage infrastructure using real programming languages
        - How to create and manage EKS clusters in AWS with Pulumi
        - Deploying new workloads to your cluster

    # The webinar presenters
    presenters:
        - name: Marina Novikova
          role: Sr. Partner Solution Architect, AWS
          photo: /images/team/marina-novikova.jpg        

    # case-sensitive
    tags:
        level: Beginner # Beginner, Intermediate, Advanced
        topics: ["Kubernetes"]
        languages: []
        clouds: ["AWS"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 2a8c274a-cf81-430b-a56b-3bb167b2af58
    salesforce_campaign_id: 701PQ00000HVrmUYAT
---
