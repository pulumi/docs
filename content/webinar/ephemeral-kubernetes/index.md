---
# Name of the webinar.
title: "Ephemeral Kubernetes"
meta_desc: "Pulumi engineer, Mike Metral, walks through workflows around around ephemeral Kubernetes."

# If the video is pre-recorded or live.
pre_recorded: true

# If the video is part of the PulumiTV series. Setting this value to true will list the video in the "PulumiTV" section.
pulumi_tv: true

# The preview image will be shown on the list page.
preview_image: "https://img.youtube.com/vi/2oNolWWRZXQ/hqdefault.jpg"

# Webinars with unlisted as true will not be shown on the webinar list
unlisted: false

# Gated webinars will have a registration form and the user will need
# to fill out the form before viewing.
gated: false

# The layout of the landing page.
type: webinar

# External webinars will link to an external page instead of a webinar
# landing/registration page.
external: false

# The url slug for the webinar landing page. If this is an external
# webinar, use the external URL as the value here.
url_slug: "ephemeral-kubernetes"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Ephemeral Kubernetes"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Ephemeral Kubernetes"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/2oNolWWRZXQ"
    # Datetime of the webinar.
    datetime: 2019-02-05 10:00:00 -07:00
    # Description of the webinar.
    description: |
        Pulumi engineer, Mike Metral, walks through workflows around around ephemeral Kubernetes.

    # The webinar presenters
    presenters:
        - name: Mike Metral
          role: Software Architect & Engineer, Pulumi

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - How to use Pulumi in CI/CD and development to provision, manage, and test Kubernetes clusters and their applications.
---
