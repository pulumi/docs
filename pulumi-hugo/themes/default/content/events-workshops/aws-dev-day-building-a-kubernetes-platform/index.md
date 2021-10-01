---
# Name of the webinar.
title: "AWS DevDay: Building a Kubernetes Platform in Amazon EKS"
meta_desc: "In this dev day workshop, you will examine how Pulumi interacts with Kubernetes, and build real-world examples of managing Amazon EKS clusters."

aws_dev_day: true

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
url_slug: "aws-dev-day-building-a-kubernetes-platform"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "AWS DevDay: Building a Kubernetes platform in Amazon EKS with Pulumi"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "AWS DevDay: Building a Kubernetes platform in Amazon EKS with Pulumi"
    youtube_url: "https://www.youtube.com/embed/1GU4D-nvtXU"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2021-05-04T09:00:00-07:00
    # Duration of the webinar.
    duration: "2 hours"
    # Datetime of the webinar.
    datetime: ""
    # Description of the webinar.
    description: |

        In this workshop, we’ll examine how Pulumi works with Kubernetes, and show real-world examples of managing Amazon EKS clusters.

        We'll guide you through your first deployment to Kubernetes with Pulumi, before showing you the power of Pulumi's reusable components to turbo-charge your platform deployment.

        Finally, we’ll examine Pulumi’s automation API and leverage it’s powerful capabilities to expose your application deployment platform into your users' hands without asking them to write a single line of code!

        **Target Audience**

        Active Pulumi users, and users considering or actively building a Kubernetes platform

        **Prerequisites**

        Attendees should be familiar with Pulumi and have the Pulumi CLI installed on their machine.
        Attendees should have access to an AWS account, temporary AWS accounts will be provided to users on a first come, first served basis.

    # The webinar presenters
    presenters:
        - name: Lee Briggs
          role: Community Engineer, Pulumi

        - name: Andrew Park
          role: Partner Solutions Architect, AWS

        - name: Mansi Vaghela
          role: Solutions Architect, AWS

        - name: Marina Novikova
          role: Partner Solutions Architect, AWS

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - How-to provision a production-ready Amazon EKS cluster with key features enabled using Pulumi
        - Provisioning the aws-load-balancer-controller to automate ingress creation
        - Install an example application to show the end-to-end user experience for users.
form:
    hubspot_form_id: "cdce51df-e0de-4192-9d81-80b0be726129"
aliases:
  - /resources/aws-dev-day-building-a-kubernetes-platform
---
