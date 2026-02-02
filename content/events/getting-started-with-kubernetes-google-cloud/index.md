---
# Name of the event, <= 60 characters
title: Getting Started with Kubernetes on Google Cloud
meta_desc: Learn how Kubernetes runs on Google Cloud using GKE. Learn to create clusters, deploy applications, and manage Kubernetes infrastructure with Pulumi.
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
url_slug: getting-started-with-kubernetes-google-cloud

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Getting Started with Kubernetes on Google Cloud
    event_type: workshop # workshop | event
    
    # URL for embedding a URL for ungated webinars.
    youtube_url:

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2026-05-13T09:00:00.000-07:00

    # Duration of the webinar.
    duration: 60 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        Getting started with Kubernetes on Google Cloud doesn’t have to be complex. This workshop introduces the fundamentals of running Kubernetes using Google Kubernetes Engine (GKE) and shows how Pulumi can be used to define and manage Kubernetes and cloud infrastructure in code.
        
        You’ll be guided through creating a GKE cluster and deploying a containerized application, using diagrams and hands-on exercises to reinforce core Kubernetes concepts. The focus is on practical, beginner-friendly workflows that help you understand how Kubernetes works on Google Cloud before moving on to more advanced topics.
    learn:
        - Create a Google Kubernetes Engine (GKE) cluster
        - Build reusable infrastructure components that scale across teams and projects
        - Deploy and update containerized applications using safe, repeatable workflows
        - Understand the lifecycle of Kubernetes infrastructure on Google Cloud
    
    # The webinar presenters
    presenters:
        - name: Adam Gordon Bell
          role: Community Engineer, Pulumi
          photo: /images/team/adam-gordon-bell.jpg

    # case-sensitive
    tags:
        level: Beginner # Beginner, Intermediate, Advanced
        topics: ["Kubernetes", "Google Kubernetes Engine (GKE)", "Automation"]
        languages: [Any]
        clouds: ["Google Cloud"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 9abcfddf-7663-442c-b13d-cfae10a7e0d9
    salesforce_campaign_id: 701Du0000009z7LIAQ

event_data:
  name: "Getting Started with Kubernetes on Google Cloud"
  start_date: 2026-05-13T09:00:00.000-07:00
  end_date: 2026-05-13T10:00:00.000-07:00
  url: "https://www.pulumi.com/events/getting-started-with-kubernetes-google-cloud/"
  description: |
    Getting started with Kubernetes on Google Cloud doesn’t have to be complex. This workshop introduces the fundamentals of running Kubernetes using Google Kubernetes Engine (GKE) and shows how Pulumi can be used to define and manage Kubernetes and cloud infrastructure in code.
---
