---
# Name of the event, <= 60 characters
title: "Migrating IaC from Terraform to TypeScript"
meta_desc: Learn how to leverage TypeScript's flexibility and ecosystem to simplify your infrastructure code and streamline cloud operations.
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
url_slug: migrating-iac-terraform-to-typescript

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Migrating IaC from Terraform to TypeScript"

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: 

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2025-01-29T09:00:00-08:00

    # Duration of the webinar.
    duration: 90 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
       Organizations often find themselves constrained by domain-specific languages when managing cloud infrastructure, leading to complex workarounds and maintenance challenges. This workshop demonstrates how transitioning to a general-purpose programming language can transform your infrastructure management, making common tasks more intuitive and maintainable.
       
       You'll discover how TypeScript's rich ecosystem of libraries and familiar syntax can simplify everything from dynamic resource creation to complex configuration management. Through practical examples, we'll explore strategies for gradually migrating existing infrastructure code while maintaining operational stability.
       
       Whether you're dealing with repetitive boilerplate, struggling with complex state management, or seeking more flexibility in your infrastructure automation, you'll learn how to leverage TypeScript's capabilities to build more elegant and powerful infrastructure solutions that scale with your organization's needs.

    learn:
        - How general-purpose languages like TypeScript make infrastructure management easier compared to domain-specific languages like HCL and YAML
        - How to introduce Pulumi IaC and either coexist with or convert your existing Terraform code
        - How Pulumi's advanced features can help enable even greater capabilities for your organization to keep teams moving fast, securely

    # The webinar presenters
    presenters:
        - name: Josh Kodroff 
          role: Principal Solutions Architect, Pulumi
          photo: /images/team/josh-kodroff.jpg

    # case-sensitive
    tags:
        level: Intermediate # Beginner, Intermediate, Advanced
        topics: ["Platform Engineering"]
        languages: ["TypeScript"]
        clouds: ["AWS"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 53f23815-4b41-45ce-a926-1dc69e5a50b5
    salesforce_campaign_id: 701PQ00000Obc8XYAR

event_data:
  name: "Migrating IaC from Terraform to TypeScript"
  start_date: 2025-01-29T09:00:00-08:00
  end_date: 2025-01-29T10:00:00-08:00
  url: "https://www.pulumi.com/resources/migrating-iac-terraform-to-typescript/"
  description: |
    Organizations often find themselves constrained by domain-specific languages when managing cloud infrastructure, leading to complex workarounds and maintenance challenges. This workshop demonstrates how transitioning to a general-purpose programming language can transform your infrastructure management, making common tasks more intuitive and maintainable.
    
    You'll discover how TypeScript's rich ecosystem of libraries and familiar syntax can simplify everything from dynamic resource creation to complex configuration management. Through practical examples, we'll explore strategies for gradually migrating existing infrastructure code while maintaining operational stability.
    
    Whether you're dealing with repetitive boilerplate, struggling with complex state management, or seeking more flexibility in your infrastructure automation, you'll learn how to leverage TypeScript's capabilities to build more elegant and powerful infrastructure solutions that scale with your organization's needs.
---
