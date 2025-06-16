---
# Name of the event, <= 60 characters
title: "Golden Paths: Infrastructure Components and Templates"
meta_desc: Create reusable infrastructure components and templates that enable developer self-service while enforcing standards.
meta_image:

# A featured webinar will display first in the list.
featured: false

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
url_slug: golden-paths

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Golden Paths: Infrastructure Components and Templates"
    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: 

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2025-08-06T12:00:00-04:00

    # Duration of the webinar.
    duration: 60 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        Golden paths are the foundation of successful Internal Developer Platforms—providing developers with pre-approved, production-ready infrastructure patterns they can self-serve. This hands-on workshop teaches you to build reusable Pulumi components and templates that encapsulate your organization's best practices. You'll learn to create composable building blocks that make the right thing the easy thing, reducing cognitive load for developers while maintaining operational excellence.
    learn:
        - How to design and build reusable Pulumi components for common infrastructure patterns
        - Template creation strategies that balance flexibility with opinionated defaults
        - Component composition techniques for building complex infrastructure applications from simple building blocks.

    # The webinar presenters
    presenters:
        - name: Rob Smith
          role: Solutions Architect, Pulumi
          photo: /images/team/Rob-Smith.png
        - name: Engin Diri
          role: Senior Solutions Architect, Pulumi
          photo: /images/team/engin-diri.jpg

    # case-sensitive
    tags:
        level: Intermediate # Beginner, Intermediate, Advanced
        topics:  ["Platform Engineering", "IaC", "Components"]
        clouds: ["AWS"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 8bca877b-1398-442f-88ea-16ae11b77182
    salesforce_campaign_id: 701PQ00000ZYBbEYAX

event_data:
  name: "Golden Paths: Infrastructure Components and Templates"
  start_date: 2025-08-06T12:00:00-04:00
  end_date: 2025-00-06T13:00:00-04:00
  url: "https://www.pulumi.com/resources/golden-paths/"
  description: |
        Golden paths are the foundation of successful Internal Developer Platforms—providing developers with pre-approved, production-ready infrastructure patterns they can self-serve. This hands-on workshop teaches you to build reusable Pulumi components and templates that encapsulate your organization's best practices. You'll learn to create composable building blocks that make the right thing the easy thing, reducing cognitive load for developers while maintaining operational excellence.
--- 