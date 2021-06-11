---
# Name of the webinar.
title: "Getting Started with Google Cloud & Infrastructure as Code"
meta_desc: "In this workshop, we’ll use the Google Cloud native provider to build infrastructure using TypeScript and examine some of Pulumi's newest features."

# A featured webinar will display first in the list.
featured: false

# If the video is pre-recorded or live.
pre_recorded: true

# If the video is part of the PulumiTV series. Setting this value to true will list the video in the "PulumiTV" section.
pulumi_tv: false

# The preview image will be shown on the list page.
preview_image: ""

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
url_slug: "getting-started-with-google-cloud-platform"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Getting Started with Google Cloud & Infrastructure as Code"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Getting Started with Google Cloud & Infrastructure as Code"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/2CHXNWiREBE"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2021-06-10T09:00:00-07:00
    # Duration of the webinar.
    duration: "2 hours"
    # Datetime of the webinar.
    datetime: "JUNE 10TH, 2021"
    # Description of the webinar.
    description: |
        Google Cloud’s product offering is continuously evolving, and infrastructure tools often can’t keep up with the speed of innovation. Pulumi’s Google Cloud Native provider is built directly from the Google Cloud API, bringing power of familiar programming languages to Google Cloud without sacrificing on latest features.

        In this workshop, we’ll use the Google Cloud native provider to build infrastructure using Pulumi’s TypeScript SDK and examine some of the features not previously possible.

    # The webinar presenters
    presenters:
        - name: Lee Briggs
          role: Community Engineer

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - How to build infrastructure in the Google Cloud Platform.
        - How to manage infrastructure running in the Google Cloud Platform.
        - How to deploy cloud applications to Google Cloud Platform infrastructure.

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 642fa736-77ef-4f0f-8a83-342a70794380
---
