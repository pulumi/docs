---
# Name of the webinar.
title: "How to Author and Publish Pulumi Packages"
meta_desc: "In this workshop, we’ll guide you through an example of building a reusable Pulumi component for a hypothetical “production ready application” in Python."

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
url_slug: "build-reusable-infrastructure-as-code-patterns"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "How to Author and Publish Pulumi Packages"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "How to Author and Publish Pulumi Packages"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/3BaDCrCw5FM"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2021-10-21T12:00:00-07:00
    # Duration of the webinar.
    duration: "1 hour"
    # Datetime of the webinar.
    datetime: "OCTOBER 21st, 2021"
    # Description of the webinar.
    description: |
        One of the great benefits of adopting [Infrastructure as Code](/what-is/what-is-infrastructure-as-code/) is that you can drastically reduce the amount of repetition when declaring your infrastructure. Using familiar languages like Python means you can use functions, loops and object oriented programming paradigms to reduce the boilerplate.

        In this workshop, we’ll guide you through an example of building a reusable Pulumi component for a hypothetical “production ready application” in Python and help you understand how to build reusable abstractions for your infrastructure as code workflow.


    # The webinar presenters
    presenters:
        - name: Lee Briggs
          role: Sales Engineer, Pulumi

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - How to build reusable Pulumi Components.
        - How to manage the components you build.
        - How to deploy these components for use by other engineers.

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: fa3c8cbb-64bd-4c8a-bd16-3b1b3a5e2d24
---
