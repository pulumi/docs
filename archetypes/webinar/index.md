---
# Name of the webinar.
title: "Name of the Webinar"
meta_desc: "Search Description"

# A featured webinar will display first in the list.
featured: false

# If the video is pre-recorded or live.
pre_recorded: false

# If the video is part of the PulumiTV series. Setting this value to true will list the video in the "PulumiTV" section.
pulumi_tv: false

# The preview image will be shown on the list page.
preview_image: ""

# Webinars with unlisted as true will not be shown on the webinar list
unlisted: false

# Gated webinars will have a registration form and the user will need
# to fill out the form before viewing.
gated: false

# The layout of the landing page.
type: webinars

# External webinars will link to an external page instead of a webinar
# landing/registration page.
external: false

# The url slug for the webinar landing page. If this is an external
# webinar, use the external URL as the value here.
url_slug: "{{ .Name }}"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: ""
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: ""
    # URL for embedding a URL for ungated webinars.
    youtube_url: ""
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2019-02-05 10:00:00 -07:00
    # Datetime of the webinar.
    datetime: ""
    # Description of the webinar.
    description: ""

    # The webinar presenters
    presenters:
        - name: ""
          role: ""

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - ""

# The right hand side form section.
form:
    # GoToWebinar webinar key. This key allows us to register people for webinars via the
    # HubSpot form.
    gotowebinar_key: ""

    # HubSpot form id.
    hubspot_form_id: ""
---
