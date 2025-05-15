---
# Name of the event, <= 60 characters
title: "Modernize Google Cloud Ops: From Infrastructure to Insights"
meta_desc: Learn how to streamline Google Cloud operations using infrastructure as code, unified secrets management, and cloud asset intelligence.
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
url_slug: modernize-google-cloud-ops

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Modernize Google Cloud Ops: From Infrastructure to Insights"

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url:

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2025-04-30T09:00:00.000-07:00

    # Duration of the webinar.
    duration: 60 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        In today's cloud-native landscape, organizations struggle with managing infrastructure, securing secrets, and maintaining visibility across their Google Cloud environments. This hands-on workshop demonstrates how modern platform teams can leverage Pulumi's comprehensive suite to address these challenges using familiar programming languages and tools.
        
        Through practical examples and live demonstrations, you'll discover how to automate Google Cloud infrastructure deployment, centralize secrets management, and gain real-time insights into your cloud assets. We'll explore how these capabilities work together to create a more efficient, secure, and observable cloud operations practice.



    learn:
        - How to deploy and manage Google Cloud infrastructure using your favorite programming languages with Pulumi IaC.
        - Best practices for centralizing secrets management across Google Cloud Secret Manager and other providers using Pulumi ESC.
        - Techniques for maintaining continuous visibility into your Google Cloud environment with Pulumi Insights.

    # The webinar presenters
    presenters:
        - name: Josh Kodroff
          role: Principal Customer Success Architect, Pulumi
          photo: /images/team/josh-kodroff.jpg

    # case-sensitive
    tags:
        level: Beginner # Beginner, Intermediate, Advanced
        topics: ["Security", "Platform Engineering"]
        languages: ["Python"]
        clouds: ["Google Cloud"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 1fe4f27e-a6c6-4516-ac28-cc9a62609a51
    salesforce_campaign_id: 701PQ00000TDXzxYAH

event_data:
  name: "Introduction to Pulumi IaC with AWS in Python"
  start_date: 2025-04-30T09:00:00-07:00
  end_date: 2025-04-30T10:00:00-07:00
  url: "https://www.pulumi.com/events/modernizing-cloud-operations-google-cloud/"
  description: |
    In today's cloud-native landscape, organizations struggle with managing infrastructure, securing secrets, and maintaining visibility across their Google Cloud environments. This hands-on workshop demonstrates how modern platform teams can leverage Pulumi's comprehensive suite to address these challenges using familiar programming languages and tools.
    
    Through practical examples and live demonstrations, you'll discover how to automate Google Cloud infrastructure deployment, centralize secrets management, and gain real-time insights into your cloud assets. We'll explore how these capabilities work together to create a more efficient, secure, and observable cloud operations practice.

---