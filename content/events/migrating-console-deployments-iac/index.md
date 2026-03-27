---
# Name of the event, <= 60 characters
title: "Migrating from Console Deployments to Infrastructure as Code"
meta_desc: Help your organization move faster by adopting automation with Infrastructure as Code
meta_image:

# A featured event will display first in the list.
featured: false

# Events with unlisted as true will not be shown on the event list
unlisted: false

# Gated events will have a registration form and the user will need
# to fill out the form before viewing.
gated: true

# External events will link to an external page instead of an event
# landing/registration page. If the event is external you will need
# set the 'block_external_search_index' flag to true so Google does not index
# the event page created.
external: false
block_external_search_index: false

# The url slug for the event landing page. If this is an external
# event, use the external URL as the value here.
url_slug: migrating-console-deployments-iac

# The event type (workshop, webinar, talk).
event_type: workshop

# URL for embedding a URL for ungated events.
youtube_url: 

# Sortable date. The datetime Hugo will use to sort the events in date order.
sortable_date: 2025-01-15T09:00:00-08:00

# Duration of the event.
duration: 90 minutes

# "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
location: virtual

# Description of the event.
description: |
   As organizations scale their cloud operations, managing infrastructure through manual console deployments becomes increasingly risky and time-consuming. This workshop bridges the gap between click-ops and modern infrastructure automation, providing both technical guidance and business context for adopting Infrastructure as Code (IaC).
   
   Participants will learn how platform engineering practices can accelerate delivery while improving reliability and security. Through hands-on demonstrations using Pulumi, attendees will discover practical strategies for transitioning existing console-created resources to code, establishing repeatable deployment patterns, and building a foundation for scalable infrastructure management. The session combines technical demonstrations with real-world business cases, making it valuable for both technical practitioners and decision-makers looking to modernize their infrastructure practices.

learn:
    - The benefits of adopting platform engineering as a practice
    - How to start your platform engineering by adopting infrastructure as code
    - How to take resources created manually in the console and bring them under IaC automation

# The event presenters
presenters:
    - name: Josh Kodroff 
      role: Principal Solutions Architect, Pulumi
      photo: /images/team/josh-kodroff.jpg
    - name: Torian Crane
      role: Senior Technical Content Engineer, Pulumi
      photo: /images/team/torian-crane.jpg

# case-sensitive
tags:
    level: Intermediate # Beginner, Intermediate, Advanced
    topics: ["Platform Engineering"]
    languages: ["TypeScript"]
    clouds: ["AWS"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 2ca022a2-1604-4236-95c7-1e74a63bfe8f
    salesforce_campaign_id: 701PQ00000ObL1IYAV

---
