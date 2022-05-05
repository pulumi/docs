---
# Name of the webinar.
title: "Analyst Report: EMA Product to Watch, Infrastructure as Code"
meta_desc: "Pulumi has been named an EMA Product to Watch in 2022/23 for the Infrastructure as Code category."

meta_image: /images/resources/ema-meta-image.png

# Set the whitepaper flag.
whitepaper: true

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
url_slug: "ema-product-to-watch"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "EMA Product to Watch"
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
    title: "EMA Product to Watch"
    # URL for embedding a URL for ungated webinars.
    youtube_url: ""
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2022-05-05T10:00:00-07:00
    # Duration of the webinar.
    duration: "8 pages"
    # Datetime of the webinar.
    datetime: ""
    # Description of the webinar.
    description: |
        Pulumi created a cloud engineering platform that allows developers, operators, and security staff to apply standard software engineering principles to creating infrastructure code and policies alongside application code. This brings the ultimate degree of consistency, compliance, and efficiency to software development, deployment, and day-2 management.

        <img src="/images/resources/ema-pie-charts.png" alt="EMA Report" />

        Submit the form to read the full report.

    # The webinar presenters
    presenters:
        - name: Torsten Volk
          role: Managing Research Director for Cloud-Native, DevOps, Machine Learning, and AI

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - Learn why Pulumi is a product to watch in 2022/2023

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: "72739cd9-0081-438e-a1a0-61df29e823b0"
---
