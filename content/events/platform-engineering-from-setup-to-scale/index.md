---
# Name of the event, <= 60 characters
title: "Platform Engineering: Zero to Scale"
meta_desc: Watch the webinar with a 7-step guide to plan, implement, and support your organization's adoption of platform engineering best practices.
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
url_slug: platform-engineering-from-setup-to-scale

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Platform Engineering: Zero to Scale"

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: https://www.youtube.com/embed/t4c3NOiuhXQ?si=dWlnHa0WokwiHYyP

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2024-09-04T09:00:00.000-07:00

    # Duration of the webinar.
    duration: 90 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        Is your organization developing an internal developer platform? How do you know if you're doing it right?

        In this session, you’ll learn when organizations need a platform and how to adopt the practice of platform engineering successfully. You’ll also learn from experienced practitioners how to judge whether your org’s platform efforts are going in the right direction and how to avoid some common and expensive mistakes.

        This workshop is suitable for Platform team contributors, DevOps engineers, IT management, and leadership. You can also read the breakdown in [The Guide to Platform Engineering: 7 Steps to Get It Right](https://www.pulumi.com/blog/the-guide-platform-engineering-idp-steps-best-practices/).

    learn:
        - A step-by-step guide to successfully implement platform engineering in all kinds of organizations.
        - How infrastructure as code, automated controls, reporting, and self-service infrastructure fit into platform engineering efforts.
        - How to handle common pitfalls to implement platform engineering in IT organizations successfully.

    # The webinar presenters
    presenters:
        - name: Josh Kodroff
          role: Senior Solutions Architect, Pulumi
          photo: /images/team/josh-kodroff.jpg

    # case-sensitive
    tags:
        level: # Beginner, Intermediate, Advanced
        topics: ["Platform Engineering","DevOps"]
        languages: []
        clouds: []

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: b51a93db-e8da-4f1c-b7e5-84a2acf5ad54
    salesforce_campaign_id: 701PQ00000HiZpyYAF
---
