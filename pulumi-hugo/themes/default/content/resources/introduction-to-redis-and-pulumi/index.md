---
# Name of the webinar.
title: "Introduction to Redis Cloud and Pulumi"
meta_desc: "Join the Redis and Pulumi team to learn how to deploy Redis Cloud resources on any cloud using any programming language with Pulumi."
meta_image: "/images/resources/intro-redis-workshop.png"

# A featured webinar will display first in the list.
featured: false

# If the video is pre-recorded or live.
pre_recorded: false

# If the video is part of the PulumiTV series.
# Setting this value to true will list the video in the "PulumiTV" section.
pulumi_tv: false

# The preview image will be shown on the list page.
preview_image: ""

# Webinars with unlisted as true will not be shown on the webinar list.
unlisted: false

# Gated webinars will have a registration form
# and the user will need to fill out the form before viewing.
gated: true

# The layout of the landing page.
type: webinars

# External webinars will link to an external page
# instead of a webinar landing/registration page.
# If the webinar is external
# you will need set the 'block_external_search_index' flag to true
# so Google does not index the webinar page created.
external: false
block_external_search_index: false

# The url slug for the webinar landing page.
# If this is an external webinar, use the external URL as the value here.
url_slug: "introduction-to-redis-and-pulumi"

# The content of the hero section.
hero:
    # The title text in the hero.
    # This also serves as the pages H1.
    title: "Introduction to Redis and Pulumi"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Webinar pages support multiple session via the 'multiple' property.
# multiple:
#   - datetime: 2020-02-05T10:00:00-07:00
#     hubspot_form_id: ""
#     gotowebinar_key: ""

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Introduction to Redis and Pulumi"
    # URL for embedding a URL for ungated webinars.
    youtube_url: ""
    # Sortable date.
    # The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2023-07-13T06:00:00-07:00
    # Duration of the webinar.
    duration: "1 hour"
    # Datetime of the webinar.
    datetime: ""
    # Description of the webinar.
    description: |
        Redis Cloud makes apps faster by providing an in-memory database that enables teams to create a real-time data platform. Join the Pulumi and Redis team to learn how to provision Redis Cloud alongside other cloud resources on AWS, Azure and Google Cloud - all using your favorite programming languages and the new Redis Cloud provider for Pulumi.

    # The webinar presenters
    presenters:
        - name: Josh Kodroff
          role: Senior Solutions Architect, Pulumi
        - name: Noam Stern
          role: Product Manager, Redis

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - How to get started with NoSQL using Redis Cloud.
        - Defining and deploying Redis Cloud resources using popular programming languages 
        - How to use Pulumi and Redis together.

form:
    salesforce_campaign_id: "701Du000000APrO"
    hubspot_form_id: "1cbe5289-28ba-4a1d-9881-0528fe711261"
---
