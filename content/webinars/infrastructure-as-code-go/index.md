---
# Name of the webinar.
title: "Modern Cloud Infrastructure in Go"
meta_desc: "Pulumi Engineer Evan Boyle uses Go to walk us through modern infrastructure-as-code concepts and best practices like functions, containers, and Kubernetes."

# A featured webinar will display first in the list.
featured: false

# If the video is pre-recorded or live.
pre_recorded: true

# If the video is part of the PulumiTV series. Setting this value to true will list the video in the "PulumiTV" section.
pulumi_tv: false

# The preview image will be shown on the list page.
preview_image: "/images/superpowers/go-demo.png"

# Webinars with unlisted as true will not be shown on the webinar list
unlisted: false

# Gated webinars will have a registration form and the user will need
# to fill out the form before viewing.
gated: false

# The layout of the landing page.
type: webinars

# External webinars will link to an external page instead of a webinar
# landing/registration page.
external: false

# The url slug for the webinar landing page. If this is an external
# webinar, use the external URL as the value here.
url_slug: "infrastructure-as-code-go"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Modern Cloud Infrastructure in Go"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Modern Cloud Infrastructure in Go"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/s91qF5MLy14"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2020-04-14T18:00:00.000-07:00
    # Duration of the webinar.
    duration: "39 minutes"
    # Datetime of the webinar.
    datetime: "TUE, APR 14, 2020 AT 6:00PM PDT"
    # Description of the webinar.
    description: >
        Declaratively defining, deploying, and managing infrastructure usually means breaking out of your day to day toolchain and using YAML or some sort of DSL. Learn how to automate modern infrastructure like functions, containers, and Kubernetes using Pulumi and Go. In this talk we'll explore the productivity superpowers that Pulumi brings to infrastructure:

        1. Provisioning - We'll author a serverless application on AWS, exploring Pulumi's familiar imperative approach using Go that still enables declarative state and change management.

        2. Testing - Pulumi's unique approach opens up a lot of options with unit and integration testing and gives you the confidence to move quickly.

        3. Architecture - Programming languages are naturally suited to encapsulation and abstraction. This enables us to represent our architecture in reusable components that can be published and shared across teams and organizations.

    # The webinar presenters
    presenters:
        - name: Evan Boyle
          role: Staff Software Engineer, Pulumi

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - How to provision cloud infrastructure in Go.
        - How to test cloud infrastructure.
---
