---
# Name of the webinar.
title: "Navigating Cloud-Native Culture, Complexity, and Compliance"
meta_desc: "Watch this talk and learn how Chef helps Dev, Sec and Ops teams overcome better work together via a codified approach to application delivery."

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
url_slug: "navigating-the-cloud-native-high-cs"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Navigating the Cloud-Native High Cs: Culture, Complexity, Compliance"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Navigating the Cloud-Native High Cs: Culture, Complexity, Compliance"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/xkhotnCPNKA"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2020-10-08T10:00:00-07:00
    # Duration of the webinar.
    duration: "15 minutes"
    # Datetime of the webinar.
    datetime: ""
    # Description of the webinar.
    description: |
        Cloud-native architectures fundamentally change the way applications are built and delivered and introduce a sea of new challenges that need to be overcome including:

        Culture: Defining new roles and responsibilities for Dev, Ops and Security team members. Complexity: Jumping into a new technology while trying to modernize and maintain legacy systems. Compliance: Dealing with cascading dependency updates, minimizing attack surfaces, avoiding container misconfigurations, and building a hardened pipeline that becomes the single source of truth.

        Join this talk and learn how Chef helps Dev, Sec and Ops teams overcome better work together via a codified approach to application delivery. During the demonstration you’ll see:

        How to eliminate container “bloat” and reduce complexity associated with dependency updates with application definition How to apply a shift-left approach to system hardening that applies both to the container and the host the container in running on How Chef fits into pipelines, integrates with tools like Pulumi and helps secure the pipeline.

    # The webinar presenters
    presenters:
        - name: Niamh Cahill
          role: Solutions Architect Manager, Chef
        - name: Heather Peyton
          role: Product Marketing Director, Application Delivery, Chef

# This section contains the transcript for a video. It is optional.
transcript: |
    Hello. Hello everyone. My name is Heather Peyton. I am a Product Marketing Director at Chef, responsible for the application delivery side of the house, and along with me today, I have Niamh Cahill, Niamh if you want to go ahead and introduce yourself. Yeah, thank you., Heather. Hey, my name is Niamh Cahill, I’m the Solution Architect Manager for the West Coast for Chef, I’m very happy to be here today, and I love working in dev-ops with all of our customers.

    Great, and as advertised today, we're going to be talking about some of the challenges organizations face, especially from the operational side of the house as they adopt cloud native architectures and how Chef helps them overcome those. So, you look at studies across the industry. Commonly, you see these, these top challenges highlighted. Culture. Complexity. And Compliance. And there's a great quote over here from Gartner talking about the you know, the move to cloud native is not simple. There's cultural changes, more things shift left, more things are done in the development side of the house.

    There is complexity, which mostly comes from all those legacy apps that have to be untangled and then there's compliance. And when you look at this picture, we see compliance many times as its own thing, and to be successful in cloud native, we really want to start thinking about compliance across the whole process. Niamh, did you want to throw anything in on that? Yeah, absolutely. I think really what's key here when you're trying to overcome the complexity and the learning curve, is cooperation between the teams and you really want to find a framework and a tool-set that enables that cooperation.

    So that's where solutions like Pulumi that support multi-cloud, and different kinds of technologies as well as Chef and Chef Habitat and InSpec, really enable all of these different circles to come together. And honestly, compliance shouldn't be over here on its own, right? It should be layered in across everything that you do along with security. Exactly. So moving along when we think about complexity, right, we think about something that looks like this. I like to call this the mess in the middle and that's what dev-ops is addressing, you know, all the tendency, all the dependencies, all the tools, all the things that have to be done to take an application from dev to release.

    And as we start to untangle that and move to a cloud made of architectures, we’re really trying to break application components, instructions for delivering, into smaller and smaller pieces that can be more easily managed. And so as we move from coding applications to assembling applications, more and more tasks become codified and automated. And there's a great quote from Gartner here that addresses that and this is really Chef’s approach to helping clients move from their. existing architectures into cloud native architectures. What we do is we provide a common approach for defining applications and breaking them into those smaller and smaller pieces that not only works for cloud native architected applications, but existing applications.

    So if you have applications that are critical to your business, but you're not going to rewrite for five years and you want to be more efficient, this process of application definition can help you gain a lot of those economies of scale and manageability that you see with cloud native architectures without having to rewrite them. So application definition. This is really the process of defining everything that application needs to be built, run, and managed, then packaged into a single artifact that's infrastructure independent, and can be run anywhere, and deploy it on-demand as part of a pipeline. But then we have a new challenge to consider as we mature this.

    We don't want to build black-boxes. Boxes that, you know, we don't know where the dependencies are coming from or what are the transitive dependencies, or, you know, what version is actually running, and who owns that version and updating it? What was the base O-S and security policies? And Niamh, I know this is an area you talk to clients a lot about, did you have any more insight here? Yeah, I think that you know really making it, making the process really clear about what your transitive dependencies are, where you're supposed to get your packages from, what packages are approved for use within your environment, and really a whole, you know, implementing a strategy around package management is very important.

    So at the end of the day whether you're creating and building a container, or you're just applying a regular application that might be more legacy, these questions and the the whole challenge of managing those packages, versioning, deployment, etc., remains the same. So it becomes very important as you're deploying to multiple different environments with legacy apps that might include certain layers that are more up-to-date and cloud native. It's a lot to get your arms around and what I hear a lot is really, you know, how do we approach that from a strategy perspective? How do you really incorporate a framework that enables and allows your developers to focus their time on development rather than the actual build and deploy process? Yeah, great.

    And I mean that's exactly where this kind of next generation of thinking around packaging, strategy, management, comes into play where after we define the application and we've created these atomic, small pieces and we have single artifacts. We also Implement a strategy for tracking and managing those packages, so that we can see what's in them and manage them better across the organization. And along that plane is the integration plane, right? You want also those packages to be consumable across your dev-ops tool-chain and other solutions. And by doing that then we end up with a transparent package that's easy to audit, easy to manage, and easy to update. And with that then, Niamh I’ll turn it over to you, who’s going to like take us through the demo and show more of this.

    Yeah, so basically if we take this from left to right, generally what you want to do is you want to be building an application package that is as skinny and minimal as you need it. As it can be. You don't want to be including transitive dependencies, you won't be able to run that package in numerous different environments. Potentially run that under a container format. And then once you produce your container you want to make sure that the container is functional, that it's compliant, and then that you can easily deploy it and understand that it's securely deployed and that there is no security gaps exposed. And with that, I'm going to pivot over to the demo really quickly. So if we take a look at how Chef’s and the Chef Solution Stack, along with solutions like Pulumi enable this process, Chef Habitat really brings a mature capability to the package management layer. So what we're looking at here is an application.

    It's a Tomcat application. It's a three-tier application, but we’re really looking at the front-end here, and what we're defining here within Habitat is the ability to say. okay, these are the layers that are required to build this application. So included in that would be the build dependencies of, obviously Maven and Corretto, and then in order to run this application, we need these layers, we need Tomcat, when you Corretto and we need Mongo Tools in order to connect into our MondgoDB back-end. And so as you're going through and building the package with Habitat it is only Including the run-time libraries that it needs in the resulting package.

    So even though it's using all of these transitive dependent packages in order to build your Tomcat application, it is not including those in the resulting package. What that means is you have a very small deployment application package that has everything that it requires to run that application within any environment, and within any platform, including container formats. And, you know, even though we only said hey, we're using Maven in order to build this application, you'll see that all of Maven in-turn depends on all of these other packages and you have very clear visibility into what version of those packages is being used within this particular application.

    And then if you want to go through and update specific packages, you can. What this enables you to do, is to build a very small, skinny container, and in a lot of the container build approaches, you'll see that you'll typically start to install an application on an O-S container like Alpine or you know, the base bunch of container of the day, but what we're doing with the Habitat is that Habitat application plan allows you to build an application container from scratch, which only contains these application libraries that are needed as well as a scratch O-S. It also allows you to specify an application service user.

    So, you know, from kind of a client's perspective if you did not want to run your application as root within the container, you can specify that within your application Habitat plan here. So you could change that package service user to root, and that is the user that we will use within the container itself. And bear in mind that this application build process, as well as the container build process, can be leveraged as part of a —, a pipeline. And then once that container itself is built, it's available to run within your environment. And typically, what we recommend doing is if you're deploying to something like kubernetes, you can update your kubernetes manifest or your home-charge with the specific tag version. We will automatically export with this tag, but you can control the tag formatting.

    So what does this look like when you're running the actual application within your environment? Well, what this looks like is essentially, it we pivot over to Chef automate. What Habitat does is it also gives you visibility into what the deployment and run-time status of your application is. And, you know, one of the best practices is to always have a health-check and status-check within your application, which Habitat can help you enforce. So not only now do you have a container that's running a very thin version of your application and the application libraries, but you also have operational visibility into whether or not that application was visible in its deployment. So you'll see here, I have my application package that was deployed.

    This is my stable release that 7 dot 0 dot 8. And you'll see here on the right-hand side, I deployed this to five different instances and they are all up and running correctly. If they were not deployed correctly, we would have a critical warning in here and you can easily fall back to the last known, good package version or container. If we talk about on the security and compliance side what Chef brings to the table in this layer, is really the ability to ensure that as you're deploying, that you're deploying in a compliant and a secure manner.

    And there are two aspects to this: one is essentially making sure that your containers are compliant to your security standards. So it's much more than just vulnerability scanning. It's really making sure that your run-time configurations for your containers, as well as kubernetes, are secure and properly configured. And it doesn't matter if you're running in a managed service in the cloud, or if you're running docker hosts yourself, or kubernetes environments yourself, if you scroll down here, you'll see that a lot of the settings that we can automatically check for, they align to C-I-S recommended best practices, but they're also really pragmatic. So if you think about, you know, where we defined a non-root user as part of our Habitat package and we have that ability.

    Here's where we can enforce that using InSpec. So as part of your pipeline, what you would do, is you would run an InSpec check against your build container and you would ensure that container does not have the setting to run the application as root, which is simply, you know, that's just best secure practices. There's other obvious ones, like do not store secrets in docker files, but also install verified packages only. And if we link that back to Habitat as well, is how do you ensure that a package is verified? Well, with Habitat you have your blessed packages that are part of your Habitat origin, and essentially you have visibility into which packages are used within which applications and how those map back into your images. And you have reportability there as well.

    So essentially you have visibility into all of these layers and it's reported into your compliance overview. There's, you know, do not install unnecessary packages in the container. And if you look at this, a lot of these right here are just, you know, within InSpec itself. It's um, it could be a manual check, but if you build this into part of your pipeline, essentially you make sure that you're secure and compliant across all of the different layers.

    Another item would be adding a health-check instruction to the container image. So part of what we do with habitat is we automatically have that health-check included as part of your application build. That's what gives you visibility into the applications tab here in our Chef automate layer. So we bring all of these capabilities over to the kubernetes side as well. So as you're running your kubernetes environments, we can similarly check that your pods and your name-spaces are running in a secure manner, that they are not open to the world, that you have correct traffic configuration, um, configured on your kubernetes clusters.

    So it's really very pragmatic from left to right, really end-to-end security and compliance for not only docker containers, or containers in general, but also just running application packages. And I also want to mention one last thing before we finish the demo, which is, this capability is amazing.

    You can also bring this capability to off-the-shelf and legacy applications, I want to highlight that, so, you know, as you go through your Habitat application definition, your plan definition, you can actually simply without even building the application, copy your binary into the Habitat package and leverage the same deploy and install mechanisms as well as all of the compliance and security that comes with that. For those off-the-shelf as well as legacy applications. So that's it for the demo.

    Heather back to you and we can wrap up. Thank you. Well, we hope you enjoyed our lightning session on how Chef helps navigate the high C’s. With that we hope to see you virtually during the rest of the event and please feel free to reach out to us with any additional questions. Thanks Heather. Thank you very much, bye!
---
