---
# Name of the event, <= 60 characters
title: Advanced CI/CD for AWS using Pulumi and GitHub Actions
meta_desc: Learn advanced topics that make up a robust infrastructure CI/CD pipeline through guided exercises.
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
url_slug: advanced-cicd-aws-pulumi-github-actions

# The event type (workshop, webinar, talk).
event_type: workshop

# URL for embedding a URL for ungated events.
youtube_url: https://www.youtube.com/embed/F3zU0K0eV88

# Sortable date. The datetime Hugo will use to sort the events in date order.
sortable_date: 2024-08-14T09:00:00.000-07:00

# Duration of the event.
duration: 90 minutes

# "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
location: virtual

# Description of the event.
description: |
    In this workshop, you will learn advanced topics that make up a robust infrastructure CI/CD pipeline through guided exercises. You will use Pulumi tooling to take your cloud infrastructure pipeline one step closer to production.

    This workshop introduces users to advanced DevOps best practices. You will add compliance checks via policies, drift detection, and isolated test environments to an existing GitHub Actions pipeline. Accelerate your AWS projects with the [code examples provided](https://github.com/pulumi/workshops/tree/main/github-aws-cicd-advanced).

    Did you miss Part 1 of the DevOps workshop series? Start with [Get started with CI/CD for AWS using Pulumi & GitHub Actions before diving into advanced techniques.](/events/cicd-for-aws-with-pulumi-and-github-actions/)

learn:
    - How to build an advanced CI pipeline to enforce compliance and correct drift
    - How to add dynamic credentials to your stack by configuring Pulumi ESC
    - How to add policy checks to test your infrastructure before each deployment
    - How to add a cron job to the pipeline to check for changes periodically (drift)
    - How to configure a dedicated cloud environment with Review Stacks

# The event presenters
presenters:
    - name: Ben De St Paer-Gotch
      role: Staff Product Manager, GitHub
      photo: /images/people/ben-de-st-paer-gotch.jpg

# case-sensitive
tags:
    level: Advanced # Beginner, Intermediate, Advanced
    topics: ["GitHub Actions","DevOps", "CI/CD"]
    languages: []
    clouds: ["AWS"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: af82ece6-c2e2-4311-ac92-0785b259e3cb
    salesforce_campaign_id: 701PQ00000FDALtYAP
---
