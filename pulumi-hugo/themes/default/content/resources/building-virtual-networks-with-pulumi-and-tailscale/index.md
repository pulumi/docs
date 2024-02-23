---
# Name of the event, <= 60 characters
title: Building Virtual Networks with Pulumi and Tailscale
meta_desc: This workshop will demonstrate how to securely connect end-user devices and cloud resources using infrastructure as code written in real programming languages.
meta_image:

# A featured webinar will display first in the list.
featured: false

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
url_slug: building-virtual-networks-with-pulumi-and-tailscale

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Building Virtual Networks with Pulumi and Tailscale

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: https://www.youtube.com/embed/6JejC_bx8Yg?rel=0

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2023-01-11T09:00:00-08:00

    # Duration of the webinar.
    duration: 1 hour

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        This workshop will demonstrate how to securely connect end-user devices and cloud resources using modern infrastructure as code written in real programming languages. Using the Pulumi Tailscale provider, we’ll create virtual machines in AWS and securely connect them without needing to create and manage firewall rules. Join us and learn how to use Pulumi with Tailscale to seamlessly and securely connect your devices and cloud resources using a modern, zero-trust model!

    learn:
        - How to create secure, performant connections between your devices and servers without needing to poke holes in firewalls.
        - How to use modern programming languages to ship infrastructure faster.
        - How to use the Tailscale Pulumi provider to automate provisioning your VPNs in TypeScript.

    # The webinar presenters
    presenters:
      - name: Josh Kodroff
        role: Sr. Solutions Architect, Pulumi
        photo: /images/team/josh-kodroff.jpg
      - name: Xe Iaso
        role: Archmage of Infrastructure, Tailscale

    # case-sensitive
    tags:
        level: Intermediate # Beginner, Intermediate, Advanced
        topics: ["Tailscale", "AWS"]
        languages: ["TypeScript"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 594f2022-90f5-439d-9105-ea528c452068
    salesforce_campaign_id: 701Du0000009Q63IAE
---
