---
# Name of the event, <= 60 characters
title: "Serverless Java Production: Resilience & Optimization in GCP"
meta_desc: Join this workshop for direct Google advice on serverless architecture, delivered with the power and convenience of Pulumi’s cloud orchestration platform.
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
url_slug: serverless-java-production-resilience-and-optimization-gcp

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Serverless Java Production: Resilience & Optimization in GCP"

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url:

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2024-04-15T09:00:00.000-07:00

    # Duration of the webinar.
    duration: 90 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        Get your next Google Cloud Serverless Java application production ready and add optimizations tuned for the most scalability and performance. Learn to balance cost, latency, and resources to design and implement JIT, AOT Native, and even touch on CRaC and Project Leyden scenarios. Join this workshop for direct Google advice on serverless architecture, delivered with the power and convenience of Pulumi’s cloud orchestration platform.

        In this workshop, you will first be introduced to Pulumi, an infrastructure as code platform, where you can use familiar programming languages to provision modern cloud infrastructure. Following the introduction, attendees will learn about multi-service app delivery on Google Cloud’s serverless platforms, including components such as Postgres, Firestore, and Backend-for-frontend (BFF), and even integrate fault resiliency observability for the ultimate production visibility and confidence.

    learn:
        - Infrastructure as Code the Pulumi way
        - How to balance cost, latency, and resources
        - Production readiness for Serverless applications
        - Java optimization on Google Cloud

    # The webinar presenters
    presenters:
        - name: Kat Morgan
          role: Sr. Community Engineer, Pulumi
          photo: /images/team/kat-morgan.jpg
        - name: Xiang Shen
          role: Solutions Architect, Google Cloud
          photo: /images/people/xiang-shen.jpg

    # case-sensitive
    tags:
        level:  # Beginner, Intermediate, Advanced
        topics: ["Serverless"]
        languages: ["Java"]
        clouds: ["Google Cloud"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 9dd83510-8c28-4976-9cc8-550dc5af0b6e
    salesforce_campaign_id: 701PQ000009Jb8MYAS
---