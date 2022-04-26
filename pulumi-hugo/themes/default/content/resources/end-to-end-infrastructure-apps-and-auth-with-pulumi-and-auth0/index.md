---
# Name of the webinar.
title: "End-To-End Infrastructure, Apps, and Auth with Auth0"
meta_desc: "In this session, we’ll walk you through the process of building and deploying a web app with React, Express, MongoDB, Auth0, and Pulumi."

# A featured webinar will display first in the list.
featured: false

# If the video is pre-recorded or live.
pre_recorded: false

# If the video is part of the PulumiTV series. Setting this value to true will list the video in the "PulumiTV" section.
pulumi_tv: false

# The preview image will be shown on the list page.
preview_image: ""

# Webinars with unlisted as true will not be shown on the webinar list
unlisted: false

# Gated webinars will have a registration form and the user will need
# to fill out the form before viewing.
gated: true

# The layout of the landing page.
type: webinars

# External webinars will link to an external page instead of a webinar
# landing/registration page. If the webinar is external you will need
# set the 'block_external_search_index' flag to true so Google does not index
# the webinar page created.
external: false
block_external_search_index: false

# The url slug for the webinar landing page. If this is an external
# webinar, use the external URL as the value here.
url_slug: "end-to-end-infrastructure-apps-and-auth-with-pulumi-and-auth0"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "End-To-End Infrastructure, Apps, and Auth with Auth0"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Webinar pages support multiple session via the 'multiple' property.
# multiple:
#   - datetime: 2020-02-05T10:00:00-07:00
#     hubspot_form_id: ""
#     gotowebinar_key: ""

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "End-To-End Infrastructure, Apps, and Auth with Auth0"
    # URL for embedding a URL for ungated webinars.
    youtube_url: ""
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2022-06-07T16:00:00-07:00
    # Duration of the webinar.
    duration: "1 hour"
    # Datetime of the webinar.
    datetime: ""
    # Description of the webinar.
    description: |
        In this session, we’ll walk you through the process of building a three-tier web app: a single-page app built with React, a back end consisting of a REST API managed with Express and MongoDB. We’ll also show you how to enable authentication to restrict access to your app.

        Everything will be configured and deployed to the cloud using Pulumi.

    # The webinar presenters
    presenters:
        - name: Matt Stratton
          role: Staff Developer Advocate, Pulumi
        - name: Ben Dechrai
          role: Senior Developer Advocate, Auth0

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - How to provision Auth0 alongside cloud resources using JavaScript and Pulumi
        - How to deploy a basic web app with authentication enabled.
        - Common-sense policies for avoiding mistakes in production.

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: "07b9a29f-5eb7-484b-8e99-b3ab79c558c2"
---
