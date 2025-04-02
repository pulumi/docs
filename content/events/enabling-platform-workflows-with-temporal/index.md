---
# Name of the event, <= 60 characters
title: Enabling Platform Workflows with Temporal
meta_desc: Unlock Temporal Cloud's full potential with Pulumi. Learn to automate resource management, enhance developer workflows, and build platform engineering solutions
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
url_slug: enabling-platform-workflows-with-temporal

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Enabling Platform Workflows with Temporal
    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: 

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2025-06-24T12:00:00-04:00

    # Duration of the webinar.
    duration: 60 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        Platform Engineering teams are responsible for giving developers clear, repeatable playbooks for orchestrating resilient, scalable applications. When using Temporal Cloud, managing Namespaces, Task Queues, and Worker configurations effectively is crucial to ensuring reliability and performance.
        
        In this workshop, we’ll explore how Pulumi empowers teams to define, provision, and manage Temporal Cloud resources using modern Infrastructure as Code (IaC) practices. You'll learn how to automate resource lifecycles, enforce policies, and integrate Temporal Cloud into platform engineering workflows—ensuring developers have a seamless and self-service experience.

    learn:
        - "IaC for Temporal Cloud: Automate the provisioning and lifecycle management of Temporal Namespaces, Task Queues, and Workers using Pulumi."
        - "Consistency & Compliance: Enforce governance, security, and best practices for Temporal Cloud resources across multiple environments."
        - "Hands-on Automation: Trigger a complex deployment cycle with Pulumi Deployments and create approval steps"


    # The webinar presenters
    presenters:
        - name: Yosef Ejigu
          role: Solutions Engineer, Pulumi, Pulumi
          photo: /images/team/yosef-ejigu.jpg
        - name: Cornelia Davis
          role: Developer Advocate, Temporal
          photo: /images/people/cornelia-davis.jpg

    # case-sensitive
    tags:
        level: Intermediate # Beginner, Intermediate, Advanced
        topics:  ["Temporal", "Platform Engineering"]
        languages: ["TypeScript"]
        clouds: ["AWS"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 45641519-d8a1-4507-8e59-da1847c4b743
    salesforce_campaign_id: 701PQ00000VDHioYAH

event_data:
  name: Enabling Platform Workflows with Temporal
  start_date: 2024-06-24T12:00:00-04:00
  end_date: 2024-06-24T13:00:00-04:00
  url: "https://www.pulumi.com/resources/enabling-platform-workflows-with-temporal/"
  description: |
    Platform Engineering teams are responsible for giving developers clear, repeatable playbooks for orchestrating resilient, scalable applications. When using Temporal Cloud, managing Namespaces, Task Queues, and Worker configurations effectively is crucial to ensuring reliability and performance.
    
    In this workshop, we’ll explore how Pulumi empowers teams to define, provision, and manage Temporal Cloud resources using modern Infrastructure as Code (IaC) practices. You'll learn how to automate resource lifecycles, enforce policies, and integrate Temporal Cloud into platform engineering workflows—ensuring developers have a seamless and self-service experience.
---
