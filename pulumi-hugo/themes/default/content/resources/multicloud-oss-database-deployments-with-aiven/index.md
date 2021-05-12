---
# Name of the webinar.
title: "Building with Any Language, Any Cloud and Any OSS Database"
meta_desc: "With Pulumi and Aiven, you can build multi-cloud applications using the language of your choice, the database of your choice, and the cloud of your choice."

# A featured webinar will display first in the list.
featured: false

# If the video is pre-recorded or live.
pre_recorded: false

# If the video is part of the PulumiTV series. Setting this value to true will list the video in the "PulumiTV" section.
pulumi_tv: false

# The preview image will be shown on the list page.
preview_image: ""

# Webinars with unlisted as true will not be shown on the webinar list
unlisted: true

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
url_slug: "multicloud-oss-database-deployments-with-aiven"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Building with Any Language, Any Cloud and Any Open Source Database with Pulumi and Aiven"
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
    title: "Building with Any Language, Any Cloud and Any Open Source Database with Pulumi and Aiven"
    # URL for embedding a URL for ungated webinars.
    youtube_url: ""
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2021-05-13T11:00:00-07:00
    # Duration of the webinar.
    duration: "1 hour"
    # Datetime of the webinar.
    datetime: "May 13th, 2021"
    # Description of the webinar.
    description: |
        With Pulumi and Aiven, you can build robust, multi-cloud applications using the language of your choice, the open source database of your choice, and the cloud of your choice.  Join Pulumi engineer Paul Stack and Aiven solution architect Trevor Kennedy to see how easy it is to define, deploy and manage production-ready apps.

    # The webinar presenters
    presenters:
        - name: Paul Stack
          role: Software Engineer, Pulumi
        - name: Trevor Kennedy
          role: Solutions Architect, Aiven

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - How Pulumi infrastructure as code makes it easy to define resources across clouds.
        - How Aiven simplifies database provisioning and management for Postgres, MySQL, Kafka, Cassandra, Elasticsearch on multiple clouds
        - How to combine solutions so that your applications can be hosted anywhere and moved across clouds and regions with zero downtime.

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: b51aa29f-63e9-4935-a929-8a3b55804c92
---
