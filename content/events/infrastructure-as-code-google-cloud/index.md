---
# Name of the event, <= 60 characters
title: Getting Started with Infrastructure as Code on Google Cloud
meta_desc: Workshop on infrastructure as code for Google Cloud, showing how to define, deploy, and manage GCP resources using general-purpose programming languages.
meta_image: /images/resources/getting-started-iac-google-josh-jay.png

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
url_slug: infrastructure-as-code-google-cloud

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Getting Started with Infrastructure as Code on Google Cloud

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url:

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2026-02-18T09:00:00-08:00

    # Duration of the webinar.
    duration: 60 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        This workshop explores how modern infrastructure management on Google Cloud can be streamlined using infrastructure as code. You’ll see how Pulumi enables teams to define, deploy, and manage GCP infrastructure using real programming languages and established software engineering practices.
        
        Through guided examples, diagrams, and walkthroughs, the workshop shows how Pulumi’s programming model connects application and infrastructure development. This approach makes cloud architectures easier to understand and change, and reduces friction when managing infrastructure on Google Cloud.
        
        The session focuses on how Pulumi fits into real-world GCP workflows and how teams use it to manage infrastructure consistently across projects and environments.
    learn:
        - How Pulumi models Google Cloud infrastructure using familiar programming constructs
        - How infrastructure as code improves reliability and repeatability on GCP
        - How Pulumi supports consistent infrastructure management across environments on Google Cloud
        
    # The webinar presenters
    presenters:
        - name: Adam Bell
          role: Community Engineer, Pulumi
          photo: /images/team/adam-gordon-bell.jpg

    # case-sensitive
    tags:
        level: Beginner # Beginner, Intermediate, Advanced
        topics: []
        languages: ["any"]
        clouds: ["Google Cloud"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 1ae87a2f-ffee-4e67-926f-c0b893bd8cfb
    salesforce_campaign_id: 701PQ00000pBFcfYAG
    
event_data:
  name: "Getting Started with Infrastructure as Code on Google Cloud"
  start_date: 2026-02-18T12:00:00-05:00
  end_date: 2026-02-18T13:00:00-05:00
  url: "https://www.pulumi.com/events/infrastructure-as-code-google-cloud"
  description: |
    Workshop on infrastructure as code for Google Cloud showing how to define, deploy, and manage GCP resources using familiar programming languages and repeatable workflows. 
---
