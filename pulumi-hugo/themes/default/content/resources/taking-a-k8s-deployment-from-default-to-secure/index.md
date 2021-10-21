---
# Name of the webinar.
title: "Taking a K8s Deployment from Default to Secure"
meta_desc: In this session we'll start with a default Nginx deployment and leverage Checkov's Kubernetes yaml scanning capability to go from default to secure.

cloud_engineering_summit:
    track: build

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
url_slug: "taking-a-k8s-deployment-from-default-to-secure"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Taking a K8s Deployment from Default to Secure"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Taking a K8s Deployment from Default to Secure"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/ouj_0Yx4Mg8"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2021-10-20T10:20:00-07:00
    # Duration of the webinar.
    duration: "25 minutes"
    # Description of the webinar.
    description: |
        A Shodan search can quickly reveal over 17 million Nginx servers currently returning a 200 OK. One would think with such adoption that building a secure Nginx Kubernetes deployment would be easy. Surely one would be overwhelmed with online content!

        Whilst best practices are in abundance and security scanning tools for helm and k8s yaml are available, it can be truly difficult to find example code or solid advice on how to successfully follow security best practices. In this session I'll start with a blank canvas of a default Nginx deployment and leverage Checkov's Kubernetes yaml scanning capability to show my own experiences with the easy, the hard and the plain confusing elements of creating a secure Nginx deployment.

    # The webinar presenters
    presenters:
        - name: Steve Giguere
          role: Developer Advocate, Bridgecrew by Palo Alto

# This section contains the transcript for a video. It is optional.
transcript: |
    Transcript is coming soon.
---
