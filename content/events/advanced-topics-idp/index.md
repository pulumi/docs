---
# Name of the event, <= 60 characters
title: "Advanced Topics for Building an IDP"
meta_desc: Learn how to build modern IDPs using Pulumi while leveraging existing IaC investments and knowledge.
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
url_slug: advanced-topics-idp

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Advanced Topics for Building an IDP"
    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: 

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2025-09-17T12:00:00-04:00

    # Duration of the webinar.
    duration: 60 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        Many organizations have significant investments in legacy IaC platforms like Terraform but want to modernize their approach to include Internal Developer Platforms. This workshop shows how to build next-generation IDPs with Pulumi while leveraging existing Terraform infrastructure and team knowledge. You'll learn interoperability patterns, and how Pulumi creates a clear path from static infrastructure as code to dynamic, self-service platforms.
    learn:
        - How to coexist with Terraform while delivering modern IDP infrastructure
        - How to modernize your IDP components incrementally - without throwing out known-good IaC.

    # The webinar presenters
    presenters:
        - name: Engin Diri
          role: Senior Solutions Architect, Pulumi
          photo: /images/team/engin-diri.jpg

    # case-sensitive
    tags:
        level: Intermediate # Beginner, Intermediate, Advanced
        topics:  ["Terraform", "Migration", "Platform Engineering"]
        clouds: ["AWS", "Azure", "Google Cloud"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 80baf260-52f7-481b-a085-5b8575eac389
    salesforce_campaign_id: 701PQ00000ZY23IYAT

event_data:
  name: "Advanced Topics for Building an IDP"
  start_date: 2025-09-17T12:00:00-04:00
  end_date: 2025-09-17T13:00:00-04:00
  url: "https://www.pulumi.com/resources/advanced-topics-idp/"
  description: |
        Many organizations have significant investments in legacy IaC platforms like Terraform but want to modernize their approach to include Internal Developer Platforms. This workshop shows how to build next-generation IDPs with Pulumi while leveraging existing Terraform infrastructure and team knowledge. You'll learn interoperability patterns, and how Pulumi creates a clear path from static infrastructure as code to dynamic, self-service platforms.
--- 