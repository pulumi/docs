---
# Name of the video.
title: "Introducing AWS App Runner"
meta_desc: "Learn how to get started using AWS App Runner with Pulumi to quickly deploy containerized web applications and APIs, at scale."

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

# The url slug for the video landing page. If this is an external
# video, use the external URL as the value here.
url_slug: "introducing-aws-app-runner"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Introducing AWS App Runner"

# Content for the left hand side section of the page.
main:
    # Video title.
    title: "Introducing AWS App Runner"
    # URL for embedding a URL for ungated videos.
    youtube_url: "https://www.youtube.com/embed/XdMynboheiA"
    # Sortable date. The datetime Hugo will use to sort the videos in date order.
    sortable_date: 2021-05-18T10:00:00-07:00
    # Duration of the video.
    duration: "3 minutes"
    # Description of the video.
    description: |
        Learn how to get started using AWS App Runner with Pulumi.

        AWS App Runner is a fully managed service that makes it easy for developers to quickly deploy containerized web applications and APIs, at scale.

        With Pulumi you can use your favorite programming language to define, deploy and manage resources on any cloud.

    # The video presenters
    presenters:
        - name: Lee Zen
          role: VP of Engineering, Pulumi

# This section contains the transcript for a video. It is optional.
transcript: |
    Hello, welcome to another episode of Modern Infrastructure Wednesday, I am your host, Lee Zen, and today we're going to be covering how easy it is to use Pulumi to deploy an application using AWS App Runner. App Runner is a new service from Amazon that lets you deploy a container image or a source code repository as an application without having to do too much around configuring anything. You don't have to configure load balancers. You don't have to configure any of that stuff you would typically have to configure. So here you can see I'm running the main.go file. It's going to create all the necessary resources along with finally the App Runner service. And we're going to go into all the source code to explain how all this works, but right now you can see what is happening is we're actually doing the Docker build that's going to publish. We're doing the Docker build and then that after the Docker build completes, it's pushing the image into our ECR repository. And then finally you can see here the update succeeds, and then we actually get the service URL. And so now let's go take a look at our service and while the service is updating, you can see that it takes a little bit of time not too much, but just a little bit of time to get going here. We're going to see how our code actually works.

    All right. So what's actually happening here? Let's look at our deployment.go file which main.go actually calls. So we actually built an Automation API based program and you can see, you know, in the outputs we create this image, we create, you know, these various things, so let's look at the code. So the first thing we do is we create an ECR repository and here we use auto naming, so it just creates the name. And then next we create a role so that App Runner can actually go ahead and pull the image from our repository. And so we create the role, we give it the correct policy. And then after that, we basically publish our image. You can see here, we have the image resource, and there we actually just feed it the repository credentials. So let's take a quick look at the Dockerfile of the thing we're building. It's just copying that index.html file over. It's a very simple file. So that's really all there is to the infrastructure. It's super simple. So if we look at the Automation API side of things, all we're doing is doing the usual Automation API stuff. We're setting up a stack we're deploying our program and after we pointed out the part where we're deploying the program right up here and as soon as we are complete as soon as we finished deploying the program we're going to use the outputs of that program. So namely the image URL and the access rule, and we'll feed that to App Runner. And that'll, we'll basically invoke the create service API call here, and that's actually what's going to do the work. So let's go back to the console and you can see here, we have the app running and voila exactly what we expect to see. So hopefully you enjoyed this demo and really, yeah, like I said, just so easy to get everything running with App Runner and just a few simple lines of code in Pulumi, thanks for watching and have a great day.
---
