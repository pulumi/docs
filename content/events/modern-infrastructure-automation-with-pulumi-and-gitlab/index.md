---
# Name of the event, <= 60 characters
title: Modern Infrastructure Automation with Pulumi and GitLab
meta_desc: Learn how to automate and manage cloud infrastructure using Pulumi's enhanced GitLab integration features for streamlined DevOps workflows.
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
url_slug: modern-infrastructure-automation-with-pulumi-and-gitlab

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Modern Infrastructure Automation with Pulumi and GitLab
    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: 

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2025-06-11T12:00:00-04:00

    # Duration of the webinar.
    duration: 60 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        Managing cloud infrastructure at scale requires robust automation and collaboration tools that seamlessly integrate with your existing development workflows. In this hands-on workshop, you'll learn how to leverage Pulumi's newly enhanced GitLab integration to automate infrastructure deployments, implement effective change management, and establish standardized infrastructure patterns across your organization.

        We'll explore Pulumi's latest GitLab features, including enhanced merge request comments, organizational templates, and first-class VCS support in Pulumi Cloud. You'll learn how to create automated infrastructure pipelines and use organizational templates to standardize infrastructure patterns.


    learn:
        - How to configure and use Pulumi's enhanced GitLab integration features, including detailed merge request comments and organizational templates
        - Techniques for standardizing infrastructure patterns across your organization using Pulumi's template gallery with GitLab repositories


    # The webinar presenters
    presenters:
        - name: Josh Kodroff
          role: Principal Solutions Architect, Pulumi
          photo: /images/team/josh-kodroff.jpg
        - name: Matt Genelin
          role: Solutions Architect, GitLab
          photo: /images/people/matt-genelin.jpg

    # case-sensitive
    tags:
        level: Intermediate # Beginner, Intermediate, Advanced
        topics:  ["CI/CD", "Platform Engineering"]
        languages: ["TypeScript"]
        clouds: ["AWS"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 45641519-d8a1-4507-8e59-da1847c4b743
    salesforce_campaign_id: 701PQ00000VDHioYAH

event_data:
  name: Modern Infrastructure Automation with Pulumi and GitLab
  start_date: 2025-06-11T12:00:00-04:00
  end_date: 2025-06-11T13:00:00-04:00
  url: "https://www.pulumi.com/events/modern-infrastructure-automation-with-pulumi-and-gitlab/"
  description: |
    Managing cloud infrastructure at scale requires robust automation and collaboration tools that seamlessly integrate with your existing development workflows. In this hands-on workshop, you'll learn how to leverage Pulumi's newly enhanced GitLab integration to automate infrastructure deployments, implement effective change management, and establish standardized infrastructure patterns across your organization.

    We'll explore Pulumi's latest GitLab features, including enhanced merge request comments, organizational templates, and first-class VCS support in Pulumi Cloud. You'll learn how to create automated infrastructure pipelines and use organizational templates to standardize infrastructure patterns.
---
