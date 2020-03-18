---
# Name of the webinar.
title: "Introduction to Crosswalk for AWS"
meta_desc: "Meet the team behind Pulumi Crosswalk for AWS, see some of what it can do across AWS ECS, EKS, Lambda, and other AWS workloads."

# If the video is pre-recorded or live.
pre_recorded: true

# If the video is part of the PulumiTV series. Setting this value to true will list the video in the "PulumiTV" section.
pulumi_tv: true

# The preview image will be shown on the list page.
preview_image: "https://img.youtube.com/vi/PQNfLqUHu64/hqdefault.jpg"

# Webinars with unlisted as true will not be shown on the webinar list
unlisted: true

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
url_slug: "intro-to-aws-crosswalk"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Introduction to Crosswalk for AWS"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Introduction to Crosswalk for AWS"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/PQNfLqUHu64"
    # Datetime of the webinar.
    datetime: 2019-02-05 10:00:00 -07:00
    # Description of the webinar.
    description: |
        Meet the team behind Pulumi Crosswalk for AWS, see some of what it can do across AWS ECS, EKS, Lambda, and other AWS workloads, and hear from partners Tableau and AWS on how they are using EKS to get Kubernetes running in AWS.

    # The webinar presenters
    presenters:
        - name: Joe Duffy
          role: Founder & CEO, Pulumi
        - name: Luke Hoban
          role: CTO, Pulumi
        - name: Mike Metral
          role: Software Architect & Engineer, Pulumi
        - name: Cyrus Najmabadi
          role: Software Engineer, Pulumi

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - How to provision cloud services that are **Well-Architected** by default.
        - Common best practices for production ready infrastructure.
---
