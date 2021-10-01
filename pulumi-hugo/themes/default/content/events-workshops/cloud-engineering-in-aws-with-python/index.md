---
# Name of the webinar.
title: "Pulumi in Practice: Cloud Engineering in AWS with Python"
meta_desc: "In this workshop, we’ll teach you how to provision infrastructure on AWS. You will how to use Pulumi through a series of hands-on exercises using Python."

# A featured webinar will display first in the list.
featured: false

# If the video is pre-recorded or live.
pre_recorded: false

# If the video is part of the PulumiTV series. Setting this value to true will list the video in the "PulumiTV" section.
pulumi_tv: false

# The preview image will be shown on the list page.
preview_image: ""

# Webinars with unlisted as true will not be shown on the webinar list
unlisted: true

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
url_slug: "cloud-engineering-in-aws-with-python"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Pulumi in Practice: Cloud Engineering in AWS with Python"
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
    title: "Pulumi in Practice: Cloud Engineering in AWS with Python"
    # URL for embedding a URL for ungated webinars.
    youtube_url: ""
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2020-11-19T11:00:00-08:00
    # Duration of the webinar.
    duration: "2 hours"
    # Datetime of the webinar.
    datetime: ""
    # Description of the webinar.
    description: |
        In this workshop, we’ll examine how Pulumi can rapidly accelerate provisioning of cloud infrastructure. We’ll examine some important Pulumi concepts, and show how Pulumi’s unique programming model can super-charge your cloud engineering efforts.

        Attendees will be guided through the process of provisioning cloud resources in AWS and see real time examples of how Pulumi’s innovative programming model helps turbocharge cloud engineering.

        **Target Audience**

        People just getting started with Pulumi, who are familiar with Pulumi basics and have followed the getting started information.

        **Prerequisites**

        Attendees should be familiar with Pulumi and have the Pulumi CLI installed on their machine.
        Attendees should have access to an AWS account, temporary AWS accounts will be provided to users on a first come, first served basis.


    # The webinar presenters
    presenters:
        - name: Lee Briggs
          role: Community Engineer, Pulumi
        - name: Yaniv Bossem
          role: Partner Solutions Architect, DevOps at Amazon Web Services (AWS)

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - How to provision AWS resources with Pulumi
        - Understanding Pulumi’s auto-naming
        - Understanding a Pulumi cloud resource
        - Setting required AWS config values
        - The Pulumi programming model
        - Pulumi Inputs, Outputs
        - Declarative vs Imperative
        - An introduction to Apply
        - Grouping Pulumi resources with ComponentResources
        - Importing existing AWS resources

# The right hand side form section.
form:
    # GoToWebinar webinar key. This key allows us to register people for webinars via the
    # HubSpot form.
    gotowebinar_key: ""

    # HubSpot form id.
    hubspot_form_id: "a1b63037-fb1e-437c-99ad-f578394b4c2c"
aliases:
  - /resources/cloud-engineering-in-aws-with-python
---
