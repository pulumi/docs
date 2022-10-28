---
# Name of the webinar.
title: "Deploying and Managing Kafka with Pulumi and Confluent"
meta_desc: "Want to learn the easy way to set up Apache Kafka to manage your real-time data feeds? Pulumi and Confluent will show you how easy it can be."

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
url_slug: "deploying-and-managing-kafka-with-pulumi-and-confluent"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Deploying and Managing Kafka with Pulumi and Confluent"
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
    title: "Deploying and Managing Kafka with Pulumi and Confluent"
    # URL for embedding a URL for ungated webinars.
    youtube_url: ""
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2022-12-06T09:00:00-08:00
    # Duration of the webinar.
    duration: "1 hour"
    # Datetime of the webinar.
    datetime: ""
    # Description of the webinar.
    description: |
        Standing up production-ready infrastructure to store and analyze your real-time data feeds used to be a major undertaking. Now, with a few lines of code you can spin up all the resources you need in the cloud. In this session, we’ll introduce you to Apache Kafka—a community distributed event streaming platform capable of handling trillions of events a day. We’ll show you how to quickly provision and connect Kafka clusters using Confluent Cloud - a fully-managed cloud-native platform built by the original creators of Kafka. With the Pulumi Conflent Provider, you’ll learn how to easily provision Kafka and a complete data streaming platform using your favorite programming languages.

    # The webinar presenters
    presenters:
        - name: "Josh Kodroff"
          role: "Solutions Architect, Pulumi"
        - name: "Spencer Shumway"
          role: "Senior Product Manager, Confluent"

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - "How to provision a data streaming platform using modern programming languages"
        - "Securing your platform with Role Based Access Control (RBAC)"
        - "Using Connectors and other common features."

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: "cfe45bda-2e03-48a9-aa69-d25fc00cbfed"
    salesforce_campaign_id: "701Du0000009Q5yIAE"
---
