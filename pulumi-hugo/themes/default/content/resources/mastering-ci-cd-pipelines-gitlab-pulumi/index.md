---
# Name of the event, <= 60 characters
title: Mastering CI/CD Pipelines with Pulumi and GitLab
meta_desc: In this workshop, you'll learn how to use Pulumi's deep integration with GitLab to create and manage CI/CD pipelines for your infrastructure.
meta_image: /images/resources/cicd-gitlab.png

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
url_slug: mastering-ci-cd-pipelines-gitlab-pulumi

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Mastering CI/CD Pipelines with Pulumi and GitLab

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url:

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2024-04-03T09:00:00.000-07:00

    # Duration of the webinar.
    duration: 90 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        In the ever-evolving landscape of DevOps and platform engineering, platform engineers are always seeking efficient and flexible tools to manage their cloud resources, especially when it comes to continuous integration/continuous delivery (CI/CD) pipelines.
        
        In this workshop, you'll learn how to use Pulumi's deep integration with GitLab to create and manage CI/CD pipelines for your infrastructure in a declarative function to empower your application and infrastructure teams to deliver safely, reproducably, and quickly.

    learn:

    # The webinar presenters
    presenters:
        - name: Josh Kodroff
          role: Sr. Solutions Architect, Pulumi
          photo: /images/team/josh-kodroff.jpg
        - name: Matt Genelin
          role: Solutions Architect, GitLab
          photo: /images/people/matt-genelin.jpg

    # case-sensitive
    tags:
        level:  # Beginner, Intermediate, Advanced
        topics: ["CI/CD", "DevOps", "GitLab"]
        languages: ["TypeScript"]
        clouds: ["AWS"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 66338b61-db6c-472a-b4b6-f8ad4b1c9ebe
    salesforce_campaign_id: 701PQ0000080HCPYA2
---
