---
# Name of the event, <= 60 characters
title: "Self-Service AI Application Platforms"
meta_desc: Build self-service platforms for delivering AI-powered applications and agents.
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
url_slug: self-service-ai-application-platforms

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Self-Service AI Application Platforms"
    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: 

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2025-09-09T12:00:00-04:00

    # Duration of the webinar.
    duration: 60 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        The rise of LLM applications creates new infrastructure challenges related to GPU resources, model serving, and cost management. This cutting-edge workshop demonstrates how to extend your IDP to support AI application teams with self-service infrastructure for AI-powered applications and agents. You'll learn to create templates for model serving, implement cost controls for GPU resources, and provide integration patterns for common use cases.
    learn:
        - How to create self-service templates for LLM application infrastructure and GPU resources
        - Security patterns for handling sensitive data in AI-powered applications and API key management.

    # The webinar presenters
    presenters:
        - name: Engin Diri
          role: Senior Solutions Architect, Pulumi
          photo: /images/team/engin-diri.jpg

    # case-sensitive
    tags:
        level: Advanced # Beginner, Intermediate, Advanced
        topics:  ["AI", "LLM", "GPU Infrastructure"]
        clouds: ["AWS"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 80baf260-52f7-481b-a085-5b8575eac389
    salesforce_campaign_id: 701PQ00000ZY23IYAT

event_data:
  name: "Self-Service AI Application Platforms"
  start_date: 2025-09-09T12:00:00-04:00
  end_date: 2025-09-09T13:00:00-04:00
  url: "https://www.pulumi.com/resources/self-service-ai-application-platforms/"
  description: |
        The rise of LLM applications creates new infrastructure challenges related to GPU resources, model serving, and cost management. This cutting-edge workshop demonstrates how to extend your IDP to support AI application teams with self-service infrastructure for AI-powered applications and agents. You'll learn to create templates for model serving, implement cost controls for GPU resources, and provide integration patterns for common use cases.
--- 