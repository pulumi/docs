---
# Name of the event, <= 60 characters
title: Building AI-powered Applications at Pulumi
meta_desc: Learn how the Pulumi engineering team builds AI-powered capabilities and the lessons learned bringing these features into production.
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
url_slug: building-ai-powered-applications-at-pulumi

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Building AI-powered Applications at Pulumi

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url:

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2024-05-15T09:00:00.000-07:00

    # Duration of the webinar.
    duration: 90 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        Developers, DevOps, and Platform Engineering teams are increasingly charged with helping their organizations to deliver product innovation using AI capabilities. For the past 18 months, Pulumi has built and shipped a variety a AI-powered capabilities for customers using Pulumi Cloud to manage underlying AI infrastructure.

        In this session, you'll hear from Pulumi Engineering Manager, Aaron Friel about the lessons learned building applications with Large Language Models at Pulumi.

    learn:
        - Best practices for experimenting with AI in product development
        - Architecture and cost considerations when managing AI infrastructure at scale

    # The webinar presenters
    presenters:
        - name: Aaron Friel
          role: Engineering Manager, Pulumi
          photo: /images/team/aaron-friel.jpg

    # case-sensitive
    tags:
        level: Intermediate # Beginner, Intermediate, Advanced
        topics: ["AI"]
        languages: []

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: ce41b4a0-18fa-4b5f-a988-ea89178dabae
    salesforce_campaign_id: 701PQ000008jy1sYAA
---