---
# Name of the event, <= 60 characters
title: Advanced Secrets Management on Kubernetes
meta_desc: Discover how to securely manage and inject secrets in Kubernetes applications with this hands-on Platform Engineering workshop.
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
url_slug: advanced-secrets-management-kubernetes

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Advanced Secrets Management on Kubernetes

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: 

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2025-04-09T15:00:00+02:00

    # Duration of the webinar.
    duration: 60 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        Secrets management on Kubernetes does not have to be a chore. In this hands-on workshop, you will learn how to secure and inject secrets into Kubernetes applications using External Secrets Operator and Secret Store CSI Driver.
        
        We will provision the infrastructure with Pulumi, then walk through retrieving both static and dynamic secrets to demonstrate how each approach can reduce the surface area for secrets injection. By the end of this session, you will have a practical understanding of modern secrets management patterns that keep sensitive data safe and manageable at scale.

    learn:
        - How to automate Kubernetes secrets management with External Secrets Operator and Secret Store CSI Driver, ensuring efficient and consistent configuration
        - Best practices for provisioning cloud infrastructure with Pulumi, including secure secrets handling and policy enforcement
        - Strategies for managing both static and dynamic secrets at scale to reduce risk and streamline secret injection
        - Real-world approaches for implementing modern secrets management patterns that protect sensitive data and support rapid, reliable platform engineering

    # The webinar presenters
    presenters:
        - name: Engin Diri
          role: Senior Solutions Architect, Pulumi
          photo: /images/team/engin-diri.jpg
    # case-sensitive
    tags:
        level: Beginner # Beginner, Intermediate, Advanced
        topics: ["Kubernetes", "Security"]
        languages: ["TypeScript"]
        clouds: ["AWS"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 9f066173-0a8a-478f-b3fd-b6a5fa04456a
    salesforce_campaign_id: 701PQ00000STcZdYAL

event_data:
  name: Advanced Secrets Management on Kubernetes
  start_date: 2025-04-09T15:00:00+02:00
  end_date: 2025-04-09T16:00:00+02:00
  url: "https://www.pulumi.com/resources/advanced-secrets-management-kubernetes/"
  description: |
    Secrets management on Kubernetes does not have to be a chore. In this hands-on workshop, you will learn how to secure and inject secrets into Kubernetes applications using External Secrets Operator and Secret Store CSI Driver. We will provision the infrastructure with Pulumi, then walk through retrieving both static and dynamic secrets to demonstrate how each approach can reduce the surface area for secrets injection. By the end of this session, you will have a practical understanding of modern secrets management patterns that keep sensitive data safe and manageable at scale.
---
