---
# Name of the webinar.
title: "Getting Started with Policy as Code for Any Cloud"
meta_desc: "Erin Krengel and Cameron Stokes will demonstrate practical examples for defining and enforcing policies on AWS, Azure and GCP."

# If the video is pre-recorded or live.
pre_recorded: false

# If the video is part of the PulumiTV series. Setting this value to true will list the video in the "PulumiTV" section.
pulumi_tv: false

# The preview image will be shown on the list page.
preview_image: "/images/webinar/pulumi_tech_talk.png"

# Webinars with unlisted as true will not be shown on the webinar list
unlisted: false

# Gated webinars will have a registration form and the user will need
# to fill out the form before viewing.
gated: true

# The layout of the landing page.
type: webinars

# External webinars will link to an external page instead of a webinar
# landing/registration page.
external: false

# The url slug for the webinar landing page. If this is an external
# webinar, use the external URL as the value here.
url_slug: "getting-started-policy-as-code-2020-04-09"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Getting Started with Policy as Code for Any Cloud"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Getting Started with Policy as Code for Any Cloud"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2020-04-09 11:00:00 -07:00
    # Datetime of the webinar.
    datetime: "THU APR 09, 2020 AT 11:00AM TO 12:00PM PDT"
    # Description of the webinar.
    description: |
        Poorly configured cloud infrastructure is a common source of security, reliability and cost issues that result in the types of headlines that make executive leaders cringe. The Pulumi team will show you how to enforce best practices by creating durable policies that scale from a single infrastructure stack to company-wide policies. From properly secured S3 buckets to mandated resource labels, Pulumi’s Policy as Code capabilities help you to prevent defective configurations from impacting your cloud of choice.

    # The webinar presenters
    presenters:
        - name: Erin Krengel
          role: Software Engineer, Pulumi
        - name: Cameron Stokes
          role: Customer Engineer, Pulumi

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - How to create policies for resource level validation.
        - How to create Policy Packs for orgainizing organization wide policies.

# The right hand side form section.
form:
    # GoToWebinar webinar key. This key allows us to register people for webinars via the
    # HubSpot form.
    gotowebinar_key: "9002810409971052299"

    # HubSpot form id.
    hubspot_form_id: "5b1083f6-e034-459c-a1b6-f2bc6d900963"
---
