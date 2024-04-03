---
# Name of the event, <= 60 characters
title: Deploying LangChain Applications on AWS with Pulumi
meta_desc: This workshop will show a practical AI use case for Pulumi. Using Pulumi & TypeScript, we'll demonstrate deploying a LangChain/LangServe app on AWS.
meta_image: "/images/resources/deploy-langchain-apps-aws-engin-lance.png"

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
url_slug: deploying-langchain-apps-on-aws-with-pulumi

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Deploying LangChain Applications on AWS with Pulumi

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: 

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2024-04-17T09:00:00-07:00

    # Duration of the webinar.
    duration: 90 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        In this workshop, you will first be introduced to Pulumi, an infrastructure-as-code platform, where you can use familiar programming languages to provision modern cloud infrastructure. Following that introduction, attendees will see how to use Pulumi to deploy an AI application using LangChain/LangServe onto AWS, providing a practical use case for how infrastructure as code helps streamline deploying AI applications.

    learn:
        - The basics of Pulumi for infrastructure as code
        - The basics of LangChain and LangServe
        - How to deploy a LangChain/LangServe application on AWS using Pulumi

    # The webinar presenters
    presenters:
        - name: Engin Diri
          role: Sr. Solutions Architect, Pulumi
          photo: /images/team/engin-diri.jpg
        - name: Lance Martin
          role: Software Engineer, LangChain
          photo: /images/people/lance-martin.jpg

    # case-sensitive
    tags:
        level: Beginner # Beginner, Intermediate, Advanced
        topics: ["AI", "LangChain", "AWS"]
        languages: ["TypeScript"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: 822b8891-28af-4054-a7a8-86f9f1e9148b
    salesforce_campaign_id: 701PQ0000074X9SYAU
---
