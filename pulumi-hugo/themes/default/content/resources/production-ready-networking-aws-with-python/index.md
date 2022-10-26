---
# Name of the webinar.
title: "Production-Ready Networking on AWS with Python"
meta_desc: "In this workshop you'll learn to apply Infrastructure as Code concepts to build a hub and spoke network topology with an inspection VPC."

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
  name: "Production-Ready Networking on AWS with Python"
  start_date: 2022-12-13T05:00:00-08:00
  end_date: 2022-12-13T06:30:00-08:00
  url: "https://www.pulumi.com/resources/production-ready-networking-aws-with-python"
  description: |
      In this workshop you'll learn to apply Infrastructure as Code concepts to build a hub and spoke network topology with an inspection VPC. This pattern is incredibly useful for standing up separate environments for development, testing and production, providing workload isolation for multiple customers and standing up shared services.

      This 200-level course will be taught in the Python language but the concepts apply to any modern programming language. The content builds upon Pulumi concepts from learn.pulumi.com and our Getting Started workshop series.

# The url slug for the webinar landing page. If this is an external
# webinar, use the external URL as the value here.
url_slug: "production-ready-networking-aws-with-python"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Production-Ready Networking on AWS with Python"
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
    title: "Production-Ready Networking on AWS with Python"
    # URL for embedding a URL for ungated webinars.
    youtube_url: ""
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2022-12-13T04:00:00-08:00
    # Duration of the webinar.
    duration: "90 minutes"
    # Datetime of the webinar.
    datetime: ""
    # Description of the webinar.
    description: |
        In this workshop you'll learn to apply Infrastructure as Code concepts to build a hub and spoke network topology with an inspection VPC. This pattern is incredibly useful for standing up separate environments for development, testing and production, providing workload isolation for multiple customers and standing up shared services.

        This 200-level course will be taught in the Python language but the concepts apply to any modern programming language. The content builds upon Pulumi concepts from [learn.pulumi.com](/learn/) and our Getting Started workshop series.

    # The webinar presenters
    presenters:
        - name: Andy Taylor
          role: Networking Specialist Solutions Architect, AWS
        - name: Jose Juhala
          role: Solutions Architect, AWS
        - name: Josh Kodroff
          role: Senior Solutions Architect, Pulumi

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - AWS networking concepts using Python
        - How to implement a hub and spoke topology on AWS
        - Configuring an inspection VPC

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: "f8d6ec38-079b-4544-8ced-42bf76de1ca3"

aws_only: true
---
