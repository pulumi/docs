---
# Name of the event, <= 60 characters
title: Advanced CI/CD for AWS using Pulumi and GitHub Actions
meta_desc: Learn advanced topics that make up a robust infrastructure CI/CD pipeline through guided exercises.
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
url_slug: advanced-cicd-aws-pulumi-github-actions

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Advanced CI/CD for AWS using Pulumi and GitHub Actions

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url:

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2024-05-16T09:00:00.000-07:00

    # Duration of the webinar.
    duration: 90 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        In this workshop, you will learn advanced topics that make up a robust infrastructure CI/CD pipeline through guided exercises. You will use Pulumi tooling to take your cloud infrastructure pipeline one step closer to production.

        This workshop introduces users to advanced DevOps best practices. You will add compliance checks via policies, drift detection, and isolated test environments to an existing GitHub Actions pipeline. Accelerate your AWS projects with the code examples provided.

    learn:
        - How to build an advanced CI pipeline to enforce compliance and correct drift
        - How to add dynamic credentials to your stack by configuring Pulumi ESC
        - How to add policy checks to test your infrastructure before each deployment
        - How to add a cron job to the pipeline to check for changes periodically (drift)
        - How to configure a dedicated cloud environment with Review Stacks

    # The webinar presenters
    presenters:
        - name: Diana Esteves
          role: Solutions Architect, Pulumi
          photo: /images/team/diana-esteves.jpg

    # case-sensitive
    tags:
        level: Advanced # Beginner, Intermediate, Advanced
        topics: ["GitHub Actions", "AWS", "DevOps", "CI/CD"]
        languages: []

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 9a6e3798-5620-43ca-a948-86b382a15932
    salesforce_campaign_id: 701PQ000008k4ATYAY
---
