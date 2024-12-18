---
# Name of the event, <= 60 characters
title: Platform Engineering with Pulumi and GitLab
meta_desc: Learn how to use Pulumi's GitLab integration to build CI/CD pipelines, empowering teams to deliver software safely, reproducibly, and faster.
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
url_slug: platform-engineering-with-pulumi-and-gitlab

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Platform Engineering with Pulumi and GitLab

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url:

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2024-08-21T09:00:00-07:00

    # Duration of the webinar.
    duration: 90 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        During this workshop, you will discover how to use Pulumi's integration with GitLab to create and manage CI/CD pipelines for your cloud infrastructure. You will learn to use Pulumi's declarative infrastructure as code that enable both application and infrastructure teams to deliver secure, high-quality software more efficiently and reproducibly, while also minimizing risk and complexity. Join us to improve your platform team's ability to efficiently and flexibly manage cloud resources.

    learn:
        - How to create GitLab pipelines for your infrastructure as code.
        - How to use the GitLab Pulumi provider to manage your GitLab resources.
        - How to to use Pulumi's Policy as Code and ESC (Environments, Secrets, and Config) to improve your organization's security posture.

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
        level: Intermediate # Beginner, Intermediate, Advanced
        topics: ["Automation", "CI/CD", "DevOps", "Platform Engineering", "Pulumi ESC"]
        languages: ["TypeScript"]
        clouds: ["AWS"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: bc1e8ce8-5379-4c99-9e29-0c29bf7e68d5
    salesforce_campaign_id: 701PQ00000GVMPdYAP
---
