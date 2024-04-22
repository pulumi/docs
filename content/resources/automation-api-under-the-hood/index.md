---
# Name of the webinar.
title: "Automation API Under the Hood"
meta_desc: Evan Boyle and Casey Huang give you a guided tour of the Pulumi Automation API and Pulumi Deployments.

cloud_engineering_days:
    track: automate_deploy
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
url_slug: "automation-api-under-the-hood"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Automation API Under the Hood"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Automation API Under the Hood"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/8nAbrJg6KFM?rel=0"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2022-11-02T11:20:00-07:00
    # Duration of the webinar.
    duration: "17 minutes"
    # Description of the webinar.
    description: |
        Evan Boyle and Casey Huang give you a guided tour of the Pulumi Automation API and Pulumi Deployments.
        Pulumi's Automation API allows you to embed Pulumi within your application code, making it easy to create custom experiences on top of Pulumi that are tailored to your use case, domain, and team. 

    # The webinar presenters
    presenters:
        - name: Casey Huang
          role: Software Engineer, Pulumi
        - name: Evan Boyle
          role: Software Engineer, Pulumi
---
