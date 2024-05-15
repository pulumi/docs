---
# Name of the event, <= 60 characters
title: Getting Started with 1Password and Pulumi
meta_desc: Join us for a hands-on lab showing you how to integrate 1Password into your Pulumi workflow.
meta_image: /images/resources/1password-pulumi-jilian.png

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
url_slug: getting-started-with-1password-and-pulumi

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Getting Started with 1Password and Pulumi

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: https://www.youtube.com/embed/K_02cyfA5gE?si=QksmdY81T6Qjb2vO?rel=0

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2023-09-12T08:00:00-07:00

    # Duration of the webinar.
    duration: 30 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        Software developers need to secure their workflows to prevent the accidental exposure of API keys and other secrets. 1Password is known as a capable password manager, but [1Password Developer Tools](https://developer.1password.com/) also provide a set of capabilities to secure secrets throughout the software development lifecycle. 

        In this session, Sr. Software Engineer Jillian Morgan digs into how to use the 1Password CLI to manage secrets in a Pulumi workflow. Join Pulumi and 1Password for a short walkthrough of this powerful new feature and get your questions answered by the experts.

    learn:
        - How to create policies for resource level validation.
        - How to create Policy Packs for orgainizing organization wide policies.

    # The webinar presenters
    presenters:
        - name: Ringo De Smet
          role: Customer Experience Architect, Pulumi
          photo: /images/team/ringo-de-smet.jpg
        - name: Jillian Morgan
          role: Senior Software Engineer, 1Password

    # case-sensitive
    tags:
        level: Beginner # Beginner, Intermediate, Advanced
        topics: ["1Password"]
        languages: []

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 18a7dd50-d3d8-480f-bf3a-af97706593c7
    salesforce_campaign_id: 701Du000000AnO6IAK
---
