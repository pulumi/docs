---
# Name of the event, <= 60 characters
title: "From Pipelines to Cloud: Master IaC with Azure DevOps"
meta_desc: Get hands-on experience automating Azure infrastructure directly from Azure DevOps pipelines.
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
url_slug: from-pipelines-to-cloud

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "From Pipelines to Cloud: Master IaC with Azure DevOps"
    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: https://www.youtube.com/embed/ttUVmRPAzCo?si=PZGBEQeDbB3qd5PR

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2025-11-04T11:00:00-06:00

    # Duration of the webinar.
    duration: 60 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        Get hands-on experience automating Azure infrastructure directly from Azure DevOps pipelines.  
        
        In this practical workshop, you’ll set up an Azure DevOps project that builds and deploys cloud resources automatically, with no manual portal clicks required. Along the way, you’ll explore how Infrastructure as Code tools like Pulumi make it simple to version, preview, and safely update your cloud environments. By the end, you’ll have a fully functional DevOps pipeline that provisions real Azure infrastructure and the confidence to extend it for larger projects.
    learn:
        - How to go from zero to a working Azure DevOps pipeline that deploys real cloud infrastructure
        - How to spin up Azure resources automatically - no portal clicking or ARM templates required
        - How to see every infrastructure change before it happens with Pulumi’s preview system
        - How to commit, push, and watch your cloud update itself from your repo

    # The webinar presenters
    presenters:
        - name: Adam Bell
          role: Community Engineer, Pulumi
          photo: /images/team/adam-gordon-bell.jpg
        - name: Zachary Cook
          role: Engineering Manager, Azure Expert, Pulumi
          photo: /images/team/zachary-cook.jpg

    # case-sensitive
    tags:
        level: Beginner # Beginner, Intermediate, Advanced
        topics:  ["CI/CD & Pipeline Optimization", "Infrastructure as Code"]
        languages: ["Any"]
        clouds: ["Azure"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 30aeaaa7-b035-4e2c-ae9e-a54e8d66c6d3
    salesforce_campaign_id: 701PQ00000htQxBYAU

event_data:
  name: "From Pipelines to Cloud: Master IaC with Azure DevOps"
  start_date: 2025-11-04T11:00:00
  end_date: 2025-11-04T12:00:00
  url: "https://www.pulumi.com/resources/from-pipelines-to-cloud/"
  description: |
        Get hands-on experience automating Azure infrastructure directly from Azure DevOps pipelines.  
        
        In this practical workshop, you’ll set up an Azure DevOps project that builds and deploys cloud resources automatically, with no manual portal clicks required. Along the way, you’ll explore how Infrastructure as Code tools like Pulumi make it simple to version, preview, and safely update your cloud environments. By the end, you’ll have a fully functional DevOps pipeline that provisions real Azure infrastructure and the confidence to extend it for larger projects.
---
