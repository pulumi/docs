---
# Name of the webinar.
title: "API Gateway for an AWS Lambda"
meta_desc: "In this week's edition of Modern Infrastructure as Code Wednesday, we’ll show you how to set up an API Gateway for an AWS Lambda function in 30 minutes."

# A featured webinar will display first in the list.
featured: false

# If the video is pre-recorded or live.
pre_recorded: true

# If the video is part of the PulumiTV series. Setting this value to true will list the video in the "PulumiTV" section.
pulumi_tv: true

# The preview image will be shown on the list page.
preview_image: "https://img.youtube.com/vi/yYWqcgs6FlA/hqdefault.jpg"

# Webinars with unlisted as true will not be shown on the webinar list
unlisted: false

# Gated webinars will have a registration form and the user will need
# to fill out the form before viewing.
gated: false

# The layout of the landing page.
type: webinars

# External webinars will link to an external page instead of a webinar
# landing/registration page.
external: false

# The url slug for the webinar landing page. If this is an external
# webinar, use the external URL as the value here.
url_slug: "aws-lambda-api-gateway"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "API Gateway for an AWS Lambda"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "API Gateway for an AWS Lambda"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/yYWqcgs6FlA"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2020-03-18 10:00:00 -07:00
    # Datetime of the webinar.
    datetime: ""
    # Description of the webinar.
    description: |
        For our Inaugural Episode, we’ll show you how to set up an API Gateway for an AWS Lambda function in 30 minutes. You’ll learn how to wire this up to a domain name and secure it using an API key for authorization. Finally, we’ll show you how to store the API key in a secrets manager.

    # The webinar presenters
    presenters:
        - name: Lee Zen
          role: VP of Engineering, Pulumi

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - How to set up an API Gateway for an AWS Lambda.
        - How to use an API key for authorization.
        - How to store an API key in a secrets manager.
---
