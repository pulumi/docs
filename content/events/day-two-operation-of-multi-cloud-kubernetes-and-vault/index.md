---
# Name of the event.
title: "Day-two Operation of Multi-cloud Kubernetes and Vault"
meta_desc: In this session you learn how Snowflake worked towards implementation and the day-2 experience of using Pulumi to manage Kubernetes and Vault.

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
url_slug: "day-two-operation-of-multi-cloud-kubernetes-and-vault"

# The content of the hero section.
# URL for embedding a URL for ungated events.
youtube_url: "https://www.youtube.com/embed/0iAwwtjQvhw"
# Sortable date. The datetime Hugo will use to sort the events in date order.
sortable_date: 2021-10-20T10:50:00-07:00
# Duration of the event.
duration: "20 minutes"
# Description of the event.
description: |
    Snowflake is multi-cloud. So is its infrastructure. For two years, Snowflake’s platform team has been building and operating 100 (and growing) Kubernetes clusters on AWS, Azure, and Google Cloud. Today, we run on average a total of 60k Pods to unlock $7M annual savings.

    We use Pulumi to provision cloud resources and manage HashiCorp Vault. In this talk, I will present how Pulumi has enabled Snowflake’s scale and growth:
    * How we leverage Pulumi Automation API to build custom rollout strategy for all Pulumi stacks
    * How we achieve blue-green upgrades for Kubernetes node pools
    * How we manage HashiCorp Vault using Pulumi:
        - rotating issuing certs (that signs Istio private gateway TLS cert)
        - static secrets (such as Teleport join-root token so k8s users could use one CLI to access all clusters and nodes)
        - cloud-provider secret engine (to generate scoped and short-lived tokens for services and automation)
    * How we generate and manage cloud-agnostic Kubernetes manifests by integrating with Pulumi stack outputs
    * How we use Pulumi Operator in CICD for auto-apply and audit

    This talk differs from the one my colleagues did in the Cloud Engineering Summit 2020. They focused on the container platform design (logging, monitoring, networking, etc). I will lean more towards implementation and the day-2 experience of using Pulumi.

# The event presenters
presenters:
    - name: Charles Xu
      role: Senior Software Engineer, Snowflake

---
