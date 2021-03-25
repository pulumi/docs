---
# Name of the webinar.
title: "Getting Started with Pulumi"
meta_desc: "In this workshop, you will learn the fundamentals of Infrastructure as Code through a series of guided exercises using Pulumi's Cloud Engineering Platform."

# A featured webinar will display first in the list.
featured: false

# If the video is pre-recorded or live.
pre_recorded: false

# If the video is part of the PulumiTV series. Setting this value to true will list the video in the "PulumiTV" section.
pulumi_tv: false

# Webinars with unlisted as true will not be shown on the webinar list
unlisted: true

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
block_external_search_index: true

# The url slug for the webinar landing page. If this is an external
# webinar, use the external URL as the value here.
url_slug: "getting-started-with-pulumi"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Getting Started with Pulumi"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Getting Started with Pulumi"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2021-03-24T09:00:00+10:00
    # Duration of the webinar.
    duration: "2 hours"
    # Datetime of the webinar.
    datetime: "WED MAR 24, 2021"
    # Description of the webinar.
    description: |
        In this workshop, you will learn the fundamentals of Infrastructure as Code through a series of guided exercises using Pulumi's Cloud Engineering Platform. You will be introduced to Pulumi, an infrastructure as code platform where you can use programming languages to provision modern cloud infrastructure.

        This workshop is designed to help users completely new to Pulumi become family with the core concepts needed to be effective with the Pulumi Infrastructure as Code platform. We will guide through the Pulumi platform with diagrams and a series of hands on exercises to help you understand the building blocks available in Pulumi.

    # The webinar presenters
    presenters:
        - name: Luke Hoban
          role: CTO, Pulumi

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - This is a 100-level introduction to setting up your infrastructure using Pulumi with multiple languages.
        - Cloud programming with your favorite language.

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 2335dfff-2d37-4799-b750-15b7ba319d0a
---
