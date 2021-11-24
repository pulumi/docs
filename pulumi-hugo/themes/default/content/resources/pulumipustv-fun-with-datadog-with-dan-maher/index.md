---
# Name of the webinar.
title: "PulumipusTV - Fun with Datadog with Dan Maher"
meta_desc: "Join Matt Stratton and Dan Maher from Datadog to learn how to set up monitoring for any stack and any app using Pulumi and Datadog"

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
url_slug: "pulumipustv-fun-with-datadog-with-dan-maher"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "PulumipusTV - Fun with Datadog with Dan Maher"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Webinar pages support multiple session via the 'multiple' property.
# multiple:
#   - datetime: 2020-02-05T10:00:00-07:00
#     hubspot_form_id: ""
#     gotowebinar_key: ""

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "PulumipusTV - Fun with Datadog with Dan Maher"
    # URL for embedding a URL for ungated webinars.
    youtube_url: ""
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2021-12-16T12:00:00-08:00
    # Duration of the webinar.
    duration: "1 hour"
    # Datetime of the webinar.
    datetime: ""
    # Description of the webinar.
    description: |
        Join Matt Stratton and Dan Maher from Datadog to learn how to set up monitoring for any stack and any app using Pulumi and Datadog.

    # The webinar presenters
    presenters:
        - name: Matt Stratton
          role: Staff Developer Advocate, Pulumi

        - name: Dan Maher
          role: Developer Advocate, Datadog

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - How to define and manage Datadog resources using Pulumi.
        - How to configure monitoring fro your apps and infrastructure using Datadog.

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: "2f2ed96d-aab4-4010-a802-508be39e9999"
---
