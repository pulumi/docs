---
# Name of the event, <= 60 characters
title: "Automate Cloud Compliance with Policy as Code"
meta_desc: Learn how to automate cloud compliance and security guardrails using policy as code to ensure consistent infrastructure governance at scale.

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
url_slug: cloud-compliance-policy-as-code

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Automate Cloud Compliance with Policy as Code"

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: 

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2025-02-19T09:00:00-08:00

    # Duration of the webinar.
    duration: 90 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
       As organizations scale their cloud infrastructure, maintaining security and compliance becomes increasingly complex. This workshop explores how Policy as Code (PaC) transforms traditional manual compliance processes into automated, version-controlled, and programmatically enforced guardrails
       
       Participants will learn how to implement effective cloud governance strategies using modern PaC approaches, including writing custom policies, integrating them into CI/CD pipelines, and establishing automated enforcement mechanisms. Through practical demonstrations using Pulumi Policies, you'll discover how to bridge the gap between security requirements and infrastructure deployment while maintaining development velocity.
       
       Whether you're dealing with cost management, security compliance, or architectural standards, you'll leave with actionable insights to implement PaC in your organization.

    learn:
        - How to transform compliance requirements into programmatic rules that can be version-controlled and automatically enforced
        - How to integrate policy enforcement into developer workflows and CI/CD pipelines to catch violations early in the development lifecycle and ensure your cloud environments stay in compliance
        - How to manage evolving security and compliance requirements against infrastructure at scale

    # The webinar presenters
    presenters:
        - name: James Connell
          role: Sr Solutions Architect, Pulumi
          photo: /images/team/James-Connell.jpg

    # case-sensitive
    tags:
        level: Intermediate # Beginner, Intermediate, Advanced
        topics: ["Platform Engineering"]
        languages: ["TypeScript"]
        clouds: ["AWS"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 37582977-ca15-467e-9238-900a45939faf
    salesforce_campaign_id: 701PQ00000ObegbYAB

event_data:
  name: "Automate Cloud Compliance with Policy as Code"
  start_date: 2025-02-19T09:00:00-08:00
  end_date: 2025-02-19T10:00:00-08:00
  url: "https://www.pulumi.com/resources/cloud-compliance-policy-as-code/"
  description: |
    As organizations scale their cloud infrastructure, maintaining security and compliance becomes increasingly complex. This workshop explores how Policy as Code (PaC) transforms traditional manual compliance processes into automated, version-controlled, and programmatically enforced guardrails.
    
    Participants will learn how to implement effective cloud governance strategies using modern PaC approaches, including writing custom policies, integrating them into CI/CD pipelines, and establishing automated enforcement mechanisms. Through practical demonstrations using Pulumi Policies, you'll discover how to bridge the gap between security requirements and infrastructure deployment while maintaining development velocity.
    
    Whether you're dealing with cost management, security compliance, or architectural standards, you'll leave with actionable insights to implement PaC in your organization.
---
