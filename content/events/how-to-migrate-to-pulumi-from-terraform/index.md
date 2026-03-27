---
# Name of the event, <= 60 characters
title: How to migrate to Pulumi from Terraform
meta_desc: Learn how to build on top of your existing Terraform codebases with Pulumi or replace Terraform entirely.
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
url_slug: how-to-migrate-to-pulumi-from-terraform

# The event type (workshop, webinar, talk).
event_type: workshop

# URL for embedding a URL for ungated events.
youtube_url:

# Sortable date. The datetime Hugo will use to sort the events in date order.
sortable_date: 2024-05-21T09:00:00-07:00

# Duration of the event.
duration: 90 minutes

# "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
location: virtual

# Description of the event.
description: |
    Many organizations are intrigued by the power of using general purpose languages with Pulumi to manage their infrastructure, but have a large existing investment in Terraform codebases. In this workshop, you'll learn how you can build on top of your existing Terraform code with Pulumi or replace Terraform entirely.

learn:
    - Approaches to using resources managed outside of Pulumi in Pulumi programs.
    - How to leverage your organization's existing Terraform by consuming TF outputs in Pulumi programs.
    - How to convert your existing Terraform code automatically to the Pulumi language of your choice and import resources from Terraform state files into your Pulumi state files.

# The event presenters
presenters:
    - name: Josh Kodroff
      role: Senior Solutions Architect, Pulumi
      photo: /images/team/josh-kodroff.jpg

# case-sensitive
tags:
    level: Beginner # Beginner, Intermediate, Advanced
    topics: []
    languages: []
    clouds: []

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 8f93df59-6803-4db3-912f-c8fdeb646e97
    salesforce_campaign_id: 701PQ00000AN6VLYA1
---
