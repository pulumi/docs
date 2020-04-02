---
# Name of the webinar.
title: "Getting Started with Infrastructure as Code"
meta_desc: "Join us on March 30th, 2020 for a deep dive into Infrastructure as Code concepts with Pulumi engineers Paul Stack and Mikhail Shilkov."

redirect_to: "/webinars/"

# If the video is pre-recorded or live.
pre_recorded: false

# If the video is part of the PulumiTV series. Setting this value to true will list the video in the "PulumiTV" section.
pulumi_tv: false

# The preview image will be shown on the list page.
preview_image: "/images/webinar/pulumi_workshop.png"

# Webinars with unlisted as true will not be shown on the webinar list
unlisted: true

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
url_slug: "getting-started-infrastructure-as-code-2020-03-30"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Getting Started with Infrastructure as Code"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Getting Started with Infrastructure as Code"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2020-03-30 11:30:00 +01:00
    # Datetime of the webinar.
    datetime: "MON MAR 30, 2020 AT 11:30AM TO 1:30PM CET"
    # Description of the webinar.
    description: |
        In this hands-on workshop, the Pulumi team will show you how to stand up basic services using Infrastructure as Code (IaC) through a series of hands-on labs. The techniques work for any cloud --- Azure, AWS, and GCP. You’ll be able to leverage your favorite languages including Python, Go, JavaScript, TypeScript, and C# instead of YAML or domain-specific languages.

        After completion of this webinar, you’ll be up and running with IaC fundamentals, modern application architectures across many clouds, and best-practices that are ready for production environments. You’ll also be ready to empower your development teams to be more productive --- continuously deploying both their applications and infrastructure.

        View the prerequisites for this workshop [here](https://github.com/pulumi/infrastructure-as-code-workshop/blob/master/00-installing-prerequisites.md).

    # The webinar presenters
    presenters:
        - name: Paul Stack
          role: Software Engineer, Pulumi
        - name: Mikhail Shilkov
          role: Software Engineer, Pulumi

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - This is a 100-level introduction to setting up your infrastructure using Pulumi with multiple languages.
        - Cloud programming with your favorite language.

# The right hand side webinar section.
form:
    # GoToWebinar webinar key. This key allows us to register people for webinars via the
    # HubSpot form.
    gotowebinar_key: "6303810629918386701"

    # HubSpot form id.
    hubspot_form_id: "c5d3d12d-360f-4381-85de-1673b627a362"
---
