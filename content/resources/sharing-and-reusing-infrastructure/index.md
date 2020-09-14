---
# Name of the webinar.
title: "Sharing & Reusing Infrastructure with Artifactory"
meta_desc: "Dan Hernandez and Melissa McKay will show you how to define resources such as VPCs, Kubernetes clusters, and policies using multiple languages."

aliases:
  - /webinars/sharing-and-reusing-infrastructure

# A featured webinar will display first in the list.
featured: false

# If the video is pre-recorded or live.
pre_recorded: true

# If the video is part of the PulumiTV series. Setting this value to true will list the video in the "PulumiTV" section.
pulumi_tv: false

# The preview image will be shown on the list page.
preview_image: "/images/webinar/jfrog-pulumi.png"

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
url_slug: "sharing-and-reusing-infrastructure"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Sharing and Reusing Infrastructure with Pulumi and Artifactory"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Sharing and Reusing Infrastructure with Pulumi and Artifactory"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2020-05-27T11:00:00-07:00
    # Duration of the webinar.
    duration: "1 hour"
    # Datetime of the webinar.
    datetime: "WED MAY 27, 2020 AT 11:00AM PDT"
    # Description of the webinar.
    description: |
        Empower your teams to move faster with shared infrastructure components that follow and enforce best practices. Dan Hernandez (Pulumi) and Melissa McKay (JFrog) will show you how to define key resources such as VPCs, storage, Kubernetes clusters, Docker images, serverless functions, and policies using multiple languages. Then, see how easy it is to share these modules across your organization with Artifactory.

    # The webinar presenters
    presenters:
        - name: Dan Hernandez
          role: Customer Engineer, Pulumi
        - name: Melissa McKay
          role: Developer Advocate, JFrog

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - Infrastructure as code concepts with Pulumi.
        - Artifact sharing best practices using Artifactory.
        - Utilizing Pulumi packages to standardize infrastructure.
        - Using Artifactory to author and manage Pulumi packages.
        - Consuming Pulumi packages stored in Artifactory.

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: "3dbc6286-201d-43cc-9602-d1150465e9e2"
---
