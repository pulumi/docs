---
# Name of the webinar.
title: "Armory + Pulumi: Continuous Delivery for your IaC"
meta_desc: "Learn how the Pulumi plugin for Spinnaker simplifies your deployments by having infrastructure and application code in a single workflow."

aliases:
  - /webinars/armory-continuos-delivery-for-infrastructure
  - /webinars/armory-continuous-delivery-for-infrastructure

# A featured webinar will display first in the list.
featured: false

# If the video is pre-recorded or live.
pre_recorded: false

# If the video is part of the PulumiTV series. Setting this value to true will list the video in the "PulumiTV" section.
pulumi_tv: false

# The preview image will be shown on the list page.
preview_image: "/images/webinar/pulumi_tech_talk.jpg"

# Webinars with unlisted as true will not be shown on the webinar list
unlisted: true

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
url_slug: "armory-continuous-delivery-for-infrastructure"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Armory + Pulumi: Continuous Delivery for your Infrastructure as Code"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Armory + Pulumi: Continuous Delivery for your Infrastructure as Code"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2020-09-10T12:00:00-07:00
    # Duration of the webinar.
    duration: "1 hour"
    # Datetime of the webinar.
    datetime: "THU AUG 6, 2020 AT 12:00 PM PDT"
    # Description of the webinar.
    description: |
        Learn how the new Pulumi plugin for Spinnaker simplifies your deployments by empowering your teams to deliver infrastructure and application code in a single workflow using the same languages.

    # The webinar presenters
    presenters:
        - name: Praneet Loke
          role: Software Engineer, Pulumi
        - name: Daniel Peach
          role: Senior Software Engineer, Armory

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - How to use the Pulumi plugin for Spinnaker
        - How to write infrastructure code in familiar programming languages

# The right hand side form section.
form:
    # GoToWebinar webinar key. This key allows us to register people for webinars via the
    # HubSpot form.
    gotowebinar_key: "7516354254778856975"

    # HubSpot form id.
    hubspot_form_id: "bdb2e44f-d0ff-4a57-97b4-b2467abf6a39"
---
