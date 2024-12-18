---
# Name of the event, <= 60 characters
title: "GitOps in Action: Deploy a Serverless AI app with Cloudflare"
meta_desc: Learn how to provision Cloudflare resources using GitOps. In particular, you'll deploy a Serverless AI text-to-image web app on Cloudflare Workers AI.
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
url_slug: create-and-deploy-serverless-ai-app-cloudflare

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "GitOps in Action: Deploy a Serverless AI app with Cloudflare"

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url:

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2024-08-07T09:00:00.000-07:00

    # Duration of the webinar.
    duration: 90 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        Develop and deploy a Serverless AI application using Cloudflare Workers and Pulumi. Throughout this workshop, you'll be guided in deploying cloud resources using a GitOps approach. Specifically, you'll utilize GitHub for version control and Pulumi as your Infrastructure as Code solution to manage your Cloudflare resources effectively.

    learn:
        - Build a Serverless AI app with Cloudflare Workers
        - Develop Infrastructure as Code with Pulumi in TypeScript
        - Implement GitOps best practices

    # The webinar presenters
    presenters:
        - name: Lizzie Siegle
          role: Developer Advocate, Cloudflare
          photo: /images/people/lizzie-siegle.jpg

    # case-sensitive
    tags:
        level: Beginner # Beginner, Intermediate, Advanced
        topics: ["GitOps"]
        languages: ["TypeScript"]
        clouds: ["Cloudflare"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 5da47c5a-c616-4266-b772-52b80c10c452
    salesforce_campaign_id: 701PQ00000DVW5lYAH
---
