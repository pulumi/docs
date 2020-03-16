---
# Name of the webinar.
title: "Getting Started with Infrastructure as Code"
meta_desc: "This is a test webinar and not meant to ever reach our actual website."

# If the video is pre-recorded or live.
pre_recorded: false

# The preview image will be shown on the list page.
preview_image: "/logos/brand/pulumipus-8bit.svg"

# Webinars with unlisted as true will not be shown on the webinar list
unlisted: false

# Gated webinars will have a registration form and the user will need
# to fill out the form before viewing.
gated: true

# The layout of the landing page.
type: webinar

# External webinars will link to an external page instead of a webinar
# landing/registration page.
external: false

# The url slug for the webinar landing page. If this is an external
# webinar, use the external URL as the value here.
url_slug: "test-webinar"

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
    # Datetime of the webinar.
    datetime: 2020-03-17 09:00:00 -07:00
    # Description of the webinar.
    description: "Paul Stack and Mikhail Shilkov from Pulumi will show you how to get started mastering your preferred cloud using your favorite languages."

    # The webinar presenters
    presenters:
        - name: Paul Stack
          role: Software Engineer, Pulumi
        - name: Mikhail Shilkov
          role: Software Engineer, Pulumi

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - Cloud programming with your favorite language.

# The right hand side webinar setion.
form:
    # GoToWebinar webinar key. This key allows us to register people for webinars via the
    # HubSpot form.
    gotowebinar_key: "3062303016678699787"

    # HubSpot form id.
    hubspot_form_id: "88fac9d7-6e56-4166-849d-e10a90892962"
---
