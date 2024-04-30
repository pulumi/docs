---
# Name of the event, <= 60 characters
title: GitOps with Pulumi and Codefresh
meta_desc: Learn how Pulumi’s infrastructure as code platform and Codefresh makes it easy to manage infrastructure code as part of your continuous delivery process.
meta_image:

# A featured webinar will display first in the list.
featured: false

# Webinars with unlisted as true will not be shown on the webinar list
unlisted: false

# Gated webinars will have a registration form and the user will need
# to fill out the form before viewing.
gated: false

# The layout of the landing page.
type: webinars

# External webinars will link to an external page instead of a webinar
# landing/registration page. If the webinar is external you will need
# set the 'block_external_search_index' flag to true so Google does not index
# the webinar page created.
external: false
block_external_search_index: false

# The url slug for the webinar landing page. If this is an external
# webinar, use the external URL as the value here.
url_slug: ci-cd-pipelines-for-kubernetes-apps-with-codefresh

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: GitOps with Pulumi and Codefresh

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: https://www.youtube.com/embed/cv5DDZxM_UM?rel=0

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2022-08-30T09:30:00-07:00

    # Duration of the webinar.
    duration: 1 hour

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        Traditionally organizations had completely different methods of deploying
        infrastructure and applications. Teams had to learn completely different tools
        as the lifecycle of an application vs the instrustructure it is hosted on have
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

    # The webinar presenters
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
