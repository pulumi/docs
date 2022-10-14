---
# Name of the webinar.
title: "Sharing Code with Pulumi Packages, Abstractions, and More"
meta_desc: "Explore how to start sharing Pulumi code with others. Use Go to build a custom architecture for GCP that we’ll compile down into a shareable library"

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
url_slug: "simpler-pulumi-package-authoring"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Sharing Code with Pulumi Packages, Abstractions, and More"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Webinar pages support multiple session via the 'multiple' property.
# multiple:

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Sharing Code with Pulumi Packages, Abstractions, and More"
    # URL for embedding a URL for ungated webinars.
    youtube_url: 
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2022-11-03T09:10:00.000-07:00
    # Duration of the webinar.
    duration: "60 minutes"
    # Datetime of the webinar.
    datetime: 
    # Description of the webinar.
    description: |
        Let’s explore how to start sharing Pulumi code with others. We’ll use Go to build a custom architecture for GCP that we’ll then compile down into a library we can share with others who work in other languages.

        If you want to code along, you’ll need a [free Pulumi SaaS account](https://app.pulumi.com/signup/), [the Pulumi CLI](https://www.pulumi.com/docs/get-started/install/), [Go](https://www.pulumi.com/docs/intro/languages/go/), and a Google Cloud account (free tier is okay).

    # The webinar presenters
    presenters:
        - name: Ringo De Smet
          role: Customer Experience Consultant, Pulumi

    # A bullet point list containing what the user will learn during the webinar.

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: "080c65c7-d07c-4ba5-abbd-04e481daf02e"

aws_only: false
---
