---
# Name of the webinar.
title: "Women who code Melbourne - Universal Infrastructure as Code"
meta_desc: "Discover and experiment with Universal Infrastructure as Code."

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
url_slug: "https://www.meetup.com/women-who-code-melbourne/events/287236999/"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Women who code Melbourne - Universal Infrastructure as Code"
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
    title: "Women who code Melbourne - Universal Infrastructure as Code"
    # URL for embedding a URL for ungated webinars.
    youtube_url: ""
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2022-08-25T00:30:00-07:00
    # Duration of the webinar.
    duration: "90 minutes"
    # Datetime of the webinar.
    datetime: ""
    # Description of the webinar.
    description: |
        Discover and experiment with Universal Infrastructure as Code

        What is Universal Infrastructure as Code?

        During this hands-on workshop, Cloud engineers Stephanie and Aurelien will take you on a discovery journey to learn about Universal Infrastructure as Code using general purpose programming languages to easily and painlessly set up and modify your infrastructure in the Cloud. 

    # The webinar presenters
    presenters:
        - name: Aurélien Requiem
          role: Senior Customer Engineer, Pulumi
        - name: Stephanie Swenson
          role: Cloud Engineer, Furō

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - What is Universal Infrastructure as Code
        - Deploying your first resources in the Cloud
        - Setting up guardrails for your deployments
---
