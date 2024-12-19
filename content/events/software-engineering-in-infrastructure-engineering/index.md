---
# Name of the webinar.
title: "Software Engineering in Infrastructure Engineering"
meta_desc: In this talk, you will go through how to use the software engineering process to solve this infrastructure engineering problem.

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
url_slug: "software-engineering-in-infrastructure-engineering"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Software Engineering in Infrastructure Engineering"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Software Engineering in Infrastructure Engineering"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/T0lbD5n9ID8"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2021-10-20T09:30:00-07:00
    # Duration of the webinar.
    duration: "18 minutes"
    # Description of the webinar.
    description: |
        When we think about the concept that is Software Engineering, we think about building well-designed software that solves the problems our customers face. The key takeaway here is that software engineers are problem solvers.

        In the world of infrastructure deployments, there are many problems that exist because of the software engineering problems we are trying to solve. Pretty ironic, right? We attempt to solve problems only to create more :). A major problem for a cloud service is having multiple instances of the service in multiple regions and maintaining high availability for users.

        As great as IaC (Infrastructure as Code) is, it can be a problem maintaining different configurations for different environments where each environment has multiple instances with varying configurations.

        In this talk, I will go through how I use the software engineering process in conjunction with pulumi stacks and state, to solve this infrastructure engineering problem.


    # The webinar presenters
    presenters:
        - name: Adora Nwodo
          role: Software Engineer at Microsoft

# This section contains the transcript for a video. It is optional.
transcript: |
    Hello, and you're welcome to Pulumi's Cloud Engineering Summit. My name is Adora, and I am very excited to be giving this talk to you today. The title of my talk is Software Engineering in Infrastructure Engineering, and in this talk, I'm going to be talking about how to solve any infrastructure engineering problem that exists by following the software engineering guidelines and principles. Well, before we get right into that, I will quickly introduce myself. My name is Adora and I am a software engineer, a Microsoft mixed reality, I am a content creator at AdoraHack.

    AdoraHack is a blog and YouTube channel that I have created to share about software engineering, share about tech. to share about software engineering, share about tech. I'm also the co-founder of unstack, which is a meetup where all our talks are tailored which is a meetup where all our talks are taliored more to workshops rather than regular talks, because we believe that people learn by doing. I'm also the vice president of the VRAR Association of Nigeria, which is a Nigerian chapter of the global VRARA. And I am here because I want to raise awareness for the And I am here because I want to raise awareness for the technology that is virtual reality, augmented reality, mixed reality in this part of the world.

    And you can find me on Twitter at adoranwodo once in a while just joking, sharing about tech, and sharing about other things that I find interesting. So before we jump right into this, I would want to quickly talk about the fact that this is a Cloud Engineering Summit. And I consider myself a cloud engineer. I wrote a book for beginner cloud engineers. So if you are somebody trying to get into cloud engineering, either as a beginner in tech or somebody trying to make a switch from one tech field to another, I wrote this book that I believe will help a lot of people find their footing.

    I would make a lot of cloud concepts make sense. And once you're able to understand the concepts that are talked about in this book, you will be, you will be ready to take on more complicated cloud concepts head on. This book is currently on pre-order for 20% off throughout this month of October, so feel free to get it. So now let's get right into the major of business of today. One of the major things that infrastructure as code solves for us when we are talking about, I see infrastructure as code infrastructure, automation is configuration drift.

    What this means is that normally before the inception of What this means is that normally before the inception of infrastructure as code, I would go to, if I have three environments, I would go to my development environment and I will start to provision resources on the portal manually. And as I provision, I would document all the steps and I do that for my staging, for my production environment. So initially, all these environments actually are similar, but as time passes, most times you find out that what happens is, if there is an error in production and it is an error that a quick infrastructure change can fix, somebody would go ahead- somebody on the team would go ahead to solve this problem. And that introduces another problem, which is the fact that it would go to the portal and change the- and make the infrastructure change. However, when this infrastructure change is made, the three environments: development, staging, and production are no longer similar.

    So if I want to create a second production environment following what is on my documentation, it's no longer the same. This problem is called configuration drift and IaC solves this problem, because if you have an infrastructure declaration, no matter how many environments you deployed to, you would always get the same results. And if you want to make any change to your infrastructure, most times you would make it to that infrastructure declaration, and doing that deployment would make the changes in the stated environment, and that keeps your infrastructure configurations always similar. But when we think about it now, we've solved the configuration drift problem with IaC and as we've started building more complicated solutions on the cloud, as we build larger infrastructure, as we build larger applications on the cloud, sometimes they might involve managing and deploying to multiple locations. For example, if as a small startup with small business, initially, for whatever reason, we were not so ambitious and we only had our cloud infrastructure deployed to one region, but as time passed, as the months passed, as the weeks passed, as the days passed, we noticed an increase in traffic, and this increase in traffic was affecting the load on the one server that we had, we may want to have multiple instances of this application, and that may require scaling to multiple regions and having a load balancer that helps us manage the traffic on routes to the best or the closest or the freest, to the best or the closest to the freest, depending on whatever metric we use, the most available server in that time.

    And this sounds very good on paper, especially for backend engineers, especially for networking engineers, even for devops engineers, on paper, this sounds very good. We have multiple regions, We have a load balancer, are able to route that traffic across multiple regions. However, when we're thinking about it, practically, we realize that it is actually a problem maintaining different configurations for different environments, where each environment has multiple instances with varying configurations. For example, let's say we have a development environment deployed to West Us, our staging environments deployed to East US, canary deployed to West Europe, and production deployed to West Europe, as well. And initially, because we have just one instance of this application in our different environments, of this application in our different environments, we're fine.

    But take a look at this next slide, which shows two development deployments, one in West Us and East US, staging two deployments as well, three Canary deployments and four production deployments. What this means is that now we have switched to a multi region scenario where in each environment, we have multiple regions. This solves our problem with service availability theoretically. However, this introduces a new problem. When it comes to deployments, how do we deploy in a multi region scenario? How do we fix this? How do we make this easy? We've been giving ISC frameworks like Pulumi as tools for work, but we still have to find a way to creatively solve this problem.

    And before we go into that, I would want to get some definitions out of the way. And I'll start by defining what a Pulumi stack is. A Pulumi stack is an isolated independently configurable instance of a Pulumi program. So initially when I was talking about environment developments, staging canary production for the single region scenario, one stack can be the development stack, another stack can be the staging stack. It is a single, independently configurable instance of It is a single, independently configurable instance of a Pulumi program, so that's what the stack is.

    A Pulumi state stores metadata about your infrastructure so that it can manage your cloud resources. And this metadata that is stored is called states. Usually your state is stored as JSON. So it helps, you know, what resources exist in that infrastructure, what resources depend on the resource and all of that. And it's- that's for JSON, JSON file that shows you all the And it's- that's for JSON, JSON file that shows you all the important things you need to know about the infrastructure, the metadata like it's called.

    In many cases, different stacks for a single projects would need differing values. For example, if you are working with app service, you may want to have a different C-A for your development stack. Each year that it's different for production stack. You might want to use the standard TF for development and a premium MTA for production and Pulumi only offers a configuration system for managing such differences instead of cloud coding these differences, you can store and retrieve configuration values using a combination of the CLA and the Pulumi programming model. So now that we have these three definitions out of the way, I want to give a final definition, which is software engineering.

    Like the title of this talk is Software Engineering and Infrastructure Engineering, which is we are using the software engineering process to solve an infrastructure engineering problem. And software engineering is defined as a process of analyzing user requirements and then designing, building, and testing an application, which will satisfy these requirements. As you can see in the diagram currently on this slide, we have the different stages in software engineering process. So there's the requirements stage, designing, developing, testing, and then deploying. So for the requirements stage, the question we want to ask ourself is: What do we want? But we already know that because that's the problem that we're trying to solve.

    It wants to be able to do multi-stack, multi-region deployments. And for the design stage, we know the problem that we are trying to solve. We know what the requirements are. So the question in this stage typically is: How do we do it? And for this particular problem, there are two ways. The first way is a stack templates.

    And the second way is independent stacks. My favorite, to be honest, is the stack templates because I like to follow the traditional software because I like to follow the traditional software engineering rule that says, "Don't repeat yourself." So I like to make the minimal changes where possible, and the start template allows you to have one template and creates multiple copies of that template. And individual configs can be added in the pipeline, and any environment wide change that you might have happens in one place. So if you need to make changes to every stack that you have deployed in development, instead of making changes to your development stack in westus2, and making changes to your development stack in westuk, and making changes to your development stack in Southeast Asia, you make that environment wide change in one place.

    And because all the other things happen in your pipeline, it just works, and this a code sample to sort of show what doing the stack templates entails. So typically first you'll do all your preliminary setups, you'd log into Pulumi. So I'm using PowerShell to rename the stack templates So I'm using Powershell to rename the stack templates to the current stack name to the current stack name to the current stack name because for me to continue my deployments, I need to have my current stack file in Pulumi I need to have my current stack file in Pulumi when I do a Pulumi up or a Pulumi stack select. So I am going to rename that. So I am going to rename that.

    So if I, if my stack template is called Pulumi.dev.yaml and I have two stacks in my development in two different regions. So let's see, I have a Pulumi.dev-wu2.yaml So let's see, I have a Pulumi.dev-wu2.yaml and I have a Pulumi.dev-eu2.yaml and I have a Pulumi.dev-eu2.yaml I am basically renaming Pulumi.dev.yaml to Pulumi.dev- to Pulumi.dev-wus2.yaml. to Pulumi.dev- to Pulumi.dev-wus2.yaml to Pulumi.dev- to Pulumi.dev-wus2.yaml to Pulumi.dev- to Pulumi.dev-wus2.yaml.

    And after I do this, then I can do a Pulumi stack selects and select the regional stack that I need for that environment. I'm adding a --create flag at the end so that for whatever reason, in case I am trying to select a stack that does not exist because this is a new region that I am just provisioning, then Pulumi would create that stack for me from the very beginning. And then this is me setting individual configs in this stage. So because everything is done in stages, I would deploy my westus2 dev stack in one stage, I would deploy my westus2 dev stack in one stage and I will go and deploy my eastus2 dev stack in another stage, I can verify what's my individual in another stage, I can verify what's my individual configurations for each stage or for each stack.

    Configurations for each stage or for each stack. Ah, let's say I want to set my region, which is obviously going to be different for each region in that environment because it's happening in different stages. For the eastus2 stage, I can set my region as eastus2, and for the westus2 stage, I can set my region as westus2. And this is still in context of my development environment. And then I can now move to my staging environment.

    And let's say, I have a UK west stage. I can set my region there as UK West. And I have a South African north stage. I can set my region there as South African north, and those are the only things that I have to touch. I'm touching them in the pipeline.

    Meaning if I want to make a change for something like app service, CFA configuration that is going to change across every single instance in the different regions I am deployed to and making that change only in one place in my Pulumi.dev.yaml stack template file. And because wet- because I'm using it in my pipeline, and I know how I'm using it, I don't need to worry about making any other change at all. I want to note that, to be doing this, this is like a hack, and that's what I'm sharing.

    One of the hacks that helped me get by. So I just want to point out to that, to do this, you have to be very careful so that you don't make any mistakes. So now the next way to do this is independent stacks. This means they are going to create a stack individually for each environment. In the previous step, you do that, but that happens in your pipeline with the scripts that you write.

    But in this step, you are going to create them manually. And these stacks are going to be checked into source control. In the previous method that I talked about, these stacks don't get checked into source control. The only thing that gets checked in at the templates and when the pipeline is running, the scripts recreate the stacks or switches to the stack and uses the template and sets all the other values. But in independent stacks, you are going to create each stack, and each stack file is going to be checked into version control.

    So what this means, like it's reading here already, multiple stacks are created and they're managed independently, and any environment wide change happens in every stack. So, like I said, again, going back to my app service example, if I want to change the app service tier for my development environment, and they have five development regions: WestUS2, EastUS2, UKWest, WestUS2, EastUS2, UKWest, South Africa North, and Southeast Asia, as is shown on this slide, I am going to make that environment wide to change to five different files. I'm going to make their environment wide change to five different places. So this is what happens in the design step, where you think about how do we creatively make this problem go away, how- how do we design a way to do CI/CD for multiple region in a way that works for multiple environments, as well, while maintaining all our configurations. So your design step answers the how.

    And once you've answered the how in your design step, then it's time for your development steps. So you need to write all your infrastructure deployment code or the partial scripts, everything you need to do, all your build scripts, you have to go and write all of them. And then the next thing that happens is that you go and test what you've done to be sure that it actually works. I know a lot of people skip this testing step, and I would highly recommend that you not because it's boosts confidence and it is very helpful long-term to know and it is very helpful long-term to know that the decode you are writing is code that actually works and not code that gets checked into production and breaks the entire system. And then after that, you do your checking in, you deploy your infrastructure changes to the cloud and see how you can now do multi region, multi environment deployments in your CI/CD pipeline.

    Thank you for watching this talk. I hope you have a great day, and I hope you enjoy every other talk from every other speaker.
---
