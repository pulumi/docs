---
# Name of the webinar.
title: "Getting Started with Azure IaC and Review Stacks"
title_tag: "Getting Started with Azure IaC and Review Stacks (July 2023 Workshop)"
meta_desc: "In this workshop, we’ll explore the new Azure Native v2 provider and Pulumi Review Stacks on GitHub"
meta_image: "/images/resources/azure-iac-review-stacks.png"

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

# data for Google Events
event_data:
  name: Pulumi - Getting Started with Azure IaC and Review Stacks
  start_date: 2023-09-19T08:00:00.000-07:00
  end_date: 2023-09-19T09:00:00.000-07:00
  url: "https://www.pulumi.com/resources/azure-github-workshop"
  description: |
    When managing cloud infrastructure, it’s important to establish a build-test-release process for your team. In this session, experts from the Azure, GitHub, and Pulumi teams will show you how to use Pulumi’s Azure Native v2 provider and your favorite programming languages to stand up new projects on Azure quickly. Then, we’ll show you how Pulumi’s new Review Stacks feature creates a temporary cloud environment for every Pull Request in GitHub automatically – making it easier than ever to validate both infrastructure and app code before release.

# The url slug for the webinar landing page. If this is an external
# webinar, use the external URL as the value here.
url_slug: "azure-github-workshop"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Getting Started with Azure IaC and Review Stacks"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Webinar pages support multiple session via the 'multiple' property.
# multiple:

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Getting Started with Azure IaC and Review Stacks"
    # URL for embedding a URL for ungated webinars.
    youtube_url:
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2023-09-19T08:00:00.000-07:00
    # Duration of the webinar.
    duration: "90 minutes"
    # Datetime of the webinar.
    datetime: "7/27/2023 8:00am - 9:30am PDT"
    # Description of the webinar.
    description: |
        When managing cloud infrastructure, it’s important to establish a build-test-release process for your team. In this session, experts from the Azure, GitHub, and Pulumi teams will show you how to use Pulumi’s Azure Native v2 provider and your favorite programming languages to stand up new projects on Azure quickly. Then, we’ll show you how Pulumi’s new Review Stacks feature creates a temporary cloud environment for every Pull Request in GitHub automatically – making it easier than ever to validate both infrastructure and app code before release.

    # The webinar presenters
    presenters:
        - name: Josh Kodroff
          role: Sr. Solutions Architect, Pulumi
        - name: Brian Benz
          role: Senior Cloud Advocate, Microsoft Azure
        - name: April Edwards
          role: Senior Enterprise Advocate, GitHub

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - Infrastructure as Code on Azure
        - Serverless architectures
        - Setting up Review Stacks with GitHub and Pulumi

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 81828ab4-e433-4bfa-94a3-40b74ea2265c
    salesforce_campaign_id: 701Du000000Ab76IAC

aws_only: false
---
