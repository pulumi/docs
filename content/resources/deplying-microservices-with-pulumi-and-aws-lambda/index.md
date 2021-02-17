---
# Name of the webinar.
title: "Deploying Microservices with Pulumi and AWS Lambda"
meta_desc: "In this workshop, we’ll examine how Pulumi can accelerate provisioning of cloud infrastructure. We’ll focus on AWS Lambda, and build a set of microservices."

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

# The url slug for the webinar landing page. If this is an external
# webinar, use the external URL as the value here.
url_slug: "deplying-microservices-with-pulumi-and-aws-lambda"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Cloud Engineering Concepts: Deploying Microservices with Pulumi and AWS Lambda"
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
    title: "Cloud Engineering Concepts: Deploying Microservices with Pulumi and AWS Lambda"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/bGZON8dRqVY"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2021-02-17T09:00:00-08:00
    # Duration of the webinar.
    duration: "2 hours"
    # Datetime of the webinar.
    datetime: "February 17th, 2021"
    # Description of the webinar.
    description: |
        In this workshop, we’ll examine how Pulumi can rapidly accelerate provisioning of cloud infrastructure. We’ll focus on AWS Lambda, and build an example set of microservices utilizing AWS’s newest Lambda features.

        Attendees will be guided through the process of provisioning a set of example Lambda resources in AWS and see real time examples of how Pulumi’s innovative programming model helps turbocharge cloud engineering.

        You can view the content of this workshop [here](https://pulumi.awsworkshop.io/40_lambda_microservices_ts.html).

        **Target Audience**

        Active Pulumi users, and users building serverless applications that are familiar with Pulumi

        **Prerequisites**

        Attendees should be familiar with Pulumi and have the Pulumi CLI installed on their machine.
        Attendees should have access to an AWS account, temporary AWS accounts will be provided to users on a first come, first served basis.

    # The webinar presenters
    presenters:
        - name: Lee Briggs
          role: Community Engineer, Pulumi

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - How-to provision a Lambda function in AWS
        - How to provision infrastructure such as DynamoDB & API Gateway to support your microservice applications
        - Learn how to take advantage of some of the newest Lambda features

# form:
#     hubspot_form_id: "67f667cd-2fca-4834-b16a-cf0289009c77"
---
