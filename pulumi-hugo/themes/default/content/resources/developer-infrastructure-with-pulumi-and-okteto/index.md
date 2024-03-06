---
# Name of the event, <= 60 characters
title: Developer Infrastructure with Pulumi and Okteto
meta_desc: Learn the essentials of automating cloud resource provisioning with Pulumi and Okteto in this hands-on session.
meta_image: /images/resources/developer-infra-okteto-engin-arsh.png

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
url_slug: developer-infrastructure-with-pulumi-and-okteto

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Developer Infrastructure with Pulumi and Okteto

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: https://www.youtube.com/embed/HuJNtRGXjs8?si=v_DZwOvZi6uF6L9W?rel=0

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2024-03-04T09:00:00.000-08:00

    # Duration of the webinar.
    duration: 1 hour

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        In this workshop, you will learn the essentials of automating cloud resource provisioning with Pulumi and Okteto. This hands-on session is tailored for developers and platform engineers eager to adopt Infrastructure as Code (IaC) practices using familiar programming languages. Learn how to deploy cloud resources efficiently across any cloud provider and enhance your development workflow with Okteto's on-demand environments.
    
        Perfect for those looking to streamline their development process and foster better collaboration between teams, this workshop promises to equip you with practical skills for more effective cloud resource management.

    learn:
        - How to create self-serviced, production-like development environments
        - How Okteto and Pulumi work together
        - How to provision and de-provision cloud resources in Okteto with Pulumi

    # The webinar presenters
    presenters:
        - name: Arsh Sharma
          role: Developer Experience Engineer, Okteto
          photo: /images/people/arsh-sharma.jpg
        - name: Engin Diri
          role: Sr. Solutions Architect, Pulumi
          photo: /images/team/engin-diri.jpg

    # case-sensitive
    tags:
        level: Beginner # Beginner, Intermediate, Advanced
        topics: ["Platform Engineering", "Developer Experience", "Okteto"]
        languages: []

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 97146af6-3e33-4bed-a12e-99e861c328fd
    salesforce_campaign_id: 701PQ000006EP1iYAG
---
