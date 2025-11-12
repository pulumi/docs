---
# Name of the event, <= 60 characters
title: "Self-Service & AI Agents for Developer Productivity"
meta_desc: Learn how Pulumi AI agents and self-service platforms enable developer productivity with templates, DigitalOcean deployments, and Kubernetes automation.
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
url_slug: self-service-enabling-developer-productivity

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Self-Service - Enabling Developer Productivity"
    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: https://www.youtube.com/embed/gK1N88I0GQ8?si=T17pPuYgupJUL2ON

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2025-11-06T12:00:00-05:00

    # Duration of the webinar.
    duration: 60 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        This hands-on workshop with Pulumi Cloud shows how AI agents and self-service platforms help teams automate infrastructure creation and standardize deployments. Sign up for free to follow along.

In this session, you’ll use Pulumi agents and templates to create a self-service developer platform—building reusable infrastructure patterns and deploying real workloads with automation. Each exercise demonstrates how intelligent agents simplify provisioning, configuration, and GitOps operations while maintaining governance and consistency.
    learn:
        - How to **build and publish Pulumi templates** that power self-service infrastructure provisioning
        - How to **deploy a monitored DigitalOcean** cluster through an **AI-assisted, wizard-style workflow**
        - How to **create reusable Kubernetes components** — like **Argo CD** — with Pulumi TypeScript and ESC environments
        - How **intelligent agents enforce best practices** and scale developer autonomy safely

    # The webinar presenters
    presenters:
        - name: Engin Diri
          role: Senior Solutions Architect, Pulumi
          photo: /images/team/engin-diri.jpg
        - name: Adam Bell
          role: Community Engineer, Pulumi
          photo: /images/team/adam-gordon-bell.jpg

    # case-sensitive
    tags:
        level: Beginner # Beginner, Intermediate, Advanced
        topics:  ["Platform Engineering", "Argo CD", "Kubernetes", "Pulumi Neo", "AI"]
        languages: ["Any"]
        clouds: ["AWS"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 01bea8e9-71fa-430d-953f-2077d3958d15
    salesforce_campaign_id: 701PQ00000edwmiYAA

event_data:
  name: "Self-Service - Enabling Developer Productivity"
  start_date: 2025-11-06T12:00:00-05:00
  end_date: 2025-11-06T13:00:00-05:00
  url: "https://www.pulumi.com/resources/self-service-enabling-developer-productivity/"
  description: |
    Teams building Internal Developer Platforms are betting that standardization and self-service will bring improved productivity to their engineering organization. In this session, we'll explore how agents can help teams launch platforms faster by simplifying the process of creating reusable abstractions and templates that standardize self-service deployments.
---
