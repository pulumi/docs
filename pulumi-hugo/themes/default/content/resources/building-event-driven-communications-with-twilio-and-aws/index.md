---
# Name of the webinar.
title: "Building Communication Workflows with Twilio and AWS"
meta_desc: "In this session, the Twilio team will show you how they use Pulumi and how you can create powerful scheduling tools for your customer communications."

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
external: true
block_external_search_index: true

# The url slug for the webinar landing page. If this is an external
# webinar, use the external URL as the value here.
url_slug: "https://ahoy.twilio.com/devgen_webinar_workflows_NAMER-1"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Building Communication Workflows with Twilio, Pulumi, and AWS"
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
    title: "Building Communication Workflows with Twilio, Pulumi, and AWS"
    # URL for embedding a URL for ungated webinars.
    youtube_url: ""
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2021-09-28T09:00:00-07:00
    # Duration of the webinar.
    duration: "1 hour"
    # Datetime of the webinar.
    datetime: "TUE SEPT 28, 2021"
    # Description of the webinar.
    description: |
        With Twilio,  you can build powerful customer engagement workflows, but what if you want to persist your data? In this session, the Twilio team will show you how to create simple to powerful communication workflows using Pulumi for infrastructure management and AWS for persisting data.

    # The webinar presenters
    presenters:
        - name: Lee Zen
          role: VP Engineering, Pulumi
        - name: Giuseppe Verni
          role: Principal Solutions Engineer,, Twilio

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - How to set up services like AWS DynamoDB using Pulumi and your favorite programming languages.
        - Managing Twilio with Pulumi using TypeScript.
        - Designing a vote system using a phone number.

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: "aaebfbfa-9d86-4258-9332-94ae99c44ead"
---
