---
# Name of the whitepaper.
title: "Name of the Webinar"
meta_desc: "Search Description"

# Set the whitepaper flag.
whitepaper: true

# A featured resource will display first in the list.
featured: false

# Resources with unlisted as true will not be shown on the webinar list
unlisted: false

# Gated resources will have a registration form and the user will need
# to fill out the form before viewing.
gated: false

# The layout of the landing page.
type: webinars

# External resources will link to an external page instead of a resource
# landing/registration page. If the resource is external you will need
# set the 'block_external_search_index' flag to true so Google does not index
# the resource page created.
external: false
block_external_search_index: false

# The url slug for the resource landing page. If this is an external
# resource, use the external URL as the value here.
url_slug: "{{ .Name }}"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: ""

# Content for the left hand side section of the page.
main:
    # Whitepaper title.
    title: ""
    # Sortable date. The datetime Hugo will use to sort the resources in date order.
    sortable_date: 2020-02-05T10:00:00-07:00
    # Duration of the whitepaper.
    duration: "2 hours"
    # Description of the whitepaper.
    description: ""

    # The whitepaper authors
    presenters:
        - name: ""
          role: ""

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - ""

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: ""
---
