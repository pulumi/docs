---
# Name of the event, <= 60 characters
title: What's New in Pulumi
meta_desc: Explore the latest features and updates in Pulumi, and learn how these enhancements can streamline your cloud infrastructure management.
meta_image: /images/resources/Whats-New-Meagan-Arun.png
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
url_slug: whats-new-pulumi-cloud

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: What's New in Pulumi

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: https://www.youtube.com/embed/xLcSUdpgtvg?si=Q5KYcL6khAVg6RwT?rel=0

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2024-02-29T09:00:00.000-08:00

    # Duration of the webinar.
    duration: 1 hour

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        Join our 'What's New in Pulumi' workshop to explore the latest features and updates in Pulumi. Learn how these enhancements can streamline your cloud infrastructure management, with practical demonstrations and insights into advanced deployment techniques. Ideal for developers looking to leverage Pulumi's cutting-edge tools for efficient cloud solutions.

    learn:
        - What's new; recent features and updates to Pulumi Cloud
        - How to leverage new solutions to support advanced deployment techniques

    # The webinar presenters
    presenters:
        - name: Meagan Cojocar
          role: Principal Product Manager, Pulumi
          photo: /images/team/meagan-cojocar.jpg
        - name: Arun Loganathan
          role: Senior Product Manager, Pulumi
          photo: /images/team/arun-loganathan.jpg

    # case-sensitive
    tags:
        level: Beginner # Beginner, Intermediate, Advanced
        topics: ["Pulumi Features"]
        languages: []

# The right hand side form section.
form:
    hubspot_form_id: cce553c0-f9ba-49f7-b8b4-f37426d7f743
    salesforce_campaign_id: 701PQ00000683jgYAA
---
