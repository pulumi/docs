---
# Name of the webinar.
title: "Getting Started with Infrastructure as Code on DigitalOcean"
meta_desc: "In this hands-on workshop, you will learn how to stand up basic services using Infrastructure as Code through a series of hands-on labs."

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
url_slug: "getting-started-with-infrastructure-as-code-on-digital-ocean"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Getting Started with Infrastructure as Code on DigitalOcean"
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
    title: "Getting Started with Infrastructure as Code on DigitalOcean"
    # URL for embedding a URL for ungated webinars.
    youtube_url: ""
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2022-07-28T08:00:00-07:00
    # Duration of the webinar.
    duration: "90 minutes"
    # Datetime of the webinar.
    datetime: ""
    # Description of the webinar.
    description: |
        In this hands-on workshop, the Pulumi and the DigitalOcean teams will show you how to stand up basic services using Infrastructure as Code (IaC) through a series of hands-on labs.

    # The webinar presenters
    presenters:
        - name: Matt Stratton
          role: Staff Developer Advocate, Pulumi
        - name: Chris Sevilleaja
          role: Senior Developer Advocate, DigitalOcean

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - How to use Pulumi to provision cloud resources
        - How to use IaC on DigitalOcean

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: "7498bb01-dceb-4519-ab4e-9413355ada23"
---
