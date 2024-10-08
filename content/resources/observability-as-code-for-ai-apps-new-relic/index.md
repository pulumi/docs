---
# Name of the event, <= 60 characters
title: Observability as Code for AI Apps with New Relic and Pulumi
meta_desc: Learn how to use AWS to generate secure infrastructure code for deploying an AI Chatbot app with Pulumi, leveraging New Relic's LLM dashboards.
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
url_slug: observability-as-code-for-ai-apps-new-relic

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Observability as Code for AI Apps with New Relic and Pulumi

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url:

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2024-10-30T09:00:00-07:00

    # Duration of the webinar.
    duration: 90 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        Learn how to effectively monitor AI application and infrastructure costs using New Relic AI, leveraging custom LLM dashboards for deep insights. We'll guide you through using Pulumi Copilot to generate the necessary cloud resources for your AI Chatbot app, transitioning it seamlessly from a local environment to production with a DevOps approach.

        Additionally, we will explore how to securely manage credentials for services like OpenAPI, Pinecone, Docker, and more using Pulumi ESC. By mastering these skills, both application and platform teams can deliver secure, high-quality software more efficiently and reproducibly, while minimizing risk and complexity.

    learn:
        - How to monitor your AI app and infra costs with New Relic AI LLM Dashboards.
        - How to use Pulumi Copilot to generate infrastructure code in Python.
        - How to manage any secret securely with Pulumi ESC.

    # The webinar presenters
    presenters:
        - name: Piers Karsenbarg
          role: Senior Solutions Engineer, Pulumi
          photo: /images/team/piers-karsenbarg.jpg
        - name: Harry Kimpel
          role: Principal Developer Relations Engineer @ New Relic
          photo: /images/people/harry-kimpel.png

    # case-sensitive
    tags:
        level: Intermediate # Beginner, Intermediate, Advanced
        topics: ["Observability", "AI", "Pulumi ESC"]
        languages: ["Python", "TypeScript"]
        clouds: ["New Relic"]

# The right hand side form section.
form:
    hubspot_form_id: 6d4060d2-4833-4d9a-a41d-95a27a27651d
    salesforce_campaign_id: 701PQ00000IefBlYAJ
---
