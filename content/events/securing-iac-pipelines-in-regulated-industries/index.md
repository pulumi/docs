---
# Name of the event, <= 60 characters
title: Securing IaC Pipelines in Regulated Industries
meta_desc: Learn best practices for securing and ensuring compliance of AWS infrastructure using Pulumi ESC and Policy as Code in your IaC pipelines.
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
url_slug: securing-iac-pipelines-in-regulated-industries

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Securing IaC Pipelines in Regulated Industries

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url:

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2024-09-26T09:00:00-07:00

    # Duration of the webinar.
    duration: 90 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        Learn foundational best practices for handling secrets and implementing policy controls. We will then demonstrate how to use Pulumi's Environments, Secrets, and Config (ESC) tool, along with the Policy as Code framework, to apply these best practices effectively. You will see a fully functional CI/CD pipeline in action, showcasing how these principles and tools can be used in your organization to ensure continuous compliance.

    learn:
        - Best practices for ensuring security and compliance for cloud infrastructure and secrets.
        - How to use tools like policy as code and automated drift detection.
        - How to to use Policy as Code and ESC (Environments, Secrets, and Config) to improve your organization's security posture.

    # The webinar presenters
    presenters:
        - name: Josh Kodroff
          role: Sr Solutions Architect, Pulumi
          photo: /images/team/josh-kodroff.jpg
        - name: Marina Novikova
          role: Sr. Partner Solutions Architect, AWS
          photo: /images/team/marina-novikova.jpg

    # case-sensitive
    tags:
        level: Intermediate # Beginner, Intermediate, Advanced
        topics: ["Automation", "CI/CD", "DevOps", "Pulumi ESC"]
        languages: []
        clouds: ["AWS"]

# The right hand side form section.
form:
    hubspot_form_id: 59b79ec5-12d3-43ac-a3a9-b0c35905e3a2
    salesforce_campaign_id: 701PQ00000IMd6sYAD
---
