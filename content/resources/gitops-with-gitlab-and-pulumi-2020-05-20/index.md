---
# Name of the webinar.
title: "GitOps with Pulumi and GitLab"
meta_desc: "Deploy and update your infrastructure the same way you deliver the rest of your application: with real code delivered through your CI/CD pipeline."

aliases:
  - /webinars/gitops-with-gitlab-and-pulumi-2020-05-20

# A featured webinar will display first in the list.
featured: false

# If the video is pre-recorded or live.
pre_recorded: true

# If the video is part of the PulumiTV series. Setting this value to true will list the video in the "PulumiTV" section.
pulumi_tv: false

# The preview image will be shown on the list page.
preview_image: "/images/superpowers/gitlab-demo.png"

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
url_slug: "gitops-with-gitlab-and-pulumi-2020-05-20"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "GitOps with Pulumi and GitLab"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "GitOps with Pulumi and GitLab"
    youtube_url: "https://www.youtube.com/embed/xI9uWFiEzAM"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2020-05-20T12:00:00-07:00
    # Duration of the webinar.
    duration: "45 minutes"
    # Datetime of the webinar.
    datetime: "MON, MAY 20, 2020 12:00 PM PDT"
    # Description of the webinar.
    description: |
        Deploy and update your infrastructure the same way you deliver the rest of your application: with real code delivered through your CI/CD pipeline. Learn how Pulumi’s modern infrastructure as code platform helps your team deliver features faster by helping you to define resources on any cloud using your favorite languages.  Praneet Loke from Pulumi and William Chia from GitLab will show you how to super-charge your team’s velocity with GitOps.

        You will receive follow-up email from Pulumi and GitLab after this tech talk with links to help you get started with GitOps.

    # The webinar presenters
    presenters:
        - name: William Chia
          role: Senior Product Marketing Manager, GitLab
        - name: Praneet Loke
          role: Software Engineer, Pulumi

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - Create a simple infrastructure stack for a static website.
        - Policy enforcement blocking unencrypted S3 buckets.
        - Setting up ‘PR to deploy’ via GitLab CI.
---
