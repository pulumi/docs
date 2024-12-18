---
# Name of the webinar.
title: "Keynote with Pulumi Founder/CEO and CTO"
meta_desc: Joe Duffy and Luke Hoban kick off Cloud Engineering Days with exciting new Pulumi announcements.

cloud_engineering_days:
    track: keynote

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
url_slug: "cloud-engineering-days-keynote"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Keynote with Pulumi Founder/CEO and CTO"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Keynote with Pulumi Founder/CEO and CTO"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/9B19Vuaq40A?rel=0"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2022-11-02T08:00:00-07:00
    # Duration of the webinar.
    duration: "1 hour"
    # Description of the webinar.
    description: |
        Joe Duffy and Luke Hoban kick off Cloud Engineering Days with exciting new Pulumi announcements.

    # The webinar presenters
    presenters:
        - name: Joe Duffy
          role: CEO, Pulumi
        - name: Luke Hoban
          role: CTO, Pulumi
---
