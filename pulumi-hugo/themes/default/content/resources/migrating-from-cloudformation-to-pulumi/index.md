---
# Name of the webinar.
title: "Panther - Migrating from CloudFormation to Pulumi"
meta_desc: Dennis Webb, Staff Software Engineer at Panther, describes his team's journey to move their infrastructure code from CloudFormation to Pulumi.

cloud_engineering_days:
    track: customer_stories

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
url_slug: "migrating-from-cloudformation-to-pulumi"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Migrating from CloudFormation to Pulumi"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Migrating from CloudFormation to Pulumi"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/BA11lhWSxZk?rel=0"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2022-11-02T10:20:00-07:00
    # Duration of the webinar.
    duration: "26 minutes"
    # Description of the webinar.
    description: |
        Dennis Webb, Staff Software Engineer at Panther, describes best practices and his team's journey to move their infrastructure code from CloudFormation to Pulumi. He provides tips and insights to teams considering modernizing their own infrastructure.

    # The webinar presenters
    presenters:
        - name: Dennis Webb
          role: Staff Software Engineer, Panther
---
