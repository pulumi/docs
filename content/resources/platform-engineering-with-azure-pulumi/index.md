---
# Name of the event, <= 60 characters
title: Platform Engineering with Microsoft Azure and Pulumi
meta_desc: Accelerate deployment with our Azure and Pulumi workshop. Use Azure Deployment Environments for efficient cloud management and quick template distribution.

meta_image: "/images/resources/platform-engineering-azure.png"

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
url_slug: platform-engineering-with-azure-pulumi

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Platform Engineering with Microsoft Azure and Pulumi

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url:

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2024-06-20T09:00:00.000-07:00

    # Duration of the webinar.
    duration: 60 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        Platform engineering has become crucial for organizations with 50 or more engineers. As an extension of DevOps at scale, effective platform engineering empowers developers and development teams to utilize self-service capabilities.

        In this session, you will learn how to use Azure Deployment Environments to share click-to-deploy templates with your development teams. This session includes hands-on labs to help you create cloud resources that meet your requirements and share these capabilities across your organization.

    learn:
        - Infrastructure as Code concepts for C# developers
        - Managing Azure resources with Pulumi, with a focus on Azure Deployment Environments
        - Enabling IaC re-use across your organization

    # The webinar presenters
    presenters:
        - name: Sagar Chandra Reddy Lankala
          role: Sr Product Manager, Microsoft
          photo: /images/people/sagar-lankala.jpg
        - name: Mikhail Shilkov
          role: Engineering Manager, Pulumi
          photo: /images/team/mikhail-shilkov.jpg
    # case-sensitive
    tags:
        level: Beginner # Beginner, Intermediate, Advanced
        topics: []
        languages: ["C#"]
        clouds: ["Azure"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 43e17b45-7bd5-4e97-9359-ba0cd9db1c57
    salesforce_campaign_id: 701PQ00000CABsvYAH
---
