---
# Name of the event, <= 60 characters
title: AI in Cloud Development
meta_desc: Explore how AI is shaping cloud development, from coding to infrastructure and observability, with expert insights on current successes and future possibilities
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
url_slug: panel-ai-in-cloud-development

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: AI in Cloud Development

    event_type: event # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: https://www.youtube.com/embed/eiVTfB3Qrqo

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2024-09-18T09:00:00-00:00

    # Duration of the webinar.
    duration: 1 hour

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        The panel discussed the role that AI is playing in the present and (near) future of cloud development across infrastructure and applications. Software development has seen some of the richest applications of novel generative AI-based experiences, and these tools continue to expand their scope from coding assistants to task planning to agents.

        Cloud development, in particular, has seen these benefits extended across the lifecycle, with exciting applications to IaC, policy, observability, and more. Hear from some of the industry experts at the forefront of applying modern AI approaches to all these areas of cloud development—what they see working well already at scale and what they are excited about for the future.

    # The webinar presenters
    presenters:
        - name: Luke Hoban
          role: CTO, Pulumi
          photo: /images/team/luke-hoban.jpg
        - name: Meagan Cojocar
          role: Principal Product Manager, Pulumi
          photo: /images/team/meagan-cojocar.jpg
        - name: Giri Sreenivas
          photo: /images/pulumiup-2023/2024-speakers/giri-sreenivas.jpg
          role: Chief Product Officer, Docker
        - name: Phillip Carter
          photo: /images/pulumiup-2023/2024-speakers/phillip-carter.jpg
          role: Principal Product Manager, HoneyComb.io
        - name: Clare Liguori
          photo: /images/pulumiup-2023/2024-speakers/clare-liguori.jpg
          role: Sr. Principal Software Engineer, AWS

    # case-sensitive
    tags:
        level: # Beginner, Intermediate, Advanced
        topics: ["AI", "Automation", "Observability"]
        languages: []

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id:
    salesforce_campaign_id:
---