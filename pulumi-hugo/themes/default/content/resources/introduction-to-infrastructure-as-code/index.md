---
# Name of the webinar.
title: "Introduction to Infrastructure as Code"
meta_desc: "In this workshop, you’re going to learn about Infrastructure as Code by exploring Pulumi to build and deploy a real-life modern application using Docker."

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
url_slug: "introduction-to-infrastructure-as-code"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Introduction to Infrastructure as Code"
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
    title: "Introduction to Infrastructure as Code"
    # URL for embedding a URL for ungated webinars.
    youtube_url: ""
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2022-05-05T14:30:00-07:00
    # Duration of the webinar.
    duration: "1 hour"
    # Datetime of the webinar.
    datetime: ""
    # Description of the webinar.
    description: |
        In this workshop, we’re going to learn more about cloud computing and Infrastructure as Code by exploring how to use Pulumi to build, configure, and deploy a real-life, modern application using Docker. We will create a frontend, a backend, and a database to deploy the Pulumipus Boba Tea Shop, and along the way, learn more about how Pulumi works to make managing all of these different moving pieces a little bit less painful!

    # The webinar presenters
    presenters:
        - name: Kat Cosgrove
          role: Staff Developer Advocate

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - How to provision, manage, and destroy cloud resources with Pulumi.
        - How to build an deploy Docker containers.
        - How to build and deploy a full stack application.

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 9a1b027e-0d19-4a6b-b184-22264403f535
---
