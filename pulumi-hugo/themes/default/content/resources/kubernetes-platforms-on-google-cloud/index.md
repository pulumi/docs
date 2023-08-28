---
# Name of the webinar.
title: Advanced Kubernetes Platforms on Google Cloud with Pulumi
title_tag: Kubernetes Platforms on Google Cloud with Pulumi (Aug 2023 Workshop)
meta_desc: In this workshop, we’ll explore how to deliver and scale a Kubernetes platform on Google Cloud.
meta_image: "/images/resources/advanced-kubernetes-on-google-cloud-engin.png"

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
  name: Pulumi - Advanced Kubernetes Platforms on Google Cloud with Pulumi
  start_date: 2023-09-11T10:00:00.000-04:00
  end_date: 2023-09-11T11:30:00.000-04:00
  url: "https://www.pulumi.com/resources/kubernetes-platforms-on-google-cloud"
  description: |
    Platform engineering teams often need to help development teams stand up core platforms, build release automation, deploy applications, and scale resources to match customer demand. A best practice in these scenarios is to break up these services into multiple stacks to enable updates to infrastructure and processes that won’t disrupt production.

    In this session, experts from Pulumi and Google Cloud will show you how to stand up networking and cluster components GKE Autopilot, configure CI/CD pipelines and run an application that leverages multiple Google Cloud resources. We’ll also show you how to scale your infrastructure across multiple regions.

# The url slug for the webinar landing page. If this is an external
# webinar, use the external URL as the value here.
url_slug: "kubernetes-platforms-on-google-cloud"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Advanced Kubernetes Platforms on Google Cloud with Pulumi"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Webinar pages support multiple session via the 'multiple' property.
# multiple:

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Advanced Kubernetes Platforms on Google Cloud with Pulumi
    # URL for embedding a URL for ungated webinars.
    youtube_url: 
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2023-09-11T10:00:00.000-04:00
    # Duration of the webinar.
    duration: 90 minutes
    # Datetime of the webinar.
    datetime: 9/11/2023 10:00am - 11:30am EDT
    # Description of the webinar.
    description: |
        Platform engineering teams often need to help development teams stand up core platforms, build release automation, deploy applications, and scale resources to match customer demand. A best practice in these scenarios is to break up these services into multiple stacks to enable updates to infrastructure and processes that won’t disrupt production.

        In this session, experts from Pulumi and Google Cloud will show you how to stand up networking and cluster components GKE Autopilot, configure CI/CD pipelines and run an application that leverages multiple Google Cloud resources. We’ll also show you how to scale your infrastructure across multiple regions.

    # The webinar presenters
    presenters:
        - name: Tim Hiatt
          role: Technical Solutions Consultant, Google Cloud
        - name: Engin Diri
          role: Customer Experience Architect, Pulumi

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - Google Cloud project and service creation
        - Managing Networks on Google Cloud
        - Setting up your development environment
        - Configuring GKE Autopilot for multiple regions
        - Setting up Cloud Build pipelines and more.

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 5f859a0d-bf36-4969-82f5-a4dd818b62ef
    salesforce_campaign_id: 701Du000000AupeIAC

aws_only: false
---
