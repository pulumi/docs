---
# Name of the event, <= 60 characters
title: Build Infrastructure as Code in Just 60 Seconds
meta_desc: Imagine the power of creating Infrastructure as Code effortlessly. With Pulumi AI, you use natural-language prompts to generate infrastructure as code
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
url_slug: build-infrastructure-as-code-just-60-seconds-modern-infrastructure

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Build Infrastructure as Code in Just 60 Seconds

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: https://www.youtube.com/embed/J7qzeLTaem4?rel=0

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2023-08-09T14:00:12Z

    # Duration of the webinar.
    duration: 2 minutes
    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        Imagine the power of creating Infrastructure as Code effortlessly. With Pulumi AI, you use natural-language prompts to generate infrastructure as code (IaC) programs in the language of your choice, such as TypeScript, Python, Go, C#., Java, or Yaml. Pulumi AI will create all the necessary parts, from the instance itself to the security groups that will allow access. 
        
        🤖 [Try Pulumi AI now](https://www.pulumi.com/ai/) and see the magic unfold!
        
        Prompt used in the video: “Please create a Linux instance I can ssh to”  But that's not all - you can iterate on the cloud infrastructure with the AI assistant, adding new features, fixing bugs, and clarifying requirements. With Pulumi AI, the possibilities are endless.  their online store.

    learn:

    # The webinar presenters
    presenters:
        - name: Carl Holzboog
          role: Solutions Engineer, Pulumi
          photo:

    # case-sensitive
    tags:
        level: Beginner # Beginner, Intermediate, Advanced
        topics: ["Pulumi AI"]
        languages: []

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id:
    salesforce_campaign_id:
---
