---
# Name of the webinar.
title: "Introduction to Pulumi"
meta_desc: In this bi-monthly workshop, you will learn the fundamentals of Infrastructure as Code through guided exercises using Pulumi's Cloud Engineering platform.

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
url_slug: "introduction-to-pulumi"

# Webinar pages support multiple session via the 'multiple' property.
multiple:
    - datetime: 2021-04-08T10:00:00-07:00
      hubspot_form_id: "64bd0999-63b9-4049-bdb4-c47686d3ffb3"

    - datetime: 2021-05-18T10:00:00-07:00
      hubspot_form_id: "4690007d-8ec6-4141-b050-d4b845f21e04"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Introduction to Pulumi"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Introduction to Pulumi"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/YfdFxae8Bxc"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2020-12-01T17:00:00-08:00
    # Duration of the webinar.
    duration: "1 hour"
    # Datetime of the webinar.
    datetime: ""
    # Description of the webinar.
    description: |
        In this workshop, you will learn the fundamentals of Infrastructure as Code through a series of guided exercises using Pulumi's Cloud Engineering platform. You will be introduced to Pulumi, an infrastructure as code platform where you can use programming languages to provision modern cloud infrastructure.

        This workshop is designed to help users completely new to Pulumi become familiar with the core concepts needed to be effective with the Pulumi Infrastructure as Code platform. We will guide through the Pulumi platform with diagrams and a series of hands on exercises to help you understand the building blocks available in Pulumi.

        **Prerequisites**

        To successfully complete all the exercises you will need to have [Docker](https://docs.docker.com/get-docker/) installed on your machine. You can also install the [Pulumi CLI](/docs/get-started/install/) ahead of time, but we will walk you through the install process during the session.


    # The webinar presenters
    presenters:
        - name: Lee Briggs
          role: Community Engineer, Pulumi

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - What is Pulumi?
        - How to install Pulumi
        - Configuring your development environment
        - Choose your Pulumi language
        - An introduction to the Pulumi state & the Pulumi console
        - An introduction to Pulumi config
        - Storing sensitive data in Pulumi securely
        - Provision your first resources
        - Understanding stacks
        - An introduction to the Pulumi programming model
---
