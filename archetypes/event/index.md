---
# Event title, <= 60 characters.
title: "{{ replace .Name "-" " " | title }}"
meta_desc: ""

# A featured event displays first in the list.
featured: false

# Hide from the event list.
unlisted: false

# Show a registration form. Requires form.hubspot_form_id.
gated: false

# Link to an external page instead of rendering the event page.
# Set block_external_search_index to true when using this.
external: false
block_external_search_index: false

# URL slug for internal events, or external URL when external: true.
url_slug: "{{ .Name }}"

# "workshop" shows a cloud-signup notice; "event" does not.
event_type: workshop # workshop | event

# YouTube embed URL. When set, the event appears in "On-demand recordings".
# When empty, it appears in "Upcoming events".
youtube_url:

# ISO 8601 datetime used for sorting and display.
sortable_date: {{ now.Format "2006-01-02T15:04:05-07:00" }}

# Human-readable duration.
duration: "60 minutes"

# "virtual" or a city/state (e.g., "Seattle, WA").
location: virtual

# Markdown description.
description: |
    Event description.

# What attendees will learn (rendered as a checklist).
learn:
    - ""

# Speakers.
presenters:
    - name: ""
      role: ""
      photo: ""

# Used for filtering on the event list page.
tags:
    level: Beginner # Beginner | Intermediate | Advanced
    topics: []
    languages: []
    clouds: []

# Registration form (only rendered when gated: true).
form:
    hubspot_form_id: ""
    salesforce_campaign_id: ""
---
