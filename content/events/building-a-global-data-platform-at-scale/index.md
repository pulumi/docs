---
# Name of the webinar.
title: "Fauna - Building a Global Data Platform at Scale"
meta_desc: Dan Swartz, Altana's Principal Software Engineer, discusses how Pulumi's Automation API can be integrated into a self-service application.

cloud_engineering_days:
    track: customer_stories

# A featured webinar will display first in the list.
featured: false

# If the video is pre-recorded or live.
pre_recorded: true

# If the video is part of the PulumiTV series. Setting this value to true will list the video in the "PulumiTV" section.
pulumi_tv: false

# Webinars with unlisted as true will not be shown on the webinar list
unlisted: false

# Gated webinars will have a registration form and the user will need
# to fill out the form before viewing.
gated: false

# The layout of the landing page.
type: webinars
layout: cloud-engineering-days-replay

# External webinars will link to an external page instead of a webinar
# landing/registration page. If the webinar is external you will need
# set the 'block_external_search_index' flag to true so Google does not index
# the webinar page created.
external: false
block_external_search_index: false

# The url slug for the webinar landing page. If this is an external
# webinar, use the external URL as the value here.
url_slug: "building-a-global-data-platform-at-scale"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Building a Global Data Platform at Scale"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Building a Global Data Platform at Scale"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/NQpDNm9pH7s?rel=0"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2022-11-02T10:20:00-07:00
    # Duration of the webinar.
    duration: "28 minutes"
    # Description of the webinar.
    description: |
        At Fauna, availability is a top priority. It informs how we build everything, including our infrastructure. I'll discuss how we balance complexity and safety in our infrastructure as code to build, maintain, and scale FaunaDB. They use AWS and Python but soon will use the multi-cloud ability.

    # The webinar presenters
    presenters:
        - name: Jeff Smick
          role: Sr. Staff Engineer, Fauna
---
