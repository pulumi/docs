---
# Name of the webinar.
title: "Serverless Architecture on AWS"
meta_desc: "Explore building up a serverless microservices architecture on AWS using infrastructure as code, cloud engineering principles, and TypeScript."

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
url_slug: "serverless-architecture-aws"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Serverless Architecture on AWS"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Webinar pages support multiple session via the 'multiple' property.
# multiple:

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Serverless Architecture on AWS"
    # URL for embedding a URL for ungated webinars.
    youtube_url: 
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2022-11-03T08:00:00.000-07:00
    # Duration of the webinar.
    duration: "60 minutes"
    # Datetime of the webinar.
    datetime: 
    # Description of the webinar.
    description: |
        Let’s explore more about building up a serverless microservices architecture on AWS using infrastructure as code and cloud engineering principles. We’ll use TypeScript to build up our new architecture, and we’ll explore more about stacks, inputs and outputs, secrets, and more.

        If you want to code along, you’ll need a [free Pulumi SaaS account](https://app.pulumi.com/signup/), [the Pulumi CLI](https://www.pulumi.com/docs/get-started/install/), [NodeJS](https://www.pulumi.com/docs/intro/languages/javascript/), and an AWS account (free tier is okay).

    # The webinar presenters
    presenters:
        - name: Piers Karsenbarg
          role: Customer Engineer, Pulumi

    # A bullet point list containing what the user will learn during the webinar.

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: "9e81381b-6e89-4d5f-84b9-8ff675eb4c30"

aws_only: false
---