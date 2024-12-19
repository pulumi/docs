---
# Name of the event, <= 60 characters
title: Building Web-Scale Cloud Applications with Go and IaC
meta_desc: Learn to use Go and Pulumi in building robust, web-scale cloud applications.
meta_image: /images/resources/web-scale-cloud-app-golang-iac_engin.png

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
url_slug: build-web-scale-cloud-app-golang-iac

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Building Web-Scale Cloud Applications with Go and IaC

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: https://www.youtube.com/embed/kOqzJFeTkto?rel=0

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2023-10-16T07:00:00-07:00

    # Duration of the webinar.
    duration: 1 hour

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
      In the modern era of cloud computing, building scalable and reliable applications is a necessity. Join us in this hands-on workshop as we dive deep into the world of Infrastructure as Code (IaC) using Pulumi and Go. Tailored for Go developers new to Pulumi, this workshop will guide you through the foundational concepts of IaC, showcasing how Go can be leveraged to design robust cloud applications ready for web-scale.

    learn:
      - Basics of Infrastructure as Code with Pulumi.
      - Using Go with Pulumi for cloud resource management.
      - Best practices for scalable cloud applications with Go and Pulumi.

    # The webinar presenters
    presenters:
        - name: Engin Diri
          role: Customer Experience Architect, Pulumi
          photo: /images/team/engin-diri.jpg

    # case-sensitive
    tags:
        level: Beginner # Beginner, Intermediate, Advanced
        topics: []
        languages: ["Golang"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: ad45d1ab-8514-4e5e-ad1f-862216bf8244
    salesforce_campaign_id: 701Du000000B2VAIA0
---
