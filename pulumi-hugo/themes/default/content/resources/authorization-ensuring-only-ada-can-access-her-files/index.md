---
# Name of the webinar.
title: "Authorization: Ensuring Only Ada Can Access Her Files"
meta_desc: In this talk, you will get a high level overview of the authorization landscape and learn how Split approached these unique challenges.

cloud_engineering_summit:
    track: manage

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
url_slug: "authorization-ensuring-only-ada-can-access-her-files"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Authorization: Ensuring Only Ada Can Access Her Files"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Authorization: Ensuring Only Ada Can Access Her Files"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/WaBjJhCATWg"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2021-10-20T14:30:00-07:00
    # Duration of the webinar.
    duration: "22 minutes"
    # Description of the webinar.
    description: |
        When an application is small, few or even no permissions are needed.  However, as they grow larger, it is common to have increasingly complex permissions models.  While things are still small, it's easy to meet these needs through something built in-house, but as they become more complex, a better model is often needed.

        The world of authorization solves precisely this problem.  There are several common models, including ACLs, RBAC, and ABAC, which work well for different use-cases.  In addition, there are several higher level architectures for implementing one of these as well as a number of different products available.

        In this talk, I will discuss a high level overview of the authorization landscape.  I will then delve into more depth about how we approached this problem at both Box and Split and some of the things we considered.  I will include the pros and cons for the various options with regards to our use-cases and what we ultimately chose to do.

    # The webinar presenters
    presenters:
        - name: Joy Ebertz
          role: Sr. Staff Engineer, Split

# This section contains the transcript for a video. It is optional.
transcript: |
    Transcript is coming soon.
---
