---
# Name of the webinar.
title: "What is OpenTelemetry?"
meta_desc: In this session you will learn how OpenTelemetry helps you understand your distributed system and the performance of individual services within it.

cloud_engineering_summit:
    track: build

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
url_slug: "what-is-opentelemetry"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "What is OpenTelemetry?"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "What is OpenTelemetry?"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/2Dg2m5a-RHo"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2021-10-20T14:30:00-07:00
    # Duration of the webinar.
    duration: "20 minutes"
    # Description of the webinar.
    description: |
        Microservices have broken monitoring tools and practices. Traditional methods of application logging and host-based metrics can’t provide accurate and timely signals for issues impacting production. OpenTelemetry solves this dilemma by providing a single set of APIs, SDKs, and automatic instrumentation tools that give you the ability to understand your distributed system and the performance of individual services within it.

    # The webinar presenters
    presenters:
        - name: Liz Fong-Jones
          role: Principal Developer Advocate, Honeycomb

# This section contains the transcript for a video. It is optional.
transcript: |
    Transcript is coming soon.
---
