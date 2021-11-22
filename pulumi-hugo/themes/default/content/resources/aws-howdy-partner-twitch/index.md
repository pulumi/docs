---
# Name of the webinar.
title: "AWS - Howdy Partner"
meta_desc: "Join Laura Santamaria as they show off some of the newest features in Pulumi and how those features make building on AWS easier than ever."

aliases:
    - /resources/aws-howdy-partner-twitch-2020-06-01

# A featured webinar will display first in the list.
featured: false

# If the video is pre-recorded or live.
pre_recorded: false

# If the video is part of the PulumiTV series. Setting this value to true will list the video in the "PulumiTV" section.
pulumi_tv: false

# The preview image will be shown on the list page.
preview_image: "/images/webinar/aws-howdy-partner.png"

# Webinars with unlisted as true will not be shown on the webinar list
unlisted: false

# Gated webinars will have a registration form and the user will need
# to fill out the form before viewing.
gated: true

# The layout of the landing page.
type: webinars

# External webinars will link to an external page instead of a webinar
# landing/registration page.
external: false
block_external_search_index: false

# The url slug for the webinar landing page. If this is an external
# webinar, use the external URL as the value here.
url_slug: "aws-howdy-partner-twitch"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "AWS Howdy Partner"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Content for the left hand side section of the page. External webinars just need the
# time and duration values filled out.
main:
    # Webinar title.
    title: "AWS Howdy Partner"
    # URL for embedding a URL for ungated webinars.
    youtube_url: ""
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2021-12-08T14:00:00-08:00
    # Duration of the webinar.
    duration: "1 hour"
    # Datetime of the webinar.
    datetime: ""
    # Description of the webinar.
    description: |
        Join Pulumi and the AWS team for a fun live coding session showing off the new AWS Native Provider.

    # The webinar presenters
    presenters:
        - name: Laura Santamaria
          role: Developer Advocate, Pulumi

        - name: Andrew Park
          role: Specialist Solutions Architect, AWS

        - name: Marina Novikova
          role: Partner Solutions Architect, AWS

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - How to provision AWS resources with Pulumi.

form:
    hubspot_form_id: "e97a5160-b983-457b-9195-878630599823"
---
