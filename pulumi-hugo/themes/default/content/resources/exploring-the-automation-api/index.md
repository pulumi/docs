---
# Name of the video.
title: "Exploring the Automation API with Komal Ali"
meta_desc: "In this demo Komal Ali will walk you through a self service cloud platform built using Pulumi's Automation API."

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
url_slug: "exploring-the-automation-api"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Exploring the Automation API with Komal Ali"

# Content for the left hand side section of the page.
main:
    # Video title.
    title: "Exploring the Automation API with Komal Ali"
    # URL for embedding a URL for ungated videos.
    youtube_url: "https://www.youtube.com/embed/kFHb8f2fk9k"
    # Sortable date. The datetime Hugo will use to sort the videos in date order.
    sortable_date: 2021-05-07T10:00:00-07:00
    # Duration of the video.
    duration: "9 minutes"
    # Description of the video.
    description: |
        In this demo Komal Ali will walk you through a self service cloud platform built using Pulumi's Automation API. With just a few clicks Komal will provision a static website without ever having to write a line of code.

        If you want to try the "platyform" yourself, here is the link to the [Github repo](https://github.com/komalali/self-service-platyform).

        For more information read our blog [here](/blog/pulumiup-automation-api-ga/).

    # The video presenters
    presenters:
        - name: Komal Ali
          role: Software Engineering, Pulumi

# This section contains the transcript for a video. It is optional.
transcript: |
    Hi, my name is Komal Ali, and I'm a software engineer here at Pulumi. Today, I'm going to show you a few of the infinite possibilities unlocked by Automation API. Modern day platform engineering teams are often in a position where they are bridging the divide between cloud providers and their internal customers. As a result, they often end up implementing their own internal infrastructure platforms, where they set up cloud resources, following internal and security best practices while exposing a user-friendly interface so that their users can focus on what's important to them. Let's take a look at how we might implement something like this with Pulumi's Automation API . First I'll show you how a user might interact with the platform. And then we'll take a look at the code that the platform team would write to enable this experience on the left. I have my terminal and on the right a web browser. First, we'll start up our application by running our flask run command with a few variables set in practice. The code running in the terminal would be running on a backend server. Now, as the user, all I have to do is navigate to the, to the website, to access the portal. Welcome to Pulumipus' self-service infrastructure platyform, a website that lets you deploy databases, virtual machines VPCs or static websites. We'll take a closer look at static websites.

    Sweet. So we don't want to have any websites deployed. Let's go ahead and create one. We can pass in either a URL or the content that we type in ourselves. So I'm going to just type in some content and we'll click create. On the left, you'll see Pulumi start running its update. It'll create a bucket, put an object inside that bucket, attach a policy to the bucket and then put out some outputs. And we'll be back to the start. Sweet. Now let's check out our website. Awesome. Looks like that worked. Let's go ahead and create another one this time. I'm just going to pass in a URL because I already created this website. Once again on the left, you'll see Pulumi run its update. It's creating a new stack for my new website, and it's running through the same process that I just described.

    All right. We're back. So let's take a look at the new website we just made. Awesome. It deployed, but I've definitely spelled some stuff wrong. So let's go ahead and fix that up. I'll click edit. You'll notice that the HTML is already there, so all I need to do is edit what needs to change. Okay.

    I'll hit update this time. As Pulumi starts running the update, you'll notice that Pulumi sees the difference in the content and it only updates the resource that is related to the change. In this case, the bucket object. You'll notice that the other three resources remain totally unchanged. All right. So let's make sure that that worked. We'll refresh the page. Awesome. That worked. So we don't really want this test website hanging around. So let's go ahead and delete that. This time you'll notice Pulumi deleting our resources.

    And then as it updates, you'll see tests disappear from the site directory on the right. So let's make sure that those resources were actually destroyed. So we'll go ahead and refresh this page 404 not found no such bucket. Awesome. That means our resources were destroyed. There's also this view and console button that takes us directly to the Pulumi console. The console gives us access to all sorts of useful information about our stack. So for instance, you can see your outputs in this case, you'll see that the outputs are the HTML and that's the HTML that we use to edit the content. And you'll also see the website URL, which we use to create the links. You also see the configuration that the stack uses, tags associated with the stack, all of the resources that go into making the stack, as well as links to the cloud provider, and all of the activity that the stack has seen.

    So in this case, we did our first update where we created the four resources and then the second update where we only updated the one bucket object. Cool. Now I'm going to show you the code that goes into making this experience. So to create this, the platform team wrote a simple application using Python and Flask. Within the application, we've registered handlers for each of the cloud components that we can deploy. If we take a closer look at one of those resources, you'll see CRUD handlers to create, update, list, and delete each of the component resources.

    These handlers are implemented using Pulumi's Automation API. Automation API allows us to write a normal Pulumi program to describe the desired state of our infrastructure, either inline, in this case, in this function or externally. In this case, our program describes the desired state of our infrastructure, including taking in an input, which is the content that we want to deploy to our website. We can then drive the deployments of the Pulumi program from our CRUD handlers. So for example, to create the website, we create a stack using Automation API, we then set some configuration values on that stack. And then we run stack that up.

    We wrap this code in a little bit of Flask boilerplate to provide inputs from the web app and deliver error messages and outputs back to the user. A similar process applies for lists, update, and delete handlers, and just a couple of hundred lines of code, we've created a self-service cloud infrastructure platform by building on top of Pulumi and Pulumi's Automation API. So this web app is just one example of how you could use Automation API to create rich experiences on top of Pulumi. Now that your Pulumi code can be embedded within your application code, the possibilities are kind of endless. You could even create an Alexa app that you can narrate your HTML to and have it deployed to a website using Pulumi. I'm not suggesting that you do that, but now at least you have the option. As a former data scientist, I love my Jupyter notebooks. So let's take a look at how we might run Automation API within a Jupyter notebook. So I've got this notebook that I created here.

    Notebooks are great because you can write prose right alongside your code. And so all I have to do is run some cells and you can deploy your website from within your Jupyter notebook. And there are so many more things that you could do. In the Automation API examples repo, we've got examples of all sorts of stuff. We've got examples in each of our languages. I've done my demo in Python because I'm a big Python nerd, but we've got examples in each of the supported Pulumi languages. You could do a multi-stack orchestration, so doing multiple stacks that are dependent on stack outputs, like this example, here, you can chain your deployment of your infrastructure with database migrations. Like this example here, or you can build a totally custom CLI that is specific to your domain and create a rich user experience on top of Pulumi, like ploy, which is a CLI that deploys local Docker images to a Kubernetes cluster in the cloud. Hopefully this demo has gotten you excited about all of the things that you can do with Automation API, and I can't wait to see what you all come up with. Thank you.

---
