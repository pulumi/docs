---
# Name of the event, <= 60 characters
title: From Infrastructure Engineering to Platform Engineering
meta_desc: In this expert panel, learn how teams at CLEAR, Modivcare, and Sokkel built internal developer platforms and evolved from infrastructure to platform engineering
meta_image:

# A featured webinar will display first in the list.
featured: false

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
external: false
block_external_search_index: false

# The url slug for the webinar landing page. If this is an external
# webinar, use the external URL as the value here.
url_slug: from-infrastructure-engineering-to-platform-engineering

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: From Infrastructure Engineering to Platform Engineering

    event_type: event # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: https://www.youtube.com/embed/ek22Sm3CAlM?rel=0

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2025-05-05T08:59:00-00:00

    # Duration of the webinar.
    duration: 1 hour

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        Platform Engineering is transforming how teams build and manage infrastructure at scale. In this panel, leaders from Clear, Modivcare, and Sokkel share how they evolved from traditional infrastructure practices to modern [internal developer platforms (IDPs)](/product/internal-developer-platforms/)—with real-world lessons on scaling self-service, improving developer experience, and maintaining governance.
    
    learn:
        - How organizations move from DevOps tooling to full platform teams
        - The role of Infrastructure as Code (IaC) and Pulumi in platform maturity
        - Strategies for enabling self-service and golden paths for developers
        - Real examples of managing compliance, scalability, and platform adoption
        - How AI, policy as code, and developer portals fit into modern platforms
        - What roles and structures make a platform team successful

    # The webinar presenters
    presenters:
        - name: Josh Kodroff
          role: Principal Customer Success Architect, Pulumi
          photo: /images/team/josh-kodroff.jpg
        - name: Zachary Cook
          role: Sr. Manager DevOps, Modivcare
          photo: /images/people/zachary-cook.jpg
        - name: James Forcier
          role: Staff Software Engineer, CLEAR
          photo: /images/people/james-forcier.jpg
        - name: Simen A. W. Olsen
          role: CEO, Sokkel
          photo: /images/team/simen-a-w-olsen.jpg

    # case-sensitive
    tags:
        level: # Beginner, Intermediate, Advanced
        topics: ["DevOps", "Security", "Platform Engineering", "Automation"]
        languages: []

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id:
    salesforce_campaign_id:
---