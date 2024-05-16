---
# Name of the event, <= 60 characters
title: Production-Ready Networking on AWS with Python
meta_desc: "Hands-on Workshop: Learn to apply Infrastructure as Code concepts to build a hub and spoke network topology with an inspection VPC."
meta_image: /images/production-ready-networking-aws-python.png
# A featured webinar will display first in the list.
featured: false

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

# The url slug for the webinar landing page. If this is an external
# webinar, use the external URL as the value here.
url_slug: production-ready-networking-aws-with-python

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Production-Ready Networking on AWS with Python

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: https://www.youtube.com/embed/gtmpPA971Us?rel=0

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2022-12-13T04:00:00-08:00

    # Duration of the webinar.
    duration: 90 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        In this workshop you'll learn to apply Infrastructure as Code concepts to build a hub and spoke network topology with an inspection VPC. This pattern is incredibly useful for standing up separate environments for development, testing and production, providing workload isolation for multiple customers and standing up shared services.

        This 200-level course will be taught in the Python language but the concepts apply to any modern programming language. The content builds upon Pulumi concepts from [learn.pulumi.com](/learn/) and our Getting Started workshop series.

    learn:
        - AWS networking concepts using Python
        - How to implement a hub and spoke topology on AWS
        - Configuring an inspection VPC

    # The webinar presenters
    presenters:
        - name: Josh Kodroff
          role: Senior Solutions Architect, Pulumi
          photo: /images/team/josh-kodroff.jpg
        - name: Andy Taylor
          role: Networking Specialist Solutions Architect, AWS
        - name: Jose Juhala
          role: Solutions Architect, AWS

    # case-sensitive
    tags:
        level: Intermediate # Beginner, Intermediate, Advanced
        topics: []
        languages: ["Python"]
        clouds: ["AWS"]

# The right hand side form section.
form:
  hubspot_form_id: f8d6ec38-079b-4544-8ced-42bf76de1ca3
  salesforce_campaign_id:
---
