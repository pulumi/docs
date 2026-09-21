---
# Case study for /customers/. Create one with:
#
#   hugo new content/customers/<slug>.md
#
# The slug is the customer name, lowercase and hyphenated, and becomes the URL
# (/customers/<slug>/). Renaming it later changes that URL — add an `aliases:`
# entry for the old one if you do.

title_tag: "{{ replace .Name "-" " " | humanize }} | Case Studies"

# An outcome-oriented headline, not just the company name (e.g.
# "Starburst: 112x deployment acceleration"). Sentence case, per the
# brand guide (brand.pulumi.com/voice/writing-style/).
title: ""

# One or two sentences shown on the customer's grid cell. `description` renders
# on the cell; meta_desc feeds search/social. Max 160 characters for meta_desc.
description: |
    ...
meta_desc: ""

# REQUIRED: the customer's id in data/customers.yaml, which owns their name,
# URL, brand color, and both logo files. Add an entry there first if this
# customer is new — see that file's ADDING A CUSTOMER checklist. `make lint`
# rejects an id that isn't in the registry.
customer: ""

# REQUIRED, singular, closed set: pick exactly one id from
# data/customers_industries.yaml, and the SAME one the registry files this
# customer under — `make lint` fails if the two disagree. It is repeated here
# only because Hugo's taxonomy engine reads front matter, not data files.
industry: ""

# Old URLs that should redirect here. A new case study has none; add an
# entry only when renaming this file (the previous /customers/<slug>/ path).
aliases: []

# Renders the hero panel on the case-study page: logo + quote on the left,
# headline stat on the right. The logo comes from the registry.
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
