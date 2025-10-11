---
# Name of the event.
title: "Name of the Event"

# Events with unlisted as true will not be shown on the event list
unlisted: false

# Events with external registrations should not be indexed
# and have redirect to the external registration page.
block_external_search_index: true
redirect_to: "/"

# Schema type for structured data (SEO). Options: auto, faq, article, blog, howto, product, event, none
# Events typically use 'event' schema. Leave as 'auto' (or omit) for intelligent detection.
# See SCHEMA.md for details.
schema_type: auto

# Event information
event:
    # The type of activities we will be doing at the event.
    type: ["talk", "booth"]
    # The event address
    location: "123 Main St Jacksonville, FL"
    # The start date of an event. Format YYYY-MM-DD
    start_date: "2020-01-01"
    # The end date of an event. Format YYYY-MM-DD
    end_date: "2020-01-01"
    # The event description shown on the event list page.
    description: "This the event description."
    # The external registration url for the event list page.
    registration_url: "/"
---
