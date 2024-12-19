---
# Name of the event, <= 60 characters
title: Getting started with CI/CD for AWS using GitHub Actions
meta_desc: In this workshop, you will learn the fundamentals of an infrastructure CI/CD pipeline through guided exercises. You will use GitHub Actions and Pulumi.
meta_image:

# A featured webinar will display first in the list.
featured: false

# Webinars with unlisted as true will not be shown on the webinar list
unlisted: true

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
url_slug: getting-started-with-ci-cd-for-aws-pulumi-github-actions

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Getting started with CI/CD for AWS using GitHub Actions

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url:

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2024-11-27T11:00:00.000+11:00

    # Duration of the webinar.
    duration: 90 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        In this workshop, you will become familiar with the core concepts needed to deploy cloud resources continuously. You'll define Infrastructure as Code (IaC), and configure Pulumi GitHub Actions to deploy AWS resources after a commit and merge.

    learn:
        - The basics of the Pulumi programming model
        - The key components of a continuous pipeline
        - How to build your own infrastructure CI/CD pipeline
        - Configuring the Pulumi GitHub Actions to deploy AWS resources

    # The webinar presenters
    presenters:
        - name: Ben De St Paer-Gotch
          role: Staff Product Manager, GitHub
          photo: /images/people/ben-de-st-paer-gotch.jpg
        - name: Aurélien Requiem
          role: Customer Engineer, Pulumi
          photo: /images/team/aurelien-requiem.jpg

    # case-sensitive
    tags:
        level: Beginner # Beginner, Intermediate, Advanced
        topics: ["CI/CD", "GitHub Actions"]
        languages: []
        clouds: ["AWS"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: f7e56bad-4772-45cc-8e56-a49c4be45764
    salesforce_campaign_id: 701PQ00000N7ODGYA3

event_data:
  name: "Getting started with CI/CD for AWS using GitHub Actions"
  start_date: 2024-11-27T11:00:00.000+11:00
  end_date: 2024-11-27T12:30:00.000+11:00
  url: "https://www.pulumi.com/resources/getting-started-with-ci-cd-for-aws-pulumi-github-actions/"
  description: |
    In this workshop, you will become familiar with the core concepts needed to deploy cloud resources continuously. You'll define Infrastructure as Code (IaC), and configure Pulumi GitHub Actions to deploy AWS resources after a commit and merge.
---