---
# Name of the event, <= 60 characters
title: Getting started on AWS with Typescript
meta_desc: Learn how to manage AWS infrastructure using TypeScript and Pulumi. Define, deploy, and manage cloud resources using familiar programming practices.
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
url_slug: getting-started-with-iac-aws-typescript

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Getting started on AWS with TypeScript

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url:

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2026-04-15T09:00:00.000-07:00

    # Duration of the webinar.
    duration: 60 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        This workshop explores how modern infrastructure management on Amazon Web Services (AWS) can be streamlined using infrastructure as code and familiar programming languages. You’ll learn how Pulumi enables teams to define, deploy, and manage AWS infrastructure using TypeScript, applying established software engineering practices to cloud infrastructure.

        Through guided examples, diagrams, and walkthroughs, the session shows how Pulumi’s programming model connects application and infrastructure development. This approach makes AWS architectures easier to understand, change, and maintain, while reducing friction when managing infrastructure across projects and environments.
    learn:
        - How to model AWS infrastructure using TypeScript and familiar programming constructs
        - How infrastructure as code improves reliability and repeatability on AWS
        - How Pulumi supports consistent infrastructure management across environments

    # The webinar presenters
    presenters:
        - name: Engin Diri
          role: Senior Solutions Architect, Pulumi
          photo: /images/team/engin-diri.jpg

    # case-sensitive
    tags:
        level: Beginner # Beginner, Intermediate, Advanced
        topics: ["IaC", "DevOps", "Automation"]
        languages: ["TypeScript"]
        clouds: ["AWS"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 644d3f9d-9e44-49dd-8e8b-13a80f0457c5
    salesforce_campaign_id: 701PQ00000qEPv7YAG
event_data:
    name: "Getting started on AWS with TypeScript"
    start_date: 2026-04-15T09:00:00.000-07:00
    end_date: 2026-04-15T10:00:00.000-07:00
    url: "https://www.pulumi.com/events/getting-started-with-iac-aws-typescript/"
    description: |
        Learn how to manage AWS infrastructure using TypeScript and Pulumi. Define, deploy, and manage cloud resources using familiar programming practices.
---
