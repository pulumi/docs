---
# Name of the webinar.
title: "Azure Infrastructure as Code Workshop"
meta_desc: "In this workshop, Paul Stack and Mikhail Shilkov show you how to tackle common challenges using Infrastructure as Code through a series of hands-on labs."

aliases:
  - /webinars/azure-infrastructure-as-code-workshop-2020-07-23

# A featured webinar will display first in the list.
featured: false

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
url_slug: "azure-infrastructure-as-code-workshop-2020-07-23"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Azure Infrastructure as Code Workshop"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Azure Infrastructure as Code Workshop"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2020-07-23T13:00:00+02:00
    # Duration of the webinar.
    duration: "2 hours"
    # Datetime of the webinar.
    datetime: "THU, JUL 23, 2020 1:00 PM CEST"
    # Description of the webinar.
    description: |
        The hardest part of Kubernetes is setting up the infrastructure: clusters, DNS, firewalls, load balancers, IAM, storage, logging, and performance monitoring, often spanning private, public, and hybrid cloud architectures.

        In this workshop, Paul Stack and Mikhail Shilkov show you how to tackle these challenges using [Infrastructure as Code](/what-is/what-is-infrastructure-as-code/) (IaC) through a series of hands-on labs. The techniques work for any cloud --- Azure, AWS, and GCP. You'll be able to leverage your favorite languages including Python, Go, JavaScript, TypeScript, and C# instead of YAML or domain-specific languages.

        After completing this workshop, you'll be up and running with IaC fundamentals, modern application architectures across many clouds, and Kubernetes best-practices that are ready for production environments. You'll also be ready to empower your development teams to be more productive --- continuously deploying both their applications and infrastructure.

    # The webinar presenters
    presenters:
        - name: Paul Stack
          role: Software Engineer, Pulumi
        - name: Mikhail Shilkov
          role: Software Engineer, Pulumi

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - Infrastructure as Code fundamentals.
        - Multi cloud architectures for modern applications.
        - Kubernetes best practices for production environments.

# The right hand side form section.
form:
    # GoToWebinar webinar key. This key allows us to register people for webinars via the
    # HubSpot form.
    gotowebinar_key: "3662436256630415375"

    # HubSpot form id.
    hubspot_form_id: "c7be4777-591c-4a43-ae76-c1e31077d5a7"
---
