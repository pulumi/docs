---
# Name of the event, <= 60 characters
title: Introduction to Redis Cloud and Pulumi
meta_desc: Join the Redis and Pulumi team to learn how to deploy Redis Cloud resources on any cloud using any programming language with Pulumi.
meta_image: /images/resources/intro-redis-workshop.png

# A featured webinar will display first in the list.
featured: false

# Webinars with unlisted as true will not be shown on the webinar list
unlisted: false

# Gated webinars will have a registration form and the user will need
# to fill out the form before viewing.
gated: false

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
url_slug: introduction-to-redis-and-pulumi

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Introduction to Redis Cloud and Pulumi

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: https://www.youtube.com/embed/4DNFtD42bYE?rel=0

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2023-07-13T06:00:00-07:00

    # Duration of the webinar.
    duration: 1 hour

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        Redis Cloud makes apps faster by providing an in-memory database that enables teams to create a real-time data platform. Join the Pulumi and Redis team to learn how to provision Redis Cloud alongside other cloud resources on AWS, Azure and Google Cloud - all using your favorite programming languages and the new Redis Cloud provider for Pulumi.

    learn:
        - How to get started with NoSQL using Redis Cloud.
        - Defining and deploying Redis Cloud resources using popular programming languages 
        - How to use Pulumi and Redis together.

    # The webinar presenters
    presenters:
        - name: Josh Kodroff
          role: Sr Solutions Architect, Pulumi
          photo: /images/team/josh-kodroff.jpg
        - name: Noam Stern
          role: Product Manager, Redis
        - name: Greg Georges
          role: Sr Enablement Architect

    # case-sensitive
    tags:
        level: Beginner # Beginner, Intermediate, Advanced
        topics: ["Redis"]
        languages: []

# The right hand side form section.
form:
  hubspot_form_id: 1cbe5289-28ba-4a1d-9881-0528fe711261
  salesforce_campaign_id: 701Du000000APrO
---
