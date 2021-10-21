---
# Name of the webinar.
title: "Lifecycle of a Pulumi Program"
meta_desc: In this talk, you will learn how Apple leveraged a custom state backend with SSO, RBAC, and pipelines powered by the Pulumi Automation API to drive IaC.

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
url_slug: "lifecycle-of-a-pulumi-program"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Lifecycle of a Pulumi Program"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Lifecycle of a Pulumi Program"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/5U7q9miKWj0"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2021-10-20T15:00:00-07:00
    # Duration of the webinar.
    duration: "24 minutes"
    # Description of the webinar.
    description: |
        Infrastructure as Code provides a way for teams and companies to standardize the way they manage and secure applications. In this talk, Fariba Khan and Stephen Van Gordon will share how they leverage a custom state backend with SSO, RBAC, and programmatically configurable pipelines powered by CICD tooling and the Pulumi Automation API to drive IaC at Apple.

        This framework of tools enables teams to provision secure-by-default Compute, Storage, Identity, Ingress, and other components available in multiple languages in very little time and without any manual interventions. This experience is complemented by operations-friendly workflows previewing infrastructure changes between deployments, as well as cost and policy violations directly in Github comments. This results in reduced cognitive overhead when making changes to a deployment. Finally, by providing the state store for IaC stacks our team gains insight into usage patterns, security issues, and compliance via rich data and analytics.

    # The webinar presenters
    presenters:
        - name: Fariba Khan
          role: Engineer, Cloud Services, Apple
        - name: Stephen Van Gordon
          role: Engineer, Cloud Services, Apple

# This section contains the transcript for a video. It is optional.
transcript: |
    Transcript is coming soon.
---
