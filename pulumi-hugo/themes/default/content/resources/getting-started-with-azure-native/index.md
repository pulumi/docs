---
# Name of the webinar.
title: "Azure: Unlocking Azure with Infrastructure as Software with TypeScript"
meta_desc: "In this workshop, you’ll use the Azure native provider to build infrastructure using TypeScript SDK and examine some of the features not previously possible."

# A featured webinar will display first in the list.
featured: false

# If the video is pre-recorded or live.
pre_recorded: false

# If the video is part of the PulumiTV series. Setting this value to true will list the video in the "PulumiTV" section.
pulumi_tv: false

# The preview image will be shown on the list page.
preview_image: ""

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
url_slug: "getting-started-with-azure-native"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Azure: Unlocking Azure with Infrastructure as Software with TypeScript"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Azure: Unlocking Azure with Infrastructure as Software with TypeScript"
    # URL for embedding a URL for ungated webinars.
    youtube_url: ""
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2021-04-27T09:00:00-07:00
    # Duration of the webinar.
    duration: "1 hour"
    # Datetime of the webinar.
    datetime: "APR 27TH, 2021"
    # Description of the webinar.
    description: |
        Microsoft Azure’s product offering is continuously evolving, and infrastructure tools often can’t keep up with the speed of innovation. Pulumi’s Azure Native provider is built directly from the Azure API, bringing power of familiar programming languages to Azure without sacrificing on latest features.

        In this workshop, you’ll use the Azure native provider to build infrastructure using Pulumi’s TypeScript SDK and examine some of the features not previously possible.

    # The webinar presenters
    presenters:
        - name: Lee Briggs
          role: Community Engineer, Pulumi

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - The basics of the Pulumi Programming Model.
        - How to provision, update, and destroy Azure resources.

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 3d988d22-21a0-4ec9-8255-8ddd03a197e6
---
