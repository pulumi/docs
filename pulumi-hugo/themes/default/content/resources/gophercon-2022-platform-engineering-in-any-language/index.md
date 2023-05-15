---
# Name of the webinar.
title: "Workshop - Platform Engineering in ANY Language"
meta_desc: "David Flanagan will guide you through building a self-service Kubernetes platform, focusing on a great developer experience, with Pulumi's Go SDK."

# A featured webinar will display first in the list.
featured: false

# If the video is pre-recorded or live.
pre_recorded: false

# If the video is part of the PulumiTV series. Setting this value to true will list the video in the "PulumiTV" section.
pulumi_tv: false

# The preview image will be shown on the list page.
preview_image: ""

# Webinars with unlisted as true will not be shown on the webinar list
unlisted: true

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
url_slug: "https://www.gophercon.co.uk/workshops/"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Workshop - Platform Engineering in ANY Language"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Webinar pages support multiple session via the 'multiple' property.
# multiple:

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Workshop - Platform Engineering in ANY Language"
    # URL for embedding a URL for ungated webinars.
    youtube_url: ""
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2022-08-16T1:00:00.000-07:00
    # Duration of the webinar.
    duration: "7 hours"
    # Datetime of the webinar.
    datetime: "8/16/2022 1:00am - 8:00am PT"
    # Description of the webinar.
    description: |
        The days of bash being the language of the Ops professional are long gone. Today, we have the privilege to operate bare metal, provision the cloud, and sprinkle annotations on our Kubernetes manifests with a plethora of programming languages.

        In this session, I will guide you through building a self-service platform in 4 different programming languages, using Pulumi with AWS, Azure, and Google Cloud.

        Would you do this in production? Maybe not. Will it be fun? You're damn right.

    # The webinar presenters
    presenters:
        - name: David Flanagan
          role: Staff Developer Advocate, Pulumi

    # A bullet point list containing what the user will learn during the webinar.
    learn:

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id:
---
