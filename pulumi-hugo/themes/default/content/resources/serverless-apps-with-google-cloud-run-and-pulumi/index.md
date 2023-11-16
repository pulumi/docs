---
# Name of the webinar.
title: "Serverless Apps with Google Cloud Run and Pulumi"
meta_desc: "Learn how to deploy applications effortlessly on Cloud Run with Pulumi, use containerization with Docker, and manage Google Cloud resources with code."

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
url_slug: "serverless-apps-with-google-cloud-run-and-pulumi"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Serverless Apps with Google Cloud Run and Pulumi"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Webinar pages support multiple session via the 'multiple' property.
# multiple:

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Serverless Apps with Google Cloud Run and Pulumi"
    # URL for embedding a URL for ungated webinars.
    youtube_url:
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2023-11-30T09:00:00.000-08:00
    # Duration of the webinar.
    duration: "60 minutes"
    # Datetime of the webinar.
    datetime: 
    # Description of the webinar.
    description: |
        Developers who need to deploy their applications often find it tough to ship quickly with many options available for running containerized apps. Cloud Run helps abstract away the complexities of container services and orchestration so you can package and deploy apps while making it easy to scale to meet customer demand.

    # The webinar presenters
    presenters:
        - name: Monica Rodriguez
          role: Sr. Product Manager, Pulumi
        - name: Jason Smith
          role: Sr. Cloud Customer Engineer, Google
    
    learn:
        - How to package your app as a Docker container
        - Defining resources in Google Cloud using Python with Pulumi
        - Running and scaling your application on Cloud Run

    # A bullet point list containing what the user will learn during the webinar.

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: c39c7789-2dbd-4516-acd2-860ceeb7f12d
    salesforce_campaign_id: 701Du000000Bkp6IAC

aws_only: false
---