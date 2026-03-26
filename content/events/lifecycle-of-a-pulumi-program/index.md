---
# Name of the event.
title: "Lifecycle of a Pulumi Program"
meta_desc: In this talk, you will learn how Apple leveraged a custom state backend with SSO, RBAC, and pipelines powered by the Pulumi Automation API to drive IaC.

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
url_slug: "lifecycle-of-a-pulumi-program"

# The content of the hero section.
# URL for embedding a URL for ungated events.
youtube_url: "https://www.youtube.com/embed/5U7q9miKWj0"
# Sortable date. The datetime Hugo will use to sort the events in date order.
sortable_date: 2021-10-20T15:00:00-07:00
# Duration of the event.
duration: "24 minutes"
# Description of the event.
description: |
    Infrastructure as Code provides a way for teams and companies to standardize the way they manage and secure applications. In this talk, Fariba Khan and Stephen Van Gordon will share how they leverage a custom state backend with SSO, RBAC, and programmatically configurable pipelines powered by CICD tooling and the Pulumi Automation API to drive IaC at Apple.

    This framework of tools enables teams to provision secure-by-default Compute, Storage, Identity, Ingress, and other components available in multiple languages in very little time and without any manual interventions. This experience is complemented by operations-friendly workflows previewing infrastructure changes between deployments, as well as cost and policy violations directly in Github comments. This results in reduced cognitive overhead when making changes to a deployment. Finally, by providing the state store for IaC stacks our team gains insight into usage patterns, security issues, and compliance via rich data and analytics.

# The event presenters
presenters:
    - name: Fariba Khan
      role: Engineer, Cloud Services, Apple
    - name: Stephen Van Gordon
      role: Engineer, Cloud Services, Apple

---
