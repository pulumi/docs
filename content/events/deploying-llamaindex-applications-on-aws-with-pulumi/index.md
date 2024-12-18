---
# Name of the event, <= 60 characters
title: Deploying LlamaIndex Applications on AWS with Pulumi
meta_desc: Dive into a session where we'll deploy an AI application using LlamaIndex on AWS. Discover the seamless integration of IaC in launching AI solutions.
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
url_slug: deploying-llamaindex-applications-on-aws-with-pulumi

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Deploying LlamaIndex Applications on AWS with Pulumi

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url:

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2024-05-08T09:00:00.000-07:00

    # Duration of the webinar.
    duration: 90 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        In this workshop, you will first be introduced to Pulumi, an infrastructure-as-code platform, where you can use familiar programming languages to provision modern cloud infrastructure. Following that introduction, attendees will see how to use Pulumi to deploy an AI application using LlamaIndex onto AWS, providing a practical use case for how infrastructure as code helps streamline deploying AI applications.

    learn:
        - The basics of Pulumi for infrastructure as code
        - The basics of LlamaIndex
        - Create a Chatbot with LlamaIndex for AWS Bedrock and Streamlit UI
        - How to deploy a LlamaIndex application on AWS using Pulumi

    # The webinar presenters
    presenters:
        - name: Engin Diri
          role: Sr. Community Engineer, Pulumi
          photo: /images/team/engin-diri.jpg
        - name: Laurie Voss
          role: VP of Developer Relations, LlamaIndex

    # case-sensitive
    tags:
        level: Beginner # Beginner, Intermediate, Advanced
        topics: ["AI"]
        languages: []
        clouds: ["AWS"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 7d8a05ce-6a0e-4c3c-b8e2-c58f6b22fc85
    salesforce_campaign_id: 701PQ000009SGMPYA4
---
