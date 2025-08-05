---
# Name of the event, <= 60 characters
title: "AWS Immersion Day: Building an IDP with Pulumi"
meta_desc: Learn best practices for platform engineering on AWS and how Pulumi makes it easier than ever to build an Internal Developer Platform (IDP) for your team.
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
url_slug: aws-immersion-day-building-an-idp

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "AWS Immersion Day: Building an IDP with Pulumi"
    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: https://www.youtube.com/embed/oMdNuso6jdM?si=rHV6kLSA0XPT6YKa

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2025-07-24T12:00:00-04:00

    # Duration of the webinar.
    duration: 60 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        Learn how to streamline platform engineering on AWS with an Internal Developer Platform (IDP). This AWS Immersion Day workshop covers best practices for platform engineering on AWS, using Infrastructure as Code (IaC) components to automate infrastructure and codify best practices, strengthen security with short-lived credentials, and gain visibility into AWS environments with Pulumi Insights.
    learn:
        - How Pulumi supports platform engineering and improves AWS infrastructure management.
        - Best practices for using Pulumi and Infrastructure as Code (IaC) across AWS and multi-cloud environments.
        - Strategies to empower developers, reduce operational overhead, and improve your organization's security posture using Pulumi's ecosystem.


    # The webinar presenters
    presenters:
        - name: Rob Smith
          role: Solutions Architect, Pulumi
          photo: /images/team/Rob-Smith.png
        - name: Josh Kodroff
          role: Principal Solutions Architect, Pulumi
          photo: /images/team/josh-kodroff.jpg

    # case-sensitive
    tags:
        level: Intermediate # Beginner, Intermediate, Advanced
        topics:  ["Pulumi Features", "Platform Engineering", "DevOps", "Security", "IaC", "Pulumi IDP"]
        languages: ["TypeScript"]
        clouds: ["AWS"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: dd71b8fd-4896-445c-b5ae-50a6ed95f4b7
    salesforce_campaign_id: 701PQ00000Z0DKUYA3

event_data:
  name: "AWS Immersion Day: Building an IDP with Pulumi"
  start_date: 2025-07-24T12:00:00-04:00
  end_date: 2025-07-24T13:00:00-04:00
  url: "https://www.pulumi.com/resources/aws-immersion-day-building-an-idp/"
  description: |
    Learn how to streamline platform engineering on AWS with an Internal Developer Platform (IDP). This AWS Immersion Day workshop covers best practices for platform engineering on AWS, using Infrastructure as Code (IaC) components to automate infrastructure and codify best practices, strengthen security with short-lived credentials, and gain visibility into AWS environments with Pulumi Insights.
--- 
