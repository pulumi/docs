---
# Name of the event, <= 60 characters
title: AWS AI Builder Lab
meta_desc: Join Pulumi in San Francisco, limited to 250 developers
meta_image:

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
external: true
block_external_search_index: true

# The url slug for the webinar landing page. If this is an external
# webinar, use the external URL as the value here.
url_slug: https://www.aicamp.ai/event/eventdetails/W2026021308

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: AWS AI Builder Lab

    event_type: event # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url:

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2026-02-13T09:00:00-08:00

    # Duration of the webinar.
    duration: 1 day

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: San Francisco, CA

    # Description of the webinar.
    description: |
        Join Pulumi in San Francisco, limited to 250 developers

    # The webinar presenters
    presenters:

    # case-sensitive
    tags:
        level: # Beginner, Intermediate, Advanced
        topics: ["AI"]
        languages: []

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id:
    salesforce_campaign_id:
---
