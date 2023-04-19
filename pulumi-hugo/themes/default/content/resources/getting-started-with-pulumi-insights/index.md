---
# Name of the webinar.
title: "Getting Started with Pulumi Insights"
meta_desc: "In this workshop, you will learn how you can improve your team's productivity with the Search, Analytics, and Intelligence capabilities of Pulumi AI"

# A featured webinar will display first in the list.
featured: true

# If the video is pre-recorded or live.
pre_recorded: false

# If the video is part of the PulumiTV series. Setting this value to true will list the video in the "PulumiTV" section.
pulumi_tv: false

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
block_external_search_index: true

# The url slug for the webinar landing page. If this is an external
# webinar, use the external URL as the value here.
url_slug: "getting-started-with-pulumi-insights"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Getting Started with Pulumi Insights"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Getting Started with Pulumi Insights"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2023-05-11T09:00:00-07:00
    # Duration of the webinar.
    duration: "1 hour"
    # Datetime of the webinar.
    datetime: "May 11, 2023"
    # Description of the webinar.
    description: |
        Pulumi makes deploying cloud resources faster and simpler at scale. As teams deploy resources across many cloud providers and SaaS platforms they generate massive amounts of data about each update and resource in their organization and can now leverage this data to derive critical business insights. With Pulumi Insights, users have Search, Analytics, and Intelligence capabilities at their fingertips and this workshop will show you how each feature can make your team more productive by:
        - Finding resources across multi-cloud deployments
        - Exporting Insights data to your favorite analytics platform
        - Assisting the creation of new infrastructure code with the power of Pulumi AI.

    # The webinar presenters
    presenters:
        - name: Josh Kodroff
          role: Senior Solutions Architect, Pulumi
        - name: Meagan Cojocar
          role: Principal Product Manager, Pulumi

    # A bullet point list containing what the user will learn during the webinar.


# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 6985d9e0-6016-48a8-8724-44c208b55a4d
    salesforce_campaign_id: 701Du000000AFe3IAG
---