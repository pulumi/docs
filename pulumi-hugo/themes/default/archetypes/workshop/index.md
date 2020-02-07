---
# Name of the event.
title: "Name of the Event"
meta_desc: "Search Description"

# The layout of the landing page.
type: events

# The url slug for the even landing page.
url_slug: "{{ .Name }}"

# Event information
event:
    # The type of activities we will be doing at the event.
    type: ["workshop"]
    # The event address
    location: "123 Main St Jacksonville, FL"
    # The start date of an event. Format YYYY-MM-DD
    start_date: "2020-01-01"
    # The end date of an event. Format YYYY-MM-DD
    end_date: "202-01-01"
    # The start and end time of an event with the time zone.
    # i.e. 5:30PM - 8:30PM (PT)
    # This is only displayed on event specific pages.
    time: "5:30PM - 8:30PM (PT)"
    # The event description shown on the event list page.
    description: "Event Description."
    # The Calendly registrtion url for event specific pages.
    calendly_url: "Registration URL"
    # The cost of an event.
    cost: "Free"
---
