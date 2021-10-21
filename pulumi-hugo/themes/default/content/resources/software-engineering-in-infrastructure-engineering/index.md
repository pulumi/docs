---
# Name of the webinar.
title: "Software Engineering in Infrastructure Engineering"
meta_desc: In this talk, you will go through how to use the software engineering process to solve this infrastructure engineering problem.

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
url_slug: "software-engineering-in-infrastructure-engineering"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Software Engineering in Infrastructure Engineering"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Software Engineering in Infrastructure Engineering"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/T0lbD5n9ID8"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2021-10-20T09:30:00-07:00
    # Duration of the webinar.
    duration: "18 minutes"
    # Description of the webinar.
    description: |
        When we think about the concept that is Software Engineering, we think about building well-designed software that solves the problems our customers face. The key takeaway here is that software engineers are problem solvers.

        In the world of infrastructure deployments, there are many problems that exist because of the software engineering problems we are trying to solve. Pretty ironic, right? We attempt to solve problems only to create more :). A major problem for a cloud service is having multiple instances of the service in multiple regions and maintaining high availability for users.

        As great as IaC (Infrastructure as Code) is, it can be a problem maintaining different configurations for different environments where each environment has multiple instances with varying configurations.

        In this talk, I will go through how I use the software engineering process in conjunction with pulumi stacks and state, to solve this infrastructure engineering problem.


    # The webinar presenters
    presenters:
        - name: Adora Nwodo
          role: Software Engineer at Microsoft

# This section contains the transcript for a video. It is optional.
transcript: |
    Transcript is coming soon.
---
