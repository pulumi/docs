---
# Case study for /case-studies/. Create one with:
#
#   hugo new content/case-studies/<slug>.md
#
# The slug is the customer name, lowercase and hyphenated.

title_tag: "{{ replace .Name "-" " " | humanize }} | Case Studies"

# An outcome-oriented headline, not just the company name (e.g.
# "Starburst: 112x deployment acceleration"). Sentence case, per the
# brand guide (brand.pulumi.com/voice/writing-style/).
title: ""
layout: case-studies

# One or two sentences shown on the case-study card. `description` renders on
# the card; meta_desc feeds search/social. Max 160 characters for meta_desc.
description: |
    ...
meta_desc: ""

customer_name: "{{ replace .Name "-" " " | title }}"

# REQUIRED, singular, closed set: pick exactly one id from
# data/case_study_industries.yaml. `make lint` enforces this.
industry: ""

# Logo assets live in assets/fingerprinted/logos/customers/. customer_logo is
# rendered on LIGHT backgrounds (case-study page quote panel, template-page
# partials) — never point it at a white/light asset.
customer_logo: /logos/customers/<slug>.svg

# Logo-tile fields for the case-studies board card (all optional; validated by
# `make lint`; full docs in layouts/partials/case-studies/card.html):
#   logo_bg_color  tile background — the customer's brand color. Omit for gray.
#   card_logo      tile-only logo override (e.g. an official white variant).
#   logo_style     white | dark — CSS-filter mono silhouette of the logo.
#   logo_size      lg — for wide wordmarks or small-viewBox SVGs that read small.
# logo_bg_color: "#0052CC"
# card_logo: /logos/customers/<slug>-white.svg
# logo_style: white
# logo_size: lg

customer_url: https://example.com

# Renders the hero panel on the case-study page: logo + quote on the left,
# headline stat on the right.
quote_block:
    quote: |
        "..."
    quote_attrib: Name, Title, Company
    headline_stat: ""
    headline: ""

# In-page TOC. Anchors must match the H2 ids in the body below.
sections:
    - label: Exec Summary
      anchor: executive-summary
    - label: Challenges
      anchor: challenges
    - label: Solution
      anchor: solution
    - label: Results
      anchor: results
---

## Executive summary

...

## Challenges

...

## Solution

...

## Results

...
