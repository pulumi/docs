---
# Name of the event, <= 60 characters
title: Security Automation—Faster. Cheaper. Better.
meta_desc: Join us for an insightful fireside chat, with by Joe Duffy, co-founder/CEO of Pulumi, featuring David Giambruno, VP of Engineering and DevOps at Tivity Health.
meta_image:

# A featured webinar will display first in the list.
featured: false

# Webinars with unlisted as true will not be shown on the webinar list
unlisted: false

# Gated webinars will have a registration form and the user will need
# to fill out the form before viewing.
gated: false

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
url_slug: security-automation-faster-cheaper-better

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Security Automation—Faster. Cheaper. Better.

    event_type: event # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: https://www.youtube.com/embed/35vAiKdDux4

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2024-09-18T09:00:00-00:00

    # Duration of the webinar.
    duration: 30 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        Join us for an insightful fireside chat, "Security Automation—Faster. Cheaper. Better." Moderated by Joe Duffy, co-founder and CEO of Pulumi, and featuring David Giambruno, VP of Engineering and DevOps at Tivity Health.

        In this session, David G. shared his expertise on how DevOps and DevSecOps teams are automating security processes to achieve higher quality and scalability. Learn how these efforts drive tangible business outcomes, accelerating development speed while creating a competitive edge.

        [Explore the intersection of security automation and business impact](https://www.pulumi.com/blog/devsecops-strategy-security-automation-tivity-health/) with an industry leader who's driving real-world results.

    # The webinar presenters
    presenters:
        - name: Joe Duffy
          role: CEO, Pulumi
          photo: /images/team/joe-duffy.jpg
        - name: David Giambruno
          role: VP Engineering and DevOps, Tivity Health
          photo: /images/people/david-giambruno.jpg

    # case-sensitive
    tags:
        level: # Beginner, Intermediate, Advanced
        topics: ["Automation", "DevOps", "DevSecOps", "Security", "GitOps"]
        languages: []

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id:
    salesforce_campaign_id:
---
