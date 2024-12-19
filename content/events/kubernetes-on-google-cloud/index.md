---
# Name of the event, <= 60 characters
title: Getting Started with Kubernetes on Google Cloud
meta_desc: In this workshop, you will learn how to deploy a Kubernetes cluster on Google Cloud and run containerized applications on the cluster.
meta_image: /images/resources/intro-k8s-google-cloud-jay.png

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
url_slug: kubernetes-on-google-cloud

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Getting Started with Kubernetes on Google Cloud

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: https://www.youtube.com/embed/eQMDlXB_Zvc?rel=0

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2023-10-05T12:00:00-04:00

    # Duration of the webinar.
    duration: 90 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        In this workshop, you will learn how to deploy a Kubernetes cluster on Google Cloud and run containerized applications on the cluster. The workshop will include a brief introduction to Pulumi, an infrastructure-as-code platform, where you can use familiar programming languages to provision modern cloud infrastructure.
        
        This 200-level workshop is designed to help users who have basic familiarity with Pulumi effectively handle real-world use cases. We will guide you through the process with diagrams and a series of labs to help accelerate your cloud projects.

    learn:
        - How to use real programming languages to manage cloud resources in a declarative fashion.
        - How to manage Google Cloud and Kubernetes resources with Pulumi.
        - How Pulumi's provider ecosystem allows you to orchestrate all the resources your cloud-native workloads need with a single tool.

    # The webinar presenters
    presenters:
        - name: Josh Kodroff
          role: Sr Solutions Architect, Pulumi
          photo: /images/team/josh-kodroff.jpg
        - name: Jason Smith
          role: Customer Engineer, Google Cloud

    # case-sensitive
    tags:
        level: Intermediate # Beginner, Intermediate, Advanced
        topics: ["Kubernetes"]
        languages: []
        clouds: ["Google Cloud"]

# The right hand side form section.
form:
  hubspot_form_id: 73602700-1d98-4bfe-921e-826cca5805a1
  salesforce_campaign_id: 701Du000000AupjIAC
---
