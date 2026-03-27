---
# Name of the event.
title: "Taking a K8s Deployment from Default to Secure"
meta_desc: In this session we'll start with a default Nginx deployment and leverage Checkov's Kubernetes yaml scanning capability to go from default to secure.

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
url_slug: "taking-a-k8s-deployment-from-default-to-secure"

# The content of the hero section.
# URL for embedding a URL for ungated events.
youtube_url: "https://www.youtube.com/embed/ouj_0Yx4Mg8"
# Sortable date. The datetime Hugo will use to sort the events in date order.
sortable_date: 2021-10-20T10:20:00-07:00
# Duration of the event.
duration: "25 minutes"
# Description of the event.
description: |
    A Shodan search can quickly reveal over 17 million Nginx servers currently returning a 200 OK. One would think with such adoption that building a secure Nginx Kubernetes deployment would be easy. Surely one would be overwhelmed with online content!

    Whilst best practices are in abundance and security scanning tools for helm and k8s yaml are available, it can be truly difficult to find example code or solid advice on how to successfully follow security best practices. In this session I'll start with a blank canvas of a default Nginx deployment and leverage Checkov's Kubernetes yaml scanning capability to show my own experiences with the easy, the hard and the plain confusing elements of creating a secure Nginx deployment.

# The event presenters
presenters:
    - name: Steve Giguere
      role: Developer Advocate, Bridgecrew by Palo Alto

---
