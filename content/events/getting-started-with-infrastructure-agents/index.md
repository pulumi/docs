---
# Name of the event, <= 60 characters
title: "Getting Started with Infrastructure Agents"
meta_desc: Platform Engineering teams looking to add intelligent automation to their infrastructure workflows must first plan controls and human oversight into their process.
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
url_slug: agentic-workflows-human-in-loop

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Getting Started with Infrastructure Agents"
    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: 

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2025-10-09T12:00:00-04:00

    # Duration of the webinar.
    duration: 90 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        Platform Engineering teams looking to add intelligent automation to their infrastructure workflows must first plan controls and human oversight into their process. In this session, we'll introduce considerations for setting up agentic workflows with a basic 'human in the loop' approval process and walk through a basic cloud deployment.
    learn:
        - Introduction to Pulumi MCP Server and agentic workflow concepts and considerations
        - Configuring agents within your environment
        - Understanding Pulumi's core platform engineering capabilities and architecture
        - Your first autonomous infrastructure workflow: provisioning cloud resources with a basic pull request approval workflow

    # The webinar presenters
    presenters:
        - name: Engin Diri
          role: Senior Solutions Architect
          photo: /images/team/engin-diri.jpg

    # case-sensitive
    tags:
        level: Beginner # Beginner, Intermediate, Advanced
        topics:  ["Pulumi MCP Server"]
        languages: ["Any"]
        clouds: ["AWS"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 1bea61d9-a914-40c8-9a7e-6c220420e05a
    salesforce_campaign_id: 701PQ00000eeMnZYAU

event_data:
  name: "Getting Started with Infrastructure Agents"
  start_date: 2025-10-09T12:00:00-04:00
  end_date: 2025-10-09T13:30:00-04:00
  url: "https://www.pulumi.com/resources/agentic-workflows-human-in-loop/"
  description: |
    Platform Engineering teams looking to add intelligent automation to their infrastructure workflows must first plan controls and human oversight into their process. In this session, we'll introduce considerations for setting up agentic workflows with a basic 'human in the loop' approval process and walk through a basic cloud deployment.
---
