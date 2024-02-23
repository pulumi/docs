---
# Name of the event, <= 60 characters
title: Getting Started with Secrets Management on AWS
meta_desc: Learn how to manage configuration and secrets across all of your AWS environments with Pulumi ESC and AWS Secrets Manager.
meta_image: /images/resources/secrets_management_aws-josh-marina-powered.png

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
url_slug: getting-started-with-secrets-management-aws

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Getting Started with Secrets Management on AWS

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: https://www.youtube.com/embed/mrVFr_uVz9s?rel=0

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2023-12-13T09:00:00.000-08:00

    # Duration of the webinar.
    duration: 1 hour

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        [Pulumi ESC](/product/esc) is a new product from Pulumi that manages and tames secrets and configuration complexity across all of your cloud infrastructure and application environments. Pulumi ESC is a new category of configuration-as-code product that enables teams to aggregate secrets and configurations from many sources, manage hierarchical collections of configurations and secrets (“environments”), and consume those configurations and secrets from a variety of different infrastructure and application services.

    learn:
        - Defining environments, which contain collections of secrets and configuration
        - Retrieving secrets from AWS Secrets Manager and other third-party sources
        - Building Pulumi ESC into your cloud provisioning workflows

    # The webinar presenters
    presenters:
        - name: Josh Kodroff
          role: Sr. Solutions Architect, Pulumi
          photo: /images/team/josh-kodroff.jpg
        - name: Ringo De Smet
          role: Customer Success Architect, Pulumi
          photo: /images/team/ringo-de-smet.jpg
        - name: Cleve Littlefield
          role: Engineering Manager, Pulumi
          photo: /images/team/cleve-littlefield.jpg

    # case-sensitive
    tags:
        level: Beginner # Beginner, Intermediate, Advanced
        topics: ["Pulumi ESC"]
        languages: []

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 660c02e4-0742-4107-ac50-cbc68c921e3e
    salesforce_campaign_id: 701Du000000BUzsIAG
---
