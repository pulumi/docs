---
# Name of the video.
title: "Name of the video"
meta_desc: "Search Description"

# A featured video will display first in the list.
featured: false

pre_recorded: true
pulumi_tv: true
unlisted: false

# Gated videos will have a registration form and the user will need
# to fill out the form before viewing.
gated: false

# The layout of the landing page.
type: webinars

external: false
block_external_search_index: false

# The url slug for the video landing page. If this is an external
# video, use the external URL as the value here.
url_slug: "{{ .Name }}"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: ""

# Content for the left hand side section of the page.
main:
    # Video title.
    title: ""
    # URL for embedding a URL for ungated videos.
    youtube_url: ""
    # Sortable date. The datetime Hugo will use to sort the videos in date order.
    sortable_date: 2021-02-05T10:00:00-07:00
    # Duration of the video.
    duration: "2 hours"
    # Description of the video.
    description: ""

    # The video presenters
    presenters:
        - name: ""
          role: ""

# This section contains the transcript for a video. It is optional.
transcript: |
    Here is where you would put the transcript for a recorded video.
---
