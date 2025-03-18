---
# Name of the event, <= 60 characters
title: "From Zero to Production: Kubernetes on AWS"
meta_desc: Learn how to manage Kubernetes on AWS with infrastructure as code. Simplify deployments, automate workloads, and integrate cloud services efficiently.
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
url_slug: kubernetes-on-aws

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "From Zero to Production: Kubernetes on AWS"

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: 

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2025-03-26T10:00:00+11:00

    # Duration of the webinar.
    duration: 90 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        Kubernetes has become the industry standard for container orchestration, offering scalability and flexibility for cloud-native applications. However, managing Kubernetes—especially across cloud environments—can be complex and time-consuming.

        In this workshop, you'll learn how to simplify Kubernetes management on AWS using infrastructure as code. By leveraging a modern approach, you can define and deploy Kubernetes resources programmatically, reduce reliance on YAML configurations, and integrate cloud services seamlessly.

        Through hands-on exercises, we’ll demonstrate how to provision, configure, and maintain Kubernetes clusters and containerized applications with efficiency and reliability.

    learn:
        - How to manage Kubernetes workloads on AWS using infrastructure as code.
        - How to deploy and orchestrate containers with Kubernetes and Docker providers in a single workflow.
        - How to integrate Kubernetes IaC with existing YAML manifests, Helm charts, and cloud services.
        - How to implement GitOps workflows with the Kubernetes Operator for automated deployments.

    # The webinar presenters
    presenters:
        - name: Laci Videmsky
          role: Solutions Architect, Pulumi
          photo: /images/team/laci-videmsky.png
        - name: Aurélien Requiem
          role: Customer Engineer, Pulumi
          photo: /images/team/aurelien-requiem.jpg
        - name: Abdul Javed
          role: Regional GTM Leader (APAC), Pulumi
          photo: /images/team/abdul-javed.jpg

    # case-sensitive
    tags:
        level: Intermediate # Beginner, Intermediate, Advanced
        topics: ["Platform Engineering", "DevOps", "Automation"]
        languages: []
        clouds: []

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 54e1bff7-1645-4c25-8ea8-8e61902e3aa5
    salesforce_campaign_id: 701PQ00000TEL7CYAX

event_data:
  name: "Kubernetes on AWS: Streamlining Deployments with Pulumi IaC"
  start_date: 2025-03-26T10:00:00+10:00
  end_date: 2025-03-26T11:00:00+10:00
  url: "https://www.pulumi.com/events/kubernetes-on-aws/"
  description: |
        Kubernetes has become the industry standard for container orchestration, offering scalability and flexibility for cloud-native applications. However, managing Kubernetes—especially across cloud environments—can be complex and time-consuming.

        In this workshop, you'll learn how to simplify Kubernetes management on AWS using infrastructure as code. By leveraging a modern approach, you can define and deploy Kubernetes resources programmatically, reduce reliance on YAML configurations, and integrate cloud services seamlessly.

        Through hands-on exercises, we’ll demonstrate how to provision, configure, and maintain Kubernetes clusters and containerized applications with efficiency and reliability.
---
