---
# Name of the event, <= 60 characters
title: Build an ETL pipeline with Amazon Redshift and AWS Glue
meta_desc: Learn how to combine AWS Glue and Amazon Redshift to build a fully-automated ETL pipeline with Pulumi. We'll use three components to complete our example.
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
url_slug: build-etl-pipeline-amazon-redshift-aws-glue-modern-infrastructure

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Build an ETL pipeline with Amazon Redshift and AWS Glue

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: https://www.youtube.com/embed/cbAzk9ovR9s?rel=0

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2023-02-01T20:40:52Z

    # Duration of the webinar.
    duration: 18 minutes
    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        Learn how to combine AWS Glue and Amazon Redshift to build a fully-automated ETL pipeline with Pulumi. We'll use three components to complete our ETL pipeline-to-be: 
        
        ▪️ A Glue crawler. The crawler is responsible for fetching data from some external source (for us, an S3 bucket) and importing it into a Glue catalog.
        
        ▪️ A Glue job. The job is responsible for running an ETL script (e.g., on a schedule) to process the data imported by the crawler into the catalog.
        
        ▪️ A Glue script. The script is where the ETL magic happens. Ours will be written in Python and be responsible for extracting data from the catalog, applying some slight transformations, and loading the transformed data into Redshift.
        
        ► [Get the code](https://www.pulumi.com/blog/redshift-etl-with-pulumi-and-aws-glue/) to follow along 
        
        ✅ [Get Started with Pulumi](https://pulumip.us/Get-Started)

        The first in a series of videos, we'll use a fictional company named Zephyr to explore common questions that users ask when working with Pulumi. Zephyr wants to increase development velocity and flexibly scale different aspects of its online store. The demo will show deploying Zephyr's application, their online store.

    learn:

    # The webinar presenters
    presenters:
        - name: Aaron Kao
          role: VP Marketing, Pulumi
          photo: /images/team/aaron-kao.jpg

    # case-sensitive
    tags:
        level: Beginner # Beginner, Intermediate, Advanced
        topics: ["AWS Glue"]
        languages: ["Python"]
        clouds: ["AWS"]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id:
    salesforce_campaign_id:
---
