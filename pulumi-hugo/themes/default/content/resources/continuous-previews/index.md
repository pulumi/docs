---
# Name of the webinar.
title: "Continuous Previews"
meta_desc: Attendees will leave this session ready to take control of their development process in ways they may not have known were possible.

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
url_slug: "continuous-previews"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Continuous Previews"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Continuous Previews"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/n2T_6RqCxMQ"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2021-10-20T15:00:00-07:00
    # Duration of the webinar.
    duration: "17 minutes"
    # Description of the webinar.
    description: |
        Continuous Integration and Continous Deployments have been part of our application lifecycle for some time now but what about Continuous Previews? The ability to easily share new features and changes to a wide audience within your organization is a game changer for accelerating the delivery of features your users need. In this talk we will walk you through everything you need to know to deploy a Continuous Previews pipeline. Starting with containerizing your application, deploying to a cluster and connecting the results back to a GitHub Pull Request. Attendees will leave this session ready to take control of their development process in ways they may not have known were possible.

    # The webinar presenters
    presenters:
        - name: Peter McKee
          role: Head of Developer Relations, Docker
        - name: Josh Thurman
          role: Developer Relations at Uffizzi

# This section contains the transcript for a video. It is optional.
transcript: |
    Transcript is coming soon.
---
