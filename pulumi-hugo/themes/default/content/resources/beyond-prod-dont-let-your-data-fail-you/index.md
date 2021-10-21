---
# Name of the webinar.
title: "Beyond Prod: Don't Let Your Data Fail You"
meta_desc: This talk will deep-dive into how whylogs fits into the infrastructure as a whole and how it can enable end-to-end observability for your data stack.

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
url_slug: "beyond-prod-dont-let-your-data-fail-you"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Beyond Prod: Don't Let Your Data Fail You"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Beyond Prod: Don't Let Your Data Fail You"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/OjCBDRDe9IA"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2021-10-20T09:00:00-07:00
    # Duration of the webinar.
    duration: "27 minutes"
    # Description of the webinar.
    description: |
        In the era of microservices, decentralized ML architectures and complex data pipelines, data quality has become a bigger challenge than ever. While infrastructure-as-code and DevOps frameworks such as Pulumi enable best practices in managing and testing the infrastructure and software, much is left to be desired for managing data quality. As data becomes more entangled in software-based decisions, it’s critical for companies to start treating data with similar rigor to what the DevOps world has. In this talk, we will address this challenge through whylogs, an open source standard for data logging. We’ll deep-dive how whylogs fit into the general infrastructure as a whole and how it can enable end-to-end observability and monitoring for your data stack. This shift in paradigm will enable companies that operate with data to move faster and safer by building discipline and processes around data.

    # The webinar presenters
    presenters:
        - name: Andy Dang
          role: Co-Founder and Engineering Lead, WhyLabs

# This section contains the transcript for a video. It is optional.
transcript: |
    Transcript is coming soon.
---
