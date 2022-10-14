---
# Name of the webinar.
title: "Pulumi 101: Serverless containers on Google Cloud"
meta_desc: "Learn the basics of Pulumi from projects to components. Use Python and templates to stand up serverless containers on Cloud Run from Google Cloud"

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
url_slug: "pulumi-101-serverless-containers-gcp"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Pulumi 101: Serverless containers on GCP"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Webinar pages support multiple session via the 'multiple' property.
# multiple:

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Pulumi 101: Serverless containers on GCP"
    # URL for embedding a URL for ungated webinars.
    youtube_url: 
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2022-11-02T13:00:00.000-07:00
    # Duration of the webinar.
    duration: "60 minutes"
    # Datetime of the webinar.
    datetime: 
    # Description of the webinar.
    description: |
        Learn the basics of Pulumi from projects to components. We’ll use Python and templates to stand up our first bit of infrastructure: A small set of serverless containers on Cloud Run from Google Cloud. Along the way, we’ll learn how infrastructure as code makes updates easier, reduces time to value, and helps you keep your cloud costs down.

        If you want to code along, you’ll need a [free Pulumi SaaS account](https://app.pulumi.com/signup/?utm_source=da&utm_medium=referral&utm_campaign=workshops&utm_content=ced-fall2022-workshops), [the Pulumi CLI](https://www.pulumi.com/docs/get-started/install/?utm_source=da&utm_medium=referral&utm_campaign=workshops&utm_content=ced-fall2022-workshops), [Python 3.9.x](https://www.pulumi.com/docs/intro/languages/python/?utm_source=da&utm_medium=referral&utm_campaign=workshops&utm_content=ced-fall2022-workshops), and a Google Cloud account (free tier is okay).

    # The webinar presenters
    presenters:
        - name: Tushar Shah
          role: Senior Customer Engineer, Pulumi

    # A bullet point list containing what the user will learn during the webinar.

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: "d862675a-2f01-405c-9069-07003d2e3fdb"

aws_only: false
---
