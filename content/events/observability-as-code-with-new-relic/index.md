---
# Name of the event, <= 60 characters
title: Observability as Code with Pulumi and New Relic
meta_desc: Observability is a key component of any site reliability strategy and New Relic and Pulumi make it easier than ever to define metrics, alerts, and dashboards.
meta_image: 
# A featured webinar will display first in the list.
featured: false

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
url_slug: observability-as-code-with-new-relic

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Observability as Code with Pulumi and New Relic

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: https://www.youtube.com/embed/0f7Pp1uDtbQ?rel=0

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2023-02-14T09:00:00-08:00

    # Duration of the webinar.
    duration: 90 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        Getting your infrastructure and application deployed on AWS is an important first step but how do you make sure that your new capabilities are running reliably in production? Observability is a key component of any site reliability strategy and New Relic and Pulumi make it easier than ever to define metrics, alerts, and dashboards using popular programming languages.

    learn:
        - Defining and managing observability capabilities using JavaScript/TypeScript
        - Creating cloud resources using infrastructure as code and deploying an example app
        - How to define metrics and alerts to ensure your app and infrastructure are healthy

    # The webinar presenters
    presenters:
        - name: Josh Kodroff
          role: Senior Solutions Architect, Pulumi
          photo: /images/team/josh-kodroff.jpg
        - name: Ptah Dunbar
          role: Solutions Consultant, New Relic

    # case-sensitive
    tags:
        level: Intermediate # Beginner, Intermediate, Advanced
        topics: ["New Relic", "Observability"]
        languages: []

# The right hand side form section.
form:
  hubspot_form_id: c1b68f53-f7c8-4f6e-a211-3cc42bd2a950
  salesforce_campaign_id: 701Du0000009YQXIA2
---
