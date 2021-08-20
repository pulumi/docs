---
# Name of the webinar.
title: "The Docker Show: Multi-language components with Pulumi"
meta_desc: "In this episode Lee Zen will show you how Pulumi's multi-language components feature makes it easy to share infrastructure code across programming languages."

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
url_slug: "docker-show-multi-language-components"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "The Docker Show: Multi-language / Multi-cloud container components with Pulumi and Docker"
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
    title: "The Docker Show: Multi-language / Multi-cloud container components with Pulumi and Docker"
    # URL for embedding a URL for ungated webinars.
    youtube_url: ""
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2021-09-23T10:00:00-07:00
    # Duration of the webinar.
    duration: "1 hour"
    # Datetime of the webinar.
    datetime: ""
    # Description of the webinar.
    description: |
        In this episode, Pulumi VP of Engineering, Lee Zen will show you how Pulumi's new multi-language components feature makes it easy to share infrastructure code across programming languages. We'll also show you how to deploy containerized apps across multiple clouds using Google Cloud Run and AWS App Runner.

    # The webinar presenters
    presenters:
        - name: Lee Zen
          role: VP Engineering, Pulumi
        - name: Peter Mckee
          role: Head of Developer Relations, Docker

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - How to Get Started with Pulumi and Docker
        - Automate Building and Deploying your Containers using Pulumi
        - Deploying your Containers to AWS using Docker and Pulumi

# This section contains the transcript for a video. It is optional.
transcript: |
    Here is where you would put the transcript for a recorded video.

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 65c0e27b-7f95-4277-930b-ee4d09122a20
---
