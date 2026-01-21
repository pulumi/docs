---
# Name of the event, <= 60 characters
title: "Zero to Production in Kubernetes"
meta_desc: Learn to deploy and manage Kubernetes clusters from zero to production with multi-cloud automation, GitOps using Argo CD, and agentic workflows.
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
url_slug: from-zero-to-production-in-kubernetes

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Zero to Production in Kubernetes"
    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url:

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2026-03-31T09:00:00-04:00

    # Duration of the webinar.
    duration: 60 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        According to the **CNCF Annual Survey, 93% of organizations** are using, piloting, or evaluating Kubernetes as their core platform for modern cloud infrastructure. Engineering teams adopt Kubernetes for its consistency, scalability, and cloud-agnostic flexibility, making it the standard for building and operating developer platforms.
        
        In this **hands-on Kubernetes workshop**, you will learn how to take clusters and workloads from zero to production using infrastructure as code, **GitOps automation**, and modern strategies for visibility and resilience. You will also explore how **agentic workflows** and AI-assisted infrastructure are reshaping the way teams manage Kubernetes at scale.
    learn:
        - Deploy production-ready applications in a repeatable and automated way
        - Manage Kubernetes fleets using GitOps workflows
        - Improve cluster and workload observability across environments

    # The webinar presenters
    presenters:
        - name: Engin Diri
          role: Senior Solutions Architect, Pulumi
          photo: /images/team/engin-diri.jpg

    # case-sensitive
    tags:
        level: Beginner # Beginner, Intermediate, Advanced
        topics:  ["Kubernetes", "GitOps", "DevOps", "Pulumi Neo"]
        languages: ["Any"]
        clouds: ["AWS"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 510e62c5-8e2e-4e88-89f5-4853bff9e567
    salesforce_campaign_id: 701PQ00000eePWvYAM

event_data:
  name: "Agentic Workflows for Production-ready Kubernetes"
  start_date: 2026-03-31T09:00:00-04:00
  end_date: 2026-03-31T10:00:00-04:00
  url: "https://www.pulumi.com/resources/from-zero-to-production-in-kubernetes/"
  description: |
    According to the CNCF Annual Survey, 93% of organizations use or are evaluating Kubernetes as the foundation of their modern cloud infrastructure. In this hands-on Kubernetes workshop, you will learn how to take clusters and workloads from zero to production, manage Kubernetes fleets using GitOps workflows, and improve cluster and workload observability across environments.
---
