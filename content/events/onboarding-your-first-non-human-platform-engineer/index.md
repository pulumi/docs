---
# Event title, <= 60 characters.
title: "Onboarding your first non-human platform engineer"
meta_desc: "Onboard an AI coding agent onto a real infrastructure repo with Pulumi ESC, Pulumi previews, and Entire's memory and review Trails."

# Co-branded Pulumi + Entire card rendered into this bundle by /event-meta-image
# (adds Lizzie Siegle's photo and the Entire lockup, neither of which the
# build-time default can know about).
meta_image: /events/onboarding-your-first-non-human-platform-engineer/meta.png
meta_image_square: /events/onboarding-your-first-non-human-platform-engineer/meta-square.png

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
sortable_date: 2026-12-08T09:00:00.000-08:00

# Human-readable duration.
duration: "60 minutes"

# "virtual" or a city/state (e.g., "Seattle, WA").
location: virtual

# Markdown description.
description: |
    Your next platform engineer doesn't need a laptop, a desk, or a welcome lunch. It does need what every new hire needs: scoped access, the house rules, a first task, a code review, and room to make a mistake without taking down prod.

    In this session we onboard an AI coding agent onto a real infrastructure repo in one week. Pulumi IaC gives it a plan for every change, and Pulumi ESC gives it credentials that can look but not touch. Entire gives it memory, a record of why it did what it did, and a review process built for agent-written code. You'll leave with an onboarding checklist you can run on your own team.

# What attendees will learn (rendered as a checklist).
learn:
    - "How to give an AI agent cloud access with Pulumi ESC so it can preview changes to production but never apply them"
    - "How to teach an agent your team's infrastructure rules once with Entire's Continuous Memory, so every future session starts with them"
    - "How to review agent-written infrastructure on an Entire Trail, where the intent, the agent session, the review findings, and the Pulumi preview check sit with the diff"
    - "Why a one-line change can pass code review and still delete your database, and how a preview gate stops it before merge"
    - "A five-step onboarding checklist for bringing coding agents onto your own infrastructure repos"

# Speakers.
presenters:
    - name: Engin Diri
      role: Principal Solutions Architect, Pulumi
      photo: /images/team/engin-diri.jpg
    - name: Lizzie Siegle
      role: Staff Developer Advocate, Entire
      photo: /events/onboarding-your-first-non-human-platform-engineer/lizzie-siegle.png

# Used for filtering on the event list page.
tags:
    level: Intermediate # Beginner | Intermediate | Advanced
    topics: ["AI", "Pulumi ESC", "Infrastructure as Code", "CI/CD"]
    languages: []
    clouds: ["AWS"]

# Registration form (only rendered when gated: true).
# TODO: wire in from MA-1262 (https://linear.app/pulumi/issue/MA-1262/date-tbd-pulumi-entire-joint-workshop-engin-entire-presenter-tbd) once marketing creates the form and campaign.
form:
    hubspot_form_id: ""
    salesforce_campaign_id: ""
---
