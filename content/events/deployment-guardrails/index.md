---
# Name of the event, <= 60 characters
title: "Deployment Guardrails with Policy as Code"
meta_desc: Implement automated governance through policy as code that enables self-service while maintaining security and compliance.
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
url_slug: deployment-guardrails

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Deployment Guardrails with Policy as Code"
    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: 

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2025-08-13T12:00:00-04:00

    # Duration of the webinar.
    duration: 60 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        Effective Internal Developer Platforms provide guardrails, not gates—enabling developer autonomy while automatically enforcing security, compliance, and operational standards. This workshop demonstrates how to implement comprehensive policy as code using Pulumi Policies. You'll learn to create policies that prevent misconfigurations, enforce tagging standards, and ensure compliance requirements are met automatically, turning your IDP into a secure-by-default platform.
    learn:
        - How to implement security and compliance policies that run automatically in CI/CD
        - Strategies for creating policies that guide rather than block developer productivity
        - Real-world policy examples for common governance requirements (tagging, security groups, encryption)

    # The webinar presenters
    presenters:
        - name: Adam Bell
          role: Community Engineer, Pulumi
          photo: /images/team/adam-gordon-bell.jpg
        - name: Josh Kodroff
          role: Principal Solutions Architect, Pulumi
          photo: /images/team/josh-kodroff.jpg

    # case-sensitive
    tags:
        level: Intermediate # Beginner, Intermediate, Advanced
        topics:  ["Security", "Policy as Code", "Governance"]
        languages: ["TypeScript"]
        clouds: ["AWS"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 541113c9-3795-4537-ab07-5485e85362a3
    salesforce_campaign_id: 701PQ00000ZYMhuYAH

event_data:
  name: "Deployment Guardrails with Policy as Code"
  start_date: 2025-08-13T12:00:00-04:00
  end_date: 2025-08-13T13:00:00-04:00
  url: "https://www.pulumi.com/resources/deployment-guardrails/"
  description: |
    Effective Internal Developer Platforms provide guardrails, not gates—enabling developer autonomy while automatically enforcing security, compliance, and operational standards. This workshop demonstrates how to implement comprehensive policy as code using Pulumi Policies. You'll learn to create policies that prevent misconfigurations, enforce tagging standards, and ensure compliance requirements are met automatically, turning your IDP into a secure-by-default platform.
--- 