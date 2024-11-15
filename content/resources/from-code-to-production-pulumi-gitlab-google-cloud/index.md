---
# Name of the event, <= 60 characters
title: From Code to Production with Pulumi, GitLab and Google Cloud
meta_desc: Learn how to use Pulumi's GitLab integration to build CI/CD pipelines, empowering teams to deliver software safely, reproducibly, and faster.
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
url_slug: from-code-to-production-pulumi-gitlab-google-cloud

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: From Code to Production with Pulumi, GitLab and Google Cloud

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: #https://www.youtube.com/embed/l8Ha60IJ6m8?si=AiKU_4MK3w3aAE_l?rel=0

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2024-12-16T09:00:00-08:00

    # Duration of the webinar.
    duration: 90 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        In this workshop, explore how Pulumi’s integration with GitLab empowers teams to create robust CI/CD pipelines for managing cloud infrastructure on Google Cloud. You’ll learn to leverage Pulumi’s declarative Infrastructure as Code (IaC) for provisioning and scaling resources, along with GitLab's DevSecOps platform..
        
        The session will dive into GitLab’s enterprise collaboration and CI/CD pipelines, including automated security checks for infrastructure. Attendees will gain hands-on experience with secrets management and automated deployments, using ESC secrets for enhanced security. By the end, you’ll be equipped to streamline infrastructure and application delivery across teams, reducing complexity and risk while maximizing flexibility and control.

    learn:
        - How to create GitLab pipelines for your infrastructure as code on Google Cloud (GCP).
        - How to use the GitLab security scanning and Pulumi provider to manage your GitLab resources.
        - How to use Pulumi's Policy as Code and ESC (Environments, Secrets, and Config) to improve your organization's security posture.

    # The webinar presenters
    presenters:
        - name: Tom Weston
          role: Customer Success Architect, Pulumi
          photo: /images/team/tom-weston.jpeg
        - name: Regnard Raquedan
          role: Senior Partner Solutions Architect, GitLab
          photo: /images/people/regnard-raquedan.jpeg
        - name: Jason Smith
          role: Sr Cloud Customer Engineer, Google
          photo: /images/people/jay-smith.png

    # case-sensitive
    tags:
        level: Intermediate # Beginner, Intermediate, Advanced
        topics: ["Automation", "CI/CD", "Platform Engineering"]
        languages: ["TypeScript"]
        clouds: ["Google Cloud"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 722fb75e-1716-43a0-bd04-6229b86ed256
    salesforce_campaign_id: 701PQ00000Me8GkYAJ

event_data:
  name: "From Code to Production with Pulumi, GitLab and Google Cloud"
  start_date: 2024-12-16T09:00:00-08:00
  end_date: 2024-12-16T10:30:00-08:00
  url: "https://www.pulumi.com/resources/from-code-to-production-pulumi-gitlab-google-cloud/"
  description: |
    In this workshop, explore how Pulumi’s integration with GitLab empowers teams to create robust CI/CD pipelines for managing cloud infrastructure on Google Cloud. You’ll learn to leverage Pulumi’s declarative Infrastructure as Code (IaC) for provisioning and scaling resources, along with GitLab's DevSecOps platform..
        
    The session will dive into GitLab’s enterprise collaboration and CI/CD pipelines, including automated security checks for infrastructure. Attendees will gain hands-on experience with secrets management and automated deployments, using ESC secrets for enhanced security. By the end, you’ll be equipped to streamline infrastructure and application delivery across teams, reducing complexity and risk while maximizing flexibility and control.
---
