---
# Name of the event, <= 60 characters
title: Policy as Code on AWS
meta_desc: In this session, we will show you how to enforce best practices by creating policies that scale from a single infrastructure stack to your entire organization
meta_image: /images/resources/policy-as-code-on-aws-marina.png

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
url_slug: getting-started-policy-as-code

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Policy as Code on AWS

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: https://www.youtube.com/embed/H_LwaEoAL3M?rel=0

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2024-02-14T09:00:00.000-08:00

    # Duration of the webinar.
    duration: 90 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        Poorly configured cloud infrastructure can be an unwelcome source of security, reliability, and cost issues. In this session, the Pulumi team will show you how to enforce best practices by creating policies that scale from a single infrastructure stack to your entire organization. And you can do all of this in TypeScript and/or Python!

    learn:
        - How to create policies for resource level validation.
        - How to create Policy Packs for orgainizing organization wide policies.

    # The webinar presenters
    presenters:
        - name: Josh Kodroff
          role: Sr. Solutions Architect, Pulumi
          photo: /images/team/josh-kodroff.jpg
        - name: Marina Novikova
          role: Sr. Partner Solutions Architect, AWS
          photo: /images/team/marina-novikova.jpg

    # case-sensitive
    tags:
        level: Beginner # Beginner, Intermediate, Advanced
        topics: []
        languages: ["TypeScript", "Python"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 5631e676-649a-4064-8bf3-8a17961c92e8
    salesforce_campaign_id: 701Du000000Bu2zIAC
---
