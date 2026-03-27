---
# Name of the event.
title: "Software Engineering in Infrastructure Engineering"
meta_desc: In this talk, you will go through how to use the software engineering process to solve this infrastructure engineering problem.

# A featured event will display first in the list.
featured: false

# Events with unlisted as true will not be shown on the event list
unlisted: false

# Gated events will have a registration form and the user will need
# to fill out the form before viewing.
gated: false

# External events will link to an external page instead of an event
# landing/registration page. If the event is external you will need
# set the 'block_external_search_index' flag to true so Google does not index
# the event page created.
external: false
block_external_search_index: false

# The event type (workshop, webinar, talk).
event_type: talk
# The url slug for the event landing page. If this is an external
# event, use the external URL as the value here.
url_slug: "software-engineering-in-infrastructure-engineering"

# The content of the hero section.
# URL for embedding a URL for ungated events.
youtube_url: "https://www.youtube.com/embed/T0lbD5n9ID8"
# Sortable date. The datetime Hugo will use to sort the events in date order.
sortable_date: 2021-10-20T09:30:00-07:00
# Duration of the event.
duration: "18 minutes"
# Description of the event.
description: |
    When we think about the concept that is Software Engineering, we think about building well-designed software that solves the problems our customers face. The key takeaway here is that software engineers are problem solvers.

    In the world of infrastructure deployments, there are many problems that exist because of the software engineering problems we are trying to solve. Pretty ironic, right? We attempt to solve problems only to create more :). A major problem for a cloud service is having multiple instances of the service in multiple regions and maintaining high availability for users.

    As great as IaC (Infrastructure as Code) is, it can be a problem maintaining different configurations for different environments where each environment has multiple instances with varying configurations.

    In this talk, I will go through how I use the software engineering process in conjunction with pulumi stacks and state, to solve this infrastructure engineering problem.

# The event presenters
presenters:
    - name: Adora Nwodo
      role: Software Engineer at Microsoft

---
