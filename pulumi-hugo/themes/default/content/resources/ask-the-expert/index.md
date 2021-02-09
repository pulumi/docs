---
# Name of the webinar.
title: "Ask the Expert"
meta_desc: "Join our Ask the Expert session with Pulumi engineers. Come with your Pulumi-based questions and we will happily help you get the answers you need."

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
url_slug: "ask-the-expert"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Ask the Expert"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Webinar pages support multiple session via the 'multiple' property.
multiple:
    - datetime: 2021-02-11T11:00:00+01:00
      hubspot_form_id: 8e1a5894-5ec5-4ae7-b741-d75d2e020b38

    - datetime: 2021-02-25T11:00:00+01:00
      hubspot_form_id: cb663e2e-2a1e-4099-8311-1dcaa2af3b5d

    - datetime: 2021-03-11T11:00:00+01:00
      hubspot_form_id: 3ec7c538-d08a-4c94-b161-2824d41ae9c9

    - datetime: 2021-03-25T11:00:00+02:00
      hubspot_form_id: 776a238e-e34c-4ac9-9af8-4d069fd303b3

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Ask the Expert"
    # URL for embedding a URL for ungated webinars.
    youtube_url: ""
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2020-02-05T10:00:00-07:00
    # Duration of the webinar.
    duration: "1 hour"
    # Datetime of the webinar.
    datetime: ""
    # Description of the webinar.
    description: |
        Join our Ask the Expert session with Pulumi engineers. Come with your Pulumi-based questions --- we'll be here to answer any questions that are Cloud Engineering related. Have a project you're currently working on? Bring it --- we love sharing!

    # The webinar presenters
    presenters:
        - name: Paul Stack
          role: Software Engineer, Pulumi
        - name: Piers Karsenbarg
          role: Customer Engineer, Pulumi

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - Interact with Pulumi and Cloud Engineering experts.
        - Hear how others are developing solutions around cloud challenges.
        - Gain advice on how to get the most out of Pulumi.
---
