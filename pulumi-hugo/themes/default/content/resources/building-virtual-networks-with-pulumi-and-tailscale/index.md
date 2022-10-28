---
# Name of the webinar.
title: "Building Virtual Networks with Pulumi and Tailscale"
meta_desc: "This workshop will demonstrate how to securely connect end-user devices and cloud resources using infrastructure as code written in real programming languages."

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
url_slug: "building-virtual-networks-with-pulumi-and-tailscale"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Building Virtual Networks with Pulumi and Tailscale"
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
    title: "Building Virtual Networks with Pulumi and Tailscale"
    # URL for embedding a URL for ungated webinars.
    youtube_url: ""
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2023-01-11T09:00:00-08:00
    # Duration of the webinar.
    duration: "1 hour"
    # Datetime of the webinar.
    datetime: ""
    # Description of the webinar.
    description: |
        This workshop will demonstrate how to securely connect end-user devices and cloud resources using modern infrastructure as code written in real programming languages. Using the Pulumi Tailscale provider, we’ll create virtual machines in AWS and securely connect them without needing to create and manage firewall rules. Join us and learn how to use Pulumi with Tailscale to seamlessly and securely connect your devices and cloud resources using a modern, zero-trust model!

    # The webinar presenters
    presenters:
        - name: "Josh Kodroff"
          role: "Solutions Architect, Pulumi"
        - name: "Xe Iaso"
          role: "Archmage of Infrastructure, Tailscale"

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - How to create secure, performant connections between your devices and servers without needing to poke holes in firewalls.
        - How to use modern programming languages to ship infrastructure faster.
        - How to use the Tailscale Pulumi provider to automate provisioning your VPNs in TypeScript.

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: "594f2022-90f5-439d-9105-ea528c452068"
    salesforce_campaign_id: "701Du0000009Q63IAE"
---
