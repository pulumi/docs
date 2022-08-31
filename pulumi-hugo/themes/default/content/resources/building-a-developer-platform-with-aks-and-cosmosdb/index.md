---
# Name of the webinar.
title: "Building a Developer Platform with AKS and Cosmos DB"
meta_desc: "Set up a platform that includes Azure Kubernetes Service (AKS) with storage by Azure Cosmos DB with API support for MongoDB – using Python and Pulumi."

# A featured webinar will display first in the list.
featured: false

# If the video is pre-recorded or live.
pre_recorded: false

# If the video is part of the PulumiTV series. Setting this value to true will list the video in the "PulumiTV" section.
pulumi_tv: false

# The preview image will be shown on the list page.
preview_image: ""

# Webinars with unlisted as true will not be shown on the webinar list
unlisted: false

# Gated webinars will have a registration form and the user will need
# to fill out the form before viewing.
gated: true

# The layout of the landing page.
type: webinars

# External webinars will link to an external page instead of a webinar
# landing/registration page. If the webinar is external you will need
# set the 'block_external_search_index' flag to true so Google does not index
# the webinar page created.
external: false
block_external_search_index: false

# data for Google Events
event_data:
  name: Pulumi - Building a Developer Platform with AKS and Cosmos DB
  start_date: 2022-09-28T09:00:00-07:00
  end_date: 2022-09-28T10:30:00-07:00
  url: "https://www.pulumi.com/resources/building-a-developer-platform-with-aks-and-cosmosdb/"
  description: |
    When platform teams are planning Cloud Native platforms for their application developers, they often need to decide how to manage persistent storage: either as a MongoDB workload running inside their Kubernetes cluster or as a managed service outside of the cluster.

    In this session, we’ll show you how to set up a platform that includes Azure Kubernetes Service (AKS) with scalable persistent storage provided by Azure Cosmos DB with its API support for MongoDB – and we’ll do it all using Python and Pulumi.

# The url slug for the webinar landing page. If this is an external
# webinar, use the external URL as the value here.
url_slug: "building-a-developer-platform-with-aks-and-cosmosdb"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Building a Developer Platform with AKS and Cosmos DB"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Webinar pages support multiple session via the 'multiple' property.
# multiple:
#   - datetime: 2020-02-05T10:00:00-07:00
#     hubspot_form_id: ""
#     gotowebinar_key: ""

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Building a Developer Platform with AKS and Cosmos DB"
    # URL for embedding a URL for ungated webinars.
    youtube_url: ""
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2022-09-28T09:00:00-07:00
    # Duration of the webinar.
    duration: "90 minutes"
    # Datetime of the webinar.
    datetime: ""
    # Description of the webinar.
    description: |
        When platform teams are planning Cloud Native platforms for their application developers, they often need to decide how to manage persistent storage: either as a MongoDB workload running inside their Kubernetes cluster or as a managed service outside of the cluster.

        In this session, we’ll show you how to set up a platform that includes Azure Kubernetes Service (AKS) with scalable persistent storage provided by Azure Cosmos DB with its API support for MongoDB – and we’ll do it all using Python and Pulumi.

    # The webinar presenters
    presenters:
        - name: Mitch Gerdisch
          role: Lead Sales Engineer, Pulumi
        - name: Jay Gordon
          role: Senior Product Manager, Microsoft

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - Deploy and manage k8s clusters
        - Deploy and manage Azure Cosmos DB with MongoDB support
        - Deploy and manage K8s services
form:
    hubspot_form_id: "168f30df-f30e-468e-b603-766e2677e33b"
---