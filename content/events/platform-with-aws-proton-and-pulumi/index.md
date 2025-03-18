---
# Name of the event, <= 60 characters
title: Platform Engineering with AWS Proton and Pulumi
meta_desc: In this workshop, you will learn how to enable self-service infrastructure for your organization using AWS Proton and Pulumi.
meta_image: /images/resources/platform-engineering-aws-proton-marina.png
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
url_slug: platform-with-aws-proton-and-pulumi

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Platform Engineering with AWS Proton and Pulumi

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: https://www.youtube.com/embed/OtSreMyaow0?rel=0

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2023-10-12T09:00:00-07:00

    # Duration of the webinar.
    duration: 90 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        In this workshop, you will learn how to enable self-service infrastructure for your organization using AWS Proton and Pulumi. The workshop will include a brief introduction to Pulumi, an infrastructure-as-code platform, where you can use familiar programming languages to provision modern cloud managed service for self-service infrastructure templates.
    
        This 200-level workshop is designed to help users who have basic familiarity with Pulumi effectively handle real-world use cases. We will guide you through using AWS Proton and Pulumi with diagrams and a series of labs to help accelerate your organization's platform engineering efforts.

    learn:
        - How to use Pulumi to manage AWS infrastructure
        - How to use Pulumi with AWS Proton to create and manage reusable templates to ensure self-service compliant and production-ready infrastructure for application teams

    # The webinar presenters
    presenters:
        - name: Josh Kodroff
          role: Senior Solutions Architect, Pulumi
          photo: /images/team/josh-kodroff.jpg
        - name: Marina Novikova
          role: Sr Solutions Architect, AWS
          photo: /images/team/marina-novikova.jpg

    # case-sensitive
    tags:
        level: Intermediate # Beginner, Intermediate, Advanced
        topics: ["AWS Proton"]
        languages: []
        clouds: ["AWS"]

# The right hand side form section.
form:
  hubspot_form_id: 23a0fd24-0fb9-434b-a1d5-f54328284d78
  salesforce_campaign_id: 701Du000000B0VnIAK
---
