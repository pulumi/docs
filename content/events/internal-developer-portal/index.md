---
# Name of the event, <= 60 characters
title: "Building an Internal Developer Platform"
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
url_slug: internal-developer-portal

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Building an Internal Developer Platform"

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: 

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2025-03-26T09:00:00-07:00

    # Duration of the webinar.
    duration: 90 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
       In today's cloud-native landscape, organizations struggle to balance developer autonomy with operational control. This workshop explores how to build an Internal Developer Platform (IDP) that transforms infrastructure provisioning from a bottleneck into a competitive advantage. You'll learn how to create a self-service platform that enables developers to safely deploy infrastructure while maintaining governance and cost control.
       
       Through practical demonstrations and architectural discussions, we'll explore how to implement golden paths, automate approvals, and manage templates that accelerate development while enforcing organizational standards. You'll see how to leverage modern infrastructure-as-code practices to create a developer experience that reduces time-to-market from days to hours, without sacrificing security or compliance.

    learn:
        - Design and implement an Internal Developer Platform that balances developer self-service with organizational control, including template management, access controls, and automated workflows
        - Create and manage reusable infrastructure patterns that enforce best practices while enabling developers to safely provision resources on demand
        - Establish effective governance mechanisms including automated approvals, audit trails, and cost management strategies that scale with your organization's growth

    # The webinar presenters
    presenters:
        - name: Josh Kodroff 
          role: Principal Solutions Architect, Pulumi
          photo: /images/team/josh-kodroff.jpg

    # case-sensitive
    tags:
        level: Intermediate # Beginner, Intermediate, Advanced
        topics: ["Platform Engineering"]
        languages: ["TypeScript"]
        clouds: ["AWS"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: ea7ab56d-8cff-4a2e-9988-760278326548
    salesforce_campaign_id: 701PQ00000ObZInYAN

event_data:
  name: "Building an Internal Developer Portal"
  start_date: 2025-03-26T09:00:00-07:00
  end_date: 2025-03-26T09:00:00-07:00
  url: "https://www.pulumi.com/resources/internal-developer-portal/"
  description: |
    In today's cloud-native landscape, organizations struggle to balance developer autonomy with operational control. This workshop explores how to build an Internal Developer Portal (IDP) that transforms infrastructure provisioning from a bottleneck into a competitive advantage. You'll learn how to create a self-service platform that enables developers to safely deploy infrastructure while maintaining governance and cost control.
    
    Through practical demonstrations and architectural discussions, we'll explore how to implement golden paths, automate approvals, and manage templates that accelerate development while enforcing organizational standards. You'll see how to leverage modern infrastructure-as-code practices to create a developer experience that reduces time-to-market from days to hours, without sacrificing security or compliance.
---
