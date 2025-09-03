---
# Name of the event, <= 60 characters
title: "Testing this sworkshop script!"
meta_desc: This is a great meta description, it should be long enough.
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
url_slug: testing-this-sworkshop-script

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Testing this sworkshop script!"
    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: 

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2025-09-30T19:00:00.000-05:00

    # Duration of the webinar.
    duration: 90 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        Some more details here - you'll love this workshop!  Woohoo!
    learn:
        - Learn
        - Love Pulumi
        - Have fun!

    # The webinar presenters
    presenters:
        - name: Pulumipus
          role: Sr Engineer
          photo: /images/team/pulumipus.jpg

    # case-sensitive
    tags:
        level: begineer # Beginner, Intermediate, Advanced
        topics:  ["AI", "Secrurity"]
        languages: ["TypeScript", "Python"]
        clouds: ["AWS"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 123
    salesforce_campaign_id: 456

event_data:
  name: "Testing this sworkshop script!"
  start_date: 2025-09-30T19:00:00.000-05:00
  end_date: 2025-09-30T20:30:00.000-05:00
  url: "https://www.pulumi.com/resources/testing-this-sworkshop-script/"
  description: |
    Some more details here - you'll love this workshop!  Woohoo!
---