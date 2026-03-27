---
# Name of the event, <= 60 characters
title: Intro to Infrastructure as Code with YAML
meta_desc: Learn the fundamentals of Infrastructure as Code (IaC) with Pulumi, using Docker, and YAML. Build and deploy a full stack app. Source code available.
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
url_slug: intro-to-infrastructure-as-code-with-yaml

# The event type (workshop, webinar, talk).
event_type: workshop

# URL for embedding a URL for ungated events.
youtube_url: https://www.youtube.com/embed/_A4hSJ_h6FQ?rel=0

# Sortable date. The datetime Hugo will use to sort the events in date order.
sortable_date: 2022-12-15T18:00:00.000Z

# Duration of the event.
duration: 1 hour

# "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
location: virtual

# Description of the event.
description: |
    In this workshop, we’re going to learn more about cloud computing and Infrastructure as Code by exploring how to use Pulumi to build, configure, and deploy a real-life, modern application using Docker. We will create a frontend, a backend, and a database to deploy the Pulumipus Boba Tea Shop, and along the way, learn more about how Pulumi works to make managing all of these different moving pieces a little bit less painful!

    If you want to code along, you’ll need a [free Pulumi SaaS account](https://app.pulumi.com/signup/) and [the Pulumi CLI](https://www.pulumi.com/docs/install/).

learn:
    - How to use YAML with Pulumi.
    - How to provision Docker containers with Pulumi.

# The event presenters
presenters:
    - name: Scott Lowe
      role: Sr. Technical Content Engineer, Pulumi
      photo: /images/team/scott-lowe.jpg

# case-sensitive
tags:
    level: Beginner # Beginner, Intermediate, Advanced
    topics: ["Docker"]
    languages: ["YAML"]

# The right hand side form section.
form:
  hubspot_form_id: 9812f461-677d-443c-bf3b-76d3d7c27310
  salesforce_campaign_id: 701Du0000009P9GIAU
---
