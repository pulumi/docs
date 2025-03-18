---
# Name of the event, <= 60 characters
title: Infrastructure as Code - Can we do better?
meta_desc: Watch industry leaders discuss the past, present, and future of Infrastructure as Code (IaC) and overall infrastructure technologies.
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
url_slug: panel-infrastructure-as-code-can-we-do-better

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Infrastructure as Code - Can we do better?

    event_type: event # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: https://www.youtube.com/embed/Stb2Gb6LnXg

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2024-09-18T09:00:00-00:00

    # Duration of the webinar.
    duration: 1 hour

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        Dive into the fascinating journey of infrastructure management, from the early days of manual server provisioning to today’s cutting-edge practices. This panel discussion explores the evolution of Infrastructure as Code (IaC), featuring insights from industry leaders like Adam Jacob, Brian Grant, Elad Ben-Israel, and Luke Hoban.

        Together, they unravel key milestones, discuss ongoing challenges like complexity and standardization, and envision future innovations like AI-driven automation. This panel provides a comprehensive look at the past, present, and future of managing modern cloud environments.

    # The webinar presenters
    presenters:
        - name: Joe Duffy
          role: CEO, Pulumi
          photo: /images/team/joe-duffy.jpg
        - name: Brian Grant
          role: CTO, Stealth
          photo: /images/pulumiup-2023/2024-speakers/brian-grant.jpeg
        - name: Elad Ben-Israel
          photo: /images/team/elad-ben-isreal.jpg
          role: Co-Founder / CEO, Winglang
        - name: Adam Jacob
          photo: /images/pulumiup-2023/2024-speakers/adam-jacob.jpeg
          role: Co-Founder / CEO, System Initiative
        - name: Luke Hoban
          photo: /images/team/luke-hoban.jpg
          role: CTO, Pulumi

    # case-sensitive
    tags:
        level: # Beginner, Intermediate, Advanced
        topics: ["DevOps", "Automation"]
        clouds: ["AWS", "Azure", "Google Cloud"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id:
    salesforce_campaign_id:
---