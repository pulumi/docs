---
# Name of the event, <= 60 characters
title: Getting Started with Infrastructure as Code on DigitalOcean
meta_desc: In this hands-on workshop, you will learn how to stand up basic services using Infrastructure as Code through a series of hands-on labs.
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
url_slug: getting-started-with-infrastructure-as-code-on-digital-ocean

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Getting Started with Infrastructure as Code on DigitalOcean

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: https://www.youtube.com/embed/VEJg-PGL8dk?rel=0

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2022-11-17T09:00:00-07:00

    # Duration of the webinar.
    duration: 90 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        In this hands-on workshop, the Pulumi and the DigitalOcean teams will show you how to stand up basic services using Infrastructure as Code (IaC) through a series of hands-on labs.ects.

    learn:
        - How to use Pulumi to provision cloud resources
        - How to use IaC on DigitalOcean

    # The webinar presenters
    presenters:
        - name: Josh Kodroff
          role: Sr Solutions Architect, Pulumi
          photo: /images/team/josh-kodroff.jpg
        - name: Christian Nunciato
          role: Technical Content Lead, Pulumi
          photo: /images/team/christian-nunciato.jpg
        - name: Chris Sevilleaja
          role: Senior Developer Advocate, DigitalOcean

    # case-sensitive
    tags:
        level: Beginner # Beginner, Intermediate, Advanced
        topics: ["DigitalOcean"]
        languages: []

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 7498bb01-dceb-4519-ab4e-9413355ada23
    salesforce_campaign_id:
---
