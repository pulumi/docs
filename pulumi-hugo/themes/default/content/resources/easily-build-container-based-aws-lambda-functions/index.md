---
# Name of the video.
title: "Easily build container-based AWS Lambda Functions"
meta_desc: "Watch as Pulumi VP of Engineering, Lee Zen, helps you to get started using Container Image Support in AWS Lambda."

# A featured video will display first in the list.
featured: false

pre_recorded: true
pulumi_tv: true
unlisted: false

# Gated videos will have a registration form and the user will need
# to fill out the form before viewing.
gated: false

# The layout of the landing page.
type: webinars

external: false
block_external_search_index: false

# The url slug for the webinar landing page. If this is an external
# webinar, use the external URL as the value here.
url_slug: "easily-build-container-based-aws-lambda-functions"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Easily build container-based AWS Lambda functions using Pulumi"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Easily build container-based AWS Lambda functions using Pulumi"
    # URL for embedding a URL for ungated videos.
    youtube_url: "https://www.youtube.com/embed/gB9T1aW3gSk"
    # Sortable date. The datetime Hugo will use to sort the videos in date order.
    sortable_date: 2020-12-01T10:00:00-07:00
    # Duration of the video.
    duration: "2 minutes"
    # Description of the video.
    description: |
        With the announcement of Container Image Support in AWS Lambda, the workflow for publishing serverless components is now easier than ever.  Watch as Pulumi VP of Engineering, Lee Zen, helps you to get started using this powerful new feature.

        [Read our blog](/blog/aws-lambda-container-support/) for more information.

    # The video presenters
    presenters:
        - name: Lee Zen
          role: VP of Engineering, Pulumi

# This section contains the transcript for a video. It is optional.
transcript: |
    Pulumi makes it easy to take advantage of AWS Lambda's ability to package serverless functions as container images. In this video, we'll build a video thumbnailer. Let's start with the bucket that we can push videos to. Before, running FFmpeg and Lambda was onerous. Now we can simply package it as part of our container, build it, and push the image to ECR. Pulumi makes it easy with a single line of code. Next, we need to give Lambda the right permissions for this function. We're able to take advantage of the IDE, use automatic completion as well as TypeScript enums.

    Let's finish off our example by creating the Lambda function and referencing the image we just pushed. It's easy to wire up the functions to the S3 bucket notifications in a single line of code. We export the bucket name for use outside of our program.

    Finally, let's augment our example by creating a callback to log information on when we create new thumbnails. That's it. And just a couple of lines of code, we built the thumbnailing service. Let's deploy it. Here, you can see it's building the container image, pushing it as well as creating the various other resources we've defined. While that's deploying, let's take a quick look at our Docker file to see how we're building our image. You can see it's fairly straightforward. Let's also take a quick look at the function handler. We're simply shelling out to FFmpeg and copying the thumbnail to S3. Let's grab a simple clip to try out. Our deployment finished in just a couple of minutes. Let's watch the logs for our stack and try uploading our clip. We can see the logs for the function processing the clip. We can also see the logs for our other function that logs thumbnail creation. Let's copy that thumbnail and take a look. Success. We hope you can see just how simple and easy Pulumi makes it to use container images with AWS Lambda. Our examples are in TypeScript, but Pulumi also supports Python, .NET and Go. Give it a try today.
---
