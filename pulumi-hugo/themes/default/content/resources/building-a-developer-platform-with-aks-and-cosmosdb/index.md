---
# Name of the event, <= 60 characters
title: Building a Developer Platform with AKS and Cosmos DB
meta_desc: Set up a platform that includes Azure Kubernetes Service (AKS) with storage by Azure Cosmos DB with API support for MongoDB – using Python and Pulumi.
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
url_slug: building-a-developer-platform-with-aks-and-cosmosdb

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Building a Developer Platform with AKS and Cosmos DB

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: https://www.youtube.com/embed/ESz5-MOfZ04?rel=0

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2022-09-28T09:00:00-07:00

    # Duration of the webinar.
    duration: 1 hour

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
      When platform teams are planning Cloud Native platforms for their application developers, they often need to decide how to manage persistent storage: either as a MongoDB workload running inside their Kubernetes cluster or as a managed service outside of the cluster.

      In this session, we’ll show you how to set up a platform that includes Azure Kubernetes Service (AKS) with scalable persistent storage provided by Azure Cosmos DB with its API support for MongoDB – and we’ll do it all using Python and Pulumi.

    learn:
        - Deploy and manage k8s clusters
        - Deploy and manage Azure Cosmos DB with MongoDB support
        - Deploy and manage K8s services

    # The webinar presenters
    presenters:
      - name: Mitch Gerdisch
        role: Lead Sales Engineer, Pulumi
        photo: /images/team/mitch-gerdisch.jpg
      - name: Jay Gordon
        role: Senior Product Manager, Microsoft

    # case-sensitive
    tags:
        level: Intermediate # Beginner, Intermediate, Advanced
        topics: ["Kubernetes", "AKS"]
        languages: ["Python"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 168f30df-f30e-468e-b603-766e2677e33b
    salesforce_campaign_id:
---