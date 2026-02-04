---
# Name of the event, <= 60 characters
title: "AI-Powered App Modernization with Pulumi on Google Cloud"
meta_desc: Learn how to accelerate app modernization using Pulumi's developer-first Infrastructure as Code with Google Cloud's AI services.
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
external: true
block_external_search_index: false

# The url slug for the webinar landing page. If this is an external
# webinar, use the external URL as the value here.
url_slug: https://rsvp.withgoogle.com/events/accelerating-ai-powered-app-modernization-with-pulumi-on-google-cloud

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "AI-Powered App Modernization with Pulumi on Google Cloud"
    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: 

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2025-12-17T10:00:00-08:00

    # Duration of the webinar.
    duration: 60 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        As enterprises race to modernize their applications for the AI era, the complexity of managing cloud infrastructure has become a critical bottleneck. This hands-on workshop demonstrates how Google Cloud customers can accelerate their app modernization journey by leveraging Pulumi's developer-first Infrastructure as Code approach alongside Google Cloud's cutting-edge AI services.

        Unlike traditional infrastructure tools like Terraform, which were built for operators, creating friction between development and DevOps teams. Pulumi revolutionizes this paradigm by empowering developers to manage Google Cloud resources using familiar programming languages, such as Python, TypeScript, Go, C#, and Java.
        No need to learn HCL or file tickets, just build, deploy, and iterate faster with code.
    learn:
        - Deploy AI/ML workloads on Google Cloud using Pulumi's intuitive programming model
        - Leverage Google Cloud's Vertex AI, GKE, and Cloud Run with familiar development practices
        - Build reusable infrastructure components that scale across teams and projects
        - Modernize legacy applications with Google Cloud's migration tools through code
        - Implement CI/CD pipelines that treat infrastructure as first-class application code
        - Create self-service platforms that eliminate developer-operator bottlenecks

    # The webinar presenters
    presenters:
        - name: Jay Smith
          role: Sr. Cloud Customer Engineer, GCP
          photo: /images/team/jason-smith.jpg
        - name: Mitch Gerdisch
          role: Principal Solutions Architect, Pulumi
          photo: /images/team/mitch-gerdisch.jpg

    # case-sensitive
    tags:
        level: Beginner # Beginner, Intermediate, Advanced
        topics:  ["AI", "LLM", "CI/CD", "GPU Infrastructure"]
        languages: []
        clouds: ["Google Cloud"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: c53f2cce-2826-4163-9acb-53163b4951a0
    salesforce_campaign_id: 701PQ00000faNrKYAU
---
