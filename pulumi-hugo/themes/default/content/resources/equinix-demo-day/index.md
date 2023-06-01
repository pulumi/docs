---
# Name of the webinar.
title: "Equinix Demo Day"
meta_desc: "In this code-centric demo you will learn the basics of Pulumi and how to deploy a workload onto Equinix Metal."

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
url_slug: "https://sched.co/1NLj0"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Equinix Demo Day"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Equinix Demo Day"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2023-06-21T08:30:00-07:00
    # Duration of the webinar.
    duration: "1 hour"
    # Datetime of the webinar.
    datetime: "June 21, 2023"
    # Description of the webinar.
    description: |
        In this code-centric session, you will learn how to manage Equinix Metal resources using Pulumi, the Open Source infrastructure as code tool that allows you to manage resources in any cloud with real programming languages. We'll teach you the basics of how Pulumi works, and we'll demonstrate deploying a workload onto Equinix Metal.
    # The webinar presenters
    presenters:
        - name: "Josh Kodroff"
          role: "Sr. Solutions Architect, Pulumi"

    # A bullet point list containing what the user will learn during the webinar.


# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id:
    salesforce_campaign_id:
---