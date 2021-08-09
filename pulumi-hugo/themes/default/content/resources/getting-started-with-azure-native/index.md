---
# Name of the webinar.
title: "Getting Started with Azure and Infrastructure as Code"
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

# Webinar pages support multiple session via the 'multiple' property.
multiple:
    - datetime: 2021-08-12T09:00:00-07:00
      hubspot_form_id: d69a09b6-9f49-4d07-a4fd-98668b1fac26

    - datetime: 2021-08-11T04:00:00-07:00
      hubspot_form_id: 5b3b8768-f2d5-45a5-8c0a-673a39b08a8f

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Getting Started with Azure and Infrastructure as Code"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Getting Started with Azure and Infrastructure as Code"
    # URL for embedding a URL for ungated webinars.
    youtube_url: ""
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2021-04-28T09:00:00-07:00
    # Duration of the webinar.
    duration: "1 hour"
    # Datetime of the webinar.
    datetime: "April 28th, 2021"
    # Description of the webinar.
    description: |
        Microsoft Azure’s product offering is continuously evolving, and infrastructure tools often can’t keep up with the speed of innovation. Pulumi’s Azure Native provider is built directly from the Azure API, bringing power of familiar programming languages to Azure without sacrificing on latest features.

        In this workshop, you’ll use the Azure native provider to build infrastructure using Pulumi’s TypeScript SDK and examine some of the features not previously possible.

    # The webinar presenters
    presenters:
        - name: Sophia Parafina
          role: Developer Advocate, Pulumi

        - name: Matt Stratton
          role: Developer Advocate, Pulumi

        - name: Mikhail Shilkov
          role: Software Engineer, Pulumi

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - The basics of the Pulumi Programming Model.
        - How to provision, update, and destroy Azure resources.
---
