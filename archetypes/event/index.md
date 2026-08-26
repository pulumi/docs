---
# Event title, <= 60 characters.
title: "{{ replace .Name "-" " " | humanize }}"
meta_desc: ""

# Social card. Leave blank to auto-generate an on-brand event card at build time
# (overline + title + presenter "With…" line + Pulumi logo + presenter photos).
# A square 1:1 card is generated alongside it as a second og:image. Set either
# field to override with a custom image committed to this bundle, e.g.
# /events/{{ .Name }}/meta.png. The /event-meta-image skill can produce both,
# plus extra social sizes, and add external co-presenters and partner logos.
# meta_image:
# meta_image_square:

# Overline shown on the generated card. Defaults to event_type (uppercased).
# overline:

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

# The event type (workshop, webinar, talk).
event_type: workshop

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

# Offering the same event on two dates (say an Americas slot and an EMEA one)?
# Add a `sessions:` array instead of duplicating the page. The event keeps one
# URL, one title, and one description; the sessions carry what actually differs.
# Each session gets a tab on the event page and its own card in every list.
#
# sessions:
#     - label: Americas              # required when there's more than one session
#       sortable_date: 2026-09-16T09:00:00.000-07:00
#       duration: 60 minutes         # optional; falls back to the value above
#       form:                        # required per session when gated: true
#           hubspot_form_id: ""
#           salesforce_campaign_id: ""
#       presenters:                  # optional; falls back to the list above.
#           - name: ""               # When every session names its own lineup,
#             role: ""               # delete the top-level list — anything that
#             photo: ""              # needs "everyone" unions the sessions.
#     - label: EMEA
#       sortable_date: 2026-10-14T10:00:00.000+02:00
#
# Two rules `make lint` enforces:
#   - the top-level `sortable_date` above must equal the earliest session's date
#     (it stays the event's own date for sorting, schema, and social cards)
#   - the top-level `form:` above must be removed, so there's no question which
#     form a session renders
#
# One rule it can't: DON'T set `youtube_url` until every session has run. A
# recording turns the page into the on-demand layout, which has no session tabs
# and no registration form — so posting the Americas recording while the EMEA
# date is still weeks out takes the EMEA form off the page, drops the event out
# of the upcoming list, and leaves any `{{< blog/card >}}` embed pointing at a
# session tab that no longer exists. Hold the recording until the last session.
---
