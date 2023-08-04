---
# Name of the webinar.
title: Getting Started with 1Password and Pulumi
meta_desc: Join us for a hands-on lab showing you how to integrate 1Password into your Pulumi workflow.
meta_image: "/images/resources/1password-pulumi.png"

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
url_slug: "getting-started-with-1password-and-pulumi"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Getting Started with 1Password and Pulumi"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Getting Started with 1Password and Pulumi"
    # URL for embedding a URL for ungated webinars.
    youtube_url:
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2023-09-12T08:00:00-07:00
    # Duration of the webinar.
    duration: "1 hour"
    # Datetime of the webinar.
    datetime: ""
    # Description of the webinar.
    description: |
      If you’re using 1Password to manage keys, account passwords and other sensitive information you can now access those secrets from the Pulumi CLI using the new Pulumi 1Password plugin.

      Join Pulumi and 1Password for a short walkthrough of this powerful new feature and get your questions answered by the experts.


    # The webinar presenters
    presenters:
        - name: Ringo De Smet
          role: Customer Experience Architect, Pulumi
        - name: Clarence Wong
          role: Senior Product Partnerships Manager, 1Password
        - name: Jason Harris
          role: Principal Platform Evangelist, 1Password
        - name: Simon Barendse
          role: Senior Software Engineer, 1Password

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - How to set up the Pulumi 1Password Plugin
        - Accessing your 1Password secrets from the Pulumi CLI
        - Best practices for securing sensitive values during your deployments

# The right hand side form section.
form:
    salesforce_campaign_id: 701Du000000AnO6IAK
    hubspot_form_id: 18a7dd50-d3d8-480f-bf3a-af97706593c7
---
