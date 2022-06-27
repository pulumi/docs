---
# Name of the webinar.
title: "AWS Immersion Day - Hands-on Infrastructure as Code"
meta_desc: "In this workshop, you will learn the fundamentals of Infrastructure as Code through a series of guided exercises using Pulumi’s Cloud Engineering platform."

# A featured webinar will display first in the list.
featured: false

# If the video is pre-recorded or live.
pre_recorded: true

# If the video is part of the PulumiTV series. Setting this value to true will list the video in the "PulumiTV" section.
pulumi_tv: false

# The preview image will be shown on the list page.
preview_image: ""

# Webinars with unlisted as true will not be shown on the webinar list
unlisted: false

# Gated webinars will have a registration form and the user will need
# to fill out the form before viewing.
gated: false

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
url_slug: "aws-immersion-day-hands-on-infrastructure-as-code"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "AWS Immersion Day - Hands-on Infrastructure as Code"
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
    title: "AWS Immersion Day - Hands-on Infrastructure as Code"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/elCqbTB3m40"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2022-06-14T09:00:00-07:00
    # Duration of the webinar.
    duration: "90 minutes"
    # Datetime of the webinar.
    datetime: ""
    # Description of the webinar.
    description: |
        In this workshop, you will learn the fundamentals of Infrastructure as Code through a series of guided exercises using Pulumi’s Cloud Engineering platform. Join Pulumi and our friends from VirtusLab and AWS for an interactive session where you will be introduced to infrastructure as code concepts, and use the Java programming language to provision resources on AWS.

        This workshop is designed to help users completely new to Pulumi to become familiar with the core concepts to be effective with the Pulumi Infrastructure as Code platform. We will guide you through the Pulumi platform with diagrams and a series of hands-on exercises to help you understand the building blocks available in Pulumi.

    # The webinar presenters
    presenters:
        - name: Laura Santamaria
          role: Developer Advocate, Pulumi
        - name: Marina Novikova
          role: Partner Solutions Architect, AWS
        - name: Paweł Prażak
          role: Cloud Architect, VirtusLab

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - The fundamentals of Infrastructure as Code.
        - Provision cloud resources on AWS.
        - All about Pulumi Java support

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: "cf51e6f8-648e-4019-81f3-b38cdefd5d22"
---
