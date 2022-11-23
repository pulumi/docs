---
# Name of the webinar.
title: "Securing Deployments with Policy as Code"
meta_desc: "The Pulumi team will show you how to enforce best practices by creating policies that scale from a single infrastructure stack to your entire organization."
meta_image: "/images/aws-immersion-day.png"

# A featured webinar will display first in the list.
featured: false

# If the video is pre-recorded or live.
pre_recorded: true

# If the video is part of the PulumiTV series. Setting this value to true will list the video in the "PulumiTV" section.
pulumi_tv: false

# The preview image will be shown on the list page.
preview_image: ""

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

# data for Google Events
event_data:
  name: "Securing Deployments with Policy as Code"
  start_date: 2022-11-15T09:00:00-08:00
  end_date: 2022-11-15T10:30:00-08:00
  url: "https://www.pulumi.com/resources/securing-deployments-policy-as-code"
  description: |
      Poorly configured cloud infrastructure can be an unwelcome source of security, reliability, and cost issues. In this session, the Pulumi team will show you how to enforce best practices by creating policies that scale from a single infrastructure stack to your entire organization. From properly secured S3 buckets to mandatory resource labels, Pulumi’s CrossGuard capability helps you to prevent defective configurations from reaching production.


# The url slug for the webinar landing page. If this is an external
# webinar, use the external URL as the value here.
url_slug: "securing-deployments-policy-as-code"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Securing Deployments with Policy as Code"
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
    title: "AWS Immersion Day: Securing Deployments with Policy as Code"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/mkt1_0q1xc0?rel=0"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2022-11-15T09:00:00-08:00
    # Duration of the webinar.
    duration: "90 minutes"
    # Datetime of the webinar.
    datetime: ""
    # Description of the webinar.
    description: |
        Poorly configured cloud infrastructure can be an unwelcome source of security, reliability, and cost issues. In this session, the Pulumi team will show you how to enforce best practices by creating policies that scale from a single infrastructure stack to your entire organization. From properly secured S3 buckets to mandatory resource labels, Pulumi’s CrossGuard capability helps you to prevent defective configurations from reaching production.

    # The webinar presenters
    presenters:
        - name: Marina Novikova
          role: Senior Partner Solutions Architect, AWS
        - name: Josh Kodroff
          role: Senior Solutions Architect, Pulumi

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - How to write policies using the Python programming language
        - Best practices for implementing and enforcing policies
        - How to use policy packs from AWS to implement best practices for your infrastructure
# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: "ee71f071-222f-4d68-a474-81ba9e801cdf"
    
aws_only: true
---
