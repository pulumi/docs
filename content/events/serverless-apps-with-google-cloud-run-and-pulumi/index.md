---
# Name of the event, <= 60 characters
title: Serverless Apps with Google Cloud Run and Pulumi
meta_desc: Learn how to deploy applications effortlessly on Cloud Run with Pulumi, use containerization with Docker, and manage Google Cloud resources with code.
meta_image:
# A featured event will display first in the list.
featured: false

# Events with unlisted as true will not be shown on the event list
unlisted: false

# Gated events will have a registration form and the user will need
# to fill out the form before viewing.
gated: false

# External events will link to an external page instead of an event
# landing/registration page. If the event is external you will need
# set the 'block_external_search_index' flag to true so Google does not index
# the event page created.
external: false
block_external_search_index: false

# The url slug for the event landing page. If this is an external
# event, use the external URL as the value here.
url_slug: serverless-apps-with-google-cloud-run-and-pulumi

# The event type (workshop, webinar, talk).
event_type: workshop

# URL for embedding a URL for ungated events.
youtube_url: https://www.youtube.com/embed/ozR86AApTyE?rel=0

# Sortable date. The datetime Hugo will use to sort the events in date order.
sortable_date: 2023-11-30T09:00:00.000-08:00

# Duration of the event.
duration: 1 hour

# "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
location: virtual

# Description of the event.
description: |
    Developers who need to deploy their applications often find it tough to ship quickly with many options available for running containerized apps. Cloud Run helps abstract away the complexities of container services and orchestration so you can package and deploy apps while making it easy to scale to meet customer demand.

learn:
    - How to package your app as a Docker container
    - Defining resources in Google Cloud using Python with Pulumi
    - Running and scaling your application on Cloud Run

# The event presenters
presenters:
    - name: Monica Rodriguez
      role: Sr Product Manager, Pulumi
      photo: /images/team/monica-rodriguez.jpg
    - name: Jason Smith
      role: Sr Cloud Customer Engineer, Google

# case-sensitive
tags:
    level: Beginner # Beginner, Intermediate, Advanced
    topics: ["Docker"]
    languages: ["Python"]
    clouds: ["Google Cloud"]

# The right hand side form section.
form:
    hubspot_form_id: c39c7789-2dbd-4516-acd2-860ceeb7f12d
    salesforce_campaign_id: 701Du000000Bkp6IAC
---