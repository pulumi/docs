---
# Name of the event, <= 60 characters
title: Getting Started with Infrastructure as Code on AWS
meta_desc: In this workshop, you will learn the fundamentals of Infrastructure as Code through a series of guided exercises using the Pulumi Cloud Engineering platform.
meta_image:

# A featured event will display first in the list.
featured: false

# Events with unlisted as true will not be shown on the event list
unlisted: false

# Gated events will have a registration form and the user will need
# to fill out the form before viewing.
gated: true

# External events will link to an external page instead of an event
# landing/registration page. If the event is external you will need
# set the 'block_external_search_index' flag to true so Google does not index
# the event page created.
external: false
block_external_search_index: false

# The url slug for the event landing page. If this is an external
# event, use the external URL as the value here.
url_slug: getting-started-with-iac-on-aws

# The event type (workshop, webinar, talk).
event_type: workshop

# URL for embedding a URL for ungated events.
youtube_url:

# Sortable date. The datetime Hugo will use to sort the events in date order.
sortable_date: 2024-05-09T09:00:00.000-07:00

# Duration of the event.
duration: 1 hour

# "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
location: virtual

# Description of the event.
description: |
    This workshop is designed to help users who are completely new to Pulumi become familiar with the core concepts to be effective with the Pulumi Infrastructure as Code platform. We will guide you through the Pulumi platform with diagrams and a series of hands-on exercises to help you understand the building blocks available in Pulumi

learn:
    - The basics of the Pulumi Programming Model
    - How to provision, update, and destroy AWS resources
    - Build a simple serverless App with Lambda and s3 bucket

# The event presenters
presenters:
    - name: Josh Kodroff
      role: Sr. Solutions Architect, Pulumi
      photo: /images/team/josh-kodroff.jpg

# case-sensitive
tags:
    level: Beginner # Beginner, Intermediate, Advanced
    topics: []
    languages: ["TypeScript"]
    clouds: ["AWS"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 65261ecc-933d-459b-9ac7-b1ede32410f4
    salesforce_campaign_id: 701PQ000008KcEFYA0
---