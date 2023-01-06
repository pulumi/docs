---
# Name of the webinar.
title: "Infrastructure as Software Best Practices"
meta_desc: Luke Hoban and Mitch Gerdisch go through these practices and how to apply them to your cloud infrastructure.

cloud_engineering_days:
    track: best_practices
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
layout: cloud-engineering-days-replay

# External webinars will link to an external page instead of a webinar
# landing/registration page. If the webinar is external you will need
# set the 'block_external_search_index' flag to true so Google does not index
# the webinar page created.
external: false
block_external_search_index: false

# The url slug for the webinar landing page. If this is an external
# webinar, use the external URL as the value here.
url_slug: "infrastructure-as-software-best-practices"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Infrastructure as Software Best Practices"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Infrastructure as Software Best Practices"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/wnFBywu7SXM?rel=0"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2022-11-02T09:30:00-07:00
    # Duration of the webinar.
    duration: "31 minutes"
    # Description of the webinar.
    description: |
        Infrastructure as Code best practices are about applying software engineering practices. In this talk,
        Luke Hoban and Mitch Gerdisch go through these practices and how to apply them to your cloud infrastructure as an individual developer, a team, or an organization. In the process, they will introduce key concepts such as secrets management, Pulumi components, and more.   

    # The webinar presenters
    presenters:
        - name: Luke Hoban
          role: CTO, Pulumi
        - name: Mitch Gerdisch
          role: Solutions Architect, Pulumi
---
