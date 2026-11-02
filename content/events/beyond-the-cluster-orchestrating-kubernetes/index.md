---
# Event title, <= 60 characters (allow_long_title keeps the full Notion title).
title: "Beyond the cluster: Orchestrating Kubernetes and everything around it with Pulumi"
allow_long_title: true
meta_desc: Orchestrate your cluster, your workloads, and everything outside the cluster, safely, from one platform using Pulumi and the Pulumi Kubernetes Operator.

meta_image: /events/beyond-the-cluster-orchestrating-kubernetes/meta.png
meta_image_square: /events/beyond-the-cluster-orchestrating-kubernetes/meta-square.png

# A featured event displays first in the list.
featured: false

# Hide from the event list.
unlisted: false

# Show a registration form. Requires form.hubspot_form_id.
gated: true

# The event type (workshop, webinar, talk).
event_type: workshop

# YouTube embed URL. When set, the event appears in "On-demand recordings".
# When empty, it appears in "Upcoming events".
youtube_url:

# ISO 8601 datetime used for sorting and display.
sortable_date: 2026-11-18T09:00:00.000-08:00

# Human-readable duration.
duration: 60 minutes

# "virtual" or a city/state (e.g., "Seattle, WA").
location: virtual

# Markdown description.
description: |
    Your platform isn't just Kubernetes. It's the cluster, workloads, databases, networks, and cloud services that live outside it, and they all need to change safely over time. In this hands-on workshop, we'll build a multi-tier application with a frontend in Kubernetes and a managed database outside the cluster, connected with stack references. We'll upgrade a cluster with a one-line change and a preview gate, let an AI agent propose infrastructure changes that a human approves, and then run the same programs from inside the cluster using the Pulumi Kubernetes Operator, triggered by a merge to main. You'll leave with a working pattern for orchestrating hybrid infrastructure, whether your team lives in GitOps, CI/CD, or somewhere in between.

# What attendees will learn (rendered as a checklist).
learn:
    - How to manage Kubernetes resources and external cloud services with one language and one Pulumi project.
    - How to run Pulumi programs from inside Kubernetes with the Pulumi Kubernetes Operator while keeping state and history in Pulumi Cloud.
    - How to use Pulumi ESC for short-lived AWS credentials and cluster access, and combine Git-driven reconciliation with previews and drift detection.

# Speakers.
presenters:
    - name: Laci Videmsky
      role: Solutions Architect, Pulumi
      photo: /images/team/laci-videmsky.png

# Used for filtering on the event list page.
tags:
    level: Intermediate # Beginner | Intermediate | Advanced
    topics: ["Kubernetes", "Platform Engineering"]
    languages: ["TypeScript"]
    clouds: ["AWS", "Azure"]

# Registration form (only rendered when gated: true).
form:
    hubspot_form_id: "d0eaf526-3014-42af-a500-c084afea0e40"
    salesforce_campaign_id: "701PQ0000122m5RYAQ"
---
