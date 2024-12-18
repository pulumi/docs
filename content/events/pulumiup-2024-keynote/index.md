---
# Name of the event, <= 60 characters
title: PulumiUP 2024 Keynote
meta_desc: Watch PulumiUP 2024's keynote. Pulumi's co-founder and CEO shared insights into the company's current landscape and future direction
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
external: false
block_external_search_index: false

# The url slug for the webinar landing page. If this is an external
# webinar, use the external URL as the value here.
url_slug: pulumiup-2024-keynote

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: PulumiUP 2024 Keynote

    event_type: event # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: https://www.youtube.com/embed/AepHQaXeNX0

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2024-09-18T09:00:00-00:00

    # Duration of the webinar.
    duration: 1 hour

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        Watch PulumiUP 2024's keynote. Pulumi's co-founder and CEO shared insights into the company's current landscape and future direction, offering a glimpse into how the company is shaping the future of cloud engineering.

        This keynote also featured presentations and demos from key members of the Pulumi team, unveiling the latest product launches designed to elevate your infrastructure management experience.
        
        Learn more about the new product launches:
        - [Pulumi - One Unified Platform For All Your Infrastructure Needs](/blog/pulumi-up-2024/)
        - Visibility, intelligence, and controls over all infrastructure with [Pulumi Insights 2.0](/blog/pulumi-insights-2/)
        - Centralized secrets management and orchestration that scales with [Pulumi ESC](/blog/pulumi-esc-ga/)

    # The webinar presenters
    presenters:
        - name: Joe Duffy
          role: CEO, Pulumi
          photo: /images/team/joe-duffy.jpg

    # case-sensitive
    tags:
        level: # Beginner, Intermediate, Advanced
        topics: ["DevOps", "Security", "AI", "Pulumi ESC", "Platform Engineering"]
        languages: []

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id:
    salesforce_campaign_id:
---