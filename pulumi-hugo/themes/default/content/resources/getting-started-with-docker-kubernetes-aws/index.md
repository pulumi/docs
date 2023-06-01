---
# Name of the webinar.
title: "Getting Started With Docker And Kubernetes On AWS"
meta_desc: "Learn the fundamentals of building and deploying containerized workloads and get an introduction to Pulumi's IaC platform and deployment on AWS."

# A featured webinar will display first in the list.
featured: false

# If the video is pre-recorded or live.
pre_recorded: false

# If the video is part of the PulumiTV series. Setting this value to true will list the video in the "PulumiTV" section.
pulumi_tv: false

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
external: true
block_external_search_index: true

# The url slug for the webinar landing page. If this is an external
# webinar, use the external URL as the value here.
url_slug: "https://webinars.devops.com/getting-started-with-docker-and-kubernetes-on-aws?hs_preview=eaZtVqQA-115941174926&utm_campaign=2023.06.27_AWS_Pulumi_Webinar_DO%2FCN&utm_source=DO-Pulumi"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Getting Started With Docker And Kubernetes On AWS"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Getting Started With Docker And Kubernetes On AWS"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2023-06-27T11:00:00-07:00
    # Duration of the webinar.
    duration: "1 hour"
    # Datetime of the webinar.
    datetime: "June 27, 2023"
    # Description of the webinar.
    description: |
        Getting started with Docker and Kubernetes doesn't have to be complex. Pulumi's infrastructure-as-code (IaC) platform can help remove the complexity and enable even beginner developers to use any programming language to provision modern infrastructure.

        In this session, you will learn the fundamentals of building and deploying containerized workloads and get an introduction to Pulumi's IaC platform and deployment on AWS.

        We’ll start by building a container image using the new Pulumi Docker provider. Next, we’ll guide you through setting up an Amazon EKS cluster on AWS and deploying your Docker image to the cluster.

        This workshop is designed to help new users become familiar with the core concepts needed to effectively deploy Kubernetes clusters and workloads on AWS. We will guide you through the Pulumi platform with diagrams and a series of examples to help accelerate your cloud projects.

    # The webinar presenters
    presenters:
        - name: Scott Lowe
          role: Sr. Technical Content Engineer, Pulumi
        - name: Marina Novikova
          role: Partner Solutions Architect, AWS

    # A bullet point list containing what the user will learn during the webinar.


# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id:
    salesforce_campaign_id:
---