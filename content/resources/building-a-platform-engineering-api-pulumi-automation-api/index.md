---
# Name of the event, <= 60 characters
title: Build a Platform Engineering API using Pulumi Automation API
meta_desc: Learn how to build a robust Platform Engineering API using Pulumi's Automation API for streamlined infrastructure management.
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
url_slug: building-a-platform-engineering-api-pulumi-automation-api

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Building a Platform Engineering API using the Pulumi Automation API

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url:

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2024-06-06T09:00:00.000-07:00

    # Duration of the webinar.
    duration: 60 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        Nowadays, everything is or should be accessible via an API, and infrastructure is no exception. Join us in this webinar to learn how to build your own Platform Engineering API using Pulumi's Automation API, with a practical example in TypeScript and Express.js. Whether you're a developer or a DevOps engineer, this session will equip you with the knowledge and tools to elevate your platform engineering skills.

    learn:
        - The fundamentals of Pulumi's Automation API and its benefits for infrastructure management.
        - How to set up and configure your environment for using Pulumi's Automation API.
        - Practical example in Typescript of building and deploying infrastructure using the Automation API.

    # The webinar presenters
    presenters:
        - name: Engin Diri
          role: Senior Community Engineer, Pulumi
          photo: /images/team/engin-diri.jpg

    # case-sensitive
    tags:
        level: Beginner # Beginner, Intermediate, Advanced
        topics: ["Automation API"]
        languages: ["TypeScript"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 3b98315d-4395-4bf7-b82d-d8b39ff085da
    salesforce_campaign_id: 701PQ00000C9giiYAB
---