---
# Name of the webinar.
title: "Get Started with Infrastructure as Code on Azure with Java"
meta_desc: "Learn the basics of Azure and Pulumi with a hands-on lab that will take you from deploying a simple static website to deploying a Spring Boot application."
meta_image: /images/get-started-azure-with-java.png

# A featured webinar will display first in the list.
featured: false

# If the video is pre-recorded or live.
pre_recorded: true

# If the video is part of the PulumiTV series. Setting this value to true will list the video in the "PulumiTV" section.
pulumi_tv: false

# The preview image will be shown on the list page.
preview_image: ""

# Webinars with unlisted as true will not be shown on the webinar list
unlisted: false

# Gated webinars will have a registration form and the user will need
# to fill out the form before viewing.
gated: false

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
  name: "Get Started with Infrastructure as Code on Azure with Java"
  start_date: 2022-11-22T09:00:00-08:00
  end_date: 2022-11-22T10:30:00-08:00
  url: "https://www.pulumi.com/resources/getting-started-infrascructure-as-code-azure-java"
  description: |
      It’s now easier than ever for Java developers to deploy their apps to Microsoft Azure using Pulumi and Java. In this session, we’ll teach you the basics of Azure and Pulumi with hands-on labs that will take you from deploying a simple static website to deploying a Spring Boot application to the Azure App Service.


# The url slug for the webinar landing page. If this is an external
# webinar, use the external URL as the value here.
url_slug: "getting-started-infrascructure-as-code-azure-java"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Get Started with Infrastructure as Code on Azure with Java"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Webinar pages support multiple session via the 'multiple' property.
# multiple:
#   - datetime: 2020-02-05T10:00:00-07:00
#     hubspot_form_id: ""
#     gotowebinar_key: ""

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Getting Started with Infrastructure as Code on Azure with Java"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/tsdZpv63lhQ?rel=0"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2022-11-22T09:00:00-08:00
    # Duration of the webinar.
    duration: "90 minutes"
    # Datetime of the webinar.
    datetime: ""
    # Description of the webinar.
    description: |
        It’s now easier than ever for Java developers to deploy their apps to Microsoft Azure using Pulumi and Java. In this session, we’ll teach you the basics of Azure and Pulumi with hands-on labs that will take you from deploying a simple static website to deploying a Spring Boot application to the Azure App Service.

    # The webinar presenters
    presenters:
        - name: Josh Kodroff
          role: Senior Solutions Architect, Pulumi
        - name: Brian Benz
          role: Senior Cloud Advocate, Microsoft
          
    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - Infrastructure as Code concepts for Java developers
        - Managing Azure resources with Pulumi
        - Deploying Spring Boot apps to the Azure App Service
# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: "1331a411-ef77-43bd-8eae-4a1f9d5698fe"
---
