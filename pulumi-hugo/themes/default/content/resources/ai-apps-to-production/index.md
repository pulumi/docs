---
# Name of the webinar.
title: "Taking AI Apps to Production"
meta_desc: "The Pinecone and Pulumi teams will explore the infrastructure and service architecture you need to scale AI apps in production."

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
url_slug: "ai-apps-to-production"

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
    title: "Taking AI Apps to Production"
    # URL for embedding a URL for ungated webinars.
    youtube_url:
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2023-12-14T09:00:00.000-08:00
    # Duration of the webinar.
    duration: "60 minutes"
    # Datetime of the webinar.
    datetime: 
    # Description of the webinar.
    description: |
        What does it take to go from an idea in a notebook to an application handling real-world traffic? In this workshop, the Pinecone and Pulumi teams will explore the infrastructure and service architecture you need to scale AI apps in production. We will delve into deploying high-volume AI systems through scalable microservices, efficient data processing, and seamless synchronization between user interfaces and databases. We will examine the nuances of containerization for enhanced portability and Infrastructure as Code (IaC) for streamlined cloud deployments. The workshop will also discuss industry best practices in scalability and security for production-grade AI systems in a cloud-native landscape.

        This workshop is designed to help AI developers and engineers gain valuable insights and practical strategies for evolving AI applications into resilient and efficient cloud-native solutions. We will guide you through the Pulumi platform with diagrams and a series of labs to help accelerate your AI apps.

    # The webinar presenters
    presenters:
        - name: Scott Lowe
          role: Principal Community Engineer, Pulumi
        - name: Zach Proser 
          role: Staff Developer Advocate, Pinecone
    
    learn:
        - The basics of infrastructure as code and the Pulumi programming model
        - How to provision, update, and destroy AWS resources (Amazon ECS clusters, networking infrastructure, messaging queues, and Amazon RDS Postgres databases)
        - How to create and manage Pinecone indexes

    # A bullet point list containing what the user will learn during the webinar.

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: dd3c952a-f4c6-4c3a-bac5-6e9675ddb72b
    salesforce_campaign_id: 701Du000000BqlcIAC

aws_only: false
---