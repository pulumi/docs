---
# Name of the event, <= 60 characters
title: "Day 2 Operations: Drift Detection and Remediation"
meta_desc: Automate infrastructure drift detection and remediation to maintain reliable self-service platforms over time.
meta_image:

# A featured webinar will display first in the list.
featured: false

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

# The url slug for the webinar landing page. If this is an external
# webinar, use the external URL as the value here.
url_slug: day-2-operations

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Day 2 Operations: Drift Detection and Remediation"
    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: 

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2025-08-20T12:00:00-04:00

    # Duration of the webinar.
    duration: 60 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        Building an IDP is just the beginning—maintaining it reliably requires robust Day 2 operations. This workshop focuses on the operational aspects that keep your platform running smoothly: detecting infrastructure drift, automating remediation, and providing visibility into platform health. You'll learn to catch issues before they impact developers, ensuring your IDP remains a trusted foundation for your organization's infrastructure.
    learn:
        - How to implement automated drift detection for platform infrastructure
        - Strategies for graceful drift remediation that minimizes developer disruption

    # The webinar presenters
    presenters:
        - name: Mitch Gerdisch
          role: Principal Solutions Architect, Pulumi
          photo: /images/team/mitch-gerdisch.jpg
        - name: Josh Kodroff
          role: Principal Solutions Architect, Pulumi
          photo: /images/team/josh-kodroff.jpg

    # case-sensitive
    tags:
        level: Intermediate # Beginner, Intermediate, Advanced
        topics:  ["Platfotm Engineering", "Monitoring", "Drift Detection"]
        languages: ["TypeScript"]
        clouds: ["AWS"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: a453e844-61b0-4bd0-acea-51459d5216cf
    salesforce_campaign_id: 701PQ00000ZYTY6YAP

event_data:
  name: "Day 2 Operations: Drift Detection and Remediation"
  start_date: 2025-08-20T12:00:00-04:00
  end_date: 2025-08-20T13:00:00-04:00
  url: "https://www.pulumi.com/resources/day-2-operations/"
  description: |
    Building an IDP is just the beginning—maintaining it reliably requires robust Day 2 operations. This workshop focuses on the operational aspects that keep your platform running smoothly: detecting infrastructure drift, automating remediation, and providing visibility into platform health. You'll learn to catch issues before they impact developers, ensuring your IDP remains a trusted foundation for your organization's infrastructure.
--- 