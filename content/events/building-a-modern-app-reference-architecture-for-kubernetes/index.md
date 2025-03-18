---
# Name of the webinar.
title: "Building a Modern App Reference Architecture for Kubernetes"
meta_desc: In this talk, we will discuss the NGINX MARA project; a turnkey modern application reference architecture.

cloud_engineering_summit:
    track: keynote

# A featured webinar will display first in the list.
featured: false

# If the video is pre-recorded or live.
pre_recorded: true

# If the video is part of the PulumiTV series. Setting this value to true will list the video in the "PulumiTV" section.
pulumi_tv: false

# Webinars with unlisted as true will not be shown on the webinar list
unlisted: false

# Gated webinars will have a registration form and the user will need
# to fill out the form before viewing.
gated: false

# The layout of the landing page.
type: webinars
layout: cloud-engineering-summit-replay

# External webinars will link to an external page instead of a webinar
# landing/registration page. If the webinar is external you will need
# set the 'block_external_search_index' flag to true so Google does not index
# the webinar page created.
external: false
block_external_search_index: false

# The url slug for the webinar landing page. If this is an external
# webinar, use the external URL as the value here.
url_slug: "building-a-modern-app-reference-architecture-for-kubernetes"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Building a Modern App Reference Architecture for Kubernetes"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Building a Modern App Reference Architecture for Kubernetes"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/4FGQS1Cwa1E"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2021-10-20T10:00:00-07:00
    # Duration of the webinar.
    duration: "10 minutes"
    # Description of the webinar.
    description: |
        In this talk, we will discuss the NGINX MARA project; a turnkey modern application reference architecture. With the help of Pulumi, this project can take you from an empty AWS account to a fully deployed modern infrastructure deployment in under an hour.

    # The webinar presenters
    presenters:
        - name: Damian Curry
          role: Community and Alliances Technical Director, NGINX
        - name: Elijah Zupancic
          role: Solutions Architect - Community and Alliances, NGINX

# This section contains the transcript for a video. It is optional.
transcript: |
    Good morning, everyone, and thank you for joining us today.  My name is Damian Curry.  I'm the Community and Alliances Technical Director here at NGINX.  And today we're gonna talk about building a modern application reference architecture for Kubernetes.  So like many projects, we kinda gotta go back to the beginning and talk about where this all start? So this really all came about with everybody asking what is a Modern Application? You know, you hear a lot of things.

    It must be a microservice.  It must be containerized.  It must be cloud native and, you know.  It obviously can't be a monolith, or it can't run on baremetal.  Those are, you know, legacy ways of doing of things.

    But, really, that's always not necessarily the case.  You can operate a monolithic-based architecture or even a baremetal-based architecture in a modern way.  And, really, the more we thought about it, the more we came up with the outcomes are more important than the pieces.  So, really, we're looking at what does a modern application architecture provide? And the main four points we've come down to are portability, scalability, resiliency, and agility.  So with all of these different pieces, that's what you're looking to get with your architecture.

    So you're able to, you know, run your infrastructure wherever it makes the most sense, whether it's in a cloud, multi-cloud, in a data center, or all of the above, you know.  With that, it also when's to use scalability.  When you have that portability to run on all those devices, it's much easier to scale out because we're no longer looking at having to build out data centers and scale out in that manner.  Now you can simply move into different geographical locations based on where your users are.  Resiliency, that's all leads into resiliency.

    The more sites you have, the more resilient your site is gonna be.  And, of course, agility.  None of these is possible without that CI/CD pipeline to make quick updates and move through everything.  So the more we talked about this internally, the more we figured that, you know, people needed a diagram to look at.  So we ended up putting together a diagram that has gone through many iterations like everything else, and we kinda end up here.

    We're kinda just wanting to touch on the core pieces of what it means to have a modern application.  And in my mind, one of the core pieces of that is, you know, that everything runs as code.  So that's why when we're looking at this, it's not just the development team that is pushing code into the code repos in CI/CD pipelines.  It's also your DevOps team, your platform ops team, your SecOps team.  One of the core things to being able to run this modern architecture is having everything defined as code.

    So when you can define your Infrastructure as Code, that provides you to be able to more easily have that resiliency, have that portability, and also, you know, have that agility because it's all based in code.  It also frees you up to have a more accurate representation of your production environment throughout the non-production stages and lifecycles of your application.  So at the end of the day, that provides you more resiliency because you're able to better test your code and how it's actually gonna run in production.  So, you know, now we kinda got the easy parts done, right? We came up with a definition.  We made a pretty diagram that people liked.

    But then we figured, you know, we need to actually show this.  How can we actually build this sort of modern application reference architecture in a way that's actually usable for people? So this, you know, kinda comes down to the key point of our talk today, and it's what are we trying to build? The main thing we're trying to build is an easily deployable Kubernetes-based architecture that isn't just a toy.  This thing should be able to be easily stood up with hopefully people with very little Kubernetes expertise, and it will actually stand up something that is built in a production-ready mindset.  It's also gonna provide us a platform to highlight F5 and partner products as well as, you know, providing easy-push button deployment for our Ingress Controller.  And one of the things that's very, very important to our team that are working on this is to provide stealable examples of how things are done in production.

    That's one of the many reasons why we built this around Pulumi, and we really love the project.  It allows us to have these different components of the architecture defined separately.  So you can run just the pieces that you need or everything.  Again, we wanted to, you know, illustrate those modern design principles and also, you know, build a community-driven project that gives back to the community with this pluggable deployment framework.  And, again, going back to the stealable code, we hope that, you know, somebody will be able to help kickstart their journey down the microservices or Kubernetes road by looking at this and hopefully cutting out some of the big hurdles to get started.

    So I mean that's a lot.  It's a very advantageous project we started down here.  And so this is kinda what we have today.  We're developing this completely in the open.  It's on GitHub.

    It's all out there.  We want people to look at the code, play with it, mess with it, you know, give us insight back, what we're doing right, what we're doing wrong.  We have Infrastructure as Code using Pulumi and Python because we're kinda focusing this at the platform, DevOps, SRE sort of space.  The Python's a very commonly known language and makes getting started and modifying it pretty easy.  We either have the option of building the NGINX Plus Ingress Controller container image manually or pulling it from our primary repositories.

    Or in the case that you don't have or don't want to use an open Plus license, you can also just leverage our open-source option that gets pulled from dockerhub.  We're currently deploying Kubernetes via AWS EKS.  We're using log management tools from Elastic, so we're running the ELK Stack.  We have TLS enabled via Cert Manager.  And the demo application that we are running is what we are calling Bank of Sirius.

    So it is a fork of the Google Bank of Anthos app that we are leveraging to use as an example microservice.  So here's kinda the breakdown.  You can see the different pieces that we're running and how everything goes through the process being deployed by Pulumi.  So, first, we stand up a VPC, you know, basic AWS stuff, you know, get everything that's the baseline and prereqs for an EKS cluster.  And we go ahead and turn on EKS, configure an ECR repo so we have somewhere to store our images.

    Then we have the image build process.  So this could either be the build process or just the pull process.  We were then pushing that image into the ECR repository.  Now, that's gonna happen whether we build the image or not just for best practices of pulling it locally in the future.  Then we use helm to deploy the Ingress Controller on the EKS cluster.

    Then the logstore gets deployed so that the Elastic ELK Stack infrastructure is in place on the EKS cluster, followed by the actual logging agent being deployed that will then collect those logs and send them to the ELK Stack.  Next, we're gonna deploy the cert manager.  That will go ahead and allow us to have TLS certs enabled with currently being provided by Let's Encrypt.  And then finally, we're deploying the Bank of Sirius that we call it, which is the fork of Google's Bank of Anthos application that we are taking and modifying and, you know, turning it into something and using it as a way to leverage some of the different functionality that you can do with using logic in the Ingress Controller rather than the application tier.  So that's where we're at today.

    This is still definitely a new project where we're not even to what we would like to call V1, but we're getting very close.  So some of the next big hurdles we wanna get done before we push to V1 is gonna be, you know, getting that observability end to end tied up using Open Telemetry and Prometheus and Grafana.  So it is a very interesting project that we are on now.  The Open Telemetry stuff is an awesome tool, but, you know, it takes some work to stitch that together.  So we're hoping that this will lead to some good content for not just the sort of environment but just using Open Telemetry in general.

    Also, we plan to add some more intelligent CD examples.  We're currently looking at Argo to run the CD pipeline.  We're also building in a performance testing framework so that we are able to easily check and see performance impacts and benefits from different changes that we make in the cluster and also just to give a really good baseline Kubernetes performance, repeatable performance testing framework.  And then the last thing we're working on, we're still kinda up in the air whether it's gonna be in 1. 0 or not, is breaking up some of the functionalities so that we have an application cluster and an admin cluster to more mimic what you would see in a production-level environment.

    Just to, you know, get those different utilities separated so that they're not stepping on each other's toes and so that you can adjust the different parameters for resources and things like that, how you see fit and what's necessary in your environment.  So I know that was a ton of information.  We've got way more to talk about.  If you'd like to hear more, please join us at our office hours.  They're gonna be starting right after this, and, yeah, hopefully we will see you there.
---
