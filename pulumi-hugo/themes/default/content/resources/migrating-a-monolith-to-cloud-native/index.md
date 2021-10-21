---
# Name of the webinar.
title: "Migrating a monolith to Cloud-Native"
meta_desc: In this talk you will learn how to migrate a large monolith codebase to Cloud-Native and learn a few gotchas along the way.

cloud_engineering_summit:
    track: deploy

# A featured webinar will display first in the list.
featured: false

# If the video is pre-recorded or live.
pre_recorded: true

# If the video is part of the PulumiTV series. Setting this value to true will list the video in the "PulumiTV" section.
pulumi_tv: false

# Webinars with unlisted as true will not be shown on the webinar list
unlisted: false

# Gated webinars will have a registration form and the user will need
# to fill out the form before viewing.
gated: false

# The layout of the landing page.
type: webinars
layout: cloud-engineering-summit-replay

# External webinars will link to an external page instead of a webinar
# landing/registration page. If the webinar is external you will need
# set the 'block_external_search_index' flag to true so Google does not index
# the webinar page created.
external: false
block_external_search_index: false

# The url slug for the webinar landing page. If this is an external
# webinar, use the external URL as the value here.
url_slug: "migrating-a-monolith-to-cloud-native"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Migrating a monolith to Cloud-Native"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Migrating a monolith to Cloud-Native"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/0Jnq-M_7se0"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2021-10-20T15:30:00-07:00
    # Duration of the webinar.
    duration: "24 minutes"
    # Description of the webinar.
    description: |
        So your company has finally decided to move to the Cloud Native ecosystem. You’ve landed on containerization as your first step. You heard that all you needed to do was containerize your first app and then push it to Kubernetes/OpenShift/Nomad, and the cost savings just come. You’ve done this, and well, things have gone not as planned. Some of the tech didn’t do what you expected, and wait, what do you mean our OpEx has gone up?

        Simply said: the promise of containerization or migrating to the Cloud Native ecosystem can be a lie if you don’t do your homework. Sadly most companies don’t. In this talk, I’ll explain a few gotchas that a “few” enterprises, in the guise of AsgharLabs, hit moving towards the Cloud Native world, and hopefully, you’ll learn from their mistakes, so you’re trip down this path will be more comfortable and closer to the promise.

    # The webinar presenters
    presenters:
        - name: JJ Asghar
          role: Developer Advocate, IBM cloud

# This section contains the transcript for a video. It is optional.
transcript: |
    Transcript is coming soon.
---
