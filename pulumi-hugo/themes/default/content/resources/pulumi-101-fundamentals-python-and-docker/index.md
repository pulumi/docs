---
# Name of the webinar.
title: "Pulumi 101: Fundamentals with Python and Docker"
meta_desc: "Learn the basics of Pulumi from projects to components. We’ll use Python and Docker to build, configure, and deploy a real-life, modern application."

# A featured webinar will display first in the list.
featured: false

# If the video is pre-recorded or live.
pre_recorded: false

# If the video is part of the PulumiTV series. Setting this value to true will list the video in the "PulumiTV" section.
pulumi_tv: false

# The preview image will be shown on the list page.
preview_image: ""

# Webinars with unlisted as true will not be shown on the webinar list
unlisted: false

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

# data for Google Events
event_data:
  name: "Pulumi 101: Fundamentals with Python and Docker"
  start_date: 2022-10-20T10:00:00.000-07:00
  end_date: 2022-10-20T11:00:00.000-07:00
  url: "https://www.pulumi.com/resources/pulumi-101-fundamentals-python-and-docker/"
  description: |
    Learn the basics of Pulumi from projects to components. We’ll use Python and Docker to build, configure, and deploy a real-life, modern application with related infrastructure: a system that runs the fictitious Pulumipus Boba Tea Shop. Along the way, we’ll learn how infrastructure as code makes updates easier, reduces time to value, and helps you keep your cloud costs down.

    If you want to code along, you’ll need a free Pulumi SaaS account, the Pulumi CLI, Python 3.9.x, and Docker installed and running on your machine.

# The url slug for the webinar landing page. If this is an external
# webinar, use the external URL as the value here.
url_slug: "pulumi-101-fundamentals-python-and-docker"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Pulumi 101: Fundamentals with Python and Docker"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Webinar pages support multiple session via the 'multiple' property.
# multiple:

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Pulumi 101: Fundamentals with Python and Docker"
    # URL for embedding a URL for ungated webinars.
    youtube_url: # "https://www.youtube.com/embed/Ap0aLb-RQSc"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2022-10-20T10:00:00.000-07:00
    # Duration of the webinar.
    duration: "60 minutes"
    # Datetime of the webinar.
    datetime: "9/12/2022 10:00am - 11:00am PT"
    # Description of the webinar.
    description: | 
      Learn the basics of Pulumi from projects to components. We’ll use Python and Docker to build, configure, and deploy a real-life, modern application with related infrastructure: a system that runs the fictitious Pulumipus Boba Tea Shop. Along the way, we’ll learn how infrastructure as code makes updates easier, reduces time to value, and helps you keep your cloud costs down.

      If you want to code along, you’ll need a [free Pulumi SaaS account](https://app.pulumi.com/signup/), [the Pulumi CLI](https://www.pulumi.com/docs/get-started/install/), [Python 3.9.x](https://www.pulumi.com/docs/intro/languages/python/), and [Docker](https://docs.docker.com/get-docker/) installed and running on your machine.

    # The webinar presenters
    presenters:
        - name: "Laura Santamaria"
          role: "Developer Advocate, Pulumi"

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - "The basics of the Pulumi Programming Model"
        - "The process to provision, update, and destroy resources with Pulumi"

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: "e3cb6f4c-d0db-486d-b22e-8f90af5a1938"
---
