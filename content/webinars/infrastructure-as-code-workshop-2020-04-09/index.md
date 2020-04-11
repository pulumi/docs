---
# Name of the webinar.
title: "Infrastructure as Code Workshop"
meta_desc: "In this workshop, Luke Hoban shows you the easy way to start using Infrastructure as Code through hands-on labs."

# A featured webinar will display first in the list.
featured: false

aliases: [ "/events/workshop-san-francisco-2020-04-09" ]

# If the video is pre-recorded or live.
pre_recorded: false

# If the video is part of the PulumiTV series. Setting this value to true will list the video in the "PulumiTV" section.
pulumi_tv: false

# The preview image will be shown on the list page.
preview_image: "/images/webinar/pulumi_workshop.jpg"

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
url_slug: "infrastructure-as-code-workshop-2020-04-09"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Infrastructure as Code Workshop"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Infrastructure as Code Workshop"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2020-04-09T17:30:00.000-07:00
    # Duration of the webinar.
    duration: "90 minutes"
    # Datetime of the webinar.
    datetime: "THU APR 09, 2020 AT 5:30PM PDT"
    # Description of the webinar.
    description: |
        In this hands-on workshop, the Pulumi team will show you how to stand up basic services using Infrastructure as Code (IaC) through a series of hands-on labs. The techniques work for any cloud --- Azure, AWS, and GCP. You’ll be able to leverage your favorite languages including Python, Go, JavaScript, TypeScript, and C# instead of YAML or domain-specific languages.

        After completion of this webinar, you’ll be up and running with IaC fundamentals, modern application architectures across many clouds, and best-practices that are ready for production environments. You’ll also be ready to empower your development teams to be more productive --- continuously deploying both their applications and infrastructure.

        View the prerequisites for this workshop [here](https://github.com/pulumi/infrastructure-as-code-workshop/blob/master/00-installing-prerequisites.md).

    # The webinar presenters
    presenters:
        - name: Luke Hoban
          role: CTO, Pulumi

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - Infrastructure as Code fundamentals.
        - Multi cloud architectures for moder applications.
        - Kubernetes best practices for production environments.

# The right hand side form section.
form:
    # GoToWebinar webinar key. This key allows us to register people for webinars via the
    # HubSpot form.
    gotowebinar_key: "9011624095200528652"

    # HubSpot form id.
    hubspot_form_id: "193a2f1e-faf3-48e7-8cd4-536a5d2502fc"
---
