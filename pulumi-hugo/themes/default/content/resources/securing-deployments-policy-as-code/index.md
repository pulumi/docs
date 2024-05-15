---
# Name of the event, <= 60 characters
title: Policy as Code on AWS
meta_desc: Learn how to write policies for AWS resources with Pulumi using Python and TypeScript!
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
url_slug: securing-deployments-policy-as-code

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Policy as Code on AWS

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url:

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2024-06-13T09:00:00-07:00

    # Duration of the webinar.
    duration: 90 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        Poorly configured cloud infrastructure can be an unwelcome source of security, reliability, and cost issues. In this session, the Pulumi team will show you how to enforce best practices by creating policies that scale from a single infrastructure stack to your entire organization. And you can do all of this in TypeScript and/or Python!

    learn:
        - How to write Pulumi policies in TypeScript and Python
        - Best practices for implementing and enforcing policies at scale
        - How to use policy packs from AWS to implement best practices for your infrastructure

    # The webinar presenters
    presenters:
        - name: Josh Kodroff
          role: Sr Solutions Architect, Pulumi
          photo: /images/team/josh-kodroff.jpg

    # case-sensitive
    tags:
        level: Beginner # Beginner, Intermediate, Advanced
        topics: []
        languages: ["Python", "TypeScript"]
        clouds: ["AWS"]

# The right hand side form section.
form:
    hubspot_form_id: 2683c422-a64a-433c-a1c5-120bbd7bab02
    salesforce_campaign_id: 701PQ00000CyelHYAR
---
