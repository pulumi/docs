---
# Name of the webinar.
title: "Observability as Code with Pulumi and New Relic"
meta_desc: "Observability is a key component of any site reliability strategy and New Relic and Pulumi make it easier than ever to define metrics, alerts, and dashboards."

# A featured webinar will display first in the list.
featured: false

# If the video is pre-recorded or live.
pre_recorded: true

# If the video is part of the PulumiTV series. Setting this value to true will list the video in the "PulumiTV" section.
pulumi_tv: false

# The preview image will be shown on the list page.
preview_image: ""

# Webinars with unlisted as true will not be shown on the webinar list
unlisted: false

# Gated webinars will have a registration form and the user will need
# to fill out the form before viewing.
gated: false

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
url_slug: "observability-as-code-with-new-relic"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Observability as Code with Pulumi and New Relic"
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
    title: "Observability as Code with Pulumi and New Relic"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/0f7Pp1uDtbQ"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2023-02-14T09:00:00-08:00
    # Duration of the webinar.
    duration: "60 minutes"
    # Datetime of the webinar.
    datetime: ""
    # Description of the webinar.
    description: |
        Getting your infrastructure and application deployed on AWS is an important first step but how do you make sure that your new capabilities are running reliably in production? Observability is a key component of any site reliability strategy and New Relic and Pulumi make it easier than ever to define metrics, alerts, and dashboards using popular programming languages.

    # The webinar presenters
    presenters:
        - name: Josh Kodroff
          role: Senior Solutions Architect, Pulumi
        - name: Ptah Dunbar
          role: Solutions Consultant, New Relic

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - Defining and managing observability capabilities using JavaScript/TypeScript
        - Creating cloud resources using infrastructure as code and deploying an example app
        - How to define metrics and alerts to ensure your app and infrastructure are healthy

form:
    salesforce_campaign_id: "701Du0000009YQXIA2"
    hubspot_form_id: "c1b68f53-f7c8-4f6e-a211-3cc42bd2a950"
---
