---
# Name of the webinar.
title: "Getting Started Severless On AWS with Pulumi"
meta_desc: "Learn how  Pulumi's IaC platform can help remove the complexity and enable beginners to quickly get up to speed with serverless architectures."

# A featured webinar will display first in the list.
featured: false

# If the video is pre-recorded or live.
pre_recorded: false

# If the video is part of the PulumiTV series. Setting this value to true will list the video in the "PulumiTV" section.
pulumi_tv: false

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
external: true
block_external_search_index: true

# The url slug for the webinar landing page. If this is an external
# webinar, use the external URL as the value here.
url_slug: "https://webinars.devops.com/getting-started-with-serverless-on-aws-with-pulumi?utm_campaign=2023.07.17_AWS_Pulumi_Webinar_DO&utm_source=pulumi&utm_medium=referral"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Getting Started Severless On AWS with Pulumi"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Getting Started Severless On AWS with Pulumi"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2023-07-17T12:00:00-07:00
    # Duration of the webinar.
    duration: "1 hour"
    # Datetime of the webinar.
    datetime: "July 17, 2023"
    # Description of the webinar.
    description: |
        Getting started with serverless doesn't have to be complex. Pulumi's infrastructure-as-code (IaC) platform can help remove the complexity and enable beginners to quickly get up to speed with serverless architectures.

        In this workshop, a series of guided exercises will teach you the fundamentals of creating serverless architectures on AWS. You will be introduced to Pulumi, an infrastructure-as-code (IaC) platform, where you can use familiar programming languages to provision modern cloud infrastructure. This workshop is designed to help new users become familiar with the core concepts needed to effectively deploy serverless architectures and workloads on AWS. We will guide you through the Pulumi platform with diagrams and a series of labs to help accelerate your cloud projects.  

    # The webinar presenters
    presenters:
        - name: "Josh Kodroff"
          role: "Sr. Solutions Architect, Pulumi"
        - name: Marina Novikova
          role: Partner Solutions Architect, AWS

    # A bullet point list containing what the user will learn during the webinar.


# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id:
    salesforce_campaign_id:
---