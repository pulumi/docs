---
# Name of the event, <= 60 characters
title: "Migrating from Console Deployments to Infrastructure as Code"
meta_desc: Help your organization move faster by adopting automation with Infrastructure as Code
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
url_slug: migrating-console-deployments-iac

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Migrating from Console Deployments to Infrastructure as Code"

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: 

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2025-01-15T09:00:00-08:00

    # Duration of the webinar.
    duration: 90 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
       As organizations scale their cloud operations, managing infrastructure through manual console deployments becomes increasingly risky and time-consuming. This workshop bridges the gap between click-ops and modern infrastructure automation, providing both technical guidance and business context for adopting Infrastructure as Code (IaC).
       
       Participants will learn how platform engineering practices can accelerate delivery while improving reliability and security. Through hands-on demonstrations using Pulumi, attendees will discover practical strategies for transitioning existing console-created resources to code, establishing repeatable deployment patterns, and building a foundation for scalable infrastructure management. The session combines technical demonstrations with real-world business cases, making it valuable for both technical practitioners and decision-makers looking to modernize their infrastructure practices.

    learn:
        - The benefits of adopting platform engineering as a practice
        - How to start your platform engineering by adopting infrastructure as code
        - How to take resources created manually in the console and bring them under IaC automation

    # The webinar presenters
    presenters:
        - name: Josh Kodroff 
          role: Principal Solutions Architect, Pulumi
          photo: /images/team/josh-kodroff.jpg
        - name: Torian Crane
          role: Senior Technical Content Engineer, Pulumi
          photo: /images/team/torian-crane.jpg

    # case-sensitive
    tags:
        level: Intermediate # Beginner, Intermediate, Advanced
        topics: ["Platform Engineering"]
        languages: ["TypeScript"]
        clouds: ["AWS"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 2ca022a2-1604-4236-95c7-1e74a63bfe8f
    salesforce_campaign_id: 701PQ00000ObL1IYAV

event_data:
  name: "Migrating from Console Deployments to Infrastructure as Code"
  start_date: 2025-01-15T09:00:00-08:00
  end_date: 2025-01-15T10:00:00-08:00
  url: "https://www.pulumi.com/resources/migrating-console-deployments-iac/"
  description: |
    As organizations scale their cloud operations, managing infrastructure through manual console deployments becomes increasingly risky and time-consuming. This workshop bridges the gap between click-ops and modern infrastructure automation, providing both technical guidance and business context for adopting Infrastructure as Code (IaC).

    Participants will learn how platform engineering practices can accelerate delivery while improving reliability and security. Through hands-on demonstrations using Pulumi, attendees will discover practical strategies for transitioning existing console-created resources to code, establishing repeatable deployment patterns, and building a foundation for scalable infrastructure management. The session combines technical demonstrations with real-world business cases, making it valuable for both technical practitioners and decision-makers looking to modernize their infrastructure practices.
---
