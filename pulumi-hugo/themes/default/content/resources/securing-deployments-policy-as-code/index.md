---
# Name of the webinar.
title: Policy as Code on AWS
meta_desc: Learn how to write policies for AWS resources with Pulumi using Python and TypeScript!
meta_image: "/images/resources/policy-as-code-on-aws-marina.png"

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
  name: "Policy as Code on AWS"
  start_date: 2023-11-02T09:00:00-07:00
  end_date: 2023-11-02T10:30:00-07:00
  url: "https://www.pulumi.com/resources/securing-deployments-policy-as-code"
  description: |
      Poorly configured cloud infrastructure can be an unwelcome source of security, reliability, and cost issues. In this session, the Pulumi team will show you how to enforce best practices by creating policies that scale from a single infrastructure stack to your entire organization. And you can do all of this in TypeScript and/or Python!


# The url slug for the webinar landing page. If this is an external
# webinar, use the external URL as the value here.
url_slug: "securing-deployments-policy-as-code"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Policy as Code on AWS"
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
    title: "Policy as Code on AWS"
    # URL for embedding a URL for ungated webinars.
    youtube_url: #"https://www.youtube.com/embed/mkt1_0q1xc0?rel=0"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2023-11-02T09:00:00-07:00
    # Duration of the webinar.
    duration: "90 minutes"
    # Datetime of the webinar.
    datetime: ""
    # Description of the webinar.
    description: |
        Poorly configured cloud infrastructure can be an unwelcome source of security, reliability, and cost issues. In this session, the Pulumi team will show you how to enforce best practices by creating policies that scale from a single infrastructure stack to your entire organization. And you can do all of this in TypeScript and/or Python!

    # The webinar presenters
    presenters:
        - name: Josh Kodroff
          role: Senior Solutions Architect, Pulumi
        - name: Marina Novikova
          role: Sr Partner Solutions Architect, AWS

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - How to write Pulumi policies in TypeScript and Python
        - Best practices for implementing and enforcing policies at scale
        - How to use policy packs from AWS to implement best practices for your infrastructure
# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 2db1d6c8-1d2c-4388-aff7-fd647eb7ec74
    salesforce_campaign_id: 701Du000000BGSgIAO
    
aws_only: true
---
