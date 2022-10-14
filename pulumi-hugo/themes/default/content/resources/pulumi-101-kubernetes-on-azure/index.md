---
# Name of the webinar.
title: "Pulumi 101: Kubernetes on Azure"
meta_desc: "Learn the basics of Pulumi using C# and templates to stand up a small Kubernetes cluster on AKS from Azure."

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

# The url slug for the webinar landing page. If this is an external
# webinar, use the external URL as the value here.
url_slug: "pulumi-101-kubernetes-on-azure"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Pulumi 101: Kubernetes on Azure"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Webinar pages support multiple session via the 'multiple' property.
# multiple:

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Pulumi 101: Kubernetes on Azure"
    # URL for embedding a URL for ungated webinars.
    youtube_url: 
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2022-11-03T08:00:00.000-07:00
    # Duration of the webinar.
    duration: "60 minutes"
    # Datetime of the webinar.
    datetime: 
    # Description of the webinar.
    description: |
        Learn the basics of Pulumi from projects to components. We’ll use C# and templates to stand up our first bit of infrastructure: A small Kubernetes cluster on AKS from Azure. Along the way, we’ll learn how infrastructure as code makes updates easier, reduces time to value, and helps you keep your cloud costs down.

        If you want to code along, you’ll need a [free Pulumi SaaS account](https://app.pulumi.com/signup/), [the Pulumi CLI](https://www.pulumi.com/docs/get-started/install), [.NET 6+](https://www.pulumi.com/docs/intro/languages/dotnet/), and an Azure account (free tier is okay).

    # The webinar presenters
    presenters:
        - name: "Laura Santamaria"
          role: "Developer Advocate, Pulumi"

    # A bullet point list containing what the user will learn during the webinar.

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: "306fa112-7213-4ece-9981-5eb440902eae"

aws_only: false
---