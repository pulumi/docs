---
# Name of the webinar.
title: "Building Arm Compatible CI/CD Pipelines"
meta_desc: In this presentation, attendees will learn how to ensure their CI/CD pipelines are Arm compatible and capable of providing Arm support in their products.

cloud_engineering_summit:
    track: deploy

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
url_slug: "building-arm-compatible-cicd-pipelines"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Building Arm Compatible CI/CD Pipelines"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Building Arm Compatible CI/CD Pipelines"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/oVFw-QhbACw"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2021-10-20T13:10:00-07:00
    # Duration of the webinar.
    duration: "22 minutes"
    # Description of the webinar.
    description: |
        Arm architectures are increasingly popular and are becoming widely adopted by teams and organizations. As this adoption grows, developers and organizations must ensure their software and services are capable to support Arm architecture which begins by ensuring their CI/CD tooling and workload are Arm capable. In this presentation, attendees will learn how to ensure their CI/CD pipelines and workloads are Arm compatible and capable of providing Arm support in their products.

    # The webinar presenters
    presenters:
        - name: Angel Rivera
          role: Senior Developer Advocate, CircleCI

# This section contains the transcript for a video. It is optional.
transcript: |
    Hello, everyone.  I wanna welcome you to my talk today.  And in this talk, I'll be discussing how to Build Docker Images for Arm Architectures from CI/CD pipelines.  Before I get into that, I'd like to introduce myself.  My name is Angel Rivera, I'm a Developer Advocate for CircleCi.

    And in my role at CircleCi, I'm engaging the developer community and understanding how they're using technologies as well as some of the struggles or obstacles they face while implementing or using these technologies.  I bring that information back to my team at CircleCi and we use those learnings to build valuable features for our developers and our customers to ease their lives while developing software.  If any of you wanna reach out to me after this talk, you know, to discuss the talk or discuss anything in general, you can reach out to me via Twitter, my Twitter handle is @punkdata.  So again, if anyone wants to reach out and have a discussion or just to chat, yeah hit me up @punkdata on Twitter.  Here some fun facts about ARM, if you didn't know, ARM stands for Advanced RISC Machines.

    Although in 1984 when ARM was originated or created in England, it was actually initially named the Acorn RISC Machine.  In 1987, ARM became the first commercial RISC processor available.  And in 1990, the ARM Ltd.  company was formed and that's when the name changed to what it's currently known as the Advanced RISC Machines processor.  And arm has been around for quite some time in 1986, it was powering the Apple IIGS and in 1993, it was also powering the Apple Newton Device.

    So again, it's been around for quite some time, but in recent years there's been some evolution or innovations made within the ARM architecture.  If you didn't know, ARM processors power a lot of smartphones, tablets, raspberry PIs and also tons of IoT device and smart devices such as televisions, appliances and wearables.  Arm is pretty much an almost all of the things that we probably use in our mobile devices that we use on a day to day and it's been supported by pretty much all the major operating systems.  It's definitely been supported by Linux for quite some time and I know that for a fact, because I've been using Linux for many, many years and always have seen the Linux distributions for ARM.  Which is pretty cool that that operating system in that community has always kind of been there to support those ARM architectures.

    Now, ARM is pretty popular in those mobile devices and IoT devices, smart devices, because the ARM processor does a great job at processing data while using very low power.  So, compared to the x86 processors, which are a bit snappier and faster in certain regards, it's still uses way more power than an ARM processor.  So, that's why it's kind of a great fit for these mobile devices, anything battery powered.  ARM is a great fit for, because of this low power consumption and it's still pretty quick at processing data, so it's a good fit.  Now, I wanna talk about ARm and implementations of ARM I kind of gave you examples already about how it's powering smart devices, smart phones and all the kind of battery powered devices.

    So, I wanted to share some information about some of how ARM has kind of been the innovations within ARM have kind of been applied to a real world use case.  So, let's talk about IoT sensors.  What I'm gonna use in my example is a moisture sensor, which is essentially detecting how much moisture is in something.  In this case, I'm gonna use the example of a moisture sensor in a farm.  So, this is a real world use case where farmers are using moisture sensors to detect how much moisture is in the ground, so that they know how much water to apply to their crops.

    This is a great way for them to kind of be efficient with watering and also helps with their growing process.  So, if you look at the sensor that I'm showing you in this slide has a little wire connected probably to a battery and you can imagine that also has a cellular type device to connect.  To a cell tower and then send the data from that moisture sensor back over to some server, some infrastructure that can capture that data and make sense of it.  In this case, the moisture sensor probably has an ARM processor, but again, it's supposed to be a power, a battery powered device.  Great, 'cause you're sitting in the farm, you don't need to have cables everywhere.

    Also when you're picking the plants, you don't wanna get caught up in any cables.  So, this is all kind of wireless technology, but the idea is, those sensors should have a long battery life.  And the only way to do that is to conserve on things such as processing and then also chirping or sending that data back to the data center.  In recent years, the arm chips have evolved, they've become more powerful, they've become a more efficient with power.  And one of the cool applications that I'm starting to see is, when you have IoT devices sitting in a farm like this remote the farmers or the organizations that are implementing these moisture sensors are now leveraging something called an edge server.

    And an edge server kind of sits a little bit physically closer to the moisture sensor, so that it can capture the information.  So, it's no longer sending data to a cloud and consuming more battery power.  It's actually sending data to a device or some sort of system that's onsite next to or very in close proximity to the moisture sensor and it's not consuming a lot of power.  It's also able to process data directly from the sensor and kind of a near real time situation and then sends a more polished or more refined dataset back to the ultimate infrastructure.  Which is maybe some server and some cloud system somewhere, but at the end of the day, these edge services are basically like preprocessors.

    They're taking some information from the moisture sensor and then processing it, maybe doing some kind of even AI on the data and then sending data up to the final infrastructure that's capturing it.  So, these are the kinds of advancements that are being made and these edge servers are starting to be powered by ARM processors.  And the reason is number one the power consumption again, even though you have a device that that's processing stuff it could still use a benefit from using a very low power consumption and the ARM processor does that.  The other part to that is the ARM processor are getting faster, so they're able to process that information just as good as an x86 architecture.  So, yeah, be on the lookout for kind of these armed powered edge devices, which are kind of becoming the norm within IoT type architectures.

    And it's a pretty interesting time to be viewing or seeing how this is advancing and the innovations that they're making.  So, again with the IoT services or edge devices, they're gonna need IoT edge applications.  So, those devices are gonna need to run applications that whenever the data from the sensor comes in, it's gonna have to do some calculations or maybe even do some sort of machine learning type situations where it's identifying patterns of watering patterns.  And then spitting out the best times to water or any kind of application like that.  But at the end of the day, those edge server devices are gonna need IoT edge applications to run them on.

    And what I'm seeing a ton of is these devices are running some form of Kubernetes.  And that's where kind of where if you're running Kubernetes, you're definitely gonna have to be running your application inside of a Docker image.  And that's where we have to build a Docker images that support ARM architectures and I'll get into that in a few.  So, another application for ARM architectures or CPUs or processors are for ARM powered servers.  Some cloud companies now are actually offering up cloud resources or compute nodes that are ARM powered.

    That means the underlying hardware that hosts your virtual machines are using an ARM processor and also requires you to use an ARM capable Kernel.  And the reason is because ARM and x86 architectures are not compatible.  And the reason for that is, they just use different instruction sets.  So, the processes understand their directives in a different way and that's basically one of the reasons why you can't use an x86 architecture or Kernel or applications with an ARM processor.  It will not understand the application, their application is built for a specific instruction set and you can't mix and match those.

    So, that means you have to compile your code to whatever architecture you're targeting, because actually the code doesn't really care about where it's operating on, but the hardware actually cares about what kind of software is being compiled and executed on it.  So the software, if it's built for x86 and again, you're running it on an ARM hardware, the process is not gonna understand the software and what it's trying to do.  So, that also kind of leads into Docker images that in compatibility, so with ARM you need to be cognizant of when you're building Docker images that you're building to an ARM architecture and not an x86 architecture.  So, ARM compatible Docker images again, you need to be cognizant of where you're targeting and again, if you're targeting an ARM architecture, you obviously need to build for that Docker image for an ARM processor.  So, one of the ways you can easily do that is by implementing, building your Docker images within CI/CD pipelines, that streamlines the process.

    The problem is a lot of the current CI/CD providers don't have ARM building capabilities or ARM capabilities to build your software, they don't have the hosts in the runtime to build your software, but you're in luck CircleCi has actually recently released that ARM resources.  So, we now have the ability for people to leverage ARM in their CI/CD pipelines.  So, you can build your application to an x86 platform or if you choose to, you can also build it for an ARM architecture.  And the way we did that as providing what we call resource classes, which again are ARM capable underlying hardware where you're running your code.  So, with that addition of the ARM resource classes, we're able to allow developers to build their applications, compile them for ARM and they also can build Docker images that support the ARM architecture.

    And that'll give a nice clean ARM feel across the board, so you can test your applications in ARM, you can run your code on an ARM hardware or ARM processor and know that the applications with Docker images and anything you build on that platform, the ARM platforms within your CI/CD pipeline are gonna function in whatever ARM architecture you're targeting.  Which in this case could be a Kubernetes cluster.  So, in this demonstration, I'm gonna go and show you how you can implement a CI/CD pipeline within CircleCi that actually builds, tests and deploys an ARM capable Docker image to a newly created infrastructure.  So, let's get started with our demonstration.  What I have here, what I'm showing you here is the code example that I'm gonna use for my demonstration.

    Essentially, what it is, this a simple static, no JS application.  It just renders a page and this will be any code changes will trigger our CI/CD pipeline that we'll do a couple things.  So, let's take a look at the CI/CD pipeline, I'm gonna jump in to just the building the Docker image portion of this pipeline or the job which is listed right here.  As you can see, I have a job named build_arm_docker_image and essentially what I'm gonna do here is build a Docker image that is built on an ARM compute node or executor on the CircleCi platform, as well as create a new Docker image from this application.  And the changes made to the application for deploying to an elastic container service on AWS.

    And the container service will also use Pulumi to be provisioned.  So, Pulumi will create all this infrastructure and it will also deploy this Docker image to this newly created elastic container service cluster.  And by the way, the cluster will also be powered by AWS Graviton2 ARM compute nodes.  So, it's kind of an ARM end to end ARM experience with the CI/CD pipeline.  So, let's get started, I'm just gonna quickly cover the main thing that you need to leverage an ARM executor.

    And it's just these quick keys here, which are essentially the machine which tells the platform to execute or to give you an executor of machine type which is a virtual machine.  And then the resource class is actually where you define what kinds of executor you wanna use.  In this case, we wanna use ARMs, so we would put the value of arm. medium or larger whatever, capacity compute node you want, I'm just gonna use medium here.  And then finally, let's jump over to the main point though, one of the main points here is that in order for you to build a Docker image that will be ARM capable, you have to inherit from the Docker image base.

    So, Docker works with inheritance, it inherits its kind of capabilities from a previous image.  In this case, we're gonna use the arm64v8 version and with a node image.  So, this line right here is essential in your Docker file to create a ARM capable Docker image for whatever service you're gonna deploy to.  Now, let's show you how we're going to trigger a pipeline, so basically we got to change some code and I wanna add just a quick message here.  Node server running.

    And then I'm just gonna add some dots or whatever, then I'm gonna save it and then it's gonna go through my regular flow like I don't know, let's see, trigger build as a commit message just to speed things along.  And then what we're gonna do is, oh we forgot to update that.  So we're gonna say, let's call it trigger another message we'll do two pushes or two commits and we're gonna push this upstream.  So, once we have that pushed upstream, we're gonna jump over to our CircleCi dashboard, which has detected my code changes.  And it's going to run all the jobs defined in my config.

    yaml file.  Now, we'll get into the details of this after things have run and been provisioned.  So, our Docker image job has completed and the Docker has been pushed to a Docker hub.  Let's check on our Pulumi provisioning process, so Pulumi is an infrastructures code, a system that enables developers and operators to basically build there architectures and other cloud resources using code.  So, you can define all of those things using code.

    In this example, I'm using Python and what I'm creating here is an AWS elastic container service powered by AWS Graviton2 ARM compute nodes.  And then I'm also creating things like security groups, VPCs all from scratch.  So, the idea here is to build a pipeline that will test my application in the environments that I'm targeting for deployment.  In this case, it's an ECS cluster powered by ARM compute nodes.  So, our Pulumi application has deployed a provision and deployed our application to the ECS cluster that I created.

    And we can test that the application is actually functioning on that cluster live by just copy and pasting the URL that was created and then we'll just show that to you here.  The application is running in an ECS cluster, if you want to take a look at that, we can show you that the cluster was created here, it's called app-arm.  And as you can see here, it's got a pretty much a service running.  Here's some easy two instances, so it's a three-node cluster.  And what I'm gonna show you real quick is the fact that it's running on a Graviton2 ARM compute node, which is this designator here, a t4g the G at the end or at the end of this initial designator or compute node type signifies that it's a Graviton2 ARM compute node.

    So again, like this cluster is powered by ARM, the Docker images is built for ARM and the pipeline itself.  If you want to take a look at that, I'll actually does what I call a smoke test.  So as you can see, it did all of these things built a Docker image, created and deployed this Pulumi infrastructure.  It also performed a smoke test, meaning it was the application deployed.  And is it functioning the way we designed it to function? In this case, it's a simple test that's just checking for an OK 200, which is it is responding and we verify that manually, but you can imagine as a developer you're working in your flow and you don't wanna stop to check if your app is running and then you continue on.

    What you do is you build a pipeline like this and then it'll automatically go through the process smoke test and then right now I put it in a manual job it was what we call it and the reason why I put that here is for this demo.  So, I can show you like you can do things like manual jobs if you actually wanna verify that it's running.  But normally what I do is I just don't have this approve job step here, because what happens is once its smoke test pass, it'll just go ahead and destroy that cluster.  And I just click that button in order for the next step of my pipeline, which is to destroy all that awesome infrastructure we built using Pulumi.  So, that's basically it in a nutshell, if anyone wants to reach out to me, to ask questions or get further details on this demonstration, just hit me up @punkdate on Twitter.

    And I wanna thank you all for attending this talk.  I almost forgot, I'd appreciate any feedback if at all possible from you.  If you could just use the URL that's on the screen and send me some feedback, constructive criticism on how I can make this talk a little bit more informative or more exciting or just better all the way around, I'd appreciate that.  Again, thank you and have a great event.
---
