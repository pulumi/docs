---
# Name of the event, <= 60 characters
title: Deploy Tailscale infrastructure in AWS with Pulumi
meta_desc: This webinar explores how to quickly create AWS infrastructure using Pulumi and Tailscale, showcasing advanced features in Kubernetes and AWS environments.
meta_image:

# A featured webinar will display first in the list.
featured: false

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
url_slug: deploy-tailscale-infrastructure-with-pulumi

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Deploy Tailscale infrastructure in AWS with Pulumi

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: 

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2024-10-15T09:00:00-07:00

    # Duration of the webinar.
    duration: 60 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        In this session, you'll learn how to use Pulumi’s expressive infrastructure as code and automation API to quickly spin up a full demo environment showcasing Tailscale’s features. This workshop will walk through a reference architecture featuring Tailscale's Kubernetes operator, AWS VPC access via subnet routers, and secure internet access with exit nodes—all provisioned in minutes using Pulumi. This webinar is ideal for cloud engineers, DevOps practitioners, and IT professionals looking to streamline infrastructure provisioning while leveraging Tailscale and Pulumi.

    learn:
        - How to set up AWS infrastructure quickly using Pulumi’s infrastructure as code and automation API.
        - Key components of Tailscale’s reference architecture, including Kubernetes operators and AWS VPC access.
        - Best practices for provisioning secure and scalable infrastructure with Tailscale and Pulumi.

    # The webinar presenters
    presenters:
        - name: Lee Briggs
          role: Sales Engineering Manager, Tailscale
          photo: /images/team/lee-briggs.jpg
        - name: Josh Kodroff 
          role: Sr Solutions Architect, Pulumi
          photo: /images/team/josh-kodroff.jpg

    # case-sensitive
    tags:
        level: Beginner # Beginner, Intermediate, Advanced
        topics: ["AWS", "Tailscale"]
        languages: ["TypeScript"]
        clouds: ["AWS"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 89d7f610-7407-4e84-ab28-0f58dc404e8e
    salesforce_campaign_id: 701PQ00000Ji6I5YAJ
---
