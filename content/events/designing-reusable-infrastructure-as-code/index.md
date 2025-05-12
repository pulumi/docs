---
# Name of the event, <= 60 characters
title: Designing Reusable Infrastructure as Code
meta_desc: "Master Pulumi Components: Learn to create reusable infrastructure code across languages, enabling DRY principles and powerful cross-team infrastructure sharing."
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
url_slug: designing-reusable-infrastructure-as-code

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Designing Reusable Infrastructure as Code
    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: 

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2025-05-14T12:00:00-04:00

    # Duration of the webinar.
    duration: 60 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        An important tenet of Platform Engineering is building infrastructure code that is DRY (don’t repeat yourself). This makes it easier to maintain core infrastructure components and ensures best practices are reflected in each new instance of your infrastructure.

        In this session, we’ll introduce the concept of Pulumi Components: packages that can be authored in one language and consumed from any other language. This enables platform engineering teams to create powerful patterns for reuse across their organization: sharing infrastructure libraries written in common programming languages that can easily be instantiated from a simple YAML file.
    learn:
        - How to author and share Pulumi Components.
        - Tips for structuring YAML (or any other language!) to consume a Library with maximum reusability.
        - How to integrate reusable components into your IDP.
        - How to reuse existing Terraform modules with your Pulumi programs.


    # The webinar presenters
    presenters:
        - name: Engin Diri
          role: Senior Solutions Architect, Pulumi
          photo: /images/team/engin-diri.jpg

    # case-sensitive
    tags:
        level: Intermediate # Beginner, Intermediate, Advanced
        topics:  ["Platform Engineering", "DevOps"]
        languages: ["TypeScript"]
        clouds: ["AWS"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 083ba5b9-638e-4751-a3cd-eb825376a940
    salesforce_campaign_id: 701PQ00000VDQviYAH

event_data:
  name: Designing Reusable Infrastructure as Code
  start_date: 2025-05-14T12:00:00-04:00
  end_date: 2025-05-14T13:00:00-04:00
  url: "https://www.pulumi.com/resources/designing-reusable-infrastructure-as-code/"
  description: |
    An important tenet of Platform Engineering is building infrastructure code that is DRY (don’t repeat yourself). This makes it easier to maintain core infrastructure components and ensures best practices are reflected in each new instance of your infrastructure.

    In this session, we’ll introduce the concept of Pulumi Components: packages that can be authored in one language and consumed from any other language. This enables platform engineering teams to create powerful patterns for reuse across their organization: sharing infrastructure libraries written in common programming languages that can easily be instantiated from a simple YAML file.
---
