---
# Name of the event, <= 60 characters
title: DevOps Days Philadelphia
meta_desc: "Join Pulumi's Josh Kodroff, Principal Customer Success Architect, in Philadelphia as he presents \"From IaC to IDP: A Practical Guide to Self-Service Maturity.\""
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
url_slug: https://www.eventbrite.com/e/devopsdays-philadelphia-2025-september-30th-october-1st-2025-tickets-1549913154969

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: DevOps Days Philadelphia

    event_type: event # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url:

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2025-09-30T09:00:00-00:00

    # Duration of the webinar.
    duration: 2 days

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: Philadelphia, PA
    # Description of the webinar.
    description: "Join Pulumi's Josh Kodroff, Principal Customer Success Architect, in Philadelphia as he presents \"From IaC to IDP: A Practical Guide to Self-Service Maturity.\""

    # The webinar presenters
    presenters:

    # case-sensitive
    tags:
        level: # Beginner, Intermediate, Advanced
        topics: []
        languages: []
        clouds: []

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id:
    salesforce_campaign_id:
---