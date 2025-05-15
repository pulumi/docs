---
# Name of the event, <= 60 characters
title: Introduction to Pulumi IaC with AWS in Python
meta_desc: Learn how Pulumi makes working with AWS easier by using general purpose languages like Python to manage infrastructure resources.
meta_image:

# A featured webinar will display first in the list.
featured: false

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

# The url slug for the webinar landing page. If this is an external
# webinar, use the external URL as the value here.
url_slug: getting-started-with-iac-on-aws-python

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Introduction to Pulumi IaC with AWS in Python

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url:

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2025-03-19T09:00:00.000-07:00

    # Duration of the webinar.
    duration: 60 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        This workshop offers a hands-on exploration of how modern infrastructure management can be streamlined using familiar programming languages. In this workshop, you'll discover how Pulumi empowers developers and operations teams to define cloud infrastructure using Python - eliminating the need to learn domain-specific languages while unlocking the full power of software engineering practices for infrastructure code.

        Participants will experience firsthand how Pulumi's approach bridges the gap between application and infrastructure development, allowing teams to manage AWS resources with the same tools, practices, and languages they already use for application development. This workshop demonstrates how this unified approach not only accelerates productivity but enables organizations to build more reliable, scalable, and secure cloud architectures.


    learn:
        - How to use Python with Pulumi to provision AWS resources, bringing modern software development practices to your infrastructure management.
        - How Pulumi's intuitive programming model can help you deploy cloud architecture on AWS with greater confidence and control.
        - How Pulumi's ecosystem supports your infrastructure needs across different environments and cloud providers.

    # The webinar presenters
    presenters:
        - name: Adam Gordon Bell
          role: Community Engineer, Pulumi
          photo: /images/team/adam-gordon-bell.jpg

    # case-sensitive
    tags:
        level: Beginner # Beginner, Intermediate, Advanced
        topics: []
        languages: ["Python"]
        clouds: ["AWS"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 2008e062-29d1-47d5-8d80-d35e9e74e9d7
    salesforce_campaign_id: 701PQ00000TEJoWYAX

event_data:
  name: "Introduction to Pulumi IaC with AWS in Python"
  start_date: 2025-03-19T09:00:00-07:00
  end_date: 2025-03-10T10:00:00-07:00
  url: "https://www.pulumi.com/events/getting-started-with-iac-on-aws-python/"
  description: |
    This workshop offers a hands-on exploration of how modern infrastructure management can be streamlined using familiar programming languages. In this workshop, you'll discover how Pulumi empowers developers and operations teams to define cloud infrastructure using Python - eliminating the need to learn domain-specific languages while unlocking the full power of software engineering practices for infrastructure code.

    Participants will experience firsthand how Pulumi's approach bridges the gap between application and infrastructure development, allowing teams to manage AWS resources with the same tools, practices, and languages they already use for application development. This workshop demonstrates how this unified approach not only accelerates productivity but enables organizations to build more reliable, scalable, and secure cloud architectures.
---