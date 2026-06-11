---
# Name of the event, <= 60 characters
title: GitOps with Pulumi and Codefresh
meta_desc: Learn how Pulumi’s infrastructure as code platform and Codefresh make it easy to manage infrastructure code as part of your continuous delivery process.
meta_image:

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

# The url slug for the event landing page. If this is an external
# event, use the external URL as the value here.
url_slug: ci-cd-pipelines-for-kubernetes-apps-with-codefresh

# The event type (workshop, webinar, talk).
event_type: workshop

# URL for embedding a URL for ungated events.
youtube_url: https://www.youtube.com/embed/cv5DDZxM_UM?rel=0

# Sortable date. The datetime Hugo will use to sort the events in date order.
sortable_date: 2022-08-30T09:30:00-07:00

# Duration of the event.
duration: 1 hour

# "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
location: virtual

# Description of the event.
description: |
    Traditionally organizations had completely different methods of deploying
    infrastructure and applications. Teams had to learn completely different tools
    as the lifecycle of an application vs the infrastructure it is hosted on have
    different requirements and limitations.

    GitOps is a set of best practices that redefines the way changes are applied and can be used
    for both infrastructure and applications. Contrary to popular belief GitOps is not constrained
    on Kubernetes applications and simply adopting infrastructure as code is not automatically GitOps.
    In this webinar we will see how you can apply GitOps to both infrastructure (even for non-kubernetes
    environments) and applications using a unified workflow is equally attractive to operators and developers.

learn:
    - How to apply GitOps to both Infrastructure and Applications
    - Infrastructure as code for Kubernetes and non-Kubernetes deployments
    - How to set up a unified workflow for both operators and app developers.

# The event presenters
presenters:
    - name: Mitch Gerdisch
      role: Senior Sales Engineer, Pulumi
      photo: /images/team/mitch-gerdisch.jpg
    - name: Christian Hernandez
      role: Head of Developer Experience and Community Management, Codefresh

# case-sensitive
tags:
    level: Intermediate # Beginner, Intermediate, Advanced
    topics: ["GitOps", "Codefresh"]
    languages: []

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 3a85893b-b023-4467-9e49-03619ce19e6d
    salesforce_campaign_id:
---
