---
# Name of the webinar.
title: "Introduction to CrossGuard: Infrastructure Policy as Code"
meta_desc: "Pulumi CrossGuard lets you enforce infrastructure policies at deployment, preventing security, cost, or best practices mistakes from making it to production."

# If the video is pre-recorded or live.
pre_recorded: true

# If the video is part of the PulumiTV series. Setting this value to true will list the video in the "PulumiTV" section.
pulumi_tv: true

# The preview image will be shown on the list page.
preview_image: "https://img.youtube.com/vi/-xJT_lON254/hqdefault.jpg"

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
url_slug: "intro-to-policy-as-code"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Introduction to CrossGuard: Infrastructure Policy as Code"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Introduction to CrossGuard: Infrastructure Policy as Code"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/-xJT_lON254"
    # Datetime of the webinar.
    datetime: 2019-02-05 10:00:00 -07:00
    # Description of the webinar.
    description: |
        Pulumi CrossGuard is a product that provides gated deployments via Policy as Code.

        Often organizations want to empower developers to manage their infrastructure yet are concerned about giving them full access. CrossGuard allows administrators to provide autonomy to their developers while ensuring compliance to defined organization policies.

        Using Policy as Code, users can express business or security rules as functions that are executed against resources in their stacks. Then using CrossGuard, organization administrators can apply these rules to particular stacks within their organization. When policies are executed as part of your Pulumi deployments, any violation will gate or block that update from proceeding.

    # The webinar presenters
    presenters:
        - name: Cameron Stokes
          role: Customer Engineer, Pulumi

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - How to express business or security rules as functions.
        - Execute policies against Pulumi deployments.
---
