---
# Name of the event, <= 60 characters
title: "Pulumi for All Your IaC: Including Terraform and HCL"

meta_desc: Connect existing Terraform workloads to Pulumi Cloud, reuse Terraform modules in Pulumi programs, and write IaC in OpenTofu-compatible HCL — live workshop.

# A featured event will display first in the list.
featured: false

# Events with unlisted as true will not be shown on the event list
unlisted: false

# Gated events will have a registration form and the user will need
# to fill out the form before viewing.
gated: true

# External events will link to an external page instead of an event
# landing/registration page.
external: false
block_external_search_index: false

# The url slug for the event landing page.
url_slug: pulumi-for-all-your-iac-terraform-hcl

# The event type (workshop, webinar, talk).
event_type: workshop

# URL for embedding a URL for ungated events.
youtube_url:

# Sortable date. The datetime Hugo will use to sort the events in date order.
sortable_date: 2026-08-19T12:00:00.000-07:00

# Duration of the event.
duration: 60 minutes

# "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
location: virtual

# Description of the event.
description: |
    Your platform team spent a decade building production Terraform, and you can't just throw it all away because you want to embrace the agentic future of infrastructure. Here's the thing: you don't have to choose because Pulumi Cloud now supports the Terraform estate you already have. There's no migration project, no rewrite and no new deployment pattern to learn.

    In this live demo, Daniel walks through three scenarios: pointing an existing Terraform Enterprise workload at Pulumi Cloud and watching remote plans, approvals, and deployments keep working exactly as they did before; reusing existing Terraform modules inside a brand-new Pulumi program; and writing infrastructure in HCL as a fully OpenTofu-compatible, first-class Pulumi language.
learn:
    - How to turn on guardrails Terraform alone doesn't give you using Neo AI code review.
    - How to reuse existing Terraform modules inside a new Pulumi program.
    - How to write Pulumi IaC in HCL. 100% OpenTofu-compatible, with access to the full Pulumi provider ecosystem.

# The event presenters
presenters:
    - name: Daniel Perlovsky
      role: Principal Product Manager, Pulumi
      photo: /images/team/daniel-perlovsky.jpg
    - name: Adam Gordon Bell
      role: Community Engineer, Pulumi
      photo: /images/team/adam-gordon-bell.jpg

# case-sensitive
tags:
    level: Beginner # Beginner, Intermediate, Advanced
    topics: ["Terraform", "Infrastructure as Code"]
    languages: []
    clouds: []

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 17009b6b-9d0c-4f9b-a144-96aa699d1ba6
    salesforce_campaign_id: 701PQ00000yh82zYAA
---
