---
# Name of the event, <= 60 characters
title: PulumiUP 2025 Keynote - New Features & Demos
meta_desc: Explore Pulumi’s Visual IaC Import, Private Registry, and Pulumi IDP—powerful new features that simplify migration, reuse, and internal platform delivery.
meta_image: /images/pulumiup/2025-keynote-meta.png

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
url_slug: pulumiup-2025-keynote

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: PulumiUP 2025 Keynote - New Features & Demos

    event_type: event # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: https://www.youtube.com/embed/q9fDyASy-VA?rel=0

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2025-05-05T09:00:00-00:00

    # Duration of the webinar.
    duration: 1 hour

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        Experience Pulumi's evolution with three game-changing additions to their infrastructure as code ecosystem. This keynote showcases Visual IaC Import for seamless migration, Private Registry for organizing cloud components, and Pulumi IDP—a complete internal developer platform.
        
        Watch demos that illustrate how these tools unite platform teams, security teams, and developers to deliver compliant cloud infrastructure at scale. With 350K+ community members and trusted by companies like NVIDIA and Docker, see why Pulumi is becoming the platform of choice for modern cloud engineering.

        For more details, read the [Pulumi IDP announcement](/blog/announcing-pulumi-idp/).

    # The webinar presenters
    presenters:
        - name: Joe Duffy
          role: CEO, Pulumi
          photo: /images/team/joe-duffy.jpg
        - name: Komal Ali
          role: Engineering Manager, Pulumi
          photo: /images/team/komal-ali.jpg
        - name: Meagan Cojocar
          role: General Manager, IaC, Pulumi
          photo: /images/team/meagan-cojocar.jpg

    # case-sensitive
    tags:
        level: # Beginner, Intermediate, Advanced
        topics: ["Pulumi Features", "Platform Engineering", "DevOps", "Security", "Pulumi IDP"]
        languages: []

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id:
    salesforce_campaign_id:
---