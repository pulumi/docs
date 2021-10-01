---
# Name of the webinar.
title: "App and Infrastructure Deployments in One CI/CD Pipeline"
meta_desc: "Adora Nwodo teaches the concepts of Infrastructure as code and how you're able to treat infrastructure deployment code the same way you treat your source code."

# A featured webinar will display first in the list.
featured: false

# If the video is pre-recorded or live.
pre_recorded: true

# If the video is part of the PulumiTV series. Setting this value to true will list the video in the "PulumiTV" section.
pulumi_tv: false

# The preview image will be shown on the list page.
preview_image: ""

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
url_slug: "managing-your-cloud-application-and-infrastructure-deployment-in-one-pipeline"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Managing Your Cloud Application and Infrastructure Deployments in One CI/CD Pipeline"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Managing Your Cloud Application and Infrastructure Deployments in One CI/CD Pipeline"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/CRmX3G9NKMU"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2020-10-08T10:00:00-07:00
    # Duration of the webinar.
    duration: "28 minutes"
    # Datetime of the webinar.
    datetime: ""
    # Description of the webinar.
    description: |
        In recent times, we have seen infrastructure automation play a very important role in building and shipping world class applications fast. We have seen how tools like Docker, Ansible, Puppet & Terraform can be used to automate infrastructure deployments.

        In this session, Adora Nwodo talks about the concepts of Infrastructure as code (IaC) and how you're able to treat your infrastructure deployment code the same way you treat your source code by being able to test, version and gracefully rollback your infrastructure deployment code.

    # The webinar presenters
    presenters:
        - name: Nenne Adaora (Adora) Nwodo
          role: Software Engineer, Microsoft

# This section contains the transcript for a video. It is optional.
transcript: |
    Hello, my name is Adora and you are welcome to Pulumi’s Cloud Engineering Summit. I am very excited to be giving this talk today. And in my talk, I would be taking you through how to manage your Cloud Applications and Infrastructure Deployments in One C-I-C-D Pipeline. But before I go any further or dive into the main details of today's talk, I want to quickly introduce myself. So as I have said at the beginning of the talk, my name is Adora and I am a Software Engineer at Microsoft Mixed Reality and I am Tech Content Creator at AdoraHack. I create a lot of YouTube videos for developers and I write articles as well.

    I’m the Co-founder of unStack, which is a community for developers to learn stuff hands-on. So we organize meetups where we mostly do workshops as opposed to anything else. I'm also on the advisory board for V-R-A-R-A Nigeria, which is the Nigeria chapter for the V-R-A-R Global Association and in a way I guess it's kind of makes sense because I am somebody that works in Mixed Reality and somebody that is really enthusiastic about extended reality and what we can do as people that live in this world with that technology, So before anything straight, you know, let's just go— let's just take a trip down memory lane. Seeing what's currently, you know, happening now and how I-A-C has made a lot of things easier in terms of you know, how we are able to manage our infrastructure.

    Sometimes you need to think back to where we came from to sort of appreciate where we currently are, you know, today. And just looking at what was in the past for people that were trying to do infrastructure deployments or just even somehow create infrastructure for whatever applications or services, whatever it is that they were trying to build in the past. It was a very tedious and error-prone process and I’ll explain why.  So I got Azure today and I choose to create a resource group. I choose to create an app service plan and then I go ahead and create a key vault, as well. I go ahead and create a static web app as well. I go ahead and create multiple resources that I need to bring my website to life. Right?

    And as I'm creating these resources, I'm documenting them somehow, but maybe some— somewhere in the middle of my entire devops process, I have a live site or something goes wrong and I have to quickly make some kind of configuration change to the particular environment that had the problem. But somehow I forgot to, for whatever reason document, that change or anything like that and now these states of the environments that I made that quick-fix in, and all my other environments, will be different and if I want to now create an entirely new environment, I will be creating off the knowledge that I already have of doing that was probably documented.

    That's if it was actually even documented at all and it's very difficult to maintain states across, you know, your different environments when you are trying to do deployment in steps, so you kind of— so if you have like a development environment, you have a staging environment, and you have a production environment you can't confidently say that your staging environment mirror—mirrors your production environment or vice-versa because in that moment you're not sure anymore because of individual tricks you've made here and there just to get something to work and you weren't maybe for some reason able to document or it escapes your mind or just wasn't even one of those things, right? I-A-C gives us, you know, version control.

    I-A-C allows us to deploy our things incrementally and because talking about Pulumi, it gives us a way to actually apply a setting design pattern to whatever infrastructure definition thing we want to do because with Pulumi I'm going to be using regular programming languages and then you can now decide, okay. I want to create for the different regions, I want it to be represented in this particular way. So as I'm going to be designing my cloud application, as I'm going to be designing my service, I'm going to be designing the app, I can also be thinking about ways to actually also design my infrastructure code thing, if that makes sense? Like I said, I think Pulumi is amazing because it gives us the ability to create our infrastructure with familiar programming languages and you can see this storage account over here.

    So this is Pulumi with typescript and during the course of this whole talk, I will be using typescript as a reference. But with Pulumi you can actually use a bunch of other programming languages. You can use C-Sharp. You can use Python you can use dot net and so many more amazing programming languages. So in this particular slide, we can see the typescript definition of a storage account. So I want to use Pulumi to create a storage account with— I want to use Pulumi’s typescript to create a storage account resource. And this is how I go ahead to you know, do that.

    Now that I've given an overview on what Pulumi is and what Pulumi can sort of like do for us, I tried not to go too deep into that because that's not what this talk is really focused on, but now that I’ve given a brief overview on that, I am going straight into the next part of this talk which is integrating Pulumi as part of our deployment process and there are two scenarios. So I'm going to be stating each scenario and possible implementations for those scenarios. So the first scenario is, you know separating infrastructure deployments from our source code deployment. So for whatever reason and this is not what this talk is focused on because like I said at the beginning of this talk, this talk is focused on being able to deploy our cloud applications and our infrastructure sideby-side in one C-I-C-D pipeline.

    So this is a valid scenario for integrating Pulumi as part of our deployment process and I just want to touch on it before I move on to the next thing which is the scenario that we actually care about in this context. So the first scenario is separating infrastructure deployments from our source code deployments and there are basically two ways to do that and you might want to do this thing for whatever reason at all. The first way is having multiple repos and then you could have like one repo for where all your infrastructure could would be and then you can have another repo for way or your application source code would be basically.

    The second scenario is having your source and your infrastructure code in the same repo, but having multiple pipelines for those things and depending on whatever conditions you set, the multiple pipelines will get triggered on different locations. So it could be that you only want to trigger the pipeline that does the infrastructure deployments when you actually edit code in the infrastructure directory. Every other time you want to run the pipeline that does the source deployments or you can decide, however, whatever condition that would make you want to have multiple pipelines and trigger them or more— on different locations.

    This is also a second scenario where you can, you know, separate your infrastructure deployments from your source code deployment. And in the second scenario, which is the one we are interested in in today's talk, is deploying infrastructure and source code changes simultaneously. Now in this scenario there are two ways to implement it. So the first way to implement this is by deploying your infrastructure with Pulumi Tasks. Are your source code with some custom YAML templates that you can write yourself. The second scenario would be deploying your infrastructure and your source code with custom Pulumi templates.

    So we're going to talk about using Pulumi Tasks in an Azure Pipeline and you can do— well you can do most of all these things regardless of whatever tool that you are using, right? So if you are using GitHub for example, if you are using Azure DevOps, for example, if you're using anything at all, if you're using CircleC-I. You can do all these things, you can do all these things with Pulumi as well. But for this talk, I'm basically talking about Azure because that's what I'm more familiar with. So using Pulumi Task and Azure Pipeline, Pulumi tasks would help you, you know, handle all the things that you need to do before you actually run the Pulumi command.

    So all the setting up, installing of Pulumi C-L-I, and all the things that you need. Then all you need to do basically is call— is use that Pulumi Task and specify the command you want to call along with other important things like your Pulumi access token for authentication. So we can see these two code snippets side-by-side. One is code for defining a function app resource in Pulumi using typescript and the other is using Pulumi Tasks what we would actually need to write to be able to run these Pulumi things in Azure pipelines. So as we can see, we have our function app and we've given it the name my function app. We have specified the app service planned location, our Resource Group, and things that we need in this function app resource. if we want to deploy this function app resource to some Azure subscription so that we can, you know, actually deploy an Azure function there and we can run the code and all of that.

    We will be writing some YAML. and we will be writing some Pulumi tasks. So I have two Pulumi Tasks here because I want to run two different Pulumi commands. So I've created a Pulumi Task that does a preview for me— a preview on all my resources just to be able to compare the current Pulumi state with what I want to do to decide, okay, how many things do I want to update? How many things do I want to create? How many things am I deleting? And what is actually going to get replaced? Just to identify how the state is going to be different. So I just want to be able to see what it looks like and if it's all good then go ahead and run a Pulumi Up. And Pulumi Up is actually what upgrades my Pulumi state to what I have currently specified that I want my new states to be in.

    So if I had docker stack running before and I don't feel like using docker anymore, and I want to switch to a serverless architecture, I can remove all the docker things and then switch to using a function app in that app service plan and have all those things go in for me. So Pulumi compares that state and does all of that for me, so I would do a Pulumi preview and do a Pulumi Up. However, if you look at these scripts properly, all that happens here is the infrastructure updates. It doesn't in any way actually update my source code and when I started this talk I talked about deploying our infrastructure and source code side-by-side in one C-I-C-D pipeline. So this is not what we need. However, this next thing is closer to what need, which is after running my Pulumi Preview and my Pulumi Up, I can go ahead to run a custom YAML template that goes to deploy my function to my new Pulumi resource in Azure for me.

    And as we can see here, that's what's currently happening on the last line. And as we can see here the names of the function apps are the same. So the function app name in my code is the same name in the pipeline so that when I say, okay, I'm creating these templates to go and deploy this function for me. It goes to deploy the function to this particular function’s resource. This particular function app. So this is the first scenario that I talked about initially, So this is the first scenario that I talked about initially, which is alright. This is the first implementation for our scenario that I talked about initially, which is deploying on my infra with Pulumi Tasks and deploying our source with custom YAML templates. Now, there's a second way to actually do this, which is the way that I prefer.

    The second way to do this is using custom Pulumi scripts in an Azure pipeline. So as opposed to using the Pulumi Tasks themselves, you can customize things to how, you know, you want them to be. And now let's take a look at how that works. I'm going to be talking about this in the context of a function app. But if you are doing docker and you're doing docker containers this also applies as well, but I'm going to be using— I'm going to be saying this in the context of a function app because I feel it's a lot faster to get by. So Pulumi has something called an archive function app that allows you to deploy a function archive alongside the function up Azure  resource when you are running Pulumi Up. So as opposed to just creating an Azure function app, creating that resource.

    If you use an archive function app and you specify the path to a deployment archive, to an actual function it will also deploy that function for you in one step so you don't have to do so much. So what this means that in like, unlike the previous scenario our infra and our source code gets deployed in one step, in one task at once. You don't have to actually do two things. You don't have to create a Pulumi Task and then go ahead to call a custom template that does that. All these things could be done in one step. So here I have my code for an archive function app. We can see that— it's a little bit different from what I had before with just the normal function app resource, because now I am adding something called a deployment archive.

    I want to specify the path to the actual Azure function that I want Pulumi to help me deploy to my Azure function app resource. I had— I want to have builds that function and I want to have a path to that function and I want to pass that path to Pulumi so that Pulumi can help me deploy whatever is in that path to my Azure function app. That's just basically what it is. And for me to go even further I want to show you two different files and I want to show you why these two different files are important. So we have the Pulumi configs. So depending on how many Pulumi stack you have, you would have multiple configs. So now I have a stack I call the test stack.

    And your configs are— you can use your configs to specify things that you want to be different across your different stacks across your different environments. It could be that, okay, you want your for example the location. That's one thing that we can use in this case. Let's say okay, you want your test stack to be deployed to West Europe. You want your staging to be deployed to like West U.S. 2. And then you want your production to be deployed to like a France central. In that kind of scenario it's always easy to specify those details that are stack related that are environment related in your Pulumi stack. And because of that I have chosen, because even in the pipeline I will be able to update my Pulumi stack config by running this command Pulumi config set, whatever the config name is and the config value.

    I will be able to perform this update in the pipeline and I'm trying to run away from scenarios where I have to hard code in a deployment path because what if things change and for whatever reason my function app does not build to that specific path anymore. Then I deploy something empty to my function app and I think that my function app is there when it's actually not there. So I want to be able to automate this whole process from the beginning to the end. I don't have to hard code at all. So I'm going to be paying attention to the Pulumi config, to the Pulumi stack config. I will also going to be paying attention to the command that will help us set our archive path. If we go back to the source code we can see that— that we have created an instance of the Pulumi config.

    We have access to that in the code and we can now get config values from our config. So in this case in the code, I'll be able to get the demployment’ archive config values and I can do whatever I want with it. So that means that when I set the value for my function deployment archive in the pipeline and I run Pulumi Up, and Pulumi is going through my code and doing all the things that it does to deploy infrastructure for me. What's going to happen is— because I run that command my configure updated and when Pulumi gets to my code and sees that it requires the deployment’s archive config value from my config. It goes to fetch that and because it's already there it fetches that path, puts that path in my archive function app and then when Pulumi is helping me create that archive function app it creates it, it fetches the built function from the path that I've specified for my archive and it goes ahead to deploy whatever is in that path to my function app itself.

    Sounds amazing, right? So when we run the command as we can see already the— the config get sets as we can see this. Now, let's get to Azure pipelines. So this is what the pipeline would look like. Instead of running a Pulumi Task, I go through and run this script and I've broken this script down into two different shell scripts. So I have a script to do setup, just in case I want to do the same setup somewhere else so that I follow the programming rules that say don't repeat yourself. And I've broken these scripts down into two things. and the other one that does the Pulumi C-L-I related things for me.

    And like I said initially, depending on where your Pulumi you can decide to be using Pulumi’s cloud. And if you're using Pulumi’s cloud then you have to pass on your access token to do authentication, But if you are using your own cloud, like you have your own storage accounts, and  your own storage blob, you will need to path in like your app client secret, your subscription I-D, your arm client I-D and your arm tenant I-D, because this thing today that I'm talking about, the pipeline, currently works with service principal authentication. So you need service principal identification to do what I'm saying that Pulumi can do for you in the pipeline today.

    So let's look at our script for setting up. So what we're going to be doing is downloading Pulumi, logging into Pulumi and downloading Node.js for our setup. So when it's time to run the Pulumi C-L-I scripts, then it's important to add the Pulumi— the path to the Pulumi executable to our path environment variable. it’s very important. So when we try to run the Pulumi command, it can pick it up and run. So the first thing we want to do is to switch to our Pulumi path— the path where our Pulumi project is and in this case it is the infra path. So I'm going to switch to infra, right? And then after doing that I want to install N-P-M and I want to build my Pulumi typescript project if that is necessary.

    Once I'm done doing that, I want to select my stack that I'm in. And in this case I'm using a test stack. So I go ahead and I run Pulumi stack select test, and after doing that, I can set my deployments archive config value. I go ahead and I set that config value to the archive path that I had already built, you know, because initially I talked about this. Before we get to the Pulumi path, there will be a chance that the function that we actually have we would have built it, would have tested it, would have published artifacts, would have done all of that. So we published the artifacts to a particular path. And that is the path that we want because once we specify that path to Pulumi, Pulumi goes to deploy whatever lies in that path to our function. So I'm going to do a Pulumi config sets, deployments archive, and I'm going to put that path right there and I'm pathing it into the script right? I'm pathing the path into the script so that it's dynamic and I don't have to hard code this path for any time.

    And after doing this, I also run a pulumi config get, just in case for whatever reason my path wasn't set so that it feels early on and I know just so that I don't go through that whole process of trying to run the Pulumi Up and then it doesn't deploy anything and I go to my app to my function app and I see that my function is empty and I wonder why for a few hours. I don't want to get into that debugging rabbit hole. So, um, I just want to put this out there just to be sure that it actually sets before and move on. And after I have done the important things, which is after I have set up, as I have switched my stack, and after I have set my deployments archive, I can go ahead and just run my Pulumi Up. And what’s going to happen is Pulumi’s going to create my Azure function app resource for me.

    Pulumi is going to deploy the code in the path that I specified to that Azure function app for me, And I did not have to do it in more than one step. So on that note we've seen how we can be able to use Pulumi to deploy both our infrastructure and our source code in one step. And like I said earlier on, this works beyond functions, right? I talked about the archive function app because it's a lot easier, but I've also done this with docker as well. So I know for a fact that this actually works. All you need to do is update the container registry in Pulumi. And when you run the Pulumi Up, Pulumi goes ahead to redeploy the thing for you. So in this case where we were updating our deployments archive path for functions, if you are doing some kind of docker or kubernetes related things, you will probably need to update your container registry as well. And it's the same effect.

    It goes ahead to redeploy, It checks the current states and if there's any changes at all, it redeploys the thing for you. So now you might be wondering if Pulumi is able to do this for me, what happens next time when I did not make any changes to my infrastructure, but I have updated my code? And because I have updated my code, I want to obviously deploy the update code to Pulumi. Like I said states. The new path in your archive function app is not going to be the same as the path that you had before because once you do like a C slash Archive slash Path 2 slash, at least something will be different, even if it’s just build I-D of the function.

    And because of that, Pulumi takes that up and goes ahead to redeploy that function to that function app for you every time. So because the state is different from what you did it yesterday at 4pm and now that you want to do it again today at 2pm, Pulumi says that the current states and the new proposed states are not the same because the path to the archives are not the same, right? So Pulumi goes ahead to redeploy that function on your behalf and Pulumi does that every time so you so you wouldn't— it would never be the case of because you did not update your infrastructure code, you are not going to get your updated source code.

    So far as every time you run the pipeline you build the code. If that happens, then Pulumi would always help you redeploy that build’s code to your function or to the container or whatever it is that that you need depending on how many times you do it. So on this note I, like I said earlier, we can now use Pulumi to deploy our infra and our source code in one step and that makes me really excited. Thank you so much for sticking around and watching my talk. Like I said, I'm really honored to be giving this talk, and I'm glad that I gave this talk and on that note. Thank you and bye.
aliases:
  - /resources/managing-your-cloud-application-and-infrastructure-deployment-in-one-pipeline
---
