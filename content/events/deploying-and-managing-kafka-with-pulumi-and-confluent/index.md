---
# Name of the event, <= 60 characters
title: Deploying and Managing Kafka with Pulumi and Confluent
meta_desc: Want to learn the easy way to set up Apache Kafka to manage your real-time data feeds? Pulumi and Confluent will show you how easy it can be.
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
url_slug: deploying-and-managing-kafka-with-pulumi-and-confluent

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Deploying and Managing Kafka with Pulumi and Confluent

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: # missing

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2022-12-06T09:00:00-08:00

    # Duration of the webinar.
    duration: 1 hour

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        Standing up production-ready infrastructure to store and analyze your real-time data feeds used to be a major undertaking. Now, with a few lines of code you can spin up all the resources you need in the cloud. In this session, we’ll introduce you to Apache Kafka—a community distributed event streaming platform capable of handling trillions of events a day. We’ll show you how to quickly provision and connect Kafka clusters using Confluent Cloud - a fully-managed cloud-native platform built by the original creators of Kafka. With the Pulumi Conflent Provider, you’ll learn how to easily provision Kafka and a complete data streaming platform using your favorite programming languages.

    learn:
        - How to provision a data streaming platform using modern programming languages
        - Securing your platform with Role Based Access Control (RBAC)
        - Using Connectors and other common features.

    # The webinar presenters
    presenters:
        - name: Josh Kodroff
          role: Senior Solutions Architect, Pulumi
          photo: /images/team/josh-kodroff.jpg
        - name: Spencer Shumway
          role: Senior Product Manager, Confluent

    # case-sensitive
    tags:
        level: Beginner # Beginner, Intermediate, Advanced
        topics: ["Kafka", "Confluent Cloud"]
        languages: []

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: cfe45bda-2e03-48a9-aa69-d25fc00cbfed
    salesforce_campaign_id: 701Du0000009Q5yIAE
---
