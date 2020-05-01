---
# Name of the webinar.
title: "Verify Infrastructure Deployments with Pulumi and CircleCI"
meta_desc: "Angel Rivera and Chris Smith walk you through best practices for app developers, DevOps, and SREs to keep configuration mistakes from reaching production."

# A featured webinar will display first in the list.
featured: false

# If the video is pre-recorded or live.
pre_recorded: false

# If the video is part of the PulumiTV series. Setting this value to true will list the video in the "PulumiTV" section.
pulumi_tv: false

# The preview image will be shown on the list page.
preview_image: "/images/webinar/circleci-pulumi.png"

# Webinars with unlisted as true will not be shown on the webinar list
unlisted: false

# Gated webinars will have a registration form and the user will need
# to fill out the form before viewing.
gated: true

# The layout of the landing page.
type: webinars

# External webinars will link to an external page instead of a webinar
# landing/registration page.
external: false

# The url slug for the webinar landing page. If this is an external
# webinar, use the external URL as the value here.
url_slug: "verify-your-infrastructure-on-deployment"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Verify Your Infrastructure on Each Deployment with Pulumi and CircleCI"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Verify Your Infrastructure on Each Deployment with Pulumi and CircleCI"
    # URL for embedding a URL for ungated webinars.
    youtube_url: ""
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2020-06-03T11:00:00-07:00
    # Duration of the webinar.
    duration: 1 hour
    # Datetime of the webinar.
    datetime: "WED, JUNE 3, 2020, 11:00 AM PDT"
    # Description of the webinar.
    description: |
        With Pulumi you can add infrastructure tests and policies to your CircleCI pipelines
        using your favorite programming languages.

        Angel Rivera and Chris Smith walk you through best practices for application developers,
        DevOps, and SREs to keep configuration mistakes from reaching production.

    # The webinar presenters
    presenters:
        - name: Angel Rivera
          role: Developer Advocate, CircleCI
        - name: Chris Smith
          role: Lead Software Engineer, Pulumi

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - How to write unit tests and use resource mocking with Pulumi.
        - Defining storage and ingress policies for security, and resource tagging policies for compliance.
        - Infrastructure integration testing with ephemeral environments
        - Configuring CircleCI to verify infrastructure as part of each deployment

# The right hand side form section.
form:
    # GoToWebinar webinar key. This key allows us to register people for webinars via the
    # HubSpot form.
    gotowebinar_key: "7364613951657082636"

    # HubSpot form id.
    hubspot_form_id: "d0544c16-826e-4e46-85b8-f7bee8f1ebdf"
---
