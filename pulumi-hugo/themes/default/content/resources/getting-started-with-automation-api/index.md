---
# Name of the webinar.
title: "How to Build a Self-Service Cloud with Python"
meta_desc: "In this workshop, you’ll build a Python & Flask web application that lets you and your developers deploy applications at the click of a button."

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
url_slug: "getting-started-with-automation-api"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "How to Build a Self-Service Cloud with Python"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Webinar pages support multiple session via the 'multiple' property.
multiple:
    - datetime: 2021-08-25T18:00:00-07:00
      hubspot_form_id: 25c90b21-1f57-49be-a171-b63ce46e7b57

    - datetime: 2021-09-09T04:00:00-07:00
      hubspot_form_id: c217773f-0f19-4b49-9f2a-ce17841b04f7

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "How to Build a Self-Service Cloud with Python"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/24qnvC-dvvw"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2021-05-20T09:00:00-07:00
    # Duration of the webinar.
    duration: "2 hours"
    # Datetime of the webinar.
    datetime: "MAY 20, 2020"
    # Description of the webinar.
    description: |
        Pulumi’s Automation API opens new horizons for infrastructure provisioning. In this workshop, you’ll examine the powerful new capabilities of Pulumi’s latest feature by building a Python & Flask web application that lets developers deploy applications at the click of a button.

    # The webinar presenters
    presenters:
        - name: Kat Cosgrove
          role: Staff Developer Advocate, Pulumi
        - name: Matty Stratton
          role: Staff Developer Advocate, Pulumi


    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - How to create cloud infrastructure with Pulumi's Automation API.
        - How to build a self-service cloud platform for deploying applications.
---
